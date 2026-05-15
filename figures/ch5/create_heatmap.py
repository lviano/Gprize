import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# --- 1. Data Definition ---
# Original data from the table
data_array = [np.array([
    [np.nan, 0.132, 0.392, 0.366, 0.067, 0.469, 0.067],
    [0.851, np.nan, 0.791, 0.790, 0.338, 0.854, 0.355],
    [0.565, 0.205, np.nan, 0.475, 0.121, 0.555, 0.121],
    [0.610, 0.210, 0.514, np.nan, 0.102, 0.583, 0.108],
    [0.928, 0.661, 0.886, 0.868, np.nan, 0.925, 0.498],
    [0.493, 0.139, 0.414, 0.401, 0.065, np.nan, 0.091],
    [0.923, 0.652, 0.869, 0.871, 0.487, 0.914, np.nan]
])
,
np.array([
    [np.nan, 0.068, 0.411, 0.421, 0.055, 0.516, 0.071],
    [0.932, np.nan, 0.894, 0.912, 0.470, 0.923, 0.528],
    [0.566, 0.113, np.nan, 0.490, 0.073, 0.588, 0.098],
    [0.579, 0.092, 0.517, np.nan, 0.071, 0.594, 0.107],
    [0.954, 0.523, 0.908, 0.913, np.nan, 0.948, 0.573],
    [0.496, 0.080, 0.399, 0.418, 0.050, np.nan, 0.071],
    [0.935, 0.475, 0.890, 0.882, 0.432, 0.937, np.nan]
]),
np.array([
    [np.nan, 0.056, 0.495, 0.473, 0.554, 0.613, 0.576],
    [0.947, np.nan, 0.949, 0.927, 0.950, 0.966, 0.953],
    [0.458, 0.055, np.nan, 0.448, 0.534, 0.586, 0.545],
    [0.501, 0.071, 0.493, np.nan, 0.564, 0.610, 0.586],
    [0.399, 0.049, 0.459, 0.416, np.nan, 0.575, 0.508],
    [0.389, 0.027, 0.394, 0.378, 0.451, np.nan, 0.433],
    [0.420, 0.040, 0.454, 0.420, 0.466, 0.564, np.nan]
]),
np.array([
    [np.nan, 0.511, 0.107, 0.368, 0.399, 0.052, 0.502, 0.062, 0.034, 0.042, 0.044, 0.053],
    [0.489, np.nan, 0.097, 0.358, 0.407, 0.063, 0.489, 0.061, 0.050, 0.048, 0.059, 0.043],
    [0.893, 0.903, np.nan, 0.850, 0.858, 0.311, 0.886, 0.326, 0.285, 0.313, 0.310, 0.291],
    [0.632, 0.642, 0.150, np.nan, 0.525, 0.079, 0.618, 0.109, 0.065, 0.077, 0.078, 0.084],
    [0.601, 0.593, 0.142, 0.475, np.nan, 0.078, 0.573, 0.088, 0.066, 0.083, 0.074, 0.068],
    [0.948, 0.937, 0.689, 0.921, 0.922, np.nan, 0.942, 0.503, 0.439, 0.460, 0.505, 0.463],
    [0.498, 0.511, 0.114, 0.382, 0.427, 0.058, np.nan, 0.068, 0.033, 0.045, 0.051, 0.044],
    [0.938, 0.939, 0.674, 0.891, 0.912, 0.497, 0.932, np.nan, 0.433, 0.448, 0.476, 0.459],
    [0.966, 0.950, 0.715, 0.935, 0.934, 0.561, 0.967, 0.567, np.nan, 0.520, 0.550, 0.520],
    [0.958, 0.952, 0.687, 0.923, 0.917, 0.540, 0.955, 0.552, 0.480, np.nan, 0.507, 0.487],
    [0.956, 0.941, 0.690, 0.922, 0.926, 0.495, 0.949, 0.524, 0.450, 0.493, np.nan, 0.486],
    [0.947, 0.957, 0.709, 0.916, 0.932, 0.537, 0.956, 0.541, 0.480, 0.513, 0.514, np.nan]
]),
np.array([
    [np.nan, 0.468, 0.042, 0.327, 0.321, 0.029, 0.429, 0.036, 0.042, 0.035, 0.042, 0.025],
    [0.532, np.nan, 0.051, 0.357, 0.369, 0.032, 0.505, 0.032, 0.057, 0.045, 0.054, 0.042],
    [0.958, 0.949, np.nan, 0.930, 0.931, 0.421, 0.957, 0.457, 0.519, 0.484, 0.481, 0.452],
    [0.673, 0.643, 0.070, np.nan, 0.529, 0.057, 0.669, 0.063, 0.088, 0.082, 0.096, 0.065],
    [0.679, 0.631, 0.069, 0.471, np.nan, 0.053, 0.641, 0.065, 0.074, 0.062, 0.074, 0.069],
    [0.971, 0.968, 0.579, 0.943, 0.947, np.nan, 0.974, 0.561, 0.591, 0.559, 0.554, 0.535],
    [0.571, 0.495, 0.043, 0.331, 0.359, 0.026, np.nan, 0.037, 0.051, 0.047, 0.050, 0.051],
    [0.964, 0.968, 0.543, 0.937, 0.935, 0.439, 0.963, np.nan, 0.546, 0.513, 0.506, 0.489],
    [0.958, 0.943, 0.481, 0.912, 0.926, 0.409, 0.949, 0.454, np.nan, 0.474, 0.467, 0.457],
    [0.965, 0.955, 0.516, 0.918, 0.938, 0.441, 0.953, 0.487, 0.526, np.nan, 0.496, 0.465],
    [0.958, 0.946, 0.519, 0.904, 0.926, 0.446, 0.950, 0.494, 0.533, 0.504, np.nan, 0.471],
    [0.975, 0.958, 0.548, 0.935, 0.931, 0.465, 0.949, 0.511, 0.543, 0.535, 0.529, np.nan]
]),
np.array([
    [np.nan, 0.340, 0.060, 0.329, 0.299, 0.379, 0.495, 0.405, 0.447, 0.022, 0.025, 0.032],
    [0.660, np.nan, 0.107, 0.466, 0.474, 0.557, 0.652, 0.590, 0.540, 0.046, 0.071, 0.054],
    [0.940, 0.893, np.nan, 0.868, 0.865, 0.905, 0.939, 0.915, 0.801, 0.236, 0.251, 0.238],
    [0.671, 0.534, 0.132, np.nan, 0.505, 0.569, 0.683, 0.593, 0.568, 0.048, 0.067, 0.054],
    [0.701, 0.526, 0.135, 0.495, np.nan, 0.582, 0.683, 0.597, 0.575, 0.053, 0.065, 0.049],
    [0.621, 0.443, 0.095, 0.431, 0.418, np.nan, 0.620, 0.510, 0.504, 0.039, 0.058, 0.038],
    [0.505, 0.348, 0.061, 0.317, 0.317, 0.380, np.nan, 0.418, 0.430, 0.026, 0.034, 0.024],
    [0.595, 0.410, 0.085, 0.407, 0.403, 0.490, 0.582, np.nan, 0.489, 0.034, 0.044, 0.033],
    [0.553, 0.460, 0.199, 0.432, 0.425, 0.496, 0.570, 0.511, np.nan, 0.071, 0.092, 0.066],
    [0.978, 0.954, 0.764, 0.952, 0.947, 0.961, 0.974, 0.966, 0.929, np.nan, 0.530, 0.486],
    [0.975, 0.929, 0.749, 0.933, 0.935, 0.942, 0.966, 0.956, 0.908, 0.470, np.nan, 0.457],
    [0.968, 0.946, 0.762, 0.946, 0.951, 0.962, 0.976, 0.967, 0.934, 0.514, 0.543, np.nan]
])
]
use_uncertainties = False
for data, scale in zip(data_array, ["135M", "360M", "1.7B", "135M_true_ratings", "360M_true_ratings", "1.7B_true_ratings"]):
    
    uncertainties = np.sqrt(data * (1 - data) / 805 * 25)
    # Row and column labels
    if "_true_" in scale:
        rows = [r"$\pi_{\mathrm{ref}}$", "DPO", "Ratings DPO", "Distilled DPO", "DPO + distilled DPO", "Ratings IPO", "IPO", "RPO",
        "Distorted DPO",  "DPO + Linear SFT","DPO + Step SFT", r"Ratings DPO with $R_{\min}$"]
        cols = rows
        if use_uncertainties: 
            fig, ax = plt.subplots(figsize=(25, 25))
        else: 
            fig, ax = plt.subplots(figsize=(14, 14))
    else:
        fig, ax = plt.subplots(figsize=(12, 8))
        rows = ["DPO", "Ratings DPO", "Distilled DPO", "DPO + distilled DPO", "Ratings IPO", "IPO", "RPO"]
        cols = ["DPO", "Ratings DPO", "Distilled DPO", "DPO + distilled DPO", "Ratings IPO", "IPO", "RPO"]
        if use_uncertainties: 
            fig, ax = plt.subplots(figsize=(24, 16))
        else: 
            fig, ax = plt.subplots(figsize=(12, 8))
    # --- 2. Uncertainty Calculation ---
    # The formula is value * (1 - value) / 805
    # We use a vectorized operation with NumPy. np.nan values will result in np.nan.
    
    # --- 3. Visualization Setup ---
    # Create a figure and axes for the plot
    

    # Define the custom colormap: red -> white -> green
    colors = [(0.5, 0, 0), (1,1,1), (1,1,1), (0, 0.9, 0), (0, 0.5, 0)]  # White, Green, Dark Green
    nodes = [0.0, 0.45, 0.55, 0.75, 1.0]
    custom_cmap = LinearSegmentedColormap.from_list("custom_div_cmap", list(zip(nodes, colors)))

    # Display the data as an image (heatmap)
    # vmin and vmax are set to 0 and 1 to ensure the color scale maps correctly
    im = ax.imshow(data, cmap=custom_cmap, vmin=0, vmax=1)

    # --- 4. Annotations and Labels ---
    # Loop over data dimensions and create text annotations.
    for i in range(len(rows)):
        for j in range(len(cols)):
            # Check if the value is not NaN (Not a Number)
            if not np.isnan(data[i, j]):
                value = data[i, j]
                value = np.round(value,2)
                uncertainty = uncertainties[i, j]
                # Format the text with the value and its uncertainty
                if use_uncertainties:
                    text_to_display = fr"{value:.2f}$\pm${uncertainty:.2f}"
                else:
                    text_to_display = f"{value:.2f}"
                ax.text(j, i, text_to_display, ha="center", va="center", color="black", fontsize=20)
            else:
                # Display a hyphen for NaN values (the diagonal)
                ax.text(j, i, "-", ha="center", va="center", color="black", fontsize=20)

    # Set the ticks and labels for x and y axes
    ax.set_xticks(np.arange(len(cols)))
    ax.set_yticks(np.arange(len(rows)))
    ax.set_xticklabels(cols, fontweight='bold', fontsize=20)
    ax.set_yticklabels(rows, fontweight='bold', fontsize=20)

    # Rotate the x-axis labels for better readability
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Set the title for the plot
    #ax.set_title("SmolLM2-135M Results @ Best Epoch", fontsize=16, pad=20)

    # Adjust layout to prevent labels from being cut off
    fig.tight_layout()

    # --- 5. Display the Plot ---
    if not use_uncertainties:
        plt.savefig(f"winrate{scale}.pdf")
    else:
        plt.savefig(f"winrate{scale}_errorbars.pdf")