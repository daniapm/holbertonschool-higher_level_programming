#!/usr/bin/python3
import hidden_4


def main():
    for count in dir(hidden_4):
        if count[:2] != "__":
            print(count)

if __name__ == "__main__":
    main()
