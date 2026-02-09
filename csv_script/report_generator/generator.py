class ReportGenerator():

    def __init__(self, data):
        self.data = data

    def choose_rep_type(self, report_type):
        available_reports = {'performance': 'get_performance_report',
                             'average-gdp': 'get_gdp_report'}

        if report_type in available_reports:
            method_name = available_reports[report_type]
            method = getattr(self, method_name)
            return method()
        else:
            raise ValueError(f'''Unknown report type {report_type}. 
                             Available {list(available_reports.keys())}''')

    def get_performance_report(self):
        position_data = {}

        for row in self.data:
            position = row['position']
            performance = float(row['performance'])
            
            if position not in position_data:
                position_data[position] = []
            position_data[position].append(performance)

        result = []

        for position, performances in position_data.items():
            average_performance = sum(performances) / len(performances)
            result.append({'position': position, 
                           'average_performance': average_performance})
            
        result.sort(key=lambda x: x['average_performance'], reverse=True)
        
        return result
    
    def get_gdp_report(self):
        gdp_data = {}

        for row in self.data:
            country = row['country']
            gdp = float(row['gdp'])
            
            if country not in gdp_data:
                gdp_data[country] = []
            gdp_data[country].append(gdp)

        result = []

        for country, gdp in gdp_data.items():
            average_gdp = sum(gdp) / len(gdp)
            result.append({'country': country, 
                           'average-gdp': average_gdp})
        
        result.sort(key=lambda x: x['average-gdp'], reverse=True)
        
        return result