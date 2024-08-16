
import random as rd
import streamlit as st 
Challenge_1=['DB Chest press', 'Flat bench Bar','shoulder press','max pull ups','DB curls','max squat','max leg press','Deadlift']
Challenge_2=['Row','2km Run','5km run','16km Sprint','Skip','Swim','Cycle','Burpees']

import streamlit as st

# List of items


# Display the dropdown selector with multiselect
selected_items = st.multiselect('Select Challenges to be excluded:',Challenge_1+Challenge_2 )

# Display the selected items

x=rd.randint(0,len(Challenge_1)-1)
y=rd.randint(0,len(Challenge_2)-1)





if st.button("Choose Challneges"):
    st.write(f"Challenge 1: {Challenge_1[x]}\n" ,f"Challenge 2: {Challenge_2[y]}")

