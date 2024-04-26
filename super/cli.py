import socket
import os

import click
from os.path import expanduser, realpath


@click.command()
def hello():
    print("Tuan dep trai")


@click.command()
def configure():
    file_path = 'C:\\Users\\ADMIN\\Desktop\\cli\\hihi.txt'

    try:
        # Mở tệp văn bản trong chế độ đọc
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")


@click.command()
@click.argument('ip_address')
@click.option('-F', '--fast', is_flag=True, help="Fast scan (scan only common ports)")
def scan(ip_address, fast):
    print("Scanning " + ip_address)
    if fast:
        common_ports = [21, 22, 23, 25, 53, 80, 443, 3306]
    else:
        # Nếu không được chọn, quét tất cả các cổng (cổng từ 1 đến 65535)
        common_ports = range(1, 65536)

    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # sock.settimeout(1)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            print(f"Port {port}: Open")
        else:
            print(f"Port {port}: Closed")
        sock.close()


@click.command()
@click.argument('controller_name', type=str)
def controller(controller_name):
    controller_code = f"""
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class {controller_name} {{

    @GetMapping("/")
    public String index() {{
        return "Hello from controller!";
    }}
}}
"""

    projectPath = os.path.join(expanduser('~'), 'Desktop', 'cli_java_test')

    file_path = os.path.join(projectPath, controller_name+".java")

    try:
        with open(file_path, "w") as file:
            file.write(controller_code)
        click.echo(f"Controller service '{file_path}' created successfully.")
    except Exception as e:
        click.echo(f"An error occurred: {e}")


@click.group()
def cli():
    pass


cli.add_command(hello)
cli.add_command(configure)
cli.add_command(scan)
cli.add_command(controller)
