def poem_calc_score(d):
    score=0
    for i in range(1,8):
        score +=int( d['q'+str(i)][0])
    return score