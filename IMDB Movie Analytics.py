# # Feature Engineering

# In[4]:


#Classifying movies based on Rating as [Excellent, Good ,Bad]

def rating (rating):
    if rating >=7.0:
        return "Excellent"
    elif rating>=6.0:
        return "Good"
    else:
            return "Average"


# In[5]:


df['Rating_Category'] = df ['Rating'].apply(rating)


# In[6]:


df.head()


# In[7]:


#Extracting decades from the Year column to create a column called Decade

df['Decade']=df['Year'].apply(lambda x:x // 10*10)


# In[33]:


df['Decade']


# In[8]:


#Creating a new column for movie length categories

df['Movie_Length_Category']=pd.cut(df['Runtime (Minutes)'],bins=[0,60,120,np.inf], labels=['Short','Medium','Long'])


# In[9]:


df['Movie_Length_Category']


# In[11]:


#Effect of Movie Length on Ratings and Reviews

movie_length_analysis=df.groupby('Movie_Length_Category')[['Rating', 'Revenue (Millions)']].mean()

print(movie_length_analysis)


# In[16]:


import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt


# In[22]:


nltk.download()


# In[14]:


#Creating a keyword column from Description column


df['Keywords'] = df['Description'].apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in stopwords.words('english')]))


# In[24]:


df['Keywords']


# In[15]:


df['Description']


# In[9]:


get_ipython().system('python --version')


# In[6]:


get_ipython().system('pip install wordcloud')


# In[ ]:


df.columns


# In[6]:


#What is the Number of Action Movies

len(df[df['Genre'].str.contains('Action',case=False)])


# In[7]:


#Find Unique Values From Genre Column

df['Genre']


# In[49]:


#Adding a comma to separate each genre

list1=[]
for value in df['Genre']:
    list1.append(value.split(','))
    
list1

len(list1)


# In[9]:


list_2=[]
for item in list1:
    for item1 in item:
        list_2.append(item1)
        
list_2


# In[10]:


#Creating the unique list
list_3=[]
for item in list_2:
    if item not in list_3:
        list_3.append(item)

#Here are the unique lists
list_3


# In[12]:


len(list_3)


# In[13]:


#Count of films made under each Genre

list_2=[]
for item in list1:
    for item1 in item:
        list_2.append(item1)


# In[16]:


from collections import Counter


# In[17]:


Counter(list_2)


# In[46]:


df.info()


# In[48]:


#Distribution of Movie Keywords by Genre

# Get the unique genres
unique_genres = df['Genre'].unique()

# Loop through each unique genre
for genre in unique_genres:
    # Filter the keywords for the current genre
    genre_keywords = df[df['Genre'] == genre]['Keywords']
   
    # Create the word cloud
    wordcloud = WordCloud(width=800, height=400, random_state=42).generate(' '.join(genre_keywords))
   
    # Display the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(f'Movie Keywords for {genre}')
    plt.savefig(f'wordcloud_{genre}.png')


# In[50]:


df.head()


# In[51]:


#Distribution of Movie Keywords by Genre Decade

# Get the unique decades
unique_decades = df['Decade'].unique()

# Loop through each unique decade
for decade in unique_decades:
    # Filter the keywords for the current decade
    decade_keywords = df[df['Decade'] == decade]['Keywords']
   
    # Create the word cloud
    wordcloud = WordCloud(width=800, height=400, random_state=42).generate(' '.join(decade_keywords))
   
    # Display the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(f'Movie Keywords for {decade}s')
    plt.savefig(f'wordcloud_{decade}s.png')


# In[ ]:




