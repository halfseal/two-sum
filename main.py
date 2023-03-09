def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


if __name__ == "__main__":
    print("nums : ")
    nums = list(map(int, input().split()))
    print("target : ")
    target = int(input())
    print(twoSum(nums, target))

