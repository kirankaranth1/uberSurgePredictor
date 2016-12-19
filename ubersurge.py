from uber_rides.session import Session
from uber_rides.client import UberRidesClient
import time
from datetime import datetime

session = Session(server_token="Rnbgt5bifs5ZGqsN9K_AMLY6XlHiHZL9jfBVQTQo")
client = UberRidesClient(session)

while(True):
    response = client.get_price_estimates(start_latitude=17.504540,
                                          start_longitude=78.364453,
                                          end_latitude=17.429934,
                                          end_longitude=78.340900,
                                          seat_count=2)

    lowEstimate = response.json.get('prices')[0]['low_estimate']
    highEstimate = response.json.get('prices')[0]['high_estimate']
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("OfficePrices.csv", 'a') as log_file:
        print(str(lowEstimate)+","+str(highEstimate)+","+str(current_time), file=log_file)
        time.sleep(5)


