---
name: gamification-economy
status: v0.1 draft — validated against §22 only
layer: 0 (core primitive)
source: UNIFIED-Buzan §11 (lines 2911-2978)
---

# Gamification Economy

## Content

### 11.1 XP Award Matrix

*Source: HOMEWORK_STANDARDS.md Section 6.1 XP values (scaled appropriately for the gamification economy).*

| Action | Base XP | Notes |
|---|---|---|
| Memory Sprint (per correct) | 100 | +10 streak bonus per consecutive correct |
| Story Mode completion | 150 | Per session |
| Tile Match (perfect) | 300 | Partial: 100-250 |
| Why Chain (per level) | 150 | Grades 1-4: 100, Grades 9-11: 200 |
| Sentence Fill (per correct) | 100 | First-attempt bonus: +25 |
| Mystery Box (per box) | 250 max | 50 type ID + 150 solution + 50 bonus |
| Real-Life Challenge | 400 | Grades 1-4: 300, Grades 9-11: 500 |
| Memory Palace (all correct) | 300 | 50 per concept recalled |
| Final Boss (3 stars) | 1000 | 2 stars: 700, 1 star: 500 |
| Reflection Journal | 100 | Completion only |
| Peer Teaching | 400 | Completeness + Clarity + Accuracy |
| Creative Lab | 500 max | Diversity + Originality + Feasibility + Communication |

---

### 11.2 Streak Multipliers

| Streak Length | XP Multiplier | Visual Indicator |
|---|---|---|
| Daily (1 day) | +20% | 1 flame |
| 7 days | +50% | 7 flames |
| 14 days | +75% | Special frame |
| 30+ days | +100% | Special frame + title |

---

### 11.3 Mastery Stars

See Phase 6 (UNIFIED-Buzan §5.6) for star criteria. Stars are awarded per session (0-3) based on Final Boss performance.

---

### 11.4 Badge System

| Badge | Requirement | Display |
|---|---|---|
| Mentor | Help 10 peers via Peer Teaching | Profile + avatar frame |
| Streak Master | 30-day streak | Profile + loading screen |
| PISA Champion | Reach PISA Level 3+ in any subject | Profile + special title |
| Boss Slayer | Defeat 50 bosses | Profile + avatar accessory |
| Speed Learner | Complete chapter in <10 min | Profile |
| Rising Star | Most improved (weekly) | Weekly rotating badge |
| Bazaar Helper | Complete 10 Real-Life Challenges | Profile |
| Creative Mind | Complete 5 Creative Lab challenges | Profile |

---

### 11.5 Leaderboard Specification

*Source: Gap analysis (Donatello) identified missing spec. Rules from source docx.*

- **Scope:** Class-level ONLY (no school-wide to prevent unhealthy competition)
- **Reset:** Weekly (every Monday)
- **Categories:** XP, Streak, Chapters Mastered, Most Improved
- **Top 3:** Recognition with rotating spotlight
- **Anti-competition:** No public shaming. Celebrate improvement, not just ranking. Parents can opt-in.
- **Student always sees:** Own position and progress, regardless of leaderboard opt-in

---

### 11.6 Avatar Customization

- Cultural-themed cosmetic items (Uzbek traditional clothing, Silk Road outfits, Registan-themed items)
- Unlocked via achievements, NEVER purchases
- Non-competitive (no "rare" items that create social pressure)
- Display in: leaderboards, reflection journal, peer teaching, profile

**Principle 3 compliance:** All gamification rewards celebrate learning progress. Zero pay-to-win. Zero real-money purchases.

---

## Scope

This economy applies across all grade bands (G1-G11) and all subjects. It governs every reward, multiplier, badge, and social feature in the platform.

- §11.1 XP Matrix: every phase that awards XP must use exactly these values; no custom XP values may be introduced by subject frameworks or tier overlays.
- §11.2 Streak Multipliers: applied on top of base XP; the four tiers (1 day, 7, 14, 30+) are fixed.
- §11.3 Stars: 0-3 per session; criteria defined in §5.6 of UNIFIED-Buzan, not here.
- §11.4 Badges: 8 defined badges; unlock conditions are non-negotiable.
- §11.5 Leaderboard: class-scope only; school-wide leaderboards are prohibited.
- §11.6 Avatar: cosmetic only, zero pay-to-win, unlocked by achievement not purchase.

## Cross-references

- `core-principles.md §1.2 Principle 3` — Intrinsic Motivation constraint is the foundational rule this entire section must satisfy. Any change to §11 must be re-evaluated against Principle 3.
- `NETS-Homework-Engine-UNIFIED-Buzan.md §5.6` — Final Boss star criteria (referenced in §11.3).
- `NETS-Tier-Overlay-Spec.md` — Basic/Premium tier split; Premium enrichment must not introduce pay-to-win mechanics or alter base XP values.
- Grading System was deleted (not approved for production). XP economy is the sole student-facing progress system.
- All subject frameworks (standards/library/subject-family/) — inherit these XP values verbatim; subject frameworks may not define custom XP amounts.

## Verification

- [ ] No XP value in any session output deviates from the §11.1 matrix.
- [ ] Streak multipliers are applied in the correct four tiers only.
- [ ] Badge unlock conditions match §11.4 exactly (no additional badges, no altered requirements).
- [ ] Leaderboard scope is class-level only — no school-wide rankings exist anywhere in the platform.
- [ ] All avatar items are unlockable via achievement; zero items require purchase.
- [ ] No "rare" cosmetic rarity tiers that create social pressure exist in the avatar system.
- [ ] Final Boss XP: 3 stars = 1000, 2 stars = 700, 1 star = 500 — no other values permitted.
