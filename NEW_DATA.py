from opcua import Client
import paho.mqtt.client as mqtt
import numpy as np
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

with open('C:\\Users\\SMDDC\\Desktop\\LAVANYA DATA\\test_rig_ml_model.pkl','rb') as file:
    model = pickle.load(file)
client = Client("opc.tcp://192.168.100.0:4840")
client.session_timeout = 3000

# Set your username and password
client.set_user("ADMIN")
client.set_password("ADMIN123")

# Define MQTT broker settings
broker_address = "127.0.0.1"  # Replace with your MQTT broker address
port = 1883  # Replace with your MQTT broker port

# Create an MQTT client
client_to_node_red = mqtt.Client()

# Connect to the broker
client_to_node_red.connect(broker_address, port)

try:
    client.connect()
    print("Connected")

    while True:
        # Rest of your code remains the same...
        node_1 = client.get_node("ns=2;s=/Plc/DB190.DBD72:REAL")
        node_value_1 = node_1.get_value()
        client_to_node_red.publish("ns=2;s=/Plc/DB190.DBD72:REAL", np.around(node_value_1, 3))

        node_2 = client.get_node("ns=2;s=/Plc/DB190.DBD76:REAL")
        node_value_2 = node_2.get_value()
        client_to_node_red.publish("ns=2;s=/Plc/DB190.DBD76:REAL", np.around(node_value_2, 3))

        node_3 = client.get_node("ns=2;s=/Plc/DB190.DBD80:REAL")
        node_value_3 = node_3.get_value()
        client_to_node_red.publish("ns=2;s=/Plc/DB190.DBD80:REAL", np.around(node_value_3, 3))

        node_4 = client.get_node("ns=2;s=/Plc/DB190.DBD84:REAL")
        node_value_4 = node_4.get_value()
        client_to_node_red.publish("ns=2;s=/Plc/DB190.DBD84:REAL", np.around(node_value_4, 3))

        node_5 = client.get_node("ns=2;s=/Plc/DB190.DBD88:REAL")
        node_value_5 = node_5.get_value()
        client_to_node_red.publish("ns=2;s=/Plc/DB190.DBD88:REAL", np.around(node_value_5, 3))

        node_6 = client.get_node("ns=2;s=/Plc/DB190.DBD92:REAL")
        node_value_6 = node_6.get_value()
        client_to_node_red.publish("ns=2;s=/Plc/DB190.DBD92:REAL", np.around(node_value_6, 3))

        node_7 = client.get_node("ns=2;s=/Plc/DB190.DBD24:REAL")
        node_value_7 = node_7.get_value()
        client_to_node_red.publish("ns=2;s=/Plc/DB190.DBD24:REAL", np.around(node_value_7, 3))

        node_8 = client.get_node("ns=2;s=/Plc/DB190.DBD28:REAL")
        node_value_8 = node_8.get_value()
        client_to_node_red.publish("ns=2;s=/Plc/DB190.DBD28:REAL", np.around(node_value_8, 3))

        node_9 = client.get_node("ns=2;s=/Plc/DB190.DBD32:REAL")
        node_value_9 = node_9.get_value()
        client_to_node_red.publish("ns=2;s=/Plc/DB190.DBD32:REAL", np.around(node_value_9, 3))

        node_10 = client.get_node("ns=2;s=/Plc/DB190.DBD36:REAL")
        node_value_10 = node_10.get_value()
        client_to_node_red.publish("ns=2;s=/Plc/DB190.DBD36:REAL", np.around(node_value_10, 3))

        node_11 = client.get_node("ns=2;s=/Plc/DB190.DBD40:REAL")
        node_value_11 = node_11.get_value()
        client_to_node_red.publish("ns=2;s=/Plc/DB190.DBD40:REAL", np.around(node_value_11, 3))

        node_12 = client.get_node("ns=2;s=/Plc/DB190.DBD44:REAL")
        node_value_12 = node_12.get_value()
        client_to_node_red.publish("ns=2;s=/Plc/DB190.DBD44:REAL", np.around(node_value_12, 3))

        node_13 = client.get_node("ns=2;s=/Nck/MachineAxis/measPos1[2]")
        node_value_13 = node_13.get_value()
        client_to_node_red.publish("ns=2;s=/Nck/MachineAxis/measPos1[2]", np.around(node_value_13, 3))

        input_data = (node_value_1, node_value_4, node_value_2, node_value_3, node_value_5, node_value_6)
        # changing the input_data to a numpy array
        input_data_as_numpy_array = np.asarray(input_data)

        # reshape the np array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

        prediction = model.predict(input_data_reshaped)
        # print(prediction)

        if prediction[0] == 0:
            print('The data is bad')
            pred_value=0
        else:
            print('The data is good')
            pred_value = 1

        client_to_node_red.publish("prediction",pred_value )
finally:
    client.disconnect()
    client_to_node_red.disconnect()
