def evaluate_response(response):

    scores = {
        "clarity": 8,
        "correctness": 8,
        "reasoning": 7
    }

    final_score = sum(scores.values()) / len(scores)

    return {
        "scores": scores,
        "final_score": final_score
    }