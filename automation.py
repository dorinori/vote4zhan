from selenium import webdriver
import time

driver = webdriver.Chrome()
for x in range (5):
    driver.get('https://live.mrf.io/starmometer.com/index/widgets.mediaBlog.html?src=marfeel/PollDaddy.js&index=0&articleUri=https://starmometer.com/2021/05/29/100-asian-heartthrobs-2021-the-final-battle/&selector=.mrf-polldaddy')
    checkbox = driver.find_element_by_xpath('//*[@id="PDI_answer49988143"]')
    checkbox.click()
    time.sleep(3)

    vote = driver.find_element_by_xpath('//*[@id="pd-vote-button10844648"]')
    vote.click()
    time.sleep(5)
