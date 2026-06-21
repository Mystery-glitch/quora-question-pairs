import os
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader
from sentence_transformers import SentenceTransformer,losses

from step1_config.config import *
from step2_utils.device import get_device
from step2_utils.logger import get_logger
from step3_data.examples import create_example
from step3_data.loader import load_dataset
from step4_evaluation.evaluator import build_evaluator

logger=get_logger(__name__)

def train_model():
    device=get_device()
    logger.info(f"Device: {device}")

    df=load_dataset(TRAIN_PATH,max_samples=MAX_SAMPLE)
    train_df,val_df=train_test_split(
        df,test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=df["is_duplicate"]
    )
    train_example=create_example(train_df)

    model=SentenceTransformer(MODEL,device=device)

    train_loader=DataLoader(
        train_example,
        batch_size=BATCH_SIZE,
        shuffle=True,
        num_workers=0
    )
    train_loss=losses.ContrastiveLoss(model)
    evalutor=build_evaluator(val_df)

    warmup_steps=int(len(train_loader)*EPOCHS*0.1)
    os.makedirs(OUTPUT_PATH,exist_ok=True)

    model.fit(
        train_objectives=[(train_loader, train_loss)],
        evaluator=evalutor,
        warmup_steps=warmup_steps,
        output_path=OUTPUT_PATH,
        save_best_model=True,
        show_progress_bar=True
    )