class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1, s2) {
          if (s1.length > s2.length) return false

  const s1CountMap = new Map()
  const s2CountMap = new Map()

  for (let c of s1) {
    s1CountMap.set(c, (s1CountMap.get(c) || 0) + 1)
  }

  for (let c of s2.slice(0, s1.length)) {
    s2CountMap.set(c, (s2CountMap.get(c) || 0) + 1)
  }

  let mathes = 26
  for (let i = 0; i < 26; i++) {
    if (
      s1CountMap.get(String.fromCharCode(i + 97)) !==
      s2CountMap.get(String.fromCharCode(i + 97))
    ) {
      mathes--
    }
  }

  let l = 1
  while (l + s1.length - 1 <= s2.length) {
    if (mathes === 26) return true

    const leftC = s2[l - 1]
    s2CountMap.set(leftC, (s2CountMap.get(leftC) || 0) - 1)
    if ((s1CountMap.get(leftC) || 0) === (s2CountMap.get(leftC) || 0)) {
      mathes++
    } else if (
      (s2CountMap.get(leftC) || 0) + 1 ===
      (s1CountMap.get(leftC) || 0)
    ) {
      mathes--
    }

    const rightC = s2[l + s1.length - 1]
    s2CountMap.set(rightC, (s2CountMap.get(rightC) || 0) + 1)
    if ((s1CountMap.get(rightC) || 0) === (s2CountMap.get(rightC) || 0)) {
      mathes++
    } else if (
      (s2CountMap.get(rightC) || 0) - 1 ===
      (s1CountMap.get(rightC) || 0)
    ) {
      mathes--
    }

    l++
  }

  return false
    }
}
