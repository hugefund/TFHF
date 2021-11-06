from selenium import webdriver
import time
# import sys
class gubaGimi(object):

    def __init__(self):
        # 开始时的url
        self.start_url = "http://guba.eastmoney.com/list,688696.html"
        # 实例化一个Chrome对象
        self.driver = webdriver.Chrome()
        # 用来写csv文件的标题
        self.start_csv = True

    # def __del__(self):
    #     self.driver.quit()

    # def get_count_page(self):
    #     html = self.driver.get(self.start_url)
    #     all_Page = self.driver.find_element_by_xpath('//div[@class="articleh normal_post"]').text
    #     count = int(all_Page[1:4])
    #     return count

    def get_content(self):
        # 先让程序两秒,保证页面所有内容都可以加载出来
        print("开始抓取")
        time.sleep(3)
        item = {}
        # 获取进入下一页的标签
        # next_page = self.driver.find_element_by_xpath("//span[@class='arrow']/a").get_attribute('href')
        # next_page_temp = self.driver.find_elements_by_xpath("//div[@class='pagination_index']")
        next_page = self.driver.find_elements_by_xpath("//span/a[@target='_self']")[-2]
        # 获取存储信息的所有li标签的列表
        # li_list = self.driver.find_elements_by_xpath('//*[@id="articlelistnew"]')
        li_list = self.driver.find_elements_by_css_selector("[class='articleh normal_post']")
        # 提取需要的数据
        for li in li_list:
            # item['read'] = li.find_element_by_xpath('.//div[@class="articleh.normal_post"]/span[@class="l1.a1"]').text
            # item['content'] = li.find_element_by_xpath('.//div[@class="articleh.normal_post"]/span[@class="l2.a2"]').text
            # item['text'] = li.find_element_by_xpath('.//div[@class="articleh.normal_post"]/span[@class="l3.a3"]').text
            # item['name'] = li.find_element_by_xpath('.//div[@class="articleh.normal_post"]/span[@class="l4.a4"]').text
            # item['time'] = li.find_element_by_xpath('.//div[@class="articleh.normal_post"]/span[@class="l5.a5"]').text
            # item_list = li.find_element_by_css_selector("[class='articleh normal_post']")
            item['read'] = li.find_element_by_xpath('./span[1]').text
            item['content'] = li.find_element_by_xpath('./span[2]').text
            item['text'] = li.find_element_by_xpath('./span[3]/a').text
            item['name'] = li.find_element_by_xpath('./span[4]/a').text
            item['time'] = li.find_element_by_xpath('./span[5]').text
            print(item)

            # 保存数据
            self.save_csv(item)
            # //*[@id="articlelistnew"]/div[83]/span/span/span[1]/a[11]
        
        # 返回是否有下一页和下一页的点击事件的标签,
        return next_page

    def save_csv(self,item):
        # 将提取存放到csv文件中的内容连接为csv格式文件
        str = ','.join([i for i in item.values()])

        with open('./gubaGimi.csv','a',encoding='utf-8') as f:
            if self.start_csv:
                f.write("阅读,评论,内容,姓名,时间\n")
                self.start_csv = False
            # 将字符串写入csv文件
            f.write(str)
            f.write('\n')
        print("save success")

    def run(self):
        # 启动chrome并定位到相应页面
        self.driver.get(self.start_url)

        for i in range(89):
            # 开始提取数据,并获取下一页的元素
            next_page = self.get_content()
            # 点击下一页
            next_page.click()
            time.sleep(2)

if __name__=='__main__':
    gubaGimi_spider = gubaGimi()
    gubaGimi_spider.run()




