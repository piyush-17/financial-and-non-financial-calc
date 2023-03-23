import pandas as pd
import matplotlib.pyplot as plt

# Load data for company 1
data1 = pd.read_csv('company1_data.csv')

# Load data for company 2
data2 = pd.read_csv('company2_data.csv')

# Calculate key financial metrics for company 1
data1['profit'] = data1['revenue'] - data1['cost_of_goods_sold']
data1['gross_profit_margin'] = data1['profit'] / data1['revenue']
data1['operating_profit_margin'] = data1['profit'] / (data1['revenue'] - data1['operating_expenses'])

# Calculate key financial metrics for company 2
data2['profit'] = data2['revenue'] - data2['cost_of_goods_sold']
data2['gross_profit_margin'] = data2['profit'] / data2['revenue']
data2['operating_profit_margin'] = data2['profit'] / (data2['revenue'] - data2['operating_expenses'])

# Calculate non-financial metrics for company 1
customer_satisfaction1 = data1['customer_satisfaction'].mean()
employee_turnover1 = data1['employee_turnover'].mean()

# Calculate non-financial metrics for company 2
customer_satisfaction2 = data2['customer_satisfaction'].mean()
employee_turnover2 = data2['employee_turnover'].mean()

# Compare financial metrics for the two companies
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10,5))

ax1.plot(data1['year'], data1['revenue'], label='Samsung')
ax1.plot(data2['year'], data2['revenue'], label='Apple')
ax1.set_xlabel('Year')
ax1.set_ylabel('Revenue')
ax1.set_title('Revenue Over Time')
ax1.legend()

ax2.bar(['Gross Profit Margin', 'Operating Profit Margin'], 
        [data1.loc[0, 'gross_profit_margin'], data1.loc[0, 'operating_profit_margin']],
        label='Samsung - Year 1', width=0.4)
ax2.bar(['Gross Profit Margin', 'Operating Profit Margin'], 
        [data1.loc[1, 'gross_profit_margin'], data1.loc[1, 'operating_profit_margin']],
        label='Samsung - Year 2', width=0.4, alpha=0.5)
ax2.bar(['Gross Profit Margin', 'Operating Profit Margin'], 
        [data2.loc[0, 'gross_profit_margin'], data2.loc[0, 'operating_profit_margin']],
        label='Apple - Year 1', width=0.4, align='edge', edgecolor='black')
ax2.bar(['Gross Profit Margin', 'Operating Profit Margin'], 
        [data2.loc[1, 'gross_profit_margin'], data2.loc[1, 'operating_profit_margin']],
        label='Apple - Year 2', width=-0.4, align='edge', edgecolor='black', alpha=0.5)
ax2.set_xlabel('Financial Metrics')
ax2.set_ylabel('Percentage')
ax2.set_title('Financial Metrics Comparison')
ax2.legend()

plt.tight_layout()
plt.show()

# Compare non-financial metrics for the two companies
# Calculate non-financial metrics for company 1
customer_satisfaction1 = data1['customer_satisfaction'].mean()
employee_turnover1 = data1['employee_turnover'].mean()

# Calculate non-financial metrics for company 2
customer_satisfaction2 = data2['customer_satisfaction'].mean()
employee_turnover2 = data2['employee_turnover'].mean()

# Compare non-financial metrics for the two companies
fig, ax = plt.subplots()

ax.bar(['Customer Satisfaction', 'Employee Turnover'], [customer_satisfaction1, employee_turnover1], 
       label='Samsung', width=0.4)
ax.bar(['Customer Satisfaction', 'Employee Turnover'], [customer_satisfaction2, employee_turnover2], 
       label='Apple', width=-0.4, align='edge', edgecolor='black', alpha=0.5)
ax.set_xlabel('Non-Financial Metrics')
ax.set_ylabel('Average Score')
ax.set_title('Non-Financial Metrics Comparison')
ax.legend()

plt.tight_layout()
plt.show()
if data1['profit'].mean() > data2['profit'].mean():
    profitability = 'Samsung is more profitable than Apple.'
else:
    profitability = 'Apple is more profitable than Samsung.'

if customer_satisfaction1 > customer_satisfaction2:
    customer_satisfaction = 'Customers are more satisfied with Samsung than Apple.'
else:
    customer_satisfaction = 'Customers are more satisfied with Apple than Samsung.'

if employee_turnover1 < employee_turnover2:
    employee_turnover = 'Samsung has a lower employee turnover rate than Apple.'
else:
    employee_turnover = 'Apple has a lower employee turnover rate than Samsung.'

print('Based on the analysis of financial and non-financial metrics, the following conclusions can be made:\n')
print(profitability)
print(customer_satisfaction)
print(employee_turnover)
