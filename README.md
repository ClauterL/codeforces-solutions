# codeforces-solutions

Codeforces-ratkaisut Pythonilla. Tili: [claikku](https://codeforces.com/profile/claikku).
Lähetyskieli Codeforcesissa: **PyPy 3.10 (64bit)**.

## Rakenne

```
solutions/<rating>/<contestId><index>.py   # yksi tiedosto per tehtävä
template.py                                # pohja uudelle ratkaisulle
scripts/run.py                             # aja ratkaisu stdin-syötteellä
scripts/new.py                             # luo uusi ratkaisu templatesta
```

Ajo: `echo "8" | python scripts/run.py 800/4A` → `YES`

## Ratkaistut tehtävät

Tila 3.10.2026: **50 tehtävää, kaikki Accepted ensimmäisellä lähetyksellä.**

### 800

| Tehtävä | Tekniikka |
| --- | --- |
| [4A Watermelon](https://codeforces.com/problemset/problem/4/A) | parillisuus, reunatapaus w=2 |
| [71A Way Too Long Words](https://codeforces.com/problemset/problem/71/A) | merkkijono |
| [231A Team](https://codeforces.com/problemset/problem/231/A) | laskeminen |
| [50A Domino piling](https://codeforces.com/problemset/problem/50/A) | matematiikka |
| [158A Next Round](https://codeforces.com/problemset/problem/158/A) | laskeminen |
| [282A Bit++](https://codeforces.com/problemset/problem/282/A) | simulaatio |
| [263A Beautiful Matrix](https://codeforces.com/problemset/problem/263/A) | Manhattan-etäisyys |
| [112A Petya and Strings](https://codeforces.com/problemset/problem/112/A) | merkkijono |
| [339A Helpful Maths](https://codeforces.com/problemset/problem/339/A) | lajittelu |
| [266A Stones on the Table](https://codeforces.com/problemset/problem/266/A) | vierekkäiset parit |
| [236A Boy or Girl](https://codeforces.com/problemset/problem/236/A) | joukko |
| [281A Word Capitalization](https://codeforces.com/problemset/problem/281/A) | merkkijono |
| [791A Bear and Big Brother](https://codeforces.com/problemset/problem/791/A) | simulaatio |
| [617A Elephant](https://codeforces.com/problemset/problem/617/A) | kattotasoitus |
| [546A Soldier and Bananas](https://codeforces.com/problemset/problem/546/A) | aritmeettinen summa |
| [59A Word](https://codeforces.com/problemset/problem/59/A) | laskeminen |
| [977A Wrong Subtraction](https://codeforces.com/problemset/problem/977/A) | simulaatio |
| [110A Nearly Lucky Number](https://codeforces.com/problemset/problem/110/A) | laskeminen |
| [734A Anton and Danik](https://codeforces.com/problemset/problem/734/A) | laskeminen |
| [41A Translation](https://codeforces.com/problemset/problem/41/A) | merkkijono |

### 900

| Tehtävä | Tekniikka |
| --- | --- |
| [96A Football](https://codeforces.com/problemset/problem/96/A) | osamerkkijono |
| [160A Twins](https://codeforces.com/problemset/problem/160/A) | lajittelu + ahne |
| [318A Even Odds](https://codeforces.com/problemset/problem/318/A) | kaava, n ≤ 10¹² |
| [405A Gravity Flip](https://codeforces.com/problemset/problem/405/A) | lajittelu |
| [133A HQ9+](https://codeforces.com/problemset/problem/133/A) | havainto |
| [580A Kefa and First Steps](https://codeforces.com/problemset/problem/580/A) | pisin ei-vähenevä pätkä |
| [208A Dubstep](https://codeforces.com/problemset/problem/208/A) | merkkijono |
| [337A Puzzles](https://codeforces.com/problemset/problem/337/A) | lajittelu + liukuva ikkuna |
| [1475A Odd Divisor](https://codeforces.com/problemset/problem/1475/A) | bittitemppu, 2:n potenssi |
| [451A Game With Sticks](https://codeforces.com/problemset/problem/451/A) | peliteoria |
| [1374B Multiply by 2, divide by 6](https://codeforces.com/problemset/problem/1374/B) | tekijöihin jako |
| [34B Sale](https://codeforces.com/problemset/problem/34/B) | lajittelu + ahne |
| [313A Ilya and Bank Account](https://codeforces.com/problemset/problem/313/A) | merkkijono |
| [1878C Vasilije in Cacak](https://codeforces.com/problemset/problem/1878/C) | summan ala- ja yläraja |
| [474A Keyboard](https://codeforces.com/problemset/problem/474/A) | taulukkohaku |

### 1000

| Tehtävä | Tekniikka |
| --- | --- |
| [1A Theatre Square](https://codeforces.com/problemset/problem/1/A) | kattotasoitus |
| [118A String Task](https://codeforces.com/problemset/problem/118/A) | merkkijono |
| [69A Young Physicist](https://codeforces.com/problemset/problem/69/A) | sarakesummat |
| [58A Chat room](https://codeforces.com/problemset/problem/58/A) | osajono, kaksi osoitinta |
| [122A Lucky Division](https://codeforces.com/problemset/problem/122/A) | brute force |
| [479A Expression](https://codeforces.com/problemset/problem/479/A) | brute force |
| [131A cAPS lOCK](https://codeforces.com/problemset/problem/131/A) | merkkijono, reunatapaus |
| [230A Dragons](https://codeforces.com/problemset/problem/230/A) | lajittelu + ahne |
| [339B Xenia and Ringroad](https://codeforces.com/problemset/problem/339/B) | modulo |
| [579A Raising Bacteria](https://codeforces.com/problemset/problem/579/A) | popcount |

### 1200

| Tehtävä | Tekniikka |
| --- | --- |
| [492B Vanya and Lanterns](https://codeforces.com/problemset/problem/492/B) | lajittelu + reunat |
| [466A Cheap Travel](https://codeforces.com/problemset/problem/466/A) | tapausjako |
| [514A Chewbacca and Number](https://codeforces.com/problemset/problem/514/A) | ahne + reunaehto |
| [1352C K-th Not Divisible by n](https://codeforces.com/problemset/problem/1352/C) | suljettu kaava |
| [474B Worms](https://codeforces.com/problemset/problem/474/B) | prefix-summa + binäärihaku |

## Käytännöt

- Monta testitapausta: `sys.stdin.read().split()` kerralla ja yksi `print("\n".join(...))`.
- Suuret syötteet: `sys.stdin.buffer.read()`.
- Pythonin kokonaisluvut eivät ylivuoda – C++:n `long long` -murheita ei ole.
