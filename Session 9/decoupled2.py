import matplotlib.pyplot as plt
import json

class DataReader:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        if self.filename.startswith('https://'):
            return self._read_from_website()
        if self.filename.endswith('.txt'):
            return self._read_text_data()
        elif self.filename.endswith('.json'):
            return self._read_json_data()
        else:
            raise ValueError("Unsupported file format")

    def _read_from_website(self):
        pass

    def _read_text_data(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            return [float(line.strip()) for line in lines]

    def _read_json_data(self):
        with open(self.filename, 'r') as file:
            data = json.load(file)
            if isinstance(data, list) and all(isinstance(item, (int, float)) for item in data):
                return data
            else:
                raise ValueError("Invalid JSON format. Expecting a list of numbers.")


class DecoupledPlotter:
    def __init__(self, data):
        self.data = data

    def plot_data(self):
        plt.plot(self.data)
        plt.show()

if __name__ == "__main__":
    data_reader = DataReader('data.txt')
    data = data_reader.read_data()

    decoupled_plotter = DecoupledPlotter(data)
    decoupled_plotter.plot_data()
