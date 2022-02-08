travel_vlog = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Berlin", "Hamburg", "Stuttgart"]
}

# travel_vlog["city_visited"] = travel_vlog["France"]
# del travel_vlog["France"]

travel_vlog["city_visited"] = travel_vlog.pop("France")
print(travel_vlog)