class TimeTraveler:
    registry = 0
    travelers = []
    def __init__(self, codename, origin_year, destination_year):
        self.codename = codename
        self.origin_year = origin_year
        self.destination_year = destination_year
        TimeTraveler.registry += 1
        TimeTraveler.travelers.append(self)
    @classmethod
    def show_registry(cls):
        print(f"Total number of travelers = {cls.registry}")
        for traveler in cls.travelers:
            print(f"Codename={traveler.codename}")

    @staticmethod
    def year_status(year):
        if year <= 2025:
            print("past")
        elif year == 2026:
            print("present")
        else:
            print("future")


r = TimeTraveler("ai", 2020, 2024)
s = TimeTraveler("cse", 2022, 2026)
t = TimeTraveler("ds", 2026, 2030)

print(TimeTraveler.registry)
TimeTraveler.year_status(2026)
TimeTraveler.show_registry()
