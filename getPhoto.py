import pymysql
import os
import urllib

baseDir = "/Volumes/DATA/photo/"
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='sagacity',db='cloud_science',charset='utf8')
cursor = db.cursor()
sqlString = "select pb.nickname,ae.OrderCode,fee.FeeName,ae.intState enrollState" \
                ",ae.AddTime,af.name,af.tel,af.age,af.sex,af.nation,af.district,af.school,af.grade,af.classInfo,af.major,af.referName,af.referTel" \
                ",af.photoURL " \
                "from activity_enroll ae " \
                "left join activity_fee fee on fee.FeeID=ae.FeeID " \
                "left join activity_form af on af.EnrollID=ae.EnrollID " \
                "left join activity_baseinfo ab on ab.ActivityID=ae.ActivityID " \
                "left join profile_baseinfo pb on pb.openid=ae.openid " \
                "where ae.intState=2 and ae.AddTime>='2017-12-14' and ae.ActivityID=11"
cursor.execute(sqlString)

for row in cursor.fetchall():
    path = baseDir+row[5]
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        imgURL = row[17]
        # print imgURL
        urllib.urlretrieve(imgURL, path+"/"+row[1]+".jpg")
    else:
        print row[5]
db.close()