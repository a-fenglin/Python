from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError
username = 'username'
password = 'password'
url = 'http://ctf5.shiyanbar.com/web/jiandan/index.php'
p = HTTPPasswordMgrWithDefaultRealm()         #创建HTTPPasswordMgrWithDefaultRealm 对象
p.add_password(None, url, username, password)  #使用类中的函数add_password(…)
auth_handler = HTTPBasicAuthHandler(p)     #实例化了一个 HTTPBasicAuthHandler 对象,参数为#HTTPPasswordMgrWithDefaultRealm 对象
opener = build_opener(auth_handler)
try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)




