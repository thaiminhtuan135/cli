import socket
import os
import json
import click
from os.path import expanduser, realpath


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


def generateControllerCode(controller_name, package):
    return f"""
package {package};
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.HttpStatus;

@RestController
public class {controller_name}Controller {{

    @GetMapping("/")
    public String index() {{
        return "Hello from controller!";
    }}

    @PostMapping("/create")
    public ResponseEntity<?> post() {{
        return new ResponseEntity<>("create", HttpStatus.OK);
    }}

    @PutMapping("/update")
    public ResponseEntity<?> put() {{
        return new ResponseEntity<>("update", HttpStatus.OK);
    }}

    @DeleteMapping("")
    public ResponseEntity<?> delete() {{
        return new ResponseEntity<>("delete", HttpStatus.OK);
    }}
}}
"""


def generateRepositoryCode(entity, package):
    return f"""
package {package};
import org.springframework.stereotype.Repository;

@Repository
public interface {entity}Repository extends JpaRepository<{entity}, Long> {{

}}
"""


def generateSearchRequestCode(entity, package):
    return f"""
package {package};
import java.io.Serializable;

public class {entity}SearchRequest implements Serializable {{
    private Long id;
    private Integer integer;
    private String string;
    private Date date;
}}
"""


def generateSaveRequestCode(entity, package):
    return f"""
package {package};
import java.io.Serializable;

public class {entity}SaveRequest implements Serializable {{
    private Long id;
    private Integer integer;
    private String string;
    private Date date;
}}
"""


def generateUpdateRequestCode(entity, package):
    return f"""
package {package};
import java.io.Serializable;

public class {entity}UpdateRequest implements Serializable {{
    private Long id;
}}
"""


def generateServiceCode(entity, package):
    return f"""
package {package};    
public interface {entity}Service {{
    {entity} save({entity} entity);

    Optional<{entity}> getById(Long id);

    List<{entity}> getList();

    void delete(int id);
}}
"""


def generateServiceImplementCode(entity, package):
    entityLower = entity[0].lower() + entity[1:]
    repo = entityLower + "Repository"

    return f"""
package {package};    
@Service
public class {entity}ServiceImpl implements {entity}Service {{
    @Autowired
    private {entity}Repository {repo};
    
    @Override
    public {entity} save({entity} {entityLower}) {{
        return {repo}.save({entityLower});
    }}
}}
"""


def convertPathToPackage(path):
    base_directory = 'java'

    parts = path.split(base_directory, 1)
    package = parts[1].replace('\\', '.').replace('/', '.')

    if package.startswith('.'):
        package = package[1:]
    return package


def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
        # click.echo(f"Created directory '{click.style(path, fg='green')}'")
        print("chuanmen")


@click.command()
@click.argument('entity', type=str)
def controller(entity):
    config = {}
    project_path = os.path.join(expanduser('~'), 'Desktop', 'tool_cli')
    config_file_path = os.path.join(project_path, 'config.txt')

    try:
        with open(config_file_path, 'r') as config_file:
            for line in config_file:
                if line.strip() and "=" in line:
                    key, value = line.strip().split('=', 1)
                    config[key] = value.strip()
    except Exception as e:
        click.echo(f"An error occurred while reading the config file: {e}")

    # path
    pathController = os.path.join(expanduser('~'), config["controller"])
    pathRepository = os.path.join(expanduser('~'), config["repository"])
    pathService = os.path.join(expanduser('~'), config["service"])
    # pathServiceImpl = os.path.join(expanduser('~'), config["serviceImpl"])

    pathRequest = os.path.join(expanduser('~'), config["request"], entity.lower())
    pathResponse = os.path.join(expanduser('~'), config["response"])
    # print(pathResponse)
    # check folder
    ensure_directory(pathController)
    ensure_directory(pathRepository)
    ensure_directory(pathService)
    ensure_directory(pathRequest)
    # ensure_directory(pathResponse)
    # if not os.path.exists(pathResponse):
    #     os.makedirs(pathResponse, exist_ok=True)
    #     # click.echo(f"Created directory '{click.style(path, fg='green')}'")
    #     print("chuanmen")
    # else:
    #     print("hoho")


    # ensure_directory(pathServiceImpl)
    # file path
    filePathController = os.path.join(pathController, entity + "Controller.java")
    filePathRepository = os.path.join(pathRepository, entity + "Repository.java")
    filePathService = os.path.join(pathService, entity + "Service.java")
    # filePathServiceImpl = os.path.join(pathServiceImpl, entity + "ServiceImpl.java")

    filePathSaveRequest = os.path.join(pathRequest, entity + "SaveRequest.java")
    filePathUpdateRequest = os.path.join(pathRequest, entity + "UpdateRequest.java")
    filePathSearchRequest = os.path.join(pathRequest, entity + "SearchRequest.java")

    # code
    controllerCode = generateControllerCode(entity, convertPathToPackage(pathController))
    repositoryCode = generateRepositoryCode(entity, convertPathToPackage(pathRepository))
    serviceCode = generateServiceCode(entity, convertPathToPackage(pathService))
    # serviceImplCode = generateServiceImplementCode(entity, convertPathToPackage(pathServiceImpl))

    saveRequestCode = generateSaveRequestCode(entity, convertPathToPackage(pathRequest))
    updateRequestCode = generateUpdateRequestCode(entity, convertPathToPackage(pathRequest))
    searchRequestCode = generateSearchRequestCode(entity, convertPathToPackage(pathRequest))

    try:
        # Ensure directories exist

        # controller
        with open(filePathController, "w") as file:
            file.write(controllerCode)
            click.echo(f"Controller service '{click.style(filePathController, fg='green')}' created successfully.")
        # repository
        with open(filePathRepository, "w") as file:
            file.write(repositoryCode)
            click.echo(f"Repository '{click.style(filePathRepository, fg='green')}' created successfully.")
        # save request
        with open(filePathSaveRequest, "w") as file:
            file.write(saveRequestCode)
            click.echo(f"Save request '{click.style(filePathSaveRequest, fg='green')}' created successfully.")
        # update request
        with open(filePathUpdateRequest, "w") as file:
            file.write(updateRequestCode)
            click.echo(f"Update request '{click.style(filePathUpdateRequest, fg='green')}' created successfully.")
        # update request
        with open(filePathSearchRequest, "w") as file:
            file.write(searchRequestCode)
            click.echo(f"Search request '{click.style(filePathSearchRequest, fg='green')}' created successfully.")
        # service
        with open(filePathService, "w") as file:
            file.write(serviceCode)
            click.echo(f"Service '{click.style(filePathService, fg='green')}' created successfully.")
        # serviceImpl
        # with open(filePathServiceImpl, "w") as file:
        #     file.write(serviceImplCode)
        #     click.echo(f"ServiceImpl '{click.style(filePathServiceImpl, fg='green')}' created successfully.")

    except Exception as e:
        click.echo(f"An error occurred: {e}")


@click.command()
# @click.option('--config', is_flag=True, help='Open or create a config file.')
def config():
    project_path = os.path.join(expanduser('~'), 'Desktop', 'tool_cli')
    config_file_path = os.path.join(project_path, 'config.txt')

    # if not os.path.exists(config_file_path):
    #     try:
    #         default_config = {
    #             "controller": "",
    #             "repository": "",
    #             "service": "",
    #             "serviceImpl": "",
    #             "request": "",
    #             "response": "",
    #             "dto": "",
    #         }
    #         with open(config_file_path, 'w') as config_file:
    #             json.dump(default_config, config_file, indent=4)
    #         click.echo(f"Created '{config_file_path}' successfully.")
    #     except Exception as e:
    #         click.echo(f"An error occurred: {e}")
    #         return
    if not os.path.exists(config_file_path):
        try:
            default_config = [
                "controller=",
                "repository=",
                "service=",
                "serviceImpl=",
                "request=",
                "response=",
                "dto=",
            ]
            with open(config_file_path, 'w') as config_file:
                config_file.write("\n".join(default_config))
            click.echo(f"Created '{config_file_path}' successfully.")
        except Exception as e:
            click.echo(f"An error occurred: {e}")
            return

    try:
        os.system(f'start {config_file_path}')
    except Exception as e:
        click.echo(f"An error occurred while opening the file: {e}")


@click.group()
def cli():
    pass


cli.add_command(configure)
cli.add_command(scan)
cli.add_command(controller)
cli.add_command(config)
