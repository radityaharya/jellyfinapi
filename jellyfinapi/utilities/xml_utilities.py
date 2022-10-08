# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import datetime
import dateutil.parser

from jellyfinapi.api_helper import APIHelper


class XmlUtilities:
    """This class hold utility methods for xml serialization and
    deserialization.
    """

    @staticmethod
    def serialize_to_xml(value, root_element_name):
        """Serializes a given value to an xml document.

        Args:
            value (mixed): The value to serialize.
            root_element_name (str): The name of the document's root element.
        """
        root = ET.Element(root_element_name)

        if value is not None:
            XmlUtilities.add_to_element(root, value)

        return ET.tostring(root).decode()

    @staticmethod
    def serialize_list_to_xml(value, root_element_name, array_item_name):
        """Serializes a given list of values to an xml document.

        Args:
            value (mixed): The value to serialize.
            root_element_name (str): The name of the document's root element.
            array_item_name (str): The element name to use for each item in
                'values'.
        """
        root = ET.Element(root_element_name)

        XmlUtilities.add_list_as_subelement(root, value, array_item_name)

        return ET.tostring(root).decode()

    @staticmethod
    def serialize_dict_to_xml(value, root_element_name):
        """Serializes a given dict of values to an xml document.

        Args:
            value (mixed): The dict to serialize.
            root_element_name (str): The name of the document's root element.
        """
        root = ET.Element(root_element_name)

        XmlUtilities.add_dict_as_subelement(root, value)

        return ET.tostring(root).decode()

    @staticmethod
    def add_to_element(element, value):
        """Converts the given value to xml and adds it to an
            existing xml.etree.Element.

        Args:
            element (xml.etree.Element): The xml tag to add the 'value' to.
            value (mixed): The value to add to the element.
        """
        # These classes can be cast directly.
        if isinstance(value, bool):
            element.text = str(value).lower()
        elif isinstance(value, (int, float, str, datetime.date, APIHelper.CustomDate)):
            element.text = str(value)
        else:
            value.to_xml_sub_element(element)

    @staticmethod
    def add_as_attribute(root, value, name):
        """Sets an attribute on an xml.etree.Element instance if the value
            isn't None.

        Args:
            root (xml.etree.Element): The parent of this xml attribute.
            value (mixed): The value to set to the attribute.
            name (str): The name of attribute being set.
        """
        if value is not None:
            if isinstance(value, bool):
                root.set(name, str(value).lower())
            else:
                root.set(name, str(value))

    @staticmethod
    def add_as_subelement(root, value, name):
        """Converts the given value to an xml.etree.Element if it is not None
            and adds it to an existing xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
            value (mixed): The value to add to the element.
            name (str): The name of the element being added.
        """
        if value is not None:
            tag = ET.SubElement(root, name)
            XmlUtilities.add_to_element(tag, value)

    @staticmethod
    def add_list_as_subelement(root, items, item_name, wrapping_element_name=None):
        """Converts the given list to an xml.etree.Element if it is not None
            and adds it to an existing xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
            items (list): The list of values to add to the element.
            item_name (str): The element name to use for each item in 'items'.
            wrapping_element_name (str): The element name to use for the
                wrapping element, if needed.
        """
        if items is not None:
            if wrapping_element_name is not None:
                parent = ET.SubElement(root, wrapping_element_name)
            else:
                parent = root

            for item in items:
                sub_elem = ET.SubElement(parent, item_name)
                XmlUtilities.add_to_element(sub_elem, item)

    @staticmethod
    def add_dict_as_subelement(root, items, dictionary_name=None):
        """Converts the given dict to an xml.etree.Element if it is not None
            and adds it to an existing xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
            items (dict): The dict of values to add to the element.
            dictionary_name (str): The element name to use for the
                encapsulating element.
        """
        if items is not None:
            if dictionary_name is not None:
                parent = ET.SubElement(root, dictionary_name)
            else:
                parent = root

            for key, value in items.items():
                if isinstance(value, list):
                    XmlUtilities.add_list_as_subelement(parent, value, key)
                else:
                    XmlUtilities.add_as_subelement(parent, value, key)

    @staticmethod
    def deserialize_xml(xml, root_element_name, clazz):
        """Deserializes an xml document to a python object of the type given
            by 'clazz'.

        Args:
            xml (str): An xml document to deserialize.
            root_element_name (str): The name of the xml document's root
                element.
            clazz (class): The class that the deserialized object should
                belong to.
        """
        if not xml:
            return None

        root = ET.fromstring(xml)

        return XmlUtilities.value_from_xml_element(root, clazz)

    @staticmethod
    def deserialize_xml_to_list(xml, root_element_name, item_name, clazz):
        """Deserializes an xml document to a list of python objects, each of
            the type given by 'clazz'.

        Args:
            xml (str): An xml document to deserialize.
            root_element_name (str): The name of the xml document's root
                element.
            item_name (str): The name of the elements that need to be extracted
                into a list.
            clazz (class): The class that the deserialized object should
                belong to.
        """
        if not xml:
            return None

        root = ET.fromstring(xml)

        if root is None:
            return None

        return XmlUtilities.list_from_xml_element(root, item_name, clazz)

    @staticmethod
    def deserialize_xml_to_dict(xml, root_element_name, clazz):
        """Deserializes an xml document to a list of python objects, each of
            the type given by 'clazz'.

        Args:
            xml (str): An xml document to deserialize.
            root_element_name (str): The name of the xml document's root
                element.
            clazz (class): The class that the values of the dictionary should
                belong to.
        """
        if not xml:
            return None

        root = ET.fromstring(xml)
        return XmlUtilities.dict_from_xml_element(root, clazz)

    @staticmethod
    def value_from_xml_attribute(attribute, clazz):
        """Extracts the value from an attribute and converts it to the type
            given by 'clazz'.

        Args:
            clazz (class): The class that the deserialized object should
                belong to.
        """
        if attribute is None:
            return None

        if clazz in [int, float, str, bool, datetime.date] or issubclass(
            clazz, APIHelper.CustomDate
        ):
            conversion_function = XmlUtilities.converter(clazz)
        else:
            conversion_function = str(clazz)

        return conversion_function(attribute)

    @staticmethod
    def value_from_xml_element(element, clazz):
        """Extracts the value from an element and converts it to the type given
            by 'clazz'.

        Args:
            clazz (class): The class that the deserialized object should
                belong to.
        """
        if element is None:
            return None

        # These classes can be cast directly.
        if clazz in [int, float, str, bool, datetime.date] or issubclass(
            clazz, APIHelper.CustomDate
        ):
            conversion_function = XmlUtilities.converter(clazz)
            value = element.text
        else:
            conversion_function = clazz.from_element
            value = element

        return conversion_function(value)

    @staticmethod
    def list_from_xml_element(root, item_name, clazz, wrapping_element_name=None):
        """Deserializes an xml document to a list of python objects, each of
            the type given by 'clazz'.

        Args:
            root (str): An xml document to deserialize.
            item_name (str): The name of the elements that need to be extracted
                into a list.
            clazz (class): The class that the deserialized object should
                belong to.
            wrapping_element_name (str): The name of the wrapping element for
                the xml element array.
        """
        if wrapping_element_name is None:
            elements = root.findall(item_name)
        elif root.find(wrapping_element_name) is None:
            elements = None
        else:
            elements = root.find(wrapping_element_name).findall(item_name)

        if elements is None:
            return None

        return [
            XmlUtilities.value_from_xml_element(element, clazz) for element in elements
        ]

    @staticmethod
    def dict_from_xml_element(element, clazz):
        """Extracts the values from an element and converts them to a
            dictionary with values of type 'clazz'.

        Args:
            clazz (class): The class that the entries of the dictionary should
                belong to.
        """
        if element is None:
            return None

        entries = list(element)

        conversion_function = XmlUtilities.converter(clazz)
        return {entry.tag: conversion_function(entry.text) for entry in entries}

    @staticmethod
    def converter(clazz):
        """Provides the function to use for converting a string to the type
            given by 'clazz'.

        Args:
            clazz (class): The class to find the conversion function for.
        """
        # These classes can be cast directly.
        if clazz in [int, float, str]:

            def conversion_function(value):
                return clazz(value)

        elif clazz is bool:

            def conversion_function(value):
                return value.lower() == "true"

        elif clazz is datetime.date:

            def conversion_function(value):
                return dateutil.parser.parse(value).date()

        # DateTime classes have their own method to convert from string.
        elif issubclass(clazz, APIHelper.CustomDate):

            def conversion_function(value):
                return clazz.from_value(value)

        return conversion_function

    @staticmethod
    def value_from_one_of_xml_elements(root, mapping_data):
        """Extracts the value from an element and converts it to the type given
            by 'clazz'.

        Args:
            mapping_data (dict): A dictionary mapping possible element names
            for a given field to corresponding types.
        """
        for element_name, tup in mapping_data.items():
            clazz = tup[0]
            is_array = tup[1]
            wrapping_element_name = tup[2]
            if is_array:
                if wrapping_element_name is None:
                    elements = root.findall(element_name)
                elif root.find(wrapping_element_name) is None:
                    elements = None
                else:
                    elements = root.find(wrapping_element_name).findall(element_name)
                if elements is not None and len(elements) > 0:
                    return XmlUtilities.list_from_xml_element(
                        root, element_name, clazz, wrapping_element_name
                    )
            else:
                element = root.find(element_name)
                if element is not None:
                    return XmlUtilities.value_from_xml_element(element, clazz)

        return None

    @staticmethod
    def list_from_multiple_one_of_xml_element(root, mapping_data):
        """Deserializes an xml document to a list of python objects
           where all types of oneof schemas are allowed (when the outer
           model is an array)

        Args:
            root (str): An xml document to deserialize.
            mapping_data (dict): A dictionary mapping possible element names
            for a given field to corresponding types.

        """
        arr = []
        for elem in root.iter():
            if elem.tag in mapping_data:
                arr.append(
                    XmlUtilities.value_from_xml_element(elem, mapping_data[elem.tag][0])
                )
        if len(arr) > 0:
            return arr
        else:
            return None
