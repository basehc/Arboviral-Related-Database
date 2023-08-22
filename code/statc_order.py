import matplotlib.pyplot as plt
import seaborn as sns

# Count the frequency of viruses under each 'Order'
order_counts = data['Order'].value_counts()

# Plot the frequency distribution
plt.figure(figsize=(14, 6))
sns.barplot(x=order_counts.index, y=order_counts.values, palette="viridis")
plt.title('Frequency Distribution of Viruses by Order')
plt.xlabel('Order')
plt.ylabel('Number of Viruses')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

order_counts_df = order_counts.reset_index()
order_counts_df.columns = ['Order', 'Number of Viruses']
order_counts_df
