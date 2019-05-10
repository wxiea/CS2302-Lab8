import math
import random
import numpy as np

def a(t):
    ans = math.sin(t)
    return ans

def b(t):
    ans = math.cos(t)
    return ans

def c(t):
    ans = math.tan(t)
    return ans

def d(t):
    ans = 1 / math.cos(t)
    return ans

def e(t):
    if t > 1 or t < -1:
        return False
    ans = math.asin(t)
    return ans

def f(t):
    if t > 1 or t < -1:
        return False
    ans = math.acos(t)
    return ans

def g(t):
    ans = math.atan(t)
    return ans

def h(t):
    ans = math.sin(-t)
    return ans

def i(t):
    ans = math.cos(-t)
    return ans

def j(t):
    ans = math.tan(-t)
    return ans

def k(t):
    ans1 = math.sin(t)
    ans2 = math.cos(t)
    ans3 = ans1 / ans2
    return ans3

def l(t):
    ans1 = math.sin(t/2)
    ans2 = math.cos(t/2)
    ans3 = (2*ans1) * (2*ans2)
    return ans3

def m(t):
    ans = math.pow(math.sin(t), 2)
    return ans

def n(t):
    ans1 = math.pow(math.cos(t), 2)
    ans2 = 1 - ans1
    return ans2

def o(t):
    ans1 = math.cos(2*t)
    ans2 = 1 - ans1
    ans3 = ans2 / 2
    return ans3

def p(t):
    ans1 = math.cos(t)
    ans2 = 1 / ans1
    return ans2


def equal(f1, f2,tries=1000,tolerance=0.0001):
    for i in range(tries):
        y1 = f1
        y2 = f2
        if np.abs(y1-y2)>tolerance:
            return False
    return True


print(a(1))
print(b(1))
print(c(1))
print(d(1))
print(e(1))
print(f(1))
print(g(1))
print(h(1))
print(i(1))
print(j(1))
print(k(1))
print(l(1))
print(m(1))
print(n(1))
print(o(1))
print(p(1))

t =  random.uniform(-3.14, 3.14)
print('Number: ', t)
print(equal(c(t),k(t)))




def Backtracking(list, last, goal):
    if goal ==0:
        return True, [], []
    if goal<0 or last<0:
        return False, [], []
    res, subset, newlist = Backtracking(list,last-1,goal-list[last]) # Take S[last]
    #print(Backtracking(list,last-1,goal-list[last]))
    if res:
        subset.append(list[last])
        print(subset)
        temp = list[:last]
        for i in range(len(temp)):
            newlist.append(list[i])
        for i in range(len(newlist)):
            for x in range(len(newlist)):
                if x < len(newlist) and i < len(newlist):
                    if newlist[i] == newlist[x]:
                        print(newlist)
                        newlist.pop(i)
                        print(newlist)
            for j in range(len(subset)):
                if i < len(newlist):                   
                    if newlist[i] == subset[j]:
                        newlist.pop(i)
        #print(newlist)
        return True, subset, newlist
    else:
        return Backtracking(list,last-1,goal) # Don't take S[last]

sum = 0
S = [1,2,4,6,7,8,10]
#[1,2,3,4,5]
#[2,4,5,9,12]
#[2,4,5,9,12]
# [2,4,5,9,12]
for i in range(len(S)):
    sum += S[i]
goal = sum / 2
print('Goal =',goal)
a,s,l = Backtracking(S,len(S)-1,goal)
if a:
    print('Solution:',s,l)
else:
    print('There is no solution')    
    
    
    


