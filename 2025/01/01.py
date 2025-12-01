with open("01_input.txt", "r") as file_content:
    input = file_content.read().split()

dail_position = 50
prev_position = 50
num_zeros = 0

for line in input:
    rem_direction = line.strip('RL')
    if len(rem_direction) > 2:
        rotation = int(rem_direction[-2:])
        num_zeros = num_zeros + int(rem_direction[:len(rem_direction)-2])
    else:
        rotation = int(rem_direction)

    if line[0] == "R":
        dail_position = dail_position + rotation
    elif line[0] == "L":
        dail_position = dail_position - rotation
    else:
        print("How?")

    if dail_position > 99:
        dail_position = dail_position - 100
        num_zeros = num_zeros + 1
    elif dail_position < 0:
        dail_position = dail_position + 100
        if prev_position != 0: # because the 0 was counted last turn
            num_zeros = num_zeros + 1
    elif dail_position == 0:
        num_zeros = num_zeros + 1


    prev_position = dail_position
    print(f"Zeros:{num_zeros}, Position:{dail_position}")