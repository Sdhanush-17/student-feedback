# score_calculator.py

def calculate_average(feedback_list):
    if not feedback_list:
        return 0
    total_score = sum(entry['score'] for entry in feedback_list)
    return total_score / len(feedback_list)
