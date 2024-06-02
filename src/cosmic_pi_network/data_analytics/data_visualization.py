import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

class AdvancedDataVisualization:
    def __init__(self, data):
        self.data = data

    def plot_histogram(self, column):
        plt.hist(self.data[column], bins=50)
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.title("Histogram of " + column)
        plt.show()

    def plot_scatterplot(self, x, y):
        plt.scatter(self.data[x], self.data[y])
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title("Scatterplot of " + x + " vs " + y)
        plt.show()

    def plot_pca(self, n_components):
        pca = PCA(n_components=n_components)
        pca_data = pca.fit_transform(self.data)
        plt.scatter(pca_data[:, 0], pca_data[:, 1])
        plt.xlabel("Principal Component 1")
        plt.ylabel("Principal Component 2")
        plt.title("PCA of " + str(n_components) + " components")
        plt.show()

    def plot_tsne(self, n_components):
        tsne = TSNE(n_components=n_components)
        tsne_data = tsne.fit_transform(self.data)
        plt.scatter(tsne_data[:, 0], tsne_data[:, 1])
        plt.xlabel("t-SNE Component 1")
        plt.ylabel("t-SNE Component 2")
        plt.title("t-SNE of " + str(n_components) + " components")
        plt.show()

    def plot_heatmap(self):
        sns.heatmap(self.data.corr(), annot=True, cmap="coolwarm")
        plt.title("Heatmap of Correlation Matrix")
        plt.show()

# Example usage
data = pd.read_csv("cosmic_pi_network_data.csv")
visualization = AdvancedDataVisualization(data)

visualization.plot_histogram("column1")
visualization.plot_scatterplot("column1", "column2")
visualization.plot_pca(2)
visualization.plot_tsne(2)
visualization.plot_heatmap()
