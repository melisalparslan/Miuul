# Mocking a dataframe with random data to simulate the heatmap generation
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Creating a random dataframe similar to what the user might have
np.random.seed(0)
data = np.random.randint(0, 1000, size=(6, 5))
columns = ['LRR', 'HB', 'CP', 'PK', 'CRP']  # Example column names
index = ['S. salmonicida', 'G. intestinalis', 'G. muris']  # Example index names
df_example = pd.DataFrame(data, columns=columns, index=index)


# Define a plotting function with the new color map
def plot_heatmap(df, output_file):
    sns.set_style("whitegrid", {'axes.grid': False})
    plt.figure(figsize=(20, 10))

    # Create the heatmap with the new color palette
    ax = sns.heatmap(df,
                     cmap="Blues",  # Changed to a standard sequential colormap
                     square=True,
                     fmt='g',
                     linewidths=.4,
                     annot=True,
                     cbar_kws={"shrink": .5},
                     annot_kws={"size": 5})

    plt.savefig(output_file, format="png", bbox_inches='tight', dpi=800)
    plt.show()


# Mock output file path
output_file_path = '/mnt/data/modified_heatmap.png'

# Plotting the heatmap with the mocked data
plot_heatmap(df_example, output_file_path)
