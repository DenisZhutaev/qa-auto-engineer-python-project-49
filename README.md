# Brain Games

[![Actions Status](https://github.com/DenisZhutaev/qa-auto-engineer-python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/DenisZhutaev/qa-auto-engineer-python-project-49/actions)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=DenisZhutaev_qa-auto-engineer-python-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=DenisZhutaev_qa-auto-engineer-python-project-49)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=DenisZhutaev_qa-auto-engineer-python-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=DenisZhutaev_qa-auto-engineer-python-project-49)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=DenisZhutaev_qa-auto-engineer-python-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=DenisZhutaev_qa-auto-engineer-python-project-49)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=DenisZhutaev_qa-auto-engineer-python-project-49&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=DenisZhutaev_qa-auto-engineer-python-project-49)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=DenisZhutaev_qa-auto-engineer-python-project-49&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=DenisZhutaev_qa-auto-engineer-python-project-49)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=DenisZhutaev_qa-auto-engineer-python-project-49&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=DenisZhutaev_qa-auto-engineer-python-project-49)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=DenisZhutaev_qa-auto-engineer-python-project-49&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=DenisZhutaev_qa-auto-engineer-python-project-49)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=DenisZhutaev_qa-auto-engineer-python-project-49&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=DenisZhutaev_qa-auto-engineer-python-project-49)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=DenisZhutaev_qa-auto-engineer-python-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=DenisZhutaev_qa-auto-engineer-python-project-49)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=DenisZhutaev_qa-auto-engineer-python-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=DenisZhutaev_qa-auto-engineer-python-project-49)

Набор математических мини-игр для тренировки ума. Проверьте свои навыки в решении простых математических задач!

## Минимальные требования

- Python 3.12 или выше
- [UV](https://github.com/astral-sh/uv) - менеджер пакетов

## Установка

```bash
uv tool install dist/hexlet_code-0.7.0-py3-none-any.whl
```

## Запуск игр

После установки доступны следующие команды:

```bash
brain-games        # Приветствие
brain-even         # Проверка на чётность
brain-calc         # Калькулятор
brain-gcd          # Наибольший общий делитель
brain-progression  # Арифметическая прогрессия
brain-prime        # Простое ли число?
```

## Описание игр

### brain-even — Проверка на чётность

Показывается случайное число. Нужно ответить `yes`, если число чётное, или `no` — если нечётное.

```bash
$ brain-even
Welcome to the Brain Games!
May I have your name? Alex
Hello, Alex!
Answer "yes" if the number is even, otherwise answer "no".

Question: 15
Your answer: no
Correct!

Question: 6
Your answer: yes
Correct!

Question: 7
Your answer: no
Correct!
Congratulations, Alex!
```

### brain-calc — Калькулятор

Показывается случайное математическое выражение. Нужно вычислить результат.

```bash
$ brain-calc
Welcome to the Brain Games!
May I have your name? Alex
Hello, Alex!
What is the result of the expression?

Question: 4 + 10
Your answer: 14
Correct!

Question: 25 - 11
Your answer: 14
Correct!

Question: 25 * 7
Your answer: 175
Correct!
Congratulations, Alex!
```

### brain-gcd — Наибольший общий делитель

Показывается два случайных числа. Нужно найти их наибольший общий делитель.

```bash
$ brain-gcd
Welcome to the Brain Games!
May I have your name? Alex
Hello, Alex!
Find the greatest common divisor of given numbers.

Question: 25 10
Your answer: 5
Correct!

Question: 100 25
Your answer: 25
Correct!

Question: 16 28
Your answer: 4
Correct!
Congratulations, Alex!
```

### brain-progression — Арифметическая прогрессия

Показывается ряд чисел, который образует арифметическую прогрессию, с одним пропущенным числом. Нужно определить пропущенное число.

```bash
$ brain-progression
Welcome to the Brain Games!
May I have your name? Alex
Hello, Alex!
What number is missing in the progression?

Question: 5 7 9 11 13 .. 17 19 21 23
Your answer: 15
Correct!

Question: 2 5 8 .. 14 17 20 23 26 29
Your answer: 11
Correct!

Question: 14 19 24 29 34 39 44 49 54 ..
Your answer: 59
Correct!
Congratulations, Alex!
```

### brain-prime — Простое ли число?

Показывается случайное число. Нужно ответить `yes`, если число простое, или `no` — если нет.

```bash
$ brain-prime
Welcome to the Brain Games!
May I have your name? Alex
Hello, Alex!
Answer "yes" if given number is prime. Otherwise answer "no".

Question: 7
Your answer: yes
Correct!

Question: 4
Your answer: no
Correct!

Question: 13
Your answer: yes
Correct!
Congratulations, Alex!
```

## Демонстрация игр

Установка пакета и запуск игры brain-even:

[![asciicast](https://asciinema.org/a/QQXsWgLTauKGD47Akjgf7D2qz.svg)](https://asciinema.org/a/QQXsWgLTauKGD47Akjgf7D2qz)

Калькулятор — победа и поражение:

[![asciicast](https://asciinema.org/a/766427.svg)](https://asciinema.org/a/766427)

Наибольший общий делитель — победа и поражение:

[![asciicast](https://asciinema.org/a/766420.svg)](https://asciinema.org/a/766420)

Арифметическая прогрессия — победа и поражение:

[![asciicast](https://asciinema.org/a/766424.svg)](https://asciinema.org/a/766424)

Простое ли число? — победа и поражение:

[![asciicast](https://asciinema.org/a/766431.svg)](https://asciinema.org/a/766431)

## Разработка

### Установка зависимостей

```bash
make install
```

### Запуск линтера

```bash
make lint
```

### Сборка пакета

```bash
make build
```

### Установка пакета в систему

```bash
make package-install
```

### Запуск игр в режиме разработки

```bash
make brain-even
make brain-calc
make brain-gcd
make brain-progression
make brain-prime
```
