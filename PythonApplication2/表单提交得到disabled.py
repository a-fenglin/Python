import urllib.parse
import urllib.request
data = bytes(urllib.parse.urlencode({'auth':'flag'}), encoding=
'UTF-8')
response = urllib.request.urlopen('http://111.198.29.45:51052/', data=data)
print(response.read().decode())
