import datetime

class GraphMaker(object):
    js_template = None
    html_template = None

    def __init__(self, username, chart_type, database, date_from, date_to):
        self.username = username
        self.chart_type = chart_type
        self.database = database
        self.date_from = date_from
        self.date_to = date_to



    def iter_data(self):
        """
        Filters database with username, then data, and then by categories from chart_type Chart.config and returns
        filtered entries
        """
        return []

    def generate(self):
        """
        Generates HTML that will be passed to view.
        """
        payments = self.filter()
        self.create_type()
        ''' Some HTML magic here'''
        pass

