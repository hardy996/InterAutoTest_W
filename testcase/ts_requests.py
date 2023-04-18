import requests
r = requests.get("http://www.baidu.com")
print(r)
print(r.status_code)
#print(r.json())
print(r.url)
print(r.text)
print(r.cookies)
