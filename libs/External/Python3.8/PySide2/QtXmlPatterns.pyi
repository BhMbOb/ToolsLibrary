# This Python file uses the following encoding: utf-8
#############################################################################
##
## Copyright (C) 2020 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of Qt for Python.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 3 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL3 included in the
## packaging of this file. Please review the following information to
## ensure the GNU Lesser General Public License version 3 requirements
## will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 2.0 or (at your option) the GNU General
## Public license version 3 or any later version approved by the KDE Free
## Qt Foundation. The licenses are as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-2.0.html and
## https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################

"""
This file contains the exact signatures for all functions in module
PySide2.QtXmlPatterns, except for defaults which are replaced by "...".
"""

# Module PySide2.QtXmlPatterns
import PySide2
try:
    import typing
except ImportError:
    from PySide2.support.signature import typing
from PySide2.support.signature.mapping import (
    Virtual, Missing, Invalid, Default, Instance)

class Object(object): pass

import shiboken2 as Shiboken
Shiboken.Object = Object

import PySide2.QtCore
import PySide2.QtXmlPatterns


class QAbstractMessageHandler(PySide2.QtCore.QObject):

    def __init__(self, parent:typing.Optional[PySide2.QtCore.QObject]=...): ...

    def handleMessage(self, type:PySide2.QtCore.QtMsgType, description:str, identifier:PySide2.QtCore.QUrl, sourceLocation:PySide2.QtXmlPatterns.QSourceLocation): ...
    def message(self, type:PySide2.QtCore.QtMsgType, description:str, identifier:PySide2.QtCore.QUrl=..., sourceLocation:PySide2.QtXmlPatterns.QSourceLocation=...): ...


class QAbstractUriResolver(PySide2.QtCore.QObject):

    def __init__(self, parent:typing.Optional[PySide2.QtCore.QObject]=...): ...

    def resolve(self, relative:PySide2.QtCore.QUrl, baseURI:PySide2.QtCore.QUrl) -> PySide2.QtCore.QUrl: ...


class QAbstractXmlNodeModel(Shiboken.Object):
    Parent                   : QAbstractXmlNodeModel = ... # 0x0
    FirstChild               : QAbstractXmlNodeModel = ... # 0x1
    InheritNamespaces        : QAbstractXmlNodeModel = ... # 0x1
    PreserveNamespaces       : QAbstractXmlNodeModel = ... # 0x2
    PreviousSibling          : QAbstractXmlNodeModel = ... # 0x2
    NextSibling              : QAbstractXmlNodeModel = ... # 0x3

    class NodeCopySetting(object):
        InheritNamespaces        : QAbstractXmlNodeModel.NodeCopySetting = ... # 0x1
        PreserveNamespaces       : QAbstractXmlNodeModel.NodeCopySetting = ... # 0x2

    class SimpleAxis(object):
        Parent                   : QAbstractXmlNodeModel.SimpleAxis = ... # 0x0
        FirstChild               : QAbstractXmlNodeModel.SimpleAxis = ... # 0x1
        PreviousSibling          : QAbstractXmlNodeModel.SimpleAxis = ... # 0x2
        NextSibling              : QAbstractXmlNodeModel.SimpleAxis = ... # 0x3

    def __init__(self): ...

    def attributes(self, element:PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> typing.List: ...
    def baseUri(self, ni:PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> PySide2.QtCore.QUrl: ...
    def compareOrder(self, ni1:PySide2.QtXmlPatterns.QXmlNodeModelIndex, ni2:PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex.DocumentOrder: ...
    @typing.overload
    def createIndex(self, data:int) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex: ...
    @typing.overload
    def createIndex(self, data:int, additionalData:int) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex: ...
    @typing.overload
    def createIndex(self, pointer:int, additionalData:int=...) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex: ...
    def documentUri(self, ni:PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> PySide2.QtCore.QUrl: ...
    def elementById(self, NCName:PySide2.QtXmlPatterns.QXmlName) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex: ...
    def isDeepEqual(self, ni1:PySide2.QtXmlPatterns.QXmlNodeModelIndex, ni2:PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> bool: ...
    def kind(self, ni:PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex.NodeKind: ...
    def name(self, ni:PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> PySide2.QtXmlPatterns.QXmlName: ...
    def namespaceBindings(self, n:PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> typing.List: ...
    def namespaceForPrefix(self, ni:PySide2.QtXmlPatterns.QXmlNodeModelIndex, prefix:Missing("PySide2.QtXmlPatterns.QXmlName.PrefixCode")) -> Missing("PySide2.QtXmlPatterns.QXmlName.NamespaceCode"): ...
    def nextFromSimpleAxis(self, axis:PySide2.QtXmlPatterns.QAbstractXmlNodeModel.SimpleAxis, origin:PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex: ...
    def nodesByIdref(self, NCName:PySide2.QtXmlPatterns.QXmlName) -> typing.List: ...
    def root(self, n:PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex: ...
    def sendNamespaces(self, n:PySide2.QtXmlPatterns.QXmlNodeModelIndex, receiver:PySide2.QtXmlPatterns.QAbstractXmlReceiver): ...
    def sourceLocation(self, index:PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> PySide2.QtXmlPatterns.QSourceLocation: ...
    def stringValue(self, n:PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> str: ...
    def typedValue(self, n:PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> typing.Any: ...


class QAbstractXmlReceiver(Shiboken.Object):

    def __init__(self): ...

    def atomicValue(self, value:typing.Any): ...
    def attribute(self, name:PySide2.QtXmlPatterns.QXmlName, value:str): ...
    def characters(self, value:str): ...
    def comment(self, value:str): ...
    def endDocument(self): ...
    def endElement(self): ...
    def endOfSequence(self): ...
    def namespaceBinding(self, name:PySide2.QtXmlPatterns.QXmlName): ...
    def processingInstruction(self, target:PySide2.QtXmlPatterns.QXmlName, value:str): ...
    def startDocument(self): ...
    def startElement(self, name:PySide2.QtXmlPatterns.QXmlName): ...
    def startOfSequence(self): ...
    def whitespaceOnly(self, value:str): ...


class QSourceLocation(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtXmlPatterns.QSourceLocation): ...
    @typing.overload
    def __init__(self, uri:PySide2.QtCore.QUrl, line:int=..., column:int=...): ...

    @staticmethod
    def __copy__(): ...
    def column(self) -> int: ...
    def isNull(self) -> bool: ...
    def line(self) -> int: ...
    def setColumn(self, newColumn:int): ...
    def setLine(self, newLine:int): ...
    def setUri(self, newUri:PySide2.QtCore.QUrl): ...
    def uri(self) -> PySide2.QtCore.QUrl: ...


class QXmlFormatter(PySide2.QtXmlPatterns.QXmlSerializer):

    def __init__(self, query:PySide2.QtXmlPatterns.QXmlQuery, outputDevice:PySide2.QtCore.QIODevice): ...

    def atomicValue(self, value:typing.Any): ...
    def attribute(self, name:PySide2.QtXmlPatterns.QXmlName, value:str): ...
    def characters(self, value:str): ...
    def comment(self, value:str): ...
    def endDocument(self): ...
    def endElement(self): ...
    def endOfSequence(self): ...
    def indentationDepth(self) -> int: ...
    def processingInstruction(self, name:PySide2.QtXmlPatterns.QXmlName, value:str): ...
    def setIndentationDepth(self, depth:int): ...
    def startDocument(self): ...
    def startElement(self, name:PySide2.QtXmlPatterns.QXmlName): ...
    def startOfSequence(self): ...


class QXmlItem(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, atomicValue:typing.Any): ...
    @typing.overload
    def __init__(self, node:PySide2.QtXmlPatterns.QXmlNodeModelIndex): ...
    @typing.overload
    def __init__(self, other:PySide2.QtXmlPatterns.QXmlItem): ...

    @staticmethod
    def __copy__(): ...
    def isAtomicValue(self) -> bool: ...
    def isNode(self) -> bool: ...
    def isNull(self) -> bool: ...
    def toAtomicValue(self) -> typing.Any: ...
    def toNodeModelIndex(self) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex: ...


class QXmlName(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, namePool:PySide2.QtXmlPatterns.QXmlNamePool, localName:str, namespaceURI:str=..., prefix:str=...): ...
    @typing.overload
    def __init__(self, other:PySide2.QtXmlPatterns.QXmlName): ...

    @staticmethod
    def __copy__(): ...
    @staticmethod
    def fromClarkName(clarkName:str, namePool:PySide2.QtXmlPatterns.QXmlNamePool) -> PySide2.QtXmlPatterns.QXmlName: ...
    @staticmethod
    def isNCName(candidate:str) -> bool: ...
    def isNull(self) -> bool: ...
    def localName(self, query:PySide2.QtXmlPatterns.QXmlNamePool) -> str: ...
    def namespaceUri(self, query:PySide2.QtXmlPatterns.QXmlNamePool) -> str: ...
    def prefix(self, query:PySide2.QtXmlPatterns.QXmlNamePool) -> str: ...
    def toClarkName(self, query:PySide2.QtXmlPatterns.QXmlNamePool) -> str: ...


class QXmlNamePool(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtXmlPatterns.QXmlNamePool): ...

    @staticmethod
    def __copy__(): ...


class QXmlNodeModelIndex(Shiboken.Object):
    Precedes                 : QXmlNodeModelIndex = ... # -0x1
    Is                       : QXmlNodeModelIndex = ... # 0x0
    Attribute                : QXmlNodeModelIndex = ... # 0x1
    Follows                  : QXmlNodeModelIndex = ... # 0x1
    Comment                  : QXmlNodeModelIndex = ... # 0x2
    Document                 : QXmlNodeModelIndex = ... # 0x4
    Element                  : QXmlNodeModelIndex = ... # 0x8
    Namespace                : QXmlNodeModelIndex = ... # 0x10
    ProcessingInstruction    : QXmlNodeModelIndex = ... # 0x20
    Text                     : QXmlNodeModelIndex = ... # 0x40

    class DocumentOrder(object):
        Precedes                 : QXmlNodeModelIndex.DocumentOrder = ... # -0x1
        Is                       : QXmlNodeModelIndex.DocumentOrder = ... # 0x0
        Follows                  : QXmlNodeModelIndex.DocumentOrder = ... # 0x1

    class NodeKind(object):
        Attribute                : QXmlNodeModelIndex.NodeKind = ... # 0x1
        Comment                  : QXmlNodeModelIndex.NodeKind = ... # 0x2
        Document                 : QXmlNodeModelIndex.NodeKind = ... # 0x4
        Element                  : QXmlNodeModelIndex.NodeKind = ... # 0x8
        Namespace                : QXmlNodeModelIndex.NodeKind = ... # 0x10
        ProcessingInstruction    : QXmlNodeModelIndex.NodeKind = ... # 0x20
        Text                     : QXmlNodeModelIndex.NodeKind = ... # 0x40

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtXmlPatterns.QXmlNodeModelIndex): ...

    @staticmethod
    def __copy__(): ...
    def additionalData(self) -> int: ...
    def data(self) -> int: ...
    def internalPointer(self) -> int: ...
    def isNull(self) -> bool: ...
    def model(self) -> PySide2.QtXmlPatterns.QAbstractXmlNodeModel: ...


class QXmlQuery(Shiboken.Object):
    XQuery10                 : QXmlQuery = ... # 0x1
    XSLT20                   : QXmlQuery = ... # 0x2
    XmlSchema11IdentityConstraintSelector: QXmlQuery = ... # 0x400
    XmlSchema11IdentityConstraintField: QXmlQuery = ... # 0x800
    XPath20                  : QXmlQuery = ... # 0x1000

    class QueryLanguage(object):
        XQuery10                 : QXmlQuery.QueryLanguage = ... # 0x1
        XSLT20                   : QXmlQuery.QueryLanguage = ... # 0x2
        XmlSchema11IdentityConstraintSelector: QXmlQuery.QueryLanguage = ... # 0x400
        XmlSchema11IdentityConstraintField: QXmlQuery.QueryLanguage = ... # 0x800
        XPath20                  : QXmlQuery.QueryLanguage = ... # 0x1000

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, np:PySide2.QtXmlPatterns.QXmlNamePool): ...
    @typing.overload
    def __init__(self, other:PySide2.QtXmlPatterns.QXmlQuery): ...
    @typing.overload
    def __init__(self, queryLanguage:PySide2.QtXmlPatterns.QXmlQuery.QueryLanguage, np:PySide2.QtXmlPatterns.QXmlNamePool=...): ...

    @staticmethod
    def __copy__(): ...
    @typing.overload
    def bindVariable(self, localName:str, arg__2:PySide2.QtCore.QIODevice): ...
    @typing.overload
    def bindVariable(self, localName:str, query:PySide2.QtXmlPatterns.QXmlQuery): ...
    @typing.overload
    def bindVariable(self, localName:str, value:PySide2.QtXmlPatterns.QXmlItem): ...
    @typing.overload
    def bindVariable(self, name:PySide2.QtXmlPatterns.QXmlName, arg__2:PySide2.QtCore.QIODevice): ...
    @typing.overload
    def bindVariable(self, name:PySide2.QtXmlPatterns.QXmlName, query:PySide2.QtXmlPatterns.QXmlQuery): ...
    @typing.overload
    def bindVariable(self, name:PySide2.QtXmlPatterns.QXmlName, value:PySide2.QtXmlPatterns.QXmlItem): ...
    @typing.overload
    def evaluateTo(self, callback:PySide2.QtXmlPatterns.QAbstractXmlReceiver) -> bool: ...
    @typing.overload
    def evaluateTo(self, result:PySide2.QtXmlPatterns.QXmlResultItems): ...
    @typing.overload
    def evaluateTo(self, target:PySide2.QtCore.QIODevice) -> bool: ...
    def initialTemplateName(self) -> PySide2.QtXmlPatterns.QXmlName: ...
    def isValid(self) -> bool: ...
    def messageHandler(self) -> PySide2.QtXmlPatterns.QAbstractMessageHandler: ...
    def namePool(self) -> PySide2.QtXmlPatterns.QXmlNamePool: ...
    def queryLanguage(self) -> PySide2.QtXmlPatterns.QXmlQuery.QueryLanguage: ...
    @typing.overload
    def setFocus(self, document:PySide2.QtCore.QIODevice) -> bool: ...
    @typing.overload
    def setFocus(self, documentURI:PySide2.QtCore.QUrl) -> bool: ...
    @typing.overload
    def setFocus(self, focus:str) -> bool: ...
    @typing.overload
    def setFocus(self, item:PySide2.QtXmlPatterns.QXmlItem): ...
    @typing.overload
    def setInitialTemplateName(self, name:PySide2.QtXmlPatterns.QXmlName): ...
    @typing.overload
    def setInitialTemplateName(self, name:str): ...
    def setMessageHandler(self, messageHandler:PySide2.QtXmlPatterns.QAbstractMessageHandler): ...
    @typing.overload
    def setQuery(self, queryURI:PySide2.QtCore.QUrl, baseURI:PySide2.QtCore.QUrl=...): ...
    @typing.overload
    def setQuery(self, sourceCode:PySide2.QtCore.QIODevice, documentURI:PySide2.QtCore.QUrl=...): ...
    @typing.overload
    def setQuery(self, sourceCode:str, documentURI:PySide2.QtCore.QUrl=...): ...
    def setUriResolver(self, resolver:PySide2.QtXmlPatterns.QAbstractUriResolver): ...
    def uriResolver(self) -> PySide2.QtXmlPatterns.QAbstractUriResolver: ...


class QXmlResultItems(Shiboken.Object):

    def __init__(self): ...

    def current(self) -> PySide2.QtXmlPatterns.QXmlItem: ...
    def hasError(self) -> bool: ...
    def next(self) -> PySide2.QtXmlPatterns.QXmlItem: ...


class QXmlSchema(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtXmlPatterns.QXmlSchema): ...

    def documentUri(self) -> PySide2.QtCore.QUrl: ...
    def isValid(self) -> bool: ...
    @typing.overload
    def load(self, data:PySide2.QtCore.QByteArray, documentUri:PySide2.QtCore.QUrl=...) -> bool: ...
    @typing.overload
    def load(self, source:PySide2.QtCore.QIODevice, documentUri:PySide2.QtCore.QUrl=...) -> bool: ...
    @typing.overload
    def load(self, source:PySide2.QtCore.QUrl) -> bool: ...
    def messageHandler(self) -> PySide2.QtXmlPatterns.QAbstractMessageHandler: ...
    def namePool(self) -> PySide2.QtXmlPatterns.QXmlNamePool: ...
    def setMessageHandler(self, handler:PySide2.QtXmlPatterns.QAbstractMessageHandler): ...
    def setUriResolver(self, resolver:PySide2.QtXmlPatterns.QAbstractUriResolver): ...
    def uriResolver(self) -> PySide2.QtXmlPatterns.QAbstractUriResolver: ...


class QXmlSchemaValidator(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, schema:PySide2.QtXmlPatterns.QXmlSchema): ...

    def messageHandler(self) -> PySide2.QtXmlPatterns.QAbstractMessageHandler: ...
    def namePool(self) -> PySide2.QtXmlPatterns.QXmlNamePool: ...
    def schema(self) -> PySide2.QtXmlPatterns.QXmlSchema: ...
    def setMessageHandler(self, handler:PySide2.QtXmlPatterns.QAbstractMessageHandler): ...
    def setSchema(self, schema:PySide2.QtXmlPatterns.QXmlSchema): ...
    def setUriResolver(self, resolver:PySide2.QtXmlPatterns.QAbstractUriResolver): ...
    def uriResolver(self) -> PySide2.QtXmlPatterns.QAbstractUriResolver: ...
    @typing.overload
    def validate(self, data:PySide2.QtCore.QByteArray, documentUri:PySide2.QtCore.QUrl=...) -> bool: ...
    @typing.overload
    def validate(self, source:PySide2.QtCore.QIODevice, documentUri:PySide2.QtCore.QUrl=...) -> bool: ...
    @typing.overload
    def validate(self, source:PySide2.QtCore.QUrl) -> bool: ...


class QXmlSerializer(PySide2.QtXmlPatterns.QAbstractXmlReceiver):

    def __init__(self, query:PySide2.QtXmlPatterns.QXmlQuery, outputDevice:PySide2.QtCore.QIODevice): ...

    def atomicValue(self, value:typing.Any): ...
    def attribute(self, name:PySide2.QtXmlPatterns.QXmlName, value:str): ...
    def characters(self, value:str): ...
    def codec(self) -> PySide2.QtCore.QTextCodec: ...
    def comment(self, value:str): ...
    def endDocument(self): ...
    def endElement(self): ...
    def endOfSequence(self): ...
    def namespaceBinding(self, nb:PySide2.QtXmlPatterns.QXmlName): ...
    def outputDevice(self) -> PySide2.QtCore.QIODevice: ...
    def processingInstruction(self, name:PySide2.QtXmlPatterns.QXmlName, value:str): ...
    def setCodec(self, codec:PySide2.QtCore.QTextCodec): ...
    def startDocument(self): ...
    def startElement(self, name:PySide2.QtXmlPatterns.QXmlName): ...
    def startOfSequence(self): ...

# eof
