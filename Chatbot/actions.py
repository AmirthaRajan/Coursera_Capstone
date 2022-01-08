from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet, Restarted, AllSlotsReset

import pandas as pd
import re

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from difflib import SequenceMatcher

# read csv file
ZomatoData = pd.read_csv('zomato.csv')
all_cities = pd.read_csv('wiki_indian_cities.csv',header=None)[0]

# drop duplicates
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)

# set the operating city list
WeOperate = ['Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 
	'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 
	'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 
	'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 
	'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']

# get the not operating cities
NotOperating = list(set(all_cities).difference(set(WeOperate)))


# convert all the cities to lowercase
NotOperating = [x.lower() for x in NotOperating]
WeOperate = [x.lower() for x in WeOperate]

temp_df=[]
price_min,price_max = None,None

# do restaurant search after getting all entities
def RestaurantSearch(city,cuisine,price):

	# filter restaurant based on cuisine and city
	TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: city.lower() in x.lower()))]
	
	# filter restaurans based on price
	if price=='low':
		TEMP=TEMP[TEMP["Average Cost for two"] < 300]
	elif price=='moderate':
		TEMP=TEMP[(TEMP['Average Cost for two'] >= 300) & (TEMP['Average Cost for two'] <= 700)]
	elif price=='high':
		TEMP=TEMP[TEMP['Average Cost for two'] > 700]

	# sort the restaurants based on rating
	TEMP = TEMP.sort_values(by='Aggregate rating',ascending=False)

	# return restauran name, address, price and rating
	return TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]


# do search restaurant action
class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}

		# get location, cuisine and price from slots
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		check_results = False

		# do restaurant search
		results = RestaurantSearch(city=loc,cuisine=cuisine,price=price)
		response=""

		# if response is empty print no response
		if results.shape[0] == 0:
			response= "no results"
			check_results = False
		else:
			check_results = True
			# get top 5 restaurants to display to users
			for restaurant in results.iloc[:5].iterrows():
				restaurant = restaurant[1]
				response=response + F" {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Aggregate rating']} \n\n"
			
			# set top 10 restaurants in global variable for email communication if required
			global temp_df
			temp_df=results.iloc[:10]
		
		# utter response to user
		dispatcher.utter_message("----- "+response+" -----")

		# set the flag for response
		return [SlotSet('check_results',check_results)]


# action class to validate location
class ActionCheckLocation(Action):
	def name(self):
		return 'action_check_location'

	def run(self, dispatcher, tracker, domain):

		try:
			# flag to check if location is confirmed
			check_location=False

			# use global variable for geting list of operating cities
			global WeOperate , NotOperating
			
			# get location from slot
			location = tracker.get_slot('location')

			# get user's last text input message 
			location_text = tracker.latest_message['text']

			# check if the location is in non-operating cities
			if location.lower() in NotOperating:
				dispatcher.utter_message(response = "utter_location")
				return [SlotSet('check_location',check_location),SlotSet('location_rerun',True)]
		
			locs = []
			# get the location text from user input the word after 'in' or 'at'
			locs = re.findall("(?:in|at)\s([A-z]+)$",str.strip(location_text),flags=2);

			if len(locs) == 0:

				# get the location text from user input
				locs = re.findall("^([A-z]+)$",str.strip(location_text),flags=2);

			# check if the location is mispelled and matching any of the operating countries for 
			# location text identified through regex
			locs_match = [loc for word in locs for loc in WeOperate if SequenceMatcher(None, word.lower(),loc).ratio() >= 0.75]

			# check for any match for location text identified by nlu in location slot
			slot_match = [loc for loc in WeOperate if SequenceMatcher(None, location,loc).ratio() >= 0.75]

			# condition if a location text is detected in slot already
			if location:

				# check if it is in operating region
				if str(location.lower()) in WeOperate:
					check_location=True
					return [SlotSet('check_location',check_location)]

				# else if there was any matching locations for input text
				elif len(locs_match):
					dispatcher.utter_message("We didn’t find any such location. Did you mean "+", ".join(locs_match)+" ?")				
					return [SlotSet('check_location',check_location),SlotSet('location',locs_match[0]),SlotSet('location_rerun',False)]
				
				# else if location has any matching word if misspelled
				elif len(slot_match):
					dispatcher.utter_message("We didn’t find any such location. Did you mean "+", ".join(slot_match)+" ?")				
					return [SlotSet('check_location',check_location),SlotSet('location',slot_match[0]),SlotSet('location_rerun',False)]

				# if the location does not match any condition
				else:
					check_location=False
					dispatcher.utter_message(response = "utter_location")
			
			# condition if there was no location text detected by nlu
			else:
				check_location=False
				
				# if there is any matching text for our operating cities
				if len(locs_match):
					dispatcher.utter_message("We didn’t find any such location. Did you mean "+", ".join(locs_match)+" ?")
					return [SlotSet('check_location',check_location),SlotSet('location',locs_match[0]),SlotSet('location_rerun',False)]
				
				# if a location was entered and not matching any cities
				elif len(locs):
					dispatcher.utter_message(response = "utter_location")
				
				# if no location was entered
				else:
					dispatcher.utter_message("Sorry. I can't seem to find any location")
		except:
			pass
		# set check location False and location rerun as true when 
		# no results are found for the given location text
		return [SlotSet('check_location',check_location),SlotSet('location_rerun',True)]


# action class to validate price
class ActionCheckPrice(Action):
	def name(self):
		return 'action_check_price'

	def run(self, dispatcher, tracker, domain):

		try:
			# get price text from slot
			price = tracker.get_slot('price')

			# skip check if nlu has already predicited the price
			if price in ['low','moderate','high']:
				return []

			# get user's last input text for price
			text = tracker.latest_message['text'];

			# check if any digit is present in the text message
			price_text = re.findall("[\d]+\.?[\d]*",text)

			if len(price_text):
				# convert the string to integer
				price_text=int(float(price_text[0]))

				# if text contains any of the below word combination set to low
				if (len(re.findall("(below|lesser|less|\<|lower).*300",text))):
					price = 'low'

				# if text contains any of the below word combination set to high
				elif(len(re.findall("(?:above|more|greater|\>|higher).*700",text))):
					price = 'high'
				
				# if text contains any of the below word combination set to moderate
				elif (len(re.findall("(?:below|lesser|less|\<|lower).*700",text)) | len(re.findall("(?:above|more|greater|\>|higher).*300",text))):
					price = 'moderate'

				# if the price is less than 300 set to low
				elif (price_text < 300):
					price = 'low'
				# else if price between 300 and 700 set to moderate
				elif ((price_text >= 300) & (price_text <= 700)):
					price = 'moderate'
				else:
					price = 'high'
		except:
			pass
		
		# set price slot
		return [SlotSet('price',price)]


# action class to validate Cuisine
class ActionValidateCuisine(Action):
	def name(self):
		return "action_check_cuisine"

	def run(self, dispatcher, tracker, domain):

		# get cuisine from slot
		cuisine = tracker.get_slot("cuisine")
		check_cuisine = True
		
		# if cuisine not preset in slot set flag check to false
		if not cuisine:
			check_cuisine = False
		else:
			default_cuisines = ["american","chinese","italian","mexican","north indian","south indian"]
			
			# if cuisine not preset list set flag check to false else true
			check_cuisine = False if cuisine.lower() not in default_cuisines else True
		
		if check_cuisine == False:
			# utter message for no cuisine
			dispatcher.utter_message("Sorry. I can't seem to find any cuisine")

		# return with slot set as False for cuisine check
		return [SlotSet("check_cuisine", check_cuisine)]


# action class to send mail
class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self, dispatcher, tracker, domain):

		# get email , location and cuisine from slots
		mailID = tracker.get_slot('email')
		city = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')

		try:
			#The mail addresses and password
			sender_address = 'upgrad.restaurant.search.chatbot@gmail.com'
			sender_pass = 'Upgrad_123'

			#Setup the MIME
			message = MIMEMultipart()

			# set from and to address
			message['From'] = sender_address
			message['To'] = mailID

			# get the top 10 restaurants from search
			global temp_df
			message['Subject'] = "Top " + str(len(temp_df)) + " " + cuisine.capitalize() + " restaurants in " + str(city).capitalize()   #The subject line
			
			# set mail subject
			mail_content = "Hi there! Here are the " + message['Subject'] + ".\n\n\n"
			
			# set mail body
			for index,restaurant in temp_df.iterrows():
				mail_content = mail_content + F" {restaurant['Restaurant Name']} in {restaurant['Address']} with Average Cost for two is said to be {restaurant['Average Cost for two']} and has been rated {restaurant['Aggregate rating']} \n\n"

			#The body and the attachments for the mail
			message.attach(MIMEText(mail_content, 'plain'))
			#Create SMTP session for sending the mail
			session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
			session.starttls() #enable security
			session.login(sender_address, sender_pass) #login with email and password
			text = message.as_string()
			session.sendmail(sender_address, mailID, text)
			session.quit()

			# utter message for mail sent succesfully
			dispatcher.utter_message(response = "utter_email_sent")
		except:
			pass

class ActionRestarted(Action):  
    def name(self):
        return 'action_restart'
 
    def run(self, dispatcher, tracker, domain):
        return[Restarted()] 
 
class ActionSlotReset(Action): 
    def name(self): 
        return 'action_slot_reset' 
 
    def run(self, dispatcher, tracker, domain): 
        return[AllSlotsReset()]
