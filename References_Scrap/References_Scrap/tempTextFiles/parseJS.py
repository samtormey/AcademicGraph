import json
import csv

json_data = open('leaves_Perm_Love.json').read()
data = json.loads(json_data)

f = csv.writer(open("test.csv", "wb+"))

for dat in data:
	try:
		dat["base"]
	except:
		dat["base"] = 0
	f.writerow([dat["base"],
				dat["field_num1"],
				dat["field_num2"],
				dat["field_num3"],
				dat["field_num4"],
				dat["field_num5"]])

