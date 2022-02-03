def non_empty(func):
    def decorate_list():
        tempList = [elem for elem in func() if elem != '' and elem != "None"]
        print(tempList)
    return decorate_list()


def main():
    @non_empty
    def get_pages():
        return ['chapter1', '', 'contents', 'None', 'line1']

if __name__ == "__main__":
    main()

