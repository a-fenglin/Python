import http.cookiejar, urllib.request
filename = 'cookies1.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://111.198.29.45:52703')
cookie.save(ignore_discard=True, ignore_expires=True)
 

