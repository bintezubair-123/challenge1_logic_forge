nums=[-1,1,0,-3,3]
def team_impact(contributions):
    n = len(contributions)
    impact = [1] * n


    left_product = 1
    for i in range(n):
        impact[i] = left_product
        left_product *= contributions[i]


    right_product = 1
    for i in range(n - 1, -1, -1):
        impact[i] *= right_product
        right_product *= contributions[i]

    return impact

print(team_impact([-1,1,0,-3,3]))        
        
