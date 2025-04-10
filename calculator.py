# calculator.py
def add(a, b):
    """두 숫자를 더합니다."""
    return a + b

def subtract(a, b):
    """두 숫자를 뺍니다."""
    return a - b

def multiply(a, b):
    """두 숫자를 곱합니다."""
    return a * b

# 간단한 테스트 (터미널에서 python calculator.py 실행 시)
if __name__ == "__main__":
    num1 = 5
    num2 = 3
    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")    

	
