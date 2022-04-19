# Auto generated from test.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-04-19T10:34:41
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
version = None

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
class slots:
    pass

slots.curie = Slot(uri=DEFAULT_.curie, name="curie", curie=DEFAULT_.curie('curie'),
                   model_uri=DEFAULT_.curie, domain=None, range=URIRef)

slots.summary = Slot(uri=DEFAULT_.summary, name="summary", curie=DEFAULT_.curie('summary'),
                   model_uri=DEFAULT_.summary, domain=InformationContentEntity, range=Optional[str])

slots.copyright_date = Slot(uri=DEFAULT_.copyright_date, name="copyright_date", curie=DEFAULT_.curie('copyright_date'),
                   model_uri=DEFAULT_.copyright_date, domain=InformationContentEntity, range=Optional[Union[str, XSDDate]])

slots.corresponding_author = Slot(uri=DEFAULT_.corresponding_author, name="corresponding_author", curie=DEFAULT_.curie('corresponding_author'),
                   model_uri=DEFAULT_.corresponding_author, domain=InformationContentEntity, range=Optional[Union[str, InformationContentEntityCurie]])

slots.first_name = Slot(uri=DEFAULT_.first_name, name="first_name", curie=DEFAULT_.curie('first_name'),
                   model_uri=DEFAULT_.first_name, domain=InformationContentEntity, range=Optional[Union[str, InformationContentEntityCurie]])

slots.middle_name = Slot(uri=DEFAULT_.middle_name, name="middle_name", curie=DEFAULT_.curie('middle_name'),
                   model_uri=DEFAULT_.middle_name, domain=InformationContentEntity, range=Optional[Union[str, InformationContentEntityCurie]])

slots.last_name = Slot(uri=DEFAULT_.last_name, name="last_name", curie=DEFAULT_.curie('last_name'),
                   model_uri=DEFAULT_.last_name, domain=InformationContentEntity, range=Optional[Union[str, InformationContentEntityCurie]])

slots.initials = Slot(uri=DEFAULT_.initials, name="initials", curie=DEFAULT_.curie('initials'),
                   model_uri=DEFAULT_.initials, domain=InformationContentEntity, range=Optional[Union[str, InformationContentEntityCurie]])

slots.title = Slot(uri=DEFAULT_.title, name="title", curie=DEFAULT_.curie('title'),
                   model_uri=DEFAULT_.title, domain=InformationContentEntity, range=Optional[str])

slots.volumes = Slot(uri=DEFAULT_.volumes, name="volumes", curie=DEFAULT_.curie('volumes'),
                   model_uri=DEFAULT_.volumes, domain=InformationContentEntity, range=Optional[str])

slots.publisher = Slot(uri=DEFAULT_.publisher, name="publisher", curie=DEFAULT_.curie('publisher'),
                   model_uri=DEFAULT_.publisher, domain=InformationContentEntity, range=Optional[Union[str, InformationContentEntityCurie]])

slots.address = Slot(uri=DEFAULT_.address, name="address", curie=DEFAULT_.curie('address'),
                   model_uri=DEFAULT_.address, domain=None, range=Optional[str])

slots.iso_abbreviation = Slot(uri=DEFAULT_.iso_abbreviation, name="iso_abbreviation", curie=DEFAULT_.curie('iso_abbreviation'),
                   model_uri=DEFAULT_.iso_abbreviation, domain=Resource, range=Optional[str])

slots.medline_abbreviation = Slot(uri=DEFAULT_.medline_abbreviation, name="medline_abbreviation", curie=DEFAULT_.curie('medline_abbreviation'),
                   model_uri=DEFAULT_.medline_abbreviation, domain=Resource, range=Optional[str])

slots.print_issn = Slot(uri=DEFAULT_.print_issn, name="print_issn", curie=DEFAULT_.curie('print_issn'),
                   model_uri=DEFAULT_.print_issn, domain=Resource, range=Optional[str])

slots.online_issn = Slot(uri=DEFAULT_.online_issn, name="online_issn", curie=DEFAULT_.curie('online_issn'),
                   model_uri=DEFAULT_.online_issn, domain=Resource, range=Optional[str])

slots.id = Slot(uri=DEFAULT_.id, name="id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.id, domain=None, range=Optional[str])

slots.Resource_id = Slot(uri=DEFAULT_.id, name="Resource_id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.Resource_id, domain=Resource, range=Optional[str])

slots.Resource_title = Slot(uri=DEFAULT_.title, name="Resource_title", curie=DEFAULT_.curie('title'),
                   model_uri=DEFAULT_.Resource_title, domain=Resource, range=Optional[str])
