// Last updated: 8/5/2025, 2:55:52 PM
public class Solution {
    public int ValidSubarrays(int[] nums) 
    {
        int currentPosition = 0;
        int subarraysFromCurrent = 1;
        int currentOutPut = 0;
        while(currentPosition < nums.Length)
        {
            if((currentPosition + subarraysFromCurrent >= nums.Length) || nums[currentPosition] > nums[currentPosition + subarraysFromCurrent])
            {
             ++currentPosition;
             currentOutPut += subarraysFromCurrent;
             subarraysFromCurrent = 1;
             continue;
            }
            ++subarraysFromCurrent;
        }
        return currentOutPut;
    }
}