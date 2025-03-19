import requests

# https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Heidelberg?unitGroup=metric&include=hours&key=ESCAWBF2JXNRZLJNTG2DS3SYQ&contentType=json

link_start = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
link_middle = "Heidelberg"
link_end = "?unitGroup=metric&include=hours&key=ESCAWBF2JXNRZLJNTG2DS3SYQ&contentType=json"
link = link_start + link_middle + link_end

r = requests.get(link)
response = r.json()
print(response)
print("ok now what?")