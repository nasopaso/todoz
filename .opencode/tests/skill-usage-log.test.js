import assert from "node:assert/strict"
import { copyFileSync, existsSync, mkdirSync, mkdtempSync, readFileSync, rmSync } from "node:fs"
import { tmpdir } from "node:os"
import { dirname, join } from "node:path"
import test from "node:test"
import plugin from "../plugins/skill-usage-log/index.js"

test("logs successful skills and docs writes in CSV", async (t) => {
  const project = mkdtempSync(join(tmpdir(), "todoz-skill-usage-"))
  t.after(() => rmSync(project, { recursive: true, force: true }))
  const hook = join(project, ".opencode/hooks/skill-usage-log.py")
  mkdirSync(dirname(hook), { recursive: true })
  copyFileSync(".opencode/hooks/skill-usage-log.py", hook)

  let after
  await plugin.setup({
    location: { directory: join(project, "subdir"), project: { directory: project } },
    tool: {
      hook: async (name, callback) => {
        assert.equal(name, "execute.after")
        after = callback
      },
    },
  })
  const call = (tool, input, extra = {}) =>
    after({ tool, input, sessionID: "ses_test", status: "completed", result: {}, ...extra })

  await call("skill", { id: "add-docs" })
  await call("skill", { id: "search-docs" })
  await call("write", { path: "../docs/new.md" })
  await call("edit", { path: join(project, "docs/existing.md") })
  await call("patch", {}, {
    result: {
      output: {
        applied: [
          { type: "add", target: join(project, "docs/added.md") },
          { type: "update", target: join(project, "docs/added.md") },
          { type: "delete", target: join(project, "docs/deleted.md") },
          { type: "add", target: join(project, "other.md") },
        ],
      },
    },
  })
  await call("skill", { id: "ignored" }, { status: "error" })
  await call("read", { path: "../docs/new.md" })
  await call("write", { path: "../docs/data.json" })

  const rows = readFileSync(join(project, ".opencode/skill-usage.csv"), "utf8").trim().split("\n")
  assert.equal(rows.shift(), "timestamp,session_id,type,value")
  assert.deepEqual(rows.map((row) => row.replace(/^[^,]+,/, "")), [
    "ses_test,skill,add-docs",
    "ses_test,skill,search-docs",
    "ses_test,write,docs/new.md",
    "ses_test,write,docs/existing.md",
    "ses_test,write,docs/added.md",
  ])
})

test("a missing Python hook does not fail the tool", async (t) => {
  const project = mkdtempSync(join(tmpdir(), "todoz-skill-usage-"))
  t.after(() => rmSync(project, { recursive: true, force: true }))
  let after
  await plugin.setup({
    location: { directory: project, project: { directory: project } },
    tool: { hook: async (_name, callback) => { after = callback } },
  })
  await after({ tool: "skill", input: { id: "search-docs" }, sessionID: "ses_test", status: "completed" })
  assert.equal(existsSync(join(project, ".opencode/skill-usage.csv")), false)
})
