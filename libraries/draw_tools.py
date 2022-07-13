
from curses import noecho
import random
import string
from lxml import etree
from datetime import datetime as dt
import uuid

def id_generator() -> str:
    #https://pynative.com/python-uuid-module-to-generate-universally-unique-identifiers/
    return str(uuid.uuid1()).replace('-','')
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase +'-_'
    size_id = 22
    return ''.join(random.choice(chars) for _ in range(size_id))

def create_layer(name:str, locked:int=1, id:str = id_generator()) -> etree._Element:
    mxcell = etree.Element('mxCell')
    mxcell.set('id',id)
    mxcell.set('value', name)
    mxcell.set('style', 'locked=' + str(locked))
    mxcell.set('parent',0)
    return mxcell

def create_node(type:str, **kwargs) -> etree._Element:
    node = etree.Element(type)
    node = set_attib_node(node=node, **kwargs)
    return node

def set_attib_node(node: etree._Element, **kwargs) -> etree._Element:
    if kwargs:
        for k,v in kwargs.items():
            if v:
                if k == 'a_s':
                    k = 'as'
                node.set(str(k),str(v))
    return node

def create_draw_io_file(diagram_xml_node: etree._Element, file_name:str = 'no_name.drawio') -> bool:
    xml_node = etree.Element('mxfile')
    xml_node.set('host', 'Electron')
    xml_node.set('modified', dt.now().strftime('%y-%m-%dT%H:%M:%SZ'))
    xml_node.set('agent', '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) draw.io/14.5.1 Chrome/89.0.4389.82 Electron/12.0.1 Safari/537.36')
    xml_node.set('etag', id_generator())
    xml_node.set('version', '14.5.1')
    xml_node.set('type', 'device')
    xml_node.append(diagram_xml_node)
    xml_tree = etree.ElementTree(xml_node)
    xml_tree.write(file_name)
    return True

def calculate_width(value: str) -> int:
    pixel_base = 10
    return len(value) * pixel_base + 15

def calculate_geometric_position(x:int, y:int, position:str = None, distance:int = None) -> tuple:
        #https://www.geeksforgeeks.org/g-fact-41-multiple-return-values-in-python/
        #https://note.nkmk.me/en/python-function-return-multiple-values/
        adtional_distance = 30
        if position == None or distance == None:
            return x,y
        if position.upper() == 'D':
            return x,(y + adtional_distance + distance)
        elif position.upper() == 'U':
            d = y - adtional_distance - distance
            if d > 0:
                return x,d
            else:
                raise Exception('Positional Invalid: x=' + str(x) + ' y=' + str(y) + ' position=' + str(position) + ' distance=' + str(distance) + ' ---> result negative y -> ' + str(d))
        elif position.upper() == 'L':
            d = x - adtional_distance - distance
            if d > 0:
                return d,y
            else:
                raise Exception('Positional Invalid: x=' + str(x) + ' y=' + str(y) + ' position=' + str(position) + ' distance=' + str(distance) + ' ---> result negative x -> ' + str(d))
        elif position.upper() == 'R':
            return (x + adtional_distance + distance),y
        else:
            raise Exception('Position Invalid: position=' + str(position) + ' Valid options are "L" (left) or "R" (right) or "U" (up) or "D" (down)')

