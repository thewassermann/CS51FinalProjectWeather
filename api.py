#data scraped using wunderground
import urllib2
import json
import datetime
import numpy

now = datetime.datetime.now()
curr_year = now.year
curr_month = now.month
curr_date = now.day

total_list = []

class Matrices:

	def produce (self, type):
		if type is "CD":
			top_range = 7
		elif type is "PD":
			top_range = 14
		else:
			"nah"

		for x in range(0, top_range):
			# if curr_month < 10:
			# 	if curr_date < 10:
			# 		concat = str(curr_year - 1) + "0" + str(curr_month) + "0" + str(curr_date - 7 + x)
			# else:
			# 	print "here"
			# 	if curr_date < 10:
			# 		concat = str(curr_year - 1) + str(curr_month) + "0" + str(curr_date - 7 + x)
			# 	else:
			# 		concat = str(curr_year - 1) + str(curr_month) + str(curr_date - 7 + x)
			#concat = str(curr_year - 1) + "0" + str(curr_month) + str(curr_date - 7 + x)
			if type is "CD":
				concat = str(curr_year) + "%02d" % curr_month + "%02d"  % (curr_date - 7 + x)	
			elif type is "PD":
				concat = str(curr_year - 1) + "%02d" % curr_month + "%02d"  % (curr_date - 7 + x)
			else:
				"Nopes"

			print concat
			link = "http://api.wunderground.com/api/8d78dd77ccf83958/history_date/q/MA/Cambridge.json"
			new_link = link.replace('date', str(concat))

			print new_link

			f = urllib2.urlopen(new_link)

			json_string = f.read() 
			 

			parsed_json = json.loads(json_string)

			temp_min = int(str(parsed_json['history']['dailysummary'][0]['mintempi']))
			temp_max = int(str(parsed_json['history']['dailysummary'][0]['maxtempi']))
			temp_precip_raw = parsed_json['history']['dailysummary'][0]['precipi']
			if temp_precip_raw == 'T':
				temp_precip = 0.0
			else:
				temp_precip = float(str(temp_precip_raw))
			print temp_precip

			# if temp_precip_raw < 0.:
			# 	temp_precip_clean = 0.
			# else:
			# 	temp_precip_clean = temp_precip_raw

			#temp_precip = float(str(temp_precip_clean))

			temp_min_10c = int((50 * (temp_min - 32))/9)
			temp_max_10c = int((50 * (temp_max - 32))/9)
			precip_10 = int(100*temp_precip)

			daily_list = [precip_10, temp_max_10c,temp_min_10c]

			total_list.append(daily_list)

			print "Max temp is: %s" % (temp_max_10c)
			print "Min temp is: %s" % (temp_min_10c)
			print "Precipitation is: %s" % (precip_10)

		f.close()

		total_array = numpy.array(total_list)

		print total_array
		return total_array


	#def CD_produce (self):

