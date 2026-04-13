# NETS Tier Overlay — Architectural Assessment (V2)

**Date:** 2026-04-11  
**Subject:** Refined Assessment of Tier Overlay Spec (Colleague 2)  
**Authority:** User Directive + `standards/system-design/v1/NETS-System-Design-v1.md`

---

## 1. Executive Summary: The "Reconciled" Model

The Tier Overlay Spec (v1.0) is a solid base but requires immediate surgical adjustments to align with the **Library Framework** and core **NETS operational standards**. 

| Status | Dimension | Action Required |
| :--- | :--- | :--- |
| ⚠️ **DEFERRED** | **Content & Homework** | Blocked by Library Framework completion. Adjustments needed post-Library. |
| 🔄 **ADJUST** | **Specialized Courses** | Requires alignment with final course catalog and path mappings. |
| ⚡ **MANDATORY** | **PISA Events** | Weekly PISA is mandatory for ALL. Basic (Free/Limited), Premium (Extended/Unlimited). |
| ❌ **REMOVE** | **Dashboards** | Irrelevant. Parent receives student data in stats format; Teacher is a separate domain. |
| ❌ **REMOVE** | **Offline Mode** | Forbidden. Platform integrity requires internet for submissions/images. No downloads. |
| 🔍 **CLARIFY** | **Session Modes** | Requires precise definition of types, triggers, and impact on learning flow. |
| ✅ **CONFIRMED** | **Pricing Model** | **Both Basic and Premium are PAID.** This is a project standard. |

---

## 2. Granular Corrections & Future Notes

### 2.1 Content & Homework (Dependency)
The current spec is "Library-unaware." 
*   **Note:** Content types, L1-L4 levels, and path-based homework sessions must be re-mapped once the **Library Framework** is fully operational.

### 2.2 PISA Events (The Participation Model)
*   **Weekly Attendance:** Mandatory for all students.
*   **Basic:** Once per week (Free/Limited sessions).
*   **Premium:** Extended session duration or unlimited weekly practice.

### 2.3 Dashboard Rationalization
*   **Status:** Removed from Tier Spec.
*   **Reasoning:** Teacher Dashboard is a standalone architectural topic. Parent access is not a separate feature but a statistical view of the existing student profile.

### 2.4 Offline Mode (The Integrity Rule)
*   **Status:** **REJECTED.**
*   **Reasoning:** Platform security and the **Notebook Capture** (image upload) mechanic necessitate active internet connectivity. No local caching or downloading of platform assets is permitted.

### 2.5 Session Modes (The Definition Gap)
*   **Status:** Needs Clarification.
*   **Requirement:** Define exactly what "Standard," "Recovery," and "Extended" modes represent. Are they time-based, content-based, or triggered by performance (IRT)? This must be documented before implementation.

### 2.6 Pricing Strategy
*   **Status:** **Project Standard.**
*   **Verdict:** Both tiers are paid. The "Free Utility" ambiguity from previous drafts is resolved. NETS is a premium national infrastructure.

---

## 3. Next Steps

1.  **Update `standards/system-design/v1/NETS-Tier-Overlay-v1.md`** to reflect these removals and mandatory rules.
2.  **Synchronize Layer 3** with the final **Library Framework** outputs.
3.  **Define Session Modes** in a standalone ADR (Architecture Decision Record).

---
*Assessed by: Gemini CLI Agent (YOLO Mode)*  
*Location: `standards/system-design/v1/TIER-OVERLAY-ASSESSMENT.md`*
