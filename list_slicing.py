def main():

    # The list below will be used for all of the exercises below:
    names = ["Abigail", "Brenda", "Chad", "Doug", "Emma", "Francis", "George", "Harold", "Imogen”",
    "Jackie", "Kurt", "Linda"]

    # Example: print the first three names from the list
    # Answer print(names[0:3])

    # 1. Print ['Doug', 'Emma']



    # 2. Print [‘Brenda’, ‘Chad’, ‘Doug’, ‘Emma’, ‘Francis’]



    # 3. [‘Francis’, ‘George’, ‘Harold’, ‘Imogen’, ‘Jackie’, ‘Kurt’, ‘Linda’] (using two numbers in the slice)


    # 4. [‘Francis’, ‘George’, ‘Harold’, ‘Imogen’, ‘Jackie’, ‘Kurt’, ‘Linda’] (using one number in the slice)



    # 5. [‘Linda’] (using a positive number)


    # 6. [‘Linda’] (using a negative number)



    # 7. [‘Brenda’, ‘Doug’, ‘Francis’, ‘Harold’]



    # 8. [‘Abigail’, ‘Chad’, ‘Emma’, ‘George’, ‘Imogen’, ‘Kurt’]



    # 9. [‘Abigail’, ‘Chad’, ‘Emma’, ‘George’, ‘Imogen’, ‘Kurt’] (using a different way than above.
    # HINT: If you leave a slice number blank, the default is either the beginning or the end of the list,
    # depending on which side of the colon is blank.


    # 10. [‘Linda’, ‘Kurt’, ‘Jackie’]


    # 11. ['Linda', 'Kurt', 'Jackie', 'Imogen', 'Harold', 'George', 'Francis', 'Emma', 'Doug', 'Chad', 'Brenda', 'Abigail']



    # 12. ['Linda', 'Kurt', 'Jackie', 'Imogen', 'Harold', 'George', 'Francis', 'Emma', 'Doug', 'Chad', 'Brenda', 'Abigail']
    # (in a different way than 11. See hint for 9 for help.)





if __name__ == '__main__':
    main()


    def swap(list_one):
        """
        Function that swaps the first and last elements of the list, regardless of length
        :param list_one: a list of at least two elements
        :return: the same list with the first and last elements swapped
        """
        pass  # make sure to remove this line before beginning work on this function


    def rotate_left(list_one):
        """
        Given a list of ints length 3, return a list with the elements "rotated left" so [1, 2, 3] yields [2, 3, 1].
        :param list_one: A list consisting of exactly three integers
        :return: a list where all the elements have been shifted 1 place to the left
        """
        pass  # make sure to remove this line before beginning work on this function


    def max_end(list_one):
        """
        This function will find if the first or last element of an list is larger, then set all the elements
        of that list to that value.
        :param list_one: A list consisting of three elements - all integers
        :return: A list where all the elements are the larger of the first or last element of the original list
        """
        pass  # make sure to remove this line before beginning work on this function


    names = ["Abigail", "Brenda", "Chad", "Doug", "Emma", "Francis", "George", "Harold", "Imogen", "Jackie", "Kurt",
             "Linda"]

    print(names[0:3])

    print(names[3:5])
    print(names[1:6])
    print(names[5:12])
    print(names[11])
    print(names[11:0])

