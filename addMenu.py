import requests
import time
from threading import Timer
#from urllib.parse import quote
# from urllib import quote
#获取accessToken
f = open("error.txt", "a+")
def getAccessToken():
    t=Timer(3, getAccessToken)
    t.start()
    try:
        url='https://api.weixin.qq.com.qw/cgi-bin/menu/get?access_token=ACCESS_TOKEN'
        r = requests.get(url)
        rj = r.json()
        errorcode=rj['errcode']
        #print(rj['errcode'])
        #return rj['errcode']
    except BaseException as e:
        str=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        f.write(str+format(e)+"\r\n")
    else:
        pass
    finally:
        pass
#定时器

if __name__ == "__main__":
    getAccessToken()