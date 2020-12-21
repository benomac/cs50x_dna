from sys import argv
import string

def main():
    if len(argv) != 3:
        print('INCORRECT NUMBER OF AGUMENTS, THERE SHOULD BE 2!')
        return 1
    else:
    # Opens the .csv file and saves the data to variable csv_data
        
        with open(argv[1]) as file:
            csv_data = file.read()
        
    # Creats a list of the csv data  
        csv_data_list = csv_tablefy(csv_data)
        
    # List with only the dna sequences we're looking for
        
        check_seq = csv_tablefy(csv_data)[0][1:]
        
    # Opens the .txt file and saves the data to variable txt_data
        
        with open(argv[2]) as file:
            txt_data = file.read()
    
    
    # Creats a string of the matching persons sequence amount for each sequence
        
        check_int_string = ''
        for i in check_seq:
            check_int_string += str(count_dnas(txt_data, i))
        
    # Create a list of lists for names and dna sequnece count for each person   
        data_used = data_seq(csv_data_list)
    
    
    # Checks if there is a match for the dna txt provided
        if not check_name(data_used, check_int_string):
            print('No match')
        else:
            print(check_name(data_used, check_int_string))
    
 # # functions area # #


# Checks for matche from databases to sequences

def check_name(data, n):
    string = ''
    for i in data:
        if ''.join(i[1:]) == n:
            return i[0]


# Modifys 2d lists

def data_seq(tab):
    tab_0_cpy = []
    for i in tab:
        tab_0_cpy.append(i)
    tab_0_cpy[0] = tab[1][0:]
    return tab_0_cpy   
    
# Creats 2d lists


def csv_tablefy(n):
    csv_data_split = n.split()
    csv_2d = []
    for i in csv_data_split:
        csv_2d.append(i.split(','))
    return csv_2d

# returns a list of the matching numbers from txt

def count_dnas(txt, seq):
    times = 1
    biggest = 0
    yes = True
    
    while yes:
        if seq * times in txt:
            biggest = times
            times += 1
        else:
            yes = False
    return biggest


main()
