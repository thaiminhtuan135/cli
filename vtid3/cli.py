import socket
import os
import pyautogui
import imaplib
import email
import email
from email.header import decode_header
import click
from os.path import expanduser, realpath


@click.group()
def cli():
    pass


# @click.command()
# def configure():
#     file_path = 'C:\\Users\\ADMIN\\Desktop\\cli\\hihi.txt'
#
#     try:
#         with open(file_path, 'r') as file:
#             content = file.read()
#             print(content)
#     except FileNotFoundError:
#         print(f"File '{file_path}' not found.")


@click.command()
@click.argument('controller_name', type=str)
def controller(controller_name):
    controller_code = f"""
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class {controller_name}Controller {{

    @GetMapping("/")
    public String index() {{
        return "Hello from controller!";
    }}
    
    @PostMapping("")
    public void post() {{
        return "Hello from controller!";
    }}
}}
"""

    controller_directory_name = 'Controller'
    if not os.path.exists(controller_directory_name):
        os.makedirs(controller_directory_name)

    controller_path = os.path.join(os.getcwd(), controller_directory_name)

    current_directory = os.path.join(controller_path, controller_name + "Controller.java")

    # click.echo(current_directory)
    try:
        with open(current_directory, "w") as file:
            file.write(controller_code)
        click.echo(f"Controller service '{current_directory}' created successfully.")
    except Exception as e:
        click.echo(f"An error occurred: {e}")


@click.command()
@click.option('--hello', help='Print a greeting message.', required=True)
@click.option('--document-name', help='Name of the document.')
@click.option('--document-version', help='Version of the document.')
def devops(hello, document_name, document_version):
    click.echo(f'Hello {hello}!')
    if document_name:
        click.echo(f'Hello {document_name}!')
    if document_version:
        click.echo(f'Hello {document_version}!')


@click.command()
@click.option('--make-controller', help='Name of controller.')
def dev(make_controller):
    controller_code = f"""
    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.RestController;

    @RestController
    public class {make_controller}Controller {{

        @GetMapping("/")
        public String index() {{
            return "Get!";
        }}

        @PostMapping("")
        public void post() {{
            return "Post!";
        }}
    }}
    """

    controller_path = os.path.join(os.getcwd(), "Controller")

    if not os.path.exists(controller_path):
        os.makedirs(controller_path)

    current_directory = os.path.join(controller_path, make_controller + "Controller.java")

    # click.echo(current_directory)
    try:
        with open(current_directory, "w") as file:
            file.write(controller_code)
        click.echo(f"Controller service '{current_directory}' created successfully.")
    except Exception as e:
        click.echo(f"An error occurred: {e}")


@click.command()
def whizlabs():
    # 1226 471
    pyautogui.press('win')
    pyautogui.sleep(0.5)
    pyautogui.write('chrome')
    pyautogui.press('enter')
    pyautogui.sleep(0.5)
    pyautogui.click(1226, 471)

    pyautogui.sleep(0.5)
    pyautogui.write('whizlabs.com')
    pyautogui.press('enter')


def decode_subject(subject):
    decoded_subject = ""
    for part, encoding in decode_header(subject):
        if encoding:
            decoded_subject += part.decode(encoding)
        else:
            decoded_subject += part
    return decoded_subject


@click.command()
def readmail():
    # 1226 471

    GMAIL_USERNAME = 'tuan.thaiminh@vti.com.vn'
    GMAIL_PASSWORD = 'azin nwbg zcdt gqie'

    imap_server = imaplib.IMAP4_SSL(host="imap.gmail.com")
    imap_server.login(GMAIL_USERNAME, GMAIL_PASSWORD)
    imap_server.select()
    # Tìm kiếm email chưa đọc
    # result, data = imap_server.search(None, "(UNSEEN)")
    result, data = imap_server.search(None, "(SEEN)")
    # Lấy 10 email đầu tiên
    email_ids = data[0].split()[-10:]
    # email_ids = data[0].split()
    emails = []
    print(email_ids)
    # Find all emails in inbox
    for email_id in email_ids:
        result, data = imap_server.fetch(email_id, "(RFC822)")
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)
        subject = msg["subject"]
        print(decode_subject(subject))




cli.add_command(controller)
cli.add_command(devops)
cli.add_command(whizlabs)
cli.add_command(dev)
cli.add_command(readmail)
