// for two strings s and t, we say "t divides s" if and only if s = t + ... + t
// given the strings s and t, return the largest string x such that x divides both s and t

var  gcdOfStrings = function(str1, str2) {
    let gcd = (a, b) => {
        if (b === 0) return a;
        return gcd(b, a % b);
    }
    if (str1 + str2 !== str2 + str1) return "";
    return str1.substring(0, gcd(str1.length, str2.length));
}

console.log(gcdOfStrings("ABCABC", "ABC"))
console.log(gcdOfStrings("ABABAB", "ABAB"))
console.log(gcdOfStrings("LEET", "CODE"))
console.log(gcdOfStrings("ABCDEF", ""))
