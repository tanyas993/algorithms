#1
#1
class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        for a in asteroids:
            while stack and stack[-1] > 0 and a<0:
                if stack[-1] < abs(a):
                    stack.pop()
                    continue
                elif stack[-1] == abs(a):
                    stack.pop()
                    a = 0
                else:
                    a = 0
                break
            if a != 0:
                stack.append(a)
        return stack





#2
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        stack = []
        j =0
        for a in pushed:
            stack.append(a)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j+=1
        return len(stack)==0

