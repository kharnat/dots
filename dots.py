if __name__ == '__main__':
    char = input('Enter your characters: ')
    num_of_char = len(char)
    result = []

    for x in char:
        if len(result) == 0:
            result.append(x)
        else:
            result_copy = result.copy()
            temp_res = [z + x for z in result_copy]
            temp_res_dot = [z + '.' + x for z in result_copy]
            result = temp_res + temp_res_dot

    num_of_var = len(result)

    print('The number of possible options for ' + str(num_of_char) + ' characters is ' + str(num_of_var))
    print(result)

    set_for_chek = set(result)
    if len(result) == len(set_for_chek):
        print('Unique')
    else:
        print('Non-unique')
