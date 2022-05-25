# import pandas
#
# # Filter the data, so it only has the Name and coordinates
# raw_data = pandas.read_csv("tr.csv")
#
# filtered_data = {
#     "city": raw_data[raw_data["capital"] == "admin"].city.tolist(),
#     "x": raw_data[raw_data["capital"] == "admin"].lng.tolist(),
#     "y": raw_data[raw_data["capital"] == "admin"].lat.tolist()
# }
#
# # Normalize the latitude and longitude
# # pandas.DataFrame(filtered_data).to_csv("filtered_list.csv")
# min_x = 26.4
# max_x = 44.0333
# min_y = 36.2
# max_y = 42.0267
#
#
# def normalize_coor(data, rmin, rmax, tmax):
#     norm = []
#     for val in data:
#         norm.append(((val - rmin) / (rmax - rmin) * tmax) - tmax / 2)
#
#     return norm
#     # # Check the results
#     # normalized_vals = {
#     #     "raw": data,
#     #     "normalized": norm
#     # }
#     # print(pandas.DataFrame(normalized_vals))
#
#
# normalized_data = {
#     "city": filtered_data["city"],
#     "x": normalize_coor(filtered_data["x"], min_x, max_x, 1100),
#     "y": normalize_coor(filtered_data["y"], min_y, max_y, 460)
# }
#
# pandas.DataFrame(normalized_data).to_csv("normalized_data.csv")

import turtle

import pandas

screen = turtle.Screen()
screen.title("Turkey Cities Game")
img = "turkey_map.gif"
screen.addshape(img)
screen.screensize()
screen.setup(1.0, 1.0)
turtle.shape(img)
# screen.tracer(0)

normalized_data = pandas.read_csv("normalized_data.csv")


def correct_city(city):
    dot = normalized_data.index[normalized_data["city"] == city][0]
    print(dot)
    city = turtle.Turtle()
    city.penup()
    city.goto(normalized_data["x"][dot], normalized_data["y"][dot])
    city.write(normalized_data["city"][dot])
    # screen.update()


guessed_cities = []
while len(guessed_cities) < 81:
    answer_city = screen.textinput(f"Score: {len(guessed_cities)}/81", "What's another city name?").title()
    if answer_city == "Exit":
        break
    if answer_city in normalized_data["city"].values and answer_city not in guessed_cities:
        correct_city(answer_city)
        guessed_cities.append(answer_city)

cities_missed = []
for city in normalized_data.city.tolist():
    if city not in guessed_cities:
        cities_missed.append(city)

pandas.DataFrame(cities_missed).to_csv("cities_to_learn.csv")
