# 🍕 PizzaFlask — Menu, Voting & Weather Web App

## 🇬🇧 English

### Description
**PizzaFlask** is a simple web application built with Flask and SQLAlchemy. It allows users to:
- View a pizza menu
- Add new pizza entries through a form
- Vote for their favorite pizza in a poll
- View poll results and voting statistics
- Check the weather using the OpenWeatherMap API

### Features
- 🍕 Pizza Menu Page
- ➕ Add Pizza Form (stores in SQLite database)
- 📊 Voting Poll ("What pizza do you like the most?")
- 📈 Statistics Page (based on `data.txt` vote storage)
- 🌦️ Weather API integration (partially implemented)

### Technologies
- Python 3
- Flask
- SQLAlchemy
- HTML + Jinja2 Templates
- Bootstrap 5
- OpenWeatherMap API (planned)

### How to Run
1. Clone the repository:
   git clone https://github.com/kskrasssss/Oderman
   cd pizza-flask-app
2. Install dependencies (use venv if needed):
   pip install flask sqlalchemy requests
3. Replace `token` in `main.py` with your OpenWeatherMap API key.
4. Run the app:
   python main.py
5. Open your browser and go to `http://localhost:7000`

---

## 🇺🇦 Українською

### Опис
**PizzaFlask** — це проста вебпрограма на Flask і SQLAlchemy, яка дозволяє:
- Переглядати меню піц
- Додавати нові піци через форму
- Голосувати за улюблену піцу
- Переглядати результати голосування і статистику
- Отримувати погоду через OpenWeatherMap API

### Функції
- 🍕 Сторінка меню піц
- ➕ Форма додавання піци (збереження в SQLite)
- 📊 Голосування ("Яка піца найкраща?")
- 📈 Сторінка результатів (зчитування з `data.txt`)
- 🌦️ Інтеграція з API погоди (частково реалізовано)

### Технології
- Python 3
- Flask
- SQLAlchemy
- HTML + Jinja2
- Bootstrap 5
- OpenWeatherMap API (опціонально)

### Як запустити
1. Клонувати репозиторій:
   git clone https://github.com/kskrasssss/Oderman
   cd pizza-flask-app
2. Встановити залежності:
   pip install flask sqlalchemy requests
3. Замінити `token` у `main.py` на свій ключ OpenWeatherMap API.
4. Запустити програму:
   python main.py

5. Відкрити браузер і перейти на `http://localhost:7000`

---

## 📬 Feedback
If you find bugs or have suggestions, feel free to open an issue or contribute with a pull request.  
Якщо знайдете помилки або маєте пропозиції — створіть issue або зробіть pull request.
