export default function appendToEachArrayValue(array, appendString) {
  array = [];
  for (const value of array) {
    array.push(appendString + value);
  };
  return array;
}
