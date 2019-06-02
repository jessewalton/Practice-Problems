// given a string, find the largest substring with the same starting and ending letter

function testGetSub() {
  var tests = {
    str: ["abcdefghijkclmnopq", "abadefbhijklmnopqr", "sup girl", "axbxcde"],
    sol: ["cdefghijkc", "badefb", "", "xbx"],
  };
  tests.num = tests.str.length;
  
  for (var testNum = 0; testNum < tests.num; testNum++) {
    var solution = getSub(tests.str[testNum]);
    if (tests.sol[testNum] === solution) {
      console.log("[pass] '" + tests.str[testNum] + "' == '" + solution + "'");
    } else {
      console.log("[fail] '" + tests.str[testNum] + "' != '" + solution + "'");
    }
  }
}
testGetSub();


function getSub(str){
  if (str.length < 2) return str;
  
  var leftPtr = 0;
  var rightPtr = str.length - 1;
  var leftChar = "";
  var rightChar = "";
  var leftCharMap = {};
  var rightCharMap = {};
 
  // odd sized string, add middle char to right map
  if (str.length % 2 === 1) {
    var idx = Math.floor(str.length / 2);
    rightCharMap[str[idx]] = idx;
  }
 
  // iterate over string from left and right
  // add each letter to map of respective half
  // if a match is found on both sides, return
  while (rightPtr > str.length/2) {
    leftChar = str[leftPtr];
    rightChar = str[rightPtr];
    
    // if left char not in left map, add idx
    if (!leftCharMap[leftChar]) {
      leftCharMap[leftChar] = leftPtr;
    } else { // else, add alt idx
      leftCharMap[leftChar + "_alt"] = leftPtr;

      // track same-side matches incase cross-side match isn't found
      // get current longest same side string and length
      if (leftCharMap.longestMatch) {
        var longChar = leftCharMap.longestMatch;
        var prevLength = leftCharMap[longChar + "_alt"] - leftCharMap[longChar] + 1;
      
        // if this alt makes a longer substring, update it
        var currLength = leftCharMap[leftChar + "_alt"] - leftCharMap[leftChar] + 1;
        if (currLength > prevLength) {
          leftCharMap.longestMatch = leftChar;
        }
      } else { // no longest match exists, add this one
        leftCharMap.longestMatch = leftChar;
      }
    }
    
    // if right char not in right map, add idx
    if (!rightCharMap[rightChar]) {
      rightCharMap[rightChar] = rightPtr;
    } else { // else, add alt idx
      rightCharMap[rightChar + "_alt"] = rightPtr;
    
      // track same-side matches incase cross-side match isn't found
      // get current longest same side string and length
      if (rightCharMap.longestMatch) {
        var longChar = rightCharMap.longestMatch;
        var prevLength = rightCharMap[longChar + "_alt"] - rightCharMap[longChar] + 1;
      
        // if this alt makes a longer substring, update it
        var currLength = rightCharMap[leftChar + "_alt"] - rightCharMap[leftChar] + 1;
        if (currLength > prevLength) {
          rightCharMap.longestMatch = rightChar;
        }
      } else { // no longest match exists, add this one
        rightCharMap.longestMatch = rightChar;
      }
    }
    
    // if left char in right map, return substring
    if (rightCharMap[leftChar]) {
      return str.substring(leftCharMap[leftChar], rightCharMap[leftChar] + 1);
    }
    
    // if right char in left map, return substring
    if (leftCharMap[rightChar]) {
      return str.substring(leftCharMap[rightChar], rightCharMap[rightChar] + 1);
    }
    
    leftPtr++;
    rightPtr--;
  }
  
  // outside of while loop, no cross-side matches were found
  // check for same side matches
  
  var longestLeftSideMatch = 0;
  if (leftCharMap.longestMatch) {
    longestChar = leftCharMap.longestMatch;
    longestLeftSideMatch = leftCharMap[longestChar + "_alt"] - leftCharMap[longestChar];
  }
  
  var longestRightSideMatch = 0;
  if (rightCharMap.longestMatch) {
    longestChar = rightCharMap.longestMatch;
    longestRightSideMatch = rightCharMap[longestChar] - leftCharMap[longestChar + "_alt"];
  }
 
  // no same side matches found, return empty string
  if (longestLeftSideMatch === 0 && longestRightSideMatch === 0) {
    return "";
  } 

  // same side match found, return substring
  var leftIdx = 0;
  var rightIdx = 0;
  if (longestLeftSideMatch >= longestRightSideMatch) {
    leftIdx = leftCharMap[leftCharMap.longestMatch];
    rightIdx = leftCharMap[leftCharMap.longestMatch + "_alt"];
  } else {
    leftIdx = rightCharMap[rightCharMap.longestMatch + "_alt"];
    rightIdx = rightCharMap[rightCharMap.longestMatch];
  }
  return str.substring(leftIdx, rightIdx + 1);
}
