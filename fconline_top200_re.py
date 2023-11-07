import selenium
import time
import random 
import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup 




options = webdriver.ChromeOptions()
#options.add_argument('--headless')        # Head-less 설정
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)


# 상위 200명 

url = "https://fconline.nexon.com/datacenter/playerstat"
driver.get(url)
time.sleep(3)



descending_button = driver.find_element(By.XPATH, '//*[@id="middle"]/div/div/div[3]/div/div[2]/div[1]/div/div[2]/div/a[1]')
descending_button.click()
time.sleep(5)

#데이터들
season_list = []
name_list = []
overall_list = []
price_list = []
id_list = []




#전체 리스트
player_list = []





#이미지 추출
image_class = driver.find_elements(By.CSS_SELECTOR, '.info_top .season') 
for each in image_class :
    image_element = each.find_element(By.TAG_NAME, 'img')
    image_src = image_element.get_attribute('src')
    image_src_list = image_src.split('/')
    class_name = image_src_list[-1].split('.')[0]
    season_list.append(class_name) 
#시즌 명단 출력 
for each in season_list :
    print(each)
#이름 추출
name_elements = driver.find_elements(By.CSS_SELECTOR, '.info_top .name')
for each in name_elements :
    name_list.append(each.text)
# 이름 명단 출력 
for each in name_list :
    print(each)



c_url = driver.current_url 

response = requests.get(url)
time.sleep(4)

soup = BeautifulSoup(response.text, 'html.parser')
info_top = soup.find('div', class_="info_top")




pid = info_top.find('input', type="hidden")
print(pid)
print('---------')
print(pid.text)












"""
# player_id 를 수집하기 bs4 로 하기 

c_url = driver.current_url 

response = requests.get(url)
time.sleep(4)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.text)

with open('soup.txt', 'w', encoding='UTF-8') as f :
    f.write(soup.text) 
d_plist = soup.find('div', class_='player_list')
hidden_input = d_plist.find('input', type = "hidden")
print(hidden_input.text)
"""






"""
<div class="info_top">
                    <div class="season"><img src="https://ssl.nexon.com/s2/game/fc/online/obt/externalAssets/season/LIVE.png" alt=""></div>
                    <div class="name">티보 쿠르투아</div>
                    <input type="hidden" name="Strong300192119" value="1/3">
                </div>
"""


"""
link  = player_detail.get_attribute('onclick')
driver.execute_script('window.open(" ");')
time.sleep(1) 
driver.switch_to.window(driver.window_handles[1]) 
driver.get(link) 
time.sleep(1.5) 
# 이동후 
# 오버롤
overall_element = driver.find_element(By.CLASS_NAME, 'ovr value')
overall_value = overall_element.text 
overall_list.append(overall_value) 
# 가격
price_element = driver.find_element(By.CSS_SELECTOR, '.add_info .txt')
price_text = price_element.text 
price_value = price_text.split('\n')[1].strip()
price_list.append(price_value) 
#탭 닫기 및 원래대로 이동 
driver.close() 
driver.switch_to.window(driver.window_handles[0])
time.sleep(1.4+random.random())
      
"""
      



#print('season_list :', len(season_list), 'name_list :', len(name_list))

#하나로 묶기
for i in range(0, len(season_list)) :
    name = name_list[i]
    season = season_list[i] 
    overall = overall_list[i]
    price = price_list[i] 

    p_list = [name, season, overall, price]
    player_list.append(p_list) 


print(player_list)

#텍스트 파일로 저장
with open('top200_player_list.txt', 'w', encoding='UTF-8') as f :
    for name in player_list :
        f.write(name[0]+" "+name[1]+"\n") 





