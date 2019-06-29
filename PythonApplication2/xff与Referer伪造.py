import random
import requests

ip_address = ['123.123.123.123']

headers = {
           #"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           #"Accept-Encoding": "gzip, deflate",
           #"Accept-Language": "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
           #"Connection": "keep-alive",
           "X-Forwarded-For": ip_address[random.randint(0, len(ip_address) - 1)],#伪造代理ip访问
           #"Host":"google.com",
           "Referer":"https://www.google.com",    #伪造Referer
           #"X-Forwarded-For":"123.123.123.123",
           #"Content-Length": "31",
           #"Content-Type": "application/x-www-form-urlencoded",
           "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

url = 'http://111.198.29.45:54674/'
html = requests.post(url=url,headers=headers)
print(html.content.decode())
'''
X-Forwarded-For:简称XFF头，它代表客户端，也就是HTTP的请求端真实的IP，
只有在通过了HTTP 代理或者负载均衡服务器时才会添加该项
HTTP Referer是header的一部分，当浏览器向web服务器发送请求的时候，
一般会带上Referer，告诉服务器我是从哪个页面链接过来的，服务器基此可以获得一些信息用于处理
'''