"""
This program is created to help perfect the timing of brewing a cup of coffee. There is a selection
of different styles to choose from that will prompt the a sequence of instructions as well as
a timer to help brew the coffee.
"""
import time
import sys


# This function welcomes the user to the app, allows them to pick which method of brewing, and thanks
# them for using the app at the end.
def main():
    print("Welcome to Brew Buddy 1.0! Brew Buddy's goal is to help you make the best "
          "cup of coffee possible.\nThere are two different methods of brewing available "
          "along with instructions on how to do each method.")

    selection = int(input("Please enter the number associated with the method you would like to use:\n"
                          "1. French Press \n2. Pour Over\nEnter Here: "))
    while True:
        if selection == 1:
            french_press()
            break
        if selection == 2:
            pour_over()
            break
        else:
            while selection not in range(1, 3):
                selection = int(input('Please enter either 1 or 2.\nEnter Here: '))

    time.sleep(5)
    print("Thank you for using Brew Buddy 1.0! We hope you enjoy your fresh cup of coffee!")


# This function gives the user equipment, ingredients, instructions, and a timer to complete the
# french press method for making coffee. It also asks the user how many cups of coffee they want using
# the amount function.
def french_press():
    print("You have selected French Press! In order to perform the French Press method, you are "
          "going to need a few items:\n1. A French Press\n2. A Kettle\n3. A Coffee Bean Grinder\n"
          "4. A Scale\n5. Coffee Beans")
    input("Press enter once you have these items. ")
    print(amount(3))
    input("Press enter when you are ready for the instructions. ")
    print('Instructions for French Press:\n1. Heat up specific water amount in Kettle to 205˚F.\n'
          '2. Weight out specific coffee bean amount on scale.\n3. Coarsely grind coffee beans '
          'in grinder.\n4. Place coffee grounds in French Press and place on top of scale.\n'
          '5. Zero out scale.\n6. Start Brew Buddy timer.\n7. Bloom coffee grounds by pouring '
          'enough water to soak the coffee beans(this is typically twice the weight of the '
          'coffee grounds).\n8. Swirl French Press and then wait 30 seconds(this should happen at '
          'the end of the first minute).\n9. Pour the remaining water into the French Press.\n10. '
          'Place French Press plunger on top of coffee grounds, then slowly push the plunger down '
          'about half an inch into the water.\n11. Wait for timer to finish, then slowly push plunger '
          'all the way down and your coffee is ready to pour and enjoy!')
    input('Press enter once you are ready to start the 4 minute timer. ')
    timer_fp(240, 60)


# This function gives the user equipment, ingredients, instructions, and a timer to complete the
# pour over method for making coffee. It also asks the user how many cups of coffee they want using
# the amount function.
def pour_over():
    print("You have selected Pour Over! In order to perform the Pour Over method, you are "
          "going to need a few items:\n1. A V-60 Dripper\n2. A Glass Coffee Server\n3. A 02W "
          "Coffee Filter\n4. A Kettle\n5. A Coffee Bean Grinder\n6. A Scale\n7. Coffee Beans")
    input("Press enter once you have these items. ")
    print(amount(2))
    input("Press enter when you are ready for the instructions. ")
    print('Instructions for Pour Over:\n1. Heat up specific water amount in Kettle to 205˚F.\n'
          '2. Weight out specific coffee bean amount on scale.\n3. Grind coffee beans to a medium '
          'fineness in grinder.\n4. Place V-60 dripper on top of glass coffee server and place both '
          'on top of the scale.\n5. Place coffee grounds in filter in V-60 dripper.\n6. Zero out '
          'scale.\n7. Start Brew Buddy timer and listen for the beeps in between each of the '
          'following steps.\n8. During the first 45 seconds, '
          'bloom coffee grounds by pouring enough water to soak the coffee beans\n   (this is typically '
          'twice the weight of the coffee grounds).\n9. Swirl V-60 dripper and wait till the 45 '
          'seconds are finished.\n10. Over the next 45 seconds, pour 60% of the total water into the '
          'V-60 dripper and swirl once.\n11. Over the next 45 seconds, pour the remaining water into '
          'the V-60 dripper and swirl once.\n12. Wait 45 seconds for the timer to finish, and then '
          'your coffee is ready to pour and enjoy!')
    input('Press enter once you are ready to start the 180 second timer. ')
    timer_po(20, 5)


# This function is used to determine the amount of water and coffee beans the user will need to make
# their desired amount of cups of coffee
def amount(max_num):
    cups = int(input("How many cups of coffee would you like to make? (Max " + str(max_num) + ")\nEnter Here: "))
    while cups not in range(1, (max_num + 1)):
        cups = int(input('Please enter a number between 1-' + str(max_num) + '.\nEnter Here: '))
    water = int(cups * 295)
    coffee_beans = int(cups * 19)
    totals = ("You will need " + str(water) + " ml of water and " + str(coffee_beans) + " grams of coffee beans.")
    return totals


# This function is a timer for the pour over method that beeps every minute for 4 minutes.
# It also lets the user know when the timer starts and ends.
def timer_fp(seconds, test_num):
    print('The 4 minute timer has begun.')
    while seconds > test_num:
        seconds -= test_num
        minutes = seconds // test_num
        time.sleep(test_num)
        print(str(minutes) + " minute(s) left.")
        beep()
    time.sleep(test_num)
    print('Timer is done!')
    beep()


# This function is a timer for the pour over method that beeps every 45 seconds for 180 seconds.
# It also lets the user know when the timer starts and ends.
def timer_po(seconds, test_num):
    print('The 180 second timer has started.')
    while seconds > test_num:
        for i in range(1, 4):
            seconds -= test_num
            time.sleep(test_num)
            print(str(45 * i) + " seconds have passed.")
            beep()
    time.sleep(test_num)
    print('Timer has ended!')
    beep()

# This function is used to create a beeping sound that will be used to alert the user
def beep():
    sys.stdout.write('\a')
    sys.stdout.flush()


if __name__ == '__main__':
    main()
