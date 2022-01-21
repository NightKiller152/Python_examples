"""Testing equality"""


def test_equal(first_val, second_val):
    """

    :param first_val:
    :param second_val:
    """
    if first_val == second_val:
        print("Pass")

    else:
        print(f"Test Failed: expected {first_val} but got {second_val}")

SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
print(SORTED_FREQUENCIES[26])
