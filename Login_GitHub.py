from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import time
from tkinter import *
from tkinter import ttk

window = Tk()
window.title('Login GitGub')
window.geometry('200x200')
window.resizable(False,False)

Label(window,text='GitHub',font=('Bold',20)).pack()

text1 = StringVar()

Label(window,text='Username,Email').pack(pady=5)
e1 = Entry(window,textvariable=text1)
e1.pack()

text2 = StringVar()

Label(window,text='password').pack(pady=5)
e2 = Entry(window,textvariable=text2)
e2.pack()




def all():
    os.environ['PATH'] = r'chromedriver'
    chrome_options = Options() 
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://google.com/')
    search = driver.find_element(By.CLASS_NAME,'gLFyf')
    search.send_keys("GitHub Login", Keys.ENTER)
    Login_Page = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/a/h3')
    Login_Page.click()
    user_name = driver.find_element(By.ID, 'login_field')
    user_name.send_keys(text1.get())
    pass_word = driver.find_element(By.ID, 'password')
    pass_word.send_keys(text2.get())
    commit = driver.find_element(By.NAME, 'commit')
    commit.click()



btn = ttk.Button(window,text='Login!',command=all)
btn.pack(pady=5)

window.mainloop()