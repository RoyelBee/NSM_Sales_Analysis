import pandas as pd

def number_style(value):

    if (len(value) > 6):
        return str(value[0:len(value) - 6] + "," + value[len(value) - 6:len(value) - 3] + ","
                   + value[len(value) - 3:len(value)])
    elif (len(value) > 3):
        return str(value[0:len(value) - 3] + "," + value[len(value) - 3:len(value)])
    elif (len(value) > 1):
        return value

    elif (len(value) == 1 and str(value) == '0'):
        return '-'
    else:
        return value

def day_calculator(value1, value2):
    value1 = value1
    value2 = int(value2)
    if value2 >= 0  and  value1 > .001:
        day = value2 / value1
        if day > 35:
            result = str(int(value2))  + '<br>'+ str(int(day)) + 'D'
        else:
            day = day - 35
            result = str(int(value2)) + '<br>' + str(int(day)) + 'D'


    else:
        result= str(value2)
    return  result

# print(day_calculator(.461, 162))
def warning(daily_sales, total_stock):

    if daily_sales <= 0:
        return False
    else:
        days_passed = total_stock / daily_sales
        # Color for NIL
        if days_passed <= 0:
            set_color = '#ff2300'

        # Super Under Stock
        elif days_passed >= 15:
            set_color = '#ff971a'

        # Under Stock
        elif days_passed <= 35:
            set_color = '#eee298'

        # Color for Normal
        elif days_passed <= 45:
            set_color = '#ffffff'

        # Color for Over Stock
        elif days_passed <= 60:
            set_color = '#cbe14c'
        else:
            # Super over stock
            set_color = '#fff900'

        return set_color


def branch_warning(total_stock):
    s = str(total_stock)

    if s== '-' or total_stock <= 0:
        set_color = 'red'
    # if total_stock <= 0:
    #     set_color = '#ff2300'

    # Super Under Stock
    elif total_stock >= 1 and total_stock <= 15:
        set_color = '#ff971a'

    # Under Stock
    elif total_stock >= 16 and total_stock <= 35:
        set_color = '#eee298'

    # Color for Normal
    elif total_stock >= 36 and total_stock <= 45:
        set_color = '#ffffff'

    # Color for Over Stock
    elif total_stock >= 46 and total_stock <= 60:
        set_color = '#cbe14c'

    elif total_stock >= 61 and total_stock <= 300000:
        set_color = '#fff900'
    else:
        # Super over stock
        set_color = 'red'

    return set_color


def create_dup_count_list(excel, colName):
    df = pd.DataFrame(excel)
    colRaw = df[colName].tolist()
    df1 = df
    df1.loc[df1.duplicated(subset=[colName]), colName] = ''
    colDup = df1[colName].tolist()
    k = 0
    colList = []
    for j in colDup:
        item1 = j
        i = 0
        for item in colRaw:
            if (item == item1):
                i = i + 1
        colList.insert(k, i)
        k = k + 1
    return colList


def status_color(status):

    if status == 'Within 15 Days':
        color = '#fd8947'

    elif status == 'Within 30 Days':
        color = '#eaff3d'

    elif status == 'Within 60 Days':
        color = '#e1e300'

    elif status == 'Within 90 Days':
        color = '#b2eb05'

    elif status == 'Within 180 Days':
        color = '#629B00'

    elif status == 'Within 210 Days':
        color = '#124B00'

    elif status == 'More Than 210 Days':
        color = '#ffffff'

    elif status == 'More Than 1 Year':
        color = '#ffffff'
    elif status == '' or len(status) <1:
        color = '#ffffff'
    else:
        color = '#f40d0d'
    return color

def integer_converter(num):
    if num == '':
        num = num
    else:
        num  = int(num)
    return num
