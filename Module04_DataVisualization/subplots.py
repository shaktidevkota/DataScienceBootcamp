import matplotlib.pyplot as plt

# Datasets
subjects = ["Python", "SQL", "Statistics", "Machine Learning", "Visualization"]
hours = [10, 6, 4, 8, 2]
marks = [45, 50, 52, 55, 58, 60, 62, 65, 68, 70, 72, 75, 98]

# Sorting bar chart data for better visualization structure
sorted_bar_data = sorted(zip(hours, subjects), reverse=True)
sorted_hours, sorted_subjects = zip(*sorted_bar_data)

# Set up the figure size for a 2x2 grid
plt.figure(figsize=(12, 10))

# --- 1. Line Chart (Top Left) ---
plt.subplot(2, 2, 1)
plt.plot(subjects, hours, marker='o', color='royalblue', linewidth=2)
plt.title('Study Hours Profile')
plt.ylabel('Hours')
plt.xticks(rotation=30, ha='right')
plt.grid(True, linestyle='--', alpha=0.5)

# --- 2. Bar Chart (Top Right) ---
plt.subplot(2, 2, 2)
plt.bar(sorted_subjects, sorted_hours, color='coral', edgecolor='black')
plt.title('Study Hours (Sorted)')
plt.ylabel('Hours')
plt.xticks(rotation=30, ha='right')

# --- 3. Histogram (Bottom Left) ---
plt.subplot(2, 2, 3)
plt.hist(marks, bins=6, color='mediumseagreen', edgecolor='black', alpha=0.8)
plt.title('Frequency of Marks')
plt.xlabel('Marks Bands')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.5)

# --- 4. Box Plot (Bottom Right) ---
plt.subplot(2, 2, 4)
# FIX: 'labels' updated to 'tick_labels' to prevent the TypeError
plt.boxplot(marks, tick_labels=['Students'])
plt.title('Marks Outlier Detection')
plt.ylabel('Marks')
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Adjust layout automatically to eliminate overlapping text
plt.tight_layout()

# Save dashboard 
plt.savefig('dashboard_2x2.png', bbox_inches='tight')
print("Dashboard saved successfully as 'dashboard_2x2.png'!")
plt.show()