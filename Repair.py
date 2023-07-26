# -*- coding:utf-8 -*-
import image
import requests,base64

def GetAccessToeken(APIKEY, SECRETKEY):
    token_host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={ak}&client_secret={sk}'.format(
      ak=APIKEY, sk=SECRETKEY)
    header = {'Content-Type': 'application/json; charset=UTF-8'}
    response = requests.post(url=token_host, headers=header)
    content = response.json()
    access_token = content.get("access_token")
    return access_token

def Reimg(img_path):
    APIKEY = 'qGYoG7U8gYQw62ldEY4buEmT'
    SECRETKEY = 'f6HfA9ciiQspFA08sVv7LhYjOoulAky1'
    # request_url = 'https://aip.baidubce.com/rest/2.0/image-process/v1/selfie_anime' # 人像动漫化
    # request_url = 'https://aip.baidubce.com/rest/2.0/image-process/v1/style_trans' # 画像风格转换
    request_url = ' https://aip.baidubce.com/rest/2.0/image-process/v1/colourize' # 黑白图像上色
    access_token = GetAccessToeken(APIKEY, SECRETKEY)
    picture1 = open(img_path,'rb')
    img_base1 = base64.b64encode(picture1.read()).decode()
    datamsg = {"image":img_base1}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=datamsg, headers=headers)
    
    if response:
        ans = response.json()
        imgData = base64.b64decode(ans['image'])
        leniyimg = open('./Repair1.jpg', 'wb')
        leniyimg.write(imgData)
        leniyimg.close()

if __name__ == '__main__':
   Reimg()