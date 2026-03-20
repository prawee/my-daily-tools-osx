# How to install `NanoClaw` CLI

```sh
curl -fsSL https://nanoclaw.dev/install-docker-sandboxes.sh | bash
```
```sh
=== NanoClaw Docker Sandbox Setup ===

Workspace: /Users/prawee.won/nanoclaw-sandbox-6527
Sandbox:   nanoclaw-sandbox-6527

Cloning NanoClaw...
Cloning into '/Users/prawee.won/nanoclaw-sandbox-6527'...
remote: Enumerating objects: 2653, done.
remote: Total 2653 (delta 0), reused 0 (delta 0), pack-reused 2653 (from 1)
Receiving objects: 100% (2653/2653), 10.44 MiB | 5.33 MiB/s, done.
Resolving deltas: 100% (1167/1167), done.
Creating sandbox...
```
```sh
claude-code: Pulling from docker/sandbox-templates
170e619d8f34: Pull complete
541fbd16e24d: Pull complete
49177719614e: Pull complete
a7e11790384f: Pull complete
a010b52f1821: Pull complete
48079e0ba80a: Pull complete
329c3e5acaac: Pull complete
c3e6f59c9db5: Pull complete
c8c0b5d24643: Pull complete
79464bbcac2e: Pull complete
1d8663afb31b: Pull complete
8943be6bf82f: Pull complete
e55d8c2d3746: Download complete
7f6c5cd4eab3: Download complete
Digest: sha256:9f9647257c586df2ab9449385672934fa880907259a737471ca29ce567d27056
Status: Downloaded newer image for docker/sandbox-templates:claude-code
✓ Created sandbox nanoclaw-sandbox-6527 in VM nanoclaw-sandbox-6527
  Workspace: /Users/prawee.won/nanoclaw-sandbox-6527
  Agent: claude

To connect to this sandbox, run:
  docker sandbox run nanoclaw-sandbox-6527
Configuring network bypass...

=========================================
  Sandbox created! Launching...
=========================================

Type /setup when Claude Code starts.

Starting claude agent in sandbox 'nanoclaw-sandbox-6527'...
Workspace: /Users/prawee.won/nanoclaw-sandbox-6527
Welcome to Claude Code v2.1.80
…………………………………………………………………………………………………………………………………………………………

     *                                       █████▓▓░
                                 *         ███▓░     ░░
            ░░░░░░                        ███▓░
    ░░░   ░░░░░░░░░░                      ███▓░
   ░░░░░░░░░░░░░░░░░░░    *                ██▓░░      ▓
                                             ░▓▓███▓▓░
 *                                 ░░░░
                                 ░░░░░░░░
                               ░░░░░░░░░░░░░░░░
       █████████                                        *
      ██▄█████▄██                        *
       █████████      *
…………………█ █   █ █………………………………………………………………………………………………………………
```
```sh
Let's get started.

 Choose the text style that looks best with your terminal
 To change this later, run /theme

   1. Dark mode ✔
 ❯ 2. Light mode
   3. Dark mode (colorblind-friendly)
   4. Light mode (colorblind-friendly)
   5. Dark mode (ANSI colors only)
   6. Light mode (ANSI colors only)

 ╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
  1  function greet() {
  2 -  console.log("Hello, World!");
  2 +  console.log("Hello, Claude!");
  3  }
```
```sh
Claude Code can be used with your Claude subscription or billed based on API
 usage through your Console account.

 Select login method:

   1. Claude account with subscription · Pro, Max, Team, or Enterprise

 ❯ 2. Anthropic Console account · API usage billing

   3. 3rd-party platform · Amazon Bedrock, Microsoft Foundry, or Vertex AI
```
```sh
Browser didn't open? Use the url below to sign in (c to copy)

https://platform.claude.com/oauth/authorize?code=true&client_id=9d1c250a-e61b-44
d9-88ed-5944d1962f5e&response_type=code&redirect_uri=https%3A%2F%2Fplatform.clau
de.com%2Foauth%2Fcode%2Fcallback&scope=org%3Acreate_api_key+user%3Aprofile+user%
3Ainference+user%3Asessions%3Aclaude_code+user%3Amcp_servers+user%3Afile_upload&
code_challenge=WGVgbxHiVqvUKuYoAtwYB5gT-m9NJ2--pbkJHiTDEVg&code_challenge_method
=S256&state=WOeoSDFh5aT7mVcJM_J77-VbA0fBGH8w7arG5aLaGMc


 Paste code here if prompted > jgJXVQC3cJXhqJCCIg3XQ9OfjOr6iQIZmlZlUuzX07Suwh5u
                               **************************************aLaGMc
```
```sh
 Logged in as ******@gmail.com
 Login successful. Press Enter to continue…
```

```sh
Security notes:

 1. Claude can make mistakes
    You should always review Claude's responses, especially when
    running code.

 2. Due to prompt injection risks, only use it with code you trust
    For more details see:
    https://code.claude.com/docs/en/security

 Press Enter to continue…
```

```sh
Accessing workspace:

 /Users/prawee.won/nanoclaw-sandbox-6527

 Quick safety check: Is this a project you created or one you trust? (Like your
  own code, a well-known open source project, or work from your team). If not,
 take a moment to review what's in this folder first.

 Claude Code'll be able to read, edit, and execute files here.

 Security guide

 ❯ 1. Yes, I trust this folder
   2. No, exit

 Enter to confirm · Esc to cancel
```

```sh
▐▛███▜▌   Claude Code v2.1.80
▝▜█████▛▘  Sonnet 4.6 · API Usage Billing
  ▘▘ ▝▝    /Users/prawee.won/nanoclaw-sandbox-6527

  ↑ Opus now defaults to 1M context · 5x more room, same pricing

────────────────────────────────────────────────────────────────────────────────
❯ Try "create a util logging.py that..."
────────────────────────────────────────────────────────────────────────────────
  ⏵⏵ bypass permissions on (shift+tab to cycle)             ◐ medium · /effort
```
