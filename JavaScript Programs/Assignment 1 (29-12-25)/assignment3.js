function calculateArea(length, width) {
    if (length < 0 || width < 0) {
        throw new Error("Length and width must be non-negative numbers.");
    }
    return length * width;
}

tempLength=5;
tempWidth=10;
area=calculateArea(tempLength, tempWidth);

try {
    // Test with valid inputs
    let area1=calculateArea(5,10);
    console.log("Area with length 5 and width 10:",area1);
    // Test with invalid inputs
    let area2=calculateArea(-5,10);
    console.log("Area with length -5 and width 10:",area2);
} catch (error) {
    console.error(error.message);
}