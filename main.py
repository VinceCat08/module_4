import fake_math as fm
import true_math as tm

fake_divide = fm.divide
true_divide = tm.divide

result1 = fake_divide(48, 8)
result2 = fake_divide(10, 0)
result3 = true_divide(81, 9)
result4 = true_divide(22, 0)

print(result1)
print(result2)
print(result3)
print(result4)