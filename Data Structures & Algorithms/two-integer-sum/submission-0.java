class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] indices = new int[2];
        HashMap<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < nums.length; i++) {
            int comp = target - nums[i];
            if(map.containsKey(comp)) {
                indices[0] = map.get(comp); 
                indices[1] = i;
                break; // We found the indices, no need to continue
            } else {
                map.put(nums[i], i);
            }
        }
        return indices;
    }
}
