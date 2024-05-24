#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Modify the GET Example: Change the get_example function to fetch a list of posts instead of just one. Analyze the JSON structure and print out the titles of all posts.

import requests

def get_example():
    
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        print("GET request successful!")
        
        # Extracting JSON data
        posts = response.json()
        # Print each post as a separate dictionary
        for i, post in enumerate(posts, start=1):
            print(f"Post {i}:")
            print(post)
            print()  # Empty line for separation
        
        
        # Extracting JSON data
        titles = response.json()
        # Print titles of all posts
        print("Titles of all posts:")
        
        for i, title in enumerate(titles, start=1):
            print(print(f"Post {i} title:"), title['title'])
    else:
        print("Failed to retrieve data")

def main():
    
    print("Executing GET example...")
    get_example()

if __name__ == "__main__":
    main()


# In[ ]:




