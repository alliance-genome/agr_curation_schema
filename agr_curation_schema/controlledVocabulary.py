# Auto generated from controlledVocabulary.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-12-13 16:38
# Schema: Alliance-Schema-Prototype-Controlled-Vocabulary
#
# id: https://github.com/alliance-genome/agr_curation_schema/controlledVocabulary.yaml
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
from . person import PersonPersonId
from linkml_runtime.linkml_model.types import Boolean, Date, Integer, String
from linkml_runtime.utils.metamodelcore import Bool, XSDDate

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ALLIANCE = CurieNamespace('alliance', 'http://alliancegenome.org')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OBOGRAPH = CurieNamespace('obograph', 'https://github.com/biodatamodels/obograph')
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_curation_schema/controlledVocabulary.yaml/')


# Types

# Class references
class VocabularyName(extended_str):
    pass


@dataclass
class VocabularyTerm(YAMLRoot):
    """
    A concept or class in a simple vocabulary.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/controlledVocabulary.yaml/VocabularyTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "VocabularyTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/controlledVocabulary.yaml/VocabularyTerm")

    name: str = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    definition: Optional[str] = None
    is_obsolete: Optional[Union[bool, Bool]] = None
    text_synonyms: Optional[Union[str, List[str]]] = empty_list()
    abbreviation: Optional[str] = None
    table_key: Optional[int] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.created_by):
            self.MissingRequiredField("created_by")
        if not isinstance(self.created_by, PersonPersonId):
            self.created_by = PersonPersonId(self.created_by)

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, PersonPersonId):
            self.modified_by = PersonPersonId(self.modified_by)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.is_obsolete is not None and not isinstance(self.is_obsolete, Bool):
            self.is_obsolete = Bool(self.is_obsolete)

        if not isinstance(self.text_synonyms, list):
            self.text_synonyms = [self.text_synonyms] if self.text_synonyms is not None else []
        self.text_synonyms = [v if isinstance(v, str) else str(v) for v in self.text_synonyms]

        if self.abbreviation is not None and not isinstance(self.abbreviation, str):
            self.abbreviation = str(self.abbreviation)

        if self.table_key is not None and not isinstance(self.table_key, int):
            self.table_key = int(self.table_key)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

        super().__post_init__(**kwargs)


@dataclass
class Vocabulary(YAMLRoot):
    """
    A set of VocabularyTerm objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/controlledVocabulary.yaml/Vocabulary")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Vocabulary"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/controlledVocabulary.yaml/Vocabulary")

    name: Union[str, VocabularyName] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    vocabulary_description: Optional[str] = None
    is_obsolete: Optional[Union[bool, Bool]] = None
    member_terms: Optional[Union[Union[dict, VocabularyTerm], List[Union[dict, VocabularyTerm]]]] = empty_list()
    table_key: Optional[int] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, VocabularyName):
            self.name = VocabularyName(self.name)

        if self._is_empty(self.created_by):
            self.MissingRequiredField("created_by")
        if not isinstance(self.created_by, PersonPersonId):
            self.created_by = PersonPersonId(self.created_by)

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, PersonPersonId):
            self.modified_by = PersonPersonId(self.modified_by)

        if self.vocabulary_description is not None and not isinstance(self.vocabulary_description, str):
            self.vocabulary_description = str(self.vocabulary_description)

        if self.is_obsolete is not None and not isinstance(self.is_obsolete, Bool):
            self.is_obsolete = Bool(self.is_obsolete)

        self._normalize_inlined_as_dict(slot_name="member_terms", slot_type=VocabularyTerm, key_name="name", keyed=False)

        if self.table_key is not None and not isinstance(self.table_key, int):
            self.table_key = int(self.table_key)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

        super().__post_init__(**kwargs)


# Enumerations


# Slots

