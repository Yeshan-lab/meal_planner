"""
Main Application Module
UI for the Sri Lankan Meal Planner
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from meal_generator import MealGenerator
from food_ai import FoodAI
import random

class MealPlannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sri Lankan Meal Planner")
        self.root.geometry("1000x700")
        self.root.configure(bg='#0f172a')
        
        # Initialize components
        self.meal_generator = MealGenerator()
        self.food_ai = FoodAI()
        
        # Create UI
        self.setup_ui()
        
        # Generate initial meal plan
        self.generate_meal_plan()
    
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(
            main_frame, 
            text="Sri Lankan Meal Planner", 
            font=("Arial", 24, "bold"),
            foreground="white",
            background="#0f172a"
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Protein goal section
        goal_frame = ttk.Frame(main_frame)
        goal_frame.grid(row=1, column=0, columnspan=2, pady=(0, 20), sticky=(tk.W, tk.E))
        
        ttk.Label(
            goal_frame, 
            text="Protein Goal (g):", 
            foreground="white",
            background="#0f172a"
        ).grid(row=0, column=0, padx=(0, 10))
        
        self.protein_goal_var = tk.IntVar(value=self.meal_generator.get_protein_goal())
        goal_entry = ttk.Entry(goal_frame, textvariable=self.protein_goal_var, width=10)
        goal_entry.grid(row=0, column=1, padx=(0, 10))
        
        ttk.Button(
            goal_frame, 
            text="Update Goal", 
            command=self.update_protein_goal
        ).grid(row=0, column=2)
        
        # Protein progress
        self.protein_label = ttk.Label(
            main_frame,
            text=f"Protein: 0/{self.meal_generator.get_protein_goal()}g",
            foreground="white",
            background="#0f172a",
            font=("Arial", 14)
        )
        self.protein_label.grid(row=2, column=0, columnspan=2, pady=(0, 20))
        
        # Tips section
        tips_frame = ttk.LabelFrame(main_frame, text="Nutrition Tips", padding="10")
        tips_frame.grid(row=3, column=0, columnspan=2, pady=(0, 20), sticky=(tk.W, tk.E))
        tips_frame.columnconfigure(0, weight=1)
        
        self.tips_text = scrolledtext.ScrolledText(
            tips_frame, 
            width=60, 
            height=4,
            font=("Arial", 10)
        )
        self.tips_text.grid(row=0, column=0, sticky=(tk.W, tk.E))
        self.tips_text.configure(state="disabled")
        
        # Buttons frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=4, column=0, columnspan=2, pady=(0, 20))
        
        ttk.Button(
            buttons_frame, 
            text="Generate New Plan", 
            command=self.generate_meal_plan
        ).grid(row=0, column=0, padx=5)
        
        ttk.Button(
            buttons_frame, 
            text="Food Scanner", 
            command=self.show_food_scanner
        ).grid(row=0, column=1, padx=5)
        
        ttk.Button(
            buttons_frame, 
            text="Nutrition Info", 
            command=self.show_nutrition_info
        ).grid(row=0, column=2, padx=5)
        
        # Meals frame
        meals_frame = ttk.Frame(main_frame)
        meals_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E))
        meals_frame.columnconfigure(0, weight=1)
        meals_frame.columnconfigure(1, weight=1)
        meals_frame.columnconfigure(2, weight=1)
        
        # Meal cards
        self.meal_frames = []
        meal_types = ["Breakfast", "Lunch", "Dinner"]
        
        for i, meal_type in enumerate(meal_types):
            frame = ttk.LabelFrame(meals_frame, text=meal_type, padding="10")
            frame.grid(row=0, column=i, padx=5, sticky=(tk.W, tk.E, tk.N, tk.S))
            frame.columnconfigure(0, weight=1)
            
            # Create labels for meal details
            protein_label = ttk.Label(frame, text="", wraplength=200)
            protein_label.grid(row=0, column=0, pady=(0, 5), sticky=tk.W)
            
            veggie_label = ttk.Label(frame, text="", wraplength=200)
            veggie_label.grid(row=1, column=0, pady=(0, 5), sticky=tk.W)
            
            carb_label = ttk.Label(frame, text="", wraplength=200)
            carb_label.grid(row=2, column=0, pady=(0, 5), sticky=tk.W)
            
            self.meal_frames.append({
                "frame": frame,
                "protein": protein_label,
                "veggie": veggie_label,
                "carb": carb_label
            })
    
    def generate_meal_plan(self):
        """Generate and display a new meal plan"""
        meal_plan = self.meal_generator.generate_meal_plan()
        
        # Update protein display
        self.protein_label.config(
            text=f"Protein: {meal_plan['total_protein']}/{self.meal_generator.get_protein_goal()}g"
        )
        
        # Update meal cards
        meals = ["breakfast", "lunch", "dinner"]
        for i, meal_key in enumerate(meals):
            meal = meal_plan[meal_key]
            meal_frame = self.meal_frames[i]
            
            meal_frame["protein"].config(
                text=f"Protein: {meal['protein']['name']} ({meal['protein']['protein']}g)"
            )
            meal_frame["veggie"].config(text=f"Veggie: {meal['veggie']}")
            meal_frame["carb"].config(text=f"Carb: {meal['carb']}")
        
        # Update tips
        tips = self.meal_generator.get_random_tips(3)
        self.tips_text.configure(state="normal")
        self.tips_text.delete(1.0, tk.END)
        self.tips_text.insert(tk.END, "\n".join(f"• {tip}" for tip in tips))
        self.tips_text.configure(state="disabled")
    
    def update_protein_goal(self):
        """Update the protein goal"""
        try:
            goal = self.protein_goal_var.get()
            if goal < 20 or goal > 150:
                messagebox.showerror("Error", "Please enter a protein goal between 20 and 150g")
                return
            
            self.meal_generator.set_protein_goal(goal)
            self.generate_meal_plan()
            messagebox.showinfo("Success", f"Protein goal updated to {goal}g")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
    
    def show_food_scanner(self):
        """Show food scanner dialog"""
        scanner_window = tk.Toplevel(self.root)
        scanner_window.title("Food Scanner")
        scanner_window.geometry("400x300")
        
        ttk.Label(
            scanner_window, 
            text="Food Scanner (AI)", 
            font=("Arial", 16, "bold")
        ).pack(pady=10)
        
        ttk.Label(
            scanner_window, 
            text="This feature would use camera to identify food", 
            wraplength=300
        ).pack(pady=5)
        
        ttk.Button(
            scanner_window, 
            text="Scan Food", 
            command=self.simulate_food_scan
        ).pack(pady=10)
        
        self.scan_result = ttk.Label(scanner_window, text="", wraplength=350)
        self.scan_result.pack(pady=10)
    
    def simulate_food_scan(self):
        """Simulate food scanning (for demo purposes)"""
        food_info = self.food_ai.recognize_food()
        self.scan_result.config(
            text=f"Detected: {food_info['name']}\n"
                 f"Protein: {food_info['protein']}g/100g\n"
                 f"Tips: {food_info['tips']}"
        )
    
    def show_nutrition_info(self):
        """Show nutrition information dialog"""
        info_window = tk.Toplevel(self.root)
        info_window.title("Nutrition Information")
        info_window.geometry("500x400")
        
        ttk.Label(
            info_window, 
            text="Sri Lankan Food Nutrition Database", 
            font=("Arial", 16, "bold")
        ).pack(pady=10)
        
        # Create search frame
        search_frame = ttk.Frame(info_window)
        search_frame.pack(pady=10, fill=tk.X, padx=20)
        
        ttk.Label(search_frame, text="Search Food:").grid(row=0, column=0, padx=(0, 10))
        
        search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=search_var, width=20)
        search_entry.grid(row=0, column=1, padx=(0, 10))
        
        search_result = ttk.Label(info_window, text="", wraplength=450)
        search_result.pack(pady=10)
        
        def perform_search():
            query = search_var.get()
            if not query:
                search_result.config(text="Please enter a food name")
                return
            
            results = self.food_ai.search_foods(query)
            if results:
                food = results[0]  # Take first result
                search_result.config(
                    text=f"{food['name']}\n"
                         f"Protein: {food['protein']}g/100g • "
                         f"Calories: {food['calories']} • "
                         f"Carbs: {food['carbs']}g • "
                         f"Fat: {food['fat']}g\n\n"
                         f"Tips: {food['tips']}"
                )
            else:
                search_result.config(text=f"No information found for '{query}'")
        
        ttk.Button(
            search_frame, 
            text="Search", 
            command=perform_search
        ).grid(row=0, column=2)

def main():
    root = tk.Tk()
    app = MealPlannerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
