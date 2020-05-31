from server.schedule import Schedule
import datetime


def main():
    test = Schedule("/Users/jengu/Desktop/")
    x = datetime.datetime.now()
    y = "mlem"
    z = "mmmmm"

    testlist = test.get(x)
    print(testlist)

    test.add(y, x)
    test.add(z, x)

    testlist = test.get(x)
    print(testlist)


if __name__ == "__main__":
    main()
