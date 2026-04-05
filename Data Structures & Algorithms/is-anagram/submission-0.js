class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
            if (s.length !== t.length) return false;
    const mapS = new Map();
    const mapT = new Map();
    for(let i = 0; i < s.length; i++){
        const charS = s[i];
        const charT = t[i];
        mapS.set(charS, mapS.get(charS) ? (mapS.get(charS) || 0) + 1 : 1);
        mapT.set(charT, mapT.get(charT) ? (mapT.get(charT) || 0) + 1 : 1);
    }
    return s.split('').every((char)=>mapS.get(char) === mapT.get(char));
    }
}
