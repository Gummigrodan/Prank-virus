from cx_Freeze import setup, Executable

setup(
    name="MyApp",
    version="1.0",
    description="Tkinter + VLC App",
    executables=[Executable("main.py", base="Win32GUI")],  # ← viktig bit
    options={
        "build_exe": {
            "include_files": ["fish.mp4"],  # inkludera videon
        }
    }
)