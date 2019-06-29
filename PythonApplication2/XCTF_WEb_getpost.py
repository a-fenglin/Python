import requests      #得先加载第三方库requests
import re
#headers = {
 #    "Content-Type": "application/x-www-form-urlencoded",
  #   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
#}
params={
    'a':1
    }
r = requests.get("http://111.198.29.45:57922/",params=params)  

print(r.content.decode())
#也可以在url上直接操作


