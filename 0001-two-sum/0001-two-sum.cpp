class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<pair<int,int>> arr;
        for (int i = 0; i < nums.size(); i++)
            arr.push_back({nums[i],i});
        sort(arr.begin(), arr.end());
        int a = 0;
        int b = nums.size() - 1;
        vector<int> ans(2);
        while (a < b){
            if (arr[a].first + arr[b].first > target)
                b--;
            else if (arr[a].first + arr[b].first < target)
                a++;
            else
                return {arr[a].second, arr[b].second};
        }
        return {};
    }
};