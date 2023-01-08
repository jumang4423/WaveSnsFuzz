import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

sites = ['soundcloud', 'twitter']

def trig_sc(driver):
    driver.find_element(By.CLASS_NAME, 'sc-button-follow').click()

def trig_twit(driver):
    driver.find_element(By.CLASS_NAME, 'css-18t94o4').click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'css-901oao').click()

print("site2fuzz (enter number):")
for i in range(len(sites)):
    print( i, sites[i])
site = sites[int(input())]

print("Duration of follow/unfollow (10min~60min): ")
DURATION_MIN = min(max(int(input()), 10) , 60)
print("Opening browser")
driver = webdriver.Chrome()

if site == 'soundcloud':
    print("Opening SoundCloud")
    driver.get('https://www.soundcloud.com/')
    print("sign in first, then press enter, waiting...")
    input()
    print("open profile page to fuzz, then press enter, waiting...")
    input()
    print("Starting fuzzing")
    session = 1
    while True:
        try:
            print("Session: " + str(session))
            trig_sc(driver)
            session += 1
            time.sleep(DURATION_MIN * 60)
        except Exception as e:
            print("follow or unfollow failed")
            print(e)
elif site == 'twitter':
    print("Opening twitter")
    driver.get('https://twitter.com/home')
    print("sign in first, then press enter, waiting...")
    input()
    print("open profile page to fuzz, then press enter, waiting...")
    input()
    print("Starting fuzzing")
    session = 1
    while True:
        try:
            print("Session: " + str(session))
            trig_twit(driver)
            session += 1
            time.sleep(DURATION_MIN * 60)
        except Exception as e:
            print("follow or unfollow failed")
            print(e)
else:
    print("site not implemented")
