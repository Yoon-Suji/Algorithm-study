function solution(id_list, report, k) {
    let answer = [];
    let count = {};
    let reportAccount = {};
    
    for (let i of id_list){
        count[i] = 0;
        reportAccount[i] = [];
    }
    for (let i=0; i<report.length; i++) {
        let accounts = report[i].split(' ');
        if (reportAccount[accounts[0]].includes(accounts[1])) continue;
        reportAccount[accounts[0]].push(accounts[1]);
        count[accounts[1]]++;
    }
    for (let i of id_list) {
        let mail = 0;
        for (let account of reportAccount[i]) {
            if (count[account] >= k) mail++;
        }
        answer.push(mail);
    }
    
    return answer;
}
