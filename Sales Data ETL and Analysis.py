import pandas as pd

df = pd.read_csv(r"C:\Users\Ganesh pendem\Downloads\sales.csv") #Load Data Set

#print(df.head()) # View Top Rows

df['Date']=pd.to_datetime(df['Date']) #Correct the date formate
df['Total_sales']=df['Quantity']*df['Unit_Price']  #adding new column as Total_Sales

#print(df.head())

#importing SQL
import sqlite3

conn= sqlite3.connect('sales_data.db') # Create a connection to SQLite DB 
df.to_sql('Sales', conn, if_exists='replace', index=False) # Write the DataFrame to SQLite table
print("Data Inserted into sql 'Sales' table sucessfully.")

# Preview the first 5 Rows
query= "Select * from Sales lIMIT 5" 
result= pd.read_sql_query(query, conn)
print(result)
conn.close() # Dont forget to close the conncetion at the end 

# Reconnect to DB
conn = sqlite3.connect('sales_data.db')

#Total Sales by Region
query="""
Select Region, Round(sum(Total_sales), 2) as Total_Revenue
from Sales
Group by Region
order by Total_Revenue
"""
df_region=pd.read_sql_query(query, conn)
print("Total_sales_by_Region")
print(df_region)

#Top 3 Selling Products

query="""
Select Product, Round(sum(Total_Sales), 2) as Revenue
from Sales
Group by Product
order by Revenue DESC
limit 3
"""

df_top_product=pd.read_sql_query(query, conn)
print("Top_3_Selling Products")
print(df_top_product)

# Monthly Sales Data
quer="""
Select strftime('%Y-%M', Date) as Month, Round(sum(Total_sales), 2) as Monthly_sales
from Sales
group by Month
order by Month
"""

df_monthly=pd.read_sql_query(query, conn)
print("Monthly_Sales_Data")
print(df_monthly)

conn.close()


