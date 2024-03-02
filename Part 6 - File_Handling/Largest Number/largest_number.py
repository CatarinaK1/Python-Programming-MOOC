
def largest()-> int:

    with open('numbers.txt') as numberFile:
        
        Highest = 0

        for number in numberFile:
            
            if int(number) > Highest:
                Highest = int(number)

    return Highest



    
