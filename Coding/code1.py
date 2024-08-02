length = 4

x = length*2 -1
y = length

for i in range(y):
    output = ''
    star_count = i+1
    next_star = -1
    for j in range(x):
        if (i+j ==length-1) or (i+j == next_star and star_count>0):
           next_star = i+j+2
           star_count -=1
           output += '*'
        else:
           output += ' '

    print(output)
    

