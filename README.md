
# 📱Mobile Price Prediction System

## Overview
The Mobile Price Prediction System is a project aimed at developing a predictive tool that utilizes advanced regression analysis techniques to accurately forecast market prices of mobile phones based on feaures of mobile device received from user.

## Installation Instructions
To run the application, execute the following command:
```bash
python app.py
```
OR 
  
[click_here](https://mobile-price-prediction-ywpk.onrender.com) to see deployed web application (deployed on Render).

## Project Timeline
![napkin-selection (4)](https://github.com/user-attachments/assets/8deaa2f4-e450-47e7-8333-c8fd1f09c8f8)

- **Data Extraction** - Utilizing Selenium and Beautiful Soup for scraping data.
```python
# code snapshot
names = []
for i in soup.find_all('div',{'class':'sm-product has-tag has-features has-actions'}):
    try:
        names.append(i.find('h2').text)
    except:
        names.append(np.nan)
```
___________________________________________________________________________________________________________
- **Data Cleaning** - Using Pandas for cleaning and preprocessing the data.
```python
# code snapshot
def make_int(string):
    '''
    Function to transform 'price' column.
    This function will extract the numerical value and make it int
    '''
    number_str = string[1:]
    try:
        list_ = number_str.split(',')
        number_str = ''.join(list_)
        return int(number_str)
    except:
        return int(number_str)
```
___________________________________________________________________________________________________________
- **Data Analysis and EDA** - Employing Pandas and Seaborn for exploratory data analysis.
  
  ![c190d87b-fbb0-49c2-9960-37085f606254](https://github.com/user-attachments/assets/e7af1a69-e55e-4cd8-83e1-8b78b44bdcd0)
___________________________________________________________________________________________________________

- **Model Building**: Implementing machine learning models using Scikit-learn.
```python
import xgboost as xgb
xgb_model = xgb.XGBRegressor(objective='reg:squarederror', colsample_bytree=0.3, learning_rate=0.1,
                             max_depth=5, alpha=10, n_estimators=100)

xgb_model.fit(X_train_trans, y_train)
```
__________________________________________________________________________________________________________
- **App Development**: Building the web application using Flask, HTML, and CSS.
```python
app = Flask(__name__)  

# Load the pre-trained model  
model = joblib.load('xgb_regressor_pipeline.joblib')  

# Home route to display the form  
@app.route('/')  
def home():  
    return render_template('index.html')
```
__________________________________________________________________________________________________________
- **Deployment**: Deploying the application on Render.
  
![Screenshot 2024-10-03 164250](https://github.com/user-attachments/assets/8f017bf3-8eab-4648-a111-fdfe80c1587d)
__________________________________________________________________________________________________________
## Technologies Used
- Selenium
- Beautiful Soup
- Pandas
- Seaborn
- Scikit-learn
- Flask
- HTML/CSS

## Contact:
For any questions or feedback, feel free to contact me at akashambure123@gmail.com

Happy Coding! 🚀
