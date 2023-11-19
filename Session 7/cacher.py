import time

def expensive_calc_function(x: int)-> int:
    time.sleep(2)
    return x*2

class Cacher:
    def  __init__(self, intensity:int) -> None:
        self._value = None
        self.intensity = intensity
    
    @property
    def value(self):
        if self._value is None:
            self._value = expensive_calc_function(self.intensity)
        return self._value


if __name__ == "__main__":

    user_age = 20
    exercise_intensity = 5

    cacher = Cacher(exercise_intensity)
    cacher2 = Cacher(exercise_intensity+5)
    

    if user_age<50:
        print(f"You should swim {cacher.value} minutes")
        print(f"You should jog {2*cacher.value} minutes")

    elif user_age<65:
        print(f"You should jog {cacher.value} minutes")

        if exercise_intensity<5:
            print(f"You should swim {cacher.value} minutes")

    else:
        print("Consult with your doctor.")




