import PySimpleGUI as sg
import pytube

def progress_check(stream, chunk, bytes_remaining):
    window['_download_progress_bar'].update(100 - (bytes_remaining / stream.filesize * 100))
def complete_check(stream, file_path):
    window['_download_progress_bar'].update(0)

# fmt: off
info_tab = [
    [sg.Text('Title'), sg.Text('', key='_title')],
    [sg.Text('Length'), sg.Text('', key='_length')],
    [sg.Text('Views'), sg.Text('', key='_views')],
    [sg.Text('Author'), sg.Text('', key='_author')],
    [
        sg.Text('Description'),
        sg.Multiline('', key='_description', size=(40, 20), no_scrollbar=True, disabled=True
    )],
]
download_tab = [
    [sg.Frame('Best Quality',
        [[
            sg.Button('Download', key='_best_res_download_button'),
            sg.Text('', key='_best_res_download_text'),
            sg.Text('', key='_best_res_download_size'),
        ]],
    )],
    [sg.Frame('Low Quality',
        [[
            sg.Button('Download', key='_low_res_download_button'),
            sg.Text('', key='_low_res_download_text'),
            sg.Text('', key='_low_res_download_size'),
        ]],
    )],
    [sg.Frame('Audio',
        [[
            sg.Button('Download', key='_audio_download'),
            sg.Text('', key='_audio_download_size'),
        ]],
    )],
    
    [sg.VPush()],
    [sg.Progress(100, size=(30, 20), expand_x=True, key='_download_progress_bar')],
]
layout = [[sg.TabGroup(
    [[
        sg.Tab('Info', info_tab),
        sg.Tab('Download', download_tab),
    ]]
)]]
link_window = [
    [sg.Input(key="_link_input")],
    [sg.Button("Submit", key="_link_submit")],
]
# fmt: on

window = sg.Window("Youtube App", link_window)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "_link_submit":
        window.close()
        _yt_object: pytube.YouTube = pytube.YouTube(
            values["_link_input"],
            on_progress_callback=progress_check,
            on_complete_callback=complete_check,
        )

        # video info
        window = sg.Window("Youtube App", layout, finalize=True)
        window["_title"].update(_yt_object.title)
        window["_author"].update(_yt_object.author)
        window["_description"].update(_yt_object.description)
        window["_length"].update(f"{round(_yt_object.length/60)} minutes")
        window["_views"].update(_yt_object.views)

        # video download
        window["_best_res_download_size"].update(
            f"{round(_yt_object.streams.get_highest_resolution().filesize/1048576, 1)} MiB"
        )
        window["_best_res_download_text"].update(
            _yt_object.streams.get_highest_resolution().resolution
        )

        window["_low_res_download_size"].update(
            f"{round(_yt_object.streams.get_lowest_resolution().filesize/1048576, 1)} MiB"
        )
        window["_low_res_download_text"].update(
            _yt_object.streams.get_lowest_resolution().resolution
        )

        window["_audio_download_size"].update(
            f"{round(_yt_object.streams.get_audio_only().filesize/1048576, 1)} MiB"
        )
    
    # fmt: off
    if event == '_best_res_download_button':
        _yt_object.streams.get_highest_resolution().download(
            filename=_yt_object.title.lower()
            .replace(" ", "_")
            .replace("\"", "_")
            .replace(":"," ")+"_"+_yt_object.streams.get_highest_resolution().resolution+".mp4"
        )
    if event == '_low_res_download_button':
        _yt_object.streams.get_lowest_resolution().download(
            filename=_yt_object.title.lower()
            .replace(" ", "_")
            .replace("\"", "_")
            .replace(":"," ")+"_"+_yt_object.streams.get_lowest_resolution().resolution+".mp4"
        )
    if event == '_audio_download':
        _yt_object.streams.get_audio_only().download(
            filename=_yt_object.title.lower()
            .replace(" ", "_")
            .replace("\"", "_")
            .replace(":"," ")+"_"+"audio.mp3"
        )
    # fmt: on
    
window.close()
