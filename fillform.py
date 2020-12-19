from selenium import webdriver
import time

web=webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')
web.get('https://clickdimensions.com/form/default.html')

time.sleep(2)

FirstName='James'
first=web.find_element_by_xpath('//*[@id="txtFirstName"]')
first.send_keys(FirstName)
LastName='Bond'
last=web.find_element_by_xpath('//*[@id="txtLastName"]')
last.send_keys(LastName)
EmailID='james.bond@gmail.com'
email=web.find_element_by_xpath('//*[@id="txtFormEmail"]')
email.send_keys(EmailID)
CompanyName='JamesBond Ltd.'
company=web.find_element_by_xpath('//*[@id="txtCompany"]')
company.send_keys(CompanyName)
CityName='New York'
city=web.find_element_by_xpath('//*[@id="txtCity"]')
city.send_keys(CityName)
CountryName='United States of America'
country=web.find_element_by_xpath('//*[@id="optCountry"]')
country.send_keys(CountryName)
PhoneNumber='9911223344'
phone=web.find_element_by_xpath('//*[@id="txtPhone"]')
phone.send_keys(PhoneNumber)
QueryText='Where is my pet.'
query=web.find_element_by_xpath('//*[@id="txtComments"]')
query.send_keys(QueryText)
CheckBox=web.find_element_by_xpath('//*[@id="chkNewsletter"]')
CheckBox.click()
SubmitButton=web.find_element_by_xpath('//*[@id="frmWebCapture"]/table/tbody/tr[12]/td[2]/input')
SubmitButton.click()