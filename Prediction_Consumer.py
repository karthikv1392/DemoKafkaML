_Author_ = "Karthik Vaidhyanathan"



from kafka import KafkaConsumer, KafkaProducer
from Initializer import Initialize
import json
import pickle
import numpy as np


init_object = Initialize()



class Prediction_Consumer():

    def predict_prize(self, franchise_fee):
        loaded_model = pickle.load(open(init_object.model_path + init_object.model_file, 'rb'))

        predicted_startup_cost = loaded_model.predict(franchise_fee)
        #print(predicted_startup_cost[0][0])
        return predicted_startup_cost[0][0]

    def gather_data(self):
        consumer = KafkaConsumer(auto_offset_reset='latest',
                                 bootstrap_servers=[init_object.kafka_host], api_version=(0, 10),
                                 consumer_timeout_ms=1000)

        consumer.subscribe(topics=['pizza'])  # Subscribe to a pattern

        while True:
            for message in consumer:
                if message.topic == "pizza":
                    pizza_val = (message.value.decode())
                    pizza_val_inference = [float(pizza_val)] # adding to list to later convert to array list
                    reshaped_franchise_fee = np.array(pizza_val_inference).reshape((-1, 1))
                    predicted_startup_cost = self.predict_prize(reshaped_franchise_fee)
                    print ("Predicted Cost ", predicted_startup_cost)



if __name__ == '__main__':
    pred_consumer = Prediction_Consumer()
    pred_consumer.gather_data()
