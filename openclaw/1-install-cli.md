# How to install `OpenClaw` on your machine (Mac)

## First command
```sh
curl -fsSL https://openclaw.ai/install.sh | bash
```

```sh
  🦞 OpenClaw Installer
  If you're lost, run doctor; if you're brave, run prod; if you're wise, run tests.

✓ Detected: macos

Install plan
OS: macos
Install method: npm
Requested version: latest

[1/3] Preparing environment
✓ Homebrew already installed
✓ Node.js v25.8.1 found
· Active Node.js: v25.8.1 (/opt/homebrew/bin/node)
· Active npm: 11.11.0 (/opt/homebrew/bin/npm)

[2/3] Installing OpenClaw
✓ Git already installed
· Installing OpenClaw v2026.3.13
✓ OpenClaw npm package installed
✓ OpenClaw installed
[3/3] Finalizing setup
· Refreshing loaded gateway service
✓ Gateway service metadata refreshed
✓ Gateway service restarted

🦞 OpenClaw installed successfully (OpenClaw 2026.3.13 (61d171a))!
Home sweet home. Don't worry, I won't rearrange the furniture.

· Config already present; running doctor
· Running doctor to migrate settings
✓ Doctor complete
· Config already present; skipping onboarding
· Starting setup

Config was last written by a newer OpenClaw (2026.3.14); current version is 2026.3.13.
Config was last written by a newer OpenClaw (2026.3.14); current version is 2026.3.13.

🦞 OpenClaw 2026.3.13 (61d171a) — I'm like tmux: confusing at first, then suddenly you can't live without me.

Config was last written by a newer OpenClaw (2026.3.14); current version is 2026.3.13.
Config was last written by a newer OpenClaw (2026.3.14); current version is 2026.3.13.
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▄▄░██░▄▄░██░▄▄▄██░▀██░██░▄▄▀██░████░▄▄▀██░███░██
██░███░██░▀▀░██░▄▄▄██░█░█░██░█████░████░▀▀░██░█░█░██
██░▀▀▀░██░█████░▀▀▀██░██▄░██░▀▀▄██░▀▀░█░██░██▄▀▄▀▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
                  🦞 OPENCLAW 🦞                    
 
┌  OpenClaw onboarding
│
◇  Security ─────────────────────────────────────────────────────────────────────────────────╮
│                                                                                            │
│  Security warning — please read.                                                           │
│                                                                                            │
│  OpenClaw is a hobby project and still in beta. Expect sharp edges.                        │
│  By default, OpenClaw is a personal agent: one trusted operator boundary.                  │
│  This bot can read files and run actions if tools are enabled.                             │
│  A bad prompt can trick it into doing unsafe things.                                       │
│                                                                                            │
│  OpenClaw is not a hostile multi-tenant boundary by default.                               │
│  If multiple users can message one tool-enabled agent, they share that delegated tool      │
│  authority.                                                                                │
│                                                                                            │
│  If you’re not comfortable with security hardening and access control, don’t run           │
│  OpenClaw.                                                                                 │
│  Ask someone experienced to help before enabling tools or exposing it to the internet.     │
│                                                                                            │
│  Recommended baseline:                                                                     │
│  - Pairing/allowlists + mention gating.                                                    │
│  - Multi-user/shared inbox: split trust boundaries (separate gateway/credentials, ideally  │
│    separate OS users/hosts).                                                               │
│  - Sandbox + least-privilege tools.                                                        │
│  - Shared inboxes: isolate DM sessions (`session.dmScope: per-channel-peer`) and keep      │
│    tool access minimal.                                                                    │
│  - Keep secrets out of the agent’s reachable filesystem.                                   │
│  - Use the strongest available model for any bot with tools or untrusted inboxes.          │
│                                                                                            │
│  Run regularly:                                                                            │
│  openclaw security audit --deep                                                            │
│  openclaw security audit --fix                                                             │
│                                                                                            │
│  Must read: https://docs.openclaw.ai/gateway/security                                      │
│                                                                                            │
├────────────────────────────────────────────────────────────────────────────────────────────╯
│
◆  I understand this is personal-by-default and shared/multi-user use requires lock-down. Continue?
│  ○ Yes / ● No
```

## Accept Risk
```sh
 I understand this is personal-by-default and shared/multi-user use requires lock-down. Continue?
│  ● Yes / ○ No
```
```sh
◇  I understand this is personal-by-default and shared/multi-user use requires lock-down. Continue?
│  Yes
Config was last written by a newer OpenClaw (2026.3.14); current version is 2026.3.13.
```

## Onboarding mode
```sh
◆  Onboarding mode
│  ● QuickStart (Configure details later via openclaw configure.)
│  ○ Manual
```

### On existing case
```sh
◇  Onboarding mode
│  QuickStart
◇  Existing config detected ────────────────╮
│                                           │
│  workspace: ~/.openclaw/workspace         │
│  model: openrouter/google/gemini-2.5-pro  │
│  gateway.mode: local                      │
│  gateway.port: 18789                      │
│  gateway.bind: loopback                   │
│                                           │
├───────────────────────────────────────────╯
◆  Config handling
│  ○ Use existing values
│  ● Update values
│  ○ Reset
```

## Pick model of AI
```sh
◆  Model/auth provider
│  ○ OpenAI
│  ● Anthropic (setup-token + API key)
│  ○ Chutes
│  ○ MiniMax
│  ○ Moonshot AI (Kimi K2.5)
│  ○ Google
│  ○ xAI (Grok)
│  ○ Mistral AI
│  ○ Volcano Engine
│  ○ BytePlus
│  ○ OpenRouter
│  ○ Kilo Gateway
│  ○ Qwen
│  ○ Z.AI
│  ○ Qianfan
│  ○ Alibaba Cloud Model Studio
│  ○ Copilot
│  ○ Vercel AI Gateway
│  ○ OpenCode
│  ○ Xiaomi
│  ○ Synthetic
│  ○ Together AI
│  ○ Hugging Face
│  ○ Venice AI
│  ○ LiteLLM
│  ○ Cloudflare AI Gateway
│  ○ Custom Provider
│  ○ Ollama
│  ○ SGLang
│  ○ vLLM
│  ○ Skip for now
└
```
```sh
◇  Model/auth provider
│  Anthropic
│
◆  Anthropic auth method
│  ○ Anthropic token (paste setup-token)
│  ● Anthropic API key
│  ○ Back
```
```sh
◇  Anthropic auth method
│  Anthropic API key
│
◆  How do you want to provide this API key?
│  ● Paste API key now (Stores the key directly in OpenClaw config)
│  ○ Use external secret provider
```
```sh
◇  How do you want to provide this API key?
│  Paste API key now
│
◆  Enter Anthropic API key
│  sk-ant-****************************************************************************oJ4TpwAA
```
```sh
◆  Default model
│  ● Keep current (anthropic/claude-sonnet-4-6)
│  ○ Enter model manually
│  ○ anthropic/claude-haiku-4-5-20251001
│  ○ anthropic/claude-haiku-4-5
│  ○ anthropic/claude-opus-4-20250514
│  ○ anthropic/claude-opus-4-0
│  ○ anthropic/claude-opus-4-1-20250805
│  ○ anthropic/claude-opus-4-1
│  ○ anthropic/claude-opus-4-5-20251101
│  ○ anthropic/claude-opus-4-5
│  ○ anthropic/claude-opus-4-6
│  ○ anthropic/claude-sonnet-4-20250514
│  ○ anthropic/claude-sonnet-4-0
│  ○ anthropic/claude-sonnet-4-5-20250929
│  ○ anthropic/claude-sonnet-4-5
│  ○ anthropic/claude-sonnet-4-6
```

## Pick channel
```sh
◆  Select channel (QuickStart)
│  ● Telegram (Bot API) (recommended · newcomer-friendly)
│  ○ WhatsApp (QR link)
│  ○ Discord (Bot API)
│  ○ IRC (Server + Nick)
│  ○ Google Chat (Chat API)
│  ○ Slack (Socket Mode)
│  ○ Signal (signal-cli)
│  ○ iMessage (imsg)
│  ○ LINE (Messaging API)
│  ○ Feishu/Lark (飞书)
│  ○ Nostr (NIP-04 DMs)
│  ○ Microsoft Teams (Bot Framework)
│  ○ Mattermost (plugin)
│  ○ Nextcloud Talk (self-hosted)
│  ○ Matrix (plugin)
│  ○ BlueBubbles (macOS app)
│  ○ Zalo (Bot API)
│  ○ Zalo (Personal Account)
│  ○ Synology Chat (Webhook)
│  ○ Tlon (Urbit)
│  ○ Skip for now
```
```sh
◇  Select channel (QuickStart)
│  Telegram (Bot API)
│
◇  Telegram bot token ───────────────────────────────────────────────────────────────────╮
│                                                                                        │
│  1) Open Telegram and chat with @BotFather                                             │
│  2) Run /newbot (or /mybots)                                                           │
│  3) Copy the token (looks like 123456:ABC...)                                          │
│  Tip: you can also set TELEGRAM_BOT_TOKEN in your env.                                 │
│  Docs: https://docs.openclaw.ai/telegram  │
│  Website: https://openclaw.ai                                                          │
│                                                                                        │
├────────────────────────────────────────────────────────────────────────────────────────╯
│
◆  How do you want to provide this Telegram bot token?
│  ● Enter Telegram bot token (Stores the credential directly in OpenClaw config)
│  ○ Use external secret provider
```
```sh
◇  How do you want to provide this Telegram bot token?
│  Enter Telegram bot token
│
◆  Enter Telegram bot token
│  87*****10:AAGu9nCBJbob**************4hr8
```

## Search Provider
```sh
◆  Search provider
│  ○ Brave Search
│  ○ Gemini (Google Search)
│  ○ Grok (xAI)
│  ○ Kimi (Moonshot)
│  ○ Perplexity Search
│  ● Skip for now (Configure later with openclaw configure --section web)
```
```sh
◇  Search provider
│  Skip for now
```

## Skill
```sh
◇  Skills status ─────────────╮
│                             │
│  Eligible: 5                │
│  Missing requirements: 47   │
│  Unsupported on this OS: 0  │
│  Blocked by allowlist: 0    │
│                             │
├─────────────────────────────╯
│
◆  Configure skills now? (recommended)
│  ● Yes / ○ No
```
```sh
◇  Configure skills now? (recommended)
│  No
```

## Hooks
```sh
◇  Hooks ──────────────────────────────────────────────────────────────────╮
│                                                                          │
│  Hooks let you automate actions when agent commands are issued.          │
│  Example: Save session context to memory when you issue /new or /reset.  │
│                                                                          │
│  Learn more: https://docs.openclaw.ai/automation/hooks                   │
│                                                                          │
├──────────────────────────────────────────────────────────────────────────╯
│
◆  Enable hooks?
│  ◻ Skip for now
│  ◼ 🚀 boot-md (Run BOOT.md on gateway startup)
│  ◻ 📎 bootstrap-extra-files
│  ◻ 📝 command-logger
│  ◻ 💾 session-memory
└
```
```sh
◇  Enable hooks?
│  🚀 boot-md
│
◇  Hooks Configured ─────────────────╮
│                                    │
│  Enabled 1 hook: boot-md           │
│                                    │
│  You can manage hooks later with:  │
│    openclaw hooks list             │
│    openclaw hooks enable <name>    │
│    openclaw hooks disable <name>   │
│                                    │
├────────────────────────────────────╯
```

## Gateway
```sh
◇  Gateway service runtime ────────────────────────────────────────────╮
│                                                                      │
│  QuickStart uses Node for the Gateway service (stable + supported).  │
│                                                                      │
├──────────────────────────────────────────────────────────────────────╯
│
◆  Gateway service already installed
│  ● Restart
│  ○ Reinstall
│  ○ Skip
└
```
```sh
◇  Gateway service runtime ────────────────────────────────────────────╮
│                                                                      │
│  QuickStart uses Node for the Gateway service (stable + supported).  │
│                                                                      │
├──────────────────────────────────────────────────────────────────────╯
│
◇  Gateway service already installed
│  Restart
│
◒  Restarting Gateway service…Restarted LaunchAgent: gui/501/ai.openclaw.gateway
◇  Gateway service restarted.
```

## Start UI
```sh
◇  Control UI ─────────────────────────────────────────────────────────────────────╮
│                                                                                  │
│  Web UI: http://127.0.0.1:18789/                                                 │
│  Web UI (with token):                                                            │
│  http://127.0.0.1:18789/#token=59eccf04737e0a83797777fe13b65ca7aa96029*******    │
│  Gateway WS: ws://127.0.0.1:18789                                                │
│  Gateway: reachable                                                              │
│  Docs: https://docs.openclaw.ai/web/control-ui                                   │
│                                                                                  │
├──────────────────────────────────────────────────────────────────────────────────╯
│
◇  Start TUI (best option!) ─────────────────────────────────╮
│                                                            │
│  This is the defining action that makes your agent you.    │
│  Please take your time.                                    │
│  The more you tell it, the better the experience will be.  │
│  We will send: "Wake up, my friend!"                       │
│                                                            │
├────────────────────────────────────────────────────────────╯
│
◇  Token ────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                            │
│  Gateway token: shared auth for the Gateway + Control UI.                                  │
│  Stored in: ~/.openclaw/openclaw.json (gateway.auth.token) or OPENCLAW_GATEWAY_TOKEN.      │
│  View token: openclaw config get gateway.auth.token                                        │
│  Generate token: openclaw doctor --generate-gateway-token                                  │
│  Web UI keeps dashboard URL tokens in memory for the current tab and strips them from the  │
│  URL after load.                                                                           │
│  Open the dashboard anytime: openclaw dashboard --no-open                                  │
│  If prompted: paste the token into Control UI settings (or use the tokenized dashboard     │
│  URL).                                                                                     │
│                                                                                            │
├────────────────────────────────────────────────────────────────────────────────────────────╯
│
◆  How do you want to hatch your bot?
│  ○ Hatch in TUI (recommended)
│  ● Open the Web UI
│  ○ Do this later
```
```sh
◇  How do you want to hatch your bot?
│  Open the Web UI
│
◇  Dashboard ready ────────────────────────────────────────────────────────────────╮
│                                                                                  │
│  Dashboard link (with token):                                                    │
│  http://127.0.0.1:18789/#token=59eccf04737e0a83797777fe13b65ca7aa96029*******    │
│  Opened in your browser. Keep that tab to control OpenClaw.                      │
│                                                                                  │
├──────────────────────────────────────────────────────────────────────────────────╯
│
◇  Workspace backup ────────────────────────────────────────╮
│                                                           │
│  Back up your agent workspace.                            │
│  Docs: https://docs.openclaw.ai/concepts/agent-workspace  │
│                                                           │
├───────────────────────────────────────────────────────────╯
│
◇  Security ──────────────────────────────────────────────────────╮
│                                                                 │
│  Running agents on your computer is risky — harden your setup:  │
│  https://docs.openclaw.ai/security                              │
│                                                                 │
├─────────────────────────────────────────────────────────────────╯
│
◇  Web search ───────────────────────────────────────╮
│                                                    │
│  Web search was skipped. You can enable it later:  │
│    openclaw configure --section web                │
│                                                    │
│  Docs: https://docs.openclaw.ai/tools/web          │
│                                                    │
├────────────────────────────────────────────────────╯
│
◇  What now ─────────────────────────────────────────────────────────────╮
│                                                                        │
│  What now: https://openclaw.ai/showcase ("What People Are Building").  │
│                                                                        │
├────────────────────────────────────────────────────────────────────────╯
│
└  Onboarding complete. Dashboard opened; keep that tab to control OpenClaw.
```
