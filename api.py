#data scraped using wunderground
import urllib2
import json
import datetime
import numpy

now = datetime.datetime.now()
curr_year = now.year
curr_month = now.month
curr_date = now.day
# PD_matrix

total_list = []

for x in range(0, 2):
	# if curr_month < 10:
	# 	if curr_date < 10:
	# 		concat = str(curr_year - 1) + "0" + str(curr_month) + "0" + str(curr_date - 7 + x)
	# else:
	# 	print "here"
	# 	if curr_date < 10:
	# 		concat = str(curr_year - 1) + str(curr_month) + "0" + str(curr_date - 7 + x)
	# 	else:
	# 		concat = str(curr_year - 1) + str(curr_month) + str(curr_date - 7 + x)
	concat = str(curr_year - 1) + "0" + str(curr_month) + str(curr_date - 7 + x)

	print concat
	link = "http://api.wunderground.com/api/8d78dd77ccf83958/history_date/q/MA/Cambridge.json"
	new_link = link.replace('date', str(concat))

	print new_link

	f = urllib2.urlopen(new_link)

	json_string = f.read() 
	 

	parsed_json = json.loads(json_string)

	temp_min = int(str(parsed_json['history']['dailysummary'][0]['mintempi']))
	temp_max = int(str(parsed_json['history']['dailysummary'][0]['maxtempi']))
	temp_precip = float(str(parsed_json['history']['dailysummary'][0]['precipi']))

	temp_min_10c = (50 * (temp_min - 32))/9
	temp_max_10c = (50 * (temp_max - 32))/9

	daily_list = [temp_min_10c,temp_max_10c,temp_precip]

	total_list.append(daily_list)

	print daily_list

	#print PD_matrix
	print "Max temp is: %s" % (temp_max_10c)
	print "Min temp is: %s" % (temp_min_10c)
	print "Precipitation is: %s" % (temp_precip)

f.close()

print total_list

total_array = numpy.array(total_list)

print total_array