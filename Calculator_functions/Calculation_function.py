def transport_footprint(transport_method, distance):
    if transport_method == 'car':
        transport_carbonft = distance * 1.5
    elif transport_method == 'bus':
        transport_carbonft = distance * 1.0
    elif transport_method == 'lorry':
        transport_carbonft = distance * 2.5
    else:
        transport_carbonft = 0

    return transport_carbonft

def electricity_footprint(usage):
    if usage is None:
        return 0
    else:
        electric_carbonft = usage * 0.5
        return electric_carbonft

def food_footprint(category, num_of_meals):
    if category == 'beef':
        food_carbonft = num_of_meals * 2.5
    elif category == 'pork':
        food_carbonft = num_of_meals * 1.8
    elif category == 'chicken':
        food_carbonft = num_of_meals * 1.2
    else:
        food_carbonft = num_of_meals * 1.0

    return food_carbonft

def calculate_total_carbon_footprint(transport_method, distance, usage, category, num_of_meals):
    individual_transportation_carbon = transport_footprint(transport_method, distance)
    individual_electricity_carbon = electricity_footprint(usage)
    individual_food_carbon = food_footprint(category, num_of_meals)

    total_individual_carbon_footprint = individual_transportation_carbon + individual_electricity_carbon + individual_food_carbon
    return total_individual_carbon_footprint

def generate_recommendations(total_carbon_footprint):
    recommendations = []
    if total_carbon_footprint > 10:  # Example threshold for high carbon footprint
        recommendations.append("Consider using public transportation or carpooling to reduce emissions from transportation.")
        recommendations.append("Switch to energy-efficient appliances and turn off unused electronics to reduce electricity consumption.")
        recommendations.append("Reduce consumption of high-carbon foods like beef and pork, and incorporate more plant-based meals into your diet.")
    elif total_carbon_footprint > 5:  # Example threshold for moderate carbon footprint
        recommendations.append("Opt for biking or walking short distances instead of driving.")
        recommendations.append("Unplug chargers and appliances when not in use to save energy.")
        recommendations.append("Choose locally sourced and seasonal foods to reduce carbon emissions from transportation.")
    else:
        recommendations.append("Continue using sustainable transportation methods.")
        recommendations.append("Keep up the good work on managing electricity usage efficiently.")
        recommendations.append("Consider supporting sustainable farming practices by choosing organic and locally produced foods.")

    return recommendations

