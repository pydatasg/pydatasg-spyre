from spyre import server
import numpy as np
from matplotlib import pyplot as plt

class SimpleApp(server.App):
    title = "Simple Sine App"

    inputs = [{ "input_type": "text",
               "variable_name": "freq",
               "value": 5,
               "action_id": "sine_wave_plot"}]

    outputs = [{"output_type": "plot",
                "output_id": "sine_wave_plot",
                "on_page_load": True }]

    def getPlot(self, params):
        f = int(params['freq'])
        # numpy.arange([start, ]stop, [step, ]dtype=None)
        x = np.arange(0, 2 * np.pi, np.pi / 150)
        y = np.sin(f * x)
        plt.plot(x, y)
        return plt.gcf()

app = SimpleApp()
app.launch()
