"""
Meal Generator Module
Handles all meal planning and nutrition logic
"""

class MealGenerator:
    def __init__(self):
        self.proteins = []
        self.veggies = []
        self.carbs = []
        self.tips = []
        self.total_protein = 0
        self.protein_goal = 50
        self.load_data()
    
    def load_data(self):
        """Load Sri Lankan food database"""
        self.proteins = [
            {"name": "Eggs (2 large)", "protein": 12, "cost": "Low", "type": "Animal"},
            {"name": "Canned Sardines (100g)", "protein": 20, "cost": "Medium", "type": "Animal"},
            {"name": "Canned Mackerel (100g)", "protein": 19, "cost": "Medium", "type": "Animal"},
            {"name": "Chicken Liver (100g)", "protein": 24, "cost": "Medium", "type": "Animal"},
            {"name": "Dhal (1 cup cooked)", "protein": 18, "cost": "Very Low", "type": "Plant"},
            {"name": "Chickpeas (1 cup cooked)", "protein": 15, "cost": "Low", "type": "Plant"},
            {"name": "Cottage Cheese (100g)", "protein": 11, "cost": "Medium", "type": "Dairy"},
            {"name": "Plain Curd (1 cup)", "protein": 8, "cost": "Low", "type": "Dairy"},
            {"name": "Dried Fish (50g)", "protein": 25, "cost": "Medium", "type": "Animal"},
            {"name": "Mackerel (100g)", "protein": 19, "cost": "Medium", "type": "Animal"},
        ]

        self.veggies = [
            "Kankun (Water Spinach) Mallung",
            "Mukunuwenna (Alternanthera) Mallung",
            "Gotukola (Centella) Sambol",
            "Cabbage Salad",
            "Spinach (Nivithi) Curry",
            "Bean Curry",
            "Brinjal (Eggplant) Moju",
            "Cucumber Salad",
            "Carrot Salad",
            "Kohila (Lasia Spinosa) Curry"
        ]

        self.carbs = [
            "Red Rice (1 scoop)",
            "White Rice (1 scoop)",
            "Roti (1 piece)",
            "Jak Fruit (1 cup)",
            "Oats (1 cup)",
            "Whole Grain Bread (2 slices)",
            "Sweet Potato (1 medium)",
            "String Hoppers (5 pieces)",
            "Hoppers (2 pieces)",
            "Kurakkan Roti (1 piece)"
        ]

        self.tips = [
            "Spread your protein intake evenly across all meals",
            "Combine rice and dhal to form a complete protein",
            "Fill half your plate with vegetables to feel full",
            "Use minimal oil when cooking - try steaming or baking",
            "Drink plenty of water before meals to reduce appetite",
            "Focus on weight training 3x/week to preserve muscle",
            "Be patient - aim for 0.5kg loss per week (not more)",
            "Get 7-8 hours of sleep for better recovery and hormones",
            "Limit sugary drinks and snacks - they add empty calories",
            "Walk for 30 minutes daily to boost metabolism",
        ]
    
    def generate_meal_plan(self):
        """Generate a complete daily meal plan"""
        meal_plan = {
            "breakfast": self.generate_meal("Breakfast"),
            "lunch": self.generate_meal("Lunch"),
            "dinner": self.generate_meal("Dinner"),
            "total_protein": 0
        }
        
        # Calculate total protein
        meal_plan["total_protein"] = sum(
            meal["protein"]["protein"] for meal in [
                meal_plan["breakfast"],
                meal_plan["lunch"],
                meal_plan["dinner"]
            ]
        )
        
        return meal_plan
    
    def generate_meal(self, meal_type):
        """Generate a single meal"""
        protein = random.choice(self.proteins)
        veggie = random.choice(self.veggies)
        carb = random.choice(self.carbs)
        
        return {
            "type": meal_type,
            "protein": protein,
            "veggie": veggie,
            "carb": carb
        }
    
    def get_random_tips(self, count=3):
        """Get random nutrition tips"""
        return random.sample(self.tips, min(count, len(self.tips)))
    
    def set_protein_goal(self, goal):
        """Set daily protein goal"""
        self.protein_goal = goal
    
    def get_protein_goal(self):
        """Get daily protein goal"""
        return self.protein_goal
