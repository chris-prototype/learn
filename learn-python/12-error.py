'''

BaseException
├── SystemExit          (sys.exit())
├── KeyboardInterrupt   (Ctrl+C)
├── GeneratorExit
└── Exception           (almost all normal errors)
    ├── ValueError
    ├── ZeroDivisionError
    └── ...
'''

try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ValueError:
    print("That's not a valid number.")
except ZeroDivisionError:
    print("You can't divide by zero.")
except Exception as e:
    print(f"Something unexpected happened: {e}")
finally:
    print(f"always prints")