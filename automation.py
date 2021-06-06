from selenium import webdriver
import time
import random

driver = webdriver.Chrome()
minutes = 10
t_end = time.time() + 60 * minutes
while time.time() < t_end:
    rand = [3, 3.5, 4, 4.5, 5]
    x = random.choice(rand)
    driver.get('https://live.mrf.io/starmometer.com/index/widgets.mediaBlog.html?src=marfeel/PollDaddy.js&index=0&articleUri=https://starmometer.com/2021/05/29/100-asian-heartthrobs-2021-the-final-battle/&selector=.mrf-polldaddy')
    checkbox = driver.find_element_by_xpath('//*[@id="PDI_answer49988143"]')
    checkbox.click()
    time.sleep(x)

    vote = driver.find_element_by_xpath('//*[@id="pd-vote-button10844648"]')
    vote.click()
    time.sleep(x)
