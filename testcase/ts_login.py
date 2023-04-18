import requests,json
def login():
    url1 = "https://whyt-api.sj56.com.cn/ricciardo/WEB/v1/login"
    data1 = {"loginType":200,"userPassword":"OJxfI566iu0AIdgyIMmIu4awSQRqOwL5dGOgbmPSxM8DSlu+hMeQF93EpZSVWthTL6KXGjgO/jj691FBjRiUPI9H12yYrTDXYF4opPHWKIx+br5q3+XTzJu9EdikKySrI79jWbxROSt9Otju3gMyWtcbYvrtO1OhAORtG0dZazI=","userPhone":"18711043349"}
    r1 = requests.post(url=url1,json=data1)
    print(r1.json())
    xyheaders1 = r1.headers
    xyheaders2 = json.load(xyheaders1)
    print(xyheaders2)
    url2 = "https://whyt-api.sj56.com.cn/ricciardo/WEB/v1/selectStructureLogin"
    data2 = {"organizationalId":"1","userId":10006059}
    r2 = requests.post(url=url2,json=data2,headers=xyheaders)
    print(r2.json())
if __name__ == "__main__":
    login()
