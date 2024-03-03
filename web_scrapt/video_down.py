import os
import json
import requests
from pathlib import Path
import pyautogui
import time
import xlrd
import pyperclip
import os
import random
import shutil
import urllib.parse
from bs4 import BeautifulSoup
from moviepy.editor import VideoFileClip
###################################以下是：模块
# 寻找图片是否出现
def zhao(img):
    for g in range(10):
        location = pyautogui.locateAllOnScreen(img, confidence=0.9)
        if len(list(location)) != 0:
            return True
        else:
            return False

# 删除目录下全部文件
def del_file(filepath):
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

# 下载图片
def xia_img(img_url, file_path, file_name):
    try:
        # 是否有这个路径
        if not os.path.exists(file_path):
            # 创建路径
            os.makedirs(file_path)
            # 获得图片后缀
        file_suffix = os.path.splitext(img_url)[1]
        print(file_suffix)
        # 拼接图片名（包含路径）
        filename = '{}{}{}{}'.format(file_path, os.sep, file_name, file_suffix)
        print(filename)
        # 下载图片，并保存到文件夹中
        urllib.request.urlretrieve(img_url, filename=filename)

    except IOError as e:
        print("IOError")
    except Exception as e:
        print("Exception")

# 获取文件夹下文件名
def wj_name(mp4_dir: Path):
    return [str(m) for m in mp4_dir.glob("*")][0]

# 点击图片
#   img 图片名，x偏移度，y偏移度
def click_img(img,i=0,x=0,y=0):
    for g in range(50):
        if zhao(img) == True:
            location = pyautogui.locateAllOnScreen(img, confidence=0.9)
            e = list(location)
            if i !=0 :
                print('e',e,'i:',i)
            pyautogui.click(list(e[i])[0]+x, list(e[i])[1]+y, clicks=1, interval=0.2, duration=0.2, button="left")
            break

# 合并视频
def merge_mp4(mp4_dir: Path, output_mp4=None):
    '''合并mp4
        使用ffmpeg拼接文件夹中的mp4视频
        :param mp4_dir: 存放mp4的文件夹
        :param output_mp4: 输出的mp4文件，若没有指定则使用文件夹的名字
        :return: None
    '''
    mp4_list = [str(m) for m in mp4_dir.glob("*.mp4")]
    #len(mp4_list)
    if output_mp4 is None:
        output_mp4 = mp4_dir / ("%s.mp4" % mp4_dir.stem)

    txt = ("file \'{}\'\n"*len(mp4_list)).format(*mp4_list)
    txt_file = mp4_dir / "video.txt"
    txt_file.write_text(txt)

    cmd = "ffmpeg -y -f concat -safe 0 -i %s -c copy %s" % (txt_file, output_mp4)
    print(cmd)
    os.system(cmd)

# bgm消音
def bgm_yin(mp4_dir: Path):
    cmd = r'ffmpeg -y -i %s -filter:a "volume=0.3" %s' % (mp4_dir, mp4_dir.parent / 'mp3_sc' / mp4_dir.name)
    print(cmd)
    os.system(cmd)

# 给视频加bgm————生成视频
def video_bgm(video: Path,bgm: Path,mp4_sc:Path):
    print(video)
    clip = VideoFileClip(str(video)).duration    #获取原视频时长
    cmd = r'ffmpeg -y -i %s -i %s -filter_complex [1:a]aloop=loop=-1:size=2e+09[out];[out][0:a]amix -ss 0 -t %s -y %s' % (video, bgm,clip,mp4_sc)
    print(cmd)
    os.system(cmd)
    os.system(r'ffmpeg -i %s-ss 00:00:02 -frames:v 1 %s' % (video, str(video).replace('mp4','png')))

# 视频mp3提取
def text_mp3(video: Path,mp3: Path):
    cmd = r'ffmpeg -i %s -f mp3 -vn %s' % (video,mp3)
    print(cmd)
    os.system(cmd)

#删除文件夹下全部文件
def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)







############################################以下是：代码部分
#搜索app介绍
def app_so_intro(u):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'
    }
    resp = requests.get(u, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    for k in soup.find_all('p', class_='intro'):  # ,string='更多'
        text = ''
        for i, t in enumerate(k.find_all(text=True)):
            if i != 0 and i != len(k.find_all(text=True))-1:
                text = text + t
        return(text)
    return('')

#酷安app点评
def app_ku_an_intro(pack):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'
        }
        resp = requests.get(r'https://www.coolapk.com/apk/'+ pack, headers=headers)
        soup = BeautifulSoup(resp.text, 'html.parser')
        for k in soup.find_all('p', class_='apk_left_title_info'):  # ,string='更多'
            text = ''
            for i, t in enumerate(k.find_all(text=True)):
                    text = text + t
            text = text.replace('android', '安卓')
            text = text.replace('Android', '安卓')
            text = text.replace('酷安', '小编')
            return (text)
        return ('')

#app介绍启动——主控制程序
def app_intro(u,pack):
    ku_an = app_ku_an_intro(pack)
    so_app = app_so_intro("http://s.downcc.com/pc/?cid=az&k="+ urllib.parse.quote(u))
    if so_app == '':
        so_app = app_so_intro('http://s.2265.com/pc/?cid=az&k='+ urllib.parse.quote(u))
    return ku_an + so_app

#生成标题
def biao_ti():
    bt1 = ['分享', '【软件推荐】', '【干货】', '【APP推荐】', '吐血分享：', '硬核！', '[干货满满]', '偷偷分享', '【硬核干货】']
    bt2 = ['几款', '几个', '6款', '六款', '6个', '六个', '一些']
    bt3 = ['实用', '超级实用', '直呼牛逼', '直呼卧槽', '逆天实用', '非常逆天', '手机必备', '必备手机', '稀缺良心', '元老级', '完全免费', '舍不得删', '颠覆三观', '冷门绝佳',
           '纯净', '必装']
    bt4 = ['宝藏', '小众', '良心', '小众神仙', '小众且实用', '高质量']
    bt5 = ['APP', '软件', '神器app', 'APP，每一款都值得收藏', '软件，每一款都值得收藏']
    for i, f in enumerate(['', '', '', '', '', '', '', '', '', '']):
        tx1 = bt1[random.randint(0, len(bt1) - 1)]
        tx2 = bt2[random.randint(0, len(bt2) - 1)]
        tx3 = bt3[random.randint(0, len(bt3) - 1)]
        tx4 = bt4[random.randint(0, len(bt4) - 1)]
        tx5 = bt5[random.randint(0, len(bt5) - 1)]

        return (tx1 + tx2 + tx3 + '的' + tx4 + tx5)

    return ('')





# 获取app资料
def get_cha(u):
    try:
        headers = {
            'User-Agent': 'iTunes/12.6.2 (Windows; Microsoft Windows 10.0 x64 Business Edition (Build 18362); x64) AppleWebKit/7603.3008.0.3'
        }
        req = urllib.request.Request(url=u, headers=headers)
        res = urllib.request.urlopen(req).read().decode('utf-8')
        return res
    except:
        print("Has tried times to access ur, all failed!" )
    return ''
def app_get(u):
    headers = {
        'User-Agent': 'iTunes/12.6.2 (Windows; Microsoft Windows 10.0 x64 Business Edition (Build 18362); x64) AppleWebKit/7603.3008.0.3'
    }
    req = urllib.request.Request(url=u, headers=headers)
    res = urllib.request.urlopen(req).read().decode('utf-8')
    return res

#下载素材启动
def go_dow_img(screenshot, icon):
    icon= "http://file.market.xiaomi.com/thumbnail/PNG/l300/" + icon
    jt = screenshot.split(',')
    fmg = ['8a5e3872bbe7f508d4b4746e349e014b.jpg', '106a8f82ed5a71e148bcde0ded492e03.jpg',
           '93a3807fb45223a897acc41a2fd234ad.jpg', '4fd71bb941864bd093da7971cd9d3f26.jpg',
           '4d42655db1ec1fd8cea49379e5459d56.jpg', 'cb2931a3279c7380d94064777a3d9fbd.jpg']
    jmg = ['', '', '', '', '', '']
    for i, f in enumerate(jt):
        img = 'http://file.market.xiaomi.com/thumbnail/jpeg/l800/' + f
        jmg[i] = img

    for i, f in enumerate(jt):
        img = 'http://file.market.xiaomi.com/thumbnail/jpeg/l800/' + f
        if len(jmg[0]) == 0:
            jmg[0] = img
        if len(jmg[1]) == 0:
            jmg[1] = img
        if len(jmg[2]) == 0:
            jmg[2] = img
        if len(jmg[3]) == 0:
            jmg[3] = img
        if len(jmg[4]) == 0:
            jmg[4] = img
        if len(jmg[5]) == 0:
            jmg[5] = img

    for i, f in enumerate(jmg):
        xia_img(jmg[i], r'C:/Users/aabb/Desktop/video/code/videos/', fmg[i])

    xia_img(icon, r'C:/Users/aabb/Desktop/video/code/videos/', 'cc9ef7d343324b3cbe47d904b95c33b3.jpg')

#控制剪映生成语音
def go_jianying_mp3():
    click_tmp3 = False
    click_text = False
    click_ld = False
    click_taiwan = False
    click_ksld = False
    os.startfile(r'C:\Users\aabb\AppData\Local\JianyingPro\Apps\JianyingPro.exe')  # 打开软件
    for a1 in range(500):
        if zhao('tmp3.png') == True:
            print('找到文本tmp3！')
            click_img('tmp3.png',0,0,0)
            click_tmp3 = True
            break

    if click_tmp3 == True:
        for a in range(20):
            if zhao('text.png') == True:
                print('找到文本text！')
                click_img('text.png', 0, 0, 10)
                click_text = True
                break

    if click_text == True:
        for a in range(20):
            if zhao('ld.jpg') == True:
                print('找到文本ld！')
                click_img('ld.jpg', 0, 0, 0)
                click_ld = True
                break


    if click_ld == True:
        for a in range(20):
            if zhao('taiwan.jpg') == True:
                print('找到文本taiwan！')
                click_img('taiwan.jpg', 0, 0, 0)
                click_taiwan=True
                break

    if click_taiwan == True:
        for a in range(20):
            if zhao('ksld.png') == True:
                print('找到文本ksld！')
                click_img('ksld.png', 0, 0, 0)
                click_ksld = True
                break

    if click_ksld == True:
        for a in range(900):
            if zhao('mp3_ok.jpg') == True:
                textReading = Path(r"C:\Users\aabb\AppData\Local\JianyingPro\User Data\Projects\com.lveditor.draft\mp3_jianying\textReading")
                mp3 = wj_name(textReading)
                print('找到文本mp3_ok！',mp3)
                return mp3
    return ''
#控制剪映生成视频
def go_jianying_mp4(i,h):
    click_app = False
    click_daochu = False
    click_name_code = False
    click_go_daochu = False
    click_ksld = False

    zpname = 'zp_name.png'
    app = 'app.png'
    if h == 0:
        zpname = 'zp_kaitou.png'
        app = 'kaitou.png'
    else:
        zpname = 'zp_name.png'
        app = 'app.png'


    os.startfile(r'C:\Users\aabb\AppData\Local\JianyingPro\Apps\JianyingPro.exe')  # 打开软件
    for a1 in range(500):
        if zhao(app) == True:
            print('找到文本'+app)
            click_img(app, 0, 30, -30)
            click_app = True
            break

    if click_app == True:
        for a in range(50):
            if zhao('daochu.png') == True:
                print('找到文本daochu！')
                click_img('daochu.png', 0, 0, 10)
                click_daochu = True
                break

    if click_daochu == True:
        for a in range(20):
            if zhao(zpname) == True:
                print('找到文本'+ zpname)
                click_img(zpname, 0, 100, 13)
                click_name_code = True
                time.sleep(2)
                if h == 0:
                    pyperclip.copy('00')
                else:
                    pyperclip.copy(i)
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.hotkey('Enter')
                break


    if click_name_code == True:
        for a in range(20):
            if zhao('go_daochu.png') == True:
                print('找到文本go_daochu！')
                click_img('go_daochu.png', 0, 30, 15)
                click_go_daochu=True
                break

    if click_go_daochu == True:
        for a in range(900):
            if zhao('daochu_ok.png') == True:
                print('找到文本daochu_ok！')
                os.system('%s%s' % ("taskkill /F /IM ", 'JianyingPro.exe'))  # 关闭程序
                return True
    return False

#json 文件修改
def wj_mp4_json(dir: Path,i,appname):
    data = json.load(open(dir,"r", encoding='UTF-8'))
    data["materials"]['texts'][2]['content'] = i
    data["materials"]['texts'][0]['content'] = appname
    data["materials"]['texts'][1]['content'] = appname
    json.dump(data,open(dir,"w", encoding='UTF-8'),indent=4)

#json 语音工程，文件修改
def wj_mp3_json(dir: Path,text):
    data = json.load(open(dir,"r", encoding='UTF-8'))
    data["materials"]['texts'][0]['content'] = text
    json.dump(data,open(dir,"w", encoding='UTF-8'),indent=4)



if __name__ == '__main__':
    for i, f in enumerate(['', '', '', '', '', '', '', '', '', '']):
        # 获取信息
        fmg = ['13B02E9A-6A39-493a-BFB0-C8FA70965616.png', '26C461AC-4107-4892-9C34-066ED2A36520.png','BBB2780C-A5DE-4b32-BA8F-DD71DACD6032.png', 'C9C41D65-C4AB-43d7-9794-546B2F526224.png','D8729FDC-40AA-49f3-9BF2-8BFEA7AB0744.png', 'FCB2316D-C3E1-483e-8C3A-627929DE8CA4.png']
        cha = get_cha("http://a.ewmtool.com/tp/index.php/Qun/appjsoncha")
        jsonbdb = json.loads(cha)
        for i, e in enumerate(jsonbdb['data']):
            t = json.loads(urllib.parse.unquote(e['text']))
            xia_img("http://file.market.xiaomi.com/thumbnail/PNG/l300/" + t['appInfo']['icon'], r'C:\Users\aabb\Desktop\video\code_kai_tou\materials\video', fmg[i])


        for i, e in enumerate(jsonbdb['data']):
            os.system('%s%s' % ("taskkill /F /IM ", 'JianyingPro.exe'))  # 关闭程序
            t = json.loads(urllib.parse.unquote(e['text']))
            id = e['ID']
            xu = '0'+str(i+1)  # 序号
            # app 介绍
            intro = t['appInfo']['displayName'] + 'App介绍' + app_intro(t['appInfo']['displayName'],t['appInfo']['packageName'])

            # ================================================
            # 开始，下载，图片素材
            go_dow_img(t['appInfo']['screenshot'], t['appInfo']['icon'])


            # 文件文本写入
            dir1 = Path(r"C:\Users\aabb\Desktop\video\code\draft_content.json")
            dir2 = Path(r"C:\Users\aabb\Desktop\video\mp3_jianying\draft_content.json")
            wj_mp4_json(dir1, xu, t['appInfo']['displayName'])
            wj_mp3_json(dir2, intro)

            if os.path.exists(r'C:\Users\aabb\AppData\Local\JianyingPro\User Data\Projects\com.lveditor.draft\mp3_jianying') == True:
                shutil.rmtree(r'C:\Users\aabb\AppData\Local\JianyingPro\User Data\Projects\com.lveditor.draft\mp3_jianying')  # 删除文件夹
            shutil.copytree(r'C:\Users\aabb\Desktop\video\mp3_jianying',r'C:\Users\aabb\AppData\Local\JianyingPro\User Data\Projects\com.lveditor.draft\mp3_jianying')  # 复制文件夹

            # 操控剪映，生成语音mp3
            mp3 = go_jianying_mp3()
            if mp3 != '':
                os.system('%s%s' % ("taskkill /F /IM ", 'JianyingPro.exe'))  # 关闭程序
                time.sleep(5)
                shutil.move(mp3, r'C:\Users\aabb\Desktop\video\code\audios\a91ca9abc7559f3eda6ef18009dec967.wav')

            if os.path.exists(r'C:\Users\aabb\AppData\Local\JianyingPro\User Data\Projects\com.lveditor.draft\code') == True:
                shutil.rmtree(r'C:\Users\aabb\AppData\Local\JianyingPro\User Data\Projects\com.lveditor.draft\code')  # 删除文件夹
            shutil.copytree(r'C:\Users\aabb\Desktop\video\code',r'C:\Users\aabb\AppData\Local\JianyingPro\User Data\Projects\com.lveditor.draft\code')  # 复制文件夹

            if os.path.exists(r'C:\Users\aabb\AppData\Local\JianyingPro\User Data\Projects\com.lveditor.draft\kai_tou') == True:
                shutil.rmtree(r'C:\Users\aabb\AppData\Local\JianyingPro\User Data\Projects\com.lveditor.draft\kai_tou')  # 删除文件夹
            shutil.copytree(r'C:\Users\aabb\Desktop\video\code_kai_tou',r'C:\Users\aabb\AppData\Local\JianyingPro\User Data\Projects\com.lveditor.draft\kai_tou')  # 复制文件夹


            # 操控剪映，生成视频
            if i == 0:
                mp4 = go_jianying_mp4(xu, i)
                time.sleep(3)
                mp4 = go_jianying_mp4(xu, i+1)
            else:
                mp4 = go_jianying_mp4(xu, i)

            if mp4 == True:
                print('生成成功')

            app_get(r'http://a.ewmtool.com/tp/index.php/Qun/appjsonchati?id='+str(id))

        #剪映视频合并
        jianying = Path(r"C:\Users\aabb\Videos")
        merge_mp4(jianying)
        time.sleep(3)
        #bgm消音
        #mp3 = Path(r"C:\Users\aabb\Desktop\video\mp3\1.m4a")
        #bgm_yin(mp3)

        #生成视频
        video = Path(r"C:\Users\aabb\Videos\Videos.mp4")
        bgm = Path(r"C:\Users\aabb\Desktop\video\mp3\mp3_sc\1.m4a")
        mp4_sc = Path(r"C:\Users\aabb\Desktop\video\video\\"+ biao_ti() +'_'+ str(random.randint(10000000,99999999))+".mp4")
        video_bgm(video,bgm,mp4_sc)
        time.sleep(10)
        os.system('%s%s' % ("taskkill /F /IM ", 'ffmpeg-win64-v4.2.2.exe'))  # 关闭程序
        del_file(r'C:\Users\aabb\Videos')#删除文件夹下全部文件

        time.sleep(3)
