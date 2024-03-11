from requests import get
from pprint import pprint

pprint(get('http://localhost:5000/api/users').json())