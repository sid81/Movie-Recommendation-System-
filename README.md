# Movie-Recommendation-System-

A content-based recommender system that recommends movies similar to that kind of genre/movie.<br>
Link to the dataset:-https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

## Overview
The movies are recommended based on the content of the movie you entered or selected. The main parameters that are considered for the recommendations are the genre,
director,overview and top 3 crew/casts.Then with the help of countvectorizer it will form a 4800*5000 dimension space,where we are going to calculate cosine similarity of ecach vector 
with respect to all the other vectors.The distance between two vectors is inversly proportional to their similarity.

## How Cosine Similarity works?
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size.
Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space.
The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), 
chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.
![70401457-a7530680-1a55-11ea-9158-97d4e8515ca4](https://user-images.githubusercontent.com/68815179/199078322-f405f453-52cd-409d-8a35-b59224a56e9e.png)

