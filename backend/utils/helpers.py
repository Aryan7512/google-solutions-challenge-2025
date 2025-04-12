import os
from werkzeug.utils import secure_filename
from flask import current_app
import requests
from backend.utils.config import Config
from backend.utils.translations import get_text

def allowed_file(filename):
    """Check if the file has an allowed extension"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

def save_uploaded_file(file):
    """Save an uploaded file and return the path"""
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # Create upload folder if it doesn't exist
        os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
        
        filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
        file.save(filepath)
        return filepath
    return None

def preprocess_image(image_path, target_size=(224, 224)):
    """
    A simplified version that just verifies the image exists
    and returns a placeholder for the demo - no OpenCV or NumPy required
    """
    if not os.path.exists(image_path):
        return None
    
    # Just return a dummy value (True) for demo purposes
    # No actual image processing needed for the MVP demo
    return True

def get_weather_data(lat, lon):
    """Get weather data for a location"""
    params = {
        'lat': lat,
        'lon': lon,
        'appid': Config.WEATHER_API_KEY,
        'units': 'metric'
    }
    
    try:
        response = requests.get(Config.WEATHER_API_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

def generate_weather_recommendations(weather_data, language='en'):
    """
    Generate farming recommendations based on weather data
    
    Args:
        weather_data (dict): Weather data from OpenWeatherMap API
        language (str): Language code for translations (en or hi)
        
    Returns:
        list: List of recommendations in the selected language
    """
    if not weather_data:
        return ["Unable to generate recommendations without weather data."]
    
    temp = weather_data.get('main', {}).get('temp')
    humidity = weather_data.get('main', {}).get('humidity')
    wind_speed = weather_data.get('wind', {}).get('speed')
    weather_desc = weather_data.get('weather', [{}])[0].get('main')
    
    # Define recommendations in English - will be translated
    recommendations_en = []
    
    # Temperature-based recommendations
    if temp is not None:
        if temp > 35:
            recommendations_en.append("High temperature alert: Ensure adequate water for crops.")
        elif temp < 10:
            recommendations_en.append("Low temperature alert: Protect sensitive crops from frost.")
    
    # Humidity-based recommendations
    if humidity is not None:
        if humidity > 80:
            recommendations_en.append("High humidity: Be aware of potential fungal diseases.")
        elif humidity < 30:
            recommendations_en.append("Low humidity: Increase watering frequency.")
    
    # Weather description-based recommendations
    if weather_desc:
        if weather_desc.lower() in ['rain', 'thunderstorm', 'drizzle']:
            recommendations_en.append("Rainfall expected: Hold off on pesticide application.")
        elif weather_desc.lower() == 'clear':
            recommendations_en.append("Clear weather: Good time for harvesting or planting.")
    
    if not recommendations_en:
        recommendations_en.append("No specific recommendations at this time.")
    
    # Weather recommendation translations
    weather_translations = {
        "High temperature alert: Ensure adequate water for crops.": {
            "en": "High temperature alert: Ensure adequate water for crops.",
            "hi": "उच्च तापमान चेतावनी: फसलों के लिए पर्याप्त पानी सुनिश्चित करें।"
        },
        "Low temperature alert: Protect sensitive crops from frost.": {
            "en": "Low temperature alert: Protect sensitive crops from frost.",
            "hi": "निम्न तापमान चेतावनी: संवेदनशील फसलों को पाले से बचाएं।"
        },
        "High humidity: Be aware of potential fungal diseases.": {
            "en": "High humidity: Be aware of potential fungal diseases.",
            "hi": "उच्च आर्द्रता: संभावित कवक रोगों से सावधान रहें।"
        },
        "Low humidity: Increase watering frequency.": {
            "en": "Low humidity: Increase watering frequency.",
            "hi": "कम आर्द्रता: पानी देने की आवृत्ति बढ़ाएं।"
        },
        "Rainfall expected: Hold off on pesticide application.": {
            "en": "Rainfall expected: Hold off on pesticide application.",
            "hi": "वर्षा की उम्मीद है: कीटनाशक के छिड़काव को रोक दें।"
        },
        "Clear weather: Good time for harvesting or planting.": {
            "en": "Clear weather: Good time for harvesting or planting.",
            "hi": "साफ मौसम: फसल काटने या बोने का अच्छा समय।"
        },
        "No specific recommendations at this time.": {
            "en": "No specific recommendations at this time.",
            "hi": "इस समय कोई विशिष्ट सिफारिशें नहीं हैं।"
        },
        "Unable to generate recommendations without weather data.": {
            "en": "Unable to generate recommendations without weather data.",
            "hi": "मौसम डेटा के बिना सिफारिशें उत्पन्न करने में असमर्थ।"
        }
    }
    
    # Translate recommendations to the requested language
    recommendations = []
    for rec in recommendations_en:
        if rec in weather_translations and language in weather_translations[rec]:
            recommendations.append(weather_translations[rec][language])
        else:
            recommendations.append(rec)  # Fallback to English if no translation
    
    return recommendations 