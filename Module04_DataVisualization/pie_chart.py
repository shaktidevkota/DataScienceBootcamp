import matplotlib.pyplot as plt

# Data
subjects = ["Python", "SQL", "Statistics", "Machine Learning", "Visualization"]
hours = [10, 6, 4, 8, 2]

# Create pie chart
plt.pie(hours, labels=subjects, autopct='%1.1f%%', startangle=90)

# Add title
plt.title('Study Hours Distribution by Subject')

# Ensure pie chart is a circle
plt.axis('equal')  

# Save the plot
plt.savefig('subjects_pie_chart.png', bbox_inches='tight')