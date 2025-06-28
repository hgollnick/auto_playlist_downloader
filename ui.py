import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText

# Create themed window
app = ttk.Window(title="YT Playlist Utility", themename="darkly", size=(900, 600))
app.place_window_center()

# Title
title = ttk.Label(app, text="YT Playlist Utility", font=("Segoe UI", 16, "bold"))
title.pack(pady=10)

# Main Frame
main_frame = ttk.Frame(app, padding=10)
main_frame.pack(fill=BOTH, expand=True)

# Playlist URL & Target Folder
url_frame = ttk.Frame(main_frame)
url_frame.pack(fill=X, pady=5)

playlist_url = ttk.Entry(url_frame, width=50)
playlist_url.insert(0, "Playlist URL")
playlist_url.pack(side=LEFT, fill=X, expand=True, padx=(0, 10))

target_folder = ttk.Entry(url_frame, width=50)
target_folder.insert(0, "Target Folder")
target_folder.pack(side=LEFT, fill=X, expand=True)

# Add Playlist Button
add_playlist_btn = ttk.Button(main_frame, text="+ Add Playlist", bootstyle=PRIMARY)
add_playlist_btn.pack(anchor=W, pady=(10, 10))

# Action Radios
ttk.Label(main_frame, text="Action", font=("Segoe UI", 10, "bold")).pack(anchor=W)

action_var = ttk.StringVar(value="download")

action_frame = ttk.Frame(main_frame)
action_frame.pack(anchor=W)

ttk.Radiobutton(action_frame, text="Download Videos", variable=action_var, value="download").pack(side=LEFT, padx=5)
ttk.Radiobutton(action_frame, text="Check for Removed Videos", variable=action_var, value="check").pack(side=LEFT, padx=5)

# Options Checkbuttons
ttk.Label(main_frame, text="Options", font=("Segoe UI", 10, "bold")).pack(anchor=W, pady=(10, 0))

options_frame = ttk.Frame(main_frame)
options_frame.pack(anchor=W)

merge_audio = ttk.BooleanVar()
auto_create = ttk.BooleanVar()
sanitize = ttk.BooleanVar()

ttk.Checkbutton(options_frame, text="Merge Audio/Video (best quality)", variable=merge_audio).pack(anchor=W)
ttk.Checkbutton(options_frame, text="Auto-create folders", variable=auto_create).pack(anchor=W)
ttk.Checkbutton(options_frame, text="Sanitize filenames", variable=sanitize).pack(anchor=W)

# Run Button
run_btn = ttk.Button(main_frame, text="Run Scripts", bootstyle=SUCCESS)
run_btn.pack(pady=10)

# Output Log
log_label = ttk.Label(main_frame, text="Output Log", font=("Segoe UI", 10, "bold"))
log_label.pack(anchor=W, pady=(5, 0))

log_output = ScrolledText(main_frame, height=10)
log_output.insert("end", "[INFO] Ready to process playlists...\n[INFO] Log will appear here...")
log_output.text.configure(state="disabled")
log_output.pack(fill=BOTH, expand=True)

# Footer
ttk.Label(app, text="YT Playlist Utility", font=("Segoe UI", 9)).pack(side="bottom", pady=5)

app.mainloop()
