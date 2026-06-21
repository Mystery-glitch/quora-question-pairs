from sentence_transformers.evaluation import BinaryClassificationEvaluator

def build_evaluator(validation_df):
    return BinaryClassificationEvaluator(
        sentences1=validation_df["question1"].tolist(),
        sentences2=validation_df["question2"].tolist(),
        labels=validation_df["is_duplicate"].tolist(),

        name="Validation"
    )