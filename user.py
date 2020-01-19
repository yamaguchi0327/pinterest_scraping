# 選択する色
r=218
g=90
b=120
user_color = [r,g,b]

# 画像の枚数
image_num = 2
# メインカラー3つ(rgb×3)×画像の枚数の配列
image_color =  [[0 for i in range(9)] for j in range(image_num)]

if __name__ == '__main__':
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
        # メインカラーを配列image_colorに代入
        for l in range(9):
            image_color[i][l] = int(rgb[l])
        # 3つごと(rgb)にfor文まわす
        for j in range(0,7,3):
            if r-20 < image_color[i][j] < r+20:
                print(i+1,'枚目の画像のrが一致！')
                if g-20 < image_color[i][j+1] < g+20:
                    print(i+1,'枚目の画像はgも一致！')
                    if b-20 < image_color[i][j+2] < b+20:
                        print(i+1,'枚目の画像は全部一致！')


    f.close()
    print(image_color)

    
