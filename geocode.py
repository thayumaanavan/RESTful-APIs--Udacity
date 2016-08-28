import httplib2
import json

def getGeocodeLocation(input):
    google_api_key="AIzaSyBHwIfs-7_rFJlVLp04Vy1XHRfMFtGS414"
    location=input.replace(" ","+")
    url=('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' %(location,google_api_key))
    h=httplib2.Http()
    response,content=h.request(url,'GET')
    result=json.loads(content)
    lat=result['results'][0]['geometry']['location']['lat']
    lng=result['results'][0]['geometry']['location']['lng']
    return lat,lng


result=getGeocodeLocation('Chennai,India')