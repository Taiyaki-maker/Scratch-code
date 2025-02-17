# -*- coding: utf-8 -*-
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import time

# 価格の取得先
url = 'https://letus.ed.tus.ac.jp/login/index.php'

# 取得結果
current_value = ''

options = Options()
# ヘッドレスモードで実行する場合
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

try:
	# 取得先URLにアクセス
	driver.get(url)
	
	# コンテンツが描画されるまで待機
	time.sleep(10)

	# 対象を抽出
	values = driver.find_element_by_id("coinyep-reverse1")
	current_value = str(values.text)
finally:
	# プラウザを閉じる
	driver.quit()

# 取得結果
print(str(current_value))