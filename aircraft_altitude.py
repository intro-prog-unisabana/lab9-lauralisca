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
        feet = int(parts[1])

        if action == "A":
            plane.ascend(feet)
        elif action == "D":
            plane.descend(feet)

    print(f"Final altitude: {plane.altitude} feet")

if __name__ == "__main__":
    main()

