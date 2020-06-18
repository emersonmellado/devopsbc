# Acummulator operator
value = 100
value_acc = value + 200
print(value, value_acc) #300

value_acc = value_acc + value  # c = c + a
print(value_acc) #400
value_acc = value_acc + value
print(value_acc) #500

value_acc += value # c = c + a
print(value_acc) #600
value_acc -= value # c = c - a
print(value_acc) #500


value_acc *= value # c = c * a| c = 500 * 100
print(value_acc) #50000

value_acc /= value # c = c / a| c = 50000 * 100
print(value_acc) #500

value_acc **= 2 # value_acc = value_acc * value_acc
print(value_acc)
value_acc **= value # value_acc = value_acc * value_acc * value_acc ... 100 times
print(value_acc)