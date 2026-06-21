from sentence_transformers import InputExample

def create_example(df):
    return [
        InputExample(texts=[str(q1),str(q2)], label=float(label)
        ) for q1,q2,label in zip(df["question1"], df["question2"], df["is_duplicate"])
    ]