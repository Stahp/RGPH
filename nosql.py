#mysqldump RGPH > RGPH.SQL

import pymongo


def main():
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	mydb = myclient["RGPH"]
	collections= ['Démographie', 'Handicap', 'Education_et_alphabétisation', 'Langues_locales_utilisées', 'Activité_et_emploi', 'Conditions_d_habitat']

	querries= {
	4: { "INDICATEUR": "Population municipale", 'TYPE': 'E', 'SEX': 'E'}
	}

	for key in querries.keys():
		print("Question " + str(key))
		mycol = mydb["Démographie"]		
		mydoc = mycol.find(querries[key])
		for x in mydoc:
			print(x)
		print("______________________________")

if __name__ == '__main__':
	main()