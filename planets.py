planet_list = ["Mercury", "Mars"]

planet_list.append('Jupiter')
planet_list.append('Saturn')
planet_list.extend(['Uranus', 'Neptune'])
planet_list.insert(1, 'Venus')
planet_list.insert(2, 'Earth')
print(planet_list)
print('---------------')
rocky_planets = planet_list[:4]
print(rocky_planets)

spacecraft = [('Galileo', ['Jupiter', 'Venus', 'Earth']), ('Pioneer 11', ['Jupiter', 'Saturn', 'Pluto']), ('2001 Mars Odyssey', ['Mars']), ('Voyager 2', ['Jupiter', 'Saturn', 'Uranus', 'Neptune'])]

[print("{} has visited {}".format(craft, planet)) for (craft, planet) in spacecraft]