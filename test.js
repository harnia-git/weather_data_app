// const myArray = [1, 2, 3, 4, 5, 6, 7, 8, 9];
// const number = 3;

// const result = [...Array(Math.ceil(myArray.length / number))].map((_, index) => myArray.slice(index * number, (index + 1) * number));
// console.log(result);

const myArray = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const result = myArray.map((element, index) => {
  console.log(`Element: ${element}, Index: ${index}`);
});