import os
import json
import random
from pathlib import Path

# Simplified soil types without TensorFlow dependency
soil_types = {
    0: "Clay Soil",
    1: "Sandy Soil",
    2: "Loamy Soil",
    3: "Silty Soil"
}

# Sample translations for Hindi
translations = {
    'en': soil_types,
    'hi': {
        0: "चिकनी मिट्टी",
        1: "रेतीली मिट्टी",
        2: "दोमट मिट्टी",
        3: "गादयुक्त मिट्टी"
    }
}

def analyze_soil(image, language='en'):
    """Simulate soil analysis without ML model"""
    # Validate language selection
    if language not in translations:
        language = 'en'  # Default to English
    
    try:
        # Generate a "prediction" (random for demo purposes)
        if image is not None:
            # For demo, we'll simulate a prediction
            soil_type = random.randint(0, 3)  # Random soil type between 0-3
            
            # Simulate soil properties
            properties = {
                "ph": round(random.uniform(5.5, 7.5), 1),
                "nitrogen": round(random.uniform(10, 40), 0),
                "phosphorus": round(random.uniform(5, 20), 0),
                "potassium": round(random.uniform(5, 20), 0),
                "organic_matter": round(random.uniform(1, 5), 1)
            }
            
            result = {
                "soil_type": translations[language][soil_type],
                "properties": properties,
                "recommendations": get_soil_recommendations(soil_type, properties, language)
            }
            
            return result
        else:
            raise Exception("Invalid image data")
    except Exception as e:
        raise Exception(f"Error analyzing soil: {e}")

def get_soil_recommendations(soil_type, properties, language='en'):
    """Get recommendations based on soil type and properties"""
    # Sample recommendations
    recommendations = {
        'en': {
            0: [  # Clay soil
                "Add organic matter to improve drainage.",
                "Avoid overwatering as clay retains moisture well.",
                "Plant crops that thrive in clay soil like cabbage and broccoli."
            ],
            1: [  # Sandy soil
                "Add compost to improve water retention.",
                "Water frequently as sandy soil drains quickly.",
                "Plant root vegetables like carrots and potatoes."
            ],
            2: [  # Loamy soil
                "Maintain organic matter levels with regular compost additions.",
                "Most crops will grow well in this balanced soil type.",
                "Rotate crops to maintain soil health."
            ],
            3: [  # Silty soil
                "Add organic matter to improve structure.",
                "Avoid walking on soil when wet to prevent compaction.",
                "Good for growing most vegetables and fruits."
            ]
        },
        'hi': {
            0: [  # Clay soil
                "जल निकासी में सुधार के लिए जैविक पदार्थ जोड़ें।",
                "अधिक पानी देने से बचें क्योंकि मिट्टी नमी को अच्छी तरह से बनाए रखती है।",
                "पत्तागोभी और ब्रोकोली जैसी फसलें लगाएं जो चिकनी मिट्टी में अच्छी तरह से उगती हैं।"
            ],
            1: [  # Sandy soil
                "पानी के धारण को बेहतर बनाने के लिए कम्पोस्ट जोड़ें।",
                "बार-बार पानी दें क्योंकि रेतीली मिट्टी जल्दी सूख जाती है।",
                "गाजर और आलू जैसी जड़ वाली सब्जियां लगाएं।"
            ],
            2: [  # Loamy soil
                "नियमित कम्पोस्ट जोड़कर जैविक पदार्थ के स्तर को बनाए रखें।",
                "अधिकांश फसलें इस संतुलित मिट्टी के प्रकार में अच्छी तरह से उगेंगी।",
                "मिट्टी के स्वास्थ्य को बनाए रखने के लिए फसलों को घुमाएं।"
            ],
            3: [  # Silty soil
                "संरचना में सुधार के लिए जैविक पदार्थ जोड़ें।",
                "संघनन को रोकने के लिए गीली मिट्टी पर चलने से बचें।",
                "अधिकांश सब्जियों और फलों के लिए अच्छी है।"
            ]
        }
    }
    
    # Additional pH-based recommendations
    ph_recommendations = {
        'en': {
            "low": "Your soil pH is low. Consider adding lime to raise pH.",
            "high": "Your soil pH is high. Consider adding sulfur to lower pH.",
            "optimal": "Your soil pH is in the optimal range for most crops."
        },
        'hi': {
            "low": "आपकी मिट्टी का पीएच कम है। पीएच बढ़ाने के लिए चूना जोड़ने पर विचार करें।",
            "high": "आपकी मिट्टी का पीएच अधिक है। पीएच कम करने के लिए सल्फर जोड़ने पर विचार करें।",
            "optimal": "आपकी मिट्टी का पीएच अधिकांश फसलों के लिए इष्टतम सीमा में है।"
        }
    }
    
    # Validate language selection
    if language not in recommendations:
        language = 'en'  # Default to English
    
    # Get basic recommendations based on soil type
    result = recommendations[language][soil_type].copy()
    
    # Add pH-specific recommendation
    ph = properties['ph']
    if ph < 6.0:
        result.append(ph_recommendations[language]["low"])
    elif ph > 7.2:
        result.append(ph_recommendations[language]["high"])
    else:
        result.append(ph_recommendations[language]["optimal"])
    
    return result 