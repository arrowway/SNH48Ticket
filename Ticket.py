# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import requests
import traceback
import threading
import json

class ORDER(object):
    def __init__(self,user,password,ticketcode,seattype,brandid,teamtype):
        self.user = user
        self.password = password
        self.ticketcode = ticketcode
        self.seattype = seattype
	self.brandid = brandid
	self.teamtype = teamtype
        self.cookies = ''
        self.req = requests.session()
        self.login()

    def login(self):
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.implicitly_wait(10)
        browser.set_page_load_timeout(30)
        browser.get('http://vip.48.cn/Home/Login/index.html')
        browser.find_element_by_id('login').click()
        browser.find_element_by_id('username').send_keys(self.user)
        browser.find_element_by_id('password').send_keys(self.password)
        browser.find_element_by_id('submit').click()
        browser.find_element_by_link_text('SNH48 GROUP官方商城').click()
        browser.switch_to_window(browser.window_handles[-1])
        for i in browser.get_cookies():
            self.cookies += i['name']
            self.cookies += '='
            self.cookies += i['value']
            self.cookies += '; '
        self.cookies.strip(';')
        print self.cookies
        browser.quit()

    def ticket(self):
        url = 'http://shop.48.cn'
        res = self.req.get(url,headers = {'Cookie':self.cookies})
        postData = {'id': self.ticketcode, 'num': '1', 'seattype': self.seattype,
                    'brand_id': '3', 'r': '0.3731131006391708','choose_times_end':'-1'}  # id:门票编号，num:门票数量，seattype:门票类型,2为VIP，3为普座，4为站票，brand_id：团体编号(gnz48为3)，’r‘:随机数
        url = 'https://shop.48.cn/Home/IndexTickets?brand_id={}&team_type={}&date_type=-1'.format(self.brandid,self.teamtype)
        index = 0
	for i in json.loads(requests.get(url).content):
		if i['tickets_id'] == int(self.ticketcode):
			break
		index += 1
	types = int(self.seattype) - 1
        
	while 1:
	        try:
	            res = self.req.get(url)
	        except:
	            traceback.print_exc()
	            continue
	        if json.loads(res.content)[index]['tickets_sales'][types]['amount']:
	            resp = self.req.post('https://shop.48.cn/TOrder/add',headers={'Cookie': self.cookies}, data=postData)
	            if resp.status_code == 200:
	                print 'order succeed...'
	        else:
	            continue
	
    def supervip(self):
	list_amt = []
	my = 0
        while 1:
                head = {'Cookie':self.cookies}
                for i in eval(get('https://shop.48.cn/pai/GetRightShowBids?id=2423',headers = head).content)['list']:
        			list_amt.append(i['bid_amt'])
                top1 = int(sorted(list_amt)[-1])
                if top1 > 35000:break # 设定上限值
                if my < top1:
                    my = int(top1) + 101 # 加价额度
                    print my
                postdata = {
                            'id':'2423',
                            'amt':str(my),
                            'num':'1'
                           }
                res = post('https://shop.48.cn/pai/ToBids',data = postdata,headers = head)
                time.sleep(0.2)

if __name__ == '__main__':
	se = ORDER('username','password','ticketcode','seattype','brandid','teamtype')  # id:门票编号，seattype:门票类型,2为VIP，3为普座，4为站票
	for i in range(30):
	    th = threading.Thread(target=se.ticket)
	    th.start()
