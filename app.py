from flask import Flask, render_template, request
import pickle
import numpy as np
from PIL import Image
import random
import openai
import os
import requests



app = Flask(__name__)

# Load models
def load_models():
    try:
        nb_model = pickle.load(open('C:\\Users\\hp\\Downloads\\New_fou\\Crop-and-Fertilizer-Recommandation-System-using-FLASK\\naive_bayes_model.pkl', 'rb'))
        rf_model = pickle.load(open('C:\\Users\\hp\\Downloads\\New_fou\\Crop-and-Fertilizer-Recommandation-System-using-FLASK\\random_forest_model.pkl', 'rb'))
    except Exception as e:
        print(f"Error loading models: {e}")
        raise
    return nb_model, rf_model

# Mapping from number to crop name
crop_dict = { 
    1: 'rice',
    2: 'maize',
    3: 'jute',
    4: 'cotton',
    5: 'coconut',
    6: 'papaya',
    7: 'orange',
    8: 'apple',
    9: 'muskmelon',
    10: 'watermelon',
    11: 'grapes',
    12: 'mango',
    13: 'banana',
    14: 'pomegranate',
    15: 'lentil',
    16: 'blackgram',
    17: 'mungbean',
    18: 'mothbeans',
    19: 'pigeonpeas',
    20: 'kidneybeans',
    21: 'chickpea',
    22: 'coffee'
}

nb_model, rf_model = load_models()

@app.route('/', methods=['GET', 'POST'])
def index():
    crop_prediction = None
    fertilizer_prediction = None
    error = None
    if request.method == 'POST':
        try:
            # Extracting input data from the form
            N = float(request.form['N'])
            P = float(request.form['P'])
            K = float(request.form['K'])
            temperature = float(request.form['temperature'])
            humidity = float(request.form['humidity'])
            ph = float(request.form['ph'])
            rainfall = float(request.form['rainfall'])

            # Preprocess the data and predict
            crop_features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            crop_prediction_num = nb_model.predict(crop_features)[0]
            crop_name = crop_dict.get(crop_prediction_num, "Unknown Crop")  # Convert number to name

            fertilizer_features = np.array([[N, P, K]])
            fertilizer_prediction = rf_model.predict(fertilizer_features)[0]

            # Fertilizer prediction mapping
            fertilizer_dict = {
                0: 'Urea',
                1: 'DAP',
                2: 'Fourteen-Thirty Five-Fourteen',
                3: 'Twenty Eight-Twenty Eight',
                4: 'Seventeen-Seventeen-Seventeen',
                5: 'Twenty-Twenty',
                6: 'Ten-Twenty Six-Twenty Six'
            }
            fertilizer_name = fertilizer_dict.get(fertilizer_prediction, "Unknown Fertilizer")
            return render_template('crop_recommendation.html', crop_prediction=crop_name, fertilizer_prediction=fertilizer_name)
        
        except Exception as e:
            error = str(e)

    return render_template('index.html', crop_prediction=crop_prediction, fertilizer_prediction=fertilizer_prediction, error=error)

@app.route('/crop-recommendation', methods=['GET', 'POST'])
def crop_recommendation():
    crop_prediction = None
    fertilizer_prediction = None
    error = None
    if request.method == 'POST':
        try:
            # Extracting input data from the form
            N = float(request.form['N'])
            P = float(request.form['P'])
            K = float(request.form['K'])
            temperature = float(request.form['temperature'])
            humidity = float(request.form['humidity'])
            ph = float(request.form['ph'])
            rainfall = float(request.form['rainfall'])

            # Preprocess the data and predict
            crop_features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            crop_prediction_num = nb_model.predict(crop_features)[0]
            crop_name = crop_dict.get(crop_prediction_num, "Unknown Crop")  # Convert number to name

            fertilizer_features = np.array([[N, P, K]])
            fertilizer_prediction = rf_model.predict(fertilizer_features)[0]

            # Fertilizer prediction mapping
            fertilizer_dict = {
                0: 'Urea',
                1: 'DAP',
                2: 'Fourteen-Thirty Five-Fourteen',
                3: 'Twenty Eight-Twenty Eight',
                4: 'Seventeen-Seventeen-Seventeen',
                5: 'Twenty-Twenty',
                6: 'Ten-Twenty Six-Twenty Six'
            }
            fertilizer_name = fertilizer_dict.get(fertilizer_prediction, "Unknown Fertilizer")
            return render_template('crop_recommendation.html', crop_prediction=crop_name, fertilizer_prediction=fertilizer_name)
        
        except Exception as e:
            error = str(e)
    return render_template('crop_recommendation.html', error=error)

# List of possible plant diseases
disease_list = [
    "Leaf Spot Disease",
    "Powdery Mildew",
    "Blight Disease",
    "Rust Disease",
    "Fungal Wilt",
    "Downy Mildew",
    "Anthracnose Disease",
    "Bacterial Spot",
    "Canker Disease",
    "Root Rot Disease"
]

# Simulate disease prediction (this should be replaced by actual model prediction logic)
def predict_disease():
    # Randomly select a disease from the disease list
    return random.choice(disease_list)

@app.route('/plant-disease', methods=['GET', 'POST'])
def plant_disease():
    disease_prediction = None
    error = None
    if request.method == 'POST':
        try:
            # Handle image upload
            plant_image = request.files['plant_image']
            if plant_image:
                # Simulate a disease prediction (replace this with your actual model logic)
                disease_prediction = predict_disease()
                return render_template('disease_prediction.html', disease_prediction=disease_prediction)
            else:
                error = "No image uploaded"
        except Exception as e:
            error = str(e)

    return render_template('disease_prediction.html', error=error)

disease_responses = {
    "Leaf Spot Disease": {
        "en": "Leaf spot disease appears as dark spots on the leaves. To control it, remove the affected leaves and keep the area clean.",
        "hi": "पत्तियों पर धब्बे दिखाई देते हैं। इसे नियंत्रित करने के लिए, प्रभावित पत्तियों को काटकर बाहर फेंक दें और फसल के आसपास की सफाई बनाए रखें।"
    },
    "Powdery Mildew": {
        "en": "Powdery mildew appears as white powder on leaves. Prune the affected leaves and use fungicides to control it.",
        "hi": "इसमें सफेद धुंध जैसा पदार्थ पत्तियों पर जमा हो जाता है। इसे नियंत्रित करने के लिए, प्रभावित पत्तियों को हटा दें और छिड़काव के लिए कवकनाशी का उपयोग करें।"
    },
    "Blight Disease": {
        "en": "Blight disease causes wilting, dark lesions, and rapid decay. It can be controlled by removing infected parts and applying fungicides.",
        "hi": "ब्लाइट रोग से मुरझाना, गहरे धब्बे और तेज सड़न होती है। इसे नियंत्रित करने के लिए, संक्रमित हिस्सों को हटा दें और कवकनाशी का प्रयोग करें।"
    },
    "Rust Disease": {
        "en": "Rust disease is characterized by red or orange pustules on leaves. Prune affected areas and use fungicides for control.",
        "hi": "रस्ट रोग पत्तियों पर लाल या नारंगी रंग के फफोले उत्पन्न करता है। प्रभावित क्षेत्रों को काटकर हटा दें और कवकनाशी का प्रयोग करें।"
    },
    "Fungal Wilt": {
        "en": "Fungal wilt causes yellowing and wilting of plants. It can be controlled by improving soil drainage and removing infected plants.",
        "hi": "फंगल वील्ट पौधों की पत्तियों को पीला कर देता है और मुरझा जाता है। इसे मिट्टी की जल निकासी सुधारने और संक्रमित पौधों को हटाने से नियंत्रित किया जा सकता है।"
    },
    "Downy Mildew": {
        "en": "Downy mildew appears as yellowish spots on leaves, followed by a fuzzy white growth. Use fungicides for control.",
        "hi": "डाउन मिल्डू पत्तियों पर पीले धब्बे उत्पन्न करता है, इसके बाद सफेद धुंध जैसा विकास होता है। इसे नियंत्रित करने के लिए, कवकनाशी का उपयोग करें।"
    },
    "Anthracnose Disease": {
        "en": "Anthracnose disease causes lesions and sunken spots on leaves. Prune affected parts and apply fungicides.",
        "hi": "एंथ्रैकनोस रोग पत्तियों पर धब्बे और धंसी हुई जगहें उत्पन्न करता है। प्रभावित हिस्सों को काटकर हटा दें और कवकनाशी का प्रयोग करें।"
    },
    "Bacterial Spot": {
        "en": "Bacterial spot causes small, water-soaked spots on leaves. Prune infected leaves and use antibacterial treatments.",
        "hi": "बैक्टीरियल स्पॉट पत्तियों पर छोटे, पानी में डूबे हुए धब्बे उत्पन्न करता है। संक्रमित पत्तियों को काटकर हटा दें और जीवाणु रोधी उपचार का उपयोग करें।"
    },
    "Canker Disease": {
        "en": "Canker disease causes sunken lesions on stems and branches. Remove infected parts and apply fungicides.",
        "hi": "कैंकर रोग तनों और शाखाओं पर धंसी हुई जगहें उत्पन्न करता है। संक्रमित हिस्सों को हटा दें और कवकनाशी का प्रयोग करें।"
    },
    "Root Rot Disease": {
        "en": "Root rot disease occurs when roots decay due to waterlogged soil. Ensure proper drainage and remove affected plants.",
        "hi": "रूट रोट रोग तब होता है जब जड़ें जलभराव वाली मिट्टी के कारण सड़ जाती हैं। सही जल निकासी सुनिश्चित करें और प्रभावित पौधों को हटा दें।"
    }
}

fertilizer_responses = {
    "Urea": {
        "en": "Urea is a nitrogen-based fertilizer that promotes healthy leaf and stem growth.",
        "hi": "यूरिया एक नाइट्रोजन आधारित उर्वरक है जो पत्तियों और तनों की स्वस्थ वृद्धि को बढ़ावा देता है।"
    },
    "DAP": {
        "en": "DAP (Diammonium Phosphate) is high in phosphorus, promoting root development and flower production.",
        "hi": "DAP (डायअमोनियम फॉस्फेट) में फास्फोरस की अधिकता होती है, जो जड़ विकास और फूलों के उत्पादन को बढ़ावा देता है।"
    },
    "Fourteen-Thirty Five-Fourteen": {
        "en": "This fertilizer contains balanced nitrogen, phosphorus, and potassium for overall plant health.",
        "hi": "यह उर्वरक समग्र पौधों के स्वास्थ्य के लिए संतुलित नाइट्रोजन, फास्फोरस और पोटेशियम प्रदान करता है।"
    },
    "Twenty Eight-Twenty Eight": {
        "en": "A balanced fertilizer that provides equal amounts of nitrogen and phosphorus for enhanced growth.",
        "hi": "एक संतुलित उर्वरक जो नाइट्रोजन और फास्फोरस की समान मात्रा प्रदान करता है, जिससे वृद्धि में सुधार होता है।"
    },
    "Seventeen-Seventeen-Seventeen": {
        "en": "This fertilizer contains equal amounts of nitrogen, phosphorus, and potassium for all-around growth.",
        "hi": "यह उर्वरक नाइट्रोजन, फास्फोरस और पोटेशियम की समान मात्रा प्रदान करता है, जिससे पौधों में सभी प्रकार की वृद्धि होती है।"
    },
    "Twenty-Twenty": {
        "en": "This fertilizer provides an equal ratio of nitrogen and potassium to support plant health.",
        "hi": "यह उर्वरक नाइट्रोजन और पोटेशियम का समान अनुपात प्रदान करता है, जिससे पौधों के स्वास्थ्य में सुधार होता है।"
    },
    "Ten-Twenty Six-Twenty Six": {
        "en": "A fertilizer high in phosphorus and potassium, ideal for flowering plants.",
        "hi": "यह उर्वरक फास्फोरस और पोटेशियम में उच्च है, जो फूलों वाले पौधों के लिए आदर्श है।"
    }
}

greeting_responses = {
    "hello": {
        "en": "Hello! How can I assist you today?",
        "hi": "नमस्ते! मैं आज आपकी कैसे मदद कर सकता हूँ?"
    },
    "hi": {
        "en": "Hi there! How may I help you?",
        "hi": "नमस्ते! मैं आपकी कैसे मदद कर सकता हूँ?"
    },
    "hey": {
        "en": "Hey! How can I help you today?",
        "hi": "हे! मैं आज आपकी कैसे मदद कर सकता हूँ?"
    }
}

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    chatbot_response = None
    error = None
    disease_prediction = None

    if request.method == 'POST':
        try:
            user_query = request.form['user_query'].lower()

            # Check if the user query matches a disease
            for disease in disease_responses:
                if disease.lower() in user_query:
                    disease_prediction = disease_responses[disease]
                    break
            # Check if the user query matches a fertilizer
            if any(fertilizer.lower() in user_query for fertilizer in fertilizer_responses):
                for fertilizer in fertilizer_responses:
                    if fertilizer.lower() in user_query:
                        disease_prediction = fertilizer_responses[fertilizer]
                        break
            else:
                disease_prediction = {"en": "Sorry, I could not recognize your query.", "hi": "मुझे आपका सवाल पहचानने में समस्या हो रही है।"}

            return render_template('chatbot.html', disease_prediction=disease_prediction, instructions="You can ask about plant diseases and fertilizers in both Hindi and English.")

        except Exception as e:
            error = str(e)

    return render_template('chatbot.html', error=error, instructions="You can ask about plant diseases and fertilizers in both Hindi and English.")

if __name__ == '__main__':
    app.run(debug=True)
