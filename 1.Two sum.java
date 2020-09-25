/* this can be done in multiple ways... if u want i can put some more approaches (write a issue)
Using HashMap, it takes >1ms i.e faster than 99.96% submissions on leetcode */
class Solution {
    public int[] twoSum(int[] nums, int target) {
        //using hashmap
        Map<Integer,Integer> myMap = new HashMap<>();
        for(int i=0; i<nums.length; i++){
            int comp = target-nums[i];
            if(myMap.containsKey(comp)){
                return new int[] {myMap.get(comp),i};
            }
            myMap.put(nums[i],i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}
