import math
import time

def get_sun_angle(hour: int) -> float:
   
    if 6 <= hour <= 18:
        # Map hours 6–18 → 0–180 degrees
        return (hour - 6) * (180 / 12)
    else:
        # Night time
        return -1  # no sun

def track_solar_panel():
    print("🌞 Solar Panel Sun-Position Tracker Started 🌞")
    for hour in range(0, 24):
        angle = get_sun_angle(hour)
        if angle >= 0:
            print(f"Hour {hour}: Sun angle = {angle:.2f}°, Panel adjusting...")
        else:
            print(f"Hour {hour}: Night time 🌙, panel at rest")
        time.sleep(0.2)  # delay to simulate real time

if __name__ == "__main__":
    track_solar_panel()

