import tkinter as tk
from loader import LOADER_FRAMES


def launch_gui(target):
    root = tk.Tk()
    root.title("JARVX")
    root.geometry("700x500")
    root.configure(bg="black")

    terminal = tk.Text(
        root,
        bg="black",
        fg="lime",
        font=("Consolas", 12),
        insertbackground="lime",
        bd=0
    )

    terminal.pack(fill="both", expand=True)

    messages = [
        "[JARVX SECURITY INTELLIGENCE CORE]\n\n",
        "Initializing protocol...\n",
        "Loading network modules...\n",
        f"Target acquired: {target}\n",
        "\nScan preparation complete.\n"
    ]

    for msg in messages:
        terminal.insert(tk.END, msg)

    loader_label = tk.Label(
        root,
        text="/",
        fg="lime",
        bg="black",
        font=("Consolas", 14)
    )
    loader_label.pack()

    def animate(index=0):
        loader_label.config(text=LOADER_FRAMES[index % len(LOADER_FRAMES)])
        root.after(200, animate, index + 1)

    animate()

    root.mainloop()