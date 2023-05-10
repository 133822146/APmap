import pandas as pd
import folium
import geocoder
import sys
args = sys.argv

locateName = args[1]

opendata_url = "https://www.opendata.metro.tokyo.lg.jp/suisyoudataset/130001_public_wireless_lan.csv"
# オープンデータのURLを表示
print("オープンデータのURL", opendata_url)

# pandasでURLをCSVデータとして読み込む
df = pd.read_csv(opendata_url, encoding="Shift-JIS")
#print(df)

lat = "緯度"
lon = "経度"
location = locateName
ret = geocoder.osm(location, timeout=5.0)
location = ret.latlng
# locationを入力した場所の緯度経度にする

# 地図の用意
map1 = folium.Map(
    # 初期位置をinputした場所にする
    location,
    # 拡大具合の設定
    zoom_start = 16,
    # 地図のスタイルの設定
    tiles =  "OpenStreetMap"
)

for i in range(len(df)):
    # プロットされる円の半径、色を設定
    folium.Circle(
        radius=50,
        location=[df.iloc[i][lat],df.iloc[i][lon]],
        color="green",
        fill=True,
        fill_color="lightgreen"
    ).add_to(map1)

map1.save("map.html")
