from plyer import notification
import time

if __name__ == '__main__':

	deccesion = input("Enter what type of notification you want ['Drink' or 'Rest']: ")

	def ShowNotification(title, message, timeout):
		notification.notify(
			title=title,
			message=message,
			timeout=timeout
		)
		return "Successful"

	if "drink" in deccesion:

		a = True

		while a:
			titles = "Drink one glass of water"
			messages = "According to the Harvard University. A programmer should drink one glass of water in every 2 hours."
			timeouts = 10

			ShowNotification(titles, messages, timeouts)

			time.sleep((60*60)*2)


	elif "rest" in deccesion:

		a = True

		while a:
			titles = "Take rest for 10 minutes"
			messages = "According to the Harvard University. A programmer should take rest in every 1 hour."
			timeouts = 10

			ShowNotification(titles, messages, timeouts)

			time.sleep((60*60)*2)

	else:

		titles = "You haven't choosen anything"
		messages = "If you will not choose anything then this notification will came up. Please, Choose Rest or Drink."
		timeouts = 15

		ShowNotification(titles, messages, timeouts)
