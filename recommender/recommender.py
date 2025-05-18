def recommend_actions(row):
    suggestions = []

    # Example rules — you can customize or expand this!
    if row['quiz_score'] < 60:
        suggestions.append("Review your quizzes and revise weak topics.")

    if row['video_watch_time'] < 150:
        suggestions.append("Watch more course videos to strengthen understanding.")

    if row['assignments_submitted'] < 4:
        suggestions.append("Submit all pending assignments on time.")

    if row['stress_level'] > 7:
        suggestions.append("Take regular breaks and manage your stress with relaxation techniques.")

    if row['focus_rating'] < 5:
        suggestions.append("Try Pomodoro technique or reduce distractions during study.")

    if row['login_frequency'] < 10:
        suggestions.append("Be more active. Try to log in daily to stay consistent.")

    if len(suggestions) == 0:
        suggestions.append("Great job! Keep up the good work and stay consistent.")

    return suggestions
