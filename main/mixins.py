from django.conf import settings
from django.shortcuts import redirect
from urllib.parse import urlencode
import requests
import json



'''
Used to append url parameters when redirecting users
'''
def RedirectParams(**kwargs):
	url = kwargs.get("url")
	params = kwargs.get("params")
	response = redirect(url)
	if params:
		query_string = urlencode(params)
		response['Location'] += '?' + query_string
	return response


class APIMixin:

	def __init__(self, *args, **kwargs):

		self.cat = kwargs.get("cat")

	def get_data(self):


		url = f'https://api.chucknorris.io/jokes/random?category={self.cat}'

		r = requests.get(url)
		if r.status_code == 200:

			return {"text" : r.json()["value"], 'image': r.json()["icon_url"]}

		return None



