def quadSolve(a, b, c):
        ans = []
        
        if (b * b) - (4 * a * c) == 0:
                ans.append((b * -1) / (2 * a))
        elif (b * b) - (4 * a * c) > 0:
                ans.append( ( (b*-1) + ( (b*b) - (4*a*c) ) ) )
                ans.append( ( (b*-1) - ( (b*b) - (4*a*c) ) ) )
        return ans


print("QUADRATIC SOLVER")
print("enter the coefficients for ax^2 + bx + c = 0")

a = int(input())
b = int(input())
c = int(input())

result = quadSolve(a, b, c)

if len(result) == 0:
        print("no real solutions")
else:
        print(quadSolve(a, b, c))

