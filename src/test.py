from step1_config.config import OUTPUT_PATH,TEST_PATH
from step3_data.loader import load_dataset
from step4_evaluation.tester import evaluate

def main():
    test_df=load_dataset(TEST_PATH)
    accuracy=evaluate(OUTPUT_PATH,test_df=test_df)
    if accuracy is not None:
        print(f"Test Accuracy: {accuracy:.2f}")


if __name__=="__main__":
    main()