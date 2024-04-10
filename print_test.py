import math
import pathlib
import sys

class  PrintNumber:
    """Print Number"""

    def __init__(self) -> None:
        pass

    def print_multiples(self, print_array:list=[]) -> None:
        for i in print_array:
            if i % 3 == 0 and i % 5 ==0:
                print(f"{i}is multiple of 3 and 5")
            elif i % 3 == 0:
                print(f"{i} is multiple of 3")
            elif i % 5 == 0:
                print(f"{i} is multiple of 5")         
            else:
                print(f"{i} is not multiple of 3 or 5")

    def palindrome(self, str_input:str = '') -> str:
        str_input = str_input.lower().strip()

        if len(str_input) < 3:
            result = f"{str_input} lenght is less than 3"
            return result
        
        if (str_input[:1:]) != (str_input[-1::]):
            result = f"{str_input} is not palindrome, using simple check"
            return result
        
        if ( str_input == str_input[::-1] ):
            result = f"{str_input} is palindrome"
        else:
            result:str = f"{str_input} is not palindrome"
                
        return result
    
    def fibo_sum(self, int_input:int=0, is_sum:bool=False) -> int:
        # Fn = Fn − 1 + Fn − 2
        a:int = 0
        b:int = 1
        c:int = -1
        fibo_sum_val:int = 0

        if int_input < 0:
            return c
        
        if int_input == 0:
            return a
        
        if int_input == 1:
            return b
        
        for n in range(1, int_input):
            c =  a + b
            a = b
            b = c
            fibo_sum_val+=b 
        if is_sum:
            return fibo_sum_val + 1
        else:
            return b
    
    def get_parent_dir(self) -> pathlib.PosixPath:
        return pathlib.Path(__file__).parent

    def open_file(self, sub_dir:str='',file_name:str='') ->None:
        main_dir = self.get_parent_dir().absolute()
        full_file_path = pathlib.PurePath(main_dir, sub_dir, file_name)
        with open(file=full_file_path, mode='r') as test_file:
            for line in test_file:
                print(line, end='')


if __name__ == '__main__':
    #print_array = list((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))
    #print_array =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    #print(type(print_array))
    print(sys.version)
    printNumber = PrintNumber()
    #printNumber.print_multiples(print_array=print_array)

    #print(printNumber.palindrome(str_input="Hannah"))
    #print(printNumber.fibo_sum(9, is_sum=True))
    printNumber.open_file(sub_dir='data',file_name='test.csv' )

