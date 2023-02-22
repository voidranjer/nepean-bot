from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import tkinter as tk
import time

seed = "https://reservation.frontdesksuite.ca/rcfs/nepeansportsplex/Home/Index?Culture=en&PageId=b0d362a1-ba36-42ae-b1e0-feefaf43fe4c&ShouldStartReserveTimeFlow=False&ButtonId=00000000-0000-0000-0000-000000000000"

# court_name = "Badminton"
# time_aria = "6:30 PM Friday February 17, 2023"
# telephone = '0123456789'
# email = 'test@gmail.com'
# name = 'James'

sleep_time = 300
retry_rate = 0.01


def auto_book(court_name, time_aria, telephone, email, name, show_browser, is_test_run):
    try:
        options = Options()
        if (not show_browser):
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)

        driver.get(seed)

        court_name_xpath = f"//div[@class='content' and text()='{court_name}']"
        driver.find_element(By.XPATH, court_name_xpath).click()

        while True:
            try:
                element = driver.find_element(By.XPATH,
                                              f"//a[@aria-label='{time_aria}']")
            except:
                print("Element not found, trying again...")
                driver.refresh()
                time.sleep(retry_rate)
                continue
            break

        driver.execute_script("arguments[0].click();", element)

        driver.find_element(By.ID, 'telephone').send_keys(telephone)
        driver.find_element(By.ID, 'email').send_keys(email)
        driver.find_element(By.XPATH,
                            "//input[starts-with(@id,'field')][@type='text']").send_keys(name)
        # driver.find_element_by_id('field5970').send_keys(name)

        driver.find_element(By.ID, 'submit-btn').click()

        if (not is_test_run):
            driver.find_element(By.ID, 'submit-btn').click()

        time.sleep(sleep_time)
        driver.quit()
        print(f"Successfully booked {court_name} at {time_aria} for {name}")
        return True
    except:
        return False


def submit_form():
    # submit_button.config(text="Stop")
    submit_button.config(text="Running...", state="disabled")
    status_bar.config(text="Attempting to book", fg="orange")
    root.update()

    court_name = court_entry.get()
    time_aria = time_entry.get()
    telephone = phone_entry.get()
    email = email_entry.get()
    name = name_entry.get()
    show_browser = show_browser_var.get()
    is_test_run = test_run_var.get()

    res = auto_book(court_name, time_aria, telephone,
                    email, name, show_browser, is_test_run)

    submit_button.config(text="Start", state="normal")
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

show_browser_var = tk.BooleanVar()
show_browser_checkbox = tk.Checkbutton(
    root, text="Show Browser", variable=show_browser_var)
show_browser_checkbox.select()
show_browser_checkbox.pack()

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
