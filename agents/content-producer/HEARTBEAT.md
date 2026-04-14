# HEARTBEAT — Monitoring Checklist

On each heartbeat check, verify:

- [ ] Read STATUS.md in the active output directory
- [ ] Is the last timestamp recent? (within expected production time per chapter)
- [ ] Is status advancing? (chapter count increasing)
- [ ] Any ❌ errors logged?
- [ ] If agent idle >10 min with incomplete work → flag as stalled
- [ ] If all chapters ✅ → report completion
