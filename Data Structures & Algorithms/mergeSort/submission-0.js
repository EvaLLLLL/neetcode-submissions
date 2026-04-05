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
    mergeSort(pairs) {
        this.mergeSortHelper(pairs, 0, pairs.length - 1)
        return pairs
    }

    mergeSortHelper(pairs, s, e) {
        if (e - s + 1 <= 1) return

        let m = Math.floor((s + e) / 2)

        this.mergeSortHelper(pairs, s, m)
        this.mergeSortHelper(pairs, m + 1, e)

        this.merge(pairs, s, m, e)
    }

    merge(pairs, s, m, e) {
        let i = 0
        let j = 0
        let k = s

        const left = pairs.slice(s, m + 1)
        const right = pairs.slice(m + 1, e + 1)

        while (i < left.length && j < right.length) {
            if (left[i].key <= right[j].key) {
                pairs[k] = left[i]
                i++
            } else {
                pairs[k] = right[j]
                j++
            }
            k++
        }

        while(i < left.length) {
            pairs[k] = left[i]
            i++
            k++
        }

        while (j < right.length) {
            pairs[k] = right[j]
            j++
            k++
        }
    }
}
