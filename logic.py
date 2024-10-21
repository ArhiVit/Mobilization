class Mobilization:
    
    def __init__(self, volume, efficiency, staff, sut, rent, staffTravel, number_staffTravel, delivery, distance, number_delivery, engineer, trailer, placeTravel, otherExpences, k_sut, k_rent, k_staffTravel, k_delivery, k_engineer, k_trailer, k_placeTravel, k_otherExpences):
        self.volume = volume
        self.efficiency = efficiency
        self.staff = staff
        self.sut = sut
        self.rent = rent
        self.staffTravel = staffTravel
        self.number_staffTravel = number_staffTravel
        self.delivery = delivery
        self.distance = distance
        self.number_delivery = number_delivery
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
        
    def get_period(self):
        return round(float(self.volume / self.efficiency / self.staff), 2)
    
    def get_total_sut(self):
        return round(float(self.staff * self.sut * self.k_sut * self.get_period() / 24 * 31), 2)
        
    def get_total_rent(self):
        return round(float(self.staff * self.rent * self.k_rent * self.get_period() / 24 * 31), 2)
    
    def get_total_staffTravel(self):
        return round(float(self.staff * self.staffTravel * self.number_staffTravel * 2 * self.k_staffTravel), 2)
    
    def get_total_delivery(self):
        return round(float(self.distance * self.delivery * self.number_delivery * 2 * self.k_delivery), 2)
    
    def get_total_engineer(self):
        return round(float(((self.engineer + (self.rent + self.sut) * 31) * self.get_period() / 24 + self.staffTravel * 2) * self.k_engineer), 2)
    
    def get_total_trailer(self):
        return round(float(self.trailer * self.k_trailer), 2)
    
    def get_total_placeTravel(self):
        return round(float(self.placeTravel * self.staff * self.get_period() * self.k_placeTravel), 2)
    
    def get_total_otherExpences(self):
        return round(float(self.otherExpences * self.k_otherExpences), 2)
        
if __name__ == "__main__":
    
    #param = [volume, efficiency, staff, sut, rent, staffTravel, number_staffTravel, delivery, distance, number_delivery, engineer, trailer, placeTravel, otherExpences]
    #k_param = [k_sut, k_rent, k_staffTravel, k_delivery, k_engineer, k_trailer, k_placeTravel, k_otherExpences]
    
    param = [1000, 3, 6, 600, 560, 3500, 1, 120, 100, 3, 130000, 150000, 200, 0]
    k_param = [2.11, 1.4, 1.4, 1.2, 1.5, 1.4, 1.4, 1.4]
    
    mob = Mobilization(*param, *k_param)
    print(mob.delivery, mob.k_delivery, mob.get_total_sut())