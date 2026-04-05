class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
    const countMap = new Map();
    const freq = [
        []
    ];
    nums.forEach((num)=>countMap.set(num, (countMap.get(num) || 0) + 1));
    Array.from(countMap.entries()).forEach(([num, count])=>{
        if (freq[count]) {
            freq[count].push(num);
        } else {
            freq[count] = [
                num
            ];
        }
    });
    const result = [];
    for(let i = freq.length - 1; i > 0; i--){
        if (!freq[i]) continue;
        const nums = Array.from(freq[i]);
        for (let n of nums){
            result.push(n);
        }
        if (result.length === k) {
            return result;
        }
    }
    return result;
    }
}
