import os
import json
import random
from pathlib import Path

# Simplified class names without TensorFlow dependency
class_names = {
    0: "Healthy",
    1: "Early Blight",
    2: "Late Blight",
    3: "Bacterial Spot",
    4: "Target Spot"
}

# Sample translations for Hindi
translations = {
    'en': class_names,
    'hi': {
        0: "स्वस्थ",
        1: "अर्ली ब्लाइट",
        2: "लेट ब्लाइट",
        3: "बैक्टीरियल स्पॉट",
        4: "टारगेट स्पॉट"
    }
}

def predict_disease(image, language='en'):
    """Simulate plant disease prediction without ML model"""
    # Validate language selection
    if language not in translations:
        language = 'en'  # Default to English
    
    try:
        # Generate a "prediction" (random for demo purposes)
        if image is not None:
            # For demo, we'll simulate a prediction
            predicted_class = random.randint(0, 4)  # Random class between 0-4
            confidence = random.uniform(0.7, 0.99)  # Random confidence
            
            result = {
                "disease": translations[language][predicted_class],
                "confidence": float(confidence),
                "recommendations": get_treatment_recommendations(predicted_class, language)
            }
            
            return result
        else:
            raise Exception("Invalid image data")
    except Exception as e:
        raise Exception(f"Error predicting disease: {e}")

def get_treatment_recommendations(disease_class, language='en'):
    """Get treatment recommendations for a disease"""
    # Sample recommendations
    recommendations = {
        'en': {
            0: ["Plant is healthy, no treatment needed."],
            1: ["Remove infected leaves.", "Apply copper-based fungicide.", "Ensure proper spacing for air circulation."],
            2: ["Remove infected plants to prevent spread.", "Apply fungicide with chlorothalonil.", "Avoid overhead irrigation."],
            3: ["Apply copper-based bactericide.", "Rotate crops.", "Avoid working with wet plants."],
            4: ["Remove infected leaves.", "Apply fungicide.", "Maintain proper plant spacing."]
        },
        'hi': {
            0: ["पौधा स्वस्थ है, कोई उपचार की आवश्यकता नहीं है।"],
            1: ["संक्रमित पत्तियों को हटा दें।", "कॉपर-आधारित फफूंदनाशक लगाएं।", "हवा के संचार के लिए उचित स्पेसिंग सुनिश्चित करें।"],
            2: ["प्रसार को रोकने के लिए संक्रमित पौधों को हटा दें।", "क्लोरोथालोनिल वाले फफूंदनाशक लगाएं।", "ऊपरी सिंचाई से बचें।"],
            3: ["कॉपर-आधारित बैक्टीरियासाइड लगाएं।", "फसलों का रोटेशन करें।", "गीले पौधों के साथ काम करने से बचें।"],
            4: ["संक्रमित पत्तियों को हटा दें।", "फफूंदनाशक लगाएं।", "उचित पौधों की स्पेसिंग बनाए रखें।"]
        }
    }
    
    # Validate language selection
    if language not in recommendations:
        language = 'en'  # Default to English
    
    return recommendations[language][disease_class] 