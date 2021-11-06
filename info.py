from selenium import webdriver
import time
import pandas as pd
import random


driver = webdriver.Chrome()
html = driver.get('http://sns.sseinfo.com/company.do?uid=195059')

# dd_list = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div/dl/dd')
# time.sleep(2)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# ret = driver.find_elements_by_css_selector("[class='m_feed_txt']")
time.sleep(5)
driver.execute_script("""
    (function () {
    var y = 0;
    var step = 100;
    window.scroll(0, 0);
    function f() {
    if (y < document.body.scrollHeight) {
    y += step;
    window.scroll(0, y);
    setTimeout(f, 100);
    } else {
    window.scroll(0, 0);
    document.title += "scroll-done";
    }
    }
    setTimeout(f, 1000);
    })();
    """)
print("下拉中...")
    # time.sleep(180)
while True:
    if "scroll-done" in driver.title:
        break
    else:
        print("还没有拉到最底端...")
        time.sleep(3)
# driver.execute_script('alert("To Bottom")')
dd_list = driver.find_elements_by_xpath('//div[@class="m_feed_item"]')

# with open('gimiInfo.csv','w',newline='') as f:
#     writer = csv.writer(f)

li=[]
for dd in dd_list:
    item = {}
    item['question'] = dd.find_element_by_xpath('.//div[@class="m_feed_detail"]//div[@class="m_feed_txt"]').text
    item['time'] = dd.find_element_by_xpath('.//div[@class="m_feed_detail"]//div[@class="m_feed_from"]/span').text
    item['source'] = dd.find_element_by_xpath('.//div[@class="m_feed_detail"]//div[@class="m_feed_func"]//a').text
    # item['answer'] = dd.find_element_by_xpath('.//div[@class="m_feed_detail.m_qa"]//div[@class="m_feed_txt"]').text
    # print(item)
    item['answer'] = dd.find_element_by_css_selector("[class='m_feed_detail m_qa']").find_element_by_xpath('.//div[@class="m_feed_txt"]').text
    print(item)
    li.append([item['time'],item['question'],item['answer'],item['source']])
    # writer.writerow(li)
# f.close()
name=['时间','问题','回答','来源']
ret=pd.DataFrame(columns=name,data=li)
ret.to_csv('极米科技投资者问答.csv')










# def get_one_page():
#     dd_list = driver.find_elements_by_xpath('//div[@class="m_feed_item"]')
#     for dd in dd_list:  
#         item = {}  
#         # item['question'] = dd.find_element_by_xpath('./div/div/div[@class="m_feed_txt"]').text.strip()
#         # item['time'] = dd.find_element_by_xpath('./div/div/div/div[@class="m_feed_from"]').text.strip()
#         # item['type'] = dd.find_element_by_xpath('./div/div/div/div[@class="m_feed_from"]/a').text.strip()
#         # item['answer'] = dd.find_element_by_xpath('./div[@class="m_feed_detail.m_qa"/div/div/div/div[@class="m_feed_txt"]').text.strip()
#         item['question'] = dd.find_element_by_css_selector("[class='m_feed_txt']").text.strip()
#         print(item)




# get_one_page()

"""
/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div[1]/div[2]/div[3]/div[2]
"""









