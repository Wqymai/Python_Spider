import requests

r = requests.get('https://pypi.python.org/pypi/requests')
print r.status_code
print r.headers['content-type']
print r.encoding
