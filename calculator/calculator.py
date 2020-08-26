"""
Calculator v0.4
"""
from ui_func import UiFunc
import sys

def main(user_input):
    if len(user_input) > 2:
        user_input = ''.join(user_input[1:])
    else:
        user_input = user_input[1]
    print(user_input)
    UiFunc.user_in_out(user_input)


if __name__ == "__main__":
    main(sys.argv)
