from FetchAPIClass import FetchAPI
import plotly.express as px
import plotly as pt

x = FetchAPI("https://coronavirus-tracker-api.herokuapp.com/all")
data = x.fetch_daily_line()

fig = px.bar(data, x="Type", y="Number Total", title="Coronavirus Global Statistics")
pt.offline.plot(fig, filename="daily_line.html", auto_open=True)
