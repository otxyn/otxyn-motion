# Tool Audit — Otxyn Motion research environment

Date: 2026-11-02 · Auditor session: OpenCode (GLM-5.3-Flash-Free) · Host: Windows 11

Purpose: verify what research infrastructure actually exists and works before
starting discovery. Every claim below was tested live unless marked otherwise.
No API keys, tokens, or secret values are reproduced in this file.

## A. Verified-working research tools (MCP servers via OpenCode)

| Tool | Status | Verified operations | Credentials | Notes for this project |
|---|---|---|---|---|
| **Tavily** (MCP, remote `mcp.tavily.com`) | ✅ Works | `tavily_search` (returned 10 results on test query), plus `tavily_extract`, `tavily_crawl`, `tavily_map`, `tavily_research` available | OAuth sign-in completed by user during setup | Primary **discovery** search engine. `tavily_extract` as content fallback. |
| **Exa** (MCP, remote `mcp.exa.ai`) | ✅ Works | `web_search_exa` (test query returned result with Title/URL/Highlights), `web_fetch_exa` | Keyless free tier | Primary **semantic/source-discovery** engine — good for "find demos like X". IPv6-only paths may 403 (documented upstream). Free-rate-limited; avoid hammering. |
| **Firecrawl** (MCP, remote `mcp.firecrawl.dev`) | ❌ Blocked (keyless) | `firecrawl_scrape` and `firecrawl_search` both return “Anonymous keyless access is unavailable for this request” on this network path | Would need API key | NOT usable this session. Substitutes: Jina Reader + Tavily extract + plain HTTP fetch. Recommendation: request Firecrawl API key for the implementation phase. |
| **Browser Use** (MCP, local `uvx browser-use --mcp`) | ✅ Connected | 16 tools: `browser_navigate`, `browser_click`, `browser_type`, `browser_get_state`, `browser_get_html`, `browser_extract_content`, `browser_screenshot`, session mgmt | Free/open source (direct-control tools need no LLM key) | Used for interactive demo exploration where Playwright’s structured snapshot is not enough. |
| **Playwright** (MCP, local `npx @playwright/mcp`) | ✅ Connected | 25 tools incl. navigation, snapshot, screenshot, console-message reading, resize, click/type | Free | Primary **visual verification** tool: load demos, capture consoles+screenshots at 1440×900 and 390×844. |
| **Context7** (MCP) | ✅ Connected | `resolve-library-id` + docs tools | Free | For authoritative GSAP/Three.js/PixiJS/Shader docs during technical analysis. |
| **DeepWiki** (MCP) | ✅ Connected | `read_wiki_structure`, `read_wiki_contents`, `ask_wiki_question` | Free (public repos) | Fast architecture overviews of candidate repos. |

## B. CLI / platform tools

| Tool | Status | Notes |
|---|---|---|
| `git` 2.52.0 | ✅ | Present. Repository here is not a git repo yet; bare folder. |
| `gh` (GitHub CLI) | ❌ Not installed | GitHub REST API via HTTP is used instead (works unauthenticated at 60 req/h per IP). Recommendation: install `gh` for heavily-coded repo investigation. |
| `node` v24.14.1, `npm` 11.12.1 | ✅ | Can run demo source locally if ever needed. |
| Python 3.11.9, `uv` 0.12.18 | ✅ | Available for validation scripts. |
| GitHub MCP server | ⏸ Disabled by explicit user decision | `api.githubcopilot.com/mcp/` is configured but `enabled: false` (OAuth registration incompatible with this OpenCode build). Do not modify config. Substitute: GitHub REST + `r.jina.ai` on GitHub HTML. |

## C. HTTP utilities (verified directly)

| Utility | Status | Evidence |
|---|---|---|
| **GitHub REST API v3 (unauthenticated)** | ✅ 200 OK | `GET api.github.com/repos/facebook/react` returned full repo metadata. 60 calls/h limit → budget carefully; prefer raw.githubusercontent.com for file contents (not rate-limit-exhausting). |
| **Jina Reader (`r.jina.ai`)** | ✅ 200 OK | Extracted `https://example.com` cleanly to Markdown. Works keyless; good for CodePen and GitHub-HTML extraction where APIs are rate-limited. |
| Plain `fetch` (Code Mode runtime) | ✅ | Available for all other page pulls. |
| Brave Search API | ❌ Not configured | Recommend adding later (needs API key approval). |
| SearXNG / Crawl4AI | ❌ Not installed | Not needed if Tavily+Exa hold up; note as optional self-hosted fallback. |
| Parallel subagents | ✅ Available (OpenCode `general`/`explore` agents) | Used as parallel per-category discovery workers; results consolidated centrally to dedupe. |

## D. Rules in effect

- No additional tool installs without approval (per mission §2).
- Secrets never enter research files or logs (none of the config above contains raw keys — env-var substitution only).
- Firecrawl replaced by Jina/Tavily extraction; re-test Firecrawl if the proxy path changes.

## E. Recommended additions (not installed — approval pending)

1. Firecrawl API key (only if heavy site crawling becomes necessary).
2. `gh` CLI (only if deep repo archaeology is required).
3. Optional: dedicated screenshot capture of demos at two mission viewports — currently Playwright MCP suffices.
