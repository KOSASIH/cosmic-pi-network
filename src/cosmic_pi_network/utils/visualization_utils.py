import matplotlib.pyplot as plt
import seaborn as sns

class VisualizationUtils:
    def __init__(self):
        pass

    def plot_histogram(self, data, column):
        plt.hist(data[column], bins=50)
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.title("Histogram of " + column)
        plt.show()

    def plot_scatterplot(self, data, x, y):
        plt.scatter(data[x], data[y])
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title("Scatterplot of " + x + " vs " + y)
        plt.show()

    def plot_bar_chart(self, data, column):
        sns.countplot(x=column, data=data)
        plt.title("Bar Chart of " + column)
        plt.show()

    def plot_heatmap(self, data):
        sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
        plt.title("Heatmap of Correlation Matrix")
        plt.show()

# Example usage
visualization_utils = VisualizationUtils()
data = pd.read_csv("data.csv")
visualization_utils.plot_histogram(data, "column1")
visualization_utils.plot_scatterplot(data, "column1", "column2")
visualization_utils.plot_bar_chart(data, "column3")
visualization_utils.plot_heatmap(data)
