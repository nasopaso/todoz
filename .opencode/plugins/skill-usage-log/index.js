import { spawn } from "node:child_process"
import { resolve } from "node:path"

function log(projectDirectory, sessionID, toolName, toolInput) {
  return new Promise((done) => {
    const child = spawn(
      "python3",
      [resolve(projectDirectory, ".opencode/hooks/skill-usage-log.py")],
      {
        cwd: projectDirectory,
        env: { ...process.env, OPENCODE_PROJECT_DIR: projectDirectory },
        stdio: ["pipe", "ignore", "ignore"],
      },
    )
    const timeout = setTimeout(() => child.kill(), 10_000)
    const finish = () => {
      clearTimeout(timeout)
      done()
    }
    child.once("error", finish)
    child.once("close", finish)
    child.stdin.on("error", () => {})
    child.stdin.end(
      JSON.stringify({ session_id: sessionID, tool_name: toolName, tool_input: toolInput }),
    )
  })
}

export default {
  id: "todoz.skill-usage-log",
  async setup(ctx) {
    const projectDirectory = ctx.location.project.directory
    const workingDirectory = ctx.location.directory

    await ctx.tool.hook("execute.after", async (event) => {
      try {
        if (event.status !== "completed") return

        if (event.tool === "skill" && typeof event.input?.id === "string") {
          await log(projectDirectory, event.sessionID, "Skill", { skill: event.input.id })
          return
        }

        let paths = []
        if (
          (event.tool === "write" || event.tool === "edit") &&
          typeof event.input?.path === "string"
        ) {
          paths = [resolve(workingDirectory, event.input.path)]
        } else if (event.tool === "patch" && Array.isArray(event.result?.output?.applied)) {
          paths = event.result.output.applied
            .filter((item) => item.type !== "delete" && typeof item.target === "string")
            .map((item) => resolve(workingDirectory, item.target))
        }

        for (const path of new Set(paths)) {
          await log(projectDirectory, event.sessionID, "Write", { file_path: path })
        }
      } catch {
        // Logging must not affect the tool result.
      }
    })
  },
}
