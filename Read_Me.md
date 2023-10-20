{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "0ef0c490",
   "metadata": {},
   "source": [
    "# Liquor Sales Prediction\n",
    "\n",
    "## Project Overview\n",
    "\n",
    "### Objective\n",
    "The dataset captures spirits purchase data of Iowa Class 'E' liquor license holders spanning from January 2021 to January 2022. This comprehensive dataset allows in-depth analysis of product sales at the store level. By leveraging machine learning, the project aims to predict future sales, empowering store owners to optimize operations and maximize revenue. With its richness in data, the dataset holds significant potential for valuable insights.\n",
    "\n",
    "### Areas Affected\n",
    "Inventory Optimization: Efficient stock management minimizes losses and ensures popular items are always in stock.\n",
    "\n",
    "Sales Enhancement: Understanding customer preferences enables targeted marketing and product promotions, resulting in promoted sales revenue.\n",
    "\n",
    "Future Expansion: Analyzing regional sales data helps identify optimal locations for new stores.\n",
    "\n",
    "Customer Satisfiction: Enriches customer satisfaction and fosters loyalty by suggusting popular products.\n",
    "\n",
    "\n",
    "## Proposed Data Science Solution\n",
    "\n",
    "### Approach:\n",
    "Exploratory Data Analysis (EDA): Conduct a profound analysis of historical sales data, identifying trends, seasonality, and customer preferences.\n",
    "\n",
    "Location Analysis: Utilize geospatial data analysis to get optimal locations for new stores based on demographic information and sales trends.  Use visualization tools to draw maps.\n",
    "\n",
    "### Impact of the Solution\n",
    "Revenue Boost: Targeted marketing and personalized customer experiences will significantly increase sales, leaeding revenue growth.\n",
    "\n",
    "Operational Efficiency: Optimized inventory management will reduce wastage and enhance efficiency, driving to cost savings.\n",
    "\n",
    "Strategic Growth: Informed decisions about store locations will ensure successful expansions, maximizing profitability.\n",
    "\n",
    "Enhanced Customer Satisfaction: Personalized offerings and a well-stocked inventory tailored to customer preferences will increase satisfaction levels.\n",
    "\n",
    "### Description of the Dataset\n",
    "From: https://www.kaggle.com/datasets/gabrielramos87/iowa-sales-liquor-jan-2021jan-2022 \n",
    "\n",
    "The dataset contains:\n",
    "Temporal Data: Date of orders.\n",
    "\n",
    "Product Insights: invoice_and_item_number, item_number, item_description, volume_sold_liters, volume_sold_gallons category, category_name and sale_dollars.\n",
    "\n",
    "Geospatial Data: address, city, zip_code, store_location, county_number and county.\n",
    "\n",
    "Sales Metrics: pack, bottle_volume_ml, state_bottle_cost, state_bottle_retail, bottles_sold.         \n",
    "\n",
    "The original data has 2805307 rows and 24 columns.\n",
    "\n",
    "\n",
    "### Important Features\n",
    "1. sale_dollars: total cost of liquor order (number of bottles multiplied by the state bottle retail).\n",
    "2. county: county where the store who ordered the liquor is located.\n",
    "3. category: category code associated with the liquor ordered.\n",
    "4. vendor_name: the vendor name of the company for the brand of liquor ordered.\n",
    "5. item_number: item number for the individual liquor product ordered.\n",
    "6. item_description: description of the individual liquor product ordered.\n",
    "7. date: date of order.\n",
    "8. store_name: name of store who ordered the liquor.\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "basicpythonkernel",
   "language": "python",
   "name": "basicpythonkernel"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
