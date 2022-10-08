# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ImageBlurHashes1(object):

    """Implementation of the 'ImageBlurHashes1' model.

    Gets or sets the blurhashes for the image tags.
    Maps image type to dictionary mapping image tag to blurhash value.

    Attributes:
        primary (dict): TODO: type description here.
        art (dict): TODO: type description here.
        backdrop (dict): TODO: type description here.
        banner (dict): TODO: type description here.
        logo (dict): TODO: type description here.
        thumb (dict): TODO: type description here.
        disc (dict): TODO: type description here.
        box (dict): TODO: type description here.
        screenshot (dict): TODO: type description here.
        menu (dict): TODO: type description here.
        chapter (dict): TODO: type description here.
        box_rear (dict): TODO: type description here.
        profile (dict): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "primary": "Primary",
        "art": "Art",
        "backdrop": "Backdrop",
        "banner": "Banner",
        "logo": "Logo",
        "thumb": "Thumb",
        "disc": "Disc",
        "box": "Box",
        "screenshot": "Screenshot",
        "menu": "Menu",
        "chapter": "Chapter",
        "box_rear": "BoxRear",
        "profile": "Profile",
    }

    _optionals = [
        "primary",
        "art",
        "backdrop",
        "banner",
        "logo",
        "thumb",
        "disc",
        "box",
        "screenshot",
        "menu",
        "chapter",
        "box_rear",
        "profile",
    ]

    def __init__(
        self,
        primary=APIHelper.SKIP,
        art=APIHelper.SKIP,
        backdrop=APIHelper.SKIP,
        banner=APIHelper.SKIP,
        logo=APIHelper.SKIP,
        thumb=APIHelper.SKIP,
        disc=APIHelper.SKIP,
        box=APIHelper.SKIP,
        screenshot=APIHelper.SKIP,
        menu=APIHelper.SKIP,
        chapter=APIHelper.SKIP,
        box_rear=APIHelper.SKIP,
        profile=APIHelper.SKIP,
    ):
        """Constructor for the ImageBlurHashes1 class"""

        # Initialize members of the class
        if primary is not APIHelper.SKIP:
            self.primary = primary
        if art is not APIHelper.SKIP:
            self.art = art
        if backdrop is not APIHelper.SKIP:
            self.backdrop = backdrop
        if banner is not APIHelper.SKIP:
            self.banner = banner
        if logo is not APIHelper.SKIP:
            self.logo = logo
        if thumb is not APIHelper.SKIP:
            self.thumb = thumb
        if disc is not APIHelper.SKIP:
            self.disc = disc
        if box is not APIHelper.SKIP:
            self.box = box
        if screenshot is not APIHelper.SKIP:
            self.screenshot = screenshot
        if menu is not APIHelper.SKIP:
            self.menu = menu
        if chapter is not APIHelper.SKIP:
            self.chapter = chapter
        if box_rear is not APIHelper.SKIP:
            self.box_rear = box_rear
        if profile is not APIHelper.SKIP:
            self.profile = profile

    @classmethod
    def from_dictionary(cls, dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        primary = (
            dictionary.get("Primary") if dictionary.get("Primary") else APIHelper.SKIP
        )
        art = dictionary.get("Art") if dictionary.get("Art") else APIHelper.SKIP
        backdrop = (
            dictionary.get("Backdrop") if dictionary.get("Backdrop") else APIHelper.SKIP
        )
        banner = (
            dictionary.get("Banner") if dictionary.get("Banner") else APIHelper.SKIP
        )
        logo = dictionary.get("Logo") if dictionary.get("Logo") else APIHelper.SKIP
        thumb = dictionary.get("Thumb") if dictionary.get("Thumb") else APIHelper.SKIP
        disc = dictionary.get("Disc") if dictionary.get("Disc") else APIHelper.SKIP
        box = dictionary.get("Box") if dictionary.get("Box") else APIHelper.SKIP
        screenshot = (
            dictionary.get("Screenshot")
            if dictionary.get("Screenshot")
            else APIHelper.SKIP
        )
        menu = dictionary.get("Menu") if dictionary.get("Menu") else APIHelper.SKIP
        chapter = (
            dictionary.get("Chapter") if dictionary.get("Chapter") else APIHelper.SKIP
        )
        box_rear = (
            dictionary.get("BoxRear") if dictionary.get("BoxRear") else APIHelper.SKIP
        )
        profile = (
            dictionary.get("Profile") if dictionary.get("Profile") else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            primary,
            art,
            backdrop,
            banner,
            logo,
            thumb,
            disc,
            box,
            screenshot,
            menu,
            chapter,
            box_rear,
            profile,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        primary = XmlUtilities.dict_from_xml_element(root.find("Primary"), dict)

        art = XmlUtilities.dict_from_xml_element(root.find("Art"), dict)

        backdrop = XmlUtilities.dict_from_xml_element(root.find("Backdrop"), dict)

        banner = XmlUtilities.dict_from_xml_element(root.find("Banner"), dict)

        logo = XmlUtilities.dict_from_xml_element(root.find("Logo"), dict)

        thumb = XmlUtilities.dict_from_xml_element(root.find("Thumb"), dict)

        disc = XmlUtilities.dict_from_xml_element(root.find("Disc"), dict)

        box = XmlUtilities.dict_from_xml_element(root.find("Box"), dict)

        screenshot = XmlUtilities.dict_from_xml_element(root.find("Screenshot"), dict)

        menu = XmlUtilities.dict_from_xml_element(root.find("Menu"), dict)

        chapter = XmlUtilities.dict_from_xml_element(root.find("Chapter"), dict)

        box_rear = XmlUtilities.dict_from_xml_element(root.find("BoxRear"), dict)

        profile = XmlUtilities.dict_from_xml_element(root.find("Profile"), dict)

        return cls(
            primary,
            art,
            backdrop,
            banner,
            logo,
            thumb,
            disc,
            box,
            screenshot,
            menu,
            chapter,
            box_rear,
            profile,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_dict_as_subelement(
            root, self.primary, dictionary_name="Primary"
        )
        XmlUtilities.add_dict_as_subelement(root, self.art, dictionary_name="Art")
        XmlUtilities.add_dict_as_subelement(
            root, self.backdrop, dictionary_name="Backdrop"
        )
        XmlUtilities.add_dict_as_subelement(root, self.banner, dictionary_name="Banner")
        XmlUtilities.add_dict_as_subelement(root, self.logo, dictionary_name="Logo")
        XmlUtilities.add_dict_as_subelement(root, self.thumb, dictionary_name="Thumb")
        XmlUtilities.add_dict_as_subelement(root, self.disc, dictionary_name="Disc")
        XmlUtilities.add_dict_as_subelement(root, self.box, dictionary_name="Box")
        XmlUtilities.add_dict_as_subelement(
            root, self.screenshot, dictionary_name="Screenshot"
        )
        XmlUtilities.add_dict_as_subelement(root, self.menu, dictionary_name="Menu")
        XmlUtilities.add_dict_as_subelement(
            root, self.chapter, dictionary_name="Chapter"
        )
        XmlUtilities.add_dict_as_subelement(
            root, self.box_rear, dictionary_name="BoxRear"
        )
        XmlUtilities.add_dict_as_subelement(
            root, self.profile, dictionary_name="Profile"
        )
