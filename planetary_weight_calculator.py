from str import isnumeric
"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""
const_mercury = .376
const_venus = .889
const_mars = .378
const_jupiter = 2.36
const_saturn = 1.081
const_uranus = .815
const_neptune = 1.14

# make an array of all the planets that we have the constants for
planets = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# turn the array to lower case
planets_lower_case = [case.lower() for case in planets]


def main():
    # enter the weight you want to convert
    weight = input("Enter a weight on Earth: ")

    # verify if it is a number and
    while not isnumeric(weight):
        print("You have not entered a valid weight as in it's not a number, please try again!")
        weight = input("Enter a weight on Earth: ")
    weight_on_earth = float(weight)

    # continue to ask for planet untill user enters only letters
    while True:
        planet_name = input("Enter a planet: ").lower()

        if planet_name.isalpha():  # verify if it is only letters
            print(f"You entered: {planet_name}")
            break  # exit while if valid
        else:
            print("Invalid planet name. Please enter only letters and these planets only: ", planets)

    while planet_name.lower() not in planets_lower_case:
        print("You have not entered a valid planet, please try again!")
        planet_name = input("Enter a planet: ").lower()
    """
    if planet_name == "mars":

    elif planet_name == "Venus":
        print("The equivalent weight on Venus: ", round(weight_on_earth * Venus , 2))
    elif planet_name ==
    elif planet_name ==
    elif planet_name ==
    else:
         planet_name ==
         """


if __name__ == "__main__":
    main()