from get_pages import Page
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from living_wage_database_setup import Base, Location, Wages, Salaries
import os

engine = create_engine(os.environ.get('DATABASE_URL'))
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add(row):
	session.add(row)
	session.commit()

def addLocation(state, site, comma_index):
	if comma_index != -1:
		site = site[:comma_index]
	location = Location(state = state, site = site)
	add(location)
	return location.id

with open('urls.json') as j:

	urls = json.load(j)

	for state in urls:
		for site, url in urls[state].iteritems():
			loc_id = addLocation(state, site, site.find(','))
			soup = Page(url).getSoup()
			add(Wages(map(lambda w: int(w.getText().strip().replace('$','').replace(',','')), soup.select('.expenses_table td')[105:]), loc_id))
			add(Salaries(map(lambda s: int(s.getText().strip().replace('$','').replace(',','')), soup.select('.occupations_table td')[1::2]), loc_id))