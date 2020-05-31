from server.schedule import Schedule
import datetime


def main():
    test = Schedule("/Users/jengu/Desktop")
    x = datetime.datetime.now()
    print(x)
    test.get(x)


if __name__ == "__main__":
    main()
