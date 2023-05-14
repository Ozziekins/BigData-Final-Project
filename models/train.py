from ModelService import ModelService
from SparkService import SparkService

SparkService()
service = ModelService()
service.retrainALS()
service.retrainBRP()