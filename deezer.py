from selenium import webdriver
import requests
import time
import json
import ast
class LocalStorage:

    def __init__(self, driver) :
        self.driver = driver

    def __len__(self):
        return self.driver.execute_script("return window.localStorage.length;")

    def items(self) :
        return self.driver.execute_script( \
            "var ls = window.localStorage, items = {}; " \
            "for (var i = 0, k; i < ls.length; ++i) " \
            "  items[k = ls.key(i)] = ls.getItem(k); " \
            "return items; ")

    def keys(self) :
        return self.driver.execute_script( \
            "var ls = window.localStorage, keys = []; " \
            "for (var i = 0; i < ls.length; ++i) " \
            "  keys[i] = ls.key(i); " \
            "return keys; ")

    def get(self, key):
        return self.driver.execute_script("return window.localStorage.getItem(arguments[0]);", key)

    def set(self, key, value):
        self.driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", key, value)

    def has(self, key):
        return key in self.keys()

    def remove(self, key):
        self.driver.execute_script("window.localStorage.removeItem(arguments[0]);", key)

    def clear(self):
        self.driver.execute_script("window.localStorage.clear();")

    def __getitem__(self, key) :
        value = self.get(key)
        if value is None :
          raise KeyError(key)
        return value

    def __setitem__(self, key, value):
        self.set(key, value)

    def __contains__(self, key):
        return key in self.keys()

    def __iter__(self):
        return self.items().__iter__()

    def __repr__(self):
        return self.items().__str__()
# driver = webdriver.Chrome(r"C:\Users\dmohammed\Downloads\chromedriver_win32\chromedriver.exe") 
# url='https://www.deezer.com/login/email'
# driver.get(url)
# user = driver.find_element_by_id("login_mail")
# password = driver.find_element_by_id("login_password")
# user.send_keys("danspike@gmail.com")
# password.send_keys("F@m!ly40328")
# form = driver.find_element_by_id("login_form_submit")
# form.click()
# time.sleep(3)	
# st = LocalStorage(driver)
# print(st.get("cookies"))

payload = {"login_mail":"danspike@gmail.com", "login_password":"F@m!ly40328"}
with requests.Session() as s:
	p = s.post("https://www.deezer.com/login/email", data=payload)
	j = ""
	with open("postText.txt", "w") as pt:
		j = str(p.headers)
	js = ast.literal_eval(j)
	sid = js["Set-Cookie"].split(";")[0]
	cookie = sid.split("=")[1]
	print(cookie)