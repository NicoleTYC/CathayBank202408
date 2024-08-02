def transform_number(number):
    ret_value = -1
    if  not number.isdigit():
        return -1

    odd_list = []
    even_list = []

    for idx in range(0, len(number)):
        if int(number[idx])%2 ==0 :
            even_list.append(number[idx])
        else:
            odd_list.append(number[idx])
    
    even_list.sort()
    odd_list.sort(reverse=True)

    odd_list.extend(even_list) # combine 2 list

    ret_value = ''.join(odd_list)
    return ret_value

input_number = input("請輸入input數字: ")
# input_number = '417324689435'

output_number = transform_number(input_number)
print("轉換後的數字為:", output_number)