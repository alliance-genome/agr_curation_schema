# Auto generated from variantConsequence.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-05-25 15:14
# Schema: variantConsequence
#
# id: https://github.com/alliance-genome/agr_persistent_schema/src/schema/variantConsequence
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
from . core import GeneId, TranscriptId
from . variation import VariantId
from linkml_runtime.linkml_model.types import Float, Integer, String

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
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_persistent_schema/src/schema/variantConsequence/')


# Types

# Class references



@dataclass
class VariantGeneConsequence(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/variantConsequence/VariantGeneConsequence")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "VariantGeneConsequence"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/variantConsequence/VariantGeneConsequence")

    subject: Union[str, VariantId] = None
    object: Union[str, GeneId] = None
    vep_consequence: Optional[Union[str, "VepConsequenceLevels"]] = None
    vep_impact: Optional[str] = None
    polyphen_score: Optional[float] = None
    polyphen_prediction: Optional[Union[str, "PolyphenPredictionLevels"]] = None
    sift_score: Optional[float] = None
    sift_prediction: Optional[Union[str, "SiftPredictionLevels"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, VariantId):
            self.subject = VariantId(self.subject)

        if self._is_empty(self.object):
            raise ValueError("object must be supplied")
        if not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.vep_consequence is not None and not isinstance(self.vep_consequence, VepConsequenceLevels):
            self.vep_consequence = VepConsequenceLevels(self.vep_consequence)

        if self.vep_impact is not None and not isinstance(self.vep_impact, str):
            self.vep_impact = str(self.vep_impact)

        if self.polyphen_score is not None and not isinstance(self.polyphen_score, float):
            self.polyphen_score = float(self.polyphen_score)

        if self.polyphen_prediction is not None and not isinstance(self.polyphen_prediction, PolyphenPredictionLevels):
            self.polyphen_prediction = PolyphenPredictionLevels(self.polyphen_prediction)

        if self.sift_score is not None and not isinstance(self.sift_score, float):
            self.sift_score = float(self.sift_score)

        if self.sift_prediction is not None and not isinstance(self.sift_prediction, SiftPredictionLevels):
            self.sift_prediction = SiftPredictionLevels(self.sift_prediction)

        super().__post_init__(**kwargs)


@dataclass
class VariantTranscriptConsequence(YAMLRoot):
    """
    Class for transcript-level VEP results
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/variantConsequence/VariantTranscriptConsequence")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "VariantTranscriptConsequence"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/variantConsequence/VariantTranscriptConsequence")

    subject: Union[str, VariantId] = None
    object: Union[str, TranscriptId] = None
    vep_consequence: Optional[Union[str, "VepConsequenceLevels"]] = None
    vep_impact: Optional[str] = None
    polyphen_score: Optional[float] = None
    polyphen_prediction: Optional[Union[str, "PolyphenPredictionLevels"]] = None
    sift_score: Optional[float] = None
    sift_prediction: Optional[Union[str, "SiftPredictionLevels"]] = None
    amino_acid_reference: Optional[str] = None
    amino_acid_variant: Optional[str] = None
    codon_reference: Optional[str] = None
    codon_variant: Optional[str] = None
    cdna_start: Optional[int] = None
    cdna_end: Optional[int] = None
    cds_start: Optional[int] = None
    cds_end: Optional[int] = None
    protein_start: Optional[int] = None
    protein_end: Optional[int] = None
    hgvs_protein_nomenclature: Optional[str] = None
    hgvs_coding_nomenclature: Optional[str] = None
    cnda_end: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, VariantId):
            self.subject = VariantId(self.subject)

        if self._is_empty(self.object):
            raise ValueError("object must be supplied")
        if not isinstance(self.object, TranscriptId):
            self.object = TranscriptId(self.object)

        if self.vep_consequence is not None and not isinstance(self.vep_consequence, VepConsequenceLevels):
            self.vep_consequence = VepConsequenceLevels(self.vep_consequence)

        if self.vep_impact is not None and not isinstance(self.vep_impact, str):
            self.vep_impact = str(self.vep_impact)

        if self.polyphen_score is not None and not isinstance(self.polyphen_score, float):
            self.polyphen_score = float(self.polyphen_score)

        if self.polyphen_prediction is not None and not isinstance(self.polyphen_prediction, PolyphenPredictionLevels):
            self.polyphen_prediction = PolyphenPredictionLevels(self.polyphen_prediction)

        if self.sift_score is not None and not isinstance(self.sift_score, float):
            self.sift_score = float(self.sift_score)

        if self.sift_prediction is not None and not isinstance(self.sift_prediction, SiftPredictionLevels):
            self.sift_prediction = SiftPredictionLevels(self.sift_prediction)

        if self.amino_acid_reference is not None and not isinstance(self.amino_acid_reference, str):
            self.amino_acid_reference = str(self.amino_acid_reference)

        if self.amino_acid_variant is not None and not isinstance(self.amino_acid_variant, str):
            self.amino_acid_variant = str(self.amino_acid_variant)

        if self.codon_reference is not None and not isinstance(self.codon_reference, str):
            self.codon_reference = str(self.codon_reference)

        if self.codon_variant is not None and not isinstance(self.codon_variant, str):
            self.codon_variant = str(self.codon_variant)

        if self.cdna_start is not None and not isinstance(self.cdna_start, int):
            self.cdna_start = int(self.cdna_start)

        if self.cdna_end is not None and not isinstance(self.cdna_end, int):
            self.cdna_end = int(self.cdna_end)

        if self.cds_start is not None and not isinstance(self.cds_start, int):
            self.cds_start = int(self.cds_start)

        if self.cds_end is not None and not isinstance(self.cds_end, int):
            self.cds_end = int(self.cds_end)

        if self.protein_start is not None and not isinstance(self.protein_start, int):
            self.protein_start = int(self.protein_start)

        if self.protein_end is not None and not isinstance(self.protein_end, int):
            self.protein_end = int(self.protein_end)

        if self.hgvs_protein_nomenclature is not None and not isinstance(self.hgvs_protein_nomenclature, str):
            self.hgvs_protein_nomenclature = str(self.hgvs_protein_nomenclature)

        if self.hgvs_coding_nomenclature is not None and not isinstance(self.hgvs_coding_nomenclature, str):
            self.hgvs_coding_nomenclature = str(self.hgvs_coding_nomenclature)

        if self.cnda_end is not None and not isinstance(self.cnda_end, str):
            self.cnda_end = str(self.cnda_end)

        super().__post_init__(**kwargs)


# Enumerations
class VepConsequenceLevels(EnumDefinitionImpl):

    high = PermissibleValue(text="high")
    moderate = PermissibleValue(text="moderate")
    low = PermissibleValue(text="low")
    modifier = PermissibleValue(text="modifier")

    _defn = EnumDefinition(
        name="VepConsequenceLevels",
    )

class SiftPredictionLevels(EnumDefinitionImpl):

    deleterious = PermissibleValue(text="deleterious")
    tolerated = PermissibleValue(text="tolerated")

    _defn = EnumDefinition(
        name="SiftPredictionLevels",
    )

class PolyphenPredictionLevels(EnumDefinitionImpl):

    possibly_damaging = PermissibleValue(text="possibly_damaging")
    probably_damaging = PermissibleValue(text="probably_damaging")
    benign = PermissibleValue(text="benign")

    _defn = EnumDefinition(
        name="PolyphenPredictionLevels",
    )

# Slots

