import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'NO':55.04,'NO2':87.10,'NOx':89.64,'NH3':33.72,'SO2':18.04,'CO':1.39,'O3':34.60,'PM2.5':113.33,'PM10':215.96})

print(r.json())