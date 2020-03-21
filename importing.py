from solution import readDataFromJsonFile
import os, pymongo

def isfloat(num):
	try:
		return float(num)
	except:
		return 0

def main():
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	mydb = myclient["RGPH"]
	collections= ['Démographie', 'Handicap', 'Education_et_alphabétisation', 'Langues_locales_utilisées', 'Activité_et_emploi', 'Conditions_d_habitat']
	dblist = myclient.list_database_names()
	if "RGPH" in dblist:
		print("The database exists. It will be dropped !")
		mydp.dropDatabase()
		return
	files= os.listdir("./data1")
	for file in files:
		data= readDataFromJsonFile("./data1/"+ file)
		code_commune= file.rsplit(".", 1)[0]
		code_province= code_commune.rsplit(".", 1)[0]
		code_region=  code_commune.split(".")[0]
		commune_querry= {"code_commune": code_commune, "code_province": code_province, "code_region": code_region}
		mydb["Communes"].insert_one(commune_querry)
		for collection in collections:
			if data[collection]:
				for item in data[collection]:
					s = item["INDICATEUR"].split("_", 1)
					querry= {"code_commune": code_commune, "INDICATEUR": s[1], "TYPE": s[0][1], "SEX": s[0][2] if len(s[0])==3 else None, "OBSERVATION": isfloat(item["DATA2014"])}
					mydb[collection].insert_one(querry)

if __name__ == '__main__':
	main()