import socket
import os
import pyautogui
import imaplib
import email
import email
from email.header import decode_header
import click


from os.path import expanduser, realpath

# config
fieldMappings = {
    'Long': 'Long',
    'Integer': 'Integer',
    'String': 'String',
    'Date': 'Date',
    'Double': 'Double'
}


def readFile(file_path):
    fieldDict = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.split(':')
            fieldDict[key.strip()] = value.strip()
    return fieldDict


# filePath = './entity.txt'
project_path = os.path.expanduser('~/.myapp/entity')
filePath = os.path.join(project_path, 'entity.txt')
fieldList = readFile(filePath)


@click.group()
def create():
    pass


# 👻👽💩🎃🤖🤖🎃😈👉
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


# @click.command()
# @click.argument('controller_name', type=str)
# def controller(controller_name):
#     controller_code = f"""
# import org.springframework.web.bind.annotation.GetMapping;
# import org.springframework.web.bind.annotation.RestController;
#
# @RestController
# public class {controller_name}Controller {{
#
#     @GetMapping("/")
#     public String index() {{
#         return "Hello from controller!";
#     }}
#
#     @PostMapping("")
#     public void post() {{
#         return "Hello from controller!";
#     }}
# }}
# """
#
#     controller_directory_name = 'Controller'
#     if not os.path.exists(controller_directory_name):
#         os.makedirs(controller_directory_name)
#
#     controller_path = os.path.join(os.getcwd(), controller_directory_name)
#
#     current_directory = os.path.join(controller_path, controller_name + "Controller.java")
#
#     # click.echo(current_directory)
#     try:
#         with open(current_directory, "w") as file:
#             file.write(controller_code)
#         click.echo(f"Controller service '{current_directory}' created successfully.")
#     except Exception as e:
#         click.echo(f"An error occurred: {e}")


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


def lowerEntity(entity):
    return entity[0].lower() + entity[1:]


def generateControllerCode(entity, package, importPathRequest, importPathResponse, importPathService):
    impPathRequest = convertPathToPackage(importPathRequest)
    impPathResponse = convertPathToPackage(importPathResponse)
    impPathService = convertPathToPackage(importPathService)
    service = lowerEntity(entity) + "Service"
    id = '{id}'
    return f"""
package {package};
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import {impPathService}.{entity}Service;
import {impPathRequest}.{entity}SearchRequest;
import {impPathRequest}.{entity}CreateRequest;
import {impPathRequest}.{entity}UpdateRequest;
import {impPathResponse}.{entity}CreateResponse;
import {impPathResponse}.{entity}UpdateResponse;
import {impPathResponse}.{entity}SearchItemResponse;

@RestController
@RequestMapping("/{lowerEntity(entity)}")
public class {entity}Controller {{
    @Autowired
    private {entity}Service {service};

    @GetMapping("/")
    public String index() {{
        return "Hello from controller!";
    }}

    @PostMapping("/list")
    public SearchResponse<{entity}SearchItemResponse> searchList(
            @RequestBody {entity}SearchRequest request) {{
        return {service}.getSearchList(request);
    }}

    @GetMapping("/{id}")
    public ResponseEntity<?> getById(@PathVariable Long id) {{
        return new ResponseEntity<>({service}.getById(id), HttpStatus.OK);
    }}

    @PostMapping("/create")
    public ResponseEntity<{entity}CreateResponse> post(@RequestBody {entity}CreateRequest request) {{
        return new ResponseEntity<>({service}.save(request), HttpStatus.OK);
    }}

    @PutMapping("/update")
    public ResponseEntity<{entity}UpdateResponse> put(@RequestBody {entity}UpdateRequest request) {{
        return new ResponseEntity<>({service}.update(request), HttpStatus.OK);
    }}

    @DeleteMapping("/{id}")
    public ResponseEntity<String> delete(@PathVariable Long id) {{
        return {service}.delete(id);
    }}
}}
"""


def generateRepositoryCode(entity, package, importEntity, importDTO):
    impPathEntity = convertPathToPackage(importEntity)
    impPathDTO = convertPathToPackage(importDTO)

    # Generate SELECT clause
    select_clause = ", ".join([f"{entity.lower()}.{field} as {field}" for field in fieldList.keys()])
    print(select_clause)
    # Generate WHERE clause
    where_clause = " AND ".join([
        # Handle `String` fields
        f"(:#{{#CONDITION.get{field.capitalize()}()}} IS NULL OR LOWER({entity.lower()}.{field}) LIKE LOWER(CONCAT('%', :#{{#CONDITION.get{field.capitalize()}()}}, '%')))"
        if fieldList[field] == 'String'
        # Handle `DATE` fields
        else f"(:#{{#CONDITION.get{field.capitalize()}()}} IS NULL OR DATE({entity.lower()}.{field}) = DATE(:#{{#CONDITION.get{field.capitalize()}()}}))"
        if fieldList[field] == 'Date'
        # Handle other types (e.g., `Integer`)
        else f"(:#{{#CONDITION.get{field.capitalize()}()}} IS NULL OR {entity.lower()}.{field} = :#{{#CONDITION.get{field.capitalize()}()}})"
        for field in fieldList.keys()
    ])

    return f"""
package {package};
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;
import org.springframework.data.jpa.repository.JpaRepository;
import {impPathEntity}.{entity}Entity;
import {impPathDTO}.SearchList{entity}DTO;
import {impPathDTO}.SearchOption{entity}DTO;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

public interface {entity}Repository extends JpaRepository<{entity}Entity, Long>,
    JpaSpecificationExecutor<{entity}Entity> {{
    
     @Query(value = "SELECT "
            + "{select_clause} "
            + "FROM {entity}Entity {lowerEntity(entity)} "
            + "WHERE {where_clause} "
            + "ORDER BY {lowerEntity(entity)}.createdAt DESC"
    )
    Page<SearchList{entity}DTO> searchList(@Param("CONDITION") SearchOption{entity}DTO options,
                                          Pageable pageRequest);
}}
"""


def generateServiceCode(entity, package, importPathRequest, importPathResponse, importPathDTO, importPathEntity):
    impPathRequest = convertPathToPackage(importPathRequest)
    impPathResponse = convertPathToPackage(importPathResponse)
    impPathDTO = convertPathToPackage(importPathDTO)
    impPathEntity = convertPathToPackage(importPathEntity)

    return f"""
package {package};    
import {impPathRequest}.{entity}SearchRequest;
import {impPathRequest}.{entity}CreateRequest;
import {impPathRequest}.{entity}UpdateRequest;
import {impPathResponse}.{entity}CreateResponse;
import {impPathResponse}.{entity}UpdateResponse;
import {impPathResponse}.{entity}DetailResponse;
import {impPathResponse}.{entity}SearchItemResponse;
import {impPathEntity}.{entity}Entity;
import {impPathDTO}.SearchList{entity}DTO;
import org.springframework.data.domain.Page;
import java.util.Optional;
import java.util.List;
import org.springframework.http.ResponseEntity;


public interface {entity}Service {{

    SearchResponse<{entity}SearchItemResponse> getSearchList({entity}SearchRequest request);
    
    {entity}CreateResponse save({entity}CreateRequest request);

    {entity}DetailResponse getById(Long id);
    
    {entity}UpdateResponse update({entity}UpdateRequest request);

    List<{entity}Entity> getList();

    ResponseEntity<String> delete(Long id);
}}
"""


def generateServiceImplementCode(entity, package, importPathRepo, importPathSerivce, importPathDTO, importPathRequest,
                                 importEntity, importResponse):
    entityLower = entity[0].lower() + entity[1:]
    repo = entityLower + "Repository"
    impPathRepository = convertPathToPackage(importPathRepo)
    impPathService = convertPathToPackage(importPathSerivce)
    impPathDTO = convertPathToPackage(importPathDTO)
    impPathRequest = convertPathToPackage(importPathRequest)
    impPathEntity = convertPathToPackage(importEntity)
    impPathResponse = convertPathToPackage(importResponse)

    # save
    entityLower = entity[0].lower() + entity[1:]
    entityInstance = entityLower

    # Generate field assignments
    fieldAssignments = []
    for field in fieldList:
        fieldAssignments.append(
            f'        {entityInstance}.set{field[0].upper() + field[1:]}(request.get{field[0].upper() + field[1:]}());')

    fieldsCode = '\n'.join(fieldAssignments)

    searchOptionsAssignments = []
    for field in fieldList:
        searchOptionsAssignments.append(
            f'              .{field[0].lower() + field[1:]}(request.get{field[0].upper() + field[1:]}())'
        )

    searchOptionsCode = '\n'.join(searchOptionsAssignments)

    return f"""package {package};    
    
import {impPathRepository}.{entity}Repository;
import {impPathService}.{entity}Service;
import {impPathEntity}.{entity}Entity;
import {impPathDTO}.SearchList{entity}DTO;
import {impPathDTO}.SearchOption{entity}DTO;
import {impPathRequest}.{entity}SearchRequest;
import {impPathRequest}.{entity}CreateRequest;
import {impPathRequest}.{entity}UpdateRequest;
import {impPathResponse}.{entity}CreateResponse;
import {impPathResponse}.{entity}UpdateResponse;
import {impPathResponse}.{entity}DetailResponse;
import {impPathResponse}.{entity}SearchItemResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.NoSuchElementException;
import java.util.List;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Page;
import java.util.stream.Collectors;

@Service
public class {entity}ServiceImpl implements {entity}Service {{
    @Autowired
    private {entity}Repository {repo};

    @Override
    public SearchResponse<{entity}SearchItemResponse> getSearchList({entity}SearchRequest request) {{
         SearchOption{entity}DTO options = SearchOption{entity}DTO.builder()
{searchOptionsCode}
              .build();
        Pageable pageRequest = request.getPageable();
        Page<SearchList{entity}DTO> page = {repo}.searchList(options,
            pageRequest);
        PaginateResponse paginate =
                PaginateResponse.builder().pageNumber(1 + page.getPageable().getPageNumber())
                        .pageSize(page.getPageable().getPageSize())
                        .totalElements(page.getTotalElements()).build();
        
        List<SearchList{entity}DTO> {lowerEntity(entity)}List = page.getContent();
        List<{entity}SearchItemResponse> itemResponses ={lowerEntity(entity)}List.stream().map({entity}SearchItemResponse::fromEntity).collect(Collectors.toList()); 
         
        return SearchResponse.createEntityResponse(paginate, itemResponses);
        
    }}

    @Override
    public {entity}CreateResponse save({entity}CreateRequest request) {{
        {entity}Entity student = new {entity}Entity();
        // TODO check duplicate
//      {entity}Entity {entityLower}Infor = {repo}.findById(request.getId())
//          .orElseThrow(() -> new CustomCommonException(ErrorConstant.MSG002, ""));
        // TODO save
{fieldsCode}
        {repo}.save(student);
        return {entity}CreateResponse.fromEntity({entityLower});
    }}

    @Override
    public {entity}UpdateResponse update({entity}UpdateRequest request) {{
        {entity}Entity {lowerEntity(entity)} = {repo}.findById(request.getId())
                    .orElseThrow(() -> new NoSuchElementException("{entity} not found with ID: " + request.getId()));
{fieldsCode}                    
        return StudentUpdateResponse.fromEntity({lowerEntity(entity)});
    }}

    @Override
    public {entity}DetailResponse getById(Long id) {{
        {entity}Entity {lowerEntity(entity)} = {repo}.findById(id)
                .orElseThrow(() -> new NoSuchElementException("{entity} not found with ID: " + id));
        return {entity}DetailResponse.fromEntity({lowerEntity(entity)});
    }}

    @Override
    public List<{entity}Entity> getList() {{
        return null;
    }}

    @Override
    public ResponseEntity<String> delete(Long id) {{
        {entity}Entity {lowerEntity(entity)} = {repo}.findById(id)
                .orElseThrow(() -> new NoSuchElementException("{entity} not found with ID: " + id));
        {repo}.deleteById(id);
        return new ResponseEntity<>("Delete successfully", HttpStatus.OK);
    }}
}}
"""


def generateCreateRequestCode(entity, package):
    fieldDefinitions = []
    importDate = False
    for fieldName, fieldType in fieldList.items():
        java_type = fieldMappings.get(fieldType, 'String')
        fieldDefinitions.append(f'    private {java_type} {fieldName};')
        if java_type == 'Date':
            importDate = True

    fields_code = '\n'.join(fieldDefinitions)
    date_import = 'import java.util.Date' if importDate else ''
    return f"""
package {package};
{date_import};
import java.io.Serializable;
import lombok.Data;

@Data
public class {entity}CreateRequest implements Serializable {{
{fields_code}
}}
"""


def generateUpdateRequestCode(entity, package):
    return f"""
package {package};
import java.io.Serializable;
import lombok.Data;

@Data
public class {entity}UpdateRequest extends {entity}CreateRequest {{
    private Long id;
}}
"""


def generateSearchListDTOCode(entity, package):
    fieldDefinitions = []
    importDate = False
    for fieldName, fieldType in fieldList.items():
        java_type = fieldMappings.get(fieldType, 'String')
        fieldDefinitions.append(f'    {java_type} get{fieldName[0].upper() + fieldName[1:]}();')
        if java_type == 'Date':
            importDate = True

    fields_code = '\n'.join(fieldDefinitions)
    date_import = 'import java.util.Date' if importDate else ''
    return f"""
package {package};    
{date_import};
public interface SearchList{entity}DTO {{
    Long getId();
{fields_code}
}}
"""


def generateSearchOptionDTOCode(entity, package):
    fieldDefinitions = []
    importDate = False
    for fieldName, fieldType in fieldList.items():
        java_type = fieldMappings.get(fieldType, 'String')
        fieldDefinitions.append(f'    private {java_type} {fieldName};')
        if java_type == 'Date':
            importDate = True

    fields_code = '\n'.join(fieldDefinitions)
    date_import = 'import java.util.Date' if importDate else ''
    return f"""
package {package};    
{date_import};
import lombok.Builder;
import lombok.Data;

@Data
@Builder
public class SearchOption{entity}DTO {{
{fields_code}
}}
"""


def generateSearchRequestCode(entity, package):
    fieldDefinitions = []
    importDate = False
    for fieldName, fieldType in fieldList.items():
        java_type = fieldMappings.get(fieldType, 'String')
        fieldDefinitions.append(f'    private {java_type} {fieldName};')
        if java_type == 'Date':
            importDate = True

    fields_code = '\n'.join(fieldDefinitions)
    date_import = 'import java.util.Date' if importDate else ''
    return f"""
package {package};
{date_import};
import java.io.Serializable;
import lombok.Data;

@Data
public class {entity}SearchRequest extends PaginateRequest {{
{fields_code}
}}
"""


def generateCreateResponseCode(entity, package, importEntity):
    impPathEntity = convertPathToPackage(importEntity)
    fieldDefinitions = []
    methodAssignments = []

    importDate = False
    for fieldName, fieldType in fieldList.items():
        java_type = fieldMappings.get(fieldType, 'String')
        fieldDefinitions.append(f'    private {java_type} {fieldName};')

        methodAssignments.append(
            f'        response.set{fieldName[0].upper() + fieldName[1:]}(entity.get{fieldName[0].upper() + fieldName[1:]}());')
        if java_type == 'Date':
            importDate = True
            # methodAssignments.append(
            #     f'        response.set{fieldName.capitalize()}(entity.get{fieldName.capitalize()}At());')

    fields_code = '\n'.join(fieldDefinitions)
    assignments_code = '\n'.join(methodAssignments)
    date_import = 'import java.util.Date' if importDate else ''

    return f"""
package {package};
{date_import};
import java.io.Serializable;
import lombok.Data;
import {impPathEntity}.{entity}Entity;

@Data
public class {entity}CreateResponse implements Serializable {{
    private Long id;
{fields_code}
    
    public static {entity}CreateResponse fromEntity({entity}Entity entity) {{
        {entity}CreateResponse response = new {entity}CreateResponse();
        response.setId(entity.getId());
{assignments_code}
        return response;
    }}
    
}}
"""


def generateUpdateResponseCode(entity, package, importEntity):
    impPathEntity = convertPathToPackage(importEntity)
    fieldDefinitions = []
    methodAssignments = []

    importDate = False
    for fieldName, fieldType in fieldList.items():
        java_type = fieldMappings.get(fieldType, 'String')
        fieldDefinitions.append(f'    private {java_type} {fieldName};')

        methodAssignments.append(
            f'        response.set{fieldName[0].upper() + fieldName[1:]}(entity.get{fieldName[0].upper() + fieldName[1:]}());')
        if java_type == 'Date':
            importDate = True
            # methodAssignments.append(
            #     f'        response.set{fieldName.capitalize()}(entity.get{fieldName.capitalize()}At());')

    fields_code = '\n'.join(fieldDefinitions)
    assignments_code = '\n'.join(methodAssignments)
    date_import = 'import java.util.Date' if importDate else ''

    return f"""
package {package};
{date_import};
import java.io.Serializable;
import lombok.Data;
import {impPathEntity}.{entity}Entity;

@Data
public class {entity}UpdateResponse implements Serializable {{
    private Long id;
{fields_code}

    public static {entity}UpdateResponse fromEntity({entity}Entity entity) {{
        {entity}UpdateResponse response = new {entity}UpdateResponse();
        response.setId(entity.getId());
{assignments_code}
        return response;
    }}

}}
"""


def generateDetailResponseCode(entity, package, importEntity):
    impPathEntity = convertPathToPackage(importEntity)
    fieldDefinitions = []
    methodAssignments = []

    importDate = False
    for fieldName, fieldType in fieldList.items():
        java_type = fieldMappings.get(fieldType, 'String')
        fieldDefinitions.append(f'    private {java_type} {fieldName};')

        methodAssignments.append(
            f'        response.set{fieldName[0].upper() + fieldName[1:]}(entity.get{fieldName[0].upper() + fieldName[1:]}());')
        if java_type == 'Date':
            importDate = True
            # methodAssignments.append(
            #     f'        response.set{fieldName.capitalize()}(entity.get{fieldName.capitalize()}At());')

    fields_code = '\n'.join(fieldDefinitions)
    assignments_code = '\n'.join(methodAssignments)
    date_import = 'import java.util.Date' if importDate else ''

    return f"""
package {package};
{date_import};
import java.io.Serializable;
import lombok.Data;
import {impPathEntity}.{entity}Entity;

@Data
public class {entity}DetailResponse implements Serializable {{
    private Long id;
{fields_code}

    public static {entity}DetailResponse fromEntity({entity}Entity entity) {{
        {entity}DetailResponse response = new {entity}DetailResponse();
        response.setId(entity.getId());
{assignments_code}
        return response;
    }}

}}
"""


def generateSearchItemResponseCode(entity, package, importEntity, importDTO):
    impPathEntity = convertPathToPackage(importEntity)
    impPathDTO = convertPathToPackage(importDTO)
    fieldDefinitions = []
    methodAssignments = []

    importDate = False
    for fieldName, fieldType in fieldList.items():
        java_type = fieldMappings.get(fieldType, 'String')
        fieldDefinitions.append(f'    private {java_type} {fieldName};')

        methodAssignments.append(
            f'        response.set{fieldName[0].upper() + fieldName[1:]}(entity.get{fieldName[0].upper() + fieldName[1:]}());')
        if java_type == 'Date':
            importDate = True
            # methodAssignments.append(
            #     f'        response.set{fieldName.capitalize()}(entity.get{fieldName.capitalize()}At());')

    fields_code = '\n'.join(fieldDefinitions)
    assignments_code = '\n'.join(methodAssignments)
    date_import = 'import java.util.Date' if importDate else ''

    return f"""
package {package};
{date_import};
import java.io.Serializable;
import lombok.Data;
import {impPathEntity}.{entity}Entity;
import {impPathDTO}.SearchList{entity}DTO;

@Data
public class {entity}SearchItemResponse implements Serializable {{
    private Long id;
{fields_code}

    public static {entity}SearchItemResponse fromEntity(SearchList{entity}DTO entity) {{
        {entity}SearchItemResponse response = new {entity}SearchItemResponse();
        response.setId(entity.getId());
{assignments_code}
        return response;
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


def checkDirectoryExist(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


@click.command()
@click.argument('entity', type=str)
@click.option('-s', '--status', is_flag=True, help="Add changeStatus method")
@click.option('-t', '--type', is_flag=True, help="Add changeType method")
def controller(entity, status, type):
    config = {}
    project_path = os.path.expanduser('~/.myapp/config')
    config_file_path = os.path.join(project_path, 'config.txt')
    try:
        with open(config_file_path, 'r') as config_file:
            for line in config_file:
                if line.strip() and "=" in line:
                    key, value = line.strip().split('=', 1)
                    config[key] = value.strip()
    except Exception as e:
        click.echo(f"An error occurred while reading the config file: {e}")

    # 😘 path
    pathController = os.path.join('.', config["controller"])
    pathRepository = os.path.join('.', config["repository"])
    pathService = os.path.join('.', config["service"])
    pathServiceImpl = os.path.join('.', config["serviceImpl"])
    pathDTO = os.path.join('.', config["dto"])
    pathEntity = os.path.join('.', config["entity"])
    #
    pathRequest = os.path.join('.', config["request"], entity.lower())
    pathResponse = os.path.join('.', config["response"], entity.lower())

    # 😘 check folder exists
    checkDirectoryExist(pathController)
    checkDirectoryExist(pathRepository)
    checkDirectoryExist(pathService)
    checkDirectoryExist(pathServiceImpl)
    checkDirectoryExist(pathDTO)
    checkDirectoryExist(pathRequest)
    checkDirectoryExist(pathResponse)

    # ensure_directory(pathServiceImpl)
    # 😘 file path
    filePathController = os.path.join(pathController, entity + "Controller.java")
    filePathRepository = os.path.join(pathRepository, entity + "Repository.java")
    filePathService = os.path.join(pathService, entity + "Service.java")
    filePathServiceImpl = os.path.join(pathServiceImpl, entity + "ServiceImpl.java")
    filePathSearchListDTO = os.path.join(pathDTO, "SearchList" + entity + "DTO.java")
    filePathSearchOptionDTO = os.path.join(pathDTO, "SearchOption" + entity + "DTO.java")
    # request
    filePathCreateRequest = os.path.join(pathRequest, entity + "CreateRequest.java")
    filePathUpdateRequest = os.path.join(pathRequest, entity + "UpdateRequest.java")
    filePathSearchRequest = os.path.join(pathRequest, entity + "SearchRequest.java")
    # response
    filePathSearchItemResponse = os.path.join(pathResponse, entity + "SearchItemResponse.java")
    filePathCreateResponse = os.path.join(pathResponse, entity + "CreateResponse.java")
    filePathUpdateResponse = os.path.join(pathResponse, entity + "UpdateResponse.java")
    filePathDetailResponse = os.path.join(pathResponse, entity + "DetailResponse.java")

    # 😘 CODE
    controllerCode = generateControllerCode(entity, convertPathToPackage(pathController), pathRequest, pathResponse,
                                            pathService)
    repositoryCode = generateRepositoryCode(entity, convertPathToPackage(pathRepository), pathEntity, pathDTO)
    serviceCode = generateServiceCode(entity, convertPathToPackage(pathService), pathRequest, pathResponse, pathDTO,
                                      pathEntity)
    serviceImplCode = generateServiceImplementCode(entity, convertPathToPackage(pathServiceImpl), pathRepository,
                                                   pathService, pathDTO, pathRequest, pathEntity, pathResponse)

    searchListDTOCode = generateSearchListDTOCode(entity, convertPathToPackage(pathDTO))
    searchOptionDTOCode = generateSearchOptionDTOCode(entity, convertPathToPackage(pathDTO))
    createRequestCode = generateCreateRequestCode(entity, convertPathToPackage(pathRequest))
    updateRequestCode = generateUpdateRequestCode(entity, convertPathToPackage(pathRequest))
    searchRequestCode = generateSearchRequestCode(entity, convertPathToPackage(pathRequest))

    searchItemResponseCode = generateSearchItemResponseCode(entity, convertPathToPackage(pathResponse), pathEntity,
                                                            pathDTO)
    createResponseCode = generateCreateResponseCode(entity, convertPathToPackage(pathResponse), pathEntity)
    updateResponseCode = generateUpdateResponseCode(entity, convertPathToPackage(pathResponse), pathEntity)
    detailResponseCode = generateDetailResponseCode(entity, convertPathToPackage(pathResponse), pathEntity)

    try:
        # controller
        with open(filePathController, "w") as file:
            file.write(controllerCode)
            click.echo(f"Controller '{click.style(filePathController, fg='green')}' created successfully.")
        # # repository
        with open(filePathRepository, "w") as file:
            file.write(repositoryCode)
            click.echo(f"Repository '{click.style(filePathRepository, fg='green')}' created successfully.")
        # # service
        with open(filePathService, "w") as file:
            file.write(serviceCode)
            click.echo(f"Service '{click.style(filePathService, fg='green')}' created successfully.")
        # serviceImpl
        with open(filePathServiceImpl, "w") as file:
            file.write(serviceImplCode)
            click.echo(f"ServiceImpl '{click.style(filePathServiceImpl, fg='green')}' created successfully.")
        # DTO
        with open(filePathSearchListDTO, "w") as file:
            file.write(searchListDTOCode)
            click.echo(f"Search list DTO '{click.style(filePathSearchListDTO, fg='green')}' created successfully.")
        # SearchOptionDTO
        with open(filePathSearchOptionDTO, "w") as file:
            file.write(searchOptionDTOCode)
            click.echo(f"Search option DTO '{click.style(filePathSearchOptionDTO, fg='green')}' created successfully.")
        # update request
        with open(filePathSearchRequest, "w") as file:
            file.write(searchRequestCode)
            click.echo(f"Search request '{click.style(filePathSearchRequest, fg='green')}' created successfully.")
        # save request
        with open(filePathCreateRequest, "w") as file:
            file.write(createRequestCode)
            click.echo(f"Create request '{click.style(filePathCreateRequest, fg='green')}' created successfully.")
        # update request
        with open(filePathUpdateRequest, "w") as file:
            file.write(updateRequestCode)
            click.echo(f"Update request '{click.style(filePathUpdateRequest, fg='green')}' created successfully.")
        # create response
        with open(filePathCreateResponse, "w") as file:
            file.write(createResponseCode)
            click.echo(f"Create response '{click.style(filePathCreateResponse, fg='green')}' created successfully.")
        # update response
        with open(filePathUpdateResponse, "w") as file:
            file.write(updateResponseCode)
            click.echo(f"Update response '{click.style(filePathUpdateResponse, fg='green')}' created successfully.")
        # detail response
        with open(filePathDetailResponse, "w") as file:
            file.write(detailResponseCode)
            click.echo(f"Detail response '{click.style(filePathDetailResponse, fg='green')}' created successfully.")
        # detail response
        with open(filePathSearchItemResponse, "w") as file:
            file.write(searchItemResponseCode)
            click.echo(
                f"Search item response '{click.style(filePathSearchItemResponse, fg='green')}' created successfully.")

    except Exception as e:
        click.echo(f"An error occurred: {e}")


@click.command()
def config():
    project_path = os.path.expanduser('~/.myapp/config')
    config_file_path = os.path.join(project_path, 'config.txt')

    if not os.path.exists(project_path):
        try:
            os.makedirs(project_path)
        except Exception as e:
            click.echo(f"An error occurred while creating directory: {e}")
            return

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
                "entity=",
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


# @click.command()
# def config():
#     project_path = os.path.join('.', 'config')
#     config_file_path = os.path.join(project_path, 'config.txt')
#
#     if not os.path.exists(project_path):
#         try:
#             os.makedirs(project_path)
#         except Exception as e:
#             click.echo(f"An error occurred while creating directory: {e}")
#             return
#     # if not os.path.exists(config_file_path):
#     #     try:
#     #         default_config = {
#     #             "controller": "",
#     #             "repository": "",
#     #             "service": "",
#     #             "serviceImpl": "",
#     #             "request": "",
#     #             "response": "",
#     #             "dto": "",
#     #         }
#     #         with open(config_file_path, 'w') as config_file:
#     #             json.dump(default_config, config_file, indent=4)
#     #         click.echo(f"Created '{config_file_path}' successfully.")
#     #     except Exception as e:
#     #         click.echo(f"An error occurred: {e}")
#     #         return
#     if not os.path.exists(config_file_path):
#         try:
#             default_config = [
#                 "controller=",
#                 "repository=",
#                 "service=",
#                 "serviceImpl=",
#                 "request=",
#                 "response=",
#                 "dto=",
#                 "entity=",
#             ]
#             with open(config_file_path, 'w') as config_file:
#                 config_file.write("\n".join(default_config))
#             click.echo(f"Created '{config_file_path}' successfully.")
#         except Exception as e:
#             click.echo(f"An error occurred: {e}")
#             return
#
#     try:
#         os.system(f'start {config_file_path}')
#     except Exception as e:
#         click.echo(f"An error occurred while opening the file: {e}")


@click.command()
def entity():
    project_path = os.path.expanduser('~/.myapp/entity')
    config_file_path = os.path.join(project_path, 'entity.txt')

    if not os.path.exists(project_path):
        try:
            os.makedirs(project_path)
        except Exception as e:
            click.echo(f"An error occurred while creating directory: {e}")
            return

    if not os.path.exists(config_file_path):
        try:
            default_config = ""
            with open(config_file_path, 'w') as config_file:
                config_file.write(default_config)
            click.echo(f"Created '{config_file_path}' successfully.")
        except Exception as e:
            click.echo(f"An error occurred: {e}")
            return

    # Mở file entity.txt sau khi tạo
    try:
        os.system(f'start {config_file_path}')
    except Exception as e:
        click.echo(f"An error occurred while opening the file: {e}")


def findFileInDirectory(directory, filename):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None


def addChangeStatusMethod(file_path):
    # Đọc nội dung file hiện tại
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        # Phương thức changeStatus cần thêm v
        changeStatusMethod = """
    @PutMapping("/changeStatus/{id}")
    public ResponseEntity<?> changeStatus(@PathVariable Long id, @RequestBody String status) {
        
        boolean success = studentService.changeStatus(id, status);
        if (success) {
            return new ResponseEntity<>(HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }
"""

        lastMethodPos = content.rfind('}')
        if lastMethodPos != -1:
            new_content = content[:lastMethodPos] + changeStatusMethod + content[lastMethodPos:]
            print(new_content)

            # with open(file_path, 'w') as file:
            # print(file)
            # file.write(new_content)
            click.echo(f"Added changeStatus method to '{file_path}'.")
        else:
            click.echo("Could not find the end of the class definition to insert the method.")


    except Exception as e:
        click.echo(f"An error occurred while adding changeStatus method: {e}")


@click.command()
@click.option('-s', '--status', is_flag=True, help="Add changeStatus method")
@click.option('-t', '--type', is_flag=True, help="Add changeType method")
@click.option('-c', '--controller', type=str, help="Specify the controller file name")
def feature(status, type, controller):
    config = {}
    projectPath = os.path.expanduser('~/.myapp/config')
    configfilePath = os.path.join(projectPath, 'config.txt')
    try:
        with open(configfilePath, 'r') as configFile:
            for line in configFile:
                if line.strip() and "=" in line:
                    key, value = line.strip().split('=', 1)
                    config[key] = value.strip()
    except Exception as e:
        click.echo(f"An error occurred while reading the config file: {e}")

    # 😘 path
    pathController = os.path.join('.', config["controller"])
    pathRepository = os.path.join('.', config["repository"])
    pathService = os.path.join('.', config["service"])
    pathServiceImpl = os.path.join('.', config["serviceImpl"])
    pathDTO = os.path.join('.', config["dto"])
    pathEntity = os.path.join('.', config["entity"])
    #
    pathRequest = os.path.join('.', config["request"])
    pathResponse = os.path.join('.', config["response"])
    print(pathController)

    filePath = findFileInDirectory(pathController, controller)

    if filePath:
        click.echo(f"File found: {filePath}")

        if status:
            addChangeStatusMethod(filePath)

        # if type:
        #     add_change_type_method(file_path)

    if filePath:
        print(f"File found: {filePath}")
    else:
        print("File not found.")

    # Kiểm tra flag `status`
    if status:
        click.echo("Status flag is set")

    # Kiểm tra flag `type`
    if type:
        click.echo("Type flag is set")


create.add_command(entity)

cli.add_command(controller)
cli.add_command(devops)
cli.add_command(whizlabs)
cli.add_command(dev)
cli.add_command(readmail)
cli.add_command(docker)
cli.add_command(dockerbasic)
cli.add_command(config)

cli.add_command(create)
cli.add_command(feature)
