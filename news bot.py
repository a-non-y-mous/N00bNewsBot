from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from random import randint
from time import sleep

lg =[ "etce : https://chat.whatsapp.com/KOJhlhRXqfQ1Kre0Ttb2yl",
 "mech : https://chat.whatsapp.com/GMmiJ4gHHFc5Nb4Kb7AbXU" ]

browser = webdriver.Chrome()
browser.get('https://web.whatsapp.com')
def scrape_news_summaries(s):
	sleep(randint(0, 2))  # relax and don't let google be angry
	r = requests.get("http://www.google.co.in/search?q="+s+"&tbm=nws")
	print(r.status_code)  # Print the status code
	content = r.text
	news_summaries = []
	soup = BeautifulSoup(content, "html.parser")
	st_divs = soup.findAll("div", {"class": "st"})
	for st_div in st_divs:
		news_summaries.append(st_div.text)
	return news_summaries
	for n in l:
		print(n)

def getNews():
	text_box = browser.find_element_by_xpath("/html[@class='js serviceworker adownload cssanimations csstransitions webp webp-alpha webp-animation webp-lossless']/body[@class='web']/div[@id='app']/div[@class='_1FPJ- _39gtr app-wrapper-web']/div[@class='app _3fUe9 two']/div[@class='_3HZor _2rI9W']/div[@id='main']/footer[@class='_1N6pS']/div[@class='_2i7Ej copyable-area']/div[@class='_13mgZ']/div[@class='_3FeAD _1PRhq focused']/div[@class='_3u328 copyable-text selectable-text']") # // changed by me
	response = "I shall fetch and send top 5 latest news once this functionality is built.\r\n"
	text_box.send_keys(response)
	#soup = BeautifulSoup(requests.get(url).content, "html5lib")
	#articles = soup.find_all('article', class_="MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d YKEnGe EyNMab t6ttFe Fm1jeb EjqUne")
	#news = [i.find_all('a',class_="ipQwMb Q7tWef")[0].text for i in articles[:5]]
	#links = [root+i.find('a')['href'][1:] for i in articles[:5]]
	#links = [requests.get("http://thelink.la/api-shorten.php?url="+link).content.decode() for link in links]
	#for i in range(5):
	#	text_box.send_keys(news[i] + "==>" + links[i] + "\n")

bot_users = {} # A dictionary that stores all the users that sent activate bot 
while True:
	unread = browser.find_elements_by_class_name("P6z4j") # The green dot tells us that the message is new // changed by me
	name,message  = '',''
	if len(unread) > 0:
		ele = unread[-1]
		action = webdriver.common.action_chains.ActionChains(browser)
		action.move_to_element_with_offset(ele, 0, -20) # move a bit to the left from the green dot

		# Clicking couple of times because sometimes whatsapp web responds after two clicks
		try:
			action.click()
			action.perform()
			action.click()
			action.perform()
		except Exception as e:
			pass
		try:
			name = browser.find_element_by_xpath("/html[@class='js serviceworker adownload cssanimations csstransitions webp webp-alpha webp-animation webp-lossless']/body[@class='web']/div[@id='app']/div[@class='_1FPJ- _39gtr app-wrapper-web']/div[@class='app _3fUe9 two']/div[@class='_3HZor _2rI9W']/div[@id='main']/header[@class='_3fs0K']/div[@class='_3V5x5']/div[@class='_1lpto']/div[@class='_19vo_']/span[@class='_19RFN']").text  # Contact name // changed by me

			#message = browser.find_elements_by_class_name("_12pGw EopGb")[-1]  # the message content

			message_list = browser.find_elements_by_xpath("//div[@class='_12pGw EopGb']/span[@class='selectable-text invisible-space copyable-text']")

			#for message in message_list:
			#print("from: "+name+ "\nmsg:\n"+str(message.text))

			last_message = message_list[-1].text
			#(//div[@class='hotProductDetails'])[position() > last() - 60]
			if 'activate bot' in last_message.lower():
				if name not in bot_users:
					bot_users[name] = True
					text_box = browser.find_element_by_xpath("/html[@class='js serviceworker adownload cssanimations csstransitions webp webp-alpha webp-animation webp-lossless']/body[@class='web']/div[@id='app']/div[@class='_1FPJ- _39gtr app-wrapper-web']/div[@class='app _3fUe9 two']/div[@class='_3HZor _2rI9W']/div[@id='main']/footer[@class='_1N6pS']/div[@class='_2i7Ej copyable-area']/div[@class='_13mgZ']/div[@class='_3FeAD _1PRhq focused']/div[@class='_3u328 copyable-text selectable-text']") # // changed by me
					response = "Hi "+name+". Primitive News Bot here :). Now I am activated for you\r\n"
					text_box.send_keys(response)

				if name in bot_users:
					text_box = browser.find_element_by_xpath("/html[@class='js serviceworker adownload cssanimations csstransitions webp webp-alpha webp-animation webp-lossless']/body[@class='web']/div[@id='app']/div[@class='_1FPJ- _39gtr app-wrapper-web']/div[@class='app _3fUe9 two']/div[@class='_3HZor _2rI9W']/div[@id='main']/footer[@class='_1N6pS']/div[@class='_2i7Ej copyable-area']/div[@class='_13mgZ']/div[@class='_3FeAD _1PRhq focused']/div[@class='_3u328 copyable-text selectable-text']") # // changed by me
					response = "Hi "+name+".I am already activated for you\r\n"
					text_box.send_keys(response)
				
			if name in bot_users and 'show me news on' in last_message.lower():
				#getNews()
				print("showing news on"+last_message.lower()[12:])
				text_box = browser.find_element_by_xpath("/html[@class='js serviceworker adownload cssanimations csstransitions webp webp-alpha webp-animation webp-lossless']/body[@class='web']/div[@id='app']/div[@class='_1FPJ- _39gtr app-wrapper-web']/div[@class='app _3fUe9 two']/div[@class='_3HZor _2rI9W']/div[@id='main']/footer[@class='_1N6pS']/div[@class='_2i7Ej copyable-area']/div[@class='_13mgZ']/div[@class='_3FeAD _1PRhq focused']/div[@class='_3u328 copyable-text selectable-text']") # // changed by me
				response_head = "showing news based on this instruction "+last_message.lower()[12:]+"\r\n"
				text_box.send_keys(response_head)
				lll = scrape_news_summaries(last_message.lower()[13:])
				for nnn in lll:
					response_body = str(nnn)+"\r\n"
					text_box.send_keys(response_body)

			if 'deactivate' in last_message.lower():
				if name in bot_users:
					text_box = browser.find_element_by_xpath("/html[@class='js serviceworker adownload cssanimations csstransitions webp webp-alpha webp-animation webp-lossless']/body[@class='web']/div[@id='app']/div[@class='_1FPJ- _39gtr app-wrapper-web']/div[@class='app _3fUe9 two']/div[@class='_3HZor _2rI9W']/div[@id='main']/footer[@class='_1N6pS']/div[@class='_2i7Ej copyable-area']/div[@class='_13mgZ']/div[@class='_3FeAD _1PRhq focused']/div[@class='_3u328 copyable-text selectable-text']") # // changed by me
					response = "Bye "+name+".\r\n"
					text_box.send_keys(response)
					del bot_users[name]

			if name == "JU students group" or name == "JU ETCE UG1(2019-2023)":
				if '!linkbot show' in last_message.lower():
					text_box = browser.find_element_by_xpath("/html[@class='js serviceworker adownload cssanimations csstransitions webp webp-alpha webp-animation webp-lossless']/body[@class='web']/div[@id='app']/div[@class='_1FPJ- _39gtr app-wrapper-web']/div[@class='app _3fUe9 two']/div[@class='_3HZor _2rI9W']/div[@id='main']/footer[@class='_1N6pS']/div[@class='_2i7Ej copyable-area']/div[@class='_13mgZ']/div[@class='_3FeAD _1PRhq focused']/div[@class='_3u328 copyable-text selectable-text']") # // changed by me
					response = "Hi @all Primitive bot here.Here are the links: \r\n"
					text_box.send_keys(response)
					for itemg in lg:
						text_box.send_keys(str(itemg)+"\r\n")

			#print("i guess the last message from"+ name + " is " + message_list[-1].text)
			
		except Exception as e:
			print(e)
			pass
	sleep(0.2) # A 2 second pause so that the program doesn't run too fast
#view rawNewsBot.py hosted with ❤ by GitHub
