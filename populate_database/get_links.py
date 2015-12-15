from get_pages import Page
import json

soup = Page().getSoup()
states = soup.select('ul.states a')
urls = {}

for state in states:
	soup = Page(state['href']).getSoup()
	state_name = state.getText().strip()
	site_urls = {}
	sites = soup.select('div.content a')
	sites.pop(0)
	for site in sites:
		site_urls[site.getText().strip()] = site['href']
	urls[state_name] = site_urls

with open('urls.json', 'w') as outfile:
    json.dump(urls, outfile)


