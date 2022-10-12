import pyfiglet


def main():
    # increase line width to print text in one line
    text = pyfiglet.figlet_format("Jetbrains  Fleet  is  ( going to be )  AWESOME !", font="big", width=160)

    # print to STDOUT
    print(text)


if __name__ == "__main__":
    main()