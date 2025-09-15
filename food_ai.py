"""
Food AI Module
Handles food recognition and analysis
"""

import random

class FoodAI:
    def __init__(self):
        self.food_db = self.load_food_database()
    
    def load_food_database(self):
        """Load food nutritional database"""
        return {
            'rice': {'name': 'Rice', 'protein': 2.7, 'calories': 130, 'carbs': 28, 'fat': 0.3, 
                    'tips': 'Good energy source. Pair with protein for balanced meal.'},
            'dhal': {'name': 'Dhal (Lentils)', 'protein': 9, 'calories': 116, 'carbs': 20, 'fat': 0.4,
                    'tips': 'Excellent plant-based protein. Rich in fiber and nutrients.'},
            'chicken': {'name': 'Chicken', 'protein': 27, 'calories': 165, 'carbs': 0, 'fat': 3.6,
                       'tips': 'Lean protein source. Remove skin to reduce fat content.'},
            'fish': {'name': 'Fish', 'protein': 22, 'calories': 120, 'carbs': 0, 'fat': 5,
                    'tips': 'Rich in omega-3 fatty acids. Great for heart health.'},
            'egg': {'name': 'Egg', 'protein': 6, 'calories': 78, 'carbs': 0.6, 'fat': 5,
                   'tips': 'Complete protein source. Contains essential amino acids.'},
            'vegetables': {'name': 'Mixed Vegetables', 'protein': 2, 'calories': 50, 'carbs': 10, 'fat': 0,
                          'tips': 'Low in calories, high in fiber and nutrients.'},
            'bread': {'name': 'Bread', 'protein': 4, 'calories': 79, 'carbs': 13, 'fat': 1,
                     'tips': 'Choose whole grain for more fiber and nutrients.'},
            'fruit': {'name': 'Fruit', 'protein': 1, 'calories': 60, 'carbs': 15, 'fat': 0,
                     'tips': 'Natural sugars with vitamins and fiber.'},
        }
    
    def recognize_food(self, image_path=None):
        """
        Recognize food from image
        In a real implementation, this would use TensorFlow Lite
        For now, we'll return a random food item for demonstration
        """
        food_keys = list(self.food_db.keys())
        selected_food = random.choice(food_keys)
        return self.food_db[selected_food]
    
    def get_food_info(self, food_name):
        """Get nutritional information for a specific food"""
        for key, value in self.food_db.items():
            if value['name'].lower() == food_name.lower():
                return value
        return None
    
    def search_foods(self, query):
        """Search for foods by name"""
        results = []
        query = query.lower()
        for key, value in self.food_db.items():
            if query in value['name'].lower():
                results.append(value)
        return results

# For future TensorFlow Lite integration
class TF LiteFoodRecognizer:
    """TensorFlow Lite implementation for food recognition"""
    
    def __init__(self, model_path):
        # This would initialize the TensorFlow Lite interpreter
        # self.interpreter = tflite.Interpreter(model_path=model_path)
        # self.interpreter.allocate_tensors()
        pass
    
    def recognize_food(self, image_path):
        # This would use the TensorFlow Lite model for food recognition
        # For now, return a placeholder
        return {"name": "Food Recognition", "message": "TensorFlow Lite model would be used here"}
