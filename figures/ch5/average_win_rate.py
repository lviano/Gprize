import numpy as np
import matplotlib.pyplot as plt

winrates_alpaca_eval = {
    "DPO": np.array([53.42, 66.38, 67.10]),
    "IPO":  np.array([66.83, 53.75, 54.42]),
    "RPO": np.array([66.40, 66.25, 53.05]),
    "Distilled DPO": np.array([59.5, 67.33, 59.70]),
    "Ratings IPO": np.array([61.38, 63.76, 55.10]),
    "DPO + Distilled DPO": np.array([60.31, 65.63, 69.65]),
    "Ratings DPO": np.array([67.52, 67.87, 70.67])
}
winrates_alpaca_eval_with_distorted = {
    "DPO": np.array([53.42, 66.38, 67.10]),
    "IPO":  np.array([66.83, 53.75, 54.42]),
    "RPO": np.array([66.40, 66.25, 53.05]),
    "Distilled DPO": np.array([59.5, 67.33, 59.70]),
    "Ratings IPO": np.array([61.38, 63.76, 55.10]),
    "DPO + Distilled DPO": np.array([60.31, 65.63, 69.65]),
    "Ratings DPO": np.array([67.52, 67.87, 70.67]),
    "Distorted DPO": np.array([66.34, 60.77 , 68.62])
}
winrates_arena_hard = {
    "DPO": np.array([ 57.7, 77.3, 79.0]),
    "IPO":  np.array([ 78.2, 62.9, 85.9]),
    "RPO": np.array([69.1, 75.7, 61.0 ]),
    "Distilled DPO": np.array([64.4, 82.3, 75.10]),
    "Ratings IPO": np.array([68.3, 80.1, 75.7]),
    "DPO + Distilled DPO": np.array([ 66.8, 81.7, 85.4]),
    "Ratings DPO": np.array([75.2, 80.2, 82.9]),
}

winrates_arena_hard_with_distorted = {
    "DPO": np.array([ 57.7, 77.3, 79.0]),
    "IPO":  np.array([ 78.2, 62.9, 85.9]),
    "RPO": np.array([69.1, 75.7, 61.0 ]),
    "Distilled DPO": np.array([64.4, 82.3, 75.10]),
    "DPO + Distilled DPO": np.array([ 66.8, 81.7, 85.4]),
    "Ratings IPO": np.array([68.3, 80.1, 75.7]),
    "Ratings DPO": np.array([75.2, 80.2, 82.9]),
    "Distorted DPO": np.array([76.4, 87.1 ,81.8])
}


# --- Function to create a styled bar chart ---

def create_win_rate_histogram(data_dict, title, color_map='viridis', save_path=None,
label_colors = None):
    """
    Creates a bar chart and optionally saves it to a file.
    
    Args:
        data_dict (dict): Dictionary with method names as keys and numpy arrays of scores as values.
        title (str): The title for the plot.
        color_map (str): The matplotlib colormap to use for the bars.
        save_path (str, optional): The file path to save the plot (e.g., 'my_plot.pdf'). 
                                   If None, the plot is displayed instead.
    """
    labels = list(data_dict.keys())
    means = [np.mean(v) for v in data_dict.values()]
    stds = [np.std(v) for v in data_dict.values()]
    
    colors = plt.cm.get_cmap(color_map, len(labels))

    fig, ax = plt.subplots(figsize=(12, 7))
    
    ax.bar(labels, means, yerr=stds, align='center', alpha=0.9, ecolor='black', capsize=10, color=colors.colors)
    
    ax.set_ylabel('Win Rate', fontsize=22)
    ax.set_title(title, fontsize=22, fontweight='bold')
    ax.set_xticklabels(labels, fontsize=20, rotation=45, ha='right', fontweight='bold')
    ax.set_yticklabels(ax.get_yticklabels(), fontsize=20, rotation=45, ha='right')
    # --- Start of new code block for coloring labels ---
    if label_colors:
        # Get the xticklabels that have been created
        xtick_labels = ax.get_xticklabels()
        for label in xtick_labels:
            # Check if the label's text is in our color dictionary
            if label.get_text() in label_colors:
                # If it is, set the color for that label
                label.set_color(label_colors[label.get_text()])
    # --- End of new code block ---
    ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
    
    ax.set_ylim(bottom=0, top=max(means) + max(stds) + 10)
    
    for i, v in enumerate(means):
        ax.text(i, v + stds[i] + 1, f"{v:.2f}", ha='center', va='bottom', fontsize=25)

    plt.tight_layout()
    
    # This block checks if a save_path was provided.
    if save_path:
        # If yes, save the figure to the specified path.
        plt.savefig(save_path, bbox_inches='tight')
        print(f"Plot successfully saved to: {save_path}")
        plt.close(fig) # Close the figure to free up memory
    else:
        # If no, just show the plot on screen.
        plt.show()

# --- Generate the two plots ---
my_label_colors = {
    "Distorted DPO": 'orange',
    "DPO + Distilled DPO": 'blue',
    "Ratings IPO": 'blue',
    "Ratings DPO": 'blue'
}
# First plot: AlpacaEval
create_win_rate_histogram(
    winrates_alpaca_eval, 
    r'Average win rates vs $\pi_{\mathrm{ref}}$ on AlpacaEval',
    color_map='plasma',
    save_path='alpaca_eval_win_rates.pdf', # Provide the filename here,
    label_colors =my_label_colors
)

# Second plot: Arena Hard
create_win_rate_histogram(
    winrates_arena_hard, 
    r'Average win rates vs $\pi_{\mathrm{ref}}$ on Arena Hard',
    color_map='plasma',
    save_path='arena_hard_win_rates.pdf', # And here for the second plot,
    label_colors =my_label_colors
)

# First plot: AlpacaEval
create_win_rate_histogram(
    winrates_alpaca_eval_with_distorted, 
    r'Average win rates vs $\pi_{\mathrm{ref}}$ on AlpacaEval',
    color_map='plasma',
    save_path='alpaca_eval_win_rates_with_distorted.pdf', # Provide the filename here,
    label_colors =my_label_colors
)

# Second plot: Arena Hard
create_win_rate_histogram(
    winrates_arena_hard_with_distorted, 
    r'Average win rates vs $\pi_{\mathrm{ref}}$ on Arena Hard',
    color_map='plasma',
    save_path='arena_hard_win_rates_with_distorted.pdf', # And here for the second plot,
    label_colors =my_label_colors
)

gpt4_llama_alpaca_winrates_alpaca_eval ={
    "Llama-3.1-8B": np.array([22.11, 1.6]),
    "DPO": np.array([25.93, 1.55]),
    "IPO":  np.array([28.26, 1.584]),
    "RPO": np.array([29.25, 1.6]),
    "Distilled DPO": np.array([22.48, 1.47]),
    "Ratings IPO": np.array([25.50, 1.54]),
    "DPO + Distilled DPO": np.array([23.54, 1.5]),
    "Ratings DPO": np.array([29.19, 1.6]),
}

gpt4_mistral_alpaca_winrates_alpaca_eval ={
    "Mistral-7B": np.array([15.71, 1.282]),
    "DPO": np.array([19.12, 1.668]),
    "IPO":  np.array([17.33, 1.333]),
    "RPO": np.array([21.77, 1.456]),
    "Distilled DPO": np.array([23.48, 1.49]),
    "Ratings IPO": np.array([19.15, 1.389]),
    "DPO + Distilled DPO": np.array([23.57, 1.496]),
    "Ratings DPO": np.array([22.26, 1.468]),
}

gpt4_zephyr_alpaca_winrates_alpaca_eval ={
    "Zephyr-7B": np.array([15.11, 1.262]),
    "DPO": np.array([22.64, 1.477]),
    "IPO":  np.array([22.29, 1.470]),
    "RPO": np.array([15.67, 1.283]),
    "Distilled DPO": np.array([13.68, 1.213]),
    "Ratings IPO": np.array([13.17, 1.193]),
    "DPO + Distilled DPO": np.array([23.45, 1.494]),
    "Ratings DPO": np.array([23.38, 1.491]),
}

gpt4_llama_winrates_arena_eval ={
    "Llama-3.1-8B": np.array([14.7, 1.5]),
    "DPO": np.array([19.8, 1.55]),
    "IPO":  np.array([31.4, 2.2]),
    "RPO": np.array([25.9, 1.4]),
    "Distilled DPO": np.array([26.4, 1.7]),
    "Ratings IPO": np.array([26.9, 1.7]),
    "DPO + Distilled DPO": np.array([28.9, 1.6]),
    "Ratings DPO": np.array([35.4, 1.9]),
}

gpt4_mistral_winrates_arena_eval ={
    "Mistral-7B": np.array([1.6, 0.4]),
    "DPO": np.array([10.0, 1.2]),
    "IPO":  np.array([2.5, 0.5]),
    "RPO": np.array([8.2, 1.0]),
    "Distilled DPO": np.array([10.6, 1.3]),
    "Ratings IPO": np.array([14.1, 1.2]),
    "DPO + Distilled DPO": np.array([10.8, 1.0]),
    "Ratings DPO": np.array([14.1, 1.4]),
}

gpt4_zephyr_winrates_arena_eval ={
    "Zephyr-7B": np.array([2.0, 0.5]),
    "DPO": np.array([7.4, 0.9]),
    "IPO":  np.array([8.8, 0.8]),
    "RPO": np.array([7.9, 0.9]),
    "Distilled DPO": np.array([15.4, 1.0]),
    "Ratings IPO": np.array([13.4, 1.4]),
    "DPO + Distilled DPO": np.array([10.0, 1.1]),
    "Ratings DPO": np.array([16.2, 1.5]),
}

def create_win_rate_histogram_from_mean_and_variance(data_dict, title, color_map='plasma', save_path=None, label_colors=None):
    """
    Creates a bar chart and optionally saves it to a file.
    
    Args:
        data_dict (dict): Dictionary with method names as keys and numpy arrays of scores as values.
        title (str): The title for the plot.
        color_map (str): The matplotlib colormap to use for the bars.
        save_path (str, optional): The file path to save the plot (e.g., 'my_plot.pdf'). 
                                   If None, the plot is displayed instead.
    """
    labels = list(data_dict.keys())
    means = [v[0] for v in data_dict.values()]
    stds = [v[1] for v in data_dict.values()]
    
    colors = plt.cm.get_cmap(color_map, len(labels))

    fig, ax = plt.subplots(figsize=(12, 7))
    
    ax.bar(labels, means, yerr=stds, align='center', alpha=0.9, ecolor='black', capsize=10, color=colors.colors)
    
    ax.set_ylabel('Win Rate', fontsize=22)
    ax.set_title(title, fontsize=22, fontweight='bold')
    ax.set_xticklabels(labels, fontsize=20, rotation=45, ha='right', fontweight='bold')
    ax.set_yticklabels(ax.get_yticklabels(), fontsize=20, rotation=45, ha='right')
    # --- Start of new code block for coloring labels ---
    if label_colors:
        # Get the xticklabels that have been created
        xtick_labels = ax.get_xticklabels()
        for label in xtick_labels:
            # Check if the label's text is in our color dictionary
            if label.get_text() in label_colors:
                # If it is, set the color for that label
                label.set_color(label_colors[label.get_text()])
    # --- End of new code block ---
    ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
    
    ax.set_ylim(bottom=0, top=max(means) + max(stds) + 10)
    
    for i, v in enumerate(means):
        ax.text(i, v + stds[i] + 1, f"{v:.2f}", ha='center', va='bottom', fontsize=25)

    plt.tight_layout()
    
    # This block checks if a save_path was provided.
    if save_path:
        # If yes, save the figure to the specified path.
        plt.savefig(save_path, bbox_inches='tight')
        print(f"Plot successfully saved to: {save_path}")
        plt.close(fig) # Close the figure to free up memory
    else:
        # If no, just show the plot on screen.
        plt.show()

# AlpacaEval plots
for llm, dictio in zip(["Llama-3.1-8B",
 "Mistral-7B", "Zephyr-7B"], [gpt4_llama_alpaca_winrates_alpaca_eval,gpt4_mistral_alpaca_winrates_alpaca_eval, 
 gpt4_zephyr_alpaca_winrates_alpaca_eval]):
    create_win_rate_histogram_from_mean_and_variance(
    dictio, 
        f'{llm} on AlpacaEval',
        color_map='plasma',
        save_path=f'{llm}alpaca_eval_win_rates.pdf', # Provide the filename here
        label_colors=my_label_colors
    )

# Second plot: Arena Hard
for llm, dictio in zip(["Llama-3.1-8B",
 "Mistral-7B", "Zephyr-7B"], [gpt4_llama_winrates_arena_eval,gpt4_mistral_winrates_arena_eval, 
 gpt4_zephyr_winrates_arena_eval]):
    create_win_rate_histogram_from_mean_and_variance(
    dictio, 
        f'{llm} on ArenaHard',
        color_map='plasma',
        save_path=f'{llm}arena_hard_win_rates.pdf', # Provide the filename here
        label_colors=my_label_colors
    )