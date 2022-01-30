def calc_score(dict):
    score=0
    for i in range(1,8):
        score +=int( dict['q'+str(i)][0])
    return score