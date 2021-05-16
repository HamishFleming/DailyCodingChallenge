




def record(order_id):
    recordlog.append(order_id)
    return 0

def get_last(i):
    val - len(recordlog)-int(i)
    return recordlog[val]

recordlog=[]
record(input("Enter Order ID: "))
record(input("Enter Order ID: "))
record(input("Enter Order ID: "))
record(input("Enter Order ID: "))
record(input("Enter Order ID: "))
print(get_last(input("Enter i to return)))
