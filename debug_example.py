def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

def main():
    print(divide_numbers(10, 2))
    print(divide_numbers(5, 0))

if __name__ == "__main__":
    main()
