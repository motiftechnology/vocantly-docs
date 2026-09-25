# Vocantly Documentation Status

## ✅ Completed

### Core Documentation
- [x] Navigation structure (`docs.json`)
- [x] Homepage (`index.mdx`)
- [x] Quick Start guide (`quickstart.mdx`) - **Fixed SDK API examples**

### Guides
- [x] Architecture overview (`guides/architecture.mdx`)
- [x] Authentication guide (`guides/authentication.mdx`)
- [x] Conversations guide (`guides/conversations.mdx`)
- [x] Messages guide (`guides/messages.mdx`)
- [x] Realtime guide (`guides/realtime.mdx`)
- [x] Webhooks guide (`guides/webhooks.mdx`)
- [x] Support Routing guide (`guides/support-routing.mdx`)
- [x] Presence & Typing guide (`guides/presence-typing.mdx`) - **NEW**
- [x] Receipts guide (`guides/receipts.mdx`) - **NEW**
- [x] Bot Overview (`guides/bots/overview.mdx`)

### SDK Documentation (Complete!)
- [x] SDK Overview (`sdk/overview.mdx`) - **Fixed with correct API**
- [x] SDK Installation (`sdk/installation.mdx`) - **Fixed**
- [x] SDK Authentication (`sdk/authentication.mdx`) - **NEW**
- [x] SDK Conversations (`sdk/conversations.mdx`) - **NEW**
- [x] SDK Messaging (`sdk/messaging.mdx`) - **NEW**
- [x] SDK Presence (`sdk/presence.mdx`) - **NEW**
- [x] SDK Typing (`sdk/typing.mdx`) - **NEW**
- [x] SDK Receipts (`sdk/receipts.mdx`) - **NEW**
- [x] SDK Support (`sdk/support.mdx`) - **NEW**
- [x] SDK Examples (`sdk/examples.mdx`) - **NEW**

### WebSocket Documentation (Complete!)
- [x] WebSocket Overview (`websocket/overview.mdx`)
- [x] WebSocket Authentication (`websocket/authentication.mdx`) - **NEW**
- [x] WebSocket Message Types (`websocket/message-types.mdx`) - **NEW**
- [x] WebSocket Rooms (`websocket/rooms.mdx`) - **NEW**
- [x] WebSocket Messaging (`websocket/messaging.mdx`) - **NEW**
- [x] WebSocket Presence (`websocket/presence.mdx`) - **NEW**
- [x] WebSocket Typing (`websocket/typing.mdx`) - **NEW**
- [x] WebSocket Receipts (`websocket/receipts.mdx`) - **NEW**
- [x] WebSocket Signaling (`websocket/signaling.mdx`) - **NEW**

### API Reference
- [x] API Introduction (`api-reference/introduction.mdx`) - **Fixed**
- [x] Register (`api-reference/auth/register.mdx`)
- [x] Login (`api-reference/auth/login.mdx`)
- [x] SDK Token (`api-reference/auth/sdk-token.mdx`) — **Deprecated**; use [Issue SDK Token](/api-reference/apps/issue-token) (`POST /apps/:id/tokens`) instead
- [x] Issue SDK Token (`api-reference/apps/issue-token.mdx`) — **NEW** (JWT or API key; backend-only keys, frontend uses tokens)
- [x] Create Conversation (`api-reference/conversations/create.mdx`) — **Updated** with `external` type, `external_id`, `participants`; note for backend use [Create EXTERNAL (API Key)](/api-reference/conversations/create-external)
- [x] Create EXTERNAL (API Key) (`api-reference/conversations/create-external.mdx`) — **NEW** — `POST /conversations/external` with API keys only; for backend integration without dashboard login
- [x] List EXTERNAL (API Key) (`api-reference/conversations/list-external.mdx`) — **NEW** — `GET /conversations/external?external_user_id=...` for inbox
- [x] Get EXTERNAL messages (API Key) (`api-reference/conversations/get-external-messages.mdx`) — **NEW** — `GET /conversations/external/:id/messages?external_user_id=...` for message history

## 📋 Still To Do

### Guides (Lower Priority)
- [ ] `guides/departments.mdx` - Department management
- [ ] `guides/agents.mdx` - Agent management
- [ ] `guides/customers.mdx` - Customer management
- [ ] `guides/bots/configuration.mdx` - Bot configuration
- [ ] `guides/bots/analytics.mdx` - Bot analytics
- [ ] `guides/bots/faq.mdx` - FAQ management
- [ ] `guides/multi-tenancy.mdx` - Multi-tenant architecture
- [ ] `guides/security.mdx` - Security best practices
- [ ] `guides/scalability.mdx` - Scaling guide
- [ ] `guides/troubleshooting.mdx` - Troubleshooting

### API Reference (To Generate)
- [ ] Tenants endpoints (2 pages)
- [ ] Apps endpoints (5 pages)
- [ ] Conversations (list, get, members - 4 pages)
- [ ] Messages endpoints (2 pages)
- [ ] Receipts endpoints (2 pages)
- [ ] Departments endpoints (5 pages)
- [ ] Agents endpoints (5 pages)
- [ ] Support endpoints (3 pages)
- [ ] Customers endpoints (2 pages)
- [ ] Bots endpoints (2 pages)
- [ ] Bot Analytics endpoints (4 pages)
- [ ] FAQs endpoints (5 pages)
- [ ] Webhooks endpoints (6 pages)

## 📊 Progress Summary

| Category | Completed | Remaining | Total |
|----------|-----------|-----------|-------|
| **SDK Documentation** | 10 | 0 | 10 ✅ |
| **WebSocket Documentation** | 9 | 0 | 9 ✅ |
| **Core Guides** | 11 | 10 | 21 |
| **API Reference** | 8 | ~43 | ~51 |
| **Total** | **35** | **~56** | **~91** |

## 🎯 Key Fixes Applied

1. **SDK API Corrections**: Fixed all incorrect `client.messages.send()` references to use correct API:
   - `client.conversations.get(id).sendMessage(content)`
   - `conversation.startTyping()` / `conversation.stopTyping()`
   - `conversation.on('message', ...)` / `conversation.on('typing', ...)`

2. **Configuration Fix**: Changed `sdkToken` to `token` in SDK initialization

3. **Complete SDK & WebSocket Docs**: Created all missing SDK and WebSocket documentation pages

4. **Warning Banner**: Added clear warning about WebSocket-only messaging in API introduction and quickstart

5. **SDK / token flow (Jan 2025)**: `POST /auth/sdk-token` deprecated. Use `POST /apps/:id/tokens` (JWT or API key). App ID, public key, and secret key are **backend-only**; frontend receives only **tokens** from your backend. Create conversations support **EXTERNAL** type with `external_id` and `participants`.

6. **Backend integration (Jan 2025)**: New `POST /conversations/external` with **API keys only** (no dashboard login). Documented in [Create EXTERNAL (API Key)](/api-reference/conversations/create-external). Quick Start and guides (conversations, authentication) updated with backend flow: create conversation → issue token → return `token` + `conversation_id` to frontend.

7. **Inbox & message history (Jan 2025)**: New `GET /conversations/external?external_user_id=...` (list EXTERNAL conversations for an external user) and `GET /conversations/external/:id/messages?external_user_id=...` (paginated message history). Both use API key auth. Documented in [List EXTERNAL](/api-reference/conversations/list-external) and [Get EXTERNAL messages](/api-reference/conversations/get-external-messages). SDK is expected to add `conversations.list()` and `convo.fetchMessages()` that call these endpoints (or app backend proxies them).

## 📝 Notes

- All SDK documentation now uses correct API matching the actual codebase
- WebSocket documentation covers complete protocol reference
- Ready for API reference generation from OpenAPI spec
