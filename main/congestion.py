def compute_congestion_score(review_count):
    if review_count >= 1000:
        return 10
    elif review_count >= 500:
        return 9
    elif review_count >= 400:
        return 8
    elif review_count >= 300:
        return 7
    elif review_count >= 200:
        return 6
    elif review_count >= 100:
        return 5
    elif review_count >= 50:
        return 4
    elif review_count >= 20:
        return 3
    elif review_count >= 5:
        return 2
    else:
        return 1