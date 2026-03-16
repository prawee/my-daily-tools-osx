# How to On Board of `OpenClaw`

## 01 Install with Daemon
```sh
openclaw onboard --install-daemon
```
```sh
🦞 OpenClaw 2026.3.13 (61d171a) — You had me at 'openclaw gateway start.'

│
◇  Doctor warnings ──────────────────────────────────────────────────────────────────────────╮
│                                                                                            │
│  - channels.telegram.groupPolicy is "allowlist" but groupAllowFrom (and allowFrom) is      │
│    empty — all group messages will be silently dropped. Add sender IDs to                  │
│    channels.telegram.groupAllowFrom or channels.telegram.allowFrom, or set groupPolicy to  │
│    "open".                                                                                 │
│                                                                                            │
├────────────────────────────────────────────────────────────────────────────────────────────╯
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
│  ● Yes / ○ No
└
```

## 02 Onboard with Quick Start
```sh
◆  Onboarding mode
│  ● QuickStart (Configure details later via openclaw configure.)
│  ○ Manual
```

```sh
◇  Onboarding mode
│  QuickStart
│
◇  Existing config detected ───────────╮
│                                      │
│  workspace: ~/.openclaw/workspace    │
│  model: anthropic/claude-sonnet-4-6  │
│  gateway.mode: local                 │
│  gateway.port: 18789                 │
│  gateway.bind: loopback              │
│                                      │
├──────────────────────────────────────╯
│
◆  Config handling
│  ○ Use existing values
│  ○ Update values
│  ● Reset
```

```sh
◇  Config handling
│  Reset
│
◆  Reset scope
│  ○ Config only
│  ○ Config + creds + sessions
│  ● Full reset (config + creds + sessions + workspace)
```

## 03 Pick AI Provider
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
```

```sh
◇  Model/auth provider
│  Anthropic
│
◆  Anthropic auth method
│  ○ Anthropic token (paste setup-token)
│  ● Anthropic API key
│  ○ Back
└
```

```sh
◇  Model/auth provider
│  Anthropic
│
◇  Anthropic auth method
│  Anthropic API key
│
◆  How do you want to provide this API key?
│  ● Paste API key now (Stores the key directly in OpenClaw config)
│  ○ Use external secret provider
└
```

```sh
◇  How do you want to provide this API key?
│  Paste API key now
│
◆  Enter Anthropic API key
│  sk-ant-api03-S67SqGdGED_*********-59MAj6WH******FWdvALPtQ-******
└
```

## Pick Model of AI
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

## Pick Channel
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
◆  How do you want to provide this Telegram bot token?
│  ● Enter Telegram bot token (Stores the credential directly in OpenClaw config)
│  ○ Use external secret provider
```

```sh
  How do you want to provide this Telegram bot token?
│  Enter Telegram bot token
│
◆  Enter Telegram bot token
│  871285****:********-*********
```

## Search Provider with Skip
```sh
◆  Search provider
│  ○ Brave Search
│  ○ Gemini (Google Search)
│  ○ Grok (xAI)
│  ○ Kimi (Moonshot)
│  ○ Perplexity Search
│  ● Skip for now (Configure later with openclaw configure --section web)
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
│  ○ Yes / ● No
```

## Hooks
```sh
◆  Enable hooks?
│  ◻ Skip for now
│  ◼ 🚀 boot-md (Run BOOT.md on gateway startup)
│  ◻ 📎 bootstrap-extra-files
│  ◻ 📝 command-logger
│  ◻ 💾 session-memory
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
│  ○ Restart
│  ● Reinstall
│  ○ Skip
```

## Start TUI
```sh
  Start TUI (best option!) ─────────────────────────────────╮
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
