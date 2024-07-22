from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load the data
lta_data = pd.read_csv('C:/Users/darshika/Downloads/TEST_MODEL_3-main/TEST_MODEL_3-main/lta_project/data/lta_data.csv')
space_data = pd.read_csv('C:/Users/darshika/Downloads/TEST_MODEL_3-main/TEST_MODEL_3-main/lta_project/data/space.csv')
ramp_data = pd.read_csv('C:/Users/darshika/Downloads/TEST_MODEL_3-main/TEST_MODEL_3-main/lta_project/data/ramp.csv')

@app.route('/')
def index():
    return render_template('index.html', lta_data=lta_data.to_dict('records'))

@app.route('/space')
def space():
    return render_template('space.html', space_data=space_data.to_dict('records'))

@app.route('/ramp')
def ramp():
    return render_template('ramp.html', ramp_data=ramp_data.to_dict('records'))


if __name__ == '__main__':
    app.run(debug=True)