import os
import glob
import PIL
from PIL import Image
import cv2
import sklearn
from sklearn.cluster import KMeans

colors = []
files = glob.glob('./img/*.jpg')
# str_data = []
# f=0

#img_path→画像のパスを入力
def get_main_color_list_img(img_path):
    
# for f in files:
    # 画像ファイルの読み込み
    cv2_img = cv2.imread(img_path)
    # BGRからRGBに変換
    cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)

    cv2_img = cv2_img.reshape(
        (cv2_img.shape[0] * cv2_img.shape[1], 3))

    cluster = KMeans(n_clusters=5)
    # クラスタ化の対象となるデータ配列を指定してクラスタ化を実行させる、戻り値はない
    cluster.fit(X=cv2_img)
    # cluster_centers_ ---- クラスタの中心（セントロイド）の座標値の配列をint型で
    cluster_centers_arr = cluster.cluster_centers_.astype(
        int, copy=False)
        
    # IMG_SIZE = 64
    # MARGIN = 15
    # width = IMG_SIZE * 5 + MARGIN * 2
    # height = IMG_SIZE + MARGIN * 2

    # tiled_color_img = Image.new(
    #     mode='RGB', size=(width, height), color='#ffffff')

    for i, rgb_arr in enumerate(cluster_centers_arr):
        color_hex_str = '#%02x%02x%02x' % tuple(rgb_arr)
    #     color_img = Image.new(
    #         mode='RGB', size=(IMG_SIZE, IMG_SIZE),
    #         color=color_hex_str)
    #     tiled_color_img.paste(
    #         im=color_img,
    #         box=(MARGIN + IMG_SIZE * i, MARGIN))

        # colors.append(color_hex_str)
        # print(color_hex_str, end='   ')
        # colors.append(str(rgb_arr))

        colors.append(str(rgb_arr[0]))
        colors.append(str(rgb_arr[1]))
        colors.append(str(rgb_arr[2]))

        # print(rgb_arr, end='   ')
    # return tiled_color_img
    # color_data='\n'.join(colors)

    #1番目からfor文で入れていく
    str_data = colors[0]
    for i in range(1,len(colors)):
        if i%15==0:
            str_data += '\n' + colors[i]
        else:
            str_data += "," + colors[i]
        # if i%3==1 or i%3==2:
        #     str_data += "," + colors[i]
        # # b(3番目)のときは改行
        # else:
        #     str_data += '\n' + colors[i]
    # テキストデータに書き込み
    with open("rgb_data.txt",'w',encoding="utf-8") as fl:
        fl.write(str_data)



# def get_original_small_img(img_path):
#     img = Image.open(fp=img_path)
#     width = int(img.size[0] / 2)
#     height = int(img.size[1] / 2)
#     img = img.resize(size=(width, height))
#     return img

if __name__ == '__main__':
    with open("name_data.txt",'w',encoding="utf-8") as namefl:
        for f in files:
            get_main_color_list_img(f)
            namefl.write(os.path.split(f)[1]+'\n')
        