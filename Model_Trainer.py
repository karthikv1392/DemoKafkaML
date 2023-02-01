_Author_ = "Karthik Vaidhyanathan"
'''
This script takes the training data set form the path provided and trains the given ML model
'''

import numpy as np
from sklearn.linear_model import LinearRegression
from Initializer import Initialize
import csv
import pickle

init_obj = Initialize()

def file_reader():
    csv_file_name = init_obj.data_path + init_obj.data_file
    print (csv_file_name)
    x_list = []
    y_list = []
    row_count = 0
    with open (csv_file_name, 'r') as file_reader:
        csv_reader = csv.reader(file_reader, delimiter=',')

        for row in csv_reader:
            print (row)
            if row_count > 0:
                x_list.append(row[0])
                y_list.append(row[1])
            row_count+=1



    x_list = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
    y_list = np.array([5, 20, 14, 32, 22, 38])

    return x_list,y_list

def model_training(x_list,y_list):

    # X: Annual franchise price
    # Y: Startup cost

    x_val_list = np.array(x_list).reshape((-1, 1))
    y_val_list = np.array(y_list).reshape((-1, 1))
    model = LinearRegression()

    model.fit(x_val_list, y_val_list)

    model = LinearRegression().fit(x_val_list, y_val_list)

    r_sq = model.score(x_val_list, y_val_list)
    print(f"coefficient of determination: {r_sq}")
    print(f"intercept: {model.intercept_}")
    print(f"slope: {model.coef_}")

    model_obj = init_obj.model_path + init_obj.model_file
    pickle.dump(model, open(model_obj, 'wb'))


    '''
    new_model = LinearRegression().fit(x, y.reshape((-1, 1)))
    
    print(f"intercept: {new_model.intercept_}")
    print(f"slope: {new_model.coef_}")
    
    y_pred = model.predict(x)
    print(f"predicted response:\n{y_pred}")
    
    x_new =  np.array([5]).reshape((-1, 1))
    
    y_new = model.predict(x_new)
    print (y_new)
    '''

def predict_prize(franchise_fee):
    loaded_model = pickle.load(open(init_obj.model_path + init_obj.model_file, 'rb'))

    predicted_startup_cost = loaded_model.predict(franchise_fee)
    print (predicted_startup_cost[0][0])

if __name__ == '__main__':
    x_list, y_list = file_reader()
    model_training(x_list,y_list)
    franchise_fee = [1000]
    reshaped_franchise_fee = np.array(franchise_fee).reshape((-1,1))
    predict_prize(reshaped_franchise_fee)
