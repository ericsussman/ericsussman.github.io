        import json
        import requests
        import pandas as pd

        def get_busTimes(bus_stop):
            URL = 'https://api.wmata.com/NextBusService.svc/json/jPredictions?StopID={}&api_key=___'.replace('{}',bus_stop)
            data = json.loads(requests.get(URL).text)
            df = pd.json_normalize(data,record_path =['Predictions'])

            stop = df.drop(columns=['DirectionNum','VehicleID','TripID'])
        
            stop = stop.to_html()

            return stop

        input_box = Element("input_box")
        get_busTimes(input_box.value)
