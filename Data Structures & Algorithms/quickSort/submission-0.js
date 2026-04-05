/** Pair class to store key-value pairs */
// class Pair {
//   /**
//    * @param {number} key The key to be stored in the pair
//    * @param {string} value The value to be stored in the pair
//    */
//   constructor(key, value) {
//       this.key = key;
//       this.value = value;
//   }
// }
class Solution {
    /**
     * @param {Pair[]} pairs
     * @returns {Pair[]}
     */
    quickSort(pairs) {
        this.quickSortHelper(pairs, 0, pairs.length - 1)
        return pairs
    }

    quickSortHelper(pairs, s, e) {
        if (e - s < 1) return

        let l = s
        for (let i = s; i < e; i++) {
            if (pairs[i].key < pairs[e].key) {
                let temp = pairs[l]
                pairs[l] = pairs[i]
                pairs[i] = temp
                l++
            }
        }

        if (l !== e) {
            let temp = pairs[l]
            pairs[l] = pairs[e]
            pairs[e] = temp
        }

        this.quickSortHelper(pairs, s, l - 1)
        this.quickSortHelper(pairs, l + 1, e)
    }
}
