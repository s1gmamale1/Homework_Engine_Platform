# HES v2.0 Operational Readiness & Scale Stress Test

**Analyst:** Raphael (Agent 61d6f6e3)
**Date:** April 2, 2026
**Task:** TMN-21 — Operational Readiness Assessment
**Source:** `HOMEWORK_STANDARDS.md` (v1.0, April 1, 2026), prior analyses by Leonardo, Donatello, Michelangelo
**Verdict:** **SIGNIFICANT GAPS — Not Deploy-Ready Without Remediation**

---

## 1. Executive Summary

HES v2.0 is a pedagogically strong specification with excellent game mechanics and a well-structured 7-step learning journey. However, it has **critical operational gaps** that would cause system failures at the scale of 8.8 million K-11 students in Uzbekistan. The document specifies *what happens during a homework session* but severely underspecifies *what happens around it* — infrastructure, sync reconciliation, integration protocols, and compliance.

**Bottom line:** The homework engine design is sound. The operational wrapper around it is not production-ready. Deploying to 8.8M students without addressing the gaps below would result in sync data loss, infrastructure collapse during peak hours, compliance violations, and teacher/parent tool failures.

| Area | Status |
|------|--------|
| Core homework engine | Ready (well-specified) |
| Infrastructure & scaling | **Not specified** — critical gap |
| Offline/sync robustness | **Partially specified** — reconciliation algorithm missing |
| Mode interaction edge cases | **Partially specified** — gaps in multi-mode transitions |
| Integration (Kundalik, SMS, etc.) | **Not specified** — critical gap |
| Data privacy & compliance | **Not specified** — critical gap |
| Teacher/parent tooling | **Specified but untested** — performance concerns |

---

## 2. Infrastructure Requirements (Peak Load Estimates)

### 2.1 Concurrency Model

| Parameter | Value | Calculation |
|-----------|-------|-------------|
| Total students | 8,800,000 | Given |
| Daily active (60%) | 5,280,000 | 8.8M × 0.60 |
| Session duration | 20–30 min | Spec §2.1 |
| Peak window | 14:00–20:00 local (6 hours) | After-school hours |
| Peak concentration factor | ~70% of daily sessions | Standard after-school curve |
| Sessions in peak window | 3,696,000 | 5.28M × 0.70 |
| Average session duration | 25 min | Midpoint of 20–30 min |
| Session slots per hour | 2.4 | 60 min / 25 min |
| Peak concurrent users | **~257,000** | 3,696,000 / (6 hrs × 2.4 slots/hr) |
| Absolute peak (15-min spike) | **~400,000–500,000** | 1.5–2× average during 16:00–17:00 rush |

**Note:** Uzbekistan has a single timezone (UTC+5), so all 8.8M students share the same peak window. There is no geographic load distribution benefit.

### 2.2 Per-Session Server Load

Each 25-minute session involves:

| Operation | Frequency per Session | Server Impact |
|-----------|----------------------|---------------|
| Content delivery (stories, media) | 3–7 segment loads | CDN + storage reads |
| AI difficulty adaptation | Every 3–5 questions (~8–15 calls) | AI inference calls |
| Real-time progress tracking | Every answer (~25–40 writes) | Database writes |
| XP/streak calculation | Every answer + session end | Compute + DB writes |
| Anti-cheat monitoring | Continuous + Final Boss | ML inference |
| Question generation (Final Boss) | 5–7 questions per boss attempt | AI generation calls |
| Theta (IRT) recalculation | After each Adaptive Quiz answer | Compute |
| Leaderboard updates | Session end | Cache + DB |

### 2.3 Aggregate Server Requirements (Estimated)

| Resource | Peak Estimate | Notes |
|----------|---------------|-------|
| **API requests/sec** | 150,000–250,000 | 400K concurrent × 0.4–0.6 req/sec per user |
| **Database writes/sec** | 60,000–100,000 | Progress tracking, XP, streaks, theta |
| **AI inference calls/sec** | 15,000–30,000 | Difficulty adaptation + question generation |
| **CDN bandwidth** | 5–15 Gbps sustained | Story Mode media (video, images, audio) |
| **WebSocket connections** | 400,000–500,000 concurrent | Real-time session state, anti-cheat |
| **Storage (question bank)** | 50–100 TB | All subjects × all grades × 3x volume × multilingual |
| **Storage (student records)** | 5–10 TB | 8.8M students × historical session data |

### 2.4 Infrastructure Assessment

**The spec does not address any of the following:**
- Server architecture (monolith vs. microservices)
- Database technology choice (relational vs. NoSQL vs. time-series)
- Caching strategy (Redis, Memcached, or equivalent)
- CDN provider and edge caching for Uzbekistan
- AI inference infrastructure (on-premise GPU clusters vs. cloud API)
- Auto-scaling policies for peak/off-peak
- Geographic redundancy and disaster recovery
- Load balancing strategy
- Rate limiting and backpressure mechanisms

**Critical concern:** Uzbekistan's internet infrastructure. According to Speedtest Global Index (2024), Uzbekistan ranks ~95th globally for fixed broadband (avg ~30 Mbps) and ~80th for mobile (avg ~25 Mbps). Rural connectivity is significantly worse. The spec assumes continuous connectivity for most features but does not account for bandwidth constraints, latency variability, or ISP reliability.

---

## 3. Critical Operational Gaps (Things That Will Break at Scale)

### 3.1 Offline/Sync Reconciliation Algorithm — UNSPECIFIED

**The Problem:**
Section 9.5 specifies a sync protocol with four steps:
1. Upload offline results
2. Server recalculates PISA level
3. "Reconcile any discrepancies"
4. Refresh cached pools

Step 3 is a hand-wave. The reconciliation algorithm is not defined, and this is where data integrity breaks down.

**Specific failure scenarios:**

| Scenario | What Happens | What the Spec Says |
|----------|-------------|-------------------|
| Offline theta diverges significantly from server theta | Student is doing well offline (θ = +1.5), but server-side data from before offline period shows θ = -0.5. Which θ is correct? | "Reconcile discrepancies" — no algorithm |
| Student completes chapters offline that were updated by content team | Student passes Final Boss for Chapter 5 offline. Content team corrected errors in Chapter 5 questions while student was offline. Is the boss completion valid? | Not addressed |
| Two devices sync conflicting data | Student starts on tablet at home, parent logs in on phone "to check." Both generate session data. Device fingerprinting flags this as cheating, but it's legitimate shared-account use. | Not addressed — anti-cheat and shared device support are in direct tension |
| Offline question pool exhaustion | Student retries Final Boss 5+ times offline. The 3x question pool is designed for ~3 attempts (5 questions × 3 = 15 questions for 5 boss questions). What happens on attempt 4+? | "3x expected volume" — but "expected" is undefined |

**Estimated impact:** With 8.8M students and offline mode designed for areas with poor connectivity, sync conflicts will affect hundreds of thousands of students daily. Without a deterministic reconciliation algorithm, data corruption is inevitable.

**Recommendation:** Define a concrete merge strategy:
- Theta reconciliation: weighted average with recency bias (e.g., 70% offline, 30% server, with confidence intervals)
- Content version conflicts: invalidate and re-test affected chapters (flag for teacher review)
- Multi-device conflicts: last-write-wins with audit trail, exempt from anti-cheat flagging for same-account
- Pool exhaustion: reshuffle existing questions with parameter variation (change numbers, not concepts)

### 3.2 Mode Interaction Edge Cases — PARTIALLY SPECIFIED

Section 9.0 defines precedence rules for 4 modes. However:

**Gap 1: Catch-Up + Low Engagement + Boost Mode triple overlap**

The spec says "at most ONE primary + secondary modes can co-exist." But the interaction between two secondary modes (Boost + Low Engagement) running simultaneously is not specified.

Example: A student returns from 6-day absence (triggers Catch-Up) AND has had <50% completion for 3 weeks (triggers Low Engagement Tier 2) AND is below class average + absolute floor (triggers Boost Mode).

- Catch-Up is primary → governs.
- But Boost says "supplements regular homework" and Low Engagement says "reduce session length."
- Catch-Up already has a 30-minute daily cap. Low Engagement wants to reduce it further. Boost wants to add supplemental practice. These three instructions conflict.

**Gap 2: Recovery Queue to Catch-Up transition timing**

The spec says Recovery Queue auto-escalates to Catch-Up if backlog exceeds 5 sessions. But:
- Recovery Queue daily total is capped at 35 minutes.
- Catch-Up daily total is capped at 30 minutes.
- During the transition session, which cap applies?
- Does the currently-in-progress recovery session complete under Recovery rules or restart under Catch-Up rules?

**Gap 3: Mode exit race conditions**

A student in Catch-Up Mode Phase 2 (Bridging) completes the gap session Final Boss with 2+ stars on the same day their Low Engagement threshold resets. Both modes want to deactivate simultaneously. The spec doesn't define whether deactivation ordering matters (it could affect analytics).

### 3.3 Device Fingerprinting vs. Shared Device Support — CONTRADICTION

Section 2.7 Anti-Cheat specifies: "Device Fingerprinting — Flag if same account on multiple devices simultaneously."

Section 9.5 specifies: "Shared device support: secure login/logout with session state preserved server-side" and "Device-agnostic: student can start on tablet, continue on phone or school computer."

**The conflict:** In Uzbekistan's educational context, shared devices are the norm, not the exception. Computer labs have 20–30 students sharing 10–15 machines. Low-income households share a single device among multiple children. The anti-cheat system will generate massive false-positive volumes.

**Estimated false positive rate:** If even 20% of the 8.8M students share devices, that's 1.76M students potentially flagged. At 1 false flag per week per shared-device student, that's **250,000 false positives per day** — making the anti-cheat system useless and overwhelming teacher review queues.

**Recommendation:** Replace device fingerprinting with session-based integrity checks:
- Sequential session validation (can't have overlapping active sessions)
- Behavioral biometrics (typing patterns, response timing) instead of device ID
- Whitelist school computer lab IPs
- Only flag simultaneous active sessions, not sequential device switches

### 3.4 Content Storage on Student Devices — UNREALISTIC

Section 9.5 specifies: "Next 7 sessions pre-cached on device."

**Estimation of cache size per student:**

| Content Type | Per Session | × 7 Sessions | Notes |
|-------------|-------------|---------------|-------|
| Story Mode video/media | 20–50 MB | 140–350 MB | AI-generated video or illustrated panels |
| Question pools (3x volume) | 2–5 MB | 14–35 MB | Questions + media assets |
| Game assets (Tile Match, etc.) | 5–10 MB | 35–70 MB | Visual assets, audio |
| Offline adaptation engine | 10–20 MB | 10–20 MB | One-time install |
| **Total per student** | | **200–475 MB** | |

**The problem:** The spec targets low-end Android tablets. Typical low-cost tablets available in Uzbekistan (2024–2026):
- Storage: 16–32 GB total, with 5–10 GB available after OS and essential apps
- RAM: 2–3 GB

At 200–475 MB for NETS cache alone, this is 2–10% of available storage. This is tight but potentially feasible for one child's account. However:
- Shared devices with 2–3 children: 400–1,425 MB total cache → 4–28% of available storage
- If Story Mode uses video (not illustrated panels): cache could reach 1–2 GB per student
- Cache refresh requires re-downloading 200–475 MB weekly, consuming significant mobile data

**Mobile data cost:** Uzbekistan average mobile data cost is ~$0.50/GB (2024). Weekly cache refresh of 200–475 MB = $0.10–0.24/week = **$4–10 per student per year** in mobile data costs for offline caching alone. For low-income families, this is a barrier.

**Recommendation:**
- Mandate illustrated panels (not video) for Story Mode to reduce cache to 50–100 MB per 7 sessions
- Implement delta-caching (only download changed content, not full refresh)
- Provide school-based WiFi sync stations for cache refresh
- Specify minimum device requirements in the deployment plan

### 3.5 SMS Cost at Scale — UNADDRESSED

Section 9.7 specifies weekly SMS summaries for parents without app access.

| Parameter | Value |
|-----------|-------|
| Students | 8,800,000 |
| Parents receiving SMS (est. 40–60% without app) | 3,520,000–5,280,000 |
| SMS per week | 3.5M–5.3M |
| SMS per year (40 school weeks) | 140M–212M |
| Cost per SMS in Uzbekistan | ~150–300 UZS ($0.012–0.024) |
| **Annual SMS cost** | **$1.68M–$5.09M** |

The spec does not mention:
- SMS provider selection (Ucell, Beeline, Uzmobile, Humans?)
- Bulk SMS pricing agreements
- SMS delivery rate in rural areas
- Fallback if SMS fails (common in rural Uzbekistan)
- Whether SMS is per-parent or per-student (families with multiple children)
- USSD-based alternatives (cheaper, works on feature phones)

### 3.6 Teacher Dashboard Performance — UNSPECIFIED

Section 9.6 specifies heat maps with per-student, per-chapter data.

**Performance concern:** A teacher with 4 classes × 30 students = 120 students, across 30+ chapters per subject, across 2–3 subjects = **7,200–10,800 data cells per teacher view**. At peak (weekday evenings when teachers review), potentially 100,000+ teachers querying simultaneously.

The spec does not address:
- Data aggregation strategy (pre-computed vs. real-time)
- Query performance requirements (max load time for dashboard)
- Whether heat map data is streamed or batch-loaded
- Mobile-responsive requirements (many Uzbek teachers use phones, not computers)

---

## 4. Compliance Risks

### 4.1 Uzbekistan Law on Personal Data (ZRU-547, 2019)

The spec cites this law in §9.7 but does not demonstrate compliance. Key requirements of ZRU-547:

| ZRU-547 Requirement | HES v2.0 Status | Risk Level |
|---------------------|------------------|------------|
| **Consent for collection** | Not specified. Who consents for minors? Parent registration flow not defined. | **High** |
| **Purpose limitation** | Partially addressed — data used for learning, but behavioral analytics (response patterns, hesitation detection, engagement tracking) may exceed educational purpose | **Medium** |
| **Data minimization** | Not addressed. The system collects extensive behavioral data (every click, timing, patterns, device info). Is all of this necessary? | **High** |
| **Storage limitation** | Not specified. How long is student data retained? After graduation? After account deletion? | **High** |
| **Cross-border data transfer** | Not specified. Where are servers hosted? If cloud-hosted outside Uzbekistan, ZRU-547 Art. 29 requires consent + adequate protection in the receiving country | **Critical** |
| **Data subject rights** | Not specified. Can parents request data deletion? Data export? Correction of inaccurate records? | **High** |
| **Data protection officer** | Not mentioned | **Medium** |

### 4.2 Child-Specific Privacy Concerns

| Concern | HES v2.0 Feature | Risk |
|---------|-------------------|------|
| **Device fingerprinting of minors** | §2.7 — fingerprints device characteristics | Collecting device identifiers from children raises privacy concerns under most frameworks |
| **Behavioral profiling** | AI adaptation tracks response patterns, hesitation, engagement levels | Constitutes profiling of minors — requires explicit parental consent and purpose limitation |
| **Performance comparison** | §9.7 — "anonymized percentile position" shown to parents | De-anonymization risk in small classes (if class has 15 students, being "in the 93rd percentile" identifies the student as #1 or #2) |
| **Peer Teaching data** | §11.11 — peer interactions are recorded and scored | Social interaction data of minors being stored and evaluated |

### 4.3 Server Location — CRITICAL GAP

The spec does not state where servers will be hosted. Options and implications:

| Hosting Location | Pros | Cons |
|------------------|------|------|
| **Uzbekistan (domestic)** | ZRU-547 compliant, low latency, data sovereignty | Limited cloud infrastructure, fewer AI GPU resources, higher cost per unit |
| **Cloud (AWS/GCP/Azure)** | Scalable, cost-efficient, AI services built-in | Cross-border transfer requires consent, latency for real-time features, dependency on international providers |
| **Hybrid** | Best of both for different workloads | Complex architecture, dual compliance requirements |

**Recommendation:** Domestic hosting for student PII and session data, with cloud burst for AI inference only (anonymized inputs, no PII sent to cloud). This satisfies ZRU-547 while accessing necessary AI compute resources.

---

## 5. Deployment Prerequisites (What Must Exist Before Launch)

### 5.1 MUST-HAVE Before Any Deployment

| # | Prerequisite | Current Status | Effort |
|---|-------------|----------------|--------|
| 1 | **Offline sync reconciliation algorithm** — deterministic merge strategy for theta, content versions, and multi-device conflicts | Missing | 2–4 weeks engineering |
| 2 | **Infrastructure architecture document** — server topology, database design, caching strategy, auto-scaling policies | Missing | 4–8 weeks architecture + procurement |
| 3 | **Data privacy impact assessment (DPIA)** under ZRU-547 — consent flows, retention policy, DPO appointment, cross-border transfer analysis | Missing | 4–6 weeks legal + technical |
| 4 | **Device minimum requirements specification** — storage, RAM, OS version, screen size for offline cache and game rendering | Missing | 1 week |
| 5 | **Kundalik/eMaktab integration specification** — API contracts, data format, auth, error handling, sync frequency | Missing (mentioned but not specified) | 4–8 weeks depending on Kundalik API availability |
| 6 | **SMS provider contract and failover strategy** — bulk pricing, rural delivery SLA, USSD fallback | Missing | 2–4 weeks procurement |
| 7 | **Load testing results** — 500K concurrent user simulation with realistic session mix | Cannot test yet (no infrastructure) | 2–4 weeks after infrastructure |
| 8 | **Anti-cheat false positive mitigation** — replace device fingerprinting with session-based integrity, whitelist school labs | Missing | 2–3 weeks engineering |
| 9 | **Content version management protocol** — what happens when content is updated while students are offline or mid-chapter | Missing | 1–2 weeks design |
| 10 | **Parental consent flow** — GDPR-style consent for minors' data processing, compliant with ZRU-547 | Missing | 2–3 weeks legal + UX |

### 5.2 SHOULD-HAVE Before Scale Deployment (8.8M)

| # | Prerequisite | Notes |
|---|-------------|-------|
| 11 | **Phased rollout plan** — start with 1 region (~500K students), validate, then expand | Standard practice for national-scale edtech |
| 12 | **Teacher training program** — dashboard usage, mode management, override policies | 400K+ teachers need onboarding |
| 13 | **Helpdesk / support structure** — who do teachers/parents contact when something breaks? | Not mentioned in spec |
| 14 | **Monitoring & alerting** — system health dashboards, anomaly detection, automated scaling triggers | Missing |
| 15 | **Disaster recovery plan** — what happens if the primary database fails during 500K concurrent sessions? | Not mentioned |
| 16 | **Bandwidth optimization** — adaptive media quality based on connection speed, progressive loading | Not mentioned |
| 17 | **Multi-language content pipeline** — content must be available in Uzbek (Latin), Uzbek (Cyrillic), and Russian simultaneously | Localization mentioned in §9.7 but not for core content |
| 18 | **Question bank population** — 8.8M students × subjects × grades × 3x question pools requires millions of calibrated questions | Production pipeline not specified |

### 5.3 Recommended Phased Rollout

| Phase | Scale | Duration | Purpose |
|-------|-------|----------|---------|
| **Alpha** | 1 school (500 students) | 2 months | Validate core homework flow, collect UX feedback |
| **Beta** | 1 district (~50K students) | 3 months | Validate offline sync, teacher tools, mode interactions |
| **Pilot** | 1 region (~500K students) | 4 months | Validate infrastructure at sub-national scale, SMS delivery, Kundalik integration |
| **National** | 8.8M students | Rolling over 6 months | Region-by-region deployment with monitoring |

---

## 6. Summary of Findings

### What Works Well
- The 7-step learning journey is well-designed and pedagogically grounded
- 14 game mechanics are fully specified with clear standards
- Mode precedence rules (§9.0) are a strong foundation
- Flow state algorithm (§7.1) is simple and implementable
- Cultural integration (Uzbek names, locations, narratives) is consistently applied

### What Will Break at Scale
1. **Offline sync** will corrupt data without a reconciliation algorithm
2. **Device fingerprinting** will generate 250K+ false positives/day on shared devices
3. **Peak concurrent load** (~400–500K users) requires infrastructure that doesn't exist yet
4. **SMS costs** of $1.7–5.1M/year are unbudgeted
5. **7-session pre-cache** may exceed device storage and mobile data budgets
6. **Teacher dashboards** will time out under load without pre-computed aggregation
7. **Kundalik/eMaktab integration** has no specification — teachers can't use the system without it
8. **Data privacy** — deploying without a DPIA is a legal risk under ZRU-547

### Overall Verdict

**SIGNIFICANT GAPS — Not Deploy-Ready Without Remediation**

The HES v2.0 specification is an excellent pedagogical design document. It is not yet an operational deployment specification. The gap between these two is where production systems fail. Closing the 10 must-have prerequisites (Section 5.1) is estimated at **3–6 months of engineering, legal, and procurement work** before even a limited pilot is safe.

The core engine is ready for Alpha testing with 500 students at a single school. National deployment to 8.8M students requires substantial additional work on infrastructure, data governance, and integration layers.
