import time
from plyer import notification


if __name__ == "__main__":
	while True:
		notification.notify(
			title = "Please take a short break",
			message = "Its good to take short breaks after 25 minutes of work (as per the Pomodoro Technique) ",
			timeout = 10
			)
		time.sleep(1500)