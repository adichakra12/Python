/* 
  Given a string that may have extra spaces at the start and the end,
  return a new string that has the extra spaces at the start and the end trimmed (removed)
  do not remove any other spaces.
*/

const str1 = "   hello world         ";
const expected1 = "hello world";

const str2 = "   hello     world     ";
const expected2 = "hello     world";

/**
 * Trims any leading or trailing white space from the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given string with any leading or trailing white space
 *    stripped.
 * 
 * pseudocode:
 * - make list of string input
 * - find out where first letter is (for loop to check if space or not)
 * - save position of first letter
 * - find and save position of last letter
 * - remove all spaces not in range of two indexes
 */
function trim(str) {

    //const list = str.split("");
    const list = str;
    console.log(str[5]);
    for (var i = 0; i < list.length; i++){
        if (list[i] != " "){
            var first = i;
            break;
        }
    }
    for (var j = list.length - 1; j > -1; j--){
        if (list[j] != " "){
            var last = j;
            break;
        }
    }

    const newString = str.slice(first, last+1);

    console.log(first)
    console.log(last)

    return newString;

}

console.log(trim(str1))

/*****************************************************************************/

/* 
  An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
  typically using all the original letters exactly once.
  Is there a quick way to determine if they aren't an anagram before spending more time?
  Given two strings
  return whether or not they are anagrams
*/

const two_strA1 = "yes";
const two_strB1 = "eys";
const two_expected1 = true;

const two_strA2 = "yes";
const two_strB2 = "eYs";
const two_expected2 = true;

const two_strA3 = "no";
const two_strB3 = "noo";
const two_expected3 = false;

const two_strA4 = "silent";
const two_strB4 = "listen";
const two_expected4 = true;

/**
 * Determines whether s1 and s2 are anagrams of each other.
 * Anagrams have all the same letters but in different orders.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether s1 and s2 are anagrams.
 * 
 * pseudocode:
 * - trim to make sure all spaces are gone, if input has any spaces
 * - check if same length, if not return false
 * - make everything lowercase
 * - split string into array
 * - sort array
 * - join array back to string
 * - check if strings are equal
 * - return boolean
 */
function isAnagram(s1, s2) {

    let string1 = s1.trim();
    let string2 = s2.trim();
    if (string1.length != string2.length){
        return false;
    }
    string1 = string1.toLowerCase();
    string2 = string2.toLowerCase();

    let list1 = string1.split("");
    let list2 = string2.split("");

    list1 = list1.sort();
    list2 = list2.sort();

    string1 = list1.join("");
    string2 = list2.join("");

    if (string1 == string2){
        return true;
    } else {
        return false;
    }

}

console.log(isAnagram(two_strA1, two_strB1))
console.log(isAnagram(two_strA3, two_strB3))