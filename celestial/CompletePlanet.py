class CompletePlanet():
    
    def __init__(self, planet, system):
        self.name = planet.name
        self.radius = float(planet.radius) * 11.21 #radius is in Jupiter radius
        self.gravity = planet.gravity
        self.distance = system.distance
        self.temperature = system.temperature
