const path = require("path");
const fs = require("fs");

// Lê o .env para expor as variáveis ao PM2
function loadEnv(envPath) {
  const env = {};
  if (!fs.existsSync(envPath)) return env;
  fs.readFileSync(envPath, "utf-8")
    .split("\n")
    .forEach((line) => {
      const trimmed = line.trim();
      if (!trimmed || trimmed.startsWith("#")) return;
      const [key, ...rest] = trimmed.split("=");
      if (key) env[key.trim()] = rest.join("=").trim();
    });
  return env;
}

const ROOT = __dirname;
const envVars = loadEnv(path.join(ROOT, ".env"));

const API_HOST = envVars.API_HOST || "127.0.0.1";
const API_PORT = envVars.API_PORT || "8040";
const FRONTEND_HOST = envVars.FRONTEND_HOST || "127.0.0.1";
const FRONTEND_PORT = envVars.FRONTEND_PORT || "8041";
const LOG_LEVEL = envVars.LOG_LEVEL || "info";

module.exports = {
  apps: [
    {
      name: "pyadvpl-backend",
      script: "/usr/bin/python3",
      args: "-m pyadvpl.engine.server",
      interpreter: "none",
      cwd: ROOT,
      env: {
        ...envVars,
        API_HOST,
        API_PORT,
        LOG_LEVEL,
      },
      error_file: path.join(ROOT, "logs/backend-error.log"),
      out_file: path.join(ROOT, "logs/backend-out.log"),
      merge_logs: true,
      autorestart: true,
      watch: false,
    },
    {
      name: "pyadvpl-frontend",
      script: "./node_modules/.bin/vite",
      args: `--host ${FRONTEND_HOST} --port ${FRONTEND_PORT}`,
      cwd: path.join(ROOT, "frontend"),
      env: {
        ...envVars,
        VITE_API_URL: envVars.VITE_API_URL || `/api`,
      },
      error_file: path.join(ROOT, "logs/frontend-error.log"),
      out_file: path.join(ROOT, "logs/frontend-out.log"),
      merge_logs: true,
      autorestart: true,
      watch: false,
    },
  ],
};
