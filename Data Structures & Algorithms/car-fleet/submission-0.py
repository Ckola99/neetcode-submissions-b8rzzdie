class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        travelling_cars = []

        for i in range(len(position)):
            travel_time = (target - position[i]) / speed[i]
            travelling_cars.append((position[i], travel_time))

        travelling_cars.sort(reverse=True)

        fleet_time = 0
        fleets = 0

        for pos, car_time in travelling_cars:
            if car_time > fleet_time:
                fleets += 1
                fleet_time = car_time

        return fleets