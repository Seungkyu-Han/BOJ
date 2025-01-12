def solution(enroll, referral, seller, amount):
    parent = dict()
    money = dict()
    
    for i in range(len(enroll)):
        cur_name, cur_parent = enroll[i], referral[i]
        
        money[cur_name] = 0
        
        if cur_parent == '-':
            parent[cur_name] = 'center'
        else:
            parent[cur_name] = cur_parent
    
    for i in range(len(amount)):
        cur_money = amount[i] * 100
        cur_seller = seller[i]
        
        while cur_money > 0 and cur_seller != 'center':
            incentive = cur_money // 10
            
            money[cur_seller] += (cur_money - incentive)
            
            cur_money = incentive
            cur_seller = parent[cur_seller]
    
    result = []
    
    for name in enroll:
        result.append(money[name])
    
    return result