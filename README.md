# Python-Works

##IMDB Movie Data Analysis

###About:
IMDb (an abbreviation of Internet Movie Database) is an online database of information related to films, television series, home videos, video games, and streaming content. There are three kinds of users who engage themselves with YouTube: Video content creators, Video content lovers and Digital marketers who use YouTube advertising service to publicize their product and service information.

###Purposes Of the Project:
This project aims to understand the YouTube landscape to understand top performing branches and products, performance trend of different service providers, customer behavior.

###About Data:
The IMDB Movie dataset was obtained from the Kaggle , this dataset contains engagement information on the most subscribed YouTube channels. The data contains 12 columns and 1000 rows:

RangeIndex: 1000 entries, 0 to 999
Data columns (total 12 columns):
    Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   Rank                1000 non-null   int64  
 1   Title               1000 non-null   object 
 2   Genre               1000 non-null   object 
 3   Description         1000 non-null   object 
 4   Director            1000 non-null   object 
 5   Actors              1000 non-null   object 
 6   Year                1000 non-null   int64  
 7   Runtime (Minutes)   1000 non-null   int64  
 8   Rating              1000 non-null   float64
 9   Votes               1000 non-null   int64  
 10  Revenue (Millions)  872 non-null    float64
 11  Metascore           936 non-null    float64
dtypes: float64(3), int64(4), object(5)
memory usage: 93.9+ KB

###Analysis Prodedure

####Data Wrangling
Accessing the Data to check for data values using
df.isnull().sum()
and
per_missing =df.isnull() .sum() * 100 / len(df)
per_missing

####Exploratory Analysis and Visualization
 Exploratory data analysis is done to answer the listed questions and aims of this project.
1.	The year with the Highest Average Voting
2.	The year with the Highest Average Revenue
3.	The average rating for each director
4.	Movies having a runtime greater than 180
5.	The Top 10 lengthy Movie Title and Runtime
6.	The Number of Movies Per Year
7.	The Most Popular Movie Title Generating the highest revenue
8.	Top 10 Highest Rated Movie Titles and its Directors
9.	Top 10 Highest Revenue Movie Titles
10.	The Average Movie Rating Yearly
11.	The Effect of Rating on Revenue

####Feature engineering and Visualization
1.	Added a new column named “Rating_Category” where movies are classified based on rating as Excellent, Good, Bad.
2.	Added a new column named “Decade” from the year column using the floor function and division by 10. This column would be used to explore how movie genres and directors have evolved over time.
3.	Creating a new column for “movie length categories” by categorizing the Runtime (Minutes) column into categories like "Short" (less than 60 minutes), "Medium" (60-120 minutes), and "Long" (more than 120 minutes). This column would be used to explore the effect of Movie Length on Ratings and Reviews.
                         Rating  Revenue (Millions)
Movie_Length_Category                              
Short                       NaN                 NaN
Medium                 6.542194           63.716784
Long                   7.168512          124.723782
4.	Creating a “Keyword column” from “Description column” by extracting relevant keywords from the Description column using stopwords removal techniques.

####Visualizations created from these analysis and new columns are
1.	Distribution of Movie Keywords by Genre using WordCloud
 
 
2.	Distribution of Movie Keywords by Genre Decade using WordCloud
 
 
