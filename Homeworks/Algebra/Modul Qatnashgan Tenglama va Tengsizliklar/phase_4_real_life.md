Mode: HARD
Level: B1

# Phase 4: Real-Life Challenge

Siz "Afrosiyob" tezyurar poyezdlarini boshqarish markazida yetakchi muhandissiz (engineer). Poyezd xavfsiz va aniq harakatlanishi uchun tezlik va harorat datchiklari (sensorlari) ma'lumotlarini kuzatib borishingiz kerak. Poyezdning ma'lum bir tekis hududdagi standart tezligi 200 km/soat etib belgilangan. Xavfsizlik qoidalariga ko'ra, poyezd tezligi standartdan ko'pi bilan 15 km/soatga farq qilishi (og'ishi) mumkin. 

Shuningdek, poyezd dvigatelining ideal ishlash harorati 85°C. Agar dvigatel harorati ideal haroratdan roppa-rosa 5°C ga farq qilsa, boshqaruv panelida ogohlantirish signali chalinishi tizimga kiritilgan. Sizning vazifangiz datchiklardan kelayotgan bu farqlarni matematik formulalar orqali aniq ifodalash va xavfsizlik oraliqlarini hisoblashdir.

<svg width="300" height="150" xmlns="http://www.w3.org/2000/svg">
  <rect x="10" y="10" width="280" height="130" fill="#ecf0f1" stroke="#34495e" stroke-width="2" rx="8"/>
  <text x="150" y="30" font-family="Arial" font-weight="bold" font-size="14" fill="#2c3e50" text-anchor="middle">Afrosiyob Nazorat Paneli</text>
  <line x1="20" y1="40" x2="280" y2="40" stroke="#34495e" stroke-width="1"/>
  <rect x="25" y="55" width="110" height="60" fill="#3498db" rx="4"/>
  <text x="80" y="75" font-family="Arial" font-size="12" fill="#fff" text-anchor="middle">Standart Tezlik</text>
  <text x="80" y="100" font-family="Arial" font-weight="bold" font-size="16" fill="#fff" text-anchor="middle">200 km/s</text>
  
  <rect x="165" y="55" width="110" height="60" fill="#e67e22" rx="4"/>
  <text x="220" y="75" font-family="Arial" font-size="12" fill="#fff" text-anchor="middle">Ideal Harorat</text>
  <text x="220" y="100" font-family="Arial" font-weight="bold" font-size="16" fill="#fff" text-anchor="middle">85 °C</text>
</svg>

**Muammoni tahlil qilish (W5H):**
- **Kim?** Siz, yetakchi muhandis.
- **Nima?** Poyezd tezligi va dvigatel haroratining o'zgarishini modul yordamida hisoblash.
- **Qayerda?** "Afrosiyob" boshqaruv markazida.
- **Nima uchun?** Xavfsizlik qoidalarini ta'minlash va ogohlantirish signallarini sozlash uchun.

---

### Challenge Questions

*(Eslatma: Har bir hisoblash bosqichini daftaringizga yozing va tizimga rasmga tushirib yuklang — Notebook Capture).*

**1-savol.** Poyezdning ruxsat etilgan tezligi `v` ni topish uchun, uning standart tezlikdan farqi 15 km/soatdan oshmasligini ko'rsatuvchi modulli tengsizlik tuzing va uni yeching. Poyezdning eng kichik va eng katta ruxsat etilgan tezligini (km/soat) toping.
`[Bloom: L3 | PISA: L2]`

**Javob:**
Modulli tengsizlik: `|v - 200| ≤ 15`. 
Yechilishi: `-15 ≤ v - 200 ≤ 15` -> `185 ≤ v ≤ 215`. 
Eng kichik tezlik: 185 km/soat, Eng katta tezlik: 215 km/soat.

---

**2-savol.** Dvigatelning harorati `t` qanday ko'rsatkichlarga yetganda ogohlantirish signali chalinishini topish uchun modulli tenglama tuzing va uni yeching.
`[Bloom: L3 | PISA: L2]`

**Javob:**
Modulli tenglama: `|t - 85| = 5`.
Yechilishi:
1-holat: `t - 85 = 5` -> `t = 90` °C.
2-holat: `t - 85 = -5` -> `t = 80` °C.
Signal 80 °C va 90 °C da chalinadi.

---

**3-savol.** (Chamalab tekshiring) Yangi yordamchi muhandis shunday dedi: "Agar poyezd tezligi 212 km/soat bo'lsa, xavfsizlik qoidasi buzilmaydi." Uning fikrini 1-savolda tuzgan modulli tengsizligingizga qoyib tekshiring. Bu fikr to'g'rimi?
`[Bloom: L4 | PISA: L3]`

**Javob:**
Tengsizlikka qo'yamiz: `|212 - 200| ≤ 15` -> `|12| ≤ 15` -> `12 ≤ 15`. 
Bu tasdiq to'g'ri. 12 soni 15 dan kichik, shuning uchun tezlik xavfsizlik oraliqida yotadi. Yordamchi muhandisning fikri to'g'ri.

---

**4-savol.** Datchiklardan birida xatolik yuz berib tizimga `|t - 85| = -2` degan ma'lumot kelib tushdi. Bu tenglamaning matematik yechimi bormi va bu amaliyotda (kompyuter tizimida) nimani anglatadi?
`[Bloom: L4 | PISA: L3]`

**Javob:**
Matematik yechimi yo'q, chunki modul (masofa va farq) hech qachon manfiy songa teng bo'lmaydi. Amaliyotda bu kompyuter datchigi yoki dasturida xatolik (bug) borligini, datchik noto'g'ri ishlaganini anglatadi.

---

**5-savol.** (Qo'shimcha vaziyat) Agar qoidalar keskin o'zgarib, poyezd tezligi faqat roppa-rosa 200 km/soat bo'lishi talab qilinsa (hech qanday farqqa ruxsat berilmasa), buni modulli tenglama orqali qanday yozasiz va yechim nima bo'ladi?
`[Bloom: L4 | PISA: L3]`

**Javob:**
Modulli tenglama: `|v - 200| = 0`.
Yechilishi: `v - 200 = 0` -> `v = 200` km/soat. (Faqat bitta yechimga ega bo'ladi).
