import urllib2
import urllib
import json
import webbrowser
import os
import sys
from pprint import pprint

class GoogleSearch(object):

	CHOICES = { '--help': 'startSettingList', '--search': 'startSearch'}

	def start(self):
		print('Hello buddy - Welcome to this command line tool for googling written in python <3')
		userInput = raw_input("Press --help for settings listing otherwise enter --search enjoy your web search >> ")

		while userInput != "--exit":
			self.actionToStart(userInput)
			print('Press --help for settings listing otherwise --search')
			userInput = raw_input('[WAITING_FOR_INPUT] Enter a new command: ')

		print('Bye bye')
		sys.exit()

	def actionToStart(self, userInput):
		methodToCall = self.CHOICES.get(userInput)
		call = getattr(GoogleSearch(), methodToCall)
		call()

	def startSearch(self):
		url = "https://www.googleapis.com/customsearch/v1?key=AIzaSyDPT7SB8IFDIO1U_XiDNTcSEq-WgE-UAgs&cx=002033749997840423941:7kmknnh8g6e&"
		userSearchKey = raw_input("What do you want to look up? >> ")
		query = urllib.urlencode({'q' : userSearchKey })
		response = urllib2.urlopen(url + query).read()
		data = json.loads(response)
		results = data['items']
  		searchCounter = 0

		for result in results:
			title = result['title']
			link = result['link']
			print(str(searchCounter) + ': ' + title + '->' + link)
			searchCounter += 1

		resultIndexToVisit = raw_input("Which hit do you want to visit? >> ")
		webbrowser.get('firefox').open_new_tab(results[int(resultIndexToVisit)]['link'])
		os.system('clear')

	def startSettingList(self):
		print('settings lists yet to come')
		print('Press --exit for quitting')

googleSearch = GoogleSearch()
googleSearch.start()
