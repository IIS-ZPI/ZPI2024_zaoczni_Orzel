class ArithmeticAdd:
    def Addition(self, A: float, B: float) -> float:
        return A + B
class ArithmeticsDivImpl:
    def Division(self, A: float, B: float) -> float:
        try:
            return A / B
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            return float('inf')

if __name__ == "__main__":
    print("ORZEL_1 devops JoOhStud")
    print("BartStud")
    print("Dutchu")
    print("pterq")
    print("Sebastian Frączak")

    # Example usage
    A = 10
    B = 5

    adder = ArithmeticAdd()
    diviser = ArithmeticsDivImpl()

    print("")
    print(f"Arithmetic operations for A={A}, B={B}")
    print(f"A + B: {adder.Addition(A, B)}")
    print(f"A / B: {diviser.Division(A, B)}")