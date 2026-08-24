import PySimpleGUI as sg

sg.Window(
  title="Hello World",
  layout=[
    [sg.Button("This is my first button!"), sg.Button("This one is disabled", disabled=True)]
    ],
  margins=(100, 50)
  ).read()