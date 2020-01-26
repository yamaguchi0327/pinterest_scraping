
# scraping-img-1.py
 
import requests # urlを読み込むためrequestsをインポート
from bs4 import BeautifulSoup # htmlを読み込むためBeautifulSoupをインポート
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import os
import uuid
import time


# ブラウザーを起動
options = Options()
# options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)


# Selenium settings
# driver = webdriver.PhantomJS(service_log_path=os.path.devnull)
# get a HTML response


# 特定のサイトにアクセスする
driver.get('https://www.pinterest.jp/search/pins/?q=web%E3%83%87%E3%82%B6%E3%82%A4%E3%83%B3&rs=typed&term_meta[]=web%E3%83%87%E3%82%B6%E3%82%A4%E3%83%B3%7Ctyped')
html = driver.page_source.encode('utf-8')  # more sophisticated methods may be availabl

# URL = 'https://www.pinterest.jp/' # URL入力
images = [] # 画像リストの配列
 
# soup = BeautifulSoup(requests.get(URL).text,'lxml') # bsでURL内を解析
soup = BeautifulSoup(html,'lxml')

#ページの高さを取得
# height = driver.execute_script("return document.body.scrollHeight")
# print(height)
#最後までスクロールすると長いので、半分の長さに割る。
# height = height 

scroll_num = 0

for sc in range(1,19):

    # num = 0
    # with open("img_data.txt",'w',encoding='utf-8') as fl:
    for link in soup.find_all("img"): # imgタグを取得しlinkに格納
        
        if link.get("src").endswith(".jpg"): # imgタグ内の.jpgであるsrcタグを取得
            images.append(link.get("src")) # imagesリストに格納
            
            # fl.write(link.get("src")+'\n')
            
        # elif link.get("src").endswith(".png"): # imgタグ内の.pngであるsrcタグを取得
        #     images.append(link.get("src")) # imagesリストに格納
        #ループ処理で少しづつ移動
        # for x in range(1,height):
        #     driver.execute_script("window.scrollTo(10, "+str(x)+");")

    # scroll_x = 'window.scrollTo(0, '
    # scroll_num = num*500
    # scroll_x += str(scroll_num) + ');'
    # print(scroll_x)
    # driver.execute_script(scroll_x)
    # time.sleep(5)

    scroll_num+=3200

    
    html01=driver.page_source
    while 1:
        driver.execute_script("window.scrollBy(0, 3200)")
        time.sleep(3)
        html02=driver.page_source
        if html01!=html02:
            html01=html02
        else:
            break

    soup = BeautifulSoup(html02,'lxml')

                
 
for target in images: # imagesからtargetに入れる
    re = requests.get(target)
    with open('img/' + target.split('/')[-1], 'wb') as f: # imgフォルダに格納
        f.write(re.content) # .contentにて画像データとして書き込む
        # print(target)
 
print("ok") # 確認