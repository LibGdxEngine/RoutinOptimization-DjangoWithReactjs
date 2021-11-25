import csv

header = ['employee', 'latitude', 'longitude', 'service_time']
data = [
    [1, 28748.0, 28748.0, 1],
    [2, 23817.41,  28748.0, 1],
    [3, 19.9,  28748.0, 1],
    [4, 4.68,  28748.0, 1],
    [5, 124.6700,  28748.0, 1]
]

with open('locations.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)