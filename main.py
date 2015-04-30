# from stat_calc import get_variation
# from weather_data import prev_day
# class main:

# 	def finishing_move (sef, get_variation, prev_day):
# 			'add variation and prev_day conditions'

# from weather_data import WeatherData

# w = WeatherData()

# a = w.make_CD('CD.csv')
# b = w.make_PD('PD.csv')

# print "CD :"
# print a
# print "\n"
# print "PD :"
# print b
# print "\n"

from api import Matrices
import urllib2
import json
import datetime

mat = Matrices()

a = mat.produce("CD")
print a
b = mat.produce("PD")
print b

from main_algorithm import MainAlgorithm

m = MainAlgorithm()

win = m.sliding_windows(b)

disList = m.euc_distance(win,a)

sel = m.select_matrix(win,disList)

print "Sliding Windows :"
print win
print "\n"
print "Euclidian Distances :"
print disList
print "\n"
print "Closest Matrix :"
print sel
print "\n"


print "precipitation VC :"
pvc = m.variation_vector(a, "prcp")
print pvc
print "\n"
print "tmax VC :"
xvc = m.variation_vector(a, "tmax")
print xvc
print "\n"
print "tmin VC :"
nvc = m.variation_vector(a, "tmin")
print nvc

print "\n\n"

print "precipitation VP :"
pvp = m.variation_vector(sel, "prcp")
print pvp
print "\n"
print "tmax VP :"
xvp = m.variation_vector(sel, "tmax")
print xvp
print "\n"
print "tmin VP :"
nvp = m.variation_vector(sel, "tmin")
print nvp
print "\n"


from stat_calc import StatCalc

s = StatCalc()

vprcp = s.variation_helper(pvc, pvp)
print "Precipitation Variation: "
print vprcp
vtmax = s.get_variation(xvc, xvp)
print "\nHigh Variation: "
print vtmax
vtmin = s.get_variation(nvc, nvp)
print "\nLow Variation: "
print vtmin


#FINAL ANSWER::::
now = datetime.datetime.now()
curr_year = now.year
curr_month = now.month
curr_date = now.day

concat = str(curr_year) + "%02d" % curr_month + "%02d"  % (curr_date - 1)
link = "http://api.wunderground.com/api/8d78dd77ccf83958/history_date/q/MA/Cambridge.json"
new_link = link.replace('date', str(concat))

f = urllib2.urlopen(new_link)

json_string = f.read() 
			 

parsed_json = json.loads(json_string)

temp_min_y = int(str(parsed_json['history']['dailysummary'][0]['mintempi']))
temp_max_y = int(str(parsed_json['history']['dailysummary'][0]['maxtempi']))
temp_precip_raw_y = parsed_json['history']['dailysummary'][0]['precipi']
if temp_precip_raw_y == 'T':
	temp_precip_y = 0.0
else:
	temp_precip_y = float(str(temp_precip_raw_y))

yesttmin = int(((50 * (temp_min_y - 32))/9)/10)
yesttmax = int(((50 * (temp_max_y - 32))/9)/10)
yestprcp = int(100*temp_precip_y)

f.close()


finalp = "%d cm" %yestprcp
finalx = "%d C" %yesttmax
finaln = "%d C" %yesttmin

print "\nTomorrow's Precipitation: "
print finalp
print "\nTomorrow's High: "
print finalx
print "\nTomorrow's Low: "
print finaln



'''A simple program to create an html file froma given string,
and call the default web browser to display the file.'''

contents = '''<!DOCTYPE HTML>
<!--
	Aerial by HTML5 UP
	html5up.net | @n33co
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
	<head>
		<title>Aerial by HTML5 UP</title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<meta name="description" content="" />
		<meta name="keywords" content="" />
		<!--[if lte IE 8]><script src="css/ie/html5shiv.js"></script><![endif]-->
		<script src="js/skel.min.js"></script>
		<script src="js/init.js"></script>
		<noscript>
			<link rel="stylesheet" href="css/skel.css" />
			<link rel="stylesheet" href="css/style.css" />
			<link rel="stylesheet" href="css/style-wide.css" />
			<link rel="stylesheet" href="css/style-noscript.css" />
		</noscript>
		<!--[if lte IE 9]><link rel="stylesheet" href="css/ie/v9.css" /><![endif]-->
		<!--[if lte IE 8]><link rel="stylesheet" href="css/ie/v8.css" /><![endif]-->
	</head>
	<body class="loading">
		<div id="wrapper">
			<div id="bg"></div>
			<div id="overlay"></div>
			<div id="main">

				<!-- Header -->
					<header id="header">
						<h2>Tomorrow's Precipitation will be :</h2>
						<h1>''' + finalp + '''</h1><h2>Tomorrow's High will be:</h2>
						<h1>''' + finalx + '''</h1><h2>Tomorrow's Low will be:</h2><h1>''' + finaln + '''</h1>
						
					</header>

				<!-- Footer -->
					<footer id="footer">
						<span class="copyright">&copy; Hoechst | Wassermann | Cinnamon | Shapiro. Design: <a href="http://html5up.net">HTML5 UP</a>.</span>
					</footer>
				
			</div>
		</div>
	</body>
</html>
'''

def main():
    browseLocal(contents)

def strToFile(text, filename):
    """Write a file with the given name and the given text."""
    output = open(filename,"w")
    output.write(text)
    output.close()

def browseLocal(webpageText, filename='tempBrowseLocal.html'):
    '''Start your webbrowser on a local file containing the text
    with given filename.'''
    import webbrowser, os.path
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename)) #elaborated for Mac

main()