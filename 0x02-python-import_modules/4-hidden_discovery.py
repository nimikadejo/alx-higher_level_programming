#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    full_list = dir(hidden_4)
    for i in range(1, len(full_list)):
        if "__" != full_list[i][:2]:
            print("{}".format(full_list[i]))
