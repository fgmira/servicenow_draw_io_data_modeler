from libraries import draw_objects
from libraries import draw_tools
from libraries import snow_request

import sys
import traceback
import json
from collections import namedtuple
import logging
import logging.config
from os import path
import argparse
from datetime import datetime as dt


def parse_config(config_file_name:str) -> tuple:
    #   references:
    #       https://pynative.com/python-convert-json-data-into-custom-python-object/
    file = open(file=config_file_name, mode='r', encoding='utf8')
    string_json = file.read()
    def config_decoder(dictionary:dict) -> tuple:
        return namedtuple(typename='Config', field_names=dictionary.keys())(*dictionary.values())
    return json.loads(string_json, object_hook=config_decoder)



def __main__():
    # initialize log
    # references:
    #       https://coderzcolumn.com/tutorials/python/logging-config-simple-guide-to-configure-loggers-from-dictionary-and-config-files-in-python
    #       https://docs.python.org/3/library/logging.html
    #       https://stackoverflow.com/questions/23161745/python-logging-file-config-keyerror-formatters
    log_config_file = path.join(path.dirname(path.abspath(__file__)),'logging_config.ini')
    logging.config.fileConfig(log_config_file, disable_existing_loggers=False)
    logger = logging.getLogger('root')
    # get prompt args
    # references:
    #       https://docs.python.org/3/library/argparse.html
    #       https://www.geeksforgeeks.org/command-line-arguments-in-python/
    #       https://realpython.com/python-command-line-arguments/
    parse_agr = argparse.ArgumentParser()
    parse_agr.add_argument("-c", "--Config", help='Configuration file')
    args = parse_agr.parse_args()


    logger.info('Start Process.')
    if not(args.Config):
        logger.error('The configuration file was not informed in the call arguments')
        raise Exception ('The configuration file was not informed in the call arguments')

    logger.info('Get config in file name: ' + str(args.Config))
    try:
        obj_cfg = parse_config(args.Config)
    except Exception as e:
        logger.error('Error in parse config. See below. Config File Name: ' + args.Config)
        logger.error(traceback.format_exc())
        sys.exit(-10)

    try:
        logger.info('Create auth session to request data')
        if obj_cfg.auth.type == 'basic':
            logger.info('Create basic auth in instance:"' + obj_cfg.instance_url + '" using user:"' + obj_cfg.auth.basic.user + '"')
            snow = snow_request.SnowRequests(instance=obj_cfg.instance_url, user=obj_cfg.auth.basic.user, password=obj_cfg.auth.basic.password)
        elif obj_cfg.auth.type == 'oauth':
            logger.error('OAuth Authentication Not Implemented')
            raise NotImplementedError('OAuth Authentication Not Implemented')
        else:
            logger.error('Type authentication invalid:' + str(obj_cfg.auth.type))
    except Exception as e:
        logger.error('Error in Create Session')
        logger.error(traceback.format_exc())
        sys.exit(-10)

    try:
        logger.info('Start extract instance data from tables: ' + str(obj_cfg.table_list))
        snow.buildQuery(obj_cfg.table_list)
        snow.getData()
    except Exception as e:
        logger.error('Error in extract data')
        logger.error(traceback.format_exc())
        sys.exit(-10)
    
    try:
        logger.info('Start build model')
        diagram = draw_objects.Diagram()
        model = draw_objects.Model()
        first_table = True
        x = 10
        y = 10
        last_table = None
        count_tables = -1
        max_height = 0
        logger.info('Create Tables')
        for r in snow.data['result']:
            if last_table != r['name']:
                count_tables += 1
                if not(first_table):
                    model.root.appendElements(table)
                    if max_height < table.geometry.height:
                        max_height = table.geometry.height
                last_table = r['name']
                table = draw_objects.Table(value=r['name'], parent='2', vertex='1')
                if first_table:
                    table.setGeometricPosition(x,y)
                else:
                    if count_tables == 4:
                        count_tables = 0
                        x = 10
                        table.setGeometricPosition(x,y, position='D', distance=max_height)
                        max_height = 0
                    else:
                        table.setGeometricPosition(x,y, position='R', distance=distance)
            if r['element'] == 'sys_id':
                key = 'PK'
            elif r['internal_type'] == 'reference':
                key = 'FK'
            elif r['internal_type'] == 'document_id':
                key = 'FK'
            else:
                key = ''
            row = draw_objects.TableRow(
                key=key,
                reference_name=r['reference.name'], 
                physical_name=r['element'], 
                type=r['internal_type'], 
                parent=table.id,
                vertex='1'
            )
            table.appendRow(row=row)
            distance = table.geometry.width
            x = table.geometry.x
            y = table.geometry.y
            first_table = False

        model.root.appendElements(table)

        logger.info('Create Tables Relations')

        for e in model.root.elements:
            if isinstance(e,draw_objects.Table):
                list_references = e.getReferenceRows()
                for r in list_references:
                    ref_table = model.root.getElementByValue(r.reference_table_row.value)
                    if ref_table:
                        pk = ref_table.getSysIDRow()
                        link_table = draw_objects.EntityRelation(value='', parent='2', vertex='1')
                        link_table.setSourcePoint(pk.id)
                        link_table.setTargetPoint(r.id)
                        model.root.appendElements(link_table)
                    else:
                        logger.warning('Table "' + str(r.reference_table_row.value) + '" is referenced in the model, however it is not in the list of tables to be extracted or does not exist in the ServiceNow instance or its data was not extracted')

        diagram.model = model
        draw_tools.create_draw_io_file(diagram_xml_node=diagram.createXmlNode())
        logger.info('Finish build model')
    except Exception as e:
        logger.error('Error in create model')
        logger.error(traceback.format_exc())
        sys.exit(-10)
    logger.info('Finish process sucessful \o/ \o/ \o/ ')
    

__main__()
