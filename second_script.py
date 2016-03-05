import sexmachine.detector as gender
import csv
import re
import geocoder

d = gender.Detector()

male = 0
female= 0
andy = 0
new_rows_list = []

with open('second_streets.csv', 'rU') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',')
     for row in spamreader:
         name = row[0]
         namesplit = re.split("\.| |'",name)
         name_score = 0

         for n in namesplit:
         	n = n.capitalize()
         	if n=='Augustine' or n=='Jude':
         		name_score +=1
         	elif n=='Bevan':
         		name_score -=1
         	else:
         		if n !='The' and n!='Piccadilly' and n!='York' and n!='Warwick' and n!='Abbey' and n!='Lane':
		         	gen = d.get_gender(n)
		                if gen=='andy':
		                    name_score +=0
		                elif gen=='male':
		                    name_score +=1
		                else:
		                    name_score -=1

         new_row = [row[0],name_score,row[1]]
         new_rows_list.append(new_row)


with open('second_results.csv', 'wb') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter =',',quoting=csv.QUOTE_NONE, escapechar="/")
	for row in new_rows_list:
		spamwriter.writerow(row)


