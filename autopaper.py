import requests
import json

'''
NOTE: The platform functionality does not work since I cannot get unsplash and pixabay api
to work because of my lack of knowledge of networking in python. To explain briefly the APIs require a header
in the request and the header has a certain format in which you embed the access keys but I didn't
know how to implement that. I just wanted to have the option although it is not necessary. I just
want to get the app to work and this is something I could do to add as an extra feature

===================
Unsplash API requirements 
=====================

access_key, secret_key
https://api.unsplash.com/photos/random
implementation status: unknown;

===================
#Pixabay API format
===================

requires access key 
url
implementation status: unknown;

===================
#Pexels API format
==================

apikey, url
implementation status: underway;

===================
'''

platform_dict = {
	"unsplash":'https://api.unsplash.com/photos/random',
	"pexels":'' #TODO, I'm leaving this out for now since I can't get it to work
	"pixabay":
		"apikey": 
		"url":'"https://pixabay.com/api/?key="'
}

options = ['unsplash','pexels','pixabay']

def main():
	# platform = input("Which platform would you want to you would like to find images on(unsplash, pexels, or pixabay): ");
	# platform.lower();

	# #foricing the user to choose an option
	# while not(platform in options):
	# 	platform = input('Please choose between unsplash, pexels and pixabay: ');
	# 	platform.lower()

	# print('\n Thank you :\n\n[SEARCHING] locating resources...)')

	url = platform_dict['pixabay']
	print('\n\n[SEARCHING] location resources...');
	response_obj = requests.get(url)
	print('Resource found parsing [JSON]')

	# json_data = json.loads(response_obj)
	print('JSON data\n ', '='*10)
	print(response_obj.text)

if __name__ == '__main__':
	main()


''' The print statements are for debuggin purposes. 

