import requests
from bs4 import BeautifulSoup

class Page():
    """This class provides a way to get html pages from livingwage.mit.edu."""
    def __init__(self, ext=''):
        self.url = 'http://livingwage.mit.edu' + ext
    def getSoup(self):
		r = requests.get(self.url)
		content = r.content
		soup = BeautifulSoup(content)
		return soup