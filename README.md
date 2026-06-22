# Zuber Project
Python / SQL Project

# Chicago Taxi Market Data Analysis — Sprint 8

## Project Overview
This project is part of Sprint 8 of the Data Analytics course. It consists of an exploratory data analysis of the taxi market in Chicago for Zuber, a new ride-sharing company launching in the city.

## Objectives
- Analyze patterns in Chicago taxi ride data
- Identify the leading taxi companies and their market share
- Determine the most popular neighborhoods as ride destinations
- Test hypotheses about the impact of weather conditions on ride duration

## Datasets

### Dataset 1: Taxi Companies (project_sql_result_01.csv)
- company_name: Taxi company name
- trips_amount: Number of trips per company (November 15–16, 2017)

### Dataset 2: Neighborhood Destinations (project_sql_result_04.csv)
- dropoff_location_name: Chicago neighborhoods where rides ended
- average_trips: Average number of rides ending in each neighborhood (November 2017)

### Dataset 3: Loop–Airport Rides (project_sql_result_07.csv)
- start_ts: Ride start date and time
- weather_conditions: Weather conditions at the start of the ride
- duration_seconds: Ride duration in seconds

## Methodology

### 1. Exploratory Data Analysis
- Initial dataset import and inspection
- Data type validation and structure review
- Identification of the top 10 taxi companies by volume
- Analysis of the top 10 neighborhoods by drop-off frequency

### 2. Data Visualization
- Bar chart: Taxi companies by number of trips
- Bar chart: Top 10 neighborhoods by destination volume
- Visual analysis of patterns and trends

### 3. Hypothesis Testing
- Null Hypothesis (H₀): The average duration of rides from the Loop to O'Hare International Airport does NOT change on rainy Saturdays
- Alternative Hypothesis (H₁): The average duration of rides from the Loop to O'Hare International Airport DOES change on rainy Saturdays
- Significance level: α = 0.05
- Method: Student's t-test for independent samples

## Libraries Used
- **pandas:** Data manipulation and analysis
- **matplotlib:** Data visualization
- **scipy:** Statistical testing
- **numpy:** Numerical operations
- **math:** Basic mathematical operations

## Key Findings

### Taxi Companies
- Flash Cab leads the market with approximately 20,000 trips during the analyzed period
- Taxi Affiliation Services ranks second with approximately 11,400 trips
- A significant gap exists between the top two companies and the remainder of the market

## Project Structure
