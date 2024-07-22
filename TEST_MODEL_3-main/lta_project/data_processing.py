import pandas as pd

def load_and_process_data():
    lta_data = pd.read_csv('C:/Users/darshika/Downloads/TEST_MODEL_3-main/TEST_MODEL_3-main/lta_project/data/lta_data.csv')
    space_data = pd.read_csv('C:/Users/darshika/Downloads/TEST_MODEL_3-main/TEST_MODEL_3-main/lta_project/data/space.csv')
    ramp_data = pd.read_csv('C:/Users/darshika/Downloads/TEST_MODEL_3-main/TEST_MODEL_3-main/lta_project/data/ramp.csv')
    
    return {
        'lta_data': lta_data,
        'space_data': space_data,
        'ramp_data': ramp_data
    }
