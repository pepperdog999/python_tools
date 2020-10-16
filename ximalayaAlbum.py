#coding=utf-8
import requests
import pymysql
import time
import traceback

headers= {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
proxy_addr= {
    'http': '140.143.48.49:1080'
}

def get_track_list(albumId):

    trackList =[]
    url = 'https://www.ximalaya.com/sets/'+str(albumId)+'.ext.json'
    # url ='https://www.ximalaya.com/revision/album/v1/getTracksList?albumId='+str(albumId)+'&pageNum='+str(pageNum)
    resp = requests.get(url, headers = headers, proxies = proxy_addr)
    result = resp.json()
    tracks = result['tracks']
    for track in tracks:
        trackList.append({'track_id': track['track_id'], 'title': track['title'], 'play_url': track['play_url']})
    return trackList

#显示数据内容
def show_track_data(track):
    title = track['title']
    url = track["play_url"]
    print("title:" + title)
    print("url:" + url)

#写入数据库
def save_track_db(courseId, track):
    title = track['title']
    url = track["play_url"]
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='sagacity', db='sagacity_course',
                         charset='utf8')

    cursor = db.cursor()

    sql1 = '''insert into course_lesson(PID,CourseID,LessonName,openState,level,viewCount,AddTime) 
        values(%s,%s,%s,%s,%s,%s,%s)'''
    sql2 = '''update course_lesson set `order`=LessonID where LessonID=%s'''
    sql3 = '''insert into course_lessondata(LessonID,CourseID,DataName,DataURL,DataType,AddTime)
        values(%s,%s,%s,%s,%s,%s)'''
    try:
        values = (int(0), int(courseId),track['title'],int(0),int(1),int(0),time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        cursor.execute(sql1, values)
        lessonId = int(cursor.lastrowid)
        cursor.execute(sql2, lessonId)
        values = (lessonId, int(courseId), track['title'], track['play_url'],'audio/x-mpeg',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        cursor.execute(sql3, values)
        db.commit()
    except:
        db.rollback()
        traceback.print_exc()
    db.close()

if __name__ == '__main__':
    courseId = 162
    albumId = 10091654

    track_list = get_track_list(albumId)
    # save_track_db(courseId, track_list[0])
    for track in track_list:
        show_track_data(track)
        # save_track_db(courseId, track)