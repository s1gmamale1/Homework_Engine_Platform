---
title: "Chigʻatoy Ulusining Tashkil Topishi — Phase 7 (Reflection)"
subject: "Oʻzbekiston Tarixi"
grade: 8
mode: Hard
family: "Ijtimoiy Fanlar"
language: uz
source_pages: "53–63"
textbook: "8-sinf_Ozbekiston_tarixi_2023"
phase: "7"
scored: false
duration: "~2 minutes"
---

# Phase 7 — Reflection

Silent analytics + yakuniy yopilish. **Baholash yoʻq** — bu fazaning maqsadi maʼlumot yigʻish va talaba uchun tinch yakun.

---

## Talaba koʻradigan ekran (student-facing)

### 1. Bugun nimani oʻrgandingiz? (Summary)

Bugun Siz **Chigʻatoy Ulusining (1225–1343) tashkil topishi va parchalanishini** oʻrgandingiz. **Chingizxonning ikkinchi oʻgʻli Chigʻatoy** Markaziy Osiyoni qabul qilib, undan keyin **Yalavochlar xonadoni** shaharlarni tikladi (1271 kumush tanga islohoti), **Kebekxon** davlatni qayta qurdi (1318–1326, tuman tizimi + kepaki), va **Alouddin Tarmashirin** islomni rasmiy dinga aylantirdi — ammo bu oʻtroq siyosat koʻchmanchi zodagonlarning isyoniga olib kelib, ulusni parchalashga sabab boʻldi.

Asosiy tushuncha: **Koʻchmanchi ↔ Oʻtroq ziddiyat** — 120 yil davomida ulus tarixidagi deyarli barcha katta voqealarni boshqargan kuch.

Zamonaviy izlari: **Qarshi** shahri ("saroy"dan), **rus "kopeyka"** (kepakidan), **Yevropa "Qora oʻlim"i** (1338 Chigʻatoy vabosidan).

---

### 2. BOST yakuni — oʻz maqsadingizni tekshirish

**Eslatma:** Phase 0-A Panel 6 da Siz shunday savolga javob berganingizni eslang:

> *"Bugun Siz Chigʻatoy Ulusi haqida aynan nimani bilmoqchi edingiz?"*

Javobingizni qayta koʻrib chiqing. Yetdingizmi?

- **Ha** — maqsadga toʻliq erishdim
- **Qisman** — koʻp narsa oʻrgandim, lekin baʼzi savollar hali ochiq
- **Hali emas** — asosiy maqsadim javob topmadi

*(Bu javob baholanmaydi — oʻqituvchi va tizim uchun maʼlumot.)*

---

### 3. Tafakkur savoli

Ushbu savollardan bittasi ekranda koʻrinadi (har safar boshqa savol rotatsiya asosida):

1. **Agar Alouddin Tarmashirin islomga oʻtmasdan, Yasoqqa sodiq qolsa edi — Chigʻatoy Ulusi uzoqroq yashay olarmidi? Nega?**
2. **Bu bobdagi qaysi shaxs bilan shaxsan uchrashishni xohlar edingiz, va qaysi savolni berar edingiz?**
3. **Chigʻatoy ulusi tarixidagi qaysi voqea Sizga eng kutilmagan tuyuldi? Nega u Sizni hayratga soldi?**

Javob berish majburiy emas — agar yozsangiz, minimum 10 belgi. Baholanmaydi; oʻqituvchi faqat umumiy mavzular statistikasini koʻradi.

---

### 4. Takrorlash jadvali (spaced repetition)

Bu mavzuni uzoq xotirada saqlash uchun Sizga quyidagi takrorlash jadvali taklif etiladi:

| Muddat | Taxmini sana | Takrorlash turi |
|---|---|---|
| 1 kun | Ertaga | Phase 0-B Flash Cards + Memory Palace |
| 3 kun | 3 kundan keyin | Boss savollarining 2-3 tasini qayta hal qilish |
| 7 kun | 7 kundan keyin | Toʻliq Memory Palace aylanishi (Phase 5) |

**Xususan diqqat qaratiladigan 3 ta tushuncha:**
1. **Koʻchmanchi ↔ Oʻtroq ziddiyati** (ramka — koʻp voqealarga kalit)
2. **Kebekxon islohotlari** (uch islohot: poytaxt, tuman, kepaki)
3. **Ibn Battuta birlamchi manbasi** (tarixchining metodi)

---

### 5. Yakuniy xabar (closing line)

**Agar umumiy natija ≥60%:**

> *[55% milliy variant]* **"Sizning tarixiy fikrlashingiz — Uchinchi Renessans poydevori. Chigʻatoy ulusini tushungan talaba — bugungi Oʻzbekistonni chuqurroq his qiladi."**
>
> *[45% global variant]* **"Sizning manbalarni tahlil qilish va ramkalarni qoʻllash qobiliyatingiz — jahon tarixchilari standartlariga mos keladi."**

**Agar umumiy natija <60%:**

> **"Hali emas! Har bir urinish miyangizni kuchaytiradi. Ertaga davom etamiz — Phase 0-A va 0-B ga qaytib, keyin Boss bilan yangidan uchrashamiz."**

*(TEFCAS framing — hech qachon "muvaffaqiyatsiz" degan soʻz ishlatilmaydi.)*

---

## Silent analytics (pipeline-only, talaba koʻrmaydi)

Jimjit yigʻiladigan maʼlumotlar — **routing decision** uchun asos.

### Layer 1 — Per-question
- `question_id`, `phase_id` (0a / 0b / 1 / 3 / 5 / 6 / 7)
- `bloom_level`, `pisa_level`, `pisa_domain` (Reading / Creative Thinking)
- `skill_tags` (Memory / Critical Thinking / Application / …)
- `correct` (boolean), `time_seconds`, `attempts`, `hints_used`, `difficulty`

### Layer 2 — Per-phase
- `phase_score_pct`, `phase_time_seconds`, `phase_completed`
- `phase_skill_breakdown` ({ Memory: X%, Critical Thinking: Y%, … })

### Layer 3 — Per-session
- `session_id`, `lesson_id` = `chigatoy_ulusining_tashkil_topishi`
- `overall_score_pct` = (Phase 1 × 10%) + (Phase 3 × 50%) + (Phase 6 × 40%)
- `passed` = `overall_score_pct ≥ 60`
- `vs_student_avg` (delta)
- `skill_deltas` (this session vs last)

### Layer 4 — Routing decision
```
IF overall_score_pct < 60:
    → identify weakest phase + failed standards
    → queue remediation: Preview (relevant panels) → Flash Cards → failed Boss Qs (easier variants)
    → mark lesson "remediation-required"
ELIF overall_score_pct ≥ 60 AND > student_subject_avg:
    → advance to next O'zbekiston Tarixi lesson
    → update student_subject_avg
ELSE:
    → advance to next lesson; flag regression signal (teacher-only)
```

---

**Phase 7 tugadi. Homework tugallandi.**

*Umumiy session vaqti: ~60 daqiqa (Preview 15 + Flash Cards 6 + Sprint 2 + Games 20 + Consolidation 3 + Boss 10 + Reflection 2 + switching ~2).*

*Graded weights: Sprint 10% + Games 50% + Boss 40% = 100%. Pass threshold: 60%.*
