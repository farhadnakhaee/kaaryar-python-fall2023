import time

def expensive_calc_function(x: int)-> int:
    time.sleep(2)
    return x*2

if __name__ == "__main__":

    user_age = 70
    exercise_intensity = 10

    result = expensive_calc_function(exercise_intensity)

    if user_age<50:
        print(f"You should swim {result} minutes")
        print(f"You should jog {2*result} minutes")

    elif user_age<65:
        print(f"You should jog {result} minutes")

        if exercise_intensity<5:
            print(f"You should swim {result} minutes")

    else:
        print("Consult with your doctor.")




