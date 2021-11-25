import folium
import pandas as pd

employees = pd.read_csv('locations.csv')
#view the dataset
print(employees.head())
center = [-0.023559, 37.9061928]
map_kenya = folium.Map(location=center, zoom_start=8)
for index, employee in employees.iterrows():
    location = [employee['latitude'], employee['longitude']]
    folium.Marker(location, popup = f'Name:{employee["employee"]}\n Revenue($):{employee["service_time"]}').add_to(map_kenya)

# save map to html file
map_kenya.save('map_view.html')