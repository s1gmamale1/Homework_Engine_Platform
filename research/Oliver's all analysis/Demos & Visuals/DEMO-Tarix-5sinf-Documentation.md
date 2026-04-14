# NETS Demo — Tarix 5-sinf: "Tarix fani nimani o'rganadi?"

**Versiya:** 1.0 — 2026-yil, 2-aprel
**Fan:** Tarix (Tarixdan hikoyalar)
**Sinf:** 5-sinf
**Mavzu:** 1-§. Tarix fani nimani o'rganadi?
**Darslik:** "Tarixdan hikoyalar", 5-sinf, 3-nashr, 2020. Mualliflar: U. Jo'rayev, Q. Usmonov, A. Nurqulov, G. Jo'rayeva
**Sahifalar:** 6-8
**PISA domeni:** Reading (O'qish) — tarix PISA tomonidan alohida baholanmaydi, lekin manba tahlili o'qish kompetensiyasi hisoblanadi
**PISA maqsad darajasi:** Level 2-3 (5-sinf uchun)
**Bloom's qamrovi:** Remember → Understand → Apply → Analyze (minimum 4 daraja)

> **Asoslanish:** UNIFIED spec 1.1-bo'lim — "Har bir uy vazifasi sessiyasi Bloom's taksonomiyasining kamida 4 darajasini qamrab olishi SHART"

---

## Mundarija

1. [Standard kodlar va teglar](#1-standard-kodlar-va-teglar)
2. [Sessiya oqimi — Standard rejim (25 daqiqa)](#2-sessiya-oqimi--standard-rejim-25-daqiqa)
3. [Sessiya oqimi — Extended rejim (45 daqiqa)](#3-sessiya-oqimi--extended-rejim-45-daqiqa)
4. [Faza 1: Xotira Sprinti (Memory Sprint)](#4-faza-1-xotira-sprinti)
5. [Faza 2: Hikoya rejimi (Story Mode)](#5-faza-2-hikoya-rejimi)
6. [Faza 3: O'yin tanaffuslari (Game Breaks)](#6-faza-3-oyin-tanaffuslari)
7. [Faza 4: Hayotiy vaziyat (Real-Life Challenge)](#7-faza-4-hayotiy-vaziyat)
8. [Faza 5: Mustahkamlash (Consolidation)](#8-faza-5-mustahkamlash)
9. [Faza 6: Yakuniy Boss (Final Boss)](#9-faza-6-yakuniy-boss)
10. [Faza 7: Tafakkur (Reflection)](#10-faza-7-tafakkur)
11. [AI rollari — demo uchun](#11-ai-rollari--demo-uchun)
12. [Kontentning to'liq ro'yxati](#12-kontentning-toliq-royxati)

---

## 1. Standard kodlar va teglar

Har bir kontent birligi quyidagi 3 ta tegga ega bo'lishi **SHART**:

> **Asoslanish:** UNIFIED spec 2.5-bo'lim — "No tag, no deployment. Tegi yo'q kontent draft holatida qoladi."

### 1.1 Darslik ma'lumotnomasi (textbook_ref)

```json
{
  "textbook_id": "tar-5-2020-uz",
  "grade": 5,
  "subject": "history",
  "language": "uz",
  "chapter": "I bob. Tarix — o'tmish guvohi va bugungi kun uchun ibrat maktabi",
  "section": "1-§. Tarix fani nimani o'rganadi?",
  "page_range": "6-8",
  "textbook_isbn": "978-9943-05-737-1",
  "textbook_year": 2020
}
```

### 1.2 Standard kodlari

| Birlamchi kod | Alias kod | Tavsif |
|---|---|---|
| `UZ-HIST-5-SOURCES-01` | `TAR.5.1.1.1` | Tarix fanining ta'rifini bilish |
| `UZ-HIST-5-SOURCES-02` | `TAR.5.1.1.2` | Tarixiy manbalarni aniqlash va tasniflash (moddiy va yozma) |
| `UZ-HIST-5-SOURCES-03` | `TAR.5.1.1.3` | Moddiy va yozma manbalarni taqqoslash va farqlash |
| `UZ-HIST-5-SOURCES-04` | `TAR.5.1.1.4` | O'zbekiston tarixiga oid yozma manbalarni bilish (Avesto va boshqalar) |

> **Asoslanish:** UNIFIED spec 2.4-bo'lim — ikki formatli standard kod tizimi. Birlamchi: `UZ-{FAN}-{SINF}-{MAVZU}-{TARTIB}`, Alias: `{FAN}.{SINF}.{BOB}.{MAVZU}.{MAQSAD}`

### 1.3 PISA teglari

| Standard | PISA daraja | Domen | Jarayon | Kontekst | O'tish ko'nikmasi |
|---|---|---|---|---|---|
| SOURCES-01 | 1 | reading | access_and_retrieve | educational | Asosiy: faktlarni eslab qolish |
| SOURCES-02 | 2 | reading | access_and_retrieve | educational | L1→L2: oddiy tasniflash va xulosalar chiqarish |
| SOURCES-03 | 2-3 | reading | integrate_and_interpret | educational | L2→L3: bir nechta ma'lumotni birlashtirish; taqqoslash |
| SOURCES-04 | 2 | reading | access_and_retrieve | societal | L1→L2: matndan aniq ma'lumotni topish |

> **Asoslanish:** UNIFIED spec 3.0-bo'lim — O'qish PISA darajalari; 7.2-bo'lim — 5-6 sinf o'qish maqsadi: "Level 2-3, Interpretation: integrate info from multiple parts of text"

---

## 2. Sessiya oqimi — Standard rejim (25 daqiqa)

```
+--------------------------------------------------------------------+
|  UY VAZIFASI: Tarix — I bob — 1-§. Tarix fani nimani o'rganadi?    |
|  Standard: UZ-HIST-5-SOURCES-01..04  |  PISA: L2-3  |  Bloom's: Mix|
+--------------------------------------------------------------------+
|                                                                      |
|  F1  XOTIRA SPRINTI ------- 2 daq --- [Kirish bobidan eslatmalar]   |
|   |                                                                  |
|  F2  HIKOYA REJIMI -------- 6 daq --- [Yosh arxeolog hikoyasi]      |
|   |    +-- har segment orasida nazorat savollari                     |
|   |                                                                  |
|  F3  O'YIN TANAFFUSLARI --- 6 daq --- [3 o'yin]                    |
|   |    +-- Tile Match / Sentence Fill / Why Chain                    |
|   |                                                                  |
|  F4  HAYOTIY VAZIYAT ------ 4 daq --- [Oilaviy arxiv topilmasi]    |
|   |                                                                  |
|  F5  MUSTAHKAMLASH -------- 2 daq --- [Memory Palace — Registon]    |
|   |                                                                  |
|  F6  YAKUNIY BOSS --------- 7 daq --- [100 HP, 5 savol]            |
|   |    +-- YUTQAZISH → Sokratik tutoring → qayta boss               |
|   |                                                                  |
|  F7  TAFAKKUR ------------- 2 daq --- [2 ta savol]                  |
|                                                                      |
|  SESSIYA YAKUNLANDI — XP berildi, yulduzlar hisoblandi              |
+--------------------------------------------------------------------+
```

> **Asoslanish:** UNIFIED spec 4.2-bo'lim — Standard rejim sessiya tuzilishi; 17.2-bo'lim — 5-8 sinf Standard rejim: 20-30 daqiqa

---

## 3. Sessiya oqimi — Extended rejim (45 daqiqa)

```
+--------------------------------------------------------------------+
|  SINF DARS: Tarix — I bob — 1-§. Tarix fani nimani o'rganadi?     |
|  Standard: UZ-HIST-5-SOURCES-01..04  |  PISA: L2-3  |  Bloom's: Mix|
+--------------------------------------------------------------------+
|                                                                      |
|  F1  XOTIRA SPRINTI ------- 2 daq --- [Kirish bobidan, 8 savol]    |
|   |                                                                  |
|  F2  HIKOYA REJIMI -------- 10 daq -- [5 segment, kengaytirilgan]   |
|   |    +-- har segment orasida nazorat savollari                     |
|   |                                                                  |
|  F3  O'YIN TANAFFUSLARI --- 10 daq -- [4 o'yin]                    |
|   |    +-- Tile Match / Sentence Fill / Why Chain / Mystery Box      |
|   |                                                                  |
|  F4  HAYOTIY VAZIYAT ------ 8 daq --- [Kengaytirilgan, 4 savol]    |
|   |                                                                  |
|  F5  MUSTAHKAMLASH -------- 5 daq --- [Memory Palace + Flashcards]  |
|   |                                                                  |
|  F6  YAKUNIY BOSS --------- 12 daq -- [100 HP, 8 savol]            |
|   |    +-- YUTQAZISH → Sokratik tutoring → qayta boss               |
|   |                                                                  |
|  F7  TAFAKKUR ------------- 3 daq --- [3 ta savol]                  |
|                                                                      |
|  SESSIYA YAKUNLANDI — XP berildi, yulduzlar hisoblandi              |
+--------------------------------------------------------------------+
```

> **Asoslanish:** UNIFIED spec 4.1-bo'lim — Extended rejim: "40-50 daqiqa, o'qituvchi boshqaruvida"

---

## 4. Faza 1: Xotira Sprinti

**Maqsad:** Oldingi bilimlarni faollashtirish. Ebbinghaus unutish egri chizig'iga qarshi kurash.

> **Asoslanish:** UNIFIED spec 5.1-bo'lim — "Oldingi boblardan tezkor eslatish savollari. JORIYdagi mavzudan EMAS."
> **Tadqiqot:** Roediger & Karpicke (2006) — "Faol esga tushirish qayta o'qishdan 3 baravar samarali"

**Manba:** Kirish bobi — "O'zbekiston — Vatanim manim" (1-§ dan OLDINGI kontent)

| # | Savol | Javob | Bloom's | Standard |
|---|---|---|---|---|
| 1 | "Vatan" so'zi qaysi tildan olingan? | Arabcha | Remember | Kirish |
| 2 | "Vatan" so'zining ma'nosi nima? | Ona yurt | Remember | Kirish |
| 3 | O'zbekiston o'tmishda qanday nomlar bilan ataldi? (kamida 2 ta) | Turon, Movarounnahr, Turkiston | Remember | Kirish |
| 4 | Davlatimiz necha ming yillik tarixga ega? | Sal kam 3 ming yil | Remember | Kirish |
| 5 | "Tarixiy xotirasiz ..." — davom ettiring | "...kelajak yo'q" | Remember | Kirish |

**Extended rejim qo'shimcha savollari (6-8):**

| 6 | Bu hikmatli so'zni kim aytgan? | Islom Karimov | Remember | Kirish |
| 7 | Islom Karimovning qaysi kitobida bu so'z bor? | "Yuksak ma'naviyat — yengilmas kuch" | Remember | Kirish |
| 8 | O'zbekiston dunyoning nechta rivojlangan davlat qatoriga kirishga intilmoqda? | 50 ta | Remember | Kirish |

**XP tizimi:**
- To'g'ri javob: +100 XP
- Tezlik bonusi (<5 soniya): +10 XP
- Ketma-ket streak: +10 XP × joriy streak
- Noto'g'ri javob uchun jazo: YO'Q (bu isitish, baholash emas)

> **Asoslanish:** UNIFIED spec 5.1-bo'lim — XP qiymatlari; HOMEWORK_STANDARDS.md 6.1-bo'lim

**Adaptatsiya qoidalari:**
```
AGAR aniqlik >= 80% → O'quvchi yangi kontentga tayyor
AGAR aniqlik 60-79% → Davom etiladi, lekin o'qituvchiga xabar beriladi
AGAR aniqlik < 60%  → Yangi kontentdan OLDIN remediation yo'naltiriladi
```

> **Asoslanish:** UNIFIED spec 5.1-bo'lim — Adaptatsiya qoidalari

---

## 5. Faza 2: Hikoya rejimi

**Maqsad:** Yangi darslik kontentini hikoya shaklida yetkazish. Tushunishni shakllantirish.

> **Asoslanish:** UNIFIED spec 5.2-bo'lim — "Tarix: Birlamchi manba parcha-lari bilan hikoya → sabab/oqibat tahlili"
> **Tadqiqot:** Willingham (2004) — "Hikoya orqali eslab qolish 22 baravar yaxshiroq"

**Madaniy narrativ:** "Yosh arxeolog — Registon siri" (5-sinf uchun)

> **Asoslanish:** UNIFIED spec 5.2-bo'lim, Madaniy narrativ jadvali — 5-sinf: Paxta terimi yoki mahalliy kontekst. Tarix fani uchun arxeologik kashfiyot narrativi mos keladi.

### Segment 1: "Tarix nima?" (2 daqiqa)

**Hikoya matni:**
> Samarqanddagi 5-sinf o'quvchisi Sardor bugun birinchi marta tarix darsiga keldi. O'qituvchisi Barno opa dedi: "Bolalar, tarix — bu o'tmish haqidagi fan. 'Tarix' arabcha so'z bo'lib, 'o'tgan voqealar haqida hikoya' degan ma'noni anglatadi."
>
> Sardor hayron bo'ldi: "Lekin o'tmishni qanday bilish mumkin? Hech kim o'sha paytda kamera bilan suratga olmagan-ku!"
>
> Barno opa kulib dedi: "Juda yaxshi savol! Ana shuning uchun biz TARIXIY MANBALAR haqida o'rganamiz."

**Nazorat savoli:**
```json
{
  "question": "'Tarix' so'zi qaysi tildan olingan va nima ma'noni anglatadi?",
  "correct_answer": "Arabcha, o'tmish yoki o'tgan voqealar haqida hikoya",
  "blooms_level": "remember",
  "pisa_level": 1,
  "transition_skill": "Asosiy: matndan aniq ma'lumotni topish",
  "explanation_on_wrong": "Hikoyada Barno opa tushuntirdi: 'Tarix' arabcha so'z bo'lib..."
}
```

### Segment 2: "Moddiy manbalar" (2 daqiqa)

**Hikoya matni:**
> Ertasi kuni sinf sayohatga chiqdi — Samarqanddagi arxeologik qazishmalar maydoniga. Arxeolog Akmal aka yerdan ehtiyotlik bilan eski tanga chiqardi.
>
> "Bu — MODDIY MANBA," dedi Akmal aka. "Moddiy manbalar — bu qadimgi odamlarning suyak qoldiqlari, ular yashagan joylar qoldiqlari, tangalar, gerblar, muhrlar va mehnat qurollari. Bularning hammasini biz arxeologlar qazish orqali topamiz."
>
> Sardor tangani ko'rdi — unda noma'lum yozuvlar bor edi. "Bu tanga necha yoshda?" deb so'radi. Akmal aka dedi: "Biz uni laboratoriyada tekshiramiz va aniq yoshini aniqlaymiz."

**Nazorat savoli:**
```json
{
  "question": "Arxeolog topgan tanga qaysi manba turiga kiradi? Nima uchun?",
  "correct_answer": "Moddiy manba, chunki u inson qo'li bilan yaratilgan ashyoviy narsa",
  "blooms_level": "understand",
  "pisa_level": 2,
  "transition_skill": "L1→L2: oddiy tasniflash va xulosalar chiqarish",
  "explanation_on_wrong": "Moddiy manbalar — qadimgi odamlar yaratgan NARSALAR: suyaklar, binolar, tangalar, qurollar..."
}
```

### Segment 3: "Yozma manbalar" (2 daqiqa)

**Hikoya matni:**
> Sayohatdan qaytib, Barno opa sinfga eski kitob rasmini ko'rsatdi.
>
> "Bu — Avesto kitobi. O'zbekiston tarixiga oid eng QADIMGI yozma manba. Bundan besh ming yil oldin odamlar qoyatoshlarga, hayvon terisiga, daraxt po'stlog'iga yozishni o'rgangan. Keyinchalik qog'oz ixtiro qilingan."
>
> "Yozma manbalar tarixiy manbalarning eng muhim va asosiy turidir. Ular arxivlarda saqlanadi."
>
> Sardor o'yladi: "Demak, Akmal aka topgan tanga — moddiy manba, Avesto kitobi — yozma manba. Ikkalasi ham o'tmish haqida gapiradi, lekin turli yo'llar bilan!"

**Nazorat savoli:**
```json
{
  "question": "Sardor qanday xulosa chiqardi? Moddiy va yozma manbalar orasidagi asosiy farq nima?",
  "correct_answer": "Moddiy manbalar — narsalar (ashyolar), yozma manbalar — yozib qoldirilgan ma'lumotlar. Ikkalasi ham o'tmish haqida gapiradi, lekin turli yo'llar bilan.",
  "blooms_level": "understand",
  "pisa_level": 2,
  "transition_skill": "L1→L2: oddiy tasniflash va xulosalar chiqarish",
  "explanation_on_wrong": "Darslikda yozilgan: moddiy manbalar — bu qo'l bilan yaratilgan NARSALAR. Yozma manbalar — bu YOZIB qoldirilgan ma'lumotlar."
}
```

**Extended rejim qo'shimcha segmentlari (4-5):**

### Segment 4 (Extended): "Arxeologlar qanday ishlaydi?" (2 daqiqa)

> Akmal aka tushuntirdi: qazish maydonini belgilash → ehtiyotlik bilan qazish → topilmani tozalash → yoshini aniqlash. "O'zbekiston olimlari shu yo'l bilan Samarqandning 2750, Toshkentning 2200 yoshda ekanini aniqladilar."

**Nazorat savoli:** "Samarqand shahri necha yoshda?"
- Javob: 2750 yosh
- Bloom's: Remember, PISA: 1

### Segment 5 (Extended): "Manbalarni solishtirish" (2 daqiqa)

> Barno opa sinf oldiga ikki narsa qo'ydi: sopol parchasini va Avesto sahifasi rasmini. "Qaysi biri ko'proq ma'lumot beradi?" O'quvchilar bahs boshladi...

**Nazorat savoli:** "Moddiy va yozma manbalardan qaysi biri o'tmish haqida ko'proq batafsil ma'lumot berishi mumkin? Nima uchun?"
- Javob: Yozma manbalar — chunki aniq ma'lumotlar, sanalar, voqealar yozilgan
- Bloom's: Analyze, PISA: 3
- Transition: L2→L3: bir nechta ma'lumotni birlashtirish; taqqoslash

**Qoidalar:**
- O'quvchi nazorat savoliga javob bermay KEYINGI segmentga o'ta OLMAYDI
- Noto'g'ri javobda: darslik sahifasiga murojaat qilib tushuntirish beriladi, qayta so'raladi
- Maksimum 2 ta qayta urinish. 2 marta noto'g'ri bo'lsa: soddalashtirilgan versiya

> **Asoslanish:** UNIFIED spec 5.2-bo'lim — "Nazorat savolini javobsiz o'tib bo'lmaydi. Maks 2 qayta urinish."

---

## 6. Faza 3: O'yin tanaffuslari

**Maqsad:** Yangi o'rganilgan tushunchalarni turli burchaklardan mashq qilish.

> **Asoslanish:** UNIFIED spec 5.3-bo'lim — "Har bir o'yin aniq bir kognitiv ko'nikmani faollashtiradi"
> **Cheklov:** UNIFIED spec 5.3-bo'lim — "Bitta mexanizm sessiyada 2 martadan ko'p takrorlanmasligi SHART"

### O'yin 1: Tile Match — "Manbalarni juftla" (2 daqiqa)

> **Tadqiqot:** Paivio (1986) — "Ikki kodlash: vizual + so'z = yaxshiroq xotira, +25-40% tanish"

**6 juft (Standard) / 8 juft (Extended):**

| Tile A (matn) | Tile B (vizual/matn) |
|---|---|
| Moddiy manba | 🪙 Qadimgi tanga rasmi |
| Yozma manba | 📜 Avesto kitobi rasmi |
| Arxeolog | ⛏️ Qazish ishlarida odam rasmi |
| Arxiv | 🏛️ Hujjatlar saqlanadigan bino |
| Suyak qoldiqlari | Moddiy manba |
| Qoyatoshga yozilgan yozuv | Yozma manba |
| **Extended qo'shimcha:** | |
| Manbashunos | Manbalarni o'rganuvchi olim |
| Hayvon terisi | Qadimgi yozuv materiali |

**Mexanika:**
- Taymer: 2:30 (ko'rinadigan ortga sanash)
- To'g'ri juft: +100 XP, taymer +3 soniya bonus
- Noto'g'ri juft: tilelar silkinadi, taymer -5 soniya
- Mukammal: 300 XP | Qisman: 100-250 XP

> **Asoslanish:** UNIFIED spec 6.2-bo'lim, Tile Match spetsifikatsiyasi — 5-8 sinf: 6-8 juft, 2:30 taymer

### O'yin 2: Sentence Fill — "Bo'shliqni to'ldiring" (2 daqiqa)

> **Tadqiqot:** Taylor (1953) — "Cloze testi — ishonchli tushunish o'lchovi, +35% so'z boyligi"

**8 ta gap (Standard) / 10 ta gap (Extended):**

1. Tarix — bu ______ haqidagi fan. *(o'tmish)*
2. "Tarix" so'zi ______ tilidan olingan. *(arab)*
3. Tarixiy manbalar ikki turga bo'linadi: ______ va yozma. *(moddiy)*
4. ______ manbalar — bu qadimgi odamlar yaratgan narsalar. *(Moddiy)*
5. O'zbekiston tarixiga oid eng qadimgi yozma manba — ______ kitobi. *(Avesto)*
6. Moddiy manbalarni ______ to'plashadi. *(arxeologlar)*
7. Eski hujjatlar saqlanadigan joy — ______. *(arxiv)*
8. Yozma manbalar tarixiy manbalarning ______ va asosiy turidir. *(muhim)*

**Extended qo'shimcha:**
9. Bundan qariyb ______ ming yil avval xalqlar alifbo yaratganlar. *(besh)*
10. Qadimgi ______, Sug'd, Baqtriya alifbolarida yozuvlar Vatanimiz tarixini o'rganishda katta ahamiyatga ega. *(Xorazm)*

**So'z banki** (5-sinf uchun: to'g'ri javoblar + har bir bo'shliq uchun 2 ta chalg'ituvchi):

> **Asoslanish:** UNIFIED spec 6.2-bo'lim, Sentence Fill — "5-7 sinf: to'g'ri javoblar + har bir bo'shliq uchun 2 ta chalg'ituvchi"

**XP:** Har to'g'ri javob: +100 XP | Birinchi urinishdan to'g'ri: +25 XP | Hammasi to'g'ri: +100 bonus

### O'yin 3: Why Chain — "Nima uchun?" zanjiri (2-3 daqiqa)

> **Tadqiqot:** Pressley va boshq. (1992) — "Elaborativ so'roq — 'nima uchun?' savollari tushunishni chuqurlashtiradi, +2 PISA sub-daraja"

**3 daraja (Standard) / 4 daraja (Extended):**

```
AI: "Nima uchun tarixiy manbalar muhim?"
O'quvchi: "O'tmish haqida bilish uchun."
AI: "Yaxshi boshlanish! Lekin NIMA UCHUN o'tmishni bilish kerak?"

O'quvchi: "O'z tarixini bilmaydigan millatning kelajagi yo'q."
AI: "Ajoyib! Demak, tarixiy manbalar kelajakka qanday bog'langan?"

O'quvchi: "O'tmishdagi xatolarni takrorlamaslik uchun."
AI: "Zo'r! Agar bizda faqat MODDIY manbalar bo'lsa-yu, YOZMA manbalar bo'lmasa — nimani bilib bo'lmas edi?"

[Extended 4-daraja:]
O'quvchi: "Aniq sanalar, ismlar, voqealar tafsilotlari."
AI: "Mukammal! Siz tushuntirdingiz: moddiy manbalar NIMA bo'lganini ko'rsatadi, yozma manbalar NIMA UCHUN bo'lganini tushuntiradi!"
```

**AI qoidalari:**
- **HECH QACHON** to'g'ridan-to'g'ri javob bermaslik
- **HAR DOIM** o'quvchining to'g'ri aytganini tan olish
- **HAR DOIM** bir daraja chuqurroq so'rash
- **SHART:** Aniq darslik sahifasiga murojaat qilish

> **Asoslanish:** UNIFIED spec 6.2-bo'lim, Why Chain — "AI: HECH QACHON to'g'ri javob bermaydi | HAR DOIM tan oladi | HAR DOIM chuqurroq so'raydi"
> AI Roles 6.3-bo'lim — Sokratik dialog cheklovlari

**XP:** Har daraja: +150 XP | Hammasi bajarilsa: +250 bonus

### O'yin 4 (Faqat Extended): Mystery Box — "Manba turini aniqla" (2-3 daqiqa)

> **Tadqiqot:** Rohrer & Taylor (2007) — "Aralashtirilgan mashq +43% ko'chirish samaradorligi"

**5 ta quti, har birida boshqa turdagi topilma:**

| Quti | Kontent | To'g'ri tur | Qiyinlik |
|---|---|---|---|
| 1 | Qoyatoshga chizilgan rasm | Moddiy manba | Oson |
| 2 | Avesto kitobidan parcha | Yozma manba | Oson |
| 3 | Toshdan yasalgan mehnat quroli | Moddiy manba | O'rta |
| 4 | Qadimgi Xorazm alifbosidagi yozuv | Yozma manba | O'rta |
| 5 | **Tanga ustidagi yozuv** — moddiy yoki yozma? | IKKISI HAM! | Qiyin |

**Mexanika:**
1. Qutini tanlash → ochiladi, topilma ko'rinadi
2. BIRINCHI: manba turini aniqlash (dropdown)
3. KEYIN: qo'shimcha savol ("Bu nima haqida ma'lumot beradi?")
4. Ikkalasi ham to'g'ri: 250 XP

> **Asoslanish:** UNIFIED spec 6.2-bo'lim, Mystery Box — "5-sinf: 3-5 quti"

**5-quti haqida maxsus izoh:** Tanga ustidagi yozuv — bu ham moddiy (tanga o'zi — ashyoviy narsa), ham yozma (ustidagi yozuv — ma'lumot). Bu tarixda "chekka holat" bo'lib, chuqurroq tafakkurni talab qiladi. PISA Level 3 — Analyze.

---

## 7. Faza 4: Hayotiy vaziyat

**Maqsad:** Transfer — darslik bilimlarini hech ko'rmagan hayotiy vaziyatga qo'llash.

> **Asoslanish:** UNIFIED spec 5.4-bo'lim — "PISA o'lchaydigan asosiy ko'nikma — bilimni real vaziyatga ko'chirish"
> **Cheklov:** UNIFIED spec 5.4-bo'lim — "PISA Level 2+ (pastroq darajadagi o'quvchilar uchun qo'shimcha Adaptive Quiz o'rniga)"

### Ssenariy: "Bobongizning sandiq siri"

**Kontekst:**
> Yozgi ta'tilda siz Buxorodagi bobongizning uyiga bordingiz. Eski sandiqdan quyidagilar topildi:
> 1. Bobongizning otasi yozgan kundalik (1940-yillar)
> 2. Oilaviy fotosurat (1950-yil)
> 3. Rasmiy hujjat — Toshkent viloyati hokimligidan (1948-yil)
> 4. Qo'shningiz Xolida xola so'zlagan hikoya: "Sizning bobongiz juda mashhur hunarmand bo'lgan"
>
> Tarixchi siz oilangiz tarixini tiklashni xohlaysiz. Lekin MUAMMO: kundalikda "dehqon" deb yozilgan, Xolida xola "hunarmand" deb aytmoqda.

**Standard rejim (2 savol):**

| # | Savol | PISA | Bloom's | O'tish ko'nikmasi |
|---|---|---|---|---|
| 1 | Topilgan 4 ta narsadan qaysilari YOZMA manba, qaysilari boshqa turdagi manba? | L2 | Understand | L1→L2: tasniflash |
| 2 | Kundalik "dehqon" deydi, Xolida xola "hunarmand" deydi. Siz tarixchi sifatida qaysi manbaga ko'proq ishonasiz? NIMA UCHUN? | L3 | Analyze | L2→L3: manbalar ishonchliligini baholash |

**Extended rejim (4 savol):**

| 3 | Agar siz haqiqiy tarixchi bo'lsangiz, bobongiz kasbini ANIQ bilish uchun yana qanday manbalarni qidirgan bo'lar edingiz? Kamida 2 ta manba taklif qiling. | L3-4 | Evaluate | L3→L4: qo'shimcha dalillar izlash zaruratini tushunish |
| 4 | Og'zaki hikoya (Xolida xola) va yozma hujjat (kundalik) orasidagi farqni tushuntiring. Qaysi biri vaqt o'tishi bilan ko'proq o'zgarishi mumkin? | L3 | Analyze | L2→L3: manbalar xususiyatlarini taqqoslash |

> **Asoslanish:** Stress-test natijasi — Ssenariy 3 yagona "haqiqiy transfer" ssenariyi. Manbalar o'rtasidagi ZIDDIYAT o'quvchini darslik ta'riflarini shunchaki takrorlashdan ko'ra chuqurroq fikrlashga majbur qiladi.
> UNIFIED spec 5.4-bo'lim — "Har bir ssenariy SHART ravishda joriy mavzudan kamida bitta standardga murojaat qilishi kerak"

**Baholash rubrikasi (2-savol):**
- To'liq ball: To'g'ri taqqoslash + asoslash bilan
- Qisman ball: To'g'ri javob, lekin tushuntirishsiz
- Ball yo'q: Tasodifiy javob yoki asossiz

---

## 8. Faza 5: Mustahkamlash

**Maqsad:** Boss jangidan oldin asosiy tushunchalarni uzoq muddatli xotiraga mustahkamlash.

> **Asoslanish:** UNIFIED spec 5.5-bo'lim — "Boss jangidan oldin muhim tushunchalarni uzoq muddatli xotiraga mustahkamlash"
> **Tadqiqot:** Maguire va boshq. (2003) — "Loci usuli: +300% eslab qolish"

### Memory Palace: Registon maydoni (Samarqand)

> **Asoslanish:** UNIFIED spec 5.5-bo'lim — "Memory Palace standart joylashuvi: Registon maydoni (Samarqand)"

**5 ta tushuncha, 5 ta joy:**

| Joy (Registonda) | Tushuncha | Vizual obraz |
|---|---|---|
| 1. Bosh darvoza | TARIX — o'tmish haqidagi fan | Darvozada katta kitob ochilib turibdi, sahifalari o'tmishga qarab uchmoqda |
| 2. Ulug'bek madrasasi | MODDIY MANBALAR — tangalar, qurollar, suyaklar | Madrasaning hovlisida arxeolog tanga qazib olmoqda |
| 3. Sherdo'r madrasasi | YOZMA MANBALAR — Avesto, yozuvlar, hujjatlar | Sherlar o'rnida ikkita katta kitob rasmi |
| 4. Tillakori madrasasi | ARXIV — eski hujjatlar saqlanadigan joy | Tillakori ichida javonlarda minglab sariq hujjatlar |
| 5. Maydon markazi | FARQ: moddiy = NARSALAR, yozma = MA'LUMOTLAR | Markazda tanga (chap) va kitob (o'ng) tarozida turibdi |

**Bosqichlar:**
1. Palata tanlash (30 soniya): Registon maydoni (standart)
2. Tushunchalarni joylashtirish (60 soniya): vizual obrazlar bilan
3. Xayoliy sayohat (30 soniya): yo'naltiruvchi vizualizatsiya
4. Esga tushirish testi (60 soniya): "Bosh darvozada nima bor edi?" — 5 ta savol

**XP:** Har to'g'ri esga tushirish: +50 XP | 5/5 to'g'ri: +50 bonus | Jami: 300 XP

**Extended qo'shimcha:** Flashcardlar (2 daqiqa) — SM-2 algoritmiga asoslangan

| Old | Orqa |
|---|---|
| Tarixiy manba — bu... | ...inson qo'li bilan yaratilgan narsalar va yozib qoldirilgan ma'lumotlar |
| Avesto — bu... | ...O'zbekiston tarixiga oid eng qadimgi yozma manba |
| Arxeolog — bu... | ...moddiy manbalarni qazish orqali o'rganuvchi olim |
| Arxiv — bu... | ...eski hujjatlar saqlanadigan joy |
| Manbashunos — bu... | ...tarixiy manbalarni sinchiklab o'rganuvchi olim |

---

## 9. Faza 6: Yakuniy Boss

**Maqsad:** PISA-kalibrlangan baholash. O'quvchi maqsadli PISA darajasida kompetentligini ISBOTLASHI shart.

> **Asoslanish:** UNIFIED spec 5.6-bo'lim — "Boss YENGILISHI SHART — hech qanday istisno yo'q"

### Boss konfiguratsiyasi

| Parametr | Qiymat | Asoslanish |
|---|---|---|
| Boss HP | **100 HP** | UNIFIED 5.6-bo'lim: "5-8 sinf: 100 HP" |
| Savol turlari | Qisqa javob + ochiq fikrlash (5+ sinf uchun MC yo'q) | UNIFIED 5.6-bo'lim |
| Hint jarima | -10 HP (boss HP qaytaradi) | UNIFIED 5.6-bo'lim: "5-8 sinf: -10 HP" |
| Combo bonus | 3 ta ketma-ket to'g'ri → keyingi zarar 2× | UNIFIED 5.6-bo'lim |
| O'tib ketish | **YO'Q. Hech qanday istisno.** | UNIFIED 5.6-bo'lim |
| AI darajasi | Tier 3 (Sokratik tutoring yutqazganda) | AI Roles 5.1-bo'lim |

### Savol taqsimoti

> **Asoslanish:** UNIFIED spec 5.6-bo'lim — "40% Oson (joriy PISA), 40% O'rta (maqsad PISA), 20% Qiyin (maqsaddan yuqori)"

**Standard rejim — 5 savol:**

| # | Daraja | Zarar | PISA | Bloom's | Savol |
|---|---|---|---|---|---|
| 1 | Oson | -10 HP | L2 | Remember | "Tarixiy manbalar necha turga bo'linadi? Ularni nomlang." |
| 2 | Oson | -10 HP | L2 | Understand | "Avesto kitobi qaysi manba turiga kiradi? Javobingizni asoslang." |
| 3 | O'rta | -20 HP | L3 | Apply | "Arxeologlar Samarqanddan qadimgi sopol topdi. Ustida yozuv bor. Bu moddiy manbami yoki yozma manbami? Yoki ikkisi ham? Tushuntiring." |
| 4 | O'rta | -20 HP | L3 | Analyze | "Moddiy va yozma manbalardan faqat BITTASINI tanlashingiz kerak bo'lsa, qaysi birini tanlagan bo'lar edingiz? NIMA UCHUN?" |
| 5 | Qiyin | -30 HP | L4 | Evaluate | "Bir tarixchi faqat yozma manbalarga, ikkinchisi faqat moddiy manbalarga tayanadi. Ikkisi ham O'zbekiston tarixini yozmoqchi. Qaysi birining ishi to'liqroq bo'ladi? Nima uchun? Ikkalasi ham nima uchun kerak?" |

**Maksimal zarar:** 10+10+20+20+30 = 90 HP (100 HP bossni yenish uchun kamida 1 hint ishlatilsa qaytariladi)

**Extended rejim — 8 savol (taqsimot: 3 Oson / 3 O'rta / 2 Qiyin ≈ 40/40/20%):**

> **Izoh:** 8 savolda aniq 40/40/20 mumkin emas (3.2/3.2/1.6). Eng yaqin: 3/3/2. Bu spec ga mos keladi.

| 6 | Oson | -10 HP | L2 | Remember | "Arxiv nima? Ta'rifini bering." |
| 7 | O'rta | -20 HP | L3 | Apply | "Sizning mahallangizda yangi bino qurilishi paytida yerdan eski buyumlar topildi. Siz arxeolog sifatida birinchi navbatda nima qilgan bo'lar edingiz?" |
| 8 | Qiyin | -30 HP | L4 | Evaluate | "Agar Avesto kitobi topilmaganida, O'zbekiston tarixini bilish qanchalik qiyin bo'lar edi? Qanday yo'llar bilan o'tmishni bilish mumkin bo'lar edi?" |

### Yutqazish oqimi

```
AGAR boss yengilmasa (HP > 0):
  1. O'quvchi qaysi standardda yutqazganini ANIQLASH
  2. Yutqazishlarni aniq darslik bo'limlariga MOSLASHTIRISH
  3. SOKRATIK TUTORING FAOLLASHTIRISH (Tier 3 AI):
     - AI yo'naltiruvchi savollar beradi, HECH QACHON javob bermaydi
     - O'quvchini aniq Hikoya rejimi segmentiga qaytaradi
  4. Boss savollarini QAYTA YARATISH (bir xil standardlar, boshqa kontekst)
  5. O'quvchi bossni qayta uradi

AGAR boss yengilsa:
  → Faza 7 ga o'tish
  → Mahorat yulduzlarini hisoblash
```

> **Asoslanish:** UNIFIED spec 5.6-bo'lim — "Yutqazish oqimi"
> AI Roles 5.1-bo'lim — "Boss qayta urinishda Tier 3 regeneratsiya"
> AI Roles 6.3-bo'lim — "HECH QACHON to'g'ri javob bermaydi"

### Mahorat yulduzlari

| Yulduzlar | Mezon | Ochiladi |
|---|---|---|
| ⭐ | Boss yengildi (har qanday urinish) | Bob yakunlandi |
| ⭐⭐ | Boss ≤2 urinishda yengildi, >50% HP qoldi | Bonus avatar element |
| ⭐⭐⭐ | Boss BIRINCHI urinishda, hintsiz, >80% HP | Maxsus nishon |

> **Asoslanish:** UNIFIED spec 5.6-bo'lim — "Mahorat yulduzlari"

---

## 10. Faza 7: Tafakkur

**Maqsad:** Metakognitiv xabardorlikni shakllantirish.

> **Asoslanish:** UNIFIED spec 5.7-bo'lim
> **Tadqiqot:** Flavell (1979) — "Tafakkur keyingi sessiya natijalarini 20-30% yaxshilaydi"

**AI prompt generatsiyasi:**
```
AGAR aniqlik >= 80%:
  → "Bugun qaysi strategiya sizga yordam berdi?"
AGAR aniqlik 60-79%:
  → "Qaysi qism qiyin bo'ldi? Qanday yechim topdingiz?"
AGAR aniqlik < 60%:
  → "Buni yaxshiroq tushunish uchun nima yordam beradi?"
```

**Standard rejim — 2 prompt:**

1. "Moddiy va yozma manbalar orasidagi farqni qanday tushuntirgan bo'lar edingiz? O'z so'zlaringiz bilan yozing."
2. "Bugungi darsdan eng muhim narsa nima edi?"

**Extended rejim — 3 prompt:** Yuqoridagi 2 + qo'shimcha:

3. "Agar siz arxeolog bo'lsangiz, qaysi turdagi manbani qidirishni afzal ko'rgan bo'lar edingiz? Nima uchun?"

**Talablar:**
- Minimal 10 ta belgi (Standard) / 2 gap (Extended)
- Avtomatik baho yo'q (barcha to'g'ri javoblar qabul qilinadi)
- O'qituvchi faqat umumiy mavzularni ko'radi, individual yozuvlarni EMAS

> **Asoslanish:** UNIFIED spec 5.7-bo'lim — "Maxfiylik: o'quvchining shaxsiy tafakkuri. O'qituvchi faqat umumiy mavzularni ko'radi."

**XP:** Tafakkur yozish uchun: +100 XP

---

## 11. AI rollari — demo uchun

> **Asoslanish:** AI Roles 0.2-bo'lim — "Demo Readiness" jadvali (Tarix uchun moslashtirilgan)

| Rol | Demo darajasi | Nima quriladi | Nima stub bo'ladi |
|---|---|---|---|
| **Kontent Pipeline AI** | STUB | 50-60 ta kontentni qo'lda darslikdan yozish | OCR, avtomatik generatsiya |
| **Sessiya Assembly AI** | SODDALASHTIRILGAN | 7-fazali sessiya yig'uvchi, qoidalarga asoslangan | To'liq Ebbinghaus modeli |
| **Adaptatsiya AI** | SODDALASHTIRILGAN | Foiz chegaralari: <60% pastga, >90% yuqoriga, 70-80% saqla | Sessiyalar arasi profil, mahorat so'nishi |
| **Baholash AI** | SODDALASHTIRILGAN | Boss HP tizimi (100 HP, zarar darajalari, combo, yulduzlar) | IRT rekalibratsiya |
| **Tutoring AI** | **TO'LIQ** | Sokratik dialog — bitta LLM API chaqiruvi. Boss yutqazganda: o'quvchi javobi + savol konteksti + darslik parcha → yo'naltiruvchi savol qaytadi | Ko'p bosqichli xotira |
| **Operatsiyalar AI** | STUB | Butunlay o'tkazib yuborish | Hamma narsa |

**Yagona LLM integratsiya nuqtasi — Sokratik tutoring:**

```
POST /api/tutor/socratic

Kirish:
{
  "student_answer": "Yozma manba",
  "correct_answer": "Ikkisi ham — moddiy (tanga o'zi) va yozma (ustidagi yozuv)",
  "was_correct": false,
  "question_context": "Arxeologlar Samarqanddan sopol topdi. Ustida yozuv bor. Bu qaysi manba turi?",
  "student_pisa_level": 1.7,
  "textbook_ref": { "page": "6-8", "section": "1-§. Tarix fani nimani o'rganadi?" },
  "language": "uz",
  "turn_number": 1,
  "max_turns": 4
}

Chiqish:
{
  "response_text": "Yaxshi fikr! Ustidagi yozuv — ha, yozma manba. Lekin sopolning O'ZI — bu nima? U inson qo'li bilan yaratilgan NARSA emasmi?",
  "probe_type": "guide_to_dual_classification",
  "references_textbook": { "page": "6-7", "hint": "Darslikning 6-betidagi ta'rifga qarang" },
  "should_continue": true
}
```

> **Asoslanish:** AI Roles 0.4-bo'lim — "Yagona LLM integratsiya nuqtasi"; AI Roles 6.2-bo'lim — Sokratik tutoring interfeys shartnomasi

**Fallback:** Agar LLM mavjud bo'lmasa → task JSON dagi oldindan yozilgan `socratic_hints` massivini ko'rsatish.

---

## 12. Kontentning to'liq ro'yxati

Har bir fazaga kerak bo'ladigan minimal kontent miqdori:

| Faza | Kontent turi | Miqdor | Manba |
|---|---|---|---|
| F1: Xotira Sprinti | `recall_item` | 8 ta | Kirish bobidan qo'lda yozish |
| F2: Hikoya rejimi | `narrative_segment` | 3-5 ta | Darslik 6-8 betlar asosida hikoya |
| F2: Hikoya rejimi | `checkpoint_question` | 3-5 ta (har segment uchun 1) | PISA-kalibrlangan |
| F3: Tile Match | `tile_match_pair` | 6-8 juft | Darslikdan tushunchalar |
| F3: Sentence Fill | `sentence_fill` | 8-10 ta | Darslik matnidan |
| F3: Why Chain | `why_chain_sequence` | 1 ta (3-4 daraja) | Tier 2 AI dialog |
| F3: Mystery Box | `mystery_box_item` | 5 ta (faqat Extended) | Darslikdan topilmalar |
| F4: Hayotiy vaziyat | `transfer_scenario` | 1 ta (2-4 savol) | Tier 2 AI + ekspert ko'rigi |
| F5: Memory Palace | `mnemonic_exercise` | 1 ta (5 tushuncha) | Qo'lda loyihalash |
| F5: Flashcards | `flashcard` | 5 ta (faqat Extended) | Darslikdan atamalar |
| F6: Boss savollari | `boss_question` | 5-8 ta (daraja bo'yicha) | PISA-kalibrlangan |
| F7: Tafakkur | `reflection_prompt` | 2-3 ta | Shablon asosida |
| **JAMI** | | **~50-60 ta** | |

> **Asoslanish:** UNIFIED spec 10.2-bo'lim — "Har bir mavzu uchun minimal: ~85 ta kontent birligi". Demo uchun 50-60 ta yetarli (AI Roles 0.3-bo'lim).

### XP jami (Standard rejim, ideal bajarilish):

| Faza | Maksimal XP |
|---|---|
| F1: Xotira Sprinti | 5 × 100 + bonus = ~600 |
| F2: Hikoya | 150 (sessiya uchun) |
| F3: Tile Match | 300 |
| F3: Sentence Fill | 8 × 100 + bonus = 900 |
| F3: Why Chain | 3 × 150 + 250 = 700 |
| F4: Hayotiy vaziyat | 400 |
| F5: Memory Palace | 300 |
| F6: Boss (3 yulduz) | 1000 |
| F7: Tafakkur | 100 |
| **JAMI** | **~4,450 XP** |

> **Asoslanish:** UNIFIED spec 11.1-bo'lim — XP mukofot matritsasi

---

## Ilovalar

### A. Sessiya yakunlanish talablari

Sessiya FAQAT quyidagilarning HAMMASI bajarilganda TUGALLANGAN hisoblanadi:

- [x] F1: Xotira Sprinti yakunlandi (barcha savollar urinildi)
- [x] F2: Barcha Hikoya segmentlari ko'rildi, barcha nazorat savollari o'tildi
- [x] F3: Barcha tayinlangan o'yinlar bajarildi
- [x] F4: Hayotiy vaziyat topshirildi (barcha savollarga urinildi)
- [x] F5: Mustahkamlash mashqi bajarildi
- [x] F6: Boss YENGILDI (HP 0 ga tushirildi)
- [x] F7: Tafakkur yozildi (minimal uzunlik bajarildi)

**Qisman yakunlash YO'Q.** O'quvchi to'liq sessiyani tugatadi yoki u "jarayonda" holatida qoladi.

> **Asoslanish:** UNIFIED spec Ilova A.1 — "Qisman yakunlash yo'q"

### B. Adaptatsiya qoidalari (barcha fazalarda)

```
HAR 3-5 SAVOLDA TEKSHIRILADI:

ASOSIY (foizga asoslangan):
  AGAR muvaffaqiyat_darajasi < 60%:
    → qiyinlik_darajasi -= 1
    → Yordam yoqiladi

  AGAR muvaffaqiyat_darajasi > 90%:
    → qiyinlik_darajasi += 1
    → Keyingi Bloom's darajasi kiritiladi

  AGAR muvaffaqiyat_darajasi 70-80%:
    → Joriy darajani saqlash (OQIM ZONASI)

FAVQULODDA:
  AGAR o'yindagi aniqlik < 40%:
    → Aniq standardni belgilash
    → Qo'shimcha Hikoya micro-segmentini kiritish
```

> **Asoslanish:** UNIFIED spec 9.1-bo'lim — "Adaptatsiya qoidalari"; Csikszentmihalyi (1990) — "Oqim holati = 70-80% muvaffaqiyat"

---

**HUJJAT TUGADI**

*Bu hujjat NETS-Homework-Engine-UNIFIED.md v2.0 va AI-Roles-and-Responsibilities.md v1.0 asosida tuzilgan.*
*Barcha qarorlar tegishli bo'lim va tadqiqot manbalariga havola qilingan.*

**Versiya:** 1.0
**Sana:** 2026-yil, 2-aprel
