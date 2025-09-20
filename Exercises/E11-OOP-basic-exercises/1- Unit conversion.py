# Unit conversion
class UnitUS:
    """Class for converting US units to the metric system"""
    def __init__(self, value):
        self.value = value

    def inch_to_cm(self):
        return self.value * 2.54

    def foot_to_meters(self):
        return self.value / 3.281

    def pound_to_kg(self):
        return self.value / 2.205

    def __repr__(self):
        return f"UnitUS(value={self.value})"

test = UnitUS(5)
print(test.inch_to_cm())
print(test.foot_to_meters())
print(test.pound_to_kg())
print(test)