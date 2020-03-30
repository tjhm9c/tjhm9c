from FetchAPIClass import FetchAPI
import plotly.express as px
import plotly as pt

x = FetchAPI("https://coronavirus-tracker-api.herokuapp.com/all")
data = x.fetch_daily_bar()


fig = px.bar(data, x="Day", y="New Cases", title="New Coronavirus Cases Per Day")
pt.offline.plot(fig, filename="daily_usa.html", auto_open=True)