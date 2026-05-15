import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# --- Set global styles for a professional look ---
# This uses LaTeX for rendering fonts, which looks much crisper.
# It might require a LaTeX installation on your system (e.g., MiKTeX, MacTeX).
try:
    mpl.rcParams.update({
        'text.usetex': False,
        #'font.family': 'serif',
        #'font.serif': ['Computer Modern Roman', 'Times New Roman'],
        'axes.titlesize': 20,
        'axes.labelsize': 50,
        'xtick.labelsize': 45,
        'ytick.labelsize': 45,
        'legend.fontsize': 30,
        'legend.title_fontsize': 14,
    })
except:
    print("LaTeX not found. Falling back to default font rendering.")
    mpl.rcParams.update(mpl.rcParamsDefault)


# --- 1. Data Setup ---
winrates = np.array([
    [29.19, 28.32298137, 29.25465839, 25.0931677],
    #[29.29104478, 30.41044776, 29.56521739],
    [28.26, 29.78855721, 31.24223602, 29.13043478],
    #[27.95031056, 28.44720497, 29.22885572],
    #[26.70807453, 27.54975124, 28.60696517]
])
errors = np.array([
    [1.6, 1.58659484, 1.60321707, 1.52648204],
    #[1.60479889, 1.62220734, 1.60696884],
    [1.59, 1.61267865, 1.63338944, 1.60121054],
    #[1.58019459, 1.58869837, 1.60259],
    #[1.55787002, 1.57290966, 1.5923694]
])
winrate_DPO = 25.93
error_DPO = 1.55
labels = [r"$\beta_1 = 1/40$",# r"$\beta_1 = 1/20$",
 r"$\beta_1 = 1/10$"] 
 #r"$\beta_1 = 1/5$", r"$\beta_1 = 1$"]
x_values_original = np.array([0.0, 0.1, 0.2, 0.3])

# --- 2. Data Filtering ---
index_to_exclude = 2
if index_to_exclude:
    x_values_filtered = np.delete(x_values_original, index_to_exclude)
    winrates_filtered = np.delete(winrates, index_to_exclude, axis=1)
    errors_filtered = np.delete(errors, index_to_exclude, axis=1)
else:
    x_values_filtered = x_values_original
    winrates_filtered = winrates
    errors_filtered = errors



# --- 3. Plotting ---
fig, ax = plt.subplots(figsize=(16, 7))

# --- DPO Baseline (drawn first) ---
ax.axhline(
    y=winrate_DPO, color='black', linestyle='--', linewidth=4,
    label='DPO', zorder=1
)
ax.axhspan(
    winrate_DPO - error_DPO, winrate_DPO + error_DPO,
    color='black', alpha=0.1, zorder=0
)

# --- Main Data Lines with a better color palette and markers ---
num_lines = len(labels)
# Use the 'viridis' colormap, which is excellent for data visualization
colors = plt.get_cmap('viridis')(np.linspace(0, 0.85, num_lines))
markers = ['o', 's', '^', 'D', 'v']  # Different marker for each line

for i in range(num_lines):
    ax.plot(
        x_values_filtered,
        winrates_filtered[i],
        label=labels[i],
        color=colors[i],
        marker=markers[i],
        markersize=15,
        linestyle='-',
        linewidth=4,
        zorder=2 # Ensure lines are drawn on top of the DPO shade
    )
    ax.fill_between(
        x_values_filtered,
        winrates_filtered[i] - errors_filtered[i],
        winrates_filtered[i] + errors_filtered[i],
        color=colors[i],
        alpha=0.1, # Lighter alpha for a more subtle shading
        zorder=1
    )

# --- 4. Customizing and Polishing the Plot ---
ax.set_xlabel(r'$\%$ of swapped $\hat{r}$ entries')
ax.set_ylabel('Winrate')
ax.set_xticks(x_values_filtered)

# Place the legend outside the plotting area for clarity
ax.legend(
    ncol=3,
    #bbox_to_anchor=(1.04, 1), # Position to the top right, outside the plot
    loc='upper left',
    borderaxespad=0.
)

# Use a light grid on the y-axis only, which is less distracting
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.6)
ax.xaxis.grid(False) # No vertical grid lines

# Remove the top and right spines for a cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('grey')
ax.spines['bottom'].set_color('grey')

# Adjust layout to make room for the legend
fig.tight_layout(rect=[0, 0, 0.85, 1]) # rect=[left, bottom, right, top]
plt.savefig("robust_alpaca.pdf")


winrates =np.array([[ 29.06832298, 26.70807453, 26.58385093, 24.78, 18.45],
 [ 30.78358209, 31.34328358, 30.31055901, 29.94, 28.70]])
errors = np.array([[ 1.59899444, 1.55787002, 1.55555208, 1.52, 1.37],
 [  1.62775576, 1.63466039, 1.61850106, 1.61, 1.59]])

x_values_filtered = np.array([ 0.1, 0.5, 1.0, 2.0, 3.0])
winrates_filtered = winrates
errors_filtered = errors


# --- 3. Plotting ---
fig, ax = plt.subplots(figsize=(16, 7))

# --- DPO Baseline (drawn first) ---
ax.axhline(
    y=winrate_DPO, color='black', linestyle='--', linewidth=4,
    label='DPO', zorder=1
)
ax.axhspan(
    winrate_DPO - error_DPO, winrate_DPO + error_DPO,
    color='black', alpha=0.1, zorder=0
)

# --- Main Data Lines with a better color palette and markers ---
num_lines = len(labels)
# Use the 'viridis' colormap, which is excellent for data visualization
colors = plt.get_cmap('viridis')(np.linspace(0, 0.85, num_lines))
markers = ['o', 's', '^', 'D', 'v']  # Different marker for each line

for i in range(num_lines):
    ax.plot(
        x_values_filtered,
        winrates_filtered[i],
        label=labels[i],
        color=colors[i],
        marker=markers[i],
        markersize=15,
        linestyle='-',
        linewidth=4,
        zorder=2 # Ensure lines are drawn on top of the DPO shade
    )
    ax.fill_between(
        x_values_filtered,
        winrates_filtered[i] - errors_filtered[i],
        winrates_filtered[i] + errors_filtered[i],
        color=colors[i],
        alpha=0.1, # Lighter alpha for a more subtle shading
        zorder=1
    )

# --- 4. Customizing and Polishing the Plot ---
ax.set_xlabel('Variance')
ax.set_ylabel('Winrate')
ax.set_xticks(x_values_filtered)

# Place the legend outside the plotting area for clarity
ax.legend(
    ncol=3,
    #bbox_to_anchor=(1.04, 1), # Position to the top right, outside the plot
    loc='upper left',
    borderaxespad=0.
)

# Use a light grid on the y-axis only, which is less distracting
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.6)
ax.xaxis.grid(False) # No vertical grid lines

# Remove the top and right spines for a cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('grey')
ax.spines['bottom'].set_color('grey')

# Adjust layout to make room for the legend
fig.tight_layout(rect=[0, 0, 0.85, 1]) # rect=[left, bottom, right, top]
plt.savefig("variance_alpaca.pdf")


winrates =np.array([[21.49, 21.86, 22.63, 20.52, 20.40],
 [22.42, 21.99, 19.80, 21.37, 21.74]])
errors = np.array([[1.45, 1.4, 1.48, 1.43,1.42],
 [1.47, 1.49915716, 1.41, 1.45, 1.45]])

x_values_filtered = np.array([ 0.1, 0.5, 1.0, 2.0, 3.0])
winrates_filtered = winrates
errors_filtered = errors

winrate_DPO = 18.03
error_DPO = 1.35
# --- 3. Plotting ---
fig, ax = plt.subplots(figsize=(16, 7))

# --- DPO Baseline (drawn first) ---
ax.axhline(
    y=winrate_DPO, color='black', linestyle='--', linewidth=4,
    label='DPO', zorder=1
)
ax.axhspan(
    winrate_DPO - error_DPO, winrate_DPO + error_DPO,
    color='black', alpha=0.1, zorder=0
)

# --- Main Data Lines with a better color palette and markers ---
num_lines = len(labels)
# Use the 'viridis' colormap, which is excellent for data visualization
colors = plt.get_cmap('viridis')(np.linspace(0, 0.85, num_lines))
markers = ['o', 's', '^', 'D', 'v']  # Different marker for each line

for i in range(num_lines):
    ax.plot(
        x_values_filtered,
        winrates_filtered[i],
        label=labels[i],
        color=colors[i],
        marker=markers[i],
        markersize=15,
        linestyle='-',
        linewidth=4,
        zorder=2 # Ensure lines are drawn on top of the DPO shade
    )
    ax.fill_between(
        x_values_filtered,
        winrates_filtered[i] - errors_filtered[i],
        winrates_filtered[i] + errors_filtered[i],
        color=colors[i],
        alpha=0.1, # Lighter alpha for a more subtle shading
        zorder=1
    )

# --- 4. Customizing and Polishing the Plot ---
ax.set_xlabel('Variance')
ax.set_ylabel('Winrate')
ax.set_xticks(x_values_filtered)

# Place the legend outside the plotting area for clarity
ax.legend(
    ncol=3,
    #bbox_to_anchor=(1.04, 1), # Position to the top right, outside the plot
    loc='upper left',
    borderaxespad=0.
)

# Use a light grid on the y-axis only, which is less distracting
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.6)
ax.xaxis.grid(False) # No vertical grid lines

# Remove the top and right spines for a cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('grey')
ax.spines['bottom'].set_color('grey')

# Adjust layout to make room for the legend
fig.tight_layout(rect=[0, 0, 0.85, 1]) # rect=[left, bottom, right, top]
plt.savefig("variance_alpaca_zephyr.pdf")
winrates =np.array([[22.5, 24.12935323, 24.12935323, 19.8630137,  17.91044776],
 [23.98, 23.6318408,   23.88059701,  21.36645963 , 22.11180124]])
errors = np.array([[1.46, 1.50991313, 1.50991313, 1.40742984, 1.35312959],
 [1.51, 1.49915716, 1.50457037, 1.44558014, 1.46359146]])

x_values_filtered = np.array([ 0.1, 0.5, 1.0, 2.0, 3.0])
winrates_filtered = winrates
errors_filtered = errors

winrate_DPO = 19.12
error_DPO = 1.668
# --- 3. Plotting ---
fig, ax = plt.subplots(figsize=(16, 7))

# --- DPO Baseline (drawn first) ---
ax.axhline(
    y=winrate_DPO, color='black', linestyle='--', linewidth=4,
    label='DPO', zorder=1
)
ax.axhspan(
    winrate_DPO - error_DPO, winrate_DPO + error_DPO,
    color='black', alpha=0.1, zorder=0
)

# --- Main Data Lines with a better color palette and markers ---
num_lines = len(labels)
# Use the 'viridis' colormap, which is excellent for data visualization
colors = plt.get_cmap('viridis')(np.linspace(0, 0.85, num_lines))
markers = ['o', 's', '^', 'D', 'v']  # Different marker for each line

for i in range(num_lines):
    ax.plot(
        x_values_filtered,
        winrates_filtered[i],
        label=labels[i],
        color=colors[i],
        marker=markers[i],
        markersize=15,
        linestyle='-',
        linewidth=4,
        zorder=2 # Ensure lines are drawn on top of the DPO shade
    )
    ax.fill_between(
        x_values_filtered,
        winrates_filtered[i] - errors_filtered[i],
        winrates_filtered[i] + errors_filtered[i],
        color=colors[i],
        alpha=0.1, # Lighter alpha for a more subtle shading
        zorder=1
    )

# --- 4. Customizing and Polishing the Plot ---
ax.set_xlabel('Variance')
ax.set_ylabel('Winrate')
ax.set_xticks(x_values_filtered)

# Place the legend outside the plotting area for clarity
ax.legend(
    ncol=3,
    #bbox_to_anchor=(1.04, 1), # Position to the top right, outside the plot
    loc='upper left',
    borderaxespad=0.
)

# Use a light grid on the y-axis only, which is less distracting
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.6)
ax.xaxis.grid(False) # No vertical grid lines

# Remove the top and right spines for a cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('grey')
ax.spines['bottom'].set_color('grey')

# Adjust layout to make room for the legend
fig.tight_layout(rect=[0, 0, 0.85, 1]) # rect=[left, bottom, right, top]
plt.savefig("variance_alpaca_mistral.pdf")


#Distilled DPO Missing data

winrates = np.array([[ 19.12, 18.41, 21.11, 22.6, 23.57]])
errors = np.array([[1.668, 1.367 ,1.439,1.47, 1.496]])
x_values_filtered = np.array([0, 0.25, 0.5, 0.75, 1.0])
labels = [r"ML-RDPO (partial)"] 
winrates_filtered = winrates
errors_filtered = errors
fig, ax = plt.subplots(figsize=(16, 7))
winrate_DDPO = 23.57
error_DDPO = 1.496
# --- DPO Baseline (drawn first) ---
ax.axhline(
    y=winrate_DPO, color='black', linestyle='--', linewidth=4,
    label='DPO', zorder=1
)
ax.axhspan(
    winrate_DPO - error_DPO, winrate_DPO + error_DPO,
    color='black', alpha=0.1, zorder=0
)
ax.axhline(
    y=winrate_DDPO, color='orange', linestyle='--', linewidth=4,
    label='ML-RDPO', zorder=1
)
ax.axhspan(
    winrate_DDPO - error_DDPO, winrate_DDPO + error_DDPO,
    color='orange', alpha=0.1, zorder=0
)

# --- Main Data Lines with a better color palette and markers ---
num_lines = len(labels)
# Use the 'viridis' colormap, which is excellent for data visualization
colors = plt.get_cmap('viridis')(np.linspace(0, 0.85, num_lines))
markers = ['o', 's', '^', 'D', 'v']  # Different marker for each line

for i in range(num_lines):
    ax.plot(
        x_values_filtered,
        winrates_filtered[i],
        label=labels[i],
        color=colors[i],
        marker=markers[i],
        markersize=15,
        linestyle='-',
        linewidth=4,
        zorder=2 # Ensure lines are drawn on top of the DPO shade
    )
    ax.fill_between(
        x_values_filtered,
        winrates_filtered[i] - errors_filtered[i],
        winrates_filtered[i] + errors_filtered[i],
        color=colors[i],
        alpha=0.1, # Lighter alpha for a more subtle shading
        zorder=1
    )

# --- 4. Customizing and Polishing the Plot ---
ax.set_xlabel('Percentage of ratings')
ax.set_ylabel('Winrate')
ax.set_xticks(x_values_filtered)

# Place the legend outside the plotting area for clarity
ax.legend(
    ncol=3,
    #bbox_to_anchor=(1.04, 1), # Position to the top right, outside the plot
    loc='upper left',
    borderaxespad=0.
)

# Use a light grid on the y-axis only, which is less distracting
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.6)
ax.xaxis.grid(False) # No vertical grid lines

# Remove the top and right spines for a cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('grey')
ax.spines['bottom'].set_color('grey')

# Adjust layout to make room for the legend
fig.tight_layout(rect=[0, 0, 0.85, 1]) # rect=[left, bottom, right, top]
plt.savefig("ml-rdpo-missing-data.pdf")

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# --- Set global styles for a professional look ---
# This uses LaTeX for rendering fonts, which looks much crisper.
# It might require a LaTeX installation on your system (e.g., MiKTeX, MacTeX).
try:
    mpl.rcParams.update({
        'text.usetex': False,
        #'font.family': 'serif',
        #'font.serif': ['Computer Modern Roman', 'Times New Roman'],
        'axes.titlesize': 20,
        'axes.labelsize': 50,
        'xtick.labelsize': 45,
        'ytick.labelsize': 45,
        'legend.fontsize': 30,
        'legend.title_fontsize': 14,
    })
except:
    print("LaTeX not found. Falling back to default font rendering.")
    mpl.rcParams.update(mpl.rcParamsDefault)


# --- 1. Data Setup ---
winrates = np.array([
    [28.32298137, 29.25465839, 25.0931677],
    [29.29104478, 30.41044776, 29.56521739],
    [29.78855721, 31.24223602, 29.13043478],
    [27.95031056, 28.44720497, 29.22885572],
    [26.70807453, 27.54975124, 28.60696517]
])
errors = np.array([
    [1.58659484, 1.60321707, 1.52648204],
    [1.60479889, 1.62220734, 1.60696884],
    [1.61267865, 1.63338944, 1.60121054],
    [1.58019459, 1.58869837, 1.60259],
    [1.55787002, 1.57290966, 1.5923694]
])
winrate_DPO = 25.93
error_DPO = 1.55
labels = [r"$\beta_1 = 1/40$", r"$\beta_1 = 1/20$",
 r"$\beta_1 = 1/10$", r"$\beta_1 = 1/5$", r"$\beta_1 = 1$"]
x_values_original = np.array([ 0.1, 0.2, 0.3])

# --- 2. Data Filtering ---
index_to_exclude = None
if index_to_exclude:
    x_values_filtered = np.delete(x_values_original, index_to_exclude)
    winrates_filtered = np.delete(winrates, index_to_exclude, axis=1)
    errors_filtered = np.delete(errors, index_to_exclude, axis=1)
else:
    x_values_filtered = x_values_original
    winrates_filtered = winrates
    errors_filtered = errors



# --- 3. Plotting ---
fig, ax = plt.subplots(figsize=(16, 7))

# --- DPO Baseline (drawn first) ---
ax.axhline(
    y=winrate_DPO, color='black', linestyle='--', linewidth=4,
    label='DPO', zorder=1
)
ax.axhspan(
    winrate_DPO - error_DPO, winrate_DPO + error_DPO,
    color='black', alpha=0.1, zorder=0
)

# --- Main Data Lines with a better color palette and markers ---
num_lines = len(labels)
# Use the 'viridis' colormap, which is excellent for data visualization
colors = plt.get_cmap('viridis')(np.linspace(0, 0.85, num_lines))
markers = ['o', 's', '^', 'D', 'v']  # Different marker for each line

for i in range(num_lines):
    ax.plot(
        x_values_filtered,
        winrates_filtered[i],
        label=labels[i],
        color=colors[i],
        marker=markers[i],
        markersize=15,
        linestyle='-',
        linewidth=4,
        zorder=2 # Ensure lines are drawn on top of the DPO shade
    )
    ax.fill_between(
        x_values_filtered,
        winrates_filtered[i] - errors_filtered[i],
        winrates_filtered[i] + errors_filtered[i],
        color=colors[i],
        alpha=0.1, # Lighter alpha for a more subtle shading
        zorder=1
    )

# --- 4. Customizing and Polishing the Plot ---
ax.set_xlabel(r'$\%$ of swapped $\hat{r}$ entries')
ax.set_ylabel('Winrate')
ax.set_xticks(x_values_filtered)

# Place the legend outside the plotting area for clarity
ax.legend(
    ncol=3,
    #bbox_to_anchor=(1.04, 1), # Position to the top right, outside the plot
    loc='upper left',
    borderaxespad=0.
)

# Use a light grid on the y-axis only, which is less distracting
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.6)
ax.xaxis.grid(False) # No vertical grid lines

# Remove the top and right spines for a cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('grey')
ax.spines['bottom'].set_color('grey')

# Adjust layout to make room for the legend
fig.tight_layout(rect=[0, 0, 0.85, 1]) # rect=[left, bottom, right, top]
plt.savefig("robust_alpaca_all.pdf")


##### Modified varaince plots
winrates =np.array([[ 29.19 ,26.58385093, 24.78, 18.45],
 [ 28.26, 30.31055901, 29.94, 28.70]])
errors = np.array([[ 1.60 ,1.55555208, 1.52, 1.37],
 [ 1.59 , 1.61850106, 1.61, 1.59]])
labels = [r"$\beta_1 = 1/40$", 
 r"$\beta_1 = 1/10$"]
x_values_filtered = np.array([ 0.0, 1.0, 2.0, 3.0])
winrates_filtered = winrates
errors_filtered = errors


# --- 3. Plotting ---
fig, ax = plt.subplots(figsize=(16, 7))

# --- DPO Baseline (drawn first) ---
ax.axhline(
    y=winrate_DPO, color='black', linestyle='--', linewidth=4,
    label='DPO', zorder=1
)
ax.axhspan(
    winrate_DPO - error_DPO, winrate_DPO + error_DPO,
    color='black', alpha=0.1, zorder=0
)

# --- Main Data Lines with a better color palette and markers ---
num_lines = len(labels)
# Use the 'viridis' colormap, which is excellent for data visualization
colors = plt.get_cmap('viridis')(np.linspace(0, 0.85, num_lines))
markers = ['o', 's', '^', 'D', 'v']  # Different marker for each line

for i in range(num_lines):
    ax.plot(
        x_values_filtered,
        winrates_filtered[i],
        label=labels[i],
        color=colors[i],
        marker=markers[i],
        markersize=15,
        linestyle='-',
        linewidth=4,
        zorder=2 # Ensure lines are drawn on top of the DPO shade
    )
    ax.fill_between(
        x_values_filtered,
        winrates_filtered[i] - errors_filtered[i],
        winrates_filtered[i] + errors_filtered[i],
        color=colors[i],
        alpha=0.1, # Lighter alpha for a more subtle shading
        zorder=1
    )

# --- 4. Customizing and Polishing the Plot ---
ax.set_xlabel('Variance')
ax.set_ylabel('Winrate')
ax.set_xticks(x_values_filtered)

# Place the legend outside the plotting area for clarity
ax.legend(
    ncol=3,
    #bbox_to_anchor=(1.04, 1), # Position to the top right, outside the plot
    loc='upper left',
    borderaxespad=0.
)

# Use a light grid on the y-axis only, which is less distracting
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.6)
ax.xaxis.grid(False) # No vertical grid lines

# Remove the top and right spines for a cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('grey')
ax.spines['bottom'].set_color('grey')

# Adjust layout to make room for the legend
fig.tight_layout(rect=[0, 0, 0.85, 1]) # rect=[left, bottom, right, top]
plt.savefig("variance_alpaca2.pdf")


winrates =np.array([[24.12935323, 24.12935323, 19.8630137,  17.91044776],
 [23.6318408,   23.88059701,  21.36645963 , 22.11180124]])
errors = np.array([[1.50991313, 1.50991313, 1.40742984, 1.35312959],
 [1.49915716, 1.50457037, 1.44558014, 1.46359146]])

x_values_filtered = np.array([ 0.0, 1.0, 2.0, 3.0])
winrates_filtered = winrates
errors_filtered = errors

winrate_DPO = 19.12
error_DPO = 1.668
# --- 3. Plotting ---
fig, ax = plt.subplots(figsize=(16, 7))

# --- DPO Baseline (drawn first) ---
ax.axhline(
    y=winrate_DPO, color='black', linestyle='--', linewidth=4,
    label='DPO', zorder=1
)
ax.axhspan(
    winrate_DPO - error_DPO, winrate_DPO + error_DPO,
    color='black', alpha=0.1, zorder=0
)

# --- Main Data Lines with a better color palette and markers ---
num_lines = len(labels)
# Use the 'viridis' colormap, which is excellent for data visualization
colors = plt.get_cmap('viridis')(np.linspace(0, 0.85, num_lines))
markers = ['o', 's', '^', 'D', 'v']  # Different marker for each line

for i in range(num_lines):
    ax.plot(
        x_values_filtered,
        winrates_filtered[i],
        label=labels[i],
        color=colors[i],
        marker=markers[i],
        markersize=15,
        linestyle='-',
        linewidth=4,
        zorder=2 # Ensure lines are drawn on top of the DPO shade
    )
    ax.fill_between(
        x_values_filtered,
        winrates_filtered[i] - errors_filtered[i],
        winrates_filtered[i] + errors_filtered[i],
        color=colors[i],
        alpha=0.1, # Lighter alpha for a more subtle shading
        zorder=1
    )

# --- 4. Customizing and Polishing the Plot ---
ax.set_xlabel('Variance')
ax.set_ylabel('Winrate')
ax.set_xticks(x_values_filtered)

# Place the legend outside the plotting area for clarity
ax.legend(
    ncol=3,
    #bbox_to_anchor=(1.04, 1), # Position to the top right, outside the plot
    loc='upper left',
    borderaxespad=0.
)

# Use a light grid on the y-axis only, which is less distracting
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.6)
ax.xaxis.grid(False) # No vertical grid lines

# Remove the top and right spines for a cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('grey')
ax.spines['bottom'].set_color('grey')

# Adjust layout to make room for the legend
fig.tight_layout(rect=[0, 0, 0.85, 1]) # rect=[left, bottom, right, top]
plt.savefig("variance_alpaca_mistral2.pdf")
