# -- coding: utf-8 --
from qiniu import Auth, put_file
from sys import argv
import os

def upload():
    # 需要填写你的 Access Key 和 Secret Key
    access_key = 'NwsBONsRlNexKJcvlD32d2LK63dJgyKFKuCDU9eB'
    secret_key = 'q5l2A_amklbuM7Bw3T-ewvwoB7FyedkX6gDEeuTX'
    # #构建鉴权对象
    q = Auth(access_key, secret_key)
    #要上传的空间
    bucket_name = 'sagacity'
    base_url = 'http://resource-sagacity.linestorm.ltd/'
    path = 'img/'
    urls = list()

    token = q.upload_token(bucket_name)
    #要上传文件列表
    for f in argv[1:]:
        if not (os.path.exists(f)):
            print ('文件不存在！')
            exit(-2)
        #上传后保存的文件名
        key = path + f.split("/")[-1]
        # 生成上传 Token，可以指定过期时间等
        ret, info = put_file(token, key, f)
        if (ret == None):
            print ("上传失败！")
            exit(-1)
        else:
            urls.append(base_url + ret['key'])

    print('Upload Success:')
    for url in urls: print(url)

if __name__ == "__main__":
    if len(argv) < 2:
        print("参数错误！")
    else:
        upload()