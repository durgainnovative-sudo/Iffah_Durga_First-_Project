# Iffah_Durga_First-_Project
##📊 Gender Analysis Project

**📌 Overview**
This project analyzes the gender pay gap across European countries using multiple datasets. It focuses on identifying trends over time, comparing countries, and understanding how inequality evolves across regions.

**🧠 Introduction**
Gender inequality in earnings remains a critical issue. This project provides a data-driven perspective on how the gender pay gap persists and changes across Europe.

**🎯 Objectives**
Analyze gender-based indicators across Europe
Understand trends over time
Compare data between countries
Perform data cleaning and transformation
Generate insights using Python

**📂 Data Sources**
This project combines data from multiple sources:

Eurostat API (via Eurostat)
Dataset: sdg_05_20 (Gender pay gap indicators)
Provides structured, up-to-date EU statistics
Local CSV Dataset
File: earn_gr_gpgr2ag
Contains gender pay gap by age group and sector
JSON Data File
File: sdg_05_20_page_jsonstat.json
Used for additional structured data extraction

**❓ Research Questions**
How has the gender pay gap changed over time in Europe?
Which countries show the highest and lowest gaps?
Is there a general trend toward equality?
How does Germany compare to the EU average?

**⚙️ Methodology**

**🔹 Data Collection**
Retrieved data using API requests
Loaded datasets from CSV and JSON files

**🔹 Data Cleaning**
Converted raw data into pandas DataFrames
Standardized column names and formats
Filtered relevant columns (country, year, values)
Handled missing values

**🔹 Data Analysis**
Grouped data by year and country
Calculated averages and trends
Compared Germany with EU-wide data

**🔹 Data Visualization**
📈 Average Gender Pay Gap Over Time

<img width="981" height="682" alt="Screenshot 2026-04-20 155446" src="https://github.com/user-attachments/assets/c6d46338-76ec-49d3-9449-2ce8e67c1b2b" />

📉 Germany Trend Over Time

<img width="862" height="631" alt="Screenshot 2026-04-20 155730" src="https://github.com/user-attachments/assets/04dd2b95-2f93-4b53-9578-53103f1c5de5" />

**🔍 Main Findings & Insights**
The gender pay gap is gradually decreasing across Europe
Progress is slow and inconsistent
Some countries show significantly better outcomes
Germany often remains above the EU average

**📊 Conclusions**

Although there is improvement, the gender pay gap persists across Europe. Differences between countries suggest that policies and labor market structures play an important role.

🔗** Resources**
Eurostat Data Portal: https://ec.europa.eu/eurostat
Dataset: Gender Pay Gap (sdg_05_20)
Kanban Board (e.g., Trello): https://trello.com/b/4qJRwJ29/my-first-project

**📁 Project Structure**

This project is organized under a main repository with multiple branches to separate work streams.

🔹 Repository
Iffah_Durga_First-_Project
🔹 Branches Overview
🌿 main branch
Contains the stable base of the project
Acts as the central repository for merged work
🌿 Durga branch

Focused on Gender Pay Gap Analysis

├── Gender_Analysis_dd.ipynb
├── README.md

**Work included:**

Gender pay gap data analysis
Data cleaning and transformation
Visualization (trends over time, country comparison)
Insights and conclusions

🌿 Iffah branch

Focused on Data Wrangling

├── Data_Wrangling_Iffah.ipynb
├── README.md

**Work included:**

Data cleaning and preprocessing
Handling missing values
Reshaping datasets
Preparing data for analysis

**🔄 Workflow Summary**
Each branch represents a separate stage of the data pipeline
Durga → Data preparation
Iffah → Analysis + visualization
main → consolidated project version
**This project follows a multi-branch workflow to simulate real-world data science collaboration using Git**.  
