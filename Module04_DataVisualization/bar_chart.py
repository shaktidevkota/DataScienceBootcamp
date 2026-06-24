import matplotlib.pyplot as plt

#data 
products=["Laptop","Mouse","Keyboard","Monitor"]
sales=[120,250,180,90]

#bar chart
plt.bar(products, sales, color='skyblue',edgecolor='black')

#add title
plt.title("Product Sales")

#add x-axis
plt.xlabel('products')

#add y-axis
plt.ylabel('sales')

#ad grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()