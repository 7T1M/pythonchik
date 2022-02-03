

def main():
    def pre_process(a):
        def dec_process(s):
            for i in range(len(s)):
                s[i] = round(s[i] - a*s[i-1], 1)
            print(s)
            return dec_process

    s = [1.2, 3.0, 0.79]

    @pre_process(a=0.93)
    def plot_signal(s):
        for sample in s:
            print(sample)


if __name__ == "__main__":
    main()
