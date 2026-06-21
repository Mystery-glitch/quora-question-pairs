from step1_config.config import OUTPUT_PATH,SIMILARITY_THRESHOLD
from step5_model.predictor import SBERTPredictor

predictor=SBERTPredictor(OUTPUT_PATH)

q1=input("Question 1: ")
q2=input("Question 2: ")
score=predictor.predict(q1,q2)

print(f"Similarity = {score:.2f}")
if score>=SIMILARITY_THRESHOLD: print("Duplicate")
else: print("Not Duplicate")