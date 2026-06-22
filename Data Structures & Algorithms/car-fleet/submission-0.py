class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []

        for p, s in zip(position, speed):
            cars.append((p, (target - p) / p))

        cars.sort(reverse=True)

        stack = []

        for pos, time in cars:
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

            return len(stack)