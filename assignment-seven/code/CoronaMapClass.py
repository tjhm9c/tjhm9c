import plotly as pt
import plotly.graph_objects as go

from FetchAPIClass import FetchAPI

x = FetchAPI("https://coronavirus-tracker-api.herokuapp.com/all")

data = x.fetch_time_map()


token = "TOKEN" # you will need your own token

fig = go.Figure(go.Scattergeo())

fig.update_geos(
    visible=False,
    resolution=110,
    scope="usa",
    showcountries=True,
    countrycolor="Black",
    showsubunits=True,
    subunitcolor="Black"
)


for i in range(len(data)):
    d = data[i]["data"]
    d.location = d.location + " Confirmed Cases: " + d.ccount
    fig.add_trace(go.Scattergeo(
        visible=False,
        lat=d.lat,
        lon=d.lon,
        mode="markers",
        marker=go.scattergeo.Marker(
            size=d.dot_size,
            color=d.dot_color,
            opacity=0.5
        ),
        text=d.location,
        hoverinfo="text",
    ))

fig.data[0].visible = True

steps = []
for i in range(1,len(fig.data)):
    step = dict(
        method="restyle",
        args=["visible", [False]*len(fig.data)],
        label=i,
    )
    step["args"][1][i] = True
    steps.append(step)

sliders = [dict(
    active=0,
    currentvalue={"prefix": "Day: "},
    pad={"t": 50,
         "l": 300,
         "b": 50,
         "r": 300},
    steps=steps
)]


fig.update_layout(
    title="Coronavirus Map of confirmed cases in the USA",
    mapbox=dict(
        accesstoken=token,
        style="light",
    ),
    margin={"r": 100,
            "t": 50,
            "l": 100,
            "b": 50},
    sliders=sliders
)

pt.offline.plot(fig, filename="map.html", auto_open=True)