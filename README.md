# Python-Works

## IMDB Movie Data Analysis

## About:
IMDb (an abbreviation of Internet Movie Database) is an online database of information related to films, television series, home videos, video games, and streaming content. The IMDB Movie dataset was obtained from the Kaggle, This dataset contains 12 columns and 1000 rows
RangeIndex: 1000 entries, 0 to 999
Data columns (total 12 columns):Rank, Title, Genre, Description, Director, Actors, Year, Runtime (Minutes), Rating, Votes, Revenue (Millions), Metascore,
 
## Purposes Of the Project:
This project aims to explore the IMDB platform to get insights on the movie trends within movie lovers and the movie industry.

## Analysis Prodedure

## 1. Data Wrangling
Accessing the Data to check for data values

## 2. Exploratory Analysis and Visualization
 Exploratory data analysis is done to answer the listed questions and aims of this project.
1.	The year with the Highest Average Voting 
3.	The year with the Highest Average Revenue
4.	The average rating for each director
5.	Movies having a runtime greater than 180
6.	The Top 10 lengthy Movie Title and Runtime
7.	The Number of Movies Per Year
8.	The Most Popular Movie Title Generating the highest revenue
9.	Top 10 Highest Rated Movie Titles and its Directors
10.	Top 10 Highest Revenue Movie Titles
11.	The Average Movie Rating Yearly
12.	The Effect of Rating on Revenue

## 3. Feature engineering and Visualization
1.	Added a new column named “Rating_Category” where movies are classified based on rating as Excellent, Good, Bad.
2.	Added a new column named “Decade” from the year column using the floor function and division by 10. This column would be used to explore how movie genres and directors have evolved over time.
3.	Creating a new column for “movie length categories” by categorizing the Runtime (Minutes) column into categories like "Short" (less than 60 minutes), "Medium" (60-120 minutes), and "Long" (more than 120 minutes). This column would be used to explore the effect of Movie Length on Ratings and Reviews.
4.	Creating a “Keyword column” from “Description column” by extracting relevant keywords from the Description column using stopwords removal techniques.

## Visualizations created from these analysis and new columns are
1.	Distribution of Movie Keywords by Genre using WordCloud
 
2.	Distribution of Movie Keywords by Decade using WordCloud
