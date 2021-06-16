import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)    #selecting web driver from PATH as the driver

ID = "6wl"                       # Imput the user ID to be checked

response = requests.get("https://api.github.com/users/"+ID)           # request to get data from AIP label data "response"
response_body = response.json()
url = "https://github.com/"+ID                     #creating the variable url as the website github/ the ID entered
driver.get(url)                                    #comand to open the webpage on the url


name0 = str(response_body["name"])                     #creating the variable name0, assigning it the string for name in the AIP response
name1 = driver.find_element_by_xpath('//*[@id="js-pjax-container"]/div[2]/div/div[1]/div/div[2]/div[2]/h1/span[1]').text      # used Xpath to assign name1 the text where the name is displayed in the browser

company0 = str(response_body["company"])#creating the variable company0, assigning it the string for company in the AIP response
try:
    company1 = driver.find_element_by_css_selector('#js-pjax-container > div.container-xl.px-3.px-md-4.px-lg-5 > div > div.flex-shrink-0.col-12.col-md-3.mb-4.mb-md-0 > div > div.d-flex.flex-column > div.js-profile-editable-area.d-flex.flex-column.d-md-block > ul > li:nth-child(1) > span > div').text        #trying to asign the company1 from the value from the browser using CSS selection
except:
    company1 = "None"     #if  class name can not be found in browser company1 is assigned None

location0 = str(response_body["location"]) #creating the variable location0, assigning it the string for location in the AIP response
try:
    location1 = driver.find_element_by_class_name("p-label").text   #trying to asign the location1 the value from the browser using the classname
except:
    location1 = "None"         #if  class name can not be found in browser location1 is assigned None


public_repos0 =str(response_body["public_repos"])               #creating the variable public_repos0, assigning it the string for public_repos in the AIP response
public_repos1 = driver.find_element_by_xpath('//*[@id="js-pjax-container"]/div[1]/div/div/div[2]/div/nav/a[2]/span').text       # used Xpath to assign public_repos1 the text where the name is displayed in the browser

followers0 = str(response_body["followers"])                ##creating the variable followers0, assigning it the string for followers in the AIP response
followers1 = driver.find_element_by_css_selector('#js-pjax-container > div.container-xl.px-3.px-md-4.px-lg-5 > div > div.flex-shrink-0.col-12.col-md-3.mb-4.mb-md-0 > div > div.d-flex.flex-column > div.js-profile-editable-area.d-flex.flex-column.d-md-block > div.flex-order-1.flex-md-order-none.mt-2.mt-md-0 > div > a:nth-child(1) > span').text
# used ccs selection to assign followers1 the text where the name is displayed in the browser

following0 = str(response_body["following"])   #creating the variable following0, assigning it the string for following in the AIP response
following1 = driver.find_element_by_css_selector('#js-pjax-container > div.container-xl.px-3.px-md-4.px-lg-5 > div > div.flex-shrink-0.col-12.col-md-3.mb-4.mb-md-0 > div > div.d-flex.flex-column > div.js-profile-editable-area.d-flex.flex-column.d-md-block > div.flex-order-1.flex-md-order-none.mt-2.mt-md-0 > div > a:nth-child(2) > span').text
# used ccs selection to assign following1 the text where the name is displayed in the browser


#if statements to check the values from the AIP (exaple0) match the values from the browser (example1)
if name0 == name1:
    print("names match")
else:
    print("names do not match. Name in API is",name0,"Name in the browser is",name1)

if company0 == company1:
    print("companies match")
else:
    print("companies do not match. company in API is",company0,"company in the browser is",company1)

if location0 == location1:
    print("locations match")
else:
    print("location do not match. location in API is",location0,"location in the browser is",location1)

if public_repos0 == public_repos1:
    print("public_repos match")
else:
    print("public_repos do not match. number of public repos in API is",public_repos0," number of public reposin the location is",public_repos1)

if followers0 == followers1:
    print("followers match")
else:
    print("followers do not match. followers in API is",followers0," followers the location is",followers1)

if following0 == following1:
    print("following match")
else:
    print("following do not match. followers in API is",following0," followers the location is",following1)