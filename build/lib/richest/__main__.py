import argparse
import requests
import sys

base_url = 'https://forbes400.herokuapp.com/api/forbes400'

def create_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('--current',required=False,action='store_true',help='Get richest people currently' )
	parser.add_argument('--youngest',required=False,action='store_true',help='Get youngest richest people' )
	parser.add_argument('--oldest',required=False,action='store_true',help='Get oldest richest people' )
	parser.add_argument('--male',required=False,action='store_true',help='Get richest males' )
	parser.add_argument('--female',required=False,action='store_true',help='Get richest females' )
	# parser.add_argument('--industries',required=False,action='store_true',metavar='<industry name>',help='Get richest people in a particular industry currently eg. technology,fashion,finance' )

	return parser

def main(argv=None):

	"""
    :desc: Entry point method
    """
	if argv is None:
		argv = sys.argv

	try:
		parser = create_parser()
		args = parser.parse_args(argv[1:])

		# Arguments initialization
		current = args.current
		youngest = args.youngest
		oldest = args.oldest
		male = args.male
		female = args.female
		# industries = args.industries

		# Parser check
		if current:
			currentfun()

		elif youngest:
			youngestfun()

		elif oldest:
			oldestfun()

		elif male:
			malefun()

		elif female:
			femalefun()

		elif industries:
			industryfun(industries)

	except KeyboardInterrupt:
		print('\nGood Bye.')
	return 0

def currentfun():
	''' Get richest people currently '''
	content = requests.get(base_url+"?limit=20").json()
	for person in content:
		rank = str(person.get('rank',"NA"))
		name = str(person.get('name',"NA"))
		age = str(person.get('age',"NA"))
		title = str(person.get('title',"NA"))
		country = str(person.get('country',"NA"))
		print("Rank : " + rank + "\nName : " + name + "\nTitle : " + title + "\nAge : " + age + "\nCountry : " + country + "\n-----------------------------------------------------------\n")

def youngestfun():
	''' Get youngest richest people '''
	content = requests.get(base_url+"/youngest?limit=20").json()
	for person in content:
		rank = str(person.get('rank',"NA"))
		name = str(person.get('name',"NA"))
		age = str(person.get('age',"NA"))
		title = str(person.get('title',"NA"))
		country = str(person.get('country',"NA"))
		print("Rank : " + rank + "\nName : " + name + "\nTitle : " + title + "\nAge : " + age + "\nCountry : " + country + "\n-----------------------------------------------------------\n")

def industryfun(industry):
	''' Get richest people in a particular industry currently eg. technology,fashion,finance'''
	content = requests.get(base_url+"/industries:" + industry + "?limit=20").json()
	for person in content:
		rank = str(person.get('rank',"NA"))
		name = str(person.get('name',"NA"))
		age = str(person.get('age',"NA"))
		title = str(person.get('title',"NA"))
		country = str(person.get('country',"NA"))
		print("Rank : " + rank + "\nName : " + name + "\nTitle : " + title + "\nAge : " + age + "\nCountry : " + country + "\n-----------------------------------------------------------\n")

def oldestfun():
	''' Get oldest richest people '''
	content = requests.get(base_url+"/oldest?limit=20").json()
	for person in content:
		rank = str(person.get('rank',"NA"))
		name = str(person.get('name',"NA"))
		age = str(person.get('age',"NA"))
		title = str(person.get('title',"NA"))
		country = str(person.get('country',"NA"))
		print("Rank : " + rank + "\nName : " + name + "\nTitle : " + title + "\nAge : " + age + "\nCountry : " + country + "\n-----------------------------------------------------------\n")

def malefun():
	''' Get richest males '''
	content = requests.get(base_url+"/male?limit=20").json()
	for person in content:
		rank = str(person.get('rank',"NA"))
		name = str(person.get('name',"NA"))
		age = str(person.get('age',"NA"))
		title = str(person.get('title',"NA"))
		country = str(person.get('country',"NA"))
		print("Rank : " + rank + "\nName : " + name + "\nTitle : " + title + "\nAge : " + age + "\nCountry : " + country + "\n-----------------------------------------------------------\n")

def femalefun():
	''' Get richest females '''
	content = requests.get(base_url+"/female?limit=20").json()
	for person in content:
		rank = str(person.get('rank',"NA"))
		name = str(person.get('name',"NA"))
		age = str(person.get('age',"NA"))
		title = str(person.get('title',"NA"))
		country = str(person.get('country',"NA"))
		print("Rank : " + rank + "\nName : " + name + "\nTitle : " + title + "\nAge : " + age + "\nCountry : " + country + "\n-----------------------------------------------------------\n")


if __name__ == '__main__':
	sys.exit(main(sys.argv))