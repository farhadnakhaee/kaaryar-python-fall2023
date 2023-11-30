import matplotlib.pyplot as plt

class TightCouplingPlotter:
    def __init__(self, filename):
        self.filename = filename
        self.data = self._read_data()

    def _read_data(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            return [float(line.strip()) for line in lines]

    def plot_data(self):
        plt.plot(self.data)
        plt.show()

if __name__ == "__main__":
    tight_coupling_plotter = TightCouplingPlotter('data.txt')
    tight_coupling_plotter.plot_data()
