import requests, json, os
import constants as const
from random import randrange, random

'''
NOTE: The platform functionality does not work since I cannot get unsplash and pixabay api
to work because of my lack of knowledge of networking in python. To explain briefly the APIs require a header
in the request and the header has a certain format in which you embed the access keys but I didn't
know how to implement that. I just wanted to have the option although it is not necessary. I just
want to get the app to work and this is something I could do to add as an extra feature

=========================
Unsplash API requirements
=========================

access_key, secret_key
https://api.unsplash.com/photos/random
implementation status: unknown;
-
========================
#Pixabay API format
========================

requires access key 
url
implementation status: unknown;

=======================
#Pexels API format
=======================

apikey, url
implementation status: underway;

=======================
'''

platform_dict = {
	"unsplash":'https://api.unsplash.com/photos/random',
	"pexels":'', #TODO, I'm leaving this out for now since I can't get it to work
	"pixabay":"https://pixabay.com/api/?key="+const.API_KEY
}

options = ['unsplash','pexels','pixabay']

def main():
	#platform functionality
	# platform = input("Which platform would you want to you would like to find images on(unsplash, pexels, or pixabay): ");
	# platform.lower();

	# #foricing the user to choose an option
	# while not(platform in options):
	# 	platform = input('Please choose between unsplash, pexels and pixabay: ');
	# 	platform.lower()

	# print('\n Thank you :)')

	url = platform_dict['pixabay']
	rand_hit = randrange(1,21)
	print('\n\n[SEARCHING] locating resources...');

	total_pages = 60
	rand_page = randrange(1,total_pages+1)
	rand_hit = randrange(1,21)

	try:
	
		response_obj = requests.get(url + '&page=' + str(rand_page))

	except:

		#In the case that the request has failed
		print('Could not find resource or denied request')

	else:
		
		#in the case that the request is successful'''
		print('Resource found, parsing JSON...')

		json_data = response_obj.json()
		line_break = '='*10

		#retrieving the url of a random image
		img_url = json_data['hits'][rand_hit]['largeImageURL']
		print('\n[SEARCHING] requesting image...')
		
		try:
			response_obj = requests.get(img_url)
		except:
			print('Image URL does not exist or has expired')
		else:
			print('\nImage found!!!\n')
			print('[WRITING] writing image to file...')
			
			img_data = response_obj.content
			
			#using a naming convention to make sure images don't overwrite each other.
			img_list = os.listdir('./images')
			print(img_list)
			img_no = len(img_list)

			img_name = 'myimage{}'.format(img_no)
			path = "./images/{}.jpg".format(img_name)
			print(line_break+'\n'+path+'\n'+line_break) 

			with open(path,'wb') as handler:
				handler.write(img_data)

			print('FINISHED. Enjoy your free stock photo')

if __name__ == '__main__':
	main()