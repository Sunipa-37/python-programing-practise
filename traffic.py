# Smart Traffic Signal Decision System

def smart_traffic_signal():
    # Taking inputs from user
    emergency = input("Is there an emergency vehicle nearby? (yes/no): ").strip().lower()
    pedestrian = input("Are pedestrians currently crossing? (yes/no): ").strip().lower()
    green_light = input("Is the traffic light green? (yes/no): ").strip().lower()
    heavy_rain = input("Is it raining heavily? (yes/no): ").strip().lower()
    accident = input("Is there an accident reported ahead? (yes/no): ").strip().lower()
    school_zone = input("Is this a school zone? (yes/no): ").strip().lower()
    rush_hour = input("Is it rush hour? (yes/no): ").strip().lower()

    print("\nOutput:")

    # Decision Rules (in strict priority order)

    # 1. Emergency Override
    if emergency == "yes":
        print("All Traffic Stop: Emergency Vehicle Passing.")
    
    # 2. Pedestrian Safety
    elif pedestrian == "yes":
        print("Stop: Pedestrians Crossing.")

    # 3. Accident Zone
    elif accident == "yes":
        print("Caution: Accident Ahead. Proceed Slowly.")

    # 4. Heavy Rain Condition
    elif heavy_rain == "yes":
        if green_light == "yes":
            print("Proceed Slowly - Wet Roads.")
        else:
            print("Wait for Green - Visibility Low.")

    # 5. School Zone Priority
    elif school_zone == "yes":
        if rush_hour == "yes":
            print("Extra Caution: School Zone during Rush Hour.")
        else:
            print("Drive Carefully - School Zone.")

    # 6. Normal Condition
    else:
        if green_light == "yes":
            print("You may go.")
        else:
            print("Stop and wait for green.")

# Run the system
smart_traffic_signal()
