import tkinter as tk
from tkinter import filedialog
from mashup import create_mashup
from file_operations import load_files
from pydub import AudioSegment

def browse_files(entry):
    filepath = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    entry.delete(0, tk.END)
    entry.insert(0, filepath)

def combine_files():
    filepaths = [entry.get() for entry in file_entries if entry.get()]
    audio_files = load_files(filepaths)
    timestamp_ranges = [
        (
            int(start_min.get() or 0) * 60 + int(start_sec.get() or 0),
            (int(end_min.get() or 0) * 60 + int(end_sec.get() or 0)) or None,
        )
        for (start_min, start_sec, end_min, end_sec) in timestamp_entries
    ]
    output_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])

    output_file = create_mashup(audio_files, timestamp_ranges)
    output_file.export(output_path, format="mp3")

root = tk.Tk()
root.title("MP3 File Mashup")

file_entries = []
timestamp_entries = []

for i in range(10):
    browse_button = tk.Button(root, text="Browse MP3 file", command=lambda i=i: browse_files(file_entries[i]))
    browse_button.grid(row=i, column=0, padx=10, pady=10)

    file_entry = tk.Entry(root, width=50)
    file_entry.grid(row=i, column=1, padx=10, pady=10)
    file_entries.append(file_entry)

    start_min_label = tk.Label(root, text="Start minutes:")
    start_min_label.grid(row=i, column=2, padx=10, pady=10)

    start_min = tk.Entry(root, width=10)
    start_min.grid(row=i, column=3, padx=10, pady=10)

    start_sec_label = tk.Label(root, text="Start seconds:")
    start_sec_label.grid(row=i, column=4, padx=10, pady=10)

    start_sec = tk.Entry(root, width=10)
    start_sec.grid(row=i, column=5, padx=10, pady=10)

    end_min_label = tk.Label(root, text="End minutes:")
    end_min_label.grid(row=i, column=6, padx=10, pady=10)

    end_min = tk.Entry(root, width=10)
    end_min.grid(row=i, column=7, padx=10, pady=10)

    end_sec_label = tk.Label(root, text="End seconds:")
    end_sec_label.grid(row=i, column=8, padx=10, pady=10)

    end_sec = tk.Entry(root, width=10)
    end_sec.grid(row=i, column=9, padx=10, pady=10)

    timestamp_entries.append((start_min, start_sec, end_min, end_sec))

combine_button = tk.Button(root, text="Combine MP3 files", command=combine_files)
combine_button.grid(row=10, columnspan=10, padx=10, pady=10)

root.mainloop()
