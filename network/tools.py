import typer
import requests

from rich import print
from nslookup import Nslookup
from typing_extensions import Annotated

app = typer.Typer(rich_markup_mode="rich", help="Pack of useful tools to diagnostic network")


@app.command(rich_help_panel="Network Tools")
def nslookup(domain: Annotated[str, typer.Argument(help="domain like [green]example.com[/green]")],
             dns: Annotated[str, typer.Option(help="set custom dns server")] = "1.1.1.1",
             verbose: Annotated[bool, typer.Option(help="show more information")] = False,
             tcp: Annotated[bool, typer.Option(help="Use TCP or UDP")] = False):
    """
    used to query DNS servers to
    retrieve information about domain names, such as IP addresses
    associated with them.

    Examples: ... nslookup promethe.dev --dns 8.8.8.8 --verbose
    """

    # Initialize Nslookup
    dns_query = Nslookup()
    # Alternatively, the Nslookup constructor supports optional
    # arguments for setting custom dns servers (defaults to system DNS),
    # verbosity (default: True) and using TCP instead of UDP (default: False)
    dns_query = Nslookup(dns_servers=[dns], verbose=verbose, tcp=tcp)

    ips_record = dns_query.dns_lookup(domain)

    # create output
    print(" nslookup tools")
    print(" " + "+" * 35)

    print(" Name        :", domain)
    print(" " + "+" * 35)
    for item, record in enumerate(ips_record.answer, 1):
        print(f" Address [{item}] : {record}")


@app.command(rich_help_panel="Network Tools")
def myip():
    """
    show your public ip
    """
    ip = requests.get("https://api.ipify.org")

    # create output
    print(" myip tools")
    print(" " + "+" * 35)

    print(f" Your Public IP : {ip.text}")
