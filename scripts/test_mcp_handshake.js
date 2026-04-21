const { spawn } = require('child_process');
const serverPath = "C:/nvm4w/nodejs/node_modules/agent-recall-mcp/dist/index.js";
const nodePath = "C:/nvm4w/nodejs/node.exe";

console.log("Starting MCP Handshake Test...");

const child = spawn(nodePath, [serverPath], {
  stdio: ['pipe', 'pipe', 'pipe']
});

let stdout = '';
let stderr = '';

child.stdout.on('data', (data) => {
  const chunk = data.toString();
  console.log("STDOUT:", JSON.stringify(chunk));
  stdout += chunk;
});

child.stderr.on('data', (data) => {
  const chunk = data.toString();
  console.log("STDERR:", JSON.stringify(chunk));
  stderr += chunk;
});

// Send an 'initialize' request
const initRequest = {
  jsonrpc: "2.0",
  id: 1,
  method: "initialize",
  params: {
    protocolVersion: "2024-11-05",
    capabilities: {},
    clientInfo: { name: "test-client", version: "1.0.0" }
  }
};

child.stdin.write(JSON.stringify(initRequest) + '\n');

setTimeout(() => {
  console.log("\n--- Final Capture ---");
  console.log("Full STDOUT:", stdout);
  console.log("Full STDERR:", stderr);
  child.kill();
  process.exit(0);
}, 3000);
