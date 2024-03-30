import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

fig = plt.figure(figsize=(10, 6))
plt.bar(df['MNTH'], df['Actuals'], width=0.5, color='#002266', align='center')
sns.despine()

# Set title with increased font size, bold and underlined
plt.title('TITLE', fontsize=20, fontweight='bold', style='underline')

# Set x-ticks with increased font size and bold
plt.xticks(fontsize=14, fontweight='bold')

# Set y-ticks with increased font size and bold, adding '%' to the labels
plt.yticks(np.arange(0, 1.2, 0.2), fontsize=14, fontweight='bold')
def percent_formatter(x, pos):
    return "{:0.2f}%".format(x*100)

# Apply the formatter function to the y-axis
formatter = FuncFormatter(percent_formatter)
plt.gca().yaxis.

# Calculate the centers of the first and last bar for correct hline positioning
bar_centers = range(len(df['MNTH']))  # Assuming 'MNTH' is the x-axis categorical data
plt.hlines([0.6, 0.8], bar_centers[0] - 0.25, bar_centers[-1] + 0.25, colors=['orange', 'red'], linestyles='dashed')

# Adjust legend to include the new y-axis label description
handles, labels = plt.gca().get_legend_handles_labels()
handles.append(plt.Line2D([], [], color='black'))  # Add a dummy handle for the '%'
labels.append('Percentage (%)')  # Add a label for the dummy handle
plt.legend(handles=handles, labels=labels, loc='upper center', bbox_to_anchor=(0.5, -0.05), frameon=False, ncol=len(df.columns))

plt.savefig('IMG1.png', dpi=720)
IMG1 = 'IMG1.png'

plt.show()
plt.clf()
