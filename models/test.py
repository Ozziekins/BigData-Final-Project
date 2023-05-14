from ModelService import ModelService
from SparkService import SparkService

SparkService()
service = ModelService()
print(service.predictItems([[11130],[3711]],5))
print(service.predictUsers([[777316],[77313]],5))
