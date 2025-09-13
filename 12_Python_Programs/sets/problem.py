command = "speak"

match command:
    case "run":
        print("The robot started to run 🏃‍♂️")
    case "speak" | "say_hi":  # multiple options (OR pattern)
        print("The robot said hi 🗣️")
    case code if command.isdigit():  # conditional
        print(f"The robot execute code: {code}")
    case _:  # _ is a wildcard that never fails (like default/else)
        print("Invalid command ❌")
