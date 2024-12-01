def main():
    with open("input.txt") as f:
        file_contents = f.read()
        #print(f"input.txt: {file_contents}")
        left_list = sorted(list(map(int, file_contents.split()[0::2])))
        right_list = sorted(list(map(int, file_contents.split()[1::2])))
        zipped_list = tuple(zip(left_list, right_list))
        new_list = []
        for pair in zipped_list:
            left = (pair[0])
            right = (pair[1])
            if left > right:
                new_list.append(left - right)
            elif left < right:
                new_list.append(right - left)


        both_list_occurrence = []        
        for number in left_list:
            occurrences = right_list.count(number)
            similarity_score = number * occurrences
            both_list_occurrence.append(similarity_score)
            

        print(f"total distance: {sum(new_list)}")
        print(f"final similarity score: {sum(both_list_occurrence)}")

        


if __name__ == "__main__":
    main()
