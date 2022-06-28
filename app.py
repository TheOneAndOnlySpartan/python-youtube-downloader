import PySimpleGUI as sg

starter_layout = [
    [sg.Input(key="_link_input")],
    [sg.Button("Submit", key="_link_submit")],
]

info_tab = [
    [sg.Text("Title"), sg.Text("", key="_title")],
    [sg.Text("Length"), sg.Text("", key="_length")],
    [sg.Text("Views"), sg.Text("", key="_views")],
    [sg.Text("Author"), sg.Text("", key="_author")],
    [
        sg.Text("Description"),
        sg.Multiline(
            "", key="_description", size=(40, 20), no_scrollbar=True, disabled=True
        ),
    ],
]
download_tab = [
    [
        sg.Frame(
            "Best Quality",
            [
                [
                    sg.Button("Download", key="_best_res_download_button"),
                    sg.Text("", key="_best_res_download_text"),
                    sg.Text("", key="_best_res_download_size"),
                ]
            ],
        )
    ],
    [
        sg.Frame(
            "Low Quality",
            [
                [
                    sg.Button("Download", key="_low_res_download_button"),
                    sg.Text("", key="_low_res_download_text"),
                    sg.Text("", key="_low_res_download_size"),
                ]
            ],
        )
    ],
    [
        sg.Frame(
            "Audio",
            [
                [
                    sg.Button("Download", key="_audio_download"),
                    sg.Text("", key="_audio_download_size"),
                ]
            ],
        )
    ],
    [sg.VPush()],
    [sg.Progress(100, size=(30, 20), expand_x=True, key="_download_progress_bar")],
]
layout = [
    [
        sg.TabGroup(
            [
                [
                    sg.Tab("Info", info_tab),
                    sg.Tab("Download", download_tab),
                ]
            ]
        )
    ]
]

window = sg.Window("Youtube App", starter_layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "_link_submit":
        window.close()
        window = sg.Window("Youtube App", layout)

window.close()
