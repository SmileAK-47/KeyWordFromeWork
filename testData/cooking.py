# # -*- coding: UTF-8 -*-
# from urllib import request
# from http import cookiejar
#
# if __name__ == '__main__':
#
#     #设置保存cookie的文件，同级目录下的cookie.txt
#     filename = 'cookie.txt'
#     #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
#     cookie = cookiejar.MozillaCookieJar(filename)
#     #利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
#     handler=request.HTTPCookieProcessor(cookie)
#     #通过CookieHandler创建opener
#     opener = request.build_opener(handler)
#     #此处的open方法打开网页
#     response = opener.open('https://mail.126.com')
#     #保存cookie到文件
#     cookie.save(ignore_discard=True, ignore_expires=True)



# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("http://www.youdao.com")
# #获得cookie信息
# cookie=driver.get_cookies()
# #将获得cookie的信息打印
# print(cookie)
# driver.quit()



from selenium import webdriver
import requests
import json
import time
def get_cookies():
    driver = webdriver.Chrome()
    driver.get("https://www.126.com/")# xxx 指定链接登录页面
    input("请登陆后按Enter")
    print(driver.get_cookies())

    # 获得cookies
    cookies = login_cookie()
    driver = webdriver.Firefox()
    driver.delete_all_cookies()  # 清除所有cookie
    # 直接访问访问后的地址添加cookie
    driver.set_page_load_timeout(20)
    driver.set_script_timeout(20)
    try:
        driver.get("https://www.126.com/")
    except:
        driver.execute_script("window.stop()")
    time.sleep(10)
    # 添加cookie到未登的录页面
    for co in cookies:
        driver.add_cookie(co)
    driver.refresh()



    cookie={}
    # for i in driver.get_cookies():
    #     cookie[i["name"]] = i["value"]
    with open("cookies.txt","w") as f:
        f.write(json.dumps(cookie))
    driver.close()

    # time.sleep(5)
    # button = browser.find_element_by_xpath('//*[@id="switcher_plogin"]')
    # button.click()
    #browser.close()

    # cookies = driver.get_cookies()
    # print(type(cookies))
    # # print ("".join(cookies))
    # f1 = open('cookie.txt', 'w')
    # f1.write(json.dumps(cookies))
    # f1.close


# def get_content():
#     user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
#     with open("cookies.txt","r")as f:
#         cookies = f.read()
#         cookies = json.loads(cookies)
#     session = requests.session()
#     html = session.get("https://www.126.com/",headers={"User-Agent":user_agent},cookies=cookies)
#     print(html.text)
# #
# def log_url():
#     driver = webdriver.Chrome()
#     driver.get("https://www.126.com/")
#     time.sleep(5)
#     f1 = open('cookies.txt')
#     cookie = f1.read()
#     cookie = json.loads(cookie)
#     for c in cookie:
#         driver.add_cookie(c)
#         print(driver.add_cookie(c))
#     # 刷新页面
#     driver.refresh()
#     time.sleep(10)
#     driver.close()

if __name__ == "__main__":
    get_cookies()
    # get_content()
    # log_url()



    cookies = browser.get_cookies()
    print("cookies",cookies)
    cookies = browser.get_cookies()
    jsonCookies = json.dumps(cookies)
    with open('cookies01.json', 'w') as f:
        f.write(jsonCookies)
    time.sleep(3)