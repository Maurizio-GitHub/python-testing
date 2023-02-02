def even_number_of_evens(numbers):
    """
    If a list in not passed into the function, it will raise a TypeError.
    Error message: "A list was not passed into the function".

    If the list is empty, it will return False;
    If the number of even numbers is odd, it will return False;
    If the numner of even numbers is even, it will return True.

    The commented-out code represents the first version of the function,
    the version built during the Test-Driven Development (TDD).

    The final version of the code is the refactored one, below:
    """

    # if isinstance(numbers, list):
    #     if numbers == []:
    #         return False
    #     else:
    #         evens = 0

    #     for n in numbers:
    #         if n % 2 == 0:
    #             evens += 1

    #     if evens:
    #         return evens % 2 == 0
    #     else:
    #         return False
    # else:
    #     raise TypeError("A list was not passed into the function")

    # return None

    if isinstance(numbers, list):
        evens = sum([1 for n in numbers if n % 2 == 0])

        return True if evens and evens % 2 == 0 else False

    else:
        raise TypeError("A list was not passed into the function")

    return None


# When Python runs a file directly, it names it __main__ and any code beneath
# the if statement will only be run if the name of the file is __main__.
# So, when we run the test file, it will have the name __main__ and this code
# will not run. However, when we run this file, it will have the name __main__
# and it will run this code:
if __name__ == "__main__":
    print(even_number_of_evens(5))
