from uber_rides.session import Session
from uber_rides.client import UberRidesClient
import time
from datetime import datetime

session = Session(server_token="Rnbgt5bifs5ZGqsN9K_AMLY6XlHiHZL9jfBVQTQo")
client = UberRidesClient(session)

home_latitude = 17.504540
home_longitide = 78.364453
work_latitude = 17.429934
work_longitide = 78.340900

while (True):
    response_home_to_work = client.get_price_estimates(start_latitude=home_latitude,
                                                       start_longitude=home_longitide,
                                                       end_latitude=work_latitude,
                                                       end_longitude=work_longitide,
                                                       seat_count=1)

    response_work_to_home = client.get_price_estimates(start_latitude=work_latitude,
                                                       start_longitude=work_longitide,
                                                       end_latitude=home_latitude,
                                                       end_longitude=home_longitide,
                                                       seat_count=1)

    lowEstimate_home_to_work = response_home_to_work.json.get('prices')[0]['low_estimate']
    highEstimate_home_to_work = response_home_to_work.json.get('prices')[0]['high_estimate']
    average_home_to_work = (float(lowEstimate_home_to_work) + float(highEstimate_home_to_work)) / 2

    lowEstimate_work_to_home = response_work_to_home.json.get('prices')[0]['low_estimate']
    highEstimate_work_to_home = response_work_to_home.json.get('prices')[0]['high_estimate']
    average_work_to_home = (float(lowEstimate_work_to_home) + float(highEstimate_work_to_home)) / 2

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    current_day = datetime.now().strftime('%Y-%m-%d')
    current_day_of_week = datetime.today().weekday()
    with open("WorktoHomeUberPrices.csv", 'a') as log_file_home_to_work:
        print("{0},{1},{2},{3},{4}".format(str(current_day_of_week), str(lowEstimate_home_to_work),
                                           str(highEstimate_home_to_work), str(average_home_to_work),
                                           str(current_time)), file=log_file_home_to_work)

    with open("HometoWorkUberPrices.csv", 'a') as log_file_work_to_home:
        print("{0},{1},{2},{3},{4}".format(str(current_day_of_week), str(lowEstimate_work_to_home),
                                           str(highEstimate_work_to_home), str(average_work_to_home),
                                           str(current_time)), file=log_file_work_to_home)
    time.sleep(7)
