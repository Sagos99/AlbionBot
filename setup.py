from cx_Freeze import setup, Executable

base = None

executables = [Executable("AutoFish.py", base=base)]

packages = ["idna","time","pyautogui"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "AutoFish",
    options = options,
    version = "1.1",
    description = 'Pesquinha da boa',
    executables = executables
)
