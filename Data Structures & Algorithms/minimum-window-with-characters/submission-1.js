class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {string}
     */
    minWindow(s, t) {
          let tMap = new Map()
  let cMap = new Map()
  let res = ''

  for (let c of t) {
    tMap.set(c, (tMap.get(c) || 0) + 1)
    cMap.set(c, 0)
  }

  let left = 0
  let count = 0

  for (let right = 0; right < s.length; right++) {
    if (cMap.has(s[right])) {
      cMap.set(s[right], (cMap.get(s[right]) || 0) + 1)

      if ((cMap.get(s[right]) || 0) === (tMap.get(s[right]) || 0)) {
        count++
      }
    }

    while (count >= tMap.size) {
      if (res.length === 0 || right - left + 1 <= res.length) {
        res = s.slice(left, right + 1)
      }

      if (cMap.has(s[left])) {
        if ((cMap.get(s[left]) || 0) === (tMap.get(s[left]) || 0)) {
          count--
        }

        cMap.set(s[left], (cMap.get(s[left]) || 0) - 1)
      }

      left++
    }
  }

  return res
    }
}
