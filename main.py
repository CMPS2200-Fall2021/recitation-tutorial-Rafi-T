




def sum_of_squares(a):
        mean = sum(a) / len(a)
        result = 0
        for i in a:
                result += (a[i-1] ** 2)
        return result
                
                
                
	

def test_one():
    assert sum_of_squares([1,2,3]) == 14

def test_two():
        assert sum_of_squares([0,0,0]) == 0



s
