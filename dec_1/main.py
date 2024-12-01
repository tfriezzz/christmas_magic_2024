def main():
    with open("input.txt") as f:
        file_contents = f.read()
        #print(f"input.txt: {file_contents}")
        left_list = sorted(list(map(int, file_contents.split()[0::2])))
        #left_list = sorted(left_list)
        right_list = sorted(list(map(int, file_contents.split()[1::2])))
        zipped_list = tuple(zip(left_list, right_list))
        print(f"test: {zipped_list}")
        """for pair in zipped_list:
            left = int(pair[0])
            right = int(pair[1])
            sum = int(pair[0]) - int(pair[1])
            print(f"{left} - {right} = {sum}")"""

        


if __name__ == "__main__":
    main()
