# Auto generated from informationContentEntity.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-05-25 15:14
# Schema: informationContentEntity
#
# id: https://github.com/alliance-genome/agr_persistent_schema/informationContentEntity
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj
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
NLMID = CurieNamespace('NLMID', 'https://www.ncbi.nlm.nih.gov/nlmcatalog/?term=')
ALLIANCE = CurieNamespace('alliance', 'http://alliancegenome.org')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
FALDO = CurieNamespace('faldo', 'http://biohackathon.org/resource/faldo#')
GFF = CurieNamespace('gff', 'https://w3id.org/gff')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'https://www.w3.org/TR/skos-reference/#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ALLIANCE


# Types

# Class references
class InformationContentEntityId(URIorCURIE):
    pass


@dataclass
class InformationContentEntity(YAMLRoot):
    """
    a piece of information that typically describes some topic of discourse or is used as support. Precedence of
    identifiers for references is as follows: PMID if available; DOI if not; actual alternate CURIE otherwise.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.InformationContentEntity
    class_class_curie: ClassVar[str] = "alliance:InformationContentEntity"
    class_name: ClassVar[str] = "InformationContentEntity"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.InformationContentEntity

    id: Union[str, InformationContentEntityId] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    curie: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            raise ValueError("id must be supplied")
        if not isinstance(self.id, InformationContentEntityId):
            self.id = InformationContentEntityId(self.id)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.curie is not None and not isinstance(self.curie, str):
            self.curie = str(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class AuthorReference(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AuthorReference
    class_class_curie: ClassVar[str] = "alliance:AuthorReference"
    class_name: ClassVar[str] = "AuthorReference"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AuthorReference

    corresponding_author: Optional[Union[str, InformationContentEntityId]] = None
    first_name: Optional[Union[str, InformationContentEntityId]] = None
    middle_names: Optional[Union[str, InformationContentEntityId]] = None
    last_name: Optional[Union[str, InformationContentEntityId]] = None
    initials: Optional[Union[str, InformationContentEntityId]] = None
    cross_references: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.corresponding_author is not None and not isinstance(self.corresponding_author, InformationContentEntityId):
            self.corresponding_author = InformationContentEntityId(self.corresponding_author)

        if self.first_name is not None and not isinstance(self.first_name, InformationContentEntityId):
            self.first_name = InformationContentEntityId(self.first_name)

        if self.middle_names is not None and not isinstance(self.middle_names, InformationContentEntityId):
            self.middle_names = InformationContentEntityId(self.middle_names)

        if self.last_name is not None and not isinstance(self.last_name, InformationContentEntityId):
            self.last_name = InformationContentEntityId(self.last_name)

        if self.initials is not None and not isinstance(self.initials, InformationContentEntityId):
            self.initials = InformationContentEntityId(self.initials)

        if not isinstance(self.cross_references, list):
            self.cross_references = [self.cross_references]
        self.cross_references = [v if isinstance(v, str) else str(v) for v in self.cross_references]

        super().__post_init__(**kwargs)


# Enumerations


# Slots

