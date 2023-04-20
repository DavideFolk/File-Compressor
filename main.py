import PySimpleGUI as sg
import zip_creator

label1 = sg.Text("Select file to compress: ")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")
label2 = sg.Text("Select destination Folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="blue")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, output_label]])
while True:
    event, values = window.read()
    match event:
        case "Compress":
            if values["files"] == '':
                sg.popup("Please select files first.", font=("Helvetica", 11))
            elif values["folder"] == '':
                sg.popup("Please select folder first.", font=("Helvetica", 11))
            else:
                filepaths = values["files"].split(';')
                folder = values["folder"]
                zip_creator.make_archive(filepaths, folder)
                window["output"].update(value="Compression completed!")
        case sg.WIN_CLOSED:
            break

window.close()