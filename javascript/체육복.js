function solution(n, lost, reserve) {
    let answer = 0;
    let count = Array.from({length: n}, () => 1); // [1, 1, 1, 1, 1] 배열 생성
    count.unshift(0); // 앞에 0 추가.
    
    for (let i=0; i<lost.length; i++) {
        count[lost[i]]--;
    }
    
    for (let i=0; i<reserve.length; i++) {
        count[reserve[i]]++;
    }

    for (let i=1; i<n+1; i++) {
        if (count[i] === 0) {
            if (count[i-1] === 2) {
                answer++;
                continue;
            }
            if (count[i+1] === 2) {
                answer++;
                count[i+1]--;
                continue;
            }
            continue;
        }
        answer++;
    }
    return answer;
}
