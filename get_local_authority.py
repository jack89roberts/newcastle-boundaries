import requests
import json


ONS_QUERY = "https://ons-inspire.esriuk.com/arcgis/rest/services/Administrative_Boundaries/Local_Athority_Districts_December_2018_Boundaries_GB_BFC/MapServer/0/query?where=UPPER(lad18nm)%20like%20'%25NEWCASTLE%20UPON%20TYNE%25'&outFields=*&outSR=4326&f=json"

r = requests.get(ONS_QUERY)
r_json = json.loads(r.content)


from arcgis.gis import GIS

print("ArcGIS Online as anonymous user")    
gis = GIS()
print("Logged in as anonymous user to " + gis.properties.portalName)

map1 = gis.map("Newcastle, UK")
map1