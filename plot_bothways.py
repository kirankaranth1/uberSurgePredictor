import plotly
import plotly.plotly as py
from plotly.graph_objs import *
import csv

f = open('HometoWorkUberPrices.csv', 'r')
reader = csv.reader(f)
csvLogList = list(reader)
average_price_list_home_to_work = [i[3] for i in csvLogList]
date_stamps_home_to_work = [i[4] for i in csvLogList]
f.close()

f2 = open('WorktoHomeUberPrices.csv', 'r')
reader = csv.reader(f2)
csvLogList = list(reader)
average_price_list_work_to_home = [i[3] for i in csvLogList]
date_stamps_work_to_home = [i[4] for i in csvLogList]
f2.close()

plotly.tools.set_credentials_file(username='kirankaranth', api_key='rHTTlycojdvIQ6qzzkIB')

work_to_home = Scatter(x=date_stamps_home_to_work, y=average_price_list_home_to_work, mode = 'lines',name = 'Home to Work')
home_to_work = Scatter(x=date_stamps_work_to_home, y=average_price_list_work_to_home, mode = 'lines',name = 'Work to Home')

data = Data([work_to_home, home_to_work])
py.plot(data, filename = 'Office-surge-both-ways', fileopt='overwrite',auto_open=False)
