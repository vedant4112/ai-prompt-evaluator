import csv
from evaluator import evaluate_response

with open("prompts.txt") as f:
    prompts = f.readlines()

results = []

for prompt in prompts:
    prompt = prompt.strip()

    # simulated AI response
    answer = "Example AI response for: " + prompt

    score = evaluate_response(answer)

    results.append([
        prompt,
        score["scores"]["clarity"],
        score["scores"]["correctness"],
        score["scores"]["reasoning"],
        score["final_score"]
    ])

    print("\nPrompt:", prompt)
    print("Score:", score)

# save results
with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Prompt", "Clarity", "Correctness", "Reasoning", "Final Score"])
    writer.writerows(results)

print("\nResults saved to results.csv")