import folium
from folium import IFrame
import os
import base64

m = folium.Map(location=[52.16008598500544,7.4998319149017325], zoom_start=17)
walkData = os.path.join('walk.json')

folium.GeoJson(walkData, name='walk').add_to(m)

tooltip = "Click to see picture"
html = '<img src="data:image/png;base64,{}">'.format

picture1 = base64.b64encode(open('./images/1.png','rb').read()).decode()
iframe1 = IFrame(html(picture1), width=600+20, height=400+20)
popup1 = folium.Popup(iframe1, max_width=650)
icon1 = folium.Icon(color="red", icon="glyphicon-home")
marker1 = folium.Marker(location=[52.16218549247337,  7.4977827072143555], popup=popup1, tooltip=tooltip, icon=icon1).add_to(m)

picture2 = base64.b64encode(open('./images/2.png','rb').read()).decode()
iframe2 = IFrame(html(picture2), width=600+20, height=400+20)
popup2 = folium.Popup(iframe2, max_width=650)
icon2 = folium.features.CustomIcon('logo2.png', icon_size=(60,60))
marker2 = folium.Marker(location=[52.15853268062991,  7.495840787887572], popup=popup2, tooltip=tooltip, icon=icon2).add_to(m)

picture3 = base64.b64encode(open('./images/3.png','rb').read()).decode()
iframe3 = IFrame(html(picture3), width=400+20, height=600+20)
popup3 = folium.Popup(iframe3, max_width=650)
icon3 = folium.features.CustomIcon('logo2.png', icon_size=(60,60))
marker3 = folium.Marker(location=[52.158657736802176, 7.499595880508423], popup=popup3, tooltip=tooltip, icon=icon3).add_to(m)

m.save("index.html")
