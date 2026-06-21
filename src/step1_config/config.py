import os

MODEL="sentence-transformers/all-MiniLM-L6-v2"

BASE_DIR=os.path.dirname(os.path.abspath(__file__))

TRAIN_PATH=os.path.join(BASE_DIR,"..","..","dataset","train.csv")
TEST_PATH=os.path.join(BASE_DIR,"..","..","dataset","test.csv")
OUTPUT_PATH=os.path.join(BASE_DIR,"..","..","output")

BATCH_SIZE=64
EPOCHS=3
MAX_SAMPLE=10000

TEST_SIZE=0.1
RANDOM_STATE=42

SIMILARITY_THRESHOLD=0.80