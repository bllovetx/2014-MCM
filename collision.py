from switch import check_safe, check_lane
def collision(q, i):
    former = i + 1
    lenq = len(q)

    while former < lenq :
        if check_lane(q[former], q[i].x) :
            break
        former += 1
    assert former < lenq and check_safe(q, i, former) == False, "should not collide!"
    
    q[i].is_collide = 1
    q[former].is_collide = 1