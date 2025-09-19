ratings = {
    "Avi": {"3 Idiots": 5, "Dangal": 3, "Bahubali": 4},
    "Ravi": {"3 Idiots": 4, "Dangal": 5, "Bahubali": 2},
    "Anu": {"3 Idiots": 2, "Dangal": 4, "Bahubali": 5},
    "Raj": {"3 Idiots": 5, "Dangal": 2}
}


def user_similarity(u1, u2):
    
    common = set(ratings[u1]).intersection(ratings[u2])
    if not common:
        return 0  


    diff = sum(abs(ratings[u1][m] - ratings[u2][m]) for m in common)
    return 1 / (1 + diff)  

def recommend_for(user):
    scores = {}

    for other in ratings:
        if other == user:
            continue
        sim = user_similarity(user, other)

        for movie, rate in ratings[other].items():
            if movie not in ratings[user]:
                scores[movie] = scores.get(movie, 0) + sim * ra
    sorted_movies = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [movie for movie, score in sorted_movies]

user = "Raj"
print(f"Recommended movies for {user}: {recommend_for(user)}")
