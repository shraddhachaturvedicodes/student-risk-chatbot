def generate_gpt_prompt(dropout_risk, predicted_score):
    if dropout_risk:
        return (
            f"The student is at risk of dropping out and is predicted to score around {predicted_score}% in the final exam. "
            "Give an empathetic message and ask if they want improvement suggestions."
        )
    else:
        return (
            f"The student is not at risk and is expected to score {predicted_score}%. "
            "Congratulate them and ask if they want tips to improve even more."
        )