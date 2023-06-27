import requests
import pandas as pd
import json

bus_stop = input_box.select(".value")
def get_busTimes(bus_stop):
    URL = 'https://api.wmata.com/NextBusService.svc/json/jPredictions?StopID={}&api_key=fe14e29e73c3466f9aba8eee3c6e508a'.replace('{}',bus_stop)
    data = json.loads(requests.get(URL).text)
    df = pd.json_normalize(data,record_path =['Predictions'])

    stop = df.drop(columns=['DirectionNum','VehicleID','TripID'])

    return stop.to_html()

get_butTimes(bus_stop)
