// Last updated: 8/5/2025, 2:56:32 PM
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortArrayByParity(int* nums, int numsSize, int* returnSize){
   /*
   Approach
   1. Two pointers in an opposite direction
   2. if you are divisble by 2 - > %2 ==> 0 so i would swap it
   3. if odd and even found swap
   4. if both odd the right pointer moves
   5. if both even then left pointer moves
   [3,1,2,4]  ->.  [4,1,2,3]
    ^     ^           ^ ^
    [3,2,6,7,4]
 */
    int left, right, temp;
    left = 0;
    right = numsSize - 1;
    *returnSize = numsSize;

    
    while (left<right){
        if (nums[left] % 2 != 0 && nums[right] % 2==0 ){
            //swap both
            temp = nums[right];
            nums[right] = nums[left];
            nums[left] = temp;
            left++;
            right--;
        }
        else if (nums[left] % 2 != 0 && nums[right] % 2!=0 )  // both are odd
        {
            right--;
        }
        else if (nums[left] % 2 == 0 && nums[right] % 2==0 )  // both are even
        {
            left++;
        }
        else //right order
        {
            left++;
            right--;
        }
    }

     return nums;
}