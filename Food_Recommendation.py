#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# Load the dataset
df = pd.read_csv('E:/Desktop/Spring2024/Capstone/ML/recipes.csv')

# Display the first few rows of the dataset to understand its structure
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Get insights into the distribution of data
print(df.describe())


# In[3]:


from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the cleaned ingredients
tfidf_matrix = tfidf_vectorizer.fit_transform(df['Cleaned_Ingredients'])

# Print the shape of the TF-IDF matrix
print("Shape of TF-IDF matrix:", tfidf_matrix.shape)


# In[5]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Load the dataset
df = pd.read_csv('E:/Desktop/Spring2024/Capstone/ML/recipes.csv')

# Initialize TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the cleaned ingredients
tfidf_matrix = tfidf_vectorizer.fit_transform(df['Cleaned_Ingredients'])

# Get user input for ingredients
user_input = input("Enter the ingredients (separated by commas): ")
user_ingredients = [ingredient.strip() for ingredient in user_input.split(',')]

# Transform user-entered ingredients using the same TF-IDF vectorizer
user_tfidf = tfidf_vectorizer.transform([' '.join(user_ingredients)])

# Calculate cosine similarity between user-entered ingredients and recipes
cosine_similarities = cosine_similarity(user_tfidf, tfidf_matrix)

# Get indices of recipes sorted by similarity
recipe_indices = cosine_similarities.argsort()[0][::-1]

# Number of top recommendations to display
top_n = 5

# Print top N recommended recipes
print(f"Top {top_n} recommended recipes based on user-entered ingredients:")
for i in range(top_n):
    recipe_index = recipe_indices[i]
    print(f"{i+1}. {df['Title'][recipe_index]}")
    print(f"   Ingredients:")
    for ingredient in eval(df['Ingredients'][recipe_index]):
        print(f"   - {ingredient}")
    print(f"   Instructions: {df['Instructions'][recipe_index]}")
    print(f"   Image: {df['Image_Name'][recipe_index]}")
    print()


# In[1]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from IPython.display import display, Image

# Load the dataset
df = pd.read_csv('E:/Desktop/Spring2024/Capstone/ML/recipes.csv')

# Initialize TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the cleaned ingredients
tfidf_matrix = tfidf_vectorizer.fit_transform(df['Cleaned_Ingredients'])

# Get user input for ingredients
user_input = input("Enter the ingredients (separated by commas): ")
user_ingredients = [ingredient.strip() for ingredient in user_input.split(',')]

# Transform user-entered ingredients using the same TF-IDF vectorizer
user_tfidf = tfidf_vectorizer.transform([' '.join(user_ingredients)])

# Calculate cosine similarity between user-entered ingredients and recipes
cosine_similarities = cosine_similarity(user_tfidf, tfidf_matrix)

# Get indices of recipes sorted by similarity
recipe_indices = cosine_similarities.argsort()[0][::-1]

# Number of top recommendations to display
top_n = 5

# Print top N recommended recipes
print(f"Top {top_n} recommended recipes based on user-entered ingredients:")
for i in range(top_n):
    recipe_index = recipe_indices[i]
    print(f"{i+1}. {df['Title'][recipe_index]}")
    print(f"   Ingredients:")
    for ingredient in eval(df['Ingredients'][recipe_index]):
        print(f"   - {ingredient}")
    print(f"   Instructions: {df['Instructions'][recipe_index]}")
    image_path = f"E:/Desktop/Spring2024/Capstone/ML/Food Images/Food Images/{df['Image_Name'][recipe_index]}.jpg"
    display(Image(filename=image_path))
    print()


# In[ ]:




