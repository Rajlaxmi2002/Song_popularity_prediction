from src.SongPopularityPrediction.config.configuration import ConfigurationManager
from src.SongPopularityPrediction.components.data_transformation import DataTransformation
from src.SongPopularityPrediction import logger
from pathlib import Path

STAGE_NAME="Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):

        try:
            with open(Path("artifacts/data_validation/status.txt"),'r') as f:
                status=f.read().split(" ")[-1]

            if status=="True":
                config=ConfigurationManager()
                data_transformation_config=config.get_data_transformation_config()
                data_transformation=DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()

            else:
                raise Exception("Data schema not valid")
            
        except Exception as e:
            print(e)
        
