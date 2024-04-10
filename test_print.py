
class PyramidTest:
    """Pyramid Test"""
    def __init__(self) -> None:
        pass

    def base_pyramid(self, n:int) -> int:
        num_asterix_factor:int = 2
        num_asterix:int = 0
        for i in range(1, n + 1):
            if i == 1:
                num_asterix = 1
            else:
                num_asterix = num_asterix + num_asterix_factor

        return num_asterix
        
    def pyramid(self, n:int) -> None:
        num_asterix_factor:int = 2
        num_asterix:int = 0
        max_num_asterix = self.base_pyramid(n=n)
        middle_point = int((max_num_asterix - 1) /2)
        for i in range(1, n +1):
            if i == 1:
                num_asterix = 1
            else:
                num_asterix = num_asterix + num_asterix_factor
                middle_point = middle_point - 1
            
            space_segment = " " * middle_point
            asterix_segment = "*" * num_asterix
            print(f"{space_segment}{asterix_segment}{space_segment}\n")

if __name__ == '__main__': 
    print("test\n",end="")
    pyramidTest = PyramidTest()
    pyramidTest.pyramid(n=10)
