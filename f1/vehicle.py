vehicles = ["car", "mc", "bike", "scooter", "atv", "truck"]


def determine_vehicle(num_wheels, has_motor):

    if not has_motor and num_wheel == 2:
        return ["bike"]

    if has_motor and num_wheel == 2:
        return ["mc", "scooter"]

    if has_motor and num_wheel == 4:
        return ["car", "atv"]

    if has_motor and num_wheel > 4:
        return ["truck"]


num_wheel = input("Antal hjul:")
has_motor = input("Har den motor? (j for ja, eller nej)")
num_wheel = int(num_wheel)
has_motor = has_motor.lower() == "j"

vehicle = determine_vehicle(num_wheel, has_motor)
print("Possibilities: ", " ".join(vehicle))
