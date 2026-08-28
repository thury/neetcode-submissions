class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let answer = [0,1];
        while (answer[0] < nums.length-1) {
            let searchingFor = target-nums[answer[0]];
            if (nums[answer[1]] == searchingFor) {
                break;
            }
            if (answer[1] == nums.length-1) {
                answer[0] = answer[0] + 1;
                answer[1] = answer[0] + 1;
                continue;
            }
            answer[1] = answer[1] + 1;
        }
        return answer;
    }
}
