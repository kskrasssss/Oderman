from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import Column, String, Integer, Text, ForeignKey

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__, template_folder='templates', static_folder="static")

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

