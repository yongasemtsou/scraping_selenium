from openpyxl import Workbook
from plotly.express import pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[contains(@id,'search')]").send_keys("Samsung phones")
driver.find_element(By.XPATH,"//input[@value='Go']").click()
driver.find_element(By.XPATH,"//span[text()='Samsung']").click()
phonenames = driver.find_elements(By.XPATH,"//span[contains(@class,' a-color-base a-text-normal')]")
prices = driver.find_elements(By.XPATH,"//span[contains(@class,'price-whole')]")

myphone=[]
myprice=[]


for phone in phonenames:
    #print(phone.text)
    myphone.append(phone.text)

print("*"*50)

for price in prices:
    #print(price.text)
    myprice.append(price.text)

finallist =zip(myphone,myprice)

for data in list(finallist):
    print(data)


wb=Workbook()
sh1=wb.active

for x in list(finallist):
    sh1.append(x)


wb.save("finallRecord.csv")
wb.save("finallRecords.xlsx")

