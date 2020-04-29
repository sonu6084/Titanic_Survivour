import numpy as np 
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as  pd
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

def process_input(inputs):
  if inputs[5].lower() == 'male':
    inputs[5]=1
  else:
    inputs[5]=0

  if inputs[6].lower == 'c':
    inputs[6]=0
    inputs.append(0)
  elif inputs[6].lower == 'q':
    inputs[6]=1
    inputs.append(0)
  else:
    inputs[6]=0
    inputs.append(1)  

  output = inputs
  for i in range(len(output)):
  	output[i] = int(output[i])
  output = np.array(output).reshape(1,-1)
  return output

@app.route('/predict',methods=['POST'])
def predict():

	inputs = [x for x in request.form.values()]
	
	output = process_input(inputs)
	
	model = pickle.load(open('titanic.pkl','rb'))
	print(output)
	
	pred = model.predict(output)

	if pred[0]==1:
		text = 'Survived'
	else:
		text = 'RIP'

	return render_template('predict.html',prediction_text= text)

# @app.route('/predict_api',methods=['POST'])
# def predict_api():
# 	'''
# 	For direct API calls through request
# 	'''
# 	

if __name__ == "__main__":
	app.run(debug=True)