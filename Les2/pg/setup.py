from cx_Freeze import setup, Executable

setup(
    name="Calculator",
    version="1.2",
    description="Calculator app",
    executables=[Executable("Progarm1.py", base=None)],
)

