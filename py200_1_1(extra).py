from py200_1_1 import Glass, GlassDefaultListArg, Node


def main():
    glass1 = Glass(200, 100)
    glass1.add_water(300)
    print(glass1)
    glass1.remove_water(700)

    print(glass1)

    glass1.add_water(100)
    print(glass1)

    glass1.remove_water(50)
    print(glass1)



if __name__  == '__main__':
    main()

