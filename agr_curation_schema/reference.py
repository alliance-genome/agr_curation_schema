# Auto generated from reference.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-11-16 23:00
# Schema: reference
#
# id: https://github.com/alliance-genome/agr_curation_schema/src/schema/reference
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
from . core import CrossReferenceCurie
from . informationContentEntity import AuthorReference, InformationContentEntity, InformationContentEntityCurie
from . person import PersonPersonId
from . resource import ResourceCurie
from linkml_runtime.linkml_model.types import Date, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DOI = CurieNamespace('DOI', 'http://identifiers.org/doi/')
FB = CurieNamespace('FB', 'http://identifiers.org/fb/')
MGI = CurieNamespace('MGI', 'http://identifiers.org/mgi/')
NLMID = CurieNamespace('NLMID', 'https://www.ncbi.nlm.nih.gov/nlmcatalog/?term=')
PMC = CurieNamespace('PMC', 'http://identifiers.org/pmc/')
PMID = CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/')
RGD = CurieNamespace('RGD', 'http://identifiers.org/rgd/')
SGD = CurieNamespace('SGD', 'http://identifiers.org/sgd/')
WB = CurieNamespace('WB', 'http://identifiers.org/wb/')
WIKIDATA_PROPERTY = CurieNamespace('WIKIDATA_PROPERTY', 'https://www.wikidata.org/wiki/Property:')
ZFIN = CurieNamespace('ZFIN', 'http://identifiers.org/zfin/')
ALLIANCE = CurieNamespace('alliance', 'http://alliancegenome.org')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
FALDO = CurieNamespace('faldo', 'http://biohackathon.org/resource/faldo#')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
GFF = CurieNamespace('gff', 'https://w3id.org/gff')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_curation_schema/src/schema/reference/')


# Types

# Class references
class ReferenceCurie(InformationContentEntityCurie):
    pass


@dataclass
class Reference(InformationContentEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/reference/Reference")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Reference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/reference/Reference")

    curie: Union[str, ReferenceCurie] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    title: Optional[str] = None
    alliance_category: Optional[str] = None
    date_published: Optional[Union[str, XSDDate]] = None
    year_published: Optional[str] = None
    month_published: Optional[str] = None
    day_published: Optional[str] = None
    date_arrived_in_PubMed: Optional[Union[str, XSDDate]] = None
    date_last_modified_in_PubMed: Optional[Union[str, XSDDate]] = None
    volume: Optional[str] = None
    pages: Optional[Union[str, List[str]]] = empty_list()
    abstract: Optional[str] = None
    citation: Optional[str] = None
    PubMed_type: Optional[str] = None
    issue_name: Optional[str] = None
    issue_date: Optional[Union[str, XSDDate]] = None
    mod_reference_types: Optional[Union[str, List[str]]] = empty_list()
    authors: Optional[Union[Union[dict, AuthorReference], List[Union[dict, AuthorReference]]]] = empty_list()
    tags: Optional[Union[Union[str, "TagSet"], List[Union[str, "TagSet"]]]] = empty_list()
    topics: Optional[Union[str, URIorCURIE]] = None
    cross_references: Optional[Union[Union[str, CrossReferenceCurie], List[Union[str, CrossReferenceCurie]]]] = empty_list()
    publisher: Optional[Union[str, InformationContentEntityCurie]] = None
    keywords: Optional[Union[str, List[str]]] = empty_list()
    from_resource: Optional[Union[str, ResourceCurie]] = None
    id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ReferenceCurie):
            self.curie = ReferenceCurie(self.curie)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.alliance_category is not None and not isinstance(self.alliance_category, str):
            self.alliance_category = str(self.alliance_category)

        if self.date_published is not None and not isinstance(self.date_published, XSDDate):
            self.date_published = XSDDate(self.date_published)

        if self.year_published is not None and not isinstance(self.year_published, str):
            self.year_published = str(self.year_published)

        if self.month_published is not None and not isinstance(self.month_published, str):
            self.month_published = str(self.month_published)

        if self.day_published is not None and not isinstance(self.day_published, str):
            self.day_published = str(self.day_published)

        if self.date_arrived_in_PubMed is not None and not isinstance(self.date_arrived_in_PubMed, XSDDate):
            self.date_arrived_in_PubMed = XSDDate(self.date_arrived_in_PubMed)

        if self.date_last_modified_in_PubMed is not None and not isinstance(self.date_last_modified_in_PubMed, XSDDate):
            self.date_last_modified_in_PubMed = XSDDate(self.date_last_modified_in_PubMed)

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if not isinstance(self.pages, list):
            self.pages = [self.pages] if self.pages is not None else []
        self.pages = [v if isinstance(v, str) else str(v) for v in self.pages]

        if self.abstract is not None and not isinstance(self.abstract, str):
            self.abstract = str(self.abstract)

        if self.citation is not None and not isinstance(self.citation, str):
            self.citation = str(self.citation)

        if self.PubMed_type is not None and not isinstance(self.PubMed_type, str):
            self.PubMed_type = str(self.PubMed_type)

        if self.issue_name is not None and not isinstance(self.issue_name, str):
            self.issue_name = str(self.issue_name)

        if self.issue_date is not None and not isinstance(self.issue_date, XSDDate):
            self.issue_date = XSDDate(self.issue_date)

        if not isinstance(self.mod_reference_types, list):
            self.mod_reference_types = [self.mod_reference_types] if self.mod_reference_types is not None else []
        self.mod_reference_types = [v if isinstance(v, str) else str(v) for v in self.mod_reference_types]

        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, AuthorReference) else AuthorReference(**as_dict(v)) for v in self.authors]

        if not isinstance(self.tags, list):
            self.tags = [self.tags] if self.tags is not None else []
        self.tags = [v if isinstance(v, TagSet) else TagSet(v) for v in self.tags]

        if self.topics is not None and not isinstance(self.topics, URIorCURIE):
            self.topics = URIorCURIE(self.topics)

        if not isinstance(self.cross_references, list):
            self.cross_references = [self.cross_references] if self.cross_references is not None else []
        self.cross_references = [v if isinstance(v, CrossReferenceCurie) else CrossReferenceCurie(v) for v in self.cross_references]

        if self.publisher is not None and not isinstance(self.publisher, InformationContentEntityCurie):
            self.publisher = InformationContentEntityCurie(self.publisher)

        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords] if self.keywords is not None else []
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        if self.from_resource is not None and not isinstance(self.from_resource, ResourceCurie):
            self.from_resource = ResourceCurie(self.from_resource)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        super().__post_init__(**kwargs)


# Enumerations
class TagSet(EnumDefinitionImpl):

    image = PermissibleValue(text="image")
    test = PermissibleValue(text="test")

    _defn = EnumDefinition(
        name="TagSet",
    )

# Slots

