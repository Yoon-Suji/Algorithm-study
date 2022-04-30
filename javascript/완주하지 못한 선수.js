function solution(participant, completion) {
    const _completion = completion.slice();
    const _participant = participant.slice();
    let length = _completion.length;
    _completion.sort()
    _participant.sort()
    
    var answer = '';
    
    for (let i=0; i<length+1; i++) {
        if (_participant[i] !== _completion[i]) {
            answer = _participant[i] // 배열 인덱스 벗어나면 undefined 값 출력됨
            break
        }
    }
    return answer;
}

// 해시를 활용한 풀이방법. 
// function solution(participant, completion) {
//     const map = new Map();

//     for(let i = 0; i < participant.length; i++) {
//         let a = participant[i], 
//             b = completion[i];

//         map.set(a, (map.get(a) || 0) + 1);
//         map.set(b, (map.get(b) || 0) - 1);
//     }

//     for(let [k, v] of map) {
//         if(v > 0) return k;
//     }

//     return 'nothing';
// }
