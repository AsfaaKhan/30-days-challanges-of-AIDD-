🎯 Task Objective
Students will connect GitHub MCP Server with the Google Gemini CLI using the Hosted
(Remote) MCP Server.

This method does not require Docker or MCP installation - it's the simplest method.
After completing this task, AI will be able to read repositories and interact with GitHub.


📌 Steps to Complete Task 6 (Easy Method)


🔹 Step 1 - Create Your GitHub Personal Access Token (PAT)
Open this link:
https://github.com/settings/personal-access-tokens/new
Generate a token with:
✔ repo (Read & Write)

[SCREENSHOT: ](https://github.com/AsfaaKhan/30-days-challanges-of-AIDD-/blob/main/task-6/screenshots/github_mcp_connected.png)


🔹 Step 2 - Store Your Token Securely


[SCREENSHOT: ](https://github.com/AsfaaKhan/30-days-challanges-of-AIDD-/blob/main/task-6/screenshots/github_mcp_token.jpeg)


🔹 Step 3 - Configure Gemini to Use GitHub MCP Server


[SCREENSHOT: ](https://github.com/AsfaaKhan/30-days-challanges-of-AIDD-/blob/main/task-6/screenshots/setting.json.png)



🔹 Step 4 - Restart Gemini CLI

[SCREENSHOT: ](https://github.com/AsfaaKhan/30-days-challanges-of-AIDD-/blob/main/task-6/screenshots/gemini_start.png)


🔹 Step 5 - Verify Connection
Run:

Expected:
🟢 github — Ready (90+ tools)

[SCREENSHOT: ](https://github.com/AsfaaKhan/30-days-challanges-of-AIDD-/blob/main/task-6/screenshots/mcp_list.png)


🔹 Step 6 - Test the Server
Ask:
“List my GitHub repositories”

[SCREENSHOT: ](https://github.com/AsfaaKhan/30-days-challanges-of-AIDD-/blob/main/task-6/screenshots/repo_list.png)

