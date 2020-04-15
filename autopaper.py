import requests
import json
import constants as const

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
	# platform = input("Which platform would you want to you would like to find images on(unsplash, pexels, or pixabay): ");
	# platform.lower();

	# #foricing the user to choose an option
	# while not(platform in options):
	# 	platform = input('Please choose between unsplash, pexels and pixabay: ');
	# 	platform.lower()

	# print('\n Thank you :)')

	url = platform_dict['pixabay']
	print('\n\n[SEARCHING] locating resources...');
	try:

		response_obj = requests.get(url)

	except:

		#In the case that the request has failed
		print('Could not find resource or denied request')

	else:
		
		#in the case that the request is successful'''
		print('Resource found, parsing JSON...')

		json_data = response_obj.json()
		line_break = '='*10

		img_url = json_data['hits'][0]['largeImageURL']
		print('\n[SEARCHING] requesting image...')
		
		try: 
			response_obj = requests.get(img_url)
		except:
			print('Image URL does not exist or has expired')
		else:
			print('\nImage found!!!\n')
			print('[WRITING] writing image to file...')
			
			img_data = response_obj.content
			img_name = 'myimage'
			path = "./images/{}.jpg".format(img_name)
			print(line_break+'\n'+path+'\n'+line_break) 

			with open(path,'wb') as handler:
				handler.write(img_data)

			print('FINISHED. Enjoy your image')

if __name__ == '__main__':
	main()