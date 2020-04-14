import request

#Unsplash API 
#Pixabay API 
#Pexels API

options = ['unsplash','pexels','pixabay']

def main():
	platform = input("Which platform would you want to you would like to find images on(unsplash, pexels, or pixabay): ");
	platform.lower();

	#foricing the user to choose an option
	while not(platform in options):
		platform = input('Please choose between unsplash, pexels and pixabay: ');
		platform.lower()

	print('\n Thank you :)')
	# response_obj = request.get()

if __name__ == '__main__':
	main()

