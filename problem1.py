#!python3
"""
Create a function that converts from degrees F to degrees C or
vice versa, depending on which initial unit is given
2 input parameters:
float: the number of degrees
string: the unit that you currently have: may be 'C' of 'F'

return: float the number of degrees of the other unit. Round answers to 2 decimals

Sample assertions:
assert convertTemp(10,'C') == 50
assert converTemp(32,'F') == 0
"""

def convertTemp(degrees, unit):
    if unit == "C":
        answer = degrees * (9/5) + 32
        answer = round(answer, 2)
        return answer
    elif unit == "F":
        answer = (degrees - 32) * (5/9)
        answer = round(answer, 2)
        return answer
    else:
        return "error"

def tests():
    assert convertTemp(10,'C') == 50.00
    assert convertTemp(32,'F') == 0.00
    assert convertTemp(100,'C') == 212.00
    assert convertTemp(100,'F') == 37.78
    
    


if __name__== "__main__":
    tests()