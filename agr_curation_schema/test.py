# Auto generated from test.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-11-16 23:00
# Schema: resource
#
# id: https://github.com/alliance-genome/agr_curation_schema/src/schema/resource
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Date, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DOI = CurieNamespace('DOI', 'http://example.org/UNKNOWN/DOI/')
FB = CurieNamespace('FB', 'http://example.org/UNKNOWN/FB/')
IAO = CurieNamespace('IAO', 'http://example.org/UNKNOWN/IAO/')
MGI = CurieNamespace('MGI', 'http://example.org/UNKNOWN/MGI/')
NLMID = CurieNamespace('NLMID', 'https://www.ncbi.nlm.nih.gov/nlmcatalog/?term=')
PMID = CurieNamespace('PMID', 'http://example.org/UNKNOWN/PMID/')
RGD = CurieNamespace('RGD', 'http://example.org/UNKNOWN/RGD/')
SGD = CurieNamespace('SGD', 'http://example.org/UNKNOWN/SGD/')
WB = CurieNamespace('WB', 'http://example.org/UNKNOWN/WB/')
ZFIN = CurieNamespace('ZFIN', 'http://example.org/UNKNOWN/ZFIN/')
ALLIANCE = CurieNamespace('alliance', 'http://alliancegenome.org')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
FALDO = CurieNamespace('faldo', 'http://biohackathon.org/resource/faldo#')
GFF = CurieNamespace('gff', 'https://w3id.org/gff')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_curation_schema/src/schema/resource/')


# Types

# Class references
class InformationContentEntityCurie(URIorCURIE):
    pass


class ResourceCurie(InformationContentEntityCurie):
    pass


@dataclass
class InformationContentEntity(YAMLRoot):
    """
    a piece of information that typically describes some topic of discourse or is used as support. Precedence of
    identifiers for references is as follows: PMID if available; DOI if not; actual alternate CURIE otherwise.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/resource/InformationContentEntity")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "InformationContentEntity"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/resource/InformationContentEntity")

    curie: Union[str, InformationContentEntityCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, InformationContentEntityCurie):
            self.curie = InformationContentEntityCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class AuthorReference(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/resource/AuthorReference")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AuthorReference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/resource/AuthorReference")

    first_name: Optional[Union[str, InformationContentEntityCurie]] = None
    middle_names: Optional[Union[str, InformationContentEntityCurie]] = None
    last_name: Optional[Union[str, InformationContentEntityCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.first_name is not None and not isinstance(self.first_name, InformationContentEntityCurie):
            self.first_name = InformationContentEntityCurie(self.first_name)

        if self.middle_names is not None and not isinstance(self.middle_names, InformationContentEntityCurie):
            self.middle_names = InformationContentEntityCurie(self.middle_names)

        if self.last_name is not None and not isinstance(self.last_name, InformationContentEntityCurie):
            self.last_name = InformationContentEntityCurie(self.last_name)

        super().__post_init__(**kwargs)


@dataclass
class Resource(InformationContentEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/resource/Resource")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/resource/Resource")

    curie: Union[str, ResourceCurie] = None
    title: Optional[str] = None
    id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ResourceCurie):
            self.curie = ResourceCurie(self.curie)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        super().__post_init__(**kwargs)


# Enumerations


# Slots

