from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import csv
import io

driver = webdriver.Chrome(executable_path="C:\\webdriver\\chromedriver.exe")

outputFile = io.open('Marks.csv','w',newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow( ['Id','Name','FirstLang','SecLang','Thirdlang','Mathematics','Science','Social','Total Marks'])

# l = ["2323105322","2323105323","2323105324"]

for i in range(2323105294,2323105493):
    try:
        driver.get('https://bse.ap.gov.in/Resultsaprthrw/')
        driver.maximize_window()
        data = []
        driver.find_element(By.ID,"txtHallTicketNo").send_keys(str(i))
        driver.find_element(By.ID,"btnSubmit").click()
        data.append(str(i))
        data.append(driver.find_element(By.ID,"lblStudentName").text)
        data.append(driver.find_element(By.ID,"lblGrPointFirstLang").text)
        data.append(driver.find_element(By.ID,"lblGrPointSecLang").text)
        data.append(driver.find_element(By.ID,"lblGrPointThirdLang").text)
        data.append(driver.find_element(By.ID,"lblGrPointMath").text)
        data.append(driver.find_element(By.ID,"lblGrPointSci").text)
        data.append(driver.find_element(By.ID,"lblGrPointSoc").text)
        data.append(driver.find_element(By.ID,'lblTotal').text)
        outputWriter.writerow(data)
    except:
        data = []
        data.append(i)
        data.append("Invalid Hallticket No")
        outputWriter.writerow(data)

driver.close()
