# system_modelling_exam
Репозиторій створено для підготовки до екзамену. Щоб додати вас в репозиторій надішліть свій нік у github у телеграм @sideshowbobgot, вам буде надіслано інвайт.

Файлик з теорією:
https://docs.google.com/document/d/1J9PgJ8gsCiIVRJ52qbz6Bxt3Ns267uXiiDWepDRU1OY/edit?usp=sharing

Білети:
https://drive.google.com/drive/folders/16UmGtUQWvLWb6Frh81y27bA4LrsqrENx?usp=sharing

## Workflow виконання білета
1. Клонуєте репозиторій:
```bash
git clone https://github.com/SideShowBoBGOT/system_modelling_exam
```
2. Конвенція назви файлів: НОМЕРБІЛЕТА(ОЦІНКА АБО ВКАЗАНЕ ЯКЕ ЗАВДАННЯ НЕПРАВЛЬНЕ). Створюєте гілку з назвою у такому форматі РІК_НОМЕРБІЛЕТА_ГРУПА_ПРІЗВИЩЕ, наприклад:
```bash
git checkout -b 2025_7_ip11_panchenko
```
3. Створюєте відповідну папку та працюєте у ній:
```bash
mkdir 025_7_ip11_panchenko
```
4. Коли ви зробили завдання, запультеся та померджіться у main-гілку:
```bash
git pull origin main
git merge main
git checkout main
git merge 2025_7_ip11_panchenko
git push origin main
```
