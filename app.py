from flask import Flask, render_template, request  
import pandas as pd
import joblib  
import numpy as np  
import sklearn
import xgboost

# printing libraries versions with names

print("Pandas version: ", pd.__version__)
print("Numpy version: ", np.__version__)
print("Joblib version: ", joblib.__version__)
print("Sklearn version: ", sklearn.__version__)
print("XGBoost version: ", xgboost.__version__)

app = Flask(__name__)  

# Load the pre-trained model  
model = joblib.load('xgb_regressor_pipeline.joblib')  

# Home route to display the form  
@app.route('/')  
def home():  
    return render_template('index.html')  

# Route to handle form submission and make predictions  
@app.route('/predict', methods=['POST'])  
def predict():  
    if request.method == 'POST':  
        # Retrieve input data from the form  
        company = request.form['company']  
        sim_count = int(request.form['sim_count'])  
        network = request.form['network']  
        processor_name = request.form['processor_name']  
        ram = int(request.form['ram'])  
        battery = float(request.form['battery'])  
        display_size = float(request.form['display_size'])  
        dis_pixel_1 = float(request.form['dis_pixel_1'])  
        dis_pixel_2 = float(request.form['dis_pixel_2'])  
        camera = float(request.form['camera'])  
        os = request.form['os']  

        # Prepare the feature array  
        array = np.array([company, sim_count, network, processor_name, ram,  
                              battery, display_size, dis_pixel_1, dis_pixel_2, camera, os])  
        # Convert the input array to a DataFrame
        input_df = pd.DataFrame([array], columns=['company', 'sim_count', 'network', 'processor_name', 'ram', 'battery', 
                                                  'display_size', 'dis_pixel_1', 'dis_pixel_2', 'camera', 'os'])
        
        # Ensure data types match the expected types
        input_df['sim_count'] = input_df['sim_count'].astype('int32')
        input_df['ram'] = input_df['ram'].astype('int32')
        input_df['battery'] = input_df['battery'].astype('float32')
        input_df['dis_pixel_1'] = input_df['dis_pixel_1'].astype('float32')
        input_df['dis_pixel_2'] = input_df['dis_pixel_2'].astype('float32')
        input_df['camera'] = input_df['camera'].astype('float32')

        # Make prediction  
        prediction = model.predict(input_df)  
        prediction = np.exp(prediction)

        # Render the result template with the prediction  
        return render_template('result.html', prediction=round(prediction[0], 2))  
    else:  
        return render_template('index.html')  

if __name__ == '__main__':  
    app.run(debug=True) 

