#! /usr/bin/env python3
# 
from PIL import Image,ImageDraw
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
    print ("<!DOCTYPE html>")
    print ("<link rel = \"stylesheet\" href = \"../stylesheet.css\">")


    # html_f = open('./top.html','w')
    # print('<html>',file=html_f)
    # print('<body>',file=html_f)
    # print('<table>',file=html_f)
    print ("<body>")

    print('<div class = "main-wrap">')
    print('<div class = "info-wrap">')
    print('<form method="POST">')
    print('<input type="text" name="r_num" placeholder="R">')
    print('<input type="text" name="g_num" placeholder="G">')
    print('<input type="text" name="b_num" placeholder="B">')
    print('<input type = "submit">')
    print('</form>')
    

    form = cgi.FieldStorage()
    r = int(form.getvalue('r_num',''))
    g = int(form.getvalue('g_num',''))
    b = int(form.getvalue('b_num',''))

    print('<div class = "color-box" style="background:rgb('+str(r)+', '+str(g)+', '+str(b)+')";>')
    print('</div>')
    print('</div class = "info-wrap">')
    # im = Image.new('RGB', (300, 300), (r, g, b))
    # d = ImageDraw.Draw(im)

    # print(r)
    # print(g)
    # print(b)

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
    print('<div class ="img-wrap">')
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

        
        # メインカラー(rgb)の一致を確認×5
        for j in range(0,15,3):
            if r-30 < image_color[i][j] < r+30:
                if g-30 < image_color[i][j+1] < g+30:
                    if b-30 < image_color[i][j+2] < b+30:
                        # img_dataのi行目を取得
                        target_line = linecache.getline('./name_data.txt', i+1)
                        # 画像のパス
                        file_path = '../img/'+ target_line
                        # 画像表示
                        print('<img src="'+file_path+'" alt="pic">')
    print('</div class ="img-wrap">')
    print('</div class = "main-wrap">')
    


    print('</body></html>')

    f.close()
    

    
