import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import csv

f = open('OfficePrices.csv', 'r')
reader = csv.reader(f)
csvLogList = list(reader)

low_price_list = [i[0] for i in csvLogList]
date_stamps = [i[2] for i in csvLogList]
f.close()

plotly.tools.set_credentials_file(username='kirankaranth', api_key='rHTTlycojdvIQ6qzzkIB')

data = [go.Scatter(
          x=date_stamps,
          y=low_price_list)]
py.plot(data, filename = 'Office-surge', fileopt='overwrite',auto_open=False)
