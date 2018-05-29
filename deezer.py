from seleniumrequests import Chrome
import requests
import time
import json
import ast
import subprocess
import os
# class LocalStorage:

#     def __init__(self, driver) :
#         self.driver = driver

#     def __len__(self):
#         return self.driver.execute_script("return window.localStorage.length;")

#     def items(self) :
#         return self.driver.execute_script( \
#             "var ls = window.localStorage, items = {}; " \
#             "for (var i = 0, k; i < ls.length; ++i) " \
#             "  items[k = ls.key(i)] = ls.getItem(k); " \
#             "return items; ")

#     def keys(self) :
#         return self.driver.execute_script( \
#             "var ls = window.localStorage, keys = []; " \
#             "for (var i = 0; i < ls.length; ++i) " \
#             "  keys[i] = ls.key(i); " \
#             "return keys; ")

#     def get(self, key):
#         return self.driver.execute_script("return window.localStorage.getItem(arguments[0]);", key)

#     def set(self, key, value):
#         self.driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", key, value)

#     def has(self, key):
#         return key in self.keys()

#     def remove(self, key):
#         self.driver.execute_script("window.localStorage.removeItem(arguments[0]);", key)

#     def clear(self):
#         self.driver.execute_script("window.localStorage.clear();")

#     def __getitem__(self, key) :
#         value = self.get(key)
#         if value is None :
#           raise KeyError(key)
#         return value

#     def __setitem__(self, key, value):
#         self.set(key, value)

#     def __contains__(self, key):
#         return key in self.keys()

#     def __iter__(self):
#         return self.items().__iter__()

#     def __repr__(self):
#         return self.items().__str__()
driver = Chrome(r"C:/Python/deezLoaderScript/chromedriver/chromedriver_win32/chromedriver.exe") 
payload = {"login_mail":"danspike@gmail.com", "login_password":"F@m!ly40328"}
pathToAPI = r"C:/Music/Deezloader-win32-x64/resources/app/deezer-api.js"
pathToDeezer = r"C:/Music/Deezloader-win32-x64/Deezloader.exe"
url='https://www.deezer.com/login/email'
driver.get(url)
user = driver.find_element_by_id("login_mail")
password = driver.find_element_by_id("login_password")
submit = driver.find_element_by_id("login_form_submit")
user.send_keys(payload["login_mail"])
password.send_keys(payload["login_password"])
submit.click()
r = driver.request("POST",url,data=payload)
j = str(r.headers)
js = ast.literal_eval(j)
sid = js["Set-Cookie"].split(";")[0]
print(sid)

changeStr = '\t\t"Cookie":"'+sid+'"'
lines = []
lineIndex = 0
with open(pathToAPI) as f:
	lines = f.read().splitlines()

for index, line in enumerate(lines):
	if "Cookie" in line:
		lineIndex = index
lines[lineIndex] = changeStr
with open(pathToAPI, "w") as f:
	f.write("\n".join(lines))
p = subprocess.Popen(pathToDeezer)
p.wait()

# pathToDeezer = r"/mnt/c/Music/Deezloader-win32-x64/Deezloader.exe"
# with requests.Session() as s:
# 	p = s.post("https://www.deezer.com/login/email", data=payload)

# 	print(sid)
# 	

# 	q = s.get("https://www.deezer.com/us/")
# 	j = str(q.headers)
# 	js = ast.literal_eval(j)
# 	sid = js["Set-Cookie"].split(";")[0]
# 	print(sid)


# 	while(True):
# 		pass
# 	print("here")
	