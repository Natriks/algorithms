from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        knight = {'x': 0, 'y': 0, 'hp': 0}
        min_hp = 0
        max_y = len(dungeon) - 1
        max_x = len(dungeon[0]) - 1
        path = []
        while knight['x'] <= max_x and knight['y'] <= max_y:
            knight['hp'] += dungeon[knight['y']][knight['x']]
            min_hp = min(min_hp, knight['hp'])
            path.append(dungeon[knight['y']][knight['x']])
            if knight['x'] == max_x:
                knight['y'] += 1
                continue
            if knight['y'] == max_y:
                knight['x'] += 1
                continue
            if dungeon[knight['y'] + 1][knight['x']] > dungeon[knight['y']][knight['x'] + 1]:
                knight['y'] += 1
            else:
                knight['x'] += 1
        return abs(min_hp) + 1


sol = Solution()
a = sol.calculateMinimumHP([[-2, -3, 3],
                            [-5, -10, 1],
                            [10, 30, -5]])
print(a)  # 7
a = sol.calculateMinimumHP([[1, -3, 3],
                            [0, -2, 0],
                            [-3, -3, -3]])
print(a)  # 3
