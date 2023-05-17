from selenium import webdriver
from selenium.webdriver.common.by import By
import io
import os.path

driver = webdriver.Chrome(executable_path="C:\\webdriver\\chromedriver.exe")
with open("id.txt","r") as f:
    l = f.readlines()
    id = []
    for i in range(len(l)):
        id.append(l[i][:7])

save_photos = 'C:\\Users\\shahidaf\\Videos\\exp-py\\Photos\\'

for i in id:
    name = os.path.join(save_photos,i+".jpg")
    try:
        driver.get('http://210.212.217.214/r_1_sevenP7/'+i+'.jpg')
        with open(name,"wb") as file:
            file.write(driver.find_element(By.CSS_SELECTOR,"img[src='http://210.212.217.214/r_1_sevenP7/"+i+".jpg']").screenshot_as_png)
    except:
        pass

driver.close()
