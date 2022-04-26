function solution(array, commands) {
    var answer = [];
    for (let command of commands) {
        i = command[0]; j = command[1]; k = command[2];
        const tmp = array.slice(i-1, j);
        tmp.sort((a,b)=> a-b);
        answer.push(tmp[k-1])
        
    }
    return answer;
}
