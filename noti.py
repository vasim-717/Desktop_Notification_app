from plyer import notification
import time


# specify the parameters\
def msg():
    while(1):
        print("\n----------- ADD NEW NOTIFICATION -------------\n")
        title = input("Enter Your Msg titel :-")
        message = input("Enter Your Msg :- ")
        t = int(input("Enter Yor Notification time (in minute) :- "))
        print(
            f"\n----------- WAIT {t} MINUTE FOR NOTIFICATION -------------\n")

        time.sleep(t*60)
        notification.notify(title=title,
                            message=message,
                            app_icon=None,
                            timeout=10,
                            toast=False)


if __name__ == '__main__':
    msg()
