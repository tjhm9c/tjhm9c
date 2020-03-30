import requests as r
import pandas as pd
import json


class FetchAPI(object):

    def __init__(self, base_link):
        self.base_link = base_link
        self.all_data = None
        self.time_map = None

    def fetch_data(self):
        self.all_data = r.get(self.base_link).json()
        with open("data.json", "w") as f:
            json.dump(self.all_data, f)
    def fetch_time_map(self):
        self.fetch_data()
        my_time_map = {}
        for i in self.all_data["confirmed"]["locations"]:
            if i["country_code"] == "US":
                for k in range(len(sorted(i["history"].keys()))):
                    my_time_map[k] = {}
                    my_time_map[k]["date"] = sorted(i["history"].keys())[k]
                    my_time_map[k]["data"] = []

        for i in self.all_data["confirmed"]["locations"]:
            if i["country_code"] == "US":
                for k, date in enumerate(sorted(i["history"].keys())):
                    count = int(i["history"][date])
                    if k > 0:
                        now_count = int(i["history"][date])
                        yesterday_count = int(i["history"][sorted(i["history"].keys())[k-1]])
                        count = now_count if now_count >= yesterday_count else yesterday_count
                    i["history"][date] = count
                    my_time_map[k]["data"].append([
                        float(i["coordinates"]["lat"]),
                        float(i["coordinates"]["long"]),
                        str(count),
                        self.dot_size(count),
                        self.dot_color(count),
                        i["province"]
                    ])
        for i in self.all_data["confirmed"]["locations"]:
            if i["country_code"] == "US":
                for k, date in enumerate(sorted(i["history"].keys())):
                    df = pd.DataFrame(data=my_time_map[k]["data"],
                                      columns=["lat", "lon", "ccount", "dot_size", "dot_color", "location"])
                    my_time_map[k]["data"] = df
        self.time_map = my_time_map
        return self.time_map

    def dot_size(self, count):
        if not count:
            return 0
        elif count <= 1:
            return 10
        elif count <= 10:
            return 20
        elif count <= 25:
            return 30
        elif count <= 50:
            return 40
        elif count <= 100:
            return 50
        elif count <= 500:
            return 60
        elif count > 500:
            return 70

    def dot_color(self, count):
        if count <= 1:
            return "rgb(0, 0, 255)"
        elif count <= 10:
            return "rgb(115, 0, 255)"
        elif count <= 25:
            return "rgb(255, 255, 0)"
        elif count <= 50:
            return "rgb(255, 140, 0)"
        elif count <= 100:
            return "rgb(255, 80, 0)"
        elif count <= 500:
            return "rgb(255, 0, 0)"
        elif count > 500:
            return "rgb(92, 0, 0)"

    def fetch_daily_bar(self, t="confirmed", d=False):
        self.fetch_data()
        dates = {}
        for i in self.all_data[t]["locations"]:
            if i["country_code"] == "US":
                for k, date in enumerate(sorted(i["history"].keys())):
                    count = int(i["history"][date])
                    if k > 0:
                        now_count = int(i["history"][date])
                        yesterday_count = int(i["history"][sorted(i["history"].keys())[k-1]])
                        count = now_count - yesterday_count if now_count >= yesterday_count else 0
                    if k+1 not in dates.keys():
                        dates[k+1] = 0
                    dates[k+1] += count
        if d:
            return dates
        my_list = []
        for i in range(len(dates)):
            my_list.append([i+1, dates[i+1]])
        df = pd.DataFrame(data=my_list,
                          columns=["Day", "New Cases"])
        return df

    def overview(self):
        self.fetch_data()
        conf = self.all_data["confirmed"]["latest"]
        print(conf)
        death = self.all_data["deaths"]["latest"]
        recov = self.all_data["recovered"]["latest"]
        return [[conf, "Confirmed"], [death, "Deaths"], [recov, "Recovered"]]

    def fetch_daily_line(self):
        d = self.overview()
        df = pd.DataFrame(data=d,
                          columns=["Number Total", "Type"])
        return df
