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
                    a = None
                else:
                    a = None
                break
            if a is not None:
                stack.append(a)
        return stack


#2
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        stack_push = []
        j =0
        for a in pushed:
            stack_push.append(a)
            while stack_push and stack_push[-1] == popped[j]:
                stack_push.pop()
                j+=1
        return len(stack_push)==0

