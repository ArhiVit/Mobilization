class Mobilization:
    
    def __init__(self, volume, efficiency, staff, sut, rent, staffTravel, numberTravel, delivery, distance, numberDelivery, engineer, trailer, placeTravel, otherExpences, k_sut, k_rent, k_staffTravel, k_delivery, k_engineer, k_trailer, k_placeTravel, k_otherExpences):
        self.volume = volume
        self.efficiency = efficiency
        self.staff = staff
        self.sut = sut
        self.rent = rent
        self.staffTravel = staffTravel
        self.numberTravel = numberTravel
        self.delivery = delivery
        self.distance = distance
        self.numberDelivery = numberDelivery
        self.engineer = engineer
        self.trailer = trailer
        self.placeTravel = placeTravel
        self.otherExpences = otherExpences
        self.k_sut = k_sut
        self.k_rent = k_rent
        self.k_staffTravel = k_staffTravel
        self.k_delivery = k_delivery
        self.k_engineer = k_engineer
        self.k_trailer = k_trailer
        self.k_placeTravel = k_placeTravel
        self.k_otherExpences = k_otherExpences
        
    def get_total_sut(self):
        return self.sut * self.k_sut
        
        
if __name__ == "__main__":
    
    #param = [volume, efficiency, staff, sut, rent, staffTravel, numberTravel, delivery, distance, numberDelivery, engineer, trailer, placeTravel, otherExpences]
    #k_param = [k_sut, k_rent, k_staffTravel, k_delivery, k_engineer, k_trailer, k_placeTravel, k_otherExpences]
    
    param = [1000, 3, 6, 600, 560, 3500, 1, 120, 100, 3, 130000, 150000, 200, 0]
    k_param = [2.11, 1.4, 1.4, 1.2, 1.5, 1.4, 1.4, 1.4]
    
    mob = Mobilization(*param, *k_param)
    print(mob.delivery, mob.k_delivery, mob.get_total_sut())