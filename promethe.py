import typer
from rich import print
from network import tools

logo = """
   )
  ((\  
  ===        ___ ___                     __  __              
 /_|_\     ---- / _ \_______  __ _  ___ / /_/ /  ___ 
   |     ----- / ___/ __/ _ \/  ' \/ -_) __/ _ \/ -_)
  \|/  _______/_/  /_/  \___/_/_/_/\__/\__/_//_/\__/

   .── ── ── ── ── ── ── ── ── ── ── ── ── ── ──.
   |                                            |
   |    Prometheus ...                          |
   |    As your breed, we are bound to fall     |
   |    But our light will scare the darkness   |
   |                                            |
   |                         --- Septicflesh    |
   |                                            |
   '── ── ── ── ── ── ── ── ── ── ── ── ── ── ──'
"""

app = typer.Typer(rich_markup_mode="rich", help="[bold bright_white]Desceription [bright_white]: [grey66]promethe is a "
                                                "set of tools & an assistant for every Back-End developers.")


def show_logo():
    """
    project logo
    """
    print(f"[bright_red]{logo}")


@app.command()
def info():
    """
    Show some useful info about tools
    """
    print(f"[grey66] ●  [bold bright_white]create @ Mon Jul 1 2019")
    print(f"[grey66] ●  [bold bright_white]Email [bright_white]: [grey66]mehran.safaripour@gmail.com")
    print(f"[grey66] ●  [bold bright_white]Github [bright_white]: [grey66]https://github.com/abysswarrior/promethe")
    print(f"[grey66] ●  [bold bright_white]Desceription [bright_white]: [grey66]promethe is a set of tools & \n"
          f" ●  an assistant for every Back-End developers")
    print(f"[grey66] ●  ")
    print(
        f"[red] ●  [bold bright_green]:boom: NOTE[bright_green]: [grey66]to see a list of tools and commands type [white]--help\n\n")


app.add_typer(tools.app, name="network", rich_help_panel="Network Tools")

if __name__ == "__main__":
    show_logo()
    app()
