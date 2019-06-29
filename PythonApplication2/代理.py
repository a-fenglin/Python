from urllib import request,parse
url = "http://111.198.29.45:54674/"
headers = {
    #伪装一个火狐浏览器
  "User-Agent":'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    "host":'123.123.123.123'
}
dict = {
    "name":"Germey"
}
data = bytes(parse.urlencode(dict),encoding="utf8")
req =request.Request(url=url,data=data,headers=headers)
response = request.urlopen(req)
print(response.read().decode("utf-8"))


