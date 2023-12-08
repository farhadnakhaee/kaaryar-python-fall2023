import matplotlib.pyplot as plt

class DataReader:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            return [float(line.strip()) for line in lines]

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
