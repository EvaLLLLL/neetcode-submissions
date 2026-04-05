class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
          let max = 0,
    l = 0
  let charSet = new Set()

  for (let i = 0; i < s.length; i++) {
    while (charSet.has(s[i])) {
      charSet.delete(s[l])
      l++
    }

    charSet.add(s[i])
    max = Math.max(max, i - l + 1)
  }

  return max
    }
}
