# FarmLink AI

FarmLink AI is an AI-powered farming assistant designed to provide smart solutions to farmers. The platform offers crop recommendations, disease prediction, and fertilizer suggestions based on various environmental and soil parameters. It leverages machine learning models and AI-powered chatbots to assist users in making informed decisions about farming practices.

## Features
- **Crop Recommendation**: Suggests the best crops based on soil parameters, weather conditions, and other environmental factors.
- **Plant Disease Prediction**: Detects and classifies plant diseases from uploaded plant images using machine learning models.
- **Fertilizer Recommendations**: Suggests the most suitable fertilizers for crops based on soil nutrient levels.
- **Chatbot**: An interactive chatbot powered by AI that answers farming-related queries in both English and Hindi, and includes voice-based inputs.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)

## Installation

To run the project locally, follow these steps:

### Prerequisites:
- Python 3.x
- pip (Python package installer)

### Step-by-step guide:

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/farmlink-ai.git
    cd farmlink-ai
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - **On Windows:**

        ```bash
        venv\Scripts\activate
        ```

    - **On macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

4. Install dependencies from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

5. Set up your environment variables (such as API keys for any external services if used).

6. Run the Flask application:

    ```bash
    python app.py
    ```

7. Open a browser and go to `http://localhost:5000` to access the app.

## Usage

Once the server is running, you can access different sections of the application:

- **Home**: Provides an overview and quick access to all features.
- **Crop Recommendation**: Enter soil parameters (e.g., Nitrogen, Phosphorus, Potassium levels) to get crop recommendations.
- **Plant Disease Prediction**: Upload an image of a plant to predict potential diseases.
- **Chatbot**: Interact with the AI-powered chatbot to get answers to farming-related queries (supports both text and voice inputs).

## Features

- **Crop Recommendation**: Uses AI models to recommend the best crops based on input soil and environmental parameters.
- **Plant Disease Prediction**: Detects and classifies diseases from plant images using machine learning techniques.
- **Fertilizer Suggestions**: Recommends suitable fertilizers for crops based on soil nutrient levels.
- **AI-powered Chatbot**: Interact with the chatbot to get instant farming advice and recommendations in both English and Hindi.
- **Voice Support**: The chatbot includes voice recognition capabilities for a more interactive experience.

## Technologies Used

- **Backend**: Flask
- **Machine Learning**: scikit-learn, TensorFlow
- **Web Scraping (if needed)**: BeautifulSoup, requests
- **Image Processing**: OpenCV, Pillow
- **Voice Recognition**: SpeechRecognition, pyttsx3, pyaudio
- **Database**: SQLite (or you can use any relational database)

## Contributing

Contributions are welcome! If you want to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch for your changes
3. Make the necessary changes
4. Submit a pull request

---
farmlink-ai/
│
├── app.py                      # Main Flask application
├── requirements.txt            # List of dependencies
├── README.md                   # Project overview and setup instructions
├── .gitignore                  # Git ignore file for unnecessary files/folders
│
├── static/                     # Static files (images, CSS, JS)
│   ├── images/                 # Folder for image assets
│   ├── css/                    # Stylesheets
│   └── js/                     # JavaScript files
│
├── templates/                  # HTML files
│   ├── base.html               # Base layout file with header/footer
│   ├── index.html              # Home page template
│   ├── crop-recommendation.html # Crop recommendation page template
│   ├── chatbot.html            # Chatbot page template
│   └── plant-disease.html      # Plant disease prediction page template
│
├── models/                     # Machine learning models and related files
│   ├── disease_model.pkl       # Pre-trained plant disease model
│   ├── crop_model.pkl          # Pre-trained crop recommendation model
│   └── fertilizer_model.pkl    # Pre-trained fertilizer recommendation model
│
├── utils/                      # Utility files and helper functions
│   ├── disease_predictor.py    # Functions for disease prediction
│   ├── crop_recommender.py     # Functions for crop recommendation
│   ├── chatbot.py              # Functions for chatbot integration
│   └── voice_recognition.py    # Functions for voice input processing
│
└── venv/                       # Virtual environment (if applicable)


Feel free to reach out to us if you have any questions or suggestions!
