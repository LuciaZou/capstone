# Liquor Sales Prediction

## Project Overview

### Problem Area
 Our project focuses on helping liquor stores deal with lots of sales data. The main problem is turning this raw data into useful information.  The core issue lies in transforming this raw data into actionable insights, crucial for optimizing inventory, increasing sales, enhancing customer experiences, and making informed business decisions.

### Areas Affected
Inventory Optimization: Efficient stock management minimizes losses and ensures popular items are always in stock.

Sales Enhancement: Understanding customer preferences enables targeted marketing and product promotions, resulting in promoted sales revenue.

Future Expansion: Analyzing regional sales data helps identify optimal locations for new stores.

Customer Satisfiction: Enriches customer satisfaction and fosters loyalty by suggusting popular products.


## Proposed Data Science Solution

### Approach:
Exploratory Data Analysis (EDA): Conduct a profound analysis of historical sales data, identifying trends, seasonality, and customer preferences.

Location Analysis: Utilize geospatial data analysis to get optimal locations for new stores based on demographic information and sales trends.  Use visualization tools to draw maps.

### Impact of the Solution
Revenue Boost: Targeted marketing and personalized customer experiences will significantly increase sales, leaeding revenue growth.

Operational Efficiency: Optimized inventory management will reduce wastage and enhance efficiency, driving to cost savings.

Strategic Growth: Informed decisions about store locations will ensure successful expansions, maximizing profitability.

Enhanced Customer Satisfaction: Personalized offerings and a well-stocked inventory tailored to customer preferences will increase satisfaction levels.

### Description of the Dataset
From: https://www.kaggle.com/datasets/gabrielramos87/iowa-sales-liquor-jan-2021jan-2022 

The dataset contains:
Temporal Data: Date of orders.

Product Insights: invoice_and_item_number, item_number, item_description, volume_sold_liters, volume_sold_gallons category, category_name and sale_dollars.

Geospatial Data: address, city, zip_code, store_location, county_number and county.

Sales Metrics: pack, bottle_volume_ml, state_bottle_cost, state_bottle_retail, bottles_sold.         

The original data has 2805307 rows and 24 columns.


### Important Features
1. sale_dollars: total cost of liquor order (number of bottles multiplied by the state bottle retail).
2. county: county where the store who ordered the liquor is located.
3. category: category code associated with the liquor ordered.
4. vendor_name: the vendor name of the company for the brand of liquor ordered.
5. item_number: item number for the individual liquor product ordered.
6. item_description: description of the individual liquor product ordered.
7. date: date of order.
8. store_name: name of store who ordered the liquor.
