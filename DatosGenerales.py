from datetime import datetime
def calcular_edad(customDate):
    today = datetime.today().date()
    age = datetime.strptime(customDate, "%Y-%m-%d").date()
    # age = customDate
    # return f"You are {age}"
    # print(type(age), type(today))
    difference = today - age
    # difference = difference.date()
    return difference

# print(calcular_edad('2021-12-12'))