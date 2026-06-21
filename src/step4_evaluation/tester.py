from sklearn.metrics import accuracy_score

from step1_config.config import SIMILARITY_THRESHOLD
from step5_model.predictor import SBERTPredictor

def evaluate(path,test_df):
    predictor=SBERTPredictor(path=path)
    
    q1_list=test_df["question1"].tolist()
    q2_list=test_df["question2"].tolist()
    
    scores=predictor.predict_batch(q1_list,q2_list)
    predictions=(scores>=SIMILARITY_THRESHOLD).astype(int)
    
    if "is_duplicate" in test_df.columns:
        accuracy=accuracy_score(
            test_df["is_duplicate"],
            predictions
        )
        return accuracy
    else:
        import os
        import pandas as pd
        os.makedirs(path, exist_ok=True)
        output_df = test_df.copy()
        output_df["predicted_score"] = scores
        output_df["is_duplicate"] = predictions
        output_file = os.path.join(path, "predictions.csv")
        output_df.to_csv(output_file, index=False)
        print(f"No labels found in dataset. Saved predictions to {output_file}")
        return None