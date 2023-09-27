def solution(name, yearning, photo):
    yearning_dict = {}
    answer = []
    for i in range(len(name)):
        yearning_dict[name[i]] = yearning[i]
    for i in range(len(photo)):
        score = 0
        for j in range(len(photo[i])):
            if (yearning_dict.get(photo[i][j])): score += yearning_dict[photo[i][j]]
        answer.append(score)
    
    return answer
