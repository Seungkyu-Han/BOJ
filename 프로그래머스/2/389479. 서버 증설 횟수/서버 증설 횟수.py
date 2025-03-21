def solution(players, m, k):
    answer = 0
    servers = [0 for _ in range(24)]
    for time in range(24):
        need_computer = players[time] // m
            
        
        if servers[time] < need_computer:
            install_server = need_computer - servers[time]
            answer += install_server
            for plus_time in range(k):
                if time + plus_time < 24:
                    servers[time + plus_time] += install_server
                else:
                    break
        print(time, need_computer, answer)
                    
    print(servers)
        
    return answer