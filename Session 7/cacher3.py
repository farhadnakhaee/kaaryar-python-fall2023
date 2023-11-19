import time
import functools
import random

@functools.cache
def expensive_calc_function(x: int)-> int:
    time.sleep(2)
    return random.randint(1,20)


if __name__ == "__main__":

    user_age = 20
    exercise_intensity = 10

    

    if user_age<50:
        print(f"You should swim {expensive_calc_function(exercise_intensity)} minutes")
        print(f"You should jog {expensive_calc_function(exercise_intensity)} minutes")

    elif user_age<65:
        print(f"You should jog {expensive_calc_function(exercise_intensity*2)} minutes")

        if exercise_intensity<5:
            print(f"You should swim {expensive_calc_function(exercise_intensity)} minutes")

    else:
        print("Consult with your doctor.")




