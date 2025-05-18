import pandas as pd
from recommender import recommend_actions

# Simulate one student record as a dictionary
student_data = {
    'quiz_score': 55,
    'video_watch_time': 100,
    'assignments_submitted': 2,
    'forum_posts': 1,
    'exam_score': 60,
    'login_frequency': 8,
    'study_hours_per_day': 1.5,
    'self_reported_mood': 3,
    'stress_level': 8,
    'focus_rating': 4
}

# Convert to DataFrame row (like real input)
row = pd.Series(student_data)

# Get suggestions
suggestions = recommend_actions(row)

# Print them
print("Suggestions:")
for s in suggestions:
    print("-", s)
