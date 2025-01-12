def solution(cap, n, deliveries, pickups):
    answer = 0
    
    deli_last = n - 1
    pick_last = n - 1
    
    while deli_last > -1 and deliveries[deli_last] == 0:
            deli_last -= 1
            
    while pick_last > -1 and pickups[pick_last] == 0:
            pick_last -= 1
    
    while deli_last > -1 or pick_last > -1:
        answer += max(deli_last + 1, pick_last + 1) * 2
        
        deli_cap, pick_cap = cap, cap
        #deli
        while deli_cap > 0 and deli_last > -1:
            if deliveries[deli_last] > deli_cap:
                deliveries[deli_last] -= deli_cap
                deli_cap = 0
            else:
                deli_cap -= deliveries[deli_last]
                deliveries[deli_last] = 0
                deli_last -= 1
        while deli_last > -1 and deliveries[deli_last] == 0:
            deli_last -= 1
        
        
        #pick
        while pick_cap > 0 and pick_last > -1:
            if pickups[pick_last] > pick_cap:
                pickups[pick_last] -= pick_cap
                pick_cap = 0
            else:
                pick_cap -= pickups[pick_last]
                pickups[pick_last] = 0
                pick_last -= 1
        while pick_last > -1 and pickups[pick_last] == 0:
            pick_last -= 1
    
    while pick_last > -1:
        answer += (pick_last + 1) * 2
        
        pick_cap = cap
        
        while pick_cap > 0 and pick_last > -1:
            if pickups[pick_last] > pick_cap:
                pickups[pick_last] -= pick_cap
                pick_cap = 0
            else:
                pick_cap -= pickups[pick_last]
                pickups[pick_last] = 0
                pick_last -= 1
        while pick_last > -1 and pickups[pick_last] == 0:
            pick_last -= 1
            
    while deli_last > -1:
        answer += (deli_last + 1) * 2
        
        deli_cap = cap
        
        while deli_cap > 0 and deli_last > -1:
            if deliveries[deli_last] > deli_cap:
                deliveries[deli_last] -= deli_cap
                deli_cap = 0
            else:
                deli_cap -= deliveries[deli_last]
                deli_cap[deli_last] = 0
                deli_last -= 1
        while deli_last > -1 and deliveries[deli_last] == 0:
            deli_last -= 1
            
    return answer