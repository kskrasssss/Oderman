from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import Column, String, Integer, Text, ForeignKey

from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__, template_folder='templates', static_folder="static")

API_KEY = 'token'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

# curl =  "http://api.openweathermap.org/data/2.5/weather?q=Kyiv&appid=your_api_key&units=metric"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    pizza = [
        {'name': 'Mozzarela', 'ingridients': 'cheese, basil, tomatoes', 'price': 120},
        {'name': 'Carbonara', 'ingridients': 'basil, eggs, Parmesan, Mozzarela', 'price': 75},
        {'name': 'Pepperoni', 'ingridients': 'salami, cream sauce, basil, tomatoes', 'price': 90},
        {'name': 'Four cheese', 'ingridients': 'Parmesan, Adyghe, Mozzarella, Dorblu', 'price': 110},
    ]

    context = {
        'pizza': pizza,
    }
    return render_template('menu.html', **context)

def weather():
    weather_data = None
    error = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            params = {
                'q': city,
                'appid': API_KEY,
                'units': 'metric'  
            }
            response = requests.get(BASE_URL, params=params)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                error = f"City '{city}' not found. Please try again."
    return render_template('menu.html', weather_data=weather_data, error=error)

engine = create_engine('sqlite:///alchemy_form.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Form(Base):
    __tablename__ = 'form'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    ingridients = Column(String(30))
    price = Column(Integer())

Base.metadata.create_all(engine)
Base.metadata.bind = engine

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        ingridients = request.form['ingridients']
        price = request.form['price']

        new_pizza = Form(name=name, ingridients=ingridients, price=int(price))
        session.add(new_pizza)
        session.commit()

        return redirect(url_for('form'))

    pizzas = session.query(Form).all()
    return render_template('form.html', pizzas=pizzas)

if __name__ == '__main__':
    app.run(port= 7000, debug=True)

