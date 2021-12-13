# Auto generated from variation.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-11-16 23:00
# Schema: Alliance-Schema-Prototype-Variation
#
# id: https://github.com/alliance-genome/agr_curation_schema/src/schema/variation
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
from . allele import AlleleCurie
from . core import BiologicalSequence, CrossReferenceCurie, GeneCurie, GenomicEntity, GenomicEntityCurie, Synonym, TranscriptCurie
from . person import PersonPersonId
from . reference import ReferenceCurie
from linkml_runtime.linkml_model.types import Date, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
NLMID = CurieNamespace('NLMID', 'https://www.ncbi.nlm.nih.gov/nlmcatalog/?term=')
SO = CurieNamespace('SO', 'http://purl.obolibrary.org/obo/SO_')
ALLIANCE = CurieNamespace('alliance', 'http://alliancegenome.org')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
FALDO = CurieNamespace('faldo', 'http://biohackathon.org/resource/faldo#')
GFF = CurieNamespace('gff', 'https://w3id.org/gff')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_curation_schema/src/schema/variation/')


# Types

# Class references
class VariantCurie(GenomicEntityCurie):
    pass


@dataclass
class Variant(GenomicEntity):
    """
    A DNA sequence that differs relative to a designated reference sequence. The sequence occurs at a single position
    or in contiguous nucleotides.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variation/Variant")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Variant"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variation/Variant")

    curie: Union[str, VariantCurie] = None
    taxon: Union[str, URIorCURIE] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    hgvs_nomenclature: Optional[str] = None
    genomic_reference_sequence: Optional[str] = None
    genomic_variant_sequence: Optional[str] = None
    padding_left: Optional[str] = None
    padding_right: Optional[Union[str, BiologicalSequence]] = None
    release: Optional[str] = None
    data_provider: Optional[Union[str, List[str]]] = empty_list()
    computed_gene: Optional[Union[str, GeneCurie]] = None
    variant_of_transcript: Optional[Union[str, TranscriptCurie]] = None
    variant_of_allele: Optional[Union[str, AlleleCurie]] = None
    synonyms: Optional[Union[Union[dict, Synonym], List[Union[dict, Synonym]]]] = empty_list()
    type: Optional[Union[str, URIorCURIE]] = None
    references: Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]] = empty_list()
    notes: Optional[Union[str, List[str]]] = empty_list()
    protein_sequence: Optional[str] = None
    cross_references: Optional[Union[Union[str, CrossReferenceCurie], List[Union[str, CrossReferenceCurie]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, VariantCurie):
            self.curie = VariantCurie(self.curie)

        if self.hgvs_nomenclature is not None and not isinstance(self.hgvs_nomenclature, str):
            self.hgvs_nomenclature = str(self.hgvs_nomenclature)

        if self.genomic_reference_sequence is not None and not isinstance(self.genomic_reference_sequence, str):
            self.genomic_reference_sequence = str(self.genomic_reference_sequence)

        if self.genomic_variant_sequence is not None and not isinstance(self.genomic_variant_sequence, str):
            self.genomic_variant_sequence = str(self.genomic_variant_sequence)

        if self.padding_left is not None and not isinstance(self.padding_left, str):
            self.padding_left = str(self.padding_left)

        if self.padding_right is not None and not isinstance(self.padding_right, BiologicalSequence):
            self.padding_right = BiologicalSequence(self.padding_right)

        if self.release is not None and not isinstance(self.release, str):
            self.release = str(self.release)

        if not isinstance(self.data_provider, list):
            self.data_provider = [self.data_provider] if self.data_provider is not None else []
        self.data_provider = [v if isinstance(v, str) else str(v) for v in self.data_provider]

        if self.computed_gene is not None and not isinstance(self.computed_gene, GeneCurie):
            self.computed_gene = GeneCurie(self.computed_gene)

        if self.variant_of_transcript is not None and not isinstance(self.variant_of_transcript, TranscriptCurie):
            self.variant_of_transcript = TranscriptCurie(self.variant_of_transcript)

        if self.variant_of_allele is not None and not isinstance(self.variant_of_allele, AlleleCurie):
            self.variant_of_allele = AlleleCurie(self.variant_of_allele)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, Synonym) else Synonym(**as_dict(v)) for v in self.synonyms]

        if self.type is not None and not isinstance(self.type, URIorCURIE):
            self.type = URIorCURIE(self.type)

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, ReferenceCurie) else ReferenceCurie(v) for v in self.references]

        if not isinstance(self.notes, list):
            self.notes = [self.notes] if self.notes is not None else []
        self.notes = [v if isinstance(v, str) else str(v) for v in self.notes]

        if self.protein_sequence is not None and not isinstance(self.protein_sequence, str):
            self.protein_sequence = str(self.protein_sequence)

        if not isinstance(self.cross_references, list):
            self.cross_references = [self.cross_references] if self.cross_references is not None else []
        self.cross_references = [v if isinstance(v, CrossReferenceCurie) else CrossReferenceCurie(v) for v in self.cross_references]

        super().__post_init__(**kwargs)


# Enumerations


# Slots

