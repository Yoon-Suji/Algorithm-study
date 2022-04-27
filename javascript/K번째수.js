function solution(array, commands) {
    let answer = []; // 변수 선언은 let, const 사용
    for (let command of commands) { // for-Each는 시간이 오래걸리므로 for of나 for문 사용. for in 도 성능 좋지 않음.
        let i = command[0]; let j = command[1]; let k = command[2];
        const tmp = array.slice(i-1, j); // 얕은 복사. 원본 배열은 변하지 않고 새로운 배열 객체 반환
        tmp.sort((a,b)=> a-b); // 배열 자체를 바꿔버리기 때문에 위처럼 인수로 전달된 배열을 복사해서 정렬하는 것이 좋음. 인수는 최대한 건드리지 않도록.
        answer.push(tmp[k-1])
        
    }
    return answer;
}
