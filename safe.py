def Safe_dis(q, i, j):
    if q[i].speed < q[j].speed:
        speed_low = q[i].speed - 5
        speed_high = q[j].speed
    else:
        speed_low = q[j].speed - 5
        speed_high = q[i].speed
    assert speed_low <= (speed_high-5)
    return (speed_high**2)/20 - (speed_low**2)/20 + speed_high*1.12 + 10