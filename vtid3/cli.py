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


GREEN = '\033[92m'
ENDC = '\033[0m'


@click.command()
def docker():
    # print("docker build image :  docker build -t <tag> <path> (exam : docker build -t my-html-app:v1.0 . ) ")
    """
    Docker Build Command Documentation

    This command helps you build a Docker image from a Dockerfile and context.

    Syntax:
        docker build [OPTIONS] PATH

    Options:
        -t, --tag list      Name and optionally a tag in the 'name:tag' format (default: 'latest')
                            Example: `docker build -t my-html-app:v1.0 .`

    Examples:
        docker build -t my-html-app:v1.0 .
            - Builds an image from the Dockerfile in the current directory and tags it as 'my-html-app' with version 'v1.0'.

        docker build -t my-repo/my-app:latest .
            - Builds an image and tags it under 'my-repo/my-app' with the tag 'latest'.

        docker build .
            - Builds an image from the Dockerfile in the current directory and tags it as 'latest' by default.

    Explanation of Options:
        -t, --tag
            Assigns a name and optionally a tag to the image that is built. If you do not specify a tag, Docker uses 'latest' as the default tag.
            The format for the tag is 'repository:tag'. You can use this tag to reference the image in subsequent Docker commands.

        PATH
            The path to the directory containing the Dockerfile and context for the build process. The context is the set of files in the directory specified.
            Typically, this is the current directory (denoted by '.').
    """
    print(f"{GREEN}Docker Build Image Command:{ENDC}")
    print(f"Usage: docker build -t <tag> <path>")
    print(f"Example: docker build -t my-html-app:v1.0 .")
    print("\nOptions:")
    print(f"{GREEN}-t, --tag list{ENDC}      Name and optionally a tag in the 'name:tag' format (default: 'latest')")
    print("\nExamples:")
    print(f"{GREEN}docker build -t my-html-app:v1.0 .{ENDC}")
    print(
        "    - Builds an image from the Dockerfile in the current directory and tags it as 'my-html-app' with version 'v1.0'.")
    print(f"{GREEN}docker build -t my-repo/my-app:latest{ENDC} .")
    print("    - Builds an image and tags it under 'my-repo/my-app' with the tag 'latest'.")
    print(f"{GREEN}docker build .{ENDC}")
    print("    - Builds an image from the Dockerfile in the current directory and tags it as 'latest' by default.")
    print("\nExplanation of Options:")
    print(f"{GREEN}-t, --tag{ENDC}")
    print(
        "    Assigns a name and optionally a tag to the image that is built. If you do not specify a tag, Docker uses 'latest' as the default tag.")
    print(
        "    The format for the tag is 'repository:tag'. You can use this tag to reference the image in subsequent Docker commands.")
    print(f"{GREEN}PATH{ENDC}")
    print(
        "    The path to the directory containing the Dockerfile and context for the build process. The context is the set of files in the directory specified.")
    print("    Typically, this is the current directory (denoted by '.').")

    print(f"\n{GREEN}Docker Run Container Command:{ENDC}")
    print(f"Usage: docker run [OPTIONS] IMAGE [COMMAND] [ARG...]")
    print(f"Example: docker run --name my-nginx-container -d -p 80:80 my-html-app")
    print("\nOptions:")
    print(f"{GREEN}-d, --detach{ENDC}        Run container in background and print container ID")
    print(f"{GREEN}-p, --publish list{ENDC}  Publish a container's port(s) to the host")
    print(f"{GREEN}--name string{ENDC}       Assign a name to the container")
    print(f"{GREEN}-v, --volume list{ENDC}   Bind mount a volume")
    print("\nExamples:")
    print(f"{GREEN}docker run --name my-nginx-container -d -p 80:80 my-html-app{ENDC}")
    print(
        "    - Runs a container named 'my-nginx-container' in detached mode, mapping port 80 of the host to port 80 of the container from the 'my-html-app' image.")
    print(f"{GREEN}docker run -d -p 8080:80 my-html-app{ENDC}")
    print(
        "    - Runs a container in detached mode, mapping port 8080 of the host to port 80 of the container from the 'my-html-app' image.")
    print(f"{GREEN}docker run -it my-html-app /bin/sh{ENDC}")
    print(
        "    - Runs a container in interactive mode with a TTY, using the 'my-html-app' image and starting a shell inside the container.")
    print("\nExplanation of Options:")
    print(f"{GREEN}-d, --detach{ENDC}")
    print(
        "    Run the container in the background (detached mode) and print the container ID. Useful for running long-lived applications.")
    print(f"{GREEN}-p, --publish{ENDC}")
    print(
        "    Publish a container's port(s) to the host. The format is 'host_port:container_port'. This allows access to the container services from the host machine.")
    print(f"{GREEN}--name{ENDC}")
    print(
        "    Assign a name to the container. This makes it easier to reference the container in subsequent Docker commands.")
    print(f"{GREEN}-v, --volume{ENDC}")
    print(
        "    Bind mount a volume. The format is 'host_path:container_path'. This is useful for persisting data or sharing files between the host and the container.")

@click.command()
def dockerbasic():
    """
    Displays a summary of basic Docker commands.
    """
    commands = f"""
    {GREEN}Docker CLI Commands Cheat Sheet{ENDC}

    {GREEN}1. docker build{ENDC}: Build an image from a Dockerfile.
        docker build -t <tag> <path>
            -t: Name and optionally a tag in the 'name:tag' format.
            -f: Specify a Dockerfile (default is 'PATH/Dockerfile').
            --no-cache: Do not use cache when building the image.

    {GREEN}2. docker run{ENDC}: Run a command in a new container.
        docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
            -d: Run container in background and print container ID.
            -p: Publish a container's port(s) to the host.
            --name: Assign a name to the container.
            -v: Bind mount a volume.

    {GREEN}3. docker ps{ENDC}: List running containers.
        docker ps
            -a: Show all containers (default shows just running).

    {GREEN}4. docker stop{ENDC}: Stop one or more running containers.
        docker stop <container_id|name>

    {GREEN}5. docker start{ENDC}: Start one or more stopped containers.
        docker start <container_id|name>

    {GREEN}6. docker rm{ENDC}: Remove one or more containers.
        docker rm <container_id|name>
            -f: Force the removal of a running container.

    {GREEN}7. docker rmi{ENDC}: Remove one or more images.
        docker rmi <image_id|name>

    {GREEN}8. docker images{ENDC}: List images.
        docker images
            -a: Show all images (default hides intermediate images).

    {GREEN}9. docker exec{ENDC}: Run a command in a running container.
        docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
            -it: Run in interactive mode with a TTY.

    {GREEN}10. docker logs{ENDC}: Fetch the logs of a container.
        docker logs <container_id|name>

    {GREEN}11. docker pull{ENDC}: Pull an image or a repository from a registry.
        docker pull <image_name>

    {GREEN}12. docker push{ENDC}: Push an image or a repository to a registry.
        docker push <image_name>

    {GREEN}13. docker network ls{ENDC}: List all networks.
        docker network ls

    {GREEN}14. docker volume ls{ENDC}: List all volumes.
        docker volume ls
        """
    print(commands)


cli.add_command(controller)
cli.add_command(devops)
cli.add_command(whizlabs)
cli.add_command(dev)
cli.add_command(readmail)
cli.add_command(docker)
cli.add_command(dockerbasic)
