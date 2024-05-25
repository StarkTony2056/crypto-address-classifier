import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS
import re
from collections import Counter
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Initialize the Flask application
app = Flask(__name__)
CORS(app)

# Load the trained model
model = joblib.load('random_forest_model.pkl')

def get_character_frequency(address):
  '''
  Returns the character frequency of the input address.
  '''
  frequency = Counter(address)
  char_freq_vector = np.zeros(256)
  for char, freq in frequency.items():
    char_freq_vector[ord(char)] = freq

  char_freq_vectors = np.array(char_freq_vector.tolist())
  return char_freq_vectors

def get_prefix(address):
  '''
  Returns prefix in a one-hot encoded version (currently working for bitcoin, ethereum, litecoin and dogecoin addresses only).
  '''
  if address[0].isdigit():
    if address[0] == '0':
      length = 2
    else:
      length = 1
  else:
    if address[0] == 'b':
      length = 3
    else:
      length = 1

  prefix = address[:length]
  prefix_0x = 0.
  prefix_1 = 0.
  prefix_3 = 0.
  prefix_9 = 0.
  prefix_a = 0.
  prefix_bc1 = 0.
  prefix_d = 0.
  prefix_l = 0.
  if prefix == '0x':
    prefix_0x = 1.
  elif prefix == '1':
    prefix_1 = 1.
  elif prefix == '3':
    prefix_3 = 1.
  elif prefix == '9':
    prefix_9 = 1.
  elif prefix == 'a':
    prefix_a = 1.
  elif prefix == 'bc1':
    prefix_bc1 = 1.
  elif prefix == 'd':
    prefix_d = 1.
  elif prefix == 'l':
    prefix_l = 1.

  prefix_list = [prefix_0x, prefix_1, prefix_3, prefix_9, prefix_a, prefix_bc1, prefix_d, prefix_l]
  prefix_array = np.array(prefix_list)
  return prefix_array

def extract_features(address):
    """
    Extract features from the cryptocurrency address.
    """
    features = {
        'length': len(address),
        'char_freq': get_character_frequency(address),
        'prefix': get_prefix(address)
    }
    # Example of converting to a flat list of feature values
    flat_features = np.concatenate((features['char_freq'], [features['length']], features['prefix']))
    return flat_features

@app.route('/classify', methods=['POST'])
def classify():
    """
    Classify the cryptocurrency address.
    """
    data = request.get_json()
    
    if 'address' not in data:
        return jsonify({'error': 'No address provided'}), 400

    address = data['address']
    
    # Simple validation (extend as needed)
    if not re.match(r'^[a-zA-Z0-9]+$', address):
        return jsonify({'error': 'Invalid address format'}), 400
    if len(address) < 26 or len(address) > 42:
        return jsonify({'error': 'Invalid address format'}), 400
    address = address.lower()

    # Extract features
    features = extract_features(address)
    
    # Predict the cryptocurrency type
    prediction = model.predict([features])
    
    return jsonify({'cryptocurrency': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
