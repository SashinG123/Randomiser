import random as rd
import streamlit as st 

Challenge_1 = ['DB Chest press', 'Flat bench Bar', 'shoulder press', 'max pull ups', 'DB curls', 'max squat', 'max leg press', 'Deadlift']
Challenge_2 = ['Row', '2km Run', '5km run', '16km Sprint', 'Skip', 'Swim', 'Cycle', 'Burpees']

# Display the dropdown selector with multiselect
selected_items = st.multiselect('Select Challenges to be excluded:', Challenge_1 + Challenge_2)

# Filter out the selected challenges
filtered_challenge_1 = [challenge for challenge in Challenge_1 if challenge not in selected_items]
filtered_challenge_2 = [challenge for challenge in Challenge_2 if challenge not in selected_items]

# Randomly select from the filtered lists
if filtered_challenge_1:
    x = rd.choice(filtered_challenge_1)
else:
    x = "No available challenges in Challenge 1"

if filtered_challenge_2:
    y = rd.choice(filtered_challenge_2)
else:
    y = "No available challenges in Challenge 2"

if st.button("Choose Challenges"):
    st.write(f"Challenge 1: {x}\n", f"Challenge 2: {y}")
