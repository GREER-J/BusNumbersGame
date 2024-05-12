from world_state import Locations

counter = 0
for location in Locations._member_names_:
    for in_car_option in ['true', 'false']:
        for has_keys_option in ['true', 'false']:
            counter += 1
            print(f"{counter}: has_keys: {has_keys_option}, in_car: {in_car_option}, location: {location}")
            