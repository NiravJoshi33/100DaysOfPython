#Nesting Dictionary

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#Nesting list in dictionary
# travel_log = {
#     "France": [ "Paris", "Lille", "Dijon" ],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }
#print(travel_log)

#Nesting dictionary in dictionary
travel_log = {
    "France": {"cities_visited": [ "Paris", "Lille", "Dijon" ], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 6},
}
print(travel_log)

travel_log_d = {
    "country": "France", "cities_visited": [ "Paris", "Lille", "Dijon" ], "total_visits": 12,
    "country": "Germany", "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 6
}

#Nesting a dictionary inside a list
travel = [
    travel_log,
    travel_log_d
]
print(travel)