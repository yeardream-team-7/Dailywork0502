class MtInput:
    def mt_input():
        while True:
            print("ex) 4/keep or 100/change")
            input_data = input("Enter the count and target: ")
            input_list = input_data.split('/')
            epoch = int(input_list[0])
            type = input_list[1]
