from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item

app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/catalog/JSON')
def catalogJSON():
    items = session.query(Item).all()
    return jsonify(items=[i.serialize for i in items])


# Show all restaurants
@app.route('/')
@app.route('/catalog/')
def showRestaurants():
    items = session.query(Item).all()
    # return "This page will show all my restaurants"
    return render_template('catalog.html', items=items)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
