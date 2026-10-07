def update_score(current_score):
    return max(0, current_score - 10)


def get_score_rating(final_score):
    if final_score >= 80:
        return "Excellent"
    elif final_score >= 50:
        return "Good"
    else:
        return "Keep Practicing"


if __name__ == "__main__":
    print("Testing score module...")
    s = 100
    s = update_score(s)
    print(f"Score after 1 wrong guess: {s}")
    print(f"Rating for score 90: {get_score_rating(s)}")