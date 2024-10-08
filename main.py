# import the required libraries
import PySimpleGUI as sg
import csv

# method to verify credentials
def verify_credentials(admin_id, pin):  
  # open the file in read mode
  with open('admin_credentials.csv', 'r') as filename:
    # create dictreader object to read the data from file
    file = csv.DictReader(filename)
    # iterate over each row and append values to empty list
    for col in file:
      if col['Admin ID'] == admin_id and col['PIN'] == pin:
        return True
  return False

# method to log in 
def login_screen():
  sg.theme('DarkTeal12')   # add a touch of color
  
  layout = [
      [sg.Text('Library Management System', size=(15, 3), font=('Arial', 25), justification='center')],
      [sg.Text('Enter the Admin ID:', size=(20, 2)), sg.Input(key='admin_id', size=(10, 2), do_not_clear=True, font=('Arial', 16))],
      [sg.Text('Enter PIN:', size=(20, 2)), sg.Input(key='pin', password_char="*", size=(10, 2), do_not_clear=True, font=('Arial', 16))],
      [sg.Text('', size=(10, 2)), sg.Button('Sign in'), sg.Button('Cancel')]
  ]
  attempts = 0
  attempts_limit = 3
  # create the window
  window = sg.Window('Login', layout)
  # event Loop to process "events" and get the "values" of the inputs
  while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    if event == "Sign in":
      admin_id = values['admin_id']
      pin = values['pin']
      attempts +=1

      if attempts <=3 and verify_credentials(admin_id, pin):  
        window.close()
        main_screen(admin_id, pin)
      elif attempts > attempts_limit:
        sg.popup("Number of attempts exceeded the limit. Contact your administrator for more details.", background_color='grey', title='Error')
        window.close()
      else:
        sg.popup("Check your ID and PIN", background_color='grey', title='Error')
        window['admin_id'].update("")
        window['pin'].update("")
        window['admin_id'].Widget.focus()
  window.close()

# method to the main screen
def main_screen(admin_id, pin):
  sg.theme('DarkTeal12')   # add a touch of color
  # all the stuff inside your window.
  layout = [
      [sg.Text('Library Management System', size=(20, 2), font=('Arial', 25), justification='center')],
      [sg.Button('Add a new book', size=(20, 2)), sg.Button('View all books', size=(20, 2))],
      [sg.Button('Issue a book', size=(20, 2)), sg.Button('Return a book', size=(20, 2))],
      [sg.Text('', size=(15, 2)), sg.Button('Logout', size=(10, 2))]
  ]

  # create the Window
  window = sg.Window('Main Screen', layout)
  # event Loop to process "events" and get the "values" of the inputs
  while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
      break

    if event == "Logout":
      window.close()
      login_screen()

  # close the active window
  window.close()

# start the login process
login_screen()