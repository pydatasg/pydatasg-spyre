from spyre import server
import pandas as pd
from pandas.io.data import DataReader
import matplotlib.pyplot as plt
import numpy as np

class StockExample(server.App):
    title = "SG Offshore & Marine"

    inputs = [{"input_type": "dropdown",
               "label": "Company",
               "options": [{"label": "Keppel Corporation", "value": "BN4.SI"},
                           {"label": "SembCorp Industries", "value": "U96.SI"},
                           {"label": "Sembcorp Marine", "value": "S51.SI"},
                           {"label": "Cosco Corporation", "value": "F83.SI"},
                           {"label": "Yangzijiang Shipbuilding", "value": "BS6.SI"},
                           {"label": "Vard Holdings", "value": "MS7.SI"},
                           {"label": "Nam Cheong", "value": "N4E.SI"}],
               "variable_name": "ticker",
               "action_id": "plot"}]

    outputs = [{"output_type": "plot",
                "output_id": "plot",
                "on_page_load": True}]

    def getData(self, params):
        ticker = params['ticker']
        df = DataReader(ticker, 'yahoo', '2007-01-01')
        df['mavg'] = pd.rolling_mean(df['Adj Close'], 200)
        return df

    def getPlot(self, params):
        df = self.getData(params)
        plt.subplot(2, 1, 1)
        plt.gca().axes.get_xaxis().set_visible(False)
        plt_obj = df.plot(y=['Adj Close', 'mavg'])
        plt.subplot(2, 1, 2)
        plt_obj = df.plot(y=['Volume'])
        return plt_obj.get_figure()

app = StockExample()
app.launch()
