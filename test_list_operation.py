class ListOperation:
    """List operation"""
    def __init__(self) -> None:
        pass

    def doubleEvenIdxOrVal(self, input_list:list=[]) -> list:
        output_list:list = input_list.copy()
        for k, i in enumerate(input_list,start=0):
            if (k%2) == 0 or (i%2)==0:
                output_list[k] = i+1
        return output_list
    
    def notInList(self, list_1:list, list_2:list) -> list:
        resulting_list:list = list()
        for i in list_1:
            if i not in list_2:
                print(i)
        resulting_list = [i for i in list_1 if i not in list_2]
        return resulting_list
    
    def tupleContiguous(self,input_list:list) -> list:
        output_list:list = list()
        input_list_sorted:list = input_list.copy()
        input_list_sorted = list(set(input_list_sorted))
        input_list_sorted.sort(reverse=False)
        contiguous_tuple:tuple = tuple()
        for k,j in enumerate(input_list_sorted,start=0):
            if k > 0:
                prev_element:object =  input_list_sorted[k-1]
                if j -1 == prev_element:
                    if prev_element not in contiguous_tuple:
                        contiguous_tuple = contiguous_tuple + (prev_element, j)
                    else:
                        contiguous_tuple = contiguous_tuple + (j,)
                else:
                    if len(contiguous_tuple) > 0:
                        output_list.append(contiguous_tuple)
                    contiguous_tuple = tuple()

        return output_list

if __name__ == '__main__':
    listOperation = ListOperation()
    output_list = listOperation.doubleEvenIdxOrVal(input_list= list((1,2,3,4,5,6,7,8,9,10)))
    print("First result:")
    print("_"*20)
    [print(1) for i in output_list]

    list_1 = list((1,2,3,4,5,6,7,8,9,10))
    list_2 = list((3,5,9))
    resulting_list = listOperation.notInList(list_1=list_1, list_2=list_2)
    print("Second result:")
    print("_"*20)
    [print(i) for i in resulting_list]
    resulting_list = listOperation.tupleContiguous(input_list=list((100, 200, 1,101, 500, 201, 1, 600, 202, 102)) )
    print("Second result:")
    print("_"*20)
    [print(i) for i in resulting_list]