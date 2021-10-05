import distutils
def main():
    from distutils import util
    def parrot_trouble(talking,hour):
        if (talking and (hour < 7 or hour > 20)):
            return True
        else:
            return False

    userInHour = int(input("hour: "))
    userInTalk = bool(distutils.util.strtobool(input("Talking: ")))

    print(parrot_trouble(userInHour,userInTalk))


if __name__ == "__main__":
    main()
