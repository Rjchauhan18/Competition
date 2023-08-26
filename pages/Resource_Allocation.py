import streamlit as st


symptom_priority = {
    "Age of patient < 18 years old" : 1,
    "Age of patient between 18 years and 60 years" : 2,
    "Age of patient > 60 years old" : 3,
    "Fever": 2,
    "Cough": 1,
    "Severe Breathing Difficulty": 3,
    "Fatigue": 1,
    "Loss of Taste or Smell": 1,
    "Loss of Smell or Taste": 1,
    "Loss of Appetite": 1,
    "Loss of Smell or Appetite": 1,

}


def triage_algorithm(selected_symptoms):
    priority_score = 0
    for symptom in selected_symptoms:
        if symptom in symptom_priority:
            priority_score += symptom_priority[symptom]
    return priority_score


def main():
    st.title("COVID-19 Symptom-Based Triage")

    
    st.subheader("Select Symptoms:")
    selected_symptoms = st.multiselect("Choose symptoms:", list(symptom_priority.keys()))

    if st.button("Calculate Priority"):
        if not selected_symptoms:
            st.warning( "Please select at least one symptom.")
        else:
            
            priority_score = triage_algorithm(selected_symptoms)

            
            st.write(f"Priority Score: {priority_score}")
            if priority_score > 0 and priority_score < 3:
                st.write(f"Low Priority")
            elif priority_score >= 3 and priority_score < 6:
                st.write(f"Medium Priority")
            elif priority_score >= 6 and priority_score < 9:
                st.write(f"High Priority")

if __name__ == "__main__":
    main()
