import pandas as pd

movies_data = {
    'Title': ['Inception', 'The Dark Knight', 'Interstellar', 'The Prestige', 'Memento'],
    'Genre': ['Sci-Fi', 'Action', 'Sci-Fi', 'Drama', 'Thriller'],
    'Keywords': ['dream heist', 'vigilante hero', 'space exploration', 'magicians rivalry', 'memory loss']
}
# print(movies_data)
movies = pd.DataFrame(movies_data)
print(movies)

movies['Combined_Features'] = movies['Genre'] + " " + movies['Keywords']

def recommend_movie(movie_title, movies_df):
    selected_movie = movies_df[movies_df['Title'] == movie_title]
    if selected_movie.empty:
        print(f"Movie '{movie_title}' not found in the dataset.")
        return
    
    selected_features = selected_movie.iloc[0]['Combined_Features']
    
    def calculate_similarity(features):
        selected_words = set(selected_features.split())
        current_words = set(features.split())
        return len(selected_words & current_words)
    
    movies_df['Similarity'] = movies_df['Combined_Features'].apply(calculate_similarity)
    recommended_movies = movies_df[movies_df['Title'] != movie_title].sort_values(by='Similarity', ascending=False)
    
    print(f"Movies similar to '{movie_title}':")
    for _, row in recommended_movies.head(3).iterrows():
        print(f"{row['Title']} (Similarity: {row['Similarity']})")

movie_input = input("Enter the movie title to find similar movies: ")
recommend_movie(movie_input, movies)
