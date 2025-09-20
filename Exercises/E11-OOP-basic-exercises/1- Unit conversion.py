# Unit conversion
class UnitUS:
    """Class for converting US units to the metric system"""
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, (int, float)):
            raise TypeError("Value must be an int or float")
        
        if new_value <= 0:
            raise ValueError("Value must be a positive number")
        self._value = new_value

    def inch_to_cm(self):
        return self.value * 2.54

    def foot_to_meters(self):
        return round(self.value / 3.281, 3)

    def pound_to_kg(self):
        return self.value / 2.205

    def __repr__(self):
        return f"UnitUS(value={self.value})"

units = UnitUS(5)
print(f"5 feet = {units.foot_to_meters()} m")
print(f"5 inch = {units.inch_to_cm()} cm")
print(f"5 pounds = {units.pound_to_kg():.2f} kg")
print(units)