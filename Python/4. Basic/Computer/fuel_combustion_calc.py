class Fuel_Combustion:

    def __init__(self):
        self.petrol = 5.09
        self.diesel = 4.85
        self.oil = 2.50
        self.combust = 10

    def cost(self, km_quantity, oil_type, combust):

        if oil_type == 'petrol':
            result = (self.petrol * km_quantity) / combust
            print(result)

        elif oil_type == 'diesel':
            result = (self.diesel * km_quantity) / combust
            print(result)

        elif oil_type == 'oil':
            result = (self.petrol * km_quantity) / combust
            print(result)

