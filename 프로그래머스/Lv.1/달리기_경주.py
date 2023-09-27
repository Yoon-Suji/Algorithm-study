def solution(players, callings):
    index = {value: index for index, value in enumerate(players)}
    for i in range(len(callings)):
        idx = index[callings[i]]
        players[idx], players[idx - 1] = players[idx - 1], players[idx]
        index[callings[i]] -= 1
        index[players[idx]] += 1
    return players
