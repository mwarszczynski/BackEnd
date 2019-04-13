from space.planet import  Planet
from space.calc import planet_mass, planet_vol

namek = Planet('Namek', 3000, 8, 'Naboo System')

namek_mass = planet_mass(namek.gravity, namek.radius)
namek_vol = planet_vol(namek.radius)

print(f'{namek.name} has a mass of {namek_mass} and volume of {namek_vol}')

# naboo = Planet('Naboo', 30, 1, 'Naboo system')
#
# naboo.vol = planet_vol(Planet.radius)
# print('=', naboo.vol)