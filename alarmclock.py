import time
from datetime import datetime

print("===== ALARM CLOCK =====")

# Get alarm time from user
alarm_time = input("Enter alarm time (HH:MM:SS): ")

print("Alarm set for", alarm_time)

while True:
    # Get current time
    current_time = datetime.now().strftime("%H:%M:%S")
    print("Current Time:", current_time, end="\r")

    # Check if alarm time matches current time
    if current_time == alarm_time:
        print("\n\nWake up! Alarm Ringing!")

        # Beep sound (works on Windows)
        try:
            import winsound

            for i in range(5):
                winsound.Beep(1000, 500)

        except:
            # If winsound is not available
            print("\a" * 5)

        break

    time.sleep(1)
    