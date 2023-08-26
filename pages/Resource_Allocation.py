import streamlit as st


st.title("Patient Treatment Prioritization")


age = st.slider("Age (years)", min_value=0, max_value=100, value=30)
weight = st.slider("Weight (kg)", min_value=0, max_value=200, value=70)
sugar_level = st.number_input("Sugar Level (mg/dL)", min_value=0.0, max_value=600.0, value=100.0)

age_weight = 0.3
weight_weight = 0.2
sugar_level_weight = 0.4    

priority_score = (age * age_weight + weight * weight_weight + sugar_level * sugar_level_weight)


st.write("Patient Priority Score:" , priority_score)


if priority_score < 30:
    priority_level = "Low Priority"
elif priority_score < 70:
    priority_level = "Medium Priority"
else:
    priority_level = "High Priority"


st.write(f"Priority Level: {priority_level}")