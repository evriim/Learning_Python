#Receiving data from the user and reporting whether it is valid or not
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#Checking all cases for license plate validity
def is_valid(plate):
    num=0
    if 2 <= len(plate) <= 6 and plate.isalnum():
            if len(plate) == 2 and plate.isalpha():
                 return True
            elif plate[0].isalpha() and plate[1].isalpha():
                 for i in plate:
                      if i.isdigit():
                            num+=1
                 if num == 1 and plate[-1].isdigit() and plate[-1] != '0':
                      return True
                 elif num == 2 and plate[-2].isdigit() and plate[-2] != '0':
                        return True
                 elif num == 3 and plate[-3].isdigit() and plate[-3] != '0':
                        return True                 
                 elif num == 4 and plate[-4].isdigit() and plate[-4] != '0':
                        return True                                                             
    else:
        return False 
    
    


main()