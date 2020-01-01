import urllib.request
url = 'https://2019shell1.picoctf.com/problem/47235/'
ext = 'robots.txt'
resptext = urllib.request.urlopen(url + ext).read()
split = (resptext.split())

# for loop that determines which byte in the array contains the .html file
for i in range (0, (len(split))):
	splitme = split[i].decode("utf-8")
	if ".html" not in splitme:
		continue
	else:
		num = i

# convert the html file path from bytes to a string format
splstring = split[num].decode("utf-8")

# read the html file and split using the flag tag (both opening and closing tags) and then extract the flag
firstsplit = urllib.request.urlopen(url + splstring).read().decode("utf-8").split("<flag>", 1)
finalflag = firstsplit[1].split("</flag>", 1)

print(finalflag[0])
