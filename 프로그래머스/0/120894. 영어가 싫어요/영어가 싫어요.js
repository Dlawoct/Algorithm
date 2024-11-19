function solution(numbers) {
    // 숫자 단어와 대응되는 숫자
    const numDict = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    };
    
    // 숫자 단어들을 문자열에서 찾아서 해당하는 숫자로 바꿈
    for (let word in numDict) {
        numbers = numbers.split(word).join(numDict[word]);
    }
    
    // 변환된 결과를 정수로 변환해서 반환
    return parseInt(numbers);
}