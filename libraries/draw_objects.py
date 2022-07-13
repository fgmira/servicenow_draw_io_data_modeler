from typing import Any
from libraries import draw_tools
from lxml import etree

class Diagram(object):
    def __init__(self) -> None:
        self.type = 'diagram'
        self.id = draw_tools.id_generator()
        self.name = 'Page-1'
        self.model = None
    def createXmlNode(self) -> etree._Element:
        xml_node = draw_tools.create_node(
            type=self.type,
            id = self.id,
            name = self.name
            )
        xml_node.append(self.model.createXmlNode())
        return xml_node

class Model(object):
    def __init__(self) -> None:
        self.type = 'mxGraphModel'
        self.dx=2062,
        self.dy=840,
        self.grid=1,
        self.gridSize=10,
        self.guides=1,
        self.tooltips=1,
        self.connect=1,
        self.arrows=1,
        self.fold=1,
        self.page=1,
        self.pageScale=1,
        self.pageWidth=850,
        self.pageHeight=1100,
        self.math=0,
        self.shadow=0
        self.root = Root()
    def createXmlNode(self) -> etree._Element:
        xml_node = draw_tools.create_node(
            type = self.type,
            dx = self.dx,
            dy = self.dy,
            grid = self.grid,
            gridSize = self.gridSize,
            guides = self.guides,
            tooltips = self.tooltips,
            connect = self.connect,
            arrows = self.arrows,
            fold = self.fold,
            page = self.page,
            pageScale = self.pageScale,
            pageWidth = self.pageWidth,
            pageHeight = self.pageHeight,
            math = self.math,
            shadow = self.shadow
            )
        xml_node.append(self.root.createXmlNode())
        return xml_node


class Root(object):
    def __init__(self) -> None:
        self.type = 'root'
        self.elements = []
        self.elements.append(SimpleMxCell(1))
        self.elements.append(SimpleMxCell(2,1))
    
    def appendElements(self, element:object) -> None:
        self.elements.append(element)
    
    def createXmlNode(self) -> etree._Element:
        xml_node = draw_tools.create_node(
            type=self.type
            )
        for e in self.elements:
            if isinstance(e,Table):
                xml_node.append(e.createXmlNode())
                for r in e.table_rows:
                    xml_node.append(r.createXmlNode())
                    xml_node.append(r.key_row.createXmlNode())
                    xml_node.append(r.physical_name_row.createXmlNode())
                    xml_node.append(r.type_row.createXmlNode())
                    xml_node.append(r.reference_table_row.createXmlNode())
            else:
                xml_node.append(e.createXmlNode())
        return xml_node
    def getElementByValue(self, search_value:Any) -> object:
        for e in self.elements:
            if e.value == search_value:
                return e


class SimpleMxCell(object):
    def __init__(self, id:int, parent:int = None) -> None:
        self.type = 'mxCell'
        self.value = None
        self.id = id
        self.parent = parent
    def createXmlNode(self) -> etree._Element:
        return draw_tools.create_node(
            type = self.type,
            id = self.id,
            parent = self.parent
            )


class Style(object):
    def __init__(self):
        self.shape = None

        self.align = None
        self.bottom= None
        self.childLayout = None
        self.collapsible = None
        self.connectable = None
        self.container = None
        self.dropTarget = None
        self.edgeStyle = None
        self.endArrow = None
        self.endFill = None
        self.entryX = None
        self.entryY = None
        self.entryDx = None
        self.entryDy = None
        self.exitX = None
        self.exitY = None
        self.exitDx = None
        self.exitDy = None
        self.fixedRows = None
        self.fillColor = None
        self.fontSize = None
        self.fontStyle = None
        self.horizontal = None
        self.html = None
        self.jumpStyle = None
        self.left = None
        self.overflow = None
        self.points = None
        self.portConstraint = None
        self.resizeLast = None
        self.right = None
        self.rounded = None
        self.rowLines = None
        self.spacingLeft = None
        self.startSize = None
        self.swimlaneBody = None
        self.swimlaneHead = None
        self.top = None
    def generateStyleString(self) -> str:
        result = ""
        for k,v in self.__dict__.items():
            if v != None:
                result +=  str(k) + '=' + str(v) + ';'
        return result


class Geometry(object):
    def __init__(self, x:int = None, y:int = None, width:int = None, height:int = None, a_s:str = None, relative:int = None) -> None:
        self.type = 'mxGeometry'
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.a_s = a_s
        self.relative = relative
        self.childs = []

    def appendChild(self, type:str ,x:int, y:int, width:int, height:int, a_s:str) -> None:
        self.childs.append(GeometryChild(type, x, y, width, height, a_s))

    def putChild(self, pos: int, **kwards) -> None:
        if kwards.get('type'):
            self.childs[pos].type = kwards.get('type')
        if kwards.get('x'):
            self.childs[pos].x = kwards.get('x')
        if kwards.get('y'):
            self.childs[pos].x = kwards.get('x')
        if kwards.get('width'):
            self.childs[pos].width = kwards.get('width')
        if kwards.get('height'):
            self.childs[pos].height = kwards.get('height')
        if kwards.get('a_s'):
            self.childs[pos].a_s = kwards.get('a_s')
    def createXmlNode(self) -> etree._Element:
        xml_node = draw_tools.create_node(
            type=self.type,
            x=self.x,
            y=self.y,
            width=self.width,
            height=self.height,
            a_s=self.a_s,
        )
        for c in self.childs:
            xml_node.append(c.createXmlNode())
        return xml_node

class GeometryChild(object):
    def __init__(self, type:str ,x:int, y:int, width:int, height:int, a_s:str) -> None:
        self.type = type
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.a_s = a_s
    def createXmlNode(self) -> etree._Element:
        return draw_tools.create_node(
            type=self.type,
            x=self.x,
            y=self.y,
            width=self.width,
            height=self.height,
            a_s=self.a_s,
        )

class DrawIOObejct(object):
    def __init__(self, value:str, parent: str = None, vertex: str=None) -> None:
        self.type = 'mxCell'
        self.id = draw_tools.id_generator()
        self.value = value
        self.style = Style()
        self.parent = parent
        self.vertex = vertex
        self.geometry = Geometry()
    def createXmlNode(self) -> etree._Element:
        xml_node = draw_tools.create_node(
            type=self.type,
            value=self.value,
            id=self.id,
            style=self.style.generateStyleString(),
            parent=self.parent,
            vertex=self.vertex
        )
        if self.geometry:
            xml_node.append(self.geometry.createXmlNode())
        return xml_node
    def setGeometricPosition(self, x:int, y:int, position:str = None, distance:int = None) -> None:
        self.geometry.x, self.geometry.y = draw_tools.calculate_geometric_position(x=x, y=y, position=position, distance=distance)

class Table(DrawIOObejct):
    def __init__(self, value: str, parent: str = None, vertex: str = None) -> None:
        super().__init__(value, parent, vertex)
        self.style.shape = 'table'
        self.style.childLayout = 'tableLayout'
        self.style.fixedRows = 1
        self.style.rowLines = 0
        self.style.fontStyle = 1
        self.style.align = 'center'
        self.style.resizeLast = 1
        self.style.collapsible = 1
        self.style.container = 1
        self.style.startSize = 30
        self.table_rows = []
        self.geometry.height = 30
        self.geometry.width=0
        self.geometry.a_s='geometry'
        self.max_width_key = 0
        self.max_width_physical = 0
        self.max_width_type = 0
        self.max_width_reference = 0
        
    def appendRow(self, row: 'TableRow') -> None:
        self.geometry.height = 30 * (len(self.table_rows) + 1 ) + 30
        row.geometry.y = 30 * (len(self.table_rows)) + 30
        if row.key_row.geometry.width > self.max_width_key:
            self.max_width_key = row.key_row.geometry.width
        if row.physical_name_row.geometry.width > self.max_width_physical:
            self.max_width_physical = row.physical_name_row.geometry.width
        if row.type_row.geometry.width > self.max_width_type:
            self.max_width_type = row.type_row.geometry.width
        if row.reference_table_row.geometry.width > self.max_width_reference:
            self.max_width_reference = row.reference_table_row.geometry.width
        row_width = self.max_width_key + self.max_width_physical + self.max_width_type + self.max_width_reference
        if row_width > self.geometry.width:
            self.geometry.width = row_width

        self.table_rows.append(row)
        for r in self.table_rows:
            r.ajustWidth(
                new_width=self.geometry.width,
                new_width_key=self.max_width_key,
                new_width_physical=self.max_width_physical,
                new_width_type=self.max_width_type,
                new_width_reference=self.max_width_reference
                )
    def getSysIDRow(self) -> 'TableRow':
        for r in self.table_rows:
            if r.physical_name_row.value == 'sys_id':
                return r
    
    def getReferenceRows(self) -> list:
        result = []
        for r in self.table_rows:
            if r.type_row.value == 'reference':
                result.append(r)
        return result


class TableRow(DrawIOObejct):
    def __init__(self, key:str, reference_name: str, physical_name:str, type:str, parent: str = None, vertex: str = None) -> None:
        super().__init__('', parent, vertex)
        self.style.shape='tableRow'
        self.style.horizontal=0
        self.style.startSize=0
        self.style.swimlaneHead=0
        self.style.swimlaneBody=0
        self.style.fillColor='none'
        self.style.collapsible=0
        self.style.dropTarget=0
        self.style.points=[[0,0.5],[1,0.5]]
        self.style.portConstraint='eastwest'
        self.style.top=0
        self.style.left=0
        self.style.right=0
        self.style.bottom=1

        self.key_row = KeyRow(value=key, parent=self.id,vertex=self.vertex)
        x = self.key_row.geometry.width
        
        self.physical_name_row = PhysicalNameRow(value=physical_name, x=x, parent=self.id,vertex=self.vertex)
        x += self.physical_name_row.geometry.width

        self.type_row = TypeRow(value=type, x=x, parent=self.id,vertex=self.vertex)
        x += self.type_row.geometry.width

        self.reference_table_row = ReferenceTableRow(value=reference_name, x=x, parent=self.id,vertex=self.vertex)
        x += self.reference_table_row.geometry.width
        
        self.geometry.width = x
        self.geometry.height = 30
        self.geometry.a_s='geometry'
    def ajustWidth(self, new_width: int, new_width_key:int, new_width_physical:int, new_width_type:int, new_width_reference:int) -> None:
        if new_width < 0:
            raise Exception('new_width < 0: new_width = ' + str(new_width))
        if new_width_key < 0:
            raise Exception('new_width_key < 0: new_width_key = ' + str(new_width_key))
        if new_width_physical < 0:
            raise Exception('new_width_physical < 0: new_width_physical = ' + str(new_width_physical))
        if new_width < 0:
            raise Exception('new_width_type < 0: new_width_type = ' + str(new_width_type))
        if new_width < 0:
            raise Exception('new_width_reference < 0: new_width_reference = ' + str(new_width_reference))
        self.geometry.width = new_width
        self.key_row.putWidth(new_width=new_width_key)
        x = new_width_key
        self.physical_name_row.putWidth(new_width=new_width_physical, new_x=x)
        x += new_width_physical
        self.type_row.putWidth(new_width=new_width_type, new_x=x)
        x += new_width_type
        self.reference_table_row.putWidth(new_width=new_width_reference, new_x=x)
        
class PartRow(DrawIOObejct):
    def __init__(self, value: str, parent: str = None, vertex: str = None) -> None:
        super().__init__(value, parent, vertex)
        self.style.shape='partialRectangle'
        self.style.connectable=0
        self.style.fillColor='none'
        self.style.top=0
        self.style.left=0
        self.style.bottom=0
        self.style.right=0
        self.style.fontStyle=1
        self.style.overflow='hidden'
        self.geometry.height=30
        self.geometry.width = draw_tools.calculate_width(value=self.value)
        self.geometry.a_s='geometry'
        self.geometry.appendChild(
            type='mxRectangle',
            x=None,
            y=None,
            width=self.geometry.width,
            height=30,
            a_s='alternateBounds'
        )
    def putWidth(self, new_width: int, new_x: int = None) -> None:
        self.geometry.x = new_x
        self.geometry.width = new_width
        self.geometry.putChild(pos=0, width=new_width)

class KeyRow(PartRow):
    def __init__(self, value: str, parent: str = None, vertex: str = None) -> None:
        super().__init__(value, parent, vertex)
        self.style.align='center'

class ReferenceTableRow(PartRow):
    def __init__(self, value: str, x: int, parent: str = None, vertex: str = None) -> None:
        super().__init__(value, parent, vertex)
        self.style.align='left'

class PhysicalNameRow(PartRow):
    def __init__(self, value: str, x: int, parent: str = None, vertex: str = None) -> None:
        super().__init__(value, parent, vertex)
        self.style.align='left'

class TypeRow(PartRow):
    def __init__(self, value: str, x: int, parent: str = None, vertex: str = None) -> None:
        super().__init__(value, parent, vertex)
        self.style.align='left'

class EntityRelation(DrawIOObejct):
    def __init__(self, value: str, source:str = None, target:str = None, edge:int = 1, parent: str = None, vertex: str = None) -> None:
        super().__init__(value, parent, vertex)
        self.source = source
        self.target = target
        self.edge = edge
        self.style.edgeStyle='entityRelationEdgeStyle'
        self.style.fontSize=12
        self.style.html=1
        self.style.endArrow='ERzeroToMany'
        self.style.endFill=1
        self.style.rounded=0
        self.style.entryX=0
        self.style.entryY=0.5
        self.style.entryDx=0
        self.style.entryDy=0
        self.style.exitX=1
        self.style.exitY=0.5
        self.style.exitDx=0
        self.style.exitDy=0
        self.style.jumpStyle='arc'
        self.geometry.width=100
        self.geometry.height=100
        self.geometry.relative=1
        self.geometry.a_s='geometry'
    def setSourcePoint(self, source:str, x:int=10, y:int=10) -> None:
        self.source = source
        self.geometry.appendChild(
            type='mxPoint',
            width=None,
            height=None,
            x=x,
            y=y,
            a_s='sourcePoint'
        )
    def setTargetPoint(self, target:str, x:int=10, y:int=10) -> None:
        self.target = target
        self.geometry.appendChild(
            type='mxPoint',
            width=None,
            height=None,
            x=x,
            y=y,
            a_s='targetPoint'
        )
    def createXmlNode(self) -> etree._Element:
        xml_node = super().createXmlNode()
        xml_node = draw_tools.set_attib_node(
            node=xml_node,
            source=self.source,
            target=self.target,
            edge=self.edge
            )
        return xml_node

