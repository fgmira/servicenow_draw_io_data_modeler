# ServiceNow Draw IO Data Modeler
### Python tool to generate data models with table information from a ServiceNow instance

## :speech_balloon: About

This is a tool developed in python to extract information from tables in a ServiceNow instance and build a data model in Draw IO.

In this document you will find how to configure the environment so that it is possible to run the tool


## :runner: Step by Step

### 1. Downloading:
If you do not want to clone the repository to your local machine, here is a suggested procedure that you can perform:
1. Downloading using the `wget` command:
    1. Open you terminal
    2. Go to the directory where you want the tool to be:
        ```
            $ cd ~/directory/of/your/choice
        ```
    3. Run wget command:
        ```
            $ wget https://github.com/fgmira/servicenow_draw_io_data_modeler/main.zip
        ```
    4. Unzip file `main.zip`
        ```
            $ unzip main.zip
        ```
    5. Enter in directory `servicenow_draw_io_data_modeler-main`, if you run the `ls -l` command do you see like:
        ```
            -rw-rw-r-- 1 fabio fabio  717 Jul 13 20:51 config.json
            -rw-rw-r-- 1 fabio fabio 6686 Jul 13 20:51 generate_sn_drawio_data_model.py
            drwxrwxr-x 2 fabio fabio 4096 Jul 13 20:51 libraries
            -rw-rw-r-- 1 fabio fabio 1074 Jul 13 20:51 LICENSE
            -rw-rw-r-- 1 fabio fabio  417 Jul 13 20:51 logging_config.ini
            -rw-rw-r-- 1 fabio fabio  156 Jul 13 20:51 README.md
            -rw-rw-r-- 1 fabio fabio  201 Jul 13 20:51 requirements.txt
        ```

### 2. Python Environment:
It is good practice to create a python virtual environment. Let's see how to do this:
1. Creating the python virtual environment: `venv`
    1. In the directory `servicenow_draw_io_data_modeler-main`, run this command to create the venv environment:
        ```
            $ python3 -m venv .
        ```
    2. If you run the `ls -l` command do you see like:
        ```
            drwxrwxr-x 2 fabio fabio 4096 Jul 13 21:31 bin
            -rw-rw-r-- 1 fabio fabio  717 Jul 13 20:51 config.json
            -rw-rw-r-- 1 fabio fabio 6686 Jul 13 20:51 generate_sn_drawio_data_model.py
            drwxrwxr-x 2 fabio fabio 4096 Jul 13 21:31 include
            drwxrwxr-x 3 fabio fabio 4096 Jul 13 21:31 lib
            lrwxrwxrwx 1 fabio fabio    3 Jul 13 21:31 lib64 -> lib
            drwxrwxr-x 2 fabio fabio 4096 Jul 13 20:51 libraries
            -rw-rw-r-- 1 fabio fabio 1074 Jul 13 20:51 LICENSE
            -rw-rw-r-- 1 fabio fabio  417 Jul 13 20:51 logging_config.ini
            -rw-rw-r-- 1 fabio fabio   70 Jul 13 21:31 pyvenv.cfg
            -rw-rw-r-- 1 fabio fabio  156 Jul 13 20:51 README.md
            -rw-rw-r-- 1 fabio fabio  201 Jul 13 20:51 requirements.txt
        ```
    3. Activate `venv` run this command:
        ```
            $ source ./bin/activate
        ```
        if OK your prompt do like this:
        ```
            (servicenow_draw_io_data_modeler-main) $
        ```
2. Install dependencies:
    1. Now we need to install the dependencies. To do this, run the following command:
        ```
            (servicenow_draw_io_data_modeler-main) $ pip install -r requirements.txt
        ```
        If everything is ok, the command output should look like this:
        ```
            Collecting certifi==2022.6.15
            Using cached certifi-2022.6.15-py3-none-any.whl (160 kB)
            Collecting charset-normalizer==2.1.0
            Using cached charset_normalizer-2.1.0-py3-none-any.whl (39 kB)
            Collecting idna==3.3
            Using cached idna-3.3-py3-none-any.whl (61 kB)
            Collecting ijson==2.6.1
            Using cached ijson-2.6.1.tar.gz (29 kB)
            Preparing metadata (setup.py) ... done
            Collecting lxml==4.9.1
            Using cached lxml-4.9.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_24_x86_64.whl (6.9 MB)
            Collecting oauthlib==3.2.0
            Using cached oauthlib-3.2.0-py3-none-any.whl (151 kB)
            Collecting python-magic==0.4.27
            Using cached python_magic-0.4.27-py2.py3-none-any.whl (13 kB)
            Collecting pytz==2019.3
            Using cached pytz-2019.3-py2.py3-none-any.whl (509 kB)
            Collecting requests==2.28.1
            Using cached requests-2.28.1-py3-none-any.whl (62 kB)
            Collecting requests-oauthlib==1.3.1
            Using cached requests_oauthlib-1.3.1-py2.py3-none-any.whl (23 kB)
            Collecting six==1.16.0
            Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
            Collecting urllib3==1.26.10
            Using cached urllib3-1.26.10-py2.py3-none-any.whl (139 kB)
            Using legacy 'setup.py install' for ijson, since package 'wheel' is not installed.
            Installing collected packages: pytz, ijson, urllib3, six, python-magic, oauthlib, lxml, idna, charset-normalizer, certifi, requests, requests-oauthlib
            Running setup.py install for ijson ... done
            Successfully installed certifi-2022.6.15 charset-normalizer-2.1.0 idna-3.3 ijson-2.6.1 lxml-4.9.1 oauthlib-3.2.0 python-magic-0.4.27 pytz-2019.3 requests-2.28.1 requests-oauthlib-1.3.1 six-1.16.0 urllib3-1.26.10        
        ```
### 3. Configuring the tool:
You have to configure two settings to run the tool: ServiceNow Instance Settings and Log Settings
1. The configuration files:
    1. Instance and table settings to be modeled: file `config.json`
    
        If you open the file `config.json` do you see a JSON like this:
        ```
        {
           "instance_url": "https://dev99999.service-now.com",
            "auth": {
                "type": "basic",
                "basic": {
                    "user": "admin",
                    "password": "pwd"
                },
                "oauth": {
                    "client_id": "",
                    "client_secret": ""
                }
            },
            "table_list":[
                "x_210268_data_fish_business_rules_sources"
                ,"x_210268_data_fish_records_processing_queue"
                ,"x_210268_data_fish_tables_configs"
                ,"sys_user"
                ,"sys_user_delegate"
                ,"sys_user_geo_location"
                ,"sys_user_grmember"
                ,"sys_user_group"
                ,"sys_user_group_type"
                ,"sys_user_has_license"
                ,"sys_user_has_role"
                ,"sys_user_role"
            ]
        }
        ```
        - **instance_url***[string]*: Instance base URL, without the slash "/" at the end of the string.
        - **auth***[object]*: Object that determines the behavior of the authentication process in the instance.
            - **type***[string]*: Tells how authentication should be performed. It can be "basic" or "oauth".
                
                > :information_source: ***Note: I haven't authenticated by oauth yet. If this configuration is used, an exception of not implemented will be returned.***
            
            - **basic***[object]*: Object containing user and password information.
            - **oauth***[object]*: Object containing client id and client secret information. ***Not implemented***
        - **table_list***[list strings]*: List of table names whose information will be extracted from the instance for the data model to be assembled.
    
    2. Loggin settings: file `logging_config.ini`
        - This is a default python log module file. To learn how to configure it, I suggest reading the following documentation:

            https://docs.python.org/3/library/logging.html

            https://coderzcolumn.com/tutorials/python/logging-config-simple-guide-to-configure-loggers-from-dictionary-and-config-files-in-python

### 4. Run \o/:
Generating the data model

1. Running and generating the data model:
    1. Enter in directory `servicenow_draw_io_data_modeler-main`, and run this command: ***remember do activate venv***
        ```
            (servicenow_draw_io_data_modeler-main) $ python generate_sn_drawio_data_model.py -c config.json
        ```
        If evereting ok, do you see this messages:
        ```
            2022-07-13 22:31:18,608 : INFO : root : generate_sn_drawio_data_model : __main__ : Start Process.
            2022-07-13 22:31:18,608 : INFO : root : generate_sn_drawio_data_model : __main__ : Get config in file name: config.json
            2022-07-13 22:31:18,609 : INFO : root : generate_sn_drawio_data_model : __main__ : Create auth session to request data
            2022-07-13 22:31:18,609 : INFO : root : generate_sn_drawio_data_model : __main__ : Create basic auth in instance:"https://dev126949.service-now.com" using user:"admin"
            2022-07-13 22:31:18,609 : INFO : root : generate_sn_drawio_data_model : __main__ : Start extract instance data from tables: ['x_210268_data_fish_business_rules_sources', 'x_210268_data_fish_records_processing_queue', 'x_210268_data_fish_tables_configs', 'sys_user', 'sys_user_delegate', 'sys_user_geo_location', 'sys_user_grmember', 'sys_user_group', 'sys_user_group_type', 'sys_user_has_license', 'sys_user_has_role', 'sys_user_role']
            2022-07-13 22:31:18,610 : DEBUG : urllib3.connectionpool : connectionpool : _new_conn : Starting new HTTPS connection (1): dev126949.service-now.com:443
            2022-07-13 22:31:19,436 : DEBUG : urllib3.connectionpool : connectionpool : _make_request : https://dev126949.service-now.com:443 "GET /api/now/table/sys_dictionary?sysparm_query=nameINx_210268_data_fish_business_rules_sources,x_210268_data_fish_records_processing_queue,x_210268_data_fish_tables_configs,sys_user,sys_user_delegate,sys_user_geo_location,sys_user_grmember,sys_user_group,sys_user_group_type,sys_user_has_license,sys_user_has_role,sys_user_role%5Einternal_type!=collection&%5EORDERBYname&sysparm_fields=name,element,internal_type,reference.name,dependent_on_field&sysparm_exclude_reference_link=True&sysparm_no_count=true HTTP/1.1" 200 None
            2022-07-13 22:31:19,734 : INFO : root : generate_sn_drawio_data_model : __main__ : Start build model
            2022-07-13 22:31:19,734 : INFO : root : generate_sn_drawio_data_model : __main__ : Create Tables
            2022-07-13 22:31:19,776 : INFO : root : generate_sn_drawio_data_model : __main__ : Create Tables Relations
            2022-07-13 22:31:19,776 : WARNING : root : generate_sn_drawio_data_model : __main__ : Table "cmn_building" is referenced in the model, however it is not in the list of tables to be extracted or does not exist in the ServiceNow instance or its data was not extracted
            2022-07-13 22:31:19,776 : WARNING : root : generate_sn_drawio_data_model : __main__ : Table "core_company" is referenced in the model, however it is not in the list of tables to be extracted or does not exist in the ServiceNow instance or its data was not extracted
            2022-07-13 22:31:19,777 : WARNING : root : generate_sn_drawio_data_model : __main__ : Table "cmn_cost_center" is referenced in the model, however it is not in the list of tables to be extracted or does not exist in the ServiceNow instance or its data was not extracted
            2022-07-13 22:31:19,777 : WARNING : root : generate_sn_drawio_data_model : __main__ : Table "sys_perspective" is referenced in the model, however it is not in the list of tables to be extracted or does not exist in the ServiceNow instance or its data was not extracted
            2022-07-13 22:31:19,777 : WARNING : root : generate_sn_drawio_data_model : __main__ : Table "cmn_department" is referenced in the model, however it is not in the list of tables to be extracted or does not exist in the ServiceNow instance or its data was not extracted
            2022-07-13 22:31:19,777 : WARNING : root : generate_sn_drawio_data_model : __main__ : Table "ldap_server_config" is referenced in the model, however it is not in the list of tables to be extracted or does not exist in the ServiceNow instance or its data was not extracted
            2022-07-13 22:31:19,777 : WARNING : root : generate_sn_drawio_data_model : __main__ : Table "cmn_location" is referenced in the model, however it is not in the list of tables to be extracted or does not exist in the ServiceNow instance or its data was not extracted
            2022-07-13 22:31:19,777 : WARNING : root : generate_sn_drawio_data_model : __main__ : Table "cmn_schedule" is referenced in the model, however it is not in the list of tables to be extracted or does not exist in the ServiceNow instance or its data was not extracted
            2022-07-13 22:31:19,778 : WARNING : root : generate_sn_drawio_data_model : __main__ : Table "cmn_cost_center" is referenced in the model, however it is not in the list of tables to be extracted or does not exist in the ServiceNow instance or its data was not extracted
            2022-07-13 22:31:19,778 : WARNING : root : generate_sn_drawio_data_model : __main__ : Table "entl_subscription_map" is referenced in the model, however it is not in the list of tables to be extracted or does not exist in the ServiceNow instance or its data was not extracted
            2022-07-13 22:31:19,778 : WARNING : root : generate_sn_drawio_data_model : __main__ : Table "license_details" is referenced in the model, however it is not in the list of tables to be extracted or does not exist in the ServiceNow instance or its data was not extracted
            2022-07-13 22:31:19,778 : WARNING : root : generate_sn_drawio_data_model : __main__ : Table "license_details_deleted" is referenced in the model, however it is not in the list of tables to be extracted or does not exist in the ServiceNow instance or its data was not extracted
            2022-07-13 22:31:19,778 : WARNING : root : generate_sn_drawio_data_model : __main__ : Table "sys_user_role_contains" is referenced in the model, however it is not in the list of tables to be extracted or does not exist in the ServiceNow instance or its data was not extracted
            2022-07-13 22:31:19,778 : WARNING : root : generate_sn_drawio_data_model : __main__ : Table "sys_db_object" is referenced in the model, however it is not in the list of tables to be extracted or does not exist in the ServiceNow instance or its data was not extracted
            2022-07-13 22:31:19,778 : WARNING : root : generate_sn_drawio_data_model : __main__ : Table "sys_script" is referenced in the model, however it is not in the list of tables to be extracted or does not exist in the ServiceNow instance or its data was not extracted
            2022-07-13 22:31:19,825 : INFO : root : generate_sn_drawio_data_model : __main__ : Finish build model
            2022-07-13 22:31:19,826 : INFO : root : generate_sn_drawio_data_model : __main__ : Finish process sucessful \o/ \o/ \o/ 

        ```
    2. In directory `servicenow_draw_io_data_modeler-main`, you have a two new files:
        - **log_app.log**: This file contains the processing log. If you have not changed the log settings, the same messages will appear on your screen.
        - **no_name.drawio**: This file contains the data model. For instruction to use Draw IO visit:
            - github: https://github.com/jgraph/drawio-desktop/tree/release
            - more infos: https://drawio-app.com/ (I think is the official site :no_good:)
            - online use: https://app.diagrams.net/
            - installation on linux: https://ubunlog.com/en/draw-io-desktop-install-ubuntu-diagram-generator/

## :stars: Thanks
    
Here I leave a thank you to @github/GanizaniSitara, who shared the code in his [drawio project](https://github.com/GanizaniSitara/drawio) project that gave me a way to start building this tool

    


