# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# init

from settings import Settings
from car import Car, sort_key
from switch import check_switch, switch_lane, check_pass
from collision import collision
from appear import appear, init_appear

q = []
settings = Settings('heavy')
init_appear(settings)
int_time = 0
time = 0
collision_times = 0


# %%
# main loop

while time <= settings.time:
    if time % 1000 == 0:
        print(time, len(q), collision_times)
    int_time += 1
    time = round(int_time * settings.time_unit, 1)
    for car in q:
        if car.update():
            q.remove(car)
    appear(q, time, settings)
    q.sort(key=sort_key)
    for i in range(len(q)-1, -1, -1):
        if q[i].y >= settings.lane_length:  # out of range: remove
            q.pop()
        elif not q[i].is_collide:
            if check_switch(-1, q, i):  # right lane(exist) is available: switch to right lane
                switch_lane(-1, q[i])
            elif check_pass(q, i):   # right lane unavalable and need to pass:
                if check_switch(1, q, i):   # left available: switch to left
                    switch_lane(1, q[i])
                else:                       # left unavailable: collide
                    collision(q, i)
                    collision_times += 1
print(collision_times)


# %%
