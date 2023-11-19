import time

def expensive_calc_function(x: int)-> int:
    time.sleep(2)
    return x*2

class Cacher:
    _cache = {}

    def value(self, intensity: int)->int:
        if self._cache.get(intensity) is None:
            self._cache[intensity] = expensive_calc_function(intensity)
        return self._cache[intensity]


if __name__ == "__main__":

    user_age = 20
    exercise_intensity = 10

    cacher = Cacher()
    

    if user_age<50:
        print(f"You should swim {cacher.value(exercise_intensity)} minutes")
        print(f"You should jog {cacher.value(exercise_intensity*3)} minutes")

    elif user_age<65:
        print(f"You should jog {cacher.value(exercise_intensity*2)} minutes")

        if exercise_intensity<5:
            print(f"You should swim {cacher.value(exercise_intensity)} minutes")

    else:
        print("Consult with your doctor.")




