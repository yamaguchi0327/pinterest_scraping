#! /usr/bin/env python3
# 
from PIL import Image
# ファイルから指定行のみをプログラム中で取り出す
import linecache 
import os
import cgi

# 選択する色
# r=40
# g=49
# b=54
# user_color = [r,g,b]

# 画像の枚数
image_num = 266
# メインカラー3つ(rgb×3)×画像の枚数の配列
image_color =  [[0 for i in range(15)] for j in range(image_num)]

if __name__ == '__main__':

    print('Content-Type: text/html; charset=UTF-8\n')

    # html_f = open('./top.html','w')
    # print('<html>',file=html_f)
    # print('<body>',file=html_f)
    # print('<table>',file=html_f)

    # print('<form method="POST">')
    # print('<input type="text" name="r">')
    # print('<input type="text" name="g">')
    # print('<input type="text" name="b">')
    # print('<input type = "submit>')
    # print('</form>')

    

    print ("<html><body>")

    form = cgi.FieldStorage()
    r = int(form.getvalue('r_num',''))
    g = int(form.getvalue('g_num',''))
    b = int(form.getvalue('b_num',''))

    print(r)
    print(g)
    print(b)

    # form_ok = 0

    # if form.has_key("r_num") and form.has_key("g_num") :
    #     form_check = 1
    # if form_check == 0 :
    #     print ("<h1>ERROR !</h1>")
    # else :
    #     print ("<h2>PRINT</h2><hr>")
    #     print ("<b>name: </b>", form["r_num"].value)
    #     print ("<b>mail: </b>", form["g_num"].value)
    #     print ("<b>mail: </b>", form["b_num"].value)
    

    # if form.has_key("r_num") and form.has_key("g_num") and form.has_key("b_num"):
    #     form_ok = 1
    #     print ("<p><b>name: </b>", form["r_num"].value)
    #     print ("<p><b>addr: </b>", form["g_num"].value)
    #     print ("<p><b>addr: </b>", form["b_num"].value)


    # rgbを書き込んだテキストデータを開く
    f = open('./rgb_data.txt','r')
    # １行読み込む
    line = f.readline()
    # 画像１枚に対しての処理
    for  i in range(0,image_num):
        # 改行とか余白を消す
        s = line.strip()
        # カンマで3つに区切ってリストにする
        rgb = s.split(",")
        # 次の行を読み込む
        line = f.readline()
        # i枚目のメインカラーを配列image_colorに代入
        for l in range(15):
            image_color[i][l] = int(rgb[l])
        # 3つごと(rgb)にfor文まわす
        for j in range(0,15,3):
            if r-10 < image_color[i][j] < r+10:
                # print(i+1,'枚目の画像のrが一致！')
                if g-10 < image_color[i][j+1] < g+10:
                    # print(i+1,'枚目の画像はgも一致！')
                    if b-10 < image_color[i][j+2] < b+10:
                        print(i+1,'枚目の画像が一致！')
                        # img_dataのi行目を取得
                        target_line = linecache.getline('./name_data.txt', i+1)
                        file_path = '../img/'+ target_line
                        print('<img src="'+file_path+'" alt="pic">')


    print('</body></html>')

    f.close()
    

    
