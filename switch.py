# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# init

from car import Car
from settings import Settings
from safe import Safe_dis
safe_dis = 10
settings = Settings('heavy')
# should be add to Settings
settings.switch_time = 10

car_1 = Car(settings, 10, 0)
car_2 = Car(settings, 10, 1)
car_3 = Car(settings, 10, 0)
q = [car_1, car_2, car_3]


# %%
# Car: add x_switch
def check_lane(car, lane) :
    if car.x == lane or (car.is_switch and car.x_switch == lane) :
        return True
    return False

# test check_lane
car_lane = car_1 = Car(settings, 10, 0)
car_lane.is_switch = 1
car_lane.x_switch = 1
print(check_lane(car_lane, 1))



# %%
# check_switch | direct: -1(x--) 1(x++)

def check_switch(direct, q, i) :
    dest = q[i].x + direct

    if dest >= 0 and dest < settings.lanes :
        former = i + 1
        latter = i - 1
        lenq = len(q)

        while former < lenq :
            if check_lane(q[former], q[i].x + direct) :
                break
            former += 1
        test_former = check_safe(q, i, former) if former < lenq else True

        while latter >= 0 :
            if check_lane(q[latter], q[i].x + direct) :
                break
            latter -= 1
        test_latter = check_safe(q, i, latter) if latter >= 0 else True

        if test_former and test_latter :
            return True
    return False

# check_safe | true: safe false: unsafe
def check_safe(q, i, j):
    safe_dis = Safe_dis(q, i, j) + (q[j].length + q[i].length)/2
    if i < j:
        return (q[j].y - q[i].y) > safe_dis or q[i].speed < q[j].speed
    else:
        return (q[i].y - q[j].y) > safe_dis or q[j].speed < q[i].speed


# %%
# test check_switch

car_1.y = 90
car_2.y = 110
car_3.y = 130
print(check_switch(-1, q, 1))

car_1.y = 90 -1
car_2.y = 110
car_3.y = 130 +1
print(check_switch(-1, q, 1))


# %%
# direct = -1: x--(rignt) | direct = 1 : x++(left)
def switch_lane(direct, car) :
    car.x_switch = car.x
    car.x += direct
    car.is_switch = 1


# %%
# check_pass | True: call-pass 
def check_pass(q, i) :
    former = i + 1
    lenq = len(q)

    while former < lenq :
        if check_lane(q[former], q[i].x) :
            break
        former += 1
    if former < lenq and (not check_safe(q, i, former)) :
        return True
    return False


# %%
# test check_pass
car_1.speed = 100
car_1.y = 100
car_2.y = 110
car_3.y = 120 - 1
assert check_pass([car_1, car_2, car_3], 0) == True


# %%


