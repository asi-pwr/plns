import datetime
from plns.payments import models
from plns.stats.util import GraphMaker
from plns.users.models import User

class LineGraphMaker(GraphMaker):
    html_template = "<canvas id=\"oneChart\" width=\"500\" height=\"500\"></canvas>"
    database = models.PaymentManager
    username = User.get_username()

    def __init__(self, chart_type,date_from, date_to):
        self.chart_type = chart_type
        self.date_from = date_from
        self.date_to = date_to



    def iterate_data(self):
        """
        Filters database with username, then data, and then by categories from chart_type Chart.config and returns
        filtered entries
        """
        query = self.database.date_sort(self.date_from, self.date_to)
        query= query.filter(user__exact=self.username)
        return query

    def generate(self):
        """
        Generates HTML that will be passed to view.
        """
        iterated = self.iterate_data()
        chart_labels = []
        chart_entries = []
        js = """ var ctx = document.getElementById("oneChart").getContext("2d");"""
        js += "var data = {\n	labels : ["
        for e in iterated:
            chart_entries.append(e.amount)
            chart_labels.append(e.timestamp.hour+":"+e.timestamp.minute)
        js.join(str(x)+"\",\"" for x in chart_entries)
        js += """],\n
            datasets : [\n
            {\n
            fillColor : "rgba(220,220,220,0.5)",\n
            strokeColor : "rgba(220,220,220,1)",\n
            pointColor : "rgba(220,220,220,1)",\n
            pointStrokeColor : "#fff",\n
            data : ["""
        js.join(str(x)+"\",\"" for x in chart_entries)
        js += """]\n
        }\n]\n         }\n
var myNewChart = new Chart(ctx).PolarArea(data);"""
        return js, self.html_template