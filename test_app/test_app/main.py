# # import mouse

# # #上にスクロールする
# # mouse.wheel(1)

# # #下にスクロールする
# # mouse.wheel(-1)

# import pyautogui as pag

# #現在のマウスカーソル位置を取得
# m_posi_x, m_posi_y = pag.position()

# #スクロール
# pag.scroll(200,m_posi_x,m_posi_y)

# # # 左ボタンを押しながら、2秒かけて座標(100, 300)にマウスをドラッグ
# # pag.dragTo(100, 300, duration=2, button="left")
# # # 右ボタンを押しながら、3秒かけて右に50, 下に100の座標までマウスをドラッグ
# # pag.drag(50, 100, duration=3, button="right")

# # 0.5秒の間隔でenterという文字列を入力 (Enterキーは押されない)
# pag.write("enter", interval=0.5)

# # 下記の文章も約0.1秒で入力が終えます
# pag.write("It was created using the Python module pyautogui.")

import pyautogui

for i in range(10):
    # 2秒かけて現在のカーソルの位置から上に200移動
    pyautogui.move(0, -i, duration=i)
    pyautogui.moveTo(500, 600, duration=3)