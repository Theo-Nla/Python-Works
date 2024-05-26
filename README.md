# Python-Works

## IMDB Movie Data Analysis

## About:
IMDb (an abbreviation of Internet Movie Database) is an online database of information related to films, television series, home videos, video games, and streaming content. There are three kinds of users who engage themselves with YouTube: Video content creators, Video content lovers and Digital marketers who use YouTube advertising service to publicize their product and service information.

## Purposes Of the Project:
This project aims to understand the YouTube landscape to understand top performing branches and products, performance trend of different service providers, customer behavior.

## About Data:
The IMDB Movie dataset was obtained from the Kaggle , this dataset contains engagement information on the most subscribed YouTube channels. The data contains 12 columns and 1000 rows
RangeIndex: 1000 entries, 0 to 999
Data columns (total 12 columns):Rank, Title, Genre, Description, Director, Actors, Year, Runtime (Minutes), Rating, Votes, Revenue (Millions), Metascore,

## Analysis Prodedure

## 1. Data Wrangling
Accessing the Data to check for data values using
df.isnull().sum()
and
per_missing =df.isnull() .sum() * 100 / len(df)
per_missing

## 2. Exploratory Analysis and Visualization
 Exploratory data analysis is done to answer the listed questions and aims of this project.
1.	The year with the Highest Average Voting

![download (2)](https://github.com/Theo-Nla/Python-Works/assets/135545087/c0c238dd-dcd7-4b82-83fe-99f3c24b982b)
   
3.	The year with the Highest Average Revenue

![download (3)](https://github.com/Theo-Nla/Python-Works/assets/135545087/e1975bd9-2af5-48d4-9474-015bc1301918)

4.	The average rating for each director

![download (4)](https://github.com/Theo-Nla/Python-Works/assets/135545087/06c4ea18-8257-4ac4-8cfa-b9ea73db8e11)

5.	Movies having a runtime greater than 180



6.	The Top 10 lengthy Movie Title and Runtime

![download (5)](https://github.com/Theo-Nla/Python-Works/assets/135545087/f1162cde-89fb-4c3a-b981-ae4f938aab7c)

7.	The Number of Movies Per Year



8.	The Most Popular Movie Title Generating the highest revenue

    50    Star Wars: Episode VII - The Force Awakens
    Name: Title, dtype: object

9.	Top 10 Highest Rated Movie Titles and its Directors

![download (6)](https://github.com/Theo-Nla/Python-Works/assets/135545087/f1430d4f-5f29-43c7-98bf-0988e03298af)

10.	Top 10 Highest Revenue Movie Titles

![download (7)](https://github.com/Theo-Nla/Python-Works/assets/135545087/e03f9f79-241b-4a6d-b014-9960a5ee5d10)

11.	The Average Movie Rating Yearly
12.	The Effect of Rating on Revenue

![download (8)](https://github.com/Theo-Nla/Python-Works/assets/135545087/9fc4ef69-64ba-4864-b2e5-c1020b723a1d)

## 3. Feature engineering and Visualization
1.	Added a new column named “Rating_Category” where movies are classified based on rating as Excellent, Good, Bad.
2.	Added a new column named “Decade” from the year column using the floor function and division by 10. This column would be used to explore how movie genres and directors have evolved over time.
3.	Creating a new column for “movie length categories” by categorizing the Runtime (Minutes) column into categories like "Short" (less than 60 minutes), "Medium" (60-120 minutes), and "Long" (more than 120 minutes). This column would be used to explore the effect of Movie Length on Ratings and Reviews.
4.	Creating a “Keyword column” from “Description column” by extracting relevant keywords from the Description column using stopwords removal techniques.

## Visualizations created from these analysis and new columns are
1.	Distribution of Movie Keywords by Genre using WordCloud
 ![wordcloud_Comedy,Drama,Music](https://github.com/Theo-Nla/Python-Works/assets/135545087/7fa4e059-db00-498e-98ec-1c3350bd0556)
 
2.	Distribution of Movie Keywords by Decade using WordCloud
 ![wordcloud_2000s](https://github.com/Theo-Nla/Python-Works/assets/135545087/86a1574a-ee3d-47c7-94ed-126dca7643dc)

 ![wordcloud_2010s](https://github.com/Theo-Nla/Python-Works/assets/135545087/b23c2cc3-4190-4f17-ba87-2d5763bc9cdf)
