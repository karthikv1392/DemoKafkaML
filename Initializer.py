_Author_ = "Karthik Vaidhyanathan"

import traceback
import yaml

'''
This class is responsible for initializing the different configurations required to execute the program
'''

class Initialize():
    def __init__(self):
        try:
            with open("config.yml", "r") as f:
                config = yaml.load(f, Loader=yaml.FullLoader)
                print(config)
                self.data_path = config["settings"]["data_path"]
                self.data_file = config["settings"]["data_file"]
                self.stream_file = config["settings"]["stream_file"]
                self.model_path = config["model"]["model_path"]
                self.model_file = config["model"]["model_file"]
                self.kafka_host = config["settings"]["kafka_host"]

        except Exception as e:
            traceback.print_exc()