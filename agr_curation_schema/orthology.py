# Auto generated from orthology.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-12-13 16:39
# Schema: Alliance-Schema-Orthology-Term
#
# id: https://github.com/alliance-genome/agr_curation_schema/ontologyTerm
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
from . core import GeneCurie
from . reference import ReferenceCurie
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
WIKIDATA_PROPERTY = CurieNamespace('WIKIDATA_PROPERTY', 'https://www.wikidata.org/wiki/Property:')
ALLIANCE = CurieNamespace('alliance', 'http://alliancegenome.org')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OBOGRAPH = CurieNamespace('obograph', 'https://github.com/biodatamodels/obograph')
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_curation_schema/ontologyTerm/')


# Types

# Class references



@dataclass
class GeneToGeneOrthology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm/GeneToGeneOrthology")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "GeneToGeneOrthology"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm/GeneToGeneOrthology")

    predicate: str = None
    gene_subject: Optional[Union[str, GeneCurie]] = None
    gene_object: Optional[Union[str, GeneCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self.gene_subject is not None and not isinstance(self.gene_subject, GeneCurie):
            self.gene_subject = GeneCurie(self.gene_subject)

        if self.gene_object is not None and not isinstance(self.gene_object, GeneCurie):
            self.gene_object = GeneCurie(self.gene_object)

        super().__post_init__(**kwargs)


@dataclass
class GeneToGeneOrthologyCurated(GeneToGeneOrthology):
    """
    Class that holds the properties necessary to store a curated orthology record.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm/GeneToGeneOrthologyCurated")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "GeneToGeneOrthologyCurated"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm/GeneToGeneOrthologyCurated")

    predicate: str = None
    has_reference: Optional[Union[str, ReferenceCurie]] = None
    evidence_code: Optional[Union[str, "EvidenceCodeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_reference is not None and not isinstance(self.has_reference, ReferenceCurie):
            self.has_reference = ReferenceCurie(self.has_reference)

        if self.evidence_code is not None and not isinstance(self.evidence_code, EvidenceCodeEnum):
            self.evidence_code = EvidenceCodeEnum(self.evidence_code)

        super().__post_init__(**kwargs)


@dataclass
class GeneToGeneOrthologyGenerated(GeneToGeneOrthology):
    """
    Class that holds the properties necessary to record an orthology record from DIOPT
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm/GeneToGeneOrthologyGenerated")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "GeneToGeneOrthologyGenerated"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm/GeneToGeneOrthologyGenerated")

    predicate: str = None
    is_best_score: Optional[str] = None
    is_best_reverse_score: Optional[str] = None
    confidence: Optional[str] = None
    strict_filter: Optional[str] = None
    moderate_filter: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.is_best_score is not None and not isinstance(self.is_best_score, str):
            self.is_best_score = str(self.is_best_score)

        if self.is_best_reverse_score is not None and not isinstance(self.is_best_reverse_score, str):
            self.is_best_reverse_score = str(self.is_best_reverse_score)

        if self.confidence is not None and not isinstance(self.confidence, str):
            self.confidence = str(self.confidence)

        if self.strict_filter is not None and not isinstance(self.strict_filter, str):
            self.strict_filter = str(self.strict_filter)

        if self.moderate_filter is not None and not isinstance(self.moderate_filter, str):
            self.moderate_filter = str(self.moderate_filter)

        super().__post_init__(**kwargs)


# Enumerations
class EvidenceCodeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EvidenceCodeEnum",
    )

# Slots

