import requests
url="http://111.198.29.45:52703/cookie.php"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"

    }
data={
    "b":1
    }
r=requests.post(url=url,data=data,headers=headers)
print(r.content.decode()) 

 


