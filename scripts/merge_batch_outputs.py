import os
import json
import glob

data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
reviews_file = os.path.join(data_dir, "editorial_reviews.json")

with open(reviews_file, "r", encoding="utf-8") as f:
    master_reviews = json.load(f)

initial_count = len(master_reviews)
batch_files = glob.glob(os.path.join(data_dir, "batch_output_*.json"))

added_tools = []
for bf in batch_files:
    try:
        with open(bf, "r", encoding="utf-8") as f:
            batch_data = json.load(f)
            for tool_id, dossier in batch_data.items():
                if tool_id not in master_reviews:
                    master_reviews[tool_id] = dossier
                    added_tools.append(tool_id)
    except Exception as e:
        print(f"Error reading {bf}: {e}")

with open(reviews_file, "w", encoding="utf-8") as f:
    json.dump(master_reviews, f, indent=2, ensure_ascii=False)

print(f"Merge Complete! Initial: {initial_count}, Added: {len(added_tools)}, Total now: {len(master_reviews)}")
print("Newly added tools:", added_tools)
