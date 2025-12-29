function createRandomArray(length, min, max) {
    if (length <= 0) {
        console.log("Array length must be greater then 0");
        return [];
    }
    let arr = [];
    for (let i=0; i<length;i++) {
        let randomNum=Math.floor(Math.random()*(max-min+1))+min;
        arr.push(randomNum);
    }
    return arr;
}


function findLargestNumber(arr) {
    if (arr.length === 0) {
        console.log("Array is empty");
        return null;
    }
    let largest=arr[0];
    for (let i=1;i<arr.length;i++) {
        if (arr[i]>largest) {
            largest=arr[i];
        }
    }
    return largest;
}


let arrayLength=10;
let minValue=1;
let maxValue=100;

let randomArray=createRandomArray(arrayLength, minValue, maxValue);

console.log(randomArray);

console.log("Largest number in the array:",findLargestNumber(randomArray));