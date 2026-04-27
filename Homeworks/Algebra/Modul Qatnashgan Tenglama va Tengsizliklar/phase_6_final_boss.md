Mode: HARD
Level: B1

# Phase 6: Final Boss Challenge

Siz "Modul" tushunchasining haqiqiy ustasiga aylandingiz! Endi o'rganganlaringizni amaliyotda, qiyin va qiziqarli masalalarni yechish orqali sinab ko'ramiz. Bu sizning yakuniy jangingiz! 

**Boss HP: 100**
Sizning maqsadingiz barcha savollarga to'g'ri javob berib, Bossni yengish. Eslatma: har bir yechim qadami uchun daftaringizdagi ishlaringizni tizimga yuklang (Notebook Capture). Agar qiynalsangiz, yordam (hint) olishingiz mumkin, lekin ular Bossga beriladigan zararni kamaytiradi!

---

### 1-savol (Easy)
`[Bloom: L3 | PISA: L2 | Damage: -10 HP]`

**Vazifa:** Quyidagi modulli tenglamani yeching va barcha ildizlarini yozing:
`|x - 7| = 15`

<details>
<summary><b>Hint 1 (-5 HP)</b></summary>
Modul qoidasiga ko'ra, ichkaridagi ifoda musbat 15 ga yoki manfiy -15 ga teng bo'lishi mumkin.
</details>

<details>
<summary><b>Hint 2 (-5 HP)</b></summary>
Ikkita oddiy tenglamani yeching: `x - 7 = 15` va `x - 7 = -15`.
</details>

**Javob:** `x1 = 22`, `x2 = -8`.
**Failure Response:** Hali emas! Modul ta'rifiga ko'ra, tenglama ikkita holatga ajraladi. Birinchi holatda `x - 7 = 15`, ikkinchi holatda esa `x - 7 = -15`. Ikkalasidan `x` ni topib ko'ring.

---

### 2-savol (Easy)
`[Bloom: L3 | PISA: L2 | Damage: -10 HP]`

**Vazifa:** Quyidagi modulli tengsizlikni yeching va javobni qo'sh tengsizlik ko'rinishida yozing:
`|2x| ≤ 18`

<details>
<summary><b>Hint 1 (-5 HP)</b></summary>
`|a| ≤ b` qoidasi bo'yicha, ichkaridagi ifoda `-b` va `b` ning orasida yotadi.
</details>

<details>
<summary><b>Hint 2 (-5 HP)</b></summary>
`-18 ≤ 2x ≤ 18` deb yozing va tengsizlikning barcha qismlarini 2 ga bo'ling.
</details>

**Javob:** `-9 ≤ x ≤ 9`
**Failure Response:** Hali emas! `|2x| ≤ 18` bu `-18 ≤ 2x ≤ 18` degani. Endi o'rtada faqat `x` qolishi uchun barcha tomonlarni 2 ga bo'ling.

---

### 3-savol (Medium)
`[Bloom: L4 | PISA: L2 | Damage: -20 HP]`

**Vazifa:** Quyidagi son o'qida qoraytirilgan chiziq orqali biror oraliq ko'rsatilgan. 

<svg width="300" height="80" xmlns="http://www.w3.org/2000/svg">
  <line x1="10" y1="40" x2="290" y2="40" stroke="#2c3e50" stroke-width="2"/>
  <polygon points="290,40 280,35 280,45" fill="#2c3e50"/>
  <polygon points="10,40 20,35 20,45" fill="#2c3e50"/>
  
  <!-- Number line ticks -->
  <line x1="50" y1="35" x2="50" y2="45" stroke="#2c3e50" stroke-width="2"/>
  <text x="50" y="60" font-family="Arial" font-size="12" text-anchor="middle">-8</text>
  
  <line x1="150" y1="35" x2="150" y2="45" stroke="#2c3e50" stroke-width="2"/>
  <text x="150" y="60" font-family="Arial" font-size="12" text-anchor="middle">0</text>
  
  <line x1="250" y1="35" x2="250" y2="45" stroke="#2c3e50" stroke-width="2"/>
  <text x="250" y="60" font-family="Arial" font-size="12" text-anchor="middle">8</text>
  
  <!-- Highlighted region -->
  <line x1="50" y1="40" x2="250" y2="40" stroke="#e74c3c" stroke-width="6"/>
  <circle cx="50" cy="40" r="4" fill="#e74c3c"/>
  <circle cx="250" cy="40" r="4" fill="#e74c3c"/>
</svg>

Shu tasvirlangan oraliqni bitta **modulli tengsizlik** ko'rinishida yozing.

<details>
<summary><b>Hint 1 (-5 HP)</b></summary>
Chizma `-8` dan `8` gacha bo'lgan barcha sonlarni (ularni ham o'z ichiga olib) ko'rsatmoqda, ya'ni `-8 ≤ x ≤ 8`.
</details>

<details>
<summary><b>Hint 2 (-5 HP)</b></summary>
Buni modul belgisi `|x|` yordamida qanday qisqartirib yozish mumkin? Kichik yoki teng belgisi (`≤`) dan foydalaning.
</details>

**Javob:** `|x| ≤ 8`
**Failure Response:** Hali emas! Chizmada noldan har ikki tomonga 8 birlik qadamgacha ruxsat berilgani ko'rsatilgan. Ya'ni masofa 8 dan oshmasligi kerak. Modul orqali buni qanday yozishni o'ylab ko'ring.

---

### 4-savol (Medium)
`[Bloom: L4 | PISA: L3 | Damage: -20 HP]`

**Vazifa:** Siz avtomobil dvigatellarini yig'uvchi muhandissiz. Dvigatelning asosiy porshenining diametri standart bo'yicha 75 mm bo'lishi talab etiladi. Mashinadagi xatolik sababli porshenning diametri farqi (og'ishi) ko'pi bilan 0.2 mm gacha ruxsat etiladi. Porshenning real diametrini `d` deb belgilab, ushbu shartni ifodalovchi **modulli tengsizlik** tuzing. So'ngra `d` ning qabul qilishi mumkin bo'lgan eng kichik va eng katta o'lchamlarini (mm da) toping.

<details>
<summary><b>Hint 1 (-5 HP)</b></summary>
Farqni topish uchun `d` dan standartni (75 ni) ayiramiz va uning modulini olamiz: `|d - 75|`.
</details>

<details>
<summary><b>Hint 2 (-5 HP)</b></summary>
Bu farq 0.2 dan oshmasligi kerak. Demak, `|d - 75| ≤ 0.2`.
</details>

<details>
<summary><b>Hint 3 (-5 HP)</b></summary>
Endi bu tengsizlikni yeching: `-0.2 ≤ d - 75 ≤ 0.2`. Barcha qismlarga 75 qo'shing.
</details>

**Javob:** `|d - 75| ≤ 0.2`. Eng kichik o'lcham: 74.8 mm, Eng katta o'lcham: 75.2 mm.
**Failure Response:** Hali emas! Modulli tengsizlik tuzish uchun har doim `|real - standart| ≤ ruxsat_etilgan_farq` qolipidan foydalaning. Keyin bu qolipni yechib o'lchamlarni hisoblang.

---

### 5-savol (Hard)
`[Bloom: L5 | PISA: L4 | Damage: -30 HP]`

**Vazifa:** Siz zamonaviy tibbiyot laboratoriyasidasiz. Maxsus vaksinalar saqlanadigan muzlatkichning ideal harorati -20°C. Muzlatkich avtomatlashtirilgan bo'lib, agar ichki harorat `T` normadan roppa-rosa 3°C ga uzoqlashsa, tizim "Xavf Signali" ni chaladi. 
1. Tizim qachon signal chalishini bildiruvchi **modulli tenglama** tuzing.
2. Tenglamani yeching va ikkita haroratni (°C da) toping.
3. Yechimlaringiz amaliyotda nimani bildiradi? Javobingizni tushuntirib bering.

<details>
<summary><b>Hint 1 (-5 HP)</b></summary>
Tenglama tuzish qolipi: `|Real - Ideal| = Farq`. Ideal harorat manfiy: -20. Uni ayirganingizda nima bo'ladi?
</details>

<details>
<summary><b>Hint 2 (-5 HP)</b></summary>
Modulli tenglama: `|T - (-20)| = 3` ya'ni `|T + 20| = 3`.
</details>

<details>
<summary><b>Hint 3 (-5 HP)</b></summary>
Tenglamani yeching: `T + 20 = 3` va `T + 20 = -3`. Yechimlar signal chalish haroratlarini bildiradi.
</details>

**Javob:**
1. Modulli tenglama: `|T - (-20)| = 3` yoki `|T + 20| = 3`.
2. Yechilishi: `T + 20 = 3` -> `T = -17` °C. `T + 20 = -3` -> `T = -23` °C.
3. Amaliy ma'nosi: Agar muzlatkich harorati -17°C gacha isib ketsa yoki -23°C gacha sovib ketsa, harorat normadan chiqib ketgani sababli tizim xavf signalini chaladi.

**Failure Response:** Hali emas! Ehtiyot bo'ling, ideal harorat o'zi manfiy bo'lgani uchun modul ichida ayirganda ishora musbatga aylanadi (`T - (-20) = T + 20`). Modul qoidalari bilan qaytadan ishlab, yechimlarni fizika va hayotiy qoidalar orqali izohlang.