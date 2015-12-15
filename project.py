from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, and_, desc
from sqlalchemy.orm import sessionmaker
from living_wage_database_setup import Base, Location, Wages, Salaries
import json
import os

from flask.ext.triangle import Triangle

engine = create_engine(os.environ.get('DATABASE_URL'))
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

Triangle(app)

@app.route('/')
def doStuff():
	return render_template('places.html')

@app.route('/data', methods=['POST'])
def getData():
	choices = request.json
	wages, salary_1 = getattr(Wages, choices['f']), getattr(Salaries, choices['o1'])
	if len(choices) == 2:
		q = session.query(Location.site, Location.state, salary_1-wages).filter(and_(Wages.loc_id==Salaries.loc_id, Wages.loc_id==Location.id)).order_by(desc(salary_1-wages)).limit(20)
	else:
		salary_2 = getattr(Salaries, choices['o2'])
		q = session.query(Location.site, Location.state, salary_1+salary_2-wages).filter(and_(Wages.loc_id==Salaries.loc_id, Wages.loc_id==Location.id)).order_by(desc(salary_1+salary_2-wages)).limit(20)
	return json.dumps(map(lambda r: {'site':r[0],'state':r[1],'dollars':r[2]}, q))

app.secret_key = os.environ.get('SECRET_KEY')
app.debug = True