from aircraft import Aircraft
def main():
    model = input()
    plane = Aircraft(model)

    while True:
        command = input().strip()
        if command == "X":
            break 

        parts = command.split()

        if len(parts) != 2:
            continue

        action = parts[0]

        try:
            feet = int(parts[1])
        except:
            continue

        if action == "A":
            plane.ascent(feet)
        elif action == "D":
            plane.descent(feet)

    print(f"Final altitude: {plane.altitude} feet")

if __name__ == "__main__":
    main()

