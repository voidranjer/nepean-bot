import tkinter as tk
from main import auto_book

seed = "https://reservation.frontdesksuite.ca/rcfs/nepeansportsplex/Home/Index?Culture=en&PageId=b0d362a1-ba36-42ae-b1e0-feefaf43fe4c&ShouldStartReserveTimeFlow=False&ButtonId=00000000-0000-0000-0000-000000000000"


def submit_form():
    submit_button.config(text="Stop")
    status_bar.config(text="Running", fg="orange")
    root.update()

    court_name = court_entry.get()
    time_aria = time_entry.get()
    telephone = phone_entry.get()
    email = email_entry.get()
    name = name_entry.get()
    is_test_run = test_run_var.get()

    res = auto_book(seed, court_name, time_aria,
                    telephone, email, name, is_test_run)

    submit_button.config(text="Start")
    status_bar.config(text="Failed", fg="red")

    if (res):
        status_bar.config(text="Completed", fg="green")

    root.update()


# Create the main window
root = tk.Tk()
root.title("Nepean Bookinator 3000")

# Create the form fields
court_label = tk.Label(root, text="Court")
court_label.pack()
court_entry = tk.Entry(root, width=30, justify="center")
court_entry.insert(0, "Badminton")
court_entry.pack()

time_label = tk.Label(root, text="Time")
time_label.pack()
time_entry = tk.Entry(root, width=30, justify="center")
time_entry.insert(0, "6:30 PM Friday February 17, 2023")
time_entry.pack()

phone_label = tk.Label(root, text="Phone Number")
phone_label.pack()
phone_entry = tk.Entry(root, width=30, justify="center")
# phone_entry.insert(0, "6138029384")
phone_entry.pack()

email_label = tk.Label(root, text="Email")
email_label.pack()
email_entry = tk.Entry(root, width=30, justify="center")
# email_entry.insert(0, "contact@jamesyap.org")
email_entry.pack()

name_label = tk.Label(root, text="Name")
name_label.pack()
name_entry = tk.Entry(root, width=30, justify="center")
# name_entry.insert(0, "James")
name_entry.pack()

test_run_var = tk.BooleanVar()
test_run_checkbox = tk.Checkbutton(
    root, text="Test Run", variable=test_run_var)
test_run_checkbox.pack()

submit_button = tk.Button(root, text="Start", command=submit_form)
submit_button.pack()

status_bar = tk.Label(root, text="Ready", fg="gray")
status_bar.pack()

footer = tk.Label(root, text="contact@jamesyap.org", fg="lightblue")
footer.pack()


root.mainloop()
