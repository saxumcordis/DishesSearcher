

import sys
import re
import urllib.request
import json

results = {"count" : 0, "dishes" : []}

def unique(list):
	result = []	
	for element in list:
		if element not in result:
			result.append(element)
	return result

def check(ingredients):
	return results['count'] == 0 or results['count'] >= len(ingredients)

if len(sys.argv) <= 1:  #Есть ли инпут?
	exit("Too few arguments")
	

for value in sys.argv[1:len(sys.argv)]: #Есть ли цифры в инпуте?
	if not re.match(r'^[A-z]+$', value):
		exit("yxadi")
		

queryString = ",".join(sys.argv[1:len(sys.argv)])

 

for p in range(1,11): #Перебор страничек
	dishes = json.loads(urllib.request.urlopen(
		'http://www.recipepuppy.com/api/?i=' + queryString
		 + '&p=' + str(p) ).read())['results']
	
	if len(dishes) == 0:
		break;

	for dish in dishes:		
		ingredients = unique(dish['ingredients'].split(','))
		
		if check(ingredients):
			results['count'] = len(ingredients)
			results['dishes'].append(
				{"link" : dish['href'], "ingredients" : ingredients}
			)

print('Nothing found' if results['count'] == 0 else results['dishes'])