import streamlit as st
import pandas as pd

# Set page title and icon
st.set_page_config(
    page_title='🍲 Recipe Sharing App 🍳',
    page_icon=':fork_and_knife:',
    layout='wide'
)

# Load custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles.css")

# Load recipes from database
def load_recipes():
    # Sample data for demonstration
    sample_data = {
        "ID": list(range(1, 17)),
        "Recipe Name": [
            "Spaghetti Bolognese", "Chicken Curry", "Beef Stew", "Salmon with Lemon Butter", "Vegetable Stir Fry", "Chocolate Cake", "Apple Pie", "Lemon Tart",
            "Pancakes", "Caesar Salad", "Shrimp Scampi", "Mushroom Risotto", "Tacos", "Banana Bread", "Lasagna", "Pumpkin Soup"
        ],
        "Ingredients": [
            "Spaghetti, Beef, Tomato Sauce, Onion, Garlic, Olive Oil, Salt, Pepper",
            "Chicken, Curry Powder, Coconut Milk, Onion, Garlic, Ginger, Tomatoes, Salt",
            "Beef, Potatoes, Carrots, Onion, Beef Broth, Flour, Salt, Pepper",
            "Salmon, Lemon, Butter, Garlic, Parsley, Salt, Pepper",
            "Mixed Vegetables, Tofu, Soy Sauce, Garlic, Ginger, Olive Oil, Salt",
            "Flour, Cocoa Powder, Sugar, Eggs, Butter, Baking Powder, Milk, Vanilla Extract",
            "Apples, Flour, Sugar, Butter, Cinnamon, Nutmeg, Lemon Juice, Pie Crust",
            "Lemon, Sugar, Eggs, Butter, Flour, Salt, Vanilla Extract",
            "Flour, Milk, Eggs, Sugar, Baking Powder, Salt, Butter, Vanilla Extract",
            "Romaine Lettuce, Caesar Dressing, Parmesan Cheese, Croutons, Chicken (optional)",
            "Shrimp, Garlic, Butter, White Wine, Lemon Juice, Parsley, Red Pepper Flakes",
            "Arborio Rice, Mushrooms, Onion, Garlic, White Wine, Vegetable Broth, Parmesan Cheese, Butter",
            "Ground Beef, Taco Seasoning, Tortillas, Lettuce, Tomato, Cheese, Salsa, Sour Cream",
            "Bananas, Flour, Sugar, Eggs, Butter, Baking Soda, Salt, Vanilla Extract",
            "Lasagna Noodles, Ground Beef, Tomato Sauce, Ricotta Cheese, Mozzarella Cheese, Parmesan Cheese, Egg, Basil, Garlic, Onion, Salt, Pepper",
            "Pumpkin, Onion, Garlic, Ginger, Vegetable Broth, Coconut Milk, Salt, Pepper, Nutmeg"
        ],
        "Instructions": [
            "1. Boil spaghetti according to package instructions.\n2. In a pan, heat olive oil and sauté onion and garlic until fragrant.\n3. Add beef and cook until browned.\n4. Stir in tomato sauce, salt, and pepper, and let simmer for 20 minutes.\n5. Serve sauce over spaghetti.",
            "1. In a pot, heat oil and sauté onion, garlic, and ginger until aromatic.\n2. Add chicken and cook until no longer pink.\n3. Stir in curry powder and cook for another minute.\n4. Add tomatoes and coconut milk, and bring to a boil.\n5. Reduce heat and simmer for 30 minutes.\n6. Serve with rice.",
            "1. In a large pot, brown the beef over medium heat.\n2. Add chopped onions and cook until translucent.\n3. Stir in flour and cook for 2 minutes.\n4. Add beef broth, potatoes, and carrots.\n5. Season with salt and pepper.\n6. Bring to a boil, then reduce heat and simmer for 1 hour.\n7. Serve hot.",
            "1. Season salmon with salt and pepper.\n2. In a pan, melt butter over medium heat.\n3. Add garlic and cook until fragrant.\n4. Add salmon and cook for 4-5 minutes on each side.\n5. Squeeze lemon juice over salmon and garnish with parsley.\n6. Serve immediately.",
            "1. Heat oil in a pan over high heat.\n2. Add garlic and ginger, and cook until fragrant.\n3. Add mixed vegetables and tofu, and stir-fry for 5-7 minutes.\n4. Add soy sauce and cook for another 2 minutes.\n5. Serve hot.",
            "1. Preheat oven to 350°F (175°C).\n2. In a bowl, mix flour, cocoa powder, sugar, and baking powder.\n3. Add eggs, melted butter, milk, and vanilla extract, and mix until smooth.\n4. Pour batter into a greased baking pan.\n5. Bake for 30-35 minutes.\n6. Let cool before serving.",
            "1. Preheat oven to 375°F (190°C).\n2. Peel and slice apples, then mix with sugar, cinnamon, nutmeg, and lemon juice.\n3. Place apple mixture into pie crust.\n4. Cover with top crust, seal edges, and cut slits for steam.\n5. Bake for 50-60 minutes.\n6. Let cool before serving.",
            "1. Preheat oven to 350°F (175°C).\n2. In a bowl, mix lemon juice, sugar, eggs, and melted butter until smooth.\n3. Pour mixture into pre-baked tart crust.\n4. Bake for 20-25 minutes.\n5. Let cool and refrigerate before serving.",
            "1. In a bowl, mix flour, sugar, baking powder, and salt.\n2. In another bowl, whisk together milk, eggs, and vanilla extract.\n3. Combine wet and dry ingredients and stir until smooth.\n4. Heat butter in a skillet over medium heat.\n5. Pour batter into skillet and cook until bubbles form.\n6. Flip and cook until golden brown.\n7. Serve with syrup.",
            "1. Chop romaine lettuce and place in a large bowl.\n2. Add Caesar dressing and toss to coat.\n3. Sprinkle with Parmesan cheese and croutons.\n4. Add grilled chicken if desired.\n5. Serve immediately.",
            "1. In a pan, melt butter over medium heat.\n2. Add garlic and cook until fragrant.\n3. Add shrimp and cook until pink.\n4. Pour in white wine and lemon juice.\n5. Add red pepper flakes and parsley.\n6. Cook for another 2-3 minutes.\n7. Serve with pasta or bread.",
            "1. In a pot, heat oil and sauté onion and garlic until fragrant.\n2. Add mushrooms and cook until soft.\n3. Stir in arborio rice and cook for 2 minutes.\n4. Add white wine and cook until evaporated.\n5. Gradually add vegetable broth, stirring constantly, until rice is cooked.\n6. Stir in Parmesan cheese and butter.\n7. Serve hot.",
            "1. In a pan, cook ground beef until browned.\n2. Add taco seasoning and water, and simmer for 5 minutes.\n3. Warm tortillas in a skillet.\n4. Assemble tacos with beef, lettuce, tomato, cheese, salsa, and sour cream.\n5. Serve immediately.",
            "1. Preheat oven to 350°F (175°C).\n2. In a bowl, mix flour, sugar, baking soda, and salt.\n3. In another bowl, mash bananas and mix with eggs, melted butter, and vanilla extract.\n4. Combine wet and dry ingredients and stir until smooth.\n5. Pour batter into a greased loaf pan.\n6. Bake for 60-70 minutes.\n7. Let cool before serving.",
            "1. Preheat oven to 375°F (190°C).\n2. Cook lasagna noodles according to package instructions.\n3. In a pan, cook ground beef with chopped onion and garlic.\n4. Add tomato sauce, salt, and pepper, and simmer for 15 minutes.\n5. In a bowl, mix ricotta cheese with egg and basil.\n6. In a baking dish, layer noodles, meat sauce, ricotta mixture, and mozzarella cheese.\n7. Repeat layers and top with Parmesan cheese.\n8. Bake for 45 minutes.\n9. Let cool before serving.",
            "1. In a pot, sauté onion, garlic, and ginger until fragrant.\n2. Add chopped pumpkin and cook for 5 minutes.\n3. Pour in vegetable broth and bring to a boil.\n4. Reduce heat and simmer until pumpkin is soft.\n5. Blend until smooth.\n6. Stir in coconut milk, salt, pepper, and nutmeg.\n7. Serve hot."
        ],
        "Preparation Time": [30, 45, 60, 20, 15, 50, 70, 45, 20, 15, 25, 40, 30, 60, 90, 40],
        "Category": ["Main Course", "Main Course", "Main Course", "Seafood", "Vegetarian", "Dessert", "Dessert", "Dessert",
                     "Breakfast", "Salad", "Seafood", "Main Course", "Main Course", "Dessert", "Main Course", "Soup"],
        "Rating": [4.5, 4.7, 4.6, 4.8, 4.3, 4.9, 4.8, 4.7, 4.5, 4.6, 4.7, 4.8, 4.6, 4.7, 4.8, 4.6],
        "Ratings Count": [150, 200, 180, 120, 100, 250, 230, 220, 160, 140, 130, 150, 170, 180, 190, 160]
    }
    return pd.DataFrame(sample_data)

# Save new recipe to database
def save_recipe(recipe_data):
    # Placeholder for saving new recipe to the database
    pass

# User Authentication
def authenticate_user(username, password):
    # Placeholder for user authentication
    # Hardcoded credentials for demonstration purposes
    return username == "admin" and password == "password"

# User Registration
def register_user(username, password):
    # Placeholder for user registration
    # Here, you might save the new user to a database
    return True  # For demonstration purposes, always return True for successful registration

def main():
    st.title('🍲 Recipe Sharing App 🍳')
    st.info('Share your favorite recipes with the world!')

    # Fascinating paragraph
    st.markdown("""
    🌟 Welcome to the culinary universe of flavor and creativity! Dive into a world where every dish tells a story, and every recipe is a masterpiece waiting to be discovered. Whether you're a seasoned chef or a novice in the kitchen, our recipe sharing app is your gateway to a tantalizing journey of gastronomic delight. From sizzling main courses to decadent desserts, each recipe is a symphony of taste, texture, and aroma. Join our community of passionate food lovers, and let's embark on a culinary adventure like no other! 🍽✨
    """)

    # Session management
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.write("### Sign Up")
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type="password")
        signup_button = st.button("Sign Up")

        if signup_button:
            if new_username and new_password:
                if register_user(new_username, new_password):
                    st.session_state.logged_in = True  # Log in immediately after successful registration
                    st.success("Account created successfully! You are now logged in.")
                else:
                    st.error("Failed to create an account. Please try again.")
            else:
                st.error("Please provide both username and password")

    else:
        # Load recipes
        recipes = load_recipes()

        # Sidebar for advanced search
        st.sidebar.title('Advanced Search')
        category = st.sidebar.selectbox('Category', ['All'] + recipes['Category'].unique().tolist())
        min_rating = st.sidebar.slider('Minimum Rating', min_value=0.0, max_value=5.0, step=0.1)
        min_prep_time = st.sidebar.number_input('Minimum Preparation Time (minutes)', min_value=0)

        # Filter recipes based on advanced search criteria
        filtered_recipes = recipes.copy()
        if category != 'All':
            filtered_recipes = filtered_recipes[filtered_recipes['Category'] == category]
        filtered_recipes = filtered_recipes[filtered_recipes['Rating'] >= min_rating]
        filtered_recipes = filtered_recipes[filtered_recipes['Preparation Time'] >= min_prep_time]

        # Display filtered recipes in an editable table
        edited_recipes = st.data_editor(
            filtered_recipes,
            num_rows='dynamic',
            column_config={
                "Preparation Time": st.column_config.NumberColumn(format="%d min"),
                "Rating": st.column_config.NumberColumn(format="%.1f"),
                "Ratings Count": st.column_config.NumberColumn(format="%d"),
            },
            key='recipe_table'
        )

        # Save changes to the database
        if st.button('Save Changes'):
            # Placeholder for saving changes to the database
            st.success('Changes saved successfully!')

        # Add new recipe
        st.header('Add a New Recipe')
        with st.form('new_recipe_form'):
            new_recipe_name = st.text_input('📝 Recipe Name')
            new_ingredients = st.text_area('🥘 Ingredients')
            new_instructions = st.text_area('📋 Instructions')
            new_prep_time = st.number_input('⏱ Preparation Time (minutes)', min_value=1)
            new_category = st.text_input('🍽 Category')
            new_rating = st.slider('⭐️ Rating', min_value=0.0, max_value=5.0, step=0.1)
            new_ratings_count = st.number_input('👍 Ratings Count', min_value=0)

            submitted = st.form_submit_button('Add Recipe')
            if submitted:
                # Save new recipe to the database
                recipe_data = {
                    "Recipe Name": new_recipe_name,
                    "Ingredients": new_ingredients,
                    "Instructions": new_instructions,
                    "Preparation Time": new_prep_time,
                    "Category": new_category,
                    "Rating": new_rating,
                    "Ratings Count": new_ratings_count
                }
                save_recipe(recipe_data)
                st.success(f'✅ Recipe "{new_recipe_name}" added successfully!')

        # Display a random recipe
        if st.button('🎲 Show a Random Recipe'):
            random_recipe = filtered_recipes.sample(1)
            st.subheader(random_recipe["Recipe Name"].values[0])
            st.write('**🥘 Ingredients:**')
            st.write(random_recipe["Ingredients"].values[0])
            st.write('**📋 Instructions:**')
            st.write(random_recipe["Instructions"].values[0])
            st.write(f'**⏱ Preparation Time:** {random_recipe["Preparation Time"].values[0]} minutes')
            st.write(f'**🍽 Category:** {random_recipe["Category"].values[0]}')
            st.write(f'**⭐️ Rating:** {random_recipe["Rating"].values[0]}')
            st.write(f'**👍 Ratings Count:** {random_recipe["Ratings Count"].values[0]}')

if __name__ == "__main__":
    main()
