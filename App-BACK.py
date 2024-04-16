import streamlit as st
from Calculator_functions.Calculation_function import calculate_total_carbon_footprint, generate_recommendations

def main():
    st.set_page_config(page_title="Planet Pulse", page_icon="🌍", layout="wide")

    st.title("Carbon Footprint Calculator")

    st.write("Welcome to the Carbon Footprint Calculator!")

    # User inputs
    transport_method = st.selectbox("Select Transport Method", ["Car", "Bus", "Lorry"])
    distance = st.number_input("Distance (in miles)")
    usage = st.number_input("Electric Usage (in kWh)")
    category = st.selectbox("Select Food Category", ["Beef", "Pork", "Chicken", "Other"])
    num_of_meals = st.number_input("Number of Meals")

    # Calculate carbon footprint
    total_carbon_footprint = calculate_total_carbon_footprint(transport_method.lower(), distance, usage, category.lower(), num_of_meals)

    # Display results
    st.write(f"Your total carbon footprint is: {total_carbon_footprint} kg CO2e")

    # Generate recommendations
    recommendations = generate_recommendations(total_carbon_footprint)
    st.write("Here are some recommendations to reduce your carbon footprint:")
    for recommendation in recommendations:
        st.write("- " + recommendation)

if __name__ == "__main__":
    main()
