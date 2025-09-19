# Movie Recommendation System using Collaborative Filtering
# Suggests movies based on similar users' preferences

# Step 1: Sample data - Users and their movie ratings (1 to 5)
ratings = {
    "Avi": {"3 Idiots": 5, "Dangal": 3, "Bahubali": 4},
    "Ravi": {"3 Idiots": 4, "Dangal": 5, "Bahubali": 2},
    "Anu": {"3 Idiots": 2, "Dangal": 4, "Bahubali": 5},
    "Raj": {"3 Idiots": 5, "Dangal": 2}
}

# Step 2: Function to check how similar two users are
def user_similarity(u1, u2):
    # Find movies rated by both users
    common = set(ratings[u1]).intersection(ratings[u2])
    if not common:
        return 0  # No common movies, so no similarity

    # Calculate difference in ratings
    diff = sum(abs(ratings[u1][m] - ratings[u2][m]) for m in common)
    return 1 / (1 + diff)  # Lower difference means higher similarity

# Step 3: Recommend movies for a user
def recommend_for(user):
    scores = {}

    for other in ratings:
        if other == user:
            continue
        sim = user_similarity(user, other)

        # For movies user has not seen, add weighted score
        for movie, rate in ratings[other].items():
            if movie not in ratings[user]:
                scores[movie] = scores.get(movie, 0) + sim * rate

    # Sort movies by highest score
    sorted_movies = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [movie for movie, score in sorted_movies]

# Step 4: Test the system
user = "Raj"
print(f"Recommended movies for {user}: {recommend_for(user)}")
