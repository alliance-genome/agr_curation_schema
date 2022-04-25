# Auto generated from variantConsequence.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-04-25T22:20:16
# Schema: variantConsequence
#
# id: https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence
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
from linkml_runtime.linkml_model.types import Boolean, Date, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DOI = CurieNamespace('DOI', 'http://identifiers.org/doi/')
ENSEMBL = CurieNamespace('ENSEMBL', 'http://identifiers.org/ensembl/')
FB = CurieNamespace('FB', 'http://identifiers.org/fb/')
HGNC = CurieNamespace('HGNC', 'http://identifiers.org/hgnc/')
MGI = CurieNamespace('MGI', 'http://identifiers.org/mgi/')
NLMID = CurieNamespace('NLMID', 'https://www.ncbi.nlm.nih.gov/nlmcatalog/?term=')
PMC = CurieNamespace('PMC', 'http://identifiers.org/pmc/')
PMID = CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/')
RGD = CurieNamespace('RGD', 'http://identifiers.org/rgd/')
SGD = CurieNamespace('SGD', 'http://identifiers.org/sgd/')
SO = CurieNamespace('SO', 'http://purl.obolibrary.org/obo/SO_')
WB = CurieNamespace('WB', 'http://identifiers.org/wb/')
WIKIDATA_PROPERTY = CurieNamespace('WIKIDATA_PROPERTY', 'https://www.wikidata.org/wiki/Property:')
ZFIN = CurieNamespace('ZFIN', 'http://identifiers.org/zfin/')
ALLIANCE = CurieNamespace('alliance', 'http://alliancegenome.org')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
FALDO = CurieNamespace('faldo', 'http://biohackathon.org/resource/faldo#')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
GFF = CurieNamespace('gff', 'https://w3id.org/gff')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OBOGRAPH = CurieNamespace('obograph', 'https://github.com/biodatamodels/obograph')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/')


# Types
class BiologicalSequence(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "biological_sequence"
    type_model_uri = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/BiologicalSequence")


# Class references
class BiologicalEntityCurie(URIorCURIE):
    pass


class GenomicEntityCurie(BiologicalEntityCurie):
    pass


class TranscriptCurie(GenomicEntityCurie):
    pass


class GeneCurie(GenomicEntityCurie):
    pass


class CrossReferenceCurie(URIorCURIE):
    pass


class ChromosomeCurie(URIorCURIE):
    pass


class AssemblyCurie(URIorCURIE):
    pass


class ProteinCurie(GenomicEntityCurie):
    pass


class VariantCurie(GenomicEntityCurie):
    pass


class ReferenceCurie(URIorCURIE):
    pass


class ResourceCurie(URIorCURIE):
    pass


class PersonUniqueId(extended_str):
    pass


class LoggedInPersonUniqueId(PersonUniqueId):
    pass


class FigureCurie(URIorCURIE):
    pass


class ImageCurie(URIorCURIE):
    pass


class OntologyTermCurie(URIorCURIE):
    pass


class DOTermCurie(OntologyTermCurie):
    pass


class ECOTermCurie(OntologyTermCurie):
    pass


class NCBITaxonTermCurie(OntologyTermCurie):
    pass


class FBCVTermCurie(OntologyTermCurie):
    pass


class GOTermCurie(OntologyTermCurie):
    pass


class ROTermCurie(OntologyTermCurie):
    pass


class MITermCurie(OntologyTermCurie):
    pass


class MMOTermCurie(OntologyTermCurie):
    pass


class MMUSDVTermCurie(OntologyTermCurie):
    pass


class SOTermCurie(OntologyTermCurie):
    pass


class XBEDTermCurie(OntologyTermCurie):
    pass


class StageTermCurie(OntologyTermCurie):
    pass


class FBDVTermCurie(StageTermCurie):
    pass


class WBLSTermCurie(StageTermCurie):
    pass


class XBSTermCurie(StageTermCurie):
    pass


class ZFSTermCurie(StageTermCurie):
    pass


class ExperimentalConditionOntologyTermCurie(OntologyTermCurie):
    pass


class ZECOTermCurie(ExperimentalConditionOntologyTermCurie):
    pass


class XCOTermCurie(ExperimentalConditionOntologyTermCurie):
    pass


class AnatomicalTermCurie(OntologyTermCurie):
    pass


class CLTermCurie(AnatomicalTermCurie):
    pass


class EMAPATermCurie(AnatomicalTermCurie):
    pass


class DAOTermCurie(AnatomicalTermCurie):
    pass


class MATermCurie(AnatomicalTermCurie):
    pass


class UBERONTermCurie(AnatomicalTermCurie):
    pass


class WBBTTermCurie(AnatomicalTermCurie):
    pass


class XBATermCurie(AnatomicalTermCurie):
    pass


class ZFATermCurie(AnatomicalTermCurie):
    pass


class PhenotypeTermCurie(OntologyTermCurie):
    pass


class XPOTermCurie(PhenotypeTermCurie):
    pass


class ChemicalTermCurie(OntologyTermCurie):
    pass


class CHEBITermCurie(ChemicalTermCurie):
    pass


class XSMOTermCurie(ChemicalTermCurie):
    pass


class MoleculeCurie(ChemicalTermCurie):
    pass


class VocabularyTermName(extended_str):
    pass


class VocabularyName(extended_str):
    pass


class AlleleCurie(GenomicEntityCurie):
    pass


class ConstructCurie(GenomicEntityCurie):
    pass


class SequenceTargetingReagentCurie(GenomicEntityCurie):
    pass


class ConstructComponentCurie(GenomicEntityCurie):
    pass


class AffectedGenomicModelCurie(GenomicEntityCurie):
    pass


@dataclass
class AuditedObject(YAMLRoot):
    """
    Base class for all other LinkML classes. Some entity for which changes are tracked, including date/time of change,
    the agent responsible for the change, and whether the entity is internal (private).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AuditedObject
    class_class_curie: ClassVar[str] = "alliance:AuditedObject"
    class_name: ClassVar[str] = "AuditedObject"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/AuditedObject")

    internal: Union[bool, Bool] = None
    table_key: Optional[int] = None
    created_by: Optional[Union[str, PersonUniqueId]] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    modified_by: Optional[Union[str, PersonUniqueId]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.internal):
            self.MissingRequiredField("internal")
        if not isinstance(self.internal, Bool):
            self.internal = Bool(self.internal)

        if self.table_key is not None and not isinstance(self.table_key, int):
            self.table_key = int(self.table_key)

        if self.created_by is not None and not isinstance(self.created_by, PersonUniqueId):
            self.created_by = PersonUniqueId(self.created_by)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.modified_by is not None and not isinstance(self.modified_by, PersonUniqueId):
            self.modified_by = PersonUniqueId(self.modified_by)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

        super().__post_init__(**kwargs)


@dataclass
class VariantConsequence(AuditedObject):
    """
    Parent class for gene- and transcript-level consequences
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/VariantConsequence")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "VariantConsequence"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/VariantConsequence")

    internal: Union[bool, Bool] = None
    subject: str = None
    object: str = None
    vep_consequence: Optional[Union[str, "VepConsequenceLevels"]] = None
    vep_impact: Optional[str] = None
    polyphen_score: Optional[float] = None
    polyphen_prediction: Optional[Union[str, "PolyphenPredictionLevels"]] = None
    sift_score: Optional[float] = None
    sift_prediction: Optional[Union[str, "SiftPredictionLevels"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, str):
            self.object = str(self.object)

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
class VariantGeneConsequence(VariantConsequence):
    """
    Class for gene-level VEP results
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/VariantGeneConsequence")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "VariantGeneConsequence"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/VariantGeneConsequence")

    internal: Union[bool, Bool] = None
    object: Union[str, GeneCurie] = None
    subject: Union[dict, "VariantGenomeLocation"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GeneCurie):
            self.object = GeneCurie(self.object)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, VariantGenomeLocation):
            self.subject = VariantGenomeLocation(**as_dict(self.subject))

        super().__post_init__(**kwargs)


@dataclass
class VariantTranscriptConsequence(VariantConsequence):
    """
    Class for transcript-level VEP results
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/VariantTranscriptConsequence")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "VariantTranscriptConsequence"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/VariantTranscriptConsequence")

    internal: Union[bool, Bool] = None
    object: Union[str, TranscriptCurie] = None
    subject: Union[dict, "VariantTranscriptLocation"] = None
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
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, TranscriptCurie):
            self.object = TranscriptCurie(self.object)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, VariantTranscriptLocation):
            self.subject = VariantTranscriptLocation(**as_dict(self.subject))

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


@dataclass
class BiologicalEntity(AuditedObject):
    """
    A high-level entity comprising .
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.BiologicalEntity
    class_class_curie: ClassVar[str] = "alliance:BiologicalEntity"
    class_name: ClassVar[str] = "BiologicalEntity"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/BiologicalEntity")

    curie: Union[str, BiologicalEntityCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, BiologicalEntityCurie):
            self.curie = BiologicalEntityCurie(self.curie)

        if self._is_empty(self.taxon):
            self.MissingRequiredField("taxon")
        if not isinstance(self.taxon, NCBITaxonTermCurie):
            self.taxon = NCBITaxonTermCurie(self.taxon)

        super().__post_init__(**kwargs)


@dataclass
class GenomicEntity(BiologicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GenomicEntity
    class_class_curie: ClassVar[str] = "alliance:GenomicEntity"
    class_name: ClassVar[str] = "GenomicEntity"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/GenomicEntity")

    curie: Union[str, GenomicEntityCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None
    name: Optional[str] = None
    synonyms: Optional[Union[Union[dict, "Synonym"], List[Union[dict, "Synonym"]]]] = empty_list()
    cross_references: Optional[Union[Dict[Union[str, CrossReferenceCurie], Union[dict, "CrossReference"]], List[Union[dict, "CrossReference"]]]] = empty_dict()
    secondary_identifiers: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, GenomicEntityCurie):
            self.curie = GenomicEntityCurie(self.curie)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        self._normalize_inlined_as_dict(slot_name="synonyms", slot_type=Synonym, key_name="internal", keyed=False)

        self._normalize_inlined_as_list(slot_name="cross_references", slot_type=CrossReference, key_name="curie", keyed=True)

        if not isinstance(self.secondary_identifiers, list):
            self.secondary_identifiers = [self.secondary_identifiers] if self.secondary_identifiers is not None else []
        self.secondary_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.secondary_identifiers]

        super().__post_init__(**kwargs)


@dataclass
class Transcript(GenomicEntity):
    """
    Placeholder.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Transcript
    class_class_curie: ClassVar[str] = "alliance:Transcript"
    class_name: ClassVar[str] = "Transcript"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/Transcript")

    curie: Union[str, TranscriptCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, TranscriptCurie):
            self.curie = TranscriptCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class Gene(GenomicEntity):
    """
    Placeholder.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Gene
    class_class_curie: ClassVar[str] = "alliance:Gene"
    class_name: ClassVar[str] = "Gene"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/Gene")

    curie: Union[str, GeneCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None
    symbol: str = None
    genomic_locations: Optional[Union[Union[dict, "GeneGenomicLocation"], List[Union[dict, "GeneGenomicLocation"]]]] = empty_list()
    gene_synopsis: Optional[str] = None
    gene_synopsis_URL: Optional[str] = None
    gene_type: Optional[Union[str, SOTermCurie]] = None
    automated_gene_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, GeneCurie):
            self.curie = GeneCurie(self.curie)

        if self._is_empty(self.symbol):
            self.MissingRequiredField("symbol")
        if not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        self._normalize_inlined_as_dict(slot_name="genomic_locations", slot_type=GeneGenomicLocation, key_name="internal", keyed=False)

        if self.gene_synopsis is not None and not isinstance(self.gene_synopsis, str):
            self.gene_synopsis = str(self.gene_synopsis)

        if self.gene_synopsis_URL is not None and not isinstance(self.gene_synopsis_URL, str):
            self.gene_synopsis_URL = str(self.gene_synopsis_URL)

        if self.gene_type is not None and not isinstance(self.gene_type, SOTermCurie):
            self.gene_type = SOTermCurie(self.gene_type)

        if self.automated_gene_description is not None and not isinstance(self.automated_gene_description, str):
            self.automated_gene_description = str(self.automated_gene_description)

        super().__post_init__(**kwargs)


@dataclass
class CrossReference(AuditedObject):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.CrossReference
    class_class_curie: ClassVar[str] = "alliance:CrossReference"
    class_name: ClassVar[str] = "CrossReference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/CrossReference")

    curie: Union[str, CrossReferenceCurie] = None
    internal: Union[bool, Bool] = None
    page_areas: Union[str, List[str]] = None
    display_name: str = None
    prefix: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, CrossReferenceCurie):
            self.curie = CrossReferenceCurie(self.curie)

        if self._is_empty(self.page_areas):
            self.MissingRequiredField("page_areas")
        if not isinstance(self.page_areas, list):
            self.page_areas = [self.page_areas] if self.page_areas is not None else []
        self.page_areas = [v if isinstance(v, str) else str(v) for v in self.page_areas]

        if self._is_empty(self.display_name):
            self.MissingRequiredField("display_name")
        if not isinstance(self.display_name, str):
            self.display_name = str(self.display_name)

        if self._is_empty(self.prefix):
            self.MissingRequiredField("prefix")
        if not isinstance(self.prefix, str):
            self.prefix = str(self.prefix)

        super().__post_init__(**kwargs)


@dataclass
class Synonym(AuditedObject):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Synonym
    class_class_curie: ClassVar[str] = "alliance:Synonym"
    class_name: ClassVar[str] = "Synonym"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/Synonym")

    internal: Union[bool, Bool] = None
    synonym: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.synonym is not None and not isinstance(self.synonym, str):
            self.synonym = str(self.synonym)

        super().__post_init__(**kwargs)


@dataclass
class Note(AuditedObject):
    """
    Note object for capturing free-text describing some attribute of an entity, coupled with a 'note type', internal
    boolean, and an optional list of references. Permissible values for 'note_type' currently = disease_summary,
    disease_note
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Note
    class_class_curie: ClassVar[str] = "alliance:Note"
    class_name: ClassVar[str] = "Note"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/Note")

    internal: Union[bool, Bool] = None
    free_text: str = None
    note_type: Union[str, VocabularyTermName] = None
    references: Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.free_text):
            self.MissingRequiredField("free_text")
        if not isinstance(self.free_text, str):
            self.free_text = str(self.free_text)

        if self._is_empty(self.note_type):
            self.MissingRequiredField("note_type")
        if not isinstance(self.note_type, VocabularyTermName):
            self.note_type = VocabularyTermName(self.note_type)

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, ReferenceCurie) else ReferenceCurie(v) for v in self.references]

        super().__post_init__(**kwargs)


@dataclass
class EntityStatement(AuditedObject):
    """
    Free-text describing some aspect of an entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.EntityStatement
    class_class_curie: ClassVar[str] = "alliance:EntityStatement"
    class_name: ClassVar[str] = "EntityStatement"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/EntityStatement")

    internal: Union[bool, Bool] = None
    statement_subject: Optional[str] = None
    statement_type: Optional[str] = None
    statement_text: Optional[str] = None
    references: Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.statement_subject is not None and not isinstance(self.statement_subject, str):
            self.statement_subject = str(self.statement_subject)

        if self.statement_type is not None and not isinstance(self.statement_type, str):
            self.statement_type = str(self.statement_type)

        if self.statement_text is not None and not isinstance(self.statement_text, str):
            self.statement_text = str(self.statement_text)

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, ReferenceCurie) else ReferenceCurie(v) for v in self.references]

        super().__post_init__(**kwargs)


@dataclass
class Association(AuditedObject):
    """
    A typed association between two entities, supported by evidence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Association
    class_class_curie: ClassVar[str] = "alliance:Association"
    class_name: ClassVar[str] = "Association"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/Association")

    internal: Union[bool, Bool] = None
    subject: str = None
    predicate: str = None
    object: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, str):
            self.object = str(self.object)

        super().__post_init__(**kwargs)


@dataclass
class EntitySynonym(Association):
    """
    A relationship between an entity and a synonym.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.EntitySynonym
    class_class_curie: ClassVar[str] = "alliance:EntitySynonym"
    class_name: ClassVar[str] = "EntitySynonym"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/EntitySynonym")

    internal: Union[bool, Bool] = None
    subject: str = None
    object: Union[dict, Synonym] = None
    predicate: Union[str, "EntitySynonymTypeSet"] = None
    references: Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, Synonym):
            self.object = Synonym(**as_dict(self.object))

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, EntitySynonymTypeSet):
            self.predicate = EntitySynonymTypeSet(self.predicate)

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, ReferenceCurie) else ReferenceCurie(v) for v in self.references]

        super().__post_init__(**kwargs)


@dataclass
class ExternalDatabaseLink(AuditedObject):
    """
    Base relation that holds the identifier prefix, base url and url suffix to help in generating URLs in
    crossReferences.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ExternalDatabaseLink
    class_class_curie: ClassVar[str] = "alliance:ExternalDatabaseLink"
    class_name: ClassVar[str] = "ExternalDatabaseLink"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/ExternalDatabaseLink")

    internal: Union[bool, Bool] = None
    prefix: str = None
    dbkey: Optional[str] = None
    url_prefix: Optional[str] = None
    url_suffix: Optional[str] = None
    prefix_page: Optional[str] = None
    prefix_order: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.prefix):
            self.MissingRequiredField("prefix")
        if not isinstance(self.prefix, str):
            self.prefix = str(self.prefix)

        if self.dbkey is not None and not isinstance(self.dbkey, str):
            self.dbkey = str(self.dbkey)

        if self.url_prefix is not None and not isinstance(self.url_prefix, str):
            self.url_prefix = str(self.url_prefix)

        if self.url_suffix is not None and not isinstance(self.url_suffix, str):
            self.url_suffix = str(self.url_suffix)

        if self.prefix_page is not None and not isinstance(self.prefix_page, str):
            self.prefix_page = str(self.prefix_page)

        if self.prefix_order is not None and not isinstance(self.prefix_order, str):
            self.prefix_order = str(self.prefix_order)

        super().__post_init__(**kwargs)


@dataclass
class Chromosome(AuditedObject):
    """
    The ID of the landmark used to establish the coordinate system for the current feature.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Chromosome
    class_class_curie: ClassVar[str] = "alliance:Chromosome"
    class_name: ClassVar[str] = "Chromosome"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/Chromosome")

    curie: Union[str, ChromosomeCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ChromosomeCurie):
            self.curie = ChromosomeCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class Assembly(AuditedObject):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Assembly
    class_class_curie: ClassVar[str] = "alliance:Assembly"
    class_name: ClassVar[str] = "Assembly"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/Assembly")

    curie: Union[str, AssemblyCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, AssemblyCurie):
            self.curie = AssemblyCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class GeneGenomicLocation(AuditedObject):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GeneGenomicLocation
    class_class_curie: ClassVar[str] = "alliance:GeneGenomicLocation"
    class_name: ClassVar[str] = "GeneGenomicLocation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/GeneGenomicLocation")

    internal: Union[bool, Bool] = None
    subject: Union[str, VariantCurie] = None
    predicate: str = None
    object: Union[str, ChromosomeCurie] = None
    has_assembly: Union[str, ChromosomeCurie] = None
    start: Optional[str] = None
    end: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, VariantCurie):
            self.subject = VariantCurie(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ChromosomeCurie):
            self.object = ChromosomeCurie(self.object)

        if self._is_empty(self.has_assembly):
            self.MissingRequiredField("has_assembly")
        if not isinstance(self.has_assembly, ChromosomeCurie):
            self.has_assembly = ChromosomeCurie(self.has_assembly)

        if self.start is not None and not isinstance(self.start, str):
            self.start = str(self.start)

        if self.end is not None and not isinstance(self.end, str):
            self.end = str(self.end)

        super().__post_init__(**kwargs)


@dataclass
class Protein(GenomicEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Protein
    class_class_curie: ClassVar[str] = "alliance:Protein"
    class_name: ClassVar[str] = "Protein"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/Protein")

    curie: Union[str, ProteinCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ProteinCurie):
            self.curie = ProteinCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class Variant(GenomicEntity):
    """
    A DNA, RNA or protein/polypeptide sequence that differs relative to a designated reference sequence. The sequence
    occurs at a single position or in a range of contiguous nucleotides or amino acids.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variation/Variant")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Variant"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/Variant")

    curie: Union[str, VariantCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None
    variant_type: Union[str, SOTermCurie] = None
    variant_genome_locations: Union[Union[dict, "VariantGenomeLocation"], List[Union[dict, "VariantGenomeLocation"]]] = None
    related_notes: Optional[Union[Union[dict, Note], List[Union[dict, Note]]]] = empty_list()
    source_general_consequence: Optional[Union[str, SOTermCurie]] = None
    variant_polypeptide_locations: Optional[Union[Union[dict, "VariantPolypeptideLocation"], List[Union[dict, "VariantPolypeptideLocation"]]]] = empty_list()
    variant_transcript_locations: Optional[Union[Union[dict, "VariantTranscriptLocation"], List[Union[dict, "VariantTranscriptLocation"]]]] = empty_list()
    source_variant_locations: Optional[Union[Union[dict, "SourceVariantLocation"], List[Union[dict, "SourceVariantLocation"]]]] = empty_list()
    variant_status: Optional[Union[str, "VariantStatusEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, VariantCurie):
            self.curie = VariantCurie(self.curie)

        if self._is_empty(self.variant_type):
            self.MissingRequiredField("variant_type")
        if not isinstance(self.variant_type, SOTermCurie):
            self.variant_type = SOTermCurie(self.variant_type)

        if self._is_empty(self.variant_genome_locations):
            self.MissingRequiredField("variant_genome_locations")
        self._normalize_inlined_as_dict(slot_name="variant_genome_locations", slot_type=VariantGenomeLocation, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="related_notes", slot_type=Note, key_name="internal", keyed=False)

        if self.source_general_consequence is not None and not isinstance(self.source_general_consequence, SOTermCurie):
            self.source_general_consequence = SOTermCurie(self.source_general_consequence)

        self._normalize_inlined_as_dict(slot_name="variant_polypeptide_locations", slot_type=VariantPolypeptideLocation, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="variant_transcript_locations", slot_type=VariantTranscriptLocation, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="source_variant_locations", slot_type=SourceVariantLocation, key_name="internal", keyed=False)

        if self.variant_status is not None and not isinstance(self.variant_status, VariantStatusEnum):
            self.variant_status = VariantStatusEnum(self.variant_status)

        super().__post_init__(**kwargs)


@dataclass
class SourceVariantLocation(AuditedObject):
    """
    Links a paper to the variant locations described in that paper
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variation/SourceVariantLocation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SourceVariantLocation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/SourceVariantLocation")

    internal: Union[bool, Bool] = None
    variant_locations: Union[Union[dict, "VariantLocation"], List[Union[dict, "VariantLocation"]]] = None
    single_reference: Union[str, ReferenceCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.variant_locations):
            self.MissingRequiredField("variant_locations")
        self._normalize_inlined_as_dict(slot_name="variant_locations", slot_type=VariantLocation, key_name="internal", keyed=False)

        if self._is_empty(self.single_reference):
            self.MissingRequiredField("single_reference")
        if not isinstance(self.single_reference, ReferenceCurie):
            self.single_reference = ReferenceCurie(self.single_reference)

        super().__post_init__(**kwargs)


@dataclass
class VariantLocation(AuditedObject):
    """
    Base class linking a variant to a position on a genomic entity and the resulting consequence to the sequence
    and/or function of that genomic entity. Slots are provided for data taken from a source publication or data load
    and for data resulting from manual curation. Where the values are the same, the curator has confirmed the
    information from the source. In other cases, the curator's analysis has resulted in different values, for
    instance, if the assembly is different, the source did not specify the transcript or protein isoform, the
    definition of the transcript or protein isoform used by the source has changed, or if there was an error in the
    source data.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variation/VariantLocation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "VariantLocation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/VariantLocation")

    internal: Union[bool, Bool] = None
    evidence_code: Optional[Union[str, ECOTermCurie]] = None
    single_reference: Optional[Union[str, ReferenceCurie]] = None
    start_position: Optional[int] = None
    end_position: Optional[int] = None
    reference_sequence: Optional[Union[str, BiologicalSequence]] = None
    variant_sequence: Optional[Union[str, BiologicalSequence]] = None
    consequence: Optional[Union[str, SOTermCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.evidence_code is not None and not isinstance(self.evidence_code, ECOTermCurie):
            self.evidence_code = ECOTermCurie(self.evidence_code)

        if self.single_reference is not None and not isinstance(self.single_reference, ReferenceCurie):
            self.single_reference = ReferenceCurie(self.single_reference)

        if self.start_position is not None and not isinstance(self.start_position, int):
            self.start_position = int(self.start_position)

        if self.end_position is not None and not isinstance(self.end_position, int):
            self.end_position = int(self.end_position)

        if self.reference_sequence is not None and not isinstance(self.reference_sequence, BiologicalSequence):
            self.reference_sequence = BiologicalSequence(self.reference_sequence)

        if self.variant_sequence is not None and not isinstance(self.variant_sequence, BiologicalSequence):
            self.variant_sequence = BiologicalSequence(self.variant_sequence)

        if self.consequence is not None and not isinstance(self.consequence, SOTermCurie):
            self.consequence = SOTermCurie(self.consequence)

        super().__post_init__(**kwargs)


@dataclass
class VariantGenomeLocation(VariantLocation):
    """
    Links a variant to a genomic position and the resulting consequence to the sequence and/or function. In practice,
    functional consequences for variants which overlap genes are not generally provided at the genome level but rather
    are calculated and annotated relative to a specific transcript or protein isoform.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variation/VariantGenomeLocation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "VariantGenomeLocation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/VariantGenomeLocation")

    internal: Union[bool, Bool] = None
    assembly: Optional[Union[str, AssemblyCurie]] = None
    chromosome: Optional[Union[str, ChromosomeCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.assembly is not None and not isinstance(self.assembly, AssemblyCurie):
            self.assembly = AssemblyCurie(self.assembly)

        if self.chromosome is not None and not isinstance(self.chromosome, ChromosomeCurie):
            self.chromosome = ChromosomeCurie(self.chromosome)

        super().__post_init__(**kwargs)


@dataclass
class VariantTranscriptLocation(VariantLocation):
    """
    Links a variant to a position on a specified transcript and the resulting consequence to the sequence and/or
    function of that transcript.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variation/VariantTranscriptLocation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "VariantTranscriptLocation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/VariantTranscriptLocation")

    internal: Union[bool, Bool] = None
    transcript: Optional[Union[str, TranscriptCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.transcript is not None and not isinstance(self.transcript, TranscriptCurie):
            self.transcript = TranscriptCurie(self.transcript)

        super().__post_init__(**kwargs)


@dataclass
class VariantPolypeptideLocation(VariantLocation):
    """
    Links a variant to a position on a specified polypeptide and the resulting consequence to the sequence and/or
    function of that polypeptide.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variation/VariantPolypeptideLocation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "VariantPolypeptideLocation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/VariantPolypeptideLocation")

    internal: Union[bool, Bool] = None
    polypeptide: Union[str, TranscriptCurie] = None
    associated_transcripts: Optional[Union[Union[str, TranscriptCurie], List[Union[str, TranscriptCurie]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.polypeptide):
            self.MissingRequiredField("polypeptide")
        if not isinstance(self.polypeptide, TranscriptCurie):
            self.polypeptide = TranscriptCurie(self.polypeptide)

        if not isinstance(self.associated_transcripts, list):
            self.associated_transcripts = [self.associated_transcripts] if self.associated_transcripts is not None else []
        self.associated_transcripts = [v if isinstance(v, TranscriptCurie) else TranscriptCurie(v) for v in self.associated_transcripts]

        super().__post_init__(**kwargs)


@dataclass
class AuthorReference(AuditedObject):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/reference/AuthorReference")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AuthorReference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/AuthorReference")

    internal: Union[bool, Bool] = None
    corresponding_author: Optional[Union[str, ReferenceCurie]] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    initials: Optional[Union[str, ReferenceCurie]] = None
    cross_references: Optional[Union[Dict[Union[str, CrossReferenceCurie], Union[dict, CrossReference]], List[Union[dict, CrossReference]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.corresponding_author is not None and not isinstance(self.corresponding_author, ReferenceCurie):
            self.corresponding_author = ReferenceCurie(self.corresponding_author)

        if self.first_name is not None and not isinstance(self.first_name, str):
            self.first_name = str(self.first_name)

        if self.middle_name is not None and not isinstance(self.middle_name, str):
            self.middle_name = str(self.middle_name)

        if self.last_name is not None and not isinstance(self.last_name, str):
            self.last_name = str(self.last_name)

        if self.initials is not None and not isinstance(self.initials, ReferenceCurie):
            self.initials = ReferenceCurie(self.initials)

        self._normalize_inlined_as_list(slot_name="cross_references", slot_type=CrossReference, key_name="curie", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Reference(AuditedObject):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/reference/Reference")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Reference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/Reference")

    curie: Union[str, ReferenceCurie] = None
    internal: Union[bool, Bool] = None
    reference_id: int = None
    abstract: Optional[str] = None
    category: Optional[Union[str, "ReferenceCategoryEnum"]] = None
    citation: Optional[str] = None
    date_arrived_in_pubmed: Optional[Union[str, List[str]]] = empty_list()
    date_created: Optional[Union[str, XSDDate]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None
    date_published: Optional[str] = None
    date_updated: Optional[Union[str, XSDDate]] = None
    issue_date: Optional[str] = None
    issue_name: Optional[str] = None
    keywords: Optional[Union[str, List[str]]] = empty_list()
    language: Optional[str] = None
    merged_into_id: Optional[Union[str, URIorCURIE]] = None
    open_access: Optional[Union[bool, Bool]] = None
    pages: Optional[str] = None
    plain_language_abstract: Optional[str] = None
    publisher: Optional[str] = None
    pubmed_abstract_languages: Optional[Union[str, List[str]]] = empty_list()
    pubmed_publication_status: Optional[Union[str, "PubmedPublicationStatusEnum"]] = None
    pubmed_type: Optional[Union[Union[str, "PubmedTypeEnum"], List[Union[str, "PubmedTypeEnum"]]]] = empty_list()
    resource_id: Optional[int] = None
    title: Optional[str] = None
    volume: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ReferenceCurie):
            self.curie = ReferenceCurie(self.curie)

        if self._is_empty(self.reference_id):
            self.MissingRequiredField("reference_id")
        if not isinstance(self.reference_id, int):
            self.reference_id = int(self.reference_id)

        if self.abstract is not None and not isinstance(self.abstract, str):
            self.abstract = str(self.abstract)

        if self.category is not None and not isinstance(self.category, ReferenceCategoryEnum):
            self.category = ReferenceCategoryEnum(self.category)

        if self.citation is not None and not isinstance(self.citation, str):
            self.citation = str(self.citation)

        if not isinstance(self.date_arrived_in_pubmed, list):
            self.date_arrived_in_pubmed = [self.date_arrived_in_pubmed] if self.date_arrived_in_pubmed is not None else []
        self.date_arrived_in_pubmed = [v if isinstance(v, str) else str(v) for v in self.date_arrived_in_pubmed]

        if self.date_created is not None and not isinstance(self.date_created, XSDDate):
            self.date_created = XSDDate(self.date_created)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

        if self.date_published is not None and not isinstance(self.date_published, str):
            self.date_published = str(self.date_published)

        if self.date_updated is not None and not isinstance(self.date_updated, XSDDate):
            self.date_updated = XSDDate(self.date_updated)

        if self.issue_date is not None and not isinstance(self.issue_date, str):
            self.issue_date = str(self.issue_date)

        if self.issue_name is not None and not isinstance(self.issue_name, str):
            self.issue_name = str(self.issue_name)

        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords] if self.keywords is not None else []
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        if self.language is not None and not isinstance(self.language, str):
            self.language = str(self.language)

        if self.merged_into_id is not None and not isinstance(self.merged_into_id, URIorCURIE):
            self.merged_into_id = URIorCURIE(self.merged_into_id)

        if self.open_access is not None and not isinstance(self.open_access, Bool):
            self.open_access = Bool(self.open_access)

        if self.pages is not None and not isinstance(self.pages, str):
            self.pages = str(self.pages)

        if self.plain_language_abstract is not None and not isinstance(self.plain_language_abstract, str):
            self.plain_language_abstract = str(self.plain_language_abstract)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if not isinstance(self.pubmed_abstract_languages, list):
            self.pubmed_abstract_languages = [self.pubmed_abstract_languages] if self.pubmed_abstract_languages is not None else []
        self.pubmed_abstract_languages = [v if isinstance(v, str) else str(v) for v in self.pubmed_abstract_languages]

        if self.pubmed_publication_status is not None and not isinstance(self.pubmed_publication_status, PubmedPublicationStatusEnum):
            self.pubmed_publication_status = PubmedPublicationStatusEnum(self.pubmed_publication_status)

        if not isinstance(self.pubmed_type, list):
            self.pubmed_type = [self.pubmed_type] if self.pubmed_type is not None else []
        self.pubmed_type = [v if isinstance(v, PubmedTypeEnum) else PubmedTypeEnum(v) for v in self.pubmed_type]

        if self.resource_id is not None and not isinstance(self.resource_id, int):
            self.resource_id = int(self.resource_id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        super().__post_init__(**kwargs)


@dataclass
class MeshDetail(AuditedObject):
    """
    Medical Subject Headings information coming from PubMed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/reference/MeshDetail")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "MeshDetail"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/MeshDetail")

    internal: Union[bool, Bool] = None
    mesh_detail_id: int = None
    reference_id: int = None
    heading_term: str = None
    qualifier_term: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.mesh_detail_id):
            self.MissingRequiredField("mesh_detail_id")
        if not isinstance(self.mesh_detail_id, int):
            self.mesh_detail_id = int(self.mesh_detail_id)

        if self._is_empty(self.reference_id):
            self.MissingRequiredField("reference_id")
        if not isinstance(self.reference_id, int):
            self.reference_id = int(self.reference_id)

        if self._is_empty(self.heading_term):
            self.MissingRequiredField("heading_term")
        if not isinstance(self.heading_term, str):
            self.heading_term = str(self.heading_term)

        if self.qualifier_term is not None and not isinstance(self.qualifier_term, str):
            self.qualifier_term = str(self.qualifier_term)

        super().__post_init__(**kwargs)


@dataclass
class Resource(AuditedObject):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/resource/Resource")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/Resource")

    curie: Union[str, ResourceCurie] = None
    internal: Union[bool, Bool] = None
    title: Optional[str] = None
    iso_abbreviation: Optional[str] = None
    medline_abbreviation: Optional[str] = None
    copyright_date: Optional[Union[str, XSDDate]] = None
    print_issn: Optional[str] = None
    online_issn: Optional[str] = None
    publisher: Optional[str] = None
    volume: Optional[str] = None
    summary: Optional[str] = None
    synonyms: Optional[Union[Union[dict, Synonym], List[Union[dict, Synonym]]]] = empty_list()
    authors: Optional[Union[Union[dict, AuthorReference], List[Union[dict, AuthorReference]]]] = empty_list()
    editors: Optional[Union[Union[dict, AuthorReference], List[Union[dict, AuthorReference]]]] = empty_list()
    id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ResourceCurie):
            self.curie = ResourceCurie(self.curie)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.iso_abbreviation is not None and not isinstance(self.iso_abbreviation, str):
            self.iso_abbreviation = str(self.iso_abbreviation)

        if self.medline_abbreviation is not None and not isinstance(self.medline_abbreviation, str):
            self.medline_abbreviation = str(self.medline_abbreviation)

        if self.copyright_date is not None and not isinstance(self.copyright_date, XSDDate):
            self.copyright_date = XSDDate(self.copyright_date)

        if self.print_issn is not None and not isinstance(self.print_issn, str):
            self.print_issn = str(self.print_issn)

        if self.online_issn is not None and not isinstance(self.online_issn, str):
            self.online_issn = str(self.online_issn)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        self._normalize_inlined_as_dict(slot_name="synonyms", slot_type=Synonym, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="authors", slot_type=AuthorReference, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="editors", slot_type=AuthorReference, key_name="internal", keyed=False)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Agent(AuditedObject):
    """
    An individual, group, organization or project that provides information and/or materials.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Agent
    class_class_curie: ClassVar[str] = "alliance:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/Agent")

    internal: Union[bool, Bool] = None

@dataclass
class Organization(Agent):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Organization
    class_class_curie: ClassVar[str] = "alliance:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/Organization")

    internal: Union[bool, Bool] = None

@dataclass
class Laboratory(Organization):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Laboratory
    class_class_curie: ClassVar[str] = "alliance:Laboratory"
    class_name: ClassVar[str] = "Laboratory"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/Laboratory")

    internal: Union[bool, Bool] = None

@dataclass
class Company(Organization):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Company
    class_class_curie: ClassVar[str] = "alliance:Company"
    class_name: ClassVar[str] = "Company"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/Company")

    internal: Union[bool, Bool] = None

@dataclass
class Person(Agent):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Person
    class_class_curie: ClassVar[str] = "alliance:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/Person")

    unique_id: Union[str, PersonUniqueId] = None
    internal: Union[bool, Bool] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    first_name: Optional[str] = None
    orcid: Optional[Union[str, URIorCURIE]] = None
    emails: Optional[Union[str, List[str]]] = empty_list()
    old_emails: Optional[Union[str, List[str]]] = empty_list()
    mod_entity_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.unique_id):
            self.MissingRequiredField("unique_id")
        if not isinstance(self.unique_id, PersonUniqueId):
            self.unique_id = PersonUniqueId(self.unique_id)

        if self.last_name is not None and not isinstance(self.last_name, str):
            self.last_name = str(self.last_name)

        if self.middle_name is not None and not isinstance(self.middle_name, str):
            self.middle_name = str(self.middle_name)

        if self.first_name is not None and not isinstance(self.first_name, str):
            self.first_name = str(self.first_name)

        if self.orcid is not None and not isinstance(self.orcid, URIorCURIE):
            self.orcid = URIorCURIE(self.orcid)

        if not isinstance(self.emails, list):
            self.emails = [self.emails] if self.emails is not None else []
        self.emails = [v if isinstance(v, str) else str(v) for v in self.emails]

        if not isinstance(self.old_emails, list):
            self.old_emails = [self.old_emails] if self.old_emails is not None else []
        self.old_emails = [v if isinstance(v, str) else str(v) for v in self.old_emails]

        if self.mod_entity_id is not None and not isinstance(self.mod_entity_id, str):
            self.mod_entity_id = str(self.mod_entity_id)

        super().__post_init__(**kwargs)


@dataclass
class LoggedInPerson(Person):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.LoggedInPerson
    class_class_curie: ClassVar[str] = "alliance:LoggedInPerson"
    class_name: ClassVar[str] = "LoggedInPerson"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/LoggedInPerson")

    unique_id: Union[str, LoggedInPersonUniqueId] = None
    internal: Union[bool, Bool] = None
    okta_id: str = None
    okta_email: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.unique_id):
            self.MissingRequiredField("unique_id")
        if not isinstance(self.unique_id, LoggedInPersonUniqueId):
            self.unique_id = LoggedInPersonUniqueId(self.unique_id)

        if self._is_empty(self.okta_id):
            self.MissingRequiredField("okta_id")
        if not isinstance(self.okta_id, str):
            self.okta_id = str(self.okta_id)

        if self._is_empty(self.okta_email):
            self.MissingRequiredField("okta_email")
        if not isinstance(self.okta_email, str):
            self.okta_email = str(self.okta_email)

        super().__post_init__(**kwargs)


@dataclass
class Figure(AuditedObject):
    """
    An entity representing a figure or table in a publication.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/image.yaml/Figure")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Figure"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/Figure")

    curie: Union[str, FigureCurie] = None
    internal: Union[bool, Bool] = None
    single_reference: Union[str, ReferenceCurie] = None
    label: Optional[str] = None
    caption: Optional[str] = None
    secondary_identifiers: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, FigureCurie):
            self.curie = FigureCurie(self.curie)

        if self._is_empty(self.single_reference):
            self.MissingRequiredField("single_reference")
        if not isinstance(self.single_reference, ReferenceCurie):
            self.single_reference = ReferenceCurie(self.single_reference)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.caption is not None and not isinstance(self.caption, str):
            self.caption = str(self.caption)

        if not isinstance(self.secondary_identifiers, list):
            self.secondary_identifiers = [self.secondary_identifiers] if self.secondary_identifiers is not None else []
        self.secondary_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.secondary_identifiers]

        super().__post_init__(**kwargs)


@dataclass
class File(AuditedObject):
    """
    A dummy object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/image.yaml/File")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "File"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/File")

    internal: Union[bool, Bool] = None

@dataclass
class Image(AuditedObject):
    """
    The set of files and metadata that constitute an image.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/image.yaml/Image")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Image"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/Image")

    curie: Union[str, ImageCurie] = None
    internal: Union[bool, Bool] = None
    associated_with_figure: Union[str, FigureCurie] = None
    width: int = None
    height: int = None
    image_file: Union[dict, File] = None
    image_medium_file: Union[dict, File] = None
    image_thumbnail_file: Union[dict, File] = None
    cropped_from: Optional[Union[str, ImageCurie]] = None
    image_x_origin: Optional[int] = None
    image_y_origin: Optional[int] = None
    video_still: Optional[Union[bool, Bool]] = None
    secondary_identifiers: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ImageCurie):
            self.curie = ImageCurie(self.curie)

        if self._is_empty(self.associated_with_figure):
            self.MissingRequiredField("associated_with_figure")
        if not isinstance(self.associated_with_figure, FigureCurie):
            self.associated_with_figure = FigureCurie(self.associated_with_figure)

        if self._is_empty(self.width):
            self.MissingRequiredField("width")
        if not isinstance(self.width, int):
            self.width = int(self.width)

        if self._is_empty(self.height):
            self.MissingRequiredField("height")
        if not isinstance(self.height, int):
            self.height = int(self.height)

        if self._is_empty(self.image_file):
            self.MissingRequiredField("image_file")
        if not isinstance(self.image_file, File):
            self.image_file = File(**as_dict(self.image_file))

        if self._is_empty(self.image_medium_file):
            self.MissingRequiredField("image_medium_file")
        if not isinstance(self.image_medium_file, File):
            self.image_medium_file = File(**as_dict(self.image_medium_file))

        if self._is_empty(self.image_thumbnail_file):
            self.MissingRequiredField("image_thumbnail_file")
        if not isinstance(self.image_thumbnail_file, File):
            self.image_thumbnail_file = File(**as_dict(self.image_thumbnail_file))

        if self.cropped_from is not None and not isinstance(self.cropped_from, ImageCurie):
            self.cropped_from = ImageCurie(self.cropped_from)

        if self.image_x_origin is not None and not isinstance(self.image_x_origin, int):
            self.image_x_origin = int(self.image_x_origin)

        if self.image_y_origin is not None and not isinstance(self.image_y_origin, int):
            self.image_y_origin = int(self.image_y_origin)

        if self.video_still is not None and not isinstance(self.video_still, Bool):
            self.video_still = Bool(self.video_still)

        if not isinstance(self.secondary_identifiers, list):
            self.secondary_identifiers = [self.secondary_identifiers] if self.secondary_identifiers is not None else []
        self.secondary_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.secondary_identifiers]

        super().__post_init__(**kwargs)


@dataclass
class ImagePane(AuditedObject):
    """
    Part of an Image that is relevant to some annotation. An annotation may reference many panes of an Image.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/image.yaml/ImagePane")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ImagePane"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/ImagePane")

    internal: Union[bool, Bool] = None
    from_image: Union[str, ImageCurie] = None
    width: int = None
    height: int = None
    label: Optional[str] = None
    image_x_origin: Optional[int] = None
    image_y_origin: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.from_image):
            self.MissingRequiredField("from_image")
        if not isinstance(self.from_image, ImageCurie):
            self.from_image = ImageCurie(self.from_image)

        if self._is_empty(self.width):
            self.MissingRequiredField("width")
        if not isinstance(self.width, int):
            self.width = int(self.width)

        if self._is_empty(self.height):
            self.MissingRequiredField("height")
        if not isinstance(self.height, int):
            self.height = int(self.height)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.image_x_origin is not None and not isinstance(self.image_x_origin, int):
            self.image_x_origin = int(self.image_x_origin)

        if self.image_y_origin is not None and not isinstance(self.image_y_origin, int):
            self.image_y_origin = int(self.image_y_origin)

        super().__post_init__(**kwargs)


@dataclass
class OntologyTerm(AuditedObject):
    """
    A concept or class in an ontology, vocabulary or thesaurus. Note, ontology terms can be found in multiple
    ontologies (ie: mireoting). defining_slots helps define an alternative key for ontology terms.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/OntologyTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "OntologyTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/OntologyTerm")

    curie: Union[str, OntologyTermCurie] = None
    internal: Union[bool, Bool] = None
    dbkey: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    definition_urls: Optional[Union[str, List[str]]] = empty_list()
    type: Optional[Union[str, URIorCURIE]] = None
    is_obsolete: Optional[Union[bool, Bool]] = None
    cross_references: Optional[Union[Dict[Union[str, CrossReferenceCurie], Union[dict, CrossReference]], List[Union[dict, CrossReference]]]] = empty_dict()
    synonyms: Optional[Union[Union[dict, Synonym], List[Union[dict, Synonym]]]] = empty_list()
    namespace: Optional[str] = None
    subsets: Optional[Union[str, List[str]]] = empty_list()
    secondary_identifiers: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, OntologyTermCurie):
            self.curie = OntologyTermCurie(self.curie)

        if self.dbkey is not None and not isinstance(self.dbkey, str):
            self.dbkey = str(self.dbkey)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if not isinstance(self.definition_urls, list):
            self.definition_urls = [self.definition_urls] if self.definition_urls is not None else []
        self.definition_urls = [v if isinstance(v, str) else str(v) for v in self.definition_urls]

        if self.type is not None and not isinstance(self.type, URIorCURIE):
            self.type = URIorCURIE(self.type)

        if self.is_obsolete is not None and not isinstance(self.is_obsolete, Bool):
            self.is_obsolete = Bool(self.is_obsolete)

        self._normalize_inlined_as_list(slot_name="cross_references", slot_type=CrossReference, key_name="curie", keyed=True)

        self._normalize_inlined_as_dict(slot_name="synonyms", slot_type=Synonym, key_name="internal", keyed=False)

        if self.namespace is not None and not isinstance(self.namespace, str):
            self.namespace = str(self.namespace)

        if not isinstance(self.subsets, list):
            self.subsets = [self.subsets] if self.subsets is not None else []
        self.subsets = [v if isinstance(v, str) else str(v) for v in self.subsets]

        if not isinstance(self.secondary_identifiers, list):
            self.secondary_identifiers = [self.secondary_identifiers] if self.secondary_identifiers is not None else []
        self.secondary_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.secondary_identifiers]

        super().__post_init__(**kwargs)


@dataclass
class DOTerm(OntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/DOTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DOTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/DOTerm")

    curie: Union[str, DOTermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, DOTermCurie):
            self.curie = DOTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class ECOTerm(OntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/ECOTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ECOTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/ECOTerm")

    curie: Union[str, ECOTermCurie] = None
    internal: Union[bool, Bool] = None
    abbreviation: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ECOTermCurie):
            self.curie = ECOTermCurie(self.curie)

        if self.abbreviation is not None and not isinstance(self.abbreviation, str):
            self.abbreviation = str(self.abbreviation)

        super().__post_init__(**kwargs)


@dataclass
class NCBITaxonTerm(OntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/NCBITaxonTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "NCBITaxonTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/NCBITaxonTerm")

    curie: Union[str, NCBITaxonTermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, NCBITaxonTermCurie):
            self.curie = NCBITaxonTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class FBCVTerm(OntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/FBCVTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "FBCVTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/FBCVTerm")

    curie: Union[str, FBCVTermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, FBCVTermCurie):
            self.curie = FBCVTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class GOTerm(OntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/GOTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "GOTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/GOTerm")

    curie: Union[str, GOTermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, GOTermCurie):
            self.curie = GOTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class ROTerm(OntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/ROTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ROTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/ROTerm")

    curie: Union[str, ROTermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ROTermCurie):
            self.curie = ROTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class MITerm(OntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/MITerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "MITerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/MITerm")

    curie: Union[str, MITermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, MITermCurie):
            self.curie = MITermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class MMOTerm(OntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/MMOTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "MMOTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/MMOTerm")

    curie: Union[str, MMOTermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, MMOTermCurie):
            self.curie = MMOTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class MMUSDVTerm(OntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/MMUSDVTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "MMUSDVTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/MMUSDVTerm")

    curie: Union[str, MMUSDVTermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, MMUSDVTermCurie):
            self.curie = MMUSDVTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class SOTerm(OntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/SOTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SOTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/SOTerm")

    curie: Union[str, SOTermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, SOTermCurie):
            self.curie = SOTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class XBEDTerm(OntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/XBEDTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "XBEDTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/XBEDTerm")

    curie: Union[str, XBEDTermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, XBEDTermCurie):
            self.curie = XBEDTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class StageTerm(OntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/StageTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "StageTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/StageTerm")

    curie: Union[str, StageTermCurie] = None
    internal: Union[bool, Bool] = None

@dataclass
class FBDVTerm(StageTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/FBDVTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "FBDVTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/FBDVTerm")

    curie: Union[str, FBDVTermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, FBDVTermCurie):
            self.curie = FBDVTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class WBLSTerm(StageTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/WBLSTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "WBLSTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/WBLSTerm")

    curie: Union[str, WBLSTermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, WBLSTermCurie):
            self.curie = WBLSTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class XBSTerm(StageTerm):
    """
    The Xenbase anatomy ontology XAO is home to Xenopus anatomy terms as well as Xenopus developmental life stage
    terms, differentiated by namespace. The anatomy term class in LinkML will be named 'XBATerm' for Xenbase Anatomy
    Term and life stage terms will be named 'XBSTerm' for Xenbase Stage Term.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/XBSTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "XBSTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/XBSTerm")

    curie: Union[str, XBSTermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, XBSTermCurie):
            self.curie = XBSTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class ZFSTerm(StageTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/ZFSTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ZFSTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/ZFSTerm")

    curie: Union[str, ZFSTermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ZFSTermCurie):
            self.curie = ZFSTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class ExperimentalConditionOntologyTerm(OntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/ExperimentalConditionOntologyTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ExperimentalConditionOntologyTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/ExperimentalConditionOntologyTerm")

    curie: Union[str, ExperimentalConditionOntologyTermCurie] = None
    internal: Union[bool, Bool] = None

@dataclass
class ZECOTerm(ExperimentalConditionOntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/ZECOTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ZECOTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/ZECOTerm")

    curie: Union[str, ZECOTermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ZECOTermCurie):
            self.curie = ZECOTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class XCOTerm(ExperimentalConditionOntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/XCOTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "XCOTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/XCOTerm")

    curie: Union[str, XCOTermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, XCOTermCurie):
            self.curie = XCOTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class AnatomicalTerm(OntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/AnatomicalTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AnatomicalTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/AnatomicalTerm")

    curie: Union[str, AnatomicalTermCurie] = None
    internal: Union[bool, Bool] = None

@dataclass
class CLTerm(AnatomicalTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/CLTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CLTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/CLTerm")

    curie: Union[str, CLTermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, CLTermCurie):
            self.curie = CLTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class EMAPATerm(AnatomicalTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/EMAPATerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "EMAPATerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/EMAPATerm")

    curie: Union[str, EMAPATermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, EMAPATermCurie):
            self.curie = EMAPATermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class DAOTerm(AnatomicalTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/DAOTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DAOTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/DAOTerm")

    curie: Union[str, DAOTermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, DAOTermCurie):
            self.curie = DAOTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class MATerm(AnatomicalTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/MATerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "MATerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/MATerm")

    curie: Union[str, MATermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, MATermCurie):
            self.curie = MATermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class UBERONTerm(AnatomicalTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/UBERONTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "UBERONTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/UBERONTerm")

    curie: Union[str, UBERONTermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, UBERONTermCurie):
            self.curie = UBERONTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class WBBTTerm(AnatomicalTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/WBBTTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "WBBTTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/WBBTTerm")

    curie: Union[str, WBBTTermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, WBBTTermCurie):
            self.curie = WBBTTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class XBATerm(AnatomicalTerm):
    """
    The Xenbase anatomy ontology XAO is home to Xenopus anatomy terms as well as Xenopus developmental life stage
    terms, differentiated by namespace. The anatomy term class in LinkML will be named 'XBATerm' for Xenbase Anatomy
    Term and life stage terms will be named 'XBSTerm' for Xenbase Stage Term.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/XBATerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "XBATerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/XBATerm")

    curie: Union[str, XBATermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, XBATermCurie):
            self.curie = XBATermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class ZFATerm(AnatomicalTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/ZFATerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ZFATerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/ZFATerm")

    curie: Union[str, ZFATermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ZFATermCurie):
            self.curie = ZFATermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class PhenotypeTerm(OntologyTerm):
    """
    An ontology term representing a characteristic of an organism. This may or may not be expressed as a difference in
    comparison to a reference organism.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/PhenotypeTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "PhenotypeTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/PhenotypeTerm")

    curie: Union[str, PhenotypeTermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, PhenotypeTermCurie):
            self.curie = PhenotypeTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class XPOTerm(PhenotypeTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/XPOTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "XPOTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/XPOTerm")

    curie: Union[str, XPOTermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, XPOTermCurie):
            self.curie = XPOTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalTerm(OntologyTerm):
    """
    An ontology term representing a chemical or molecule
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/ChemicalTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ChemicalTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/ChemicalTerm")

    curie: Union[str, ChemicalTermCurie] = None
    internal: Union[bool, Bool] = None
    inchi: Optional[str] = None
    inchi_key: Optional[str] = None
    iupac: Optional[str] = None
    formula: Optional[str] = None
    smiles: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.inchi is not None and not isinstance(self.inchi, str):
            self.inchi = str(self.inchi)

        if self.inchi_key is not None and not isinstance(self.inchi_key, str):
            self.inchi_key = str(self.inchi_key)

        if self.iupac is not None and not isinstance(self.iupac, str):
            self.iupac = str(self.iupac)

        if self.formula is not None and not isinstance(self.formula, str):
            self.formula = str(self.formula)

        if self.smiles is not None and not isinstance(self.smiles, str):
            self.smiles = str(self.smiles)

        super().__post_init__(**kwargs)


@dataclass
class CHEBITerm(ChemicalTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/CHEBITerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CHEBITerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/CHEBITerm")

    curie: Union[str, CHEBITermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, CHEBITermCurie):
            self.curie = CHEBITermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class XSMOTerm(ChemicalTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/XSMOTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "XSMOTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/XSMOTerm")

    curie: Union[str, XSMOTermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, XSMOTermCurie):
            self.curie = XSMOTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class Molecule(ChemicalTerm):
    """
    Molecules as described by WormBase
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/Molecule")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Molecule"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/Molecule")

    curie: Union[str, MoleculeCurie] = None
    internal: Union[bool, Bool] = None
    table_key: Optional[int] = None
    created_by: Optional[Union[str, PersonUniqueId]] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    modified_by: Optional[Union[str, PersonUniqueId]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, MoleculeCurie):
            self.curie = MoleculeCurie(self.curie)

        if self._is_empty(self.internal):
            self.MissingRequiredField("internal")
        if not isinstance(self.internal, Bool):
            self.internal = Bool(self.internal)

        if self.table_key is not None and not isinstance(self.table_key, int):
            self.table_key = int(self.table_key)

        if self.created_by is not None and not isinstance(self.created_by, PersonUniqueId):
            self.created_by = PersonUniqueId(self.created_by)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.modified_by is not None and not isinstance(self.modified_by, PersonUniqueId):
            self.modified_by = PersonUniqueId(self.modified_by)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

        super().__post_init__(**kwargs)


@dataclass
class VocabularyTerm(AuditedObject):
    """
    A concept or class in a simple vocabulary.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/controlledVocabulary.yaml/VocabularyTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "VocabularyTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/VocabularyTerm")

    name: Union[str, VocabularyTermName] = None
    internal: Union[bool, Bool] = None
    abbreviation: Optional[str] = None
    definition: Optional[str] = None
    is_obsolete: Optional[Union[bool, Bool]] = None
    text_synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, VocabularyTermName):
            self.name = VocabularyTermName(self.name)

        if self.abbreviation is not None and not isinstance(self.abbreviation, str):
            self.abbreviation = str(self.abbreviation)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.is_obsolete is not None and not isinstance(self.is_obsolete, Bool):
            self.is_obsolete = Bool(self.is_obsolete)

        if not isinstance(self.text_synonyms, list):
            self.text_synonyms = [self.text_synonyms] if self.text_synonyms is not None else []
        self.text_synonyms = [v if isinstance(v, str) else str(v) for v in self.text_synonyms]

        super().__post_init__(**kwargs)


@dataclass
class Vocabulary(AuditedObject):
    """
    A set of VocabularyTerm objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/controlledVocabulary.yaml/Vocabulary")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Vocabulary"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/Vocabulary")

    name: Union[str, VocabularyName] = None
    internal: Union[bool, Bool] = None
    vocabulary_description: Optional[str] = None
    is_obsolete: Optional[Union[bool, Bool]] = None
    member_terms: Optional[Union[Union[str, VocabularyTermName], List[Union[str, VocabularyTermName]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, VocabularyName):
            self.name = VocabularyName(self.name)

        if self.vocabulary_description is not None and not isinstance(self.vocabulary_description, str):
            self.vocabulary_description = str(self.vocabulary_description)

        if self.is_obsolete is not None and not isinstance(self.is_obsolete, Bool):
            self.is_obsolete = Bool(self.is_obsolete)

        if not isinstance(self.member_terms, list):
            self.member_terms = [self.member_terms] if self.member_terms is not None else []
        self.member_terms = [v if isinstance(v, VocabularyTermName) else VocabularyTermName(v) for v in self.member_terms]

        super().__post_init__(**kwargs)


@dataclass
class Allele(GenomicEntity):
    """
    One of multiple possible forms of a functional genomic element (most often described as a locus or gene),
    differing from the reference DNA sequence. The genomic element can be endogenous or constructed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/Allele")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Allele"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/Allele")

    curie: Union[str, AlleleCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None
    name: str = None
    symbol: Optional[str] = None
    contains_constructs: Optional[Union[Union[str, ConstructCurie], List[Union[str, ConstructCurie]]]] = empty_list()
    molecular_mutations: Optional[Union[str, List[str]]] = empty_list()
    functional_impact: Optional[str] = None
    generation_method: Optional[str] = None
    associated_references: Optional[Union[Union[dict, "AssociatedReference"], List[Union[dict, "AssociatedReference"]]]] = empty_list()
    related_notes: Optional[Union[Union[dict, Note], List[Union[dict, Note]]]] = empty_list()
    germline_transmission_status: Optional[Union[str, VocabularyTermName]] = None
    parent_cell_line: Optional[Union[dict, "CellLine"]] = None
    mutant_cell_lines: Optional[Union[Union[dict, "CellLine"], List[Union[dict, "CellLine"]]]] = empty_list()
    embryonic_stem_cell_lines: Optional[Union[Union[dict, "CellLine"], List[Union[dict, "CellLine"]]]] = empty_list()
    images: Optional[Union[str, ImageCurie]] = None
    origins: Optional[Union[Union[str, AffectedGenomicModelCurie], List[Union[str, AffectedGenomicModelCurie]]]] = empty_list()
    database_status: Optional[Union[str, VocabularyTermName]] = None
    inheritence_mode: Optional[Union[str, VocabularyTermName]] = None
    in_collection: Optional[Union[str, VocabularyTermName]] = None
    transposon_insertion: Optional[str] = None
    aberration: Optional[str] = None
    is_extinct: Optional[Union[bool, Bool]] = None
    sequencing_status: Optional[Union[str, VocabularyTermName]] = None
    synonyms: Optional[Union[Union[dict, Synonym], List[Union[dict, Synonym]]]] = empty_list()
    embryonic_cell_lines: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, AlleleCurie):
            self.curie = AlleleCurie(self.curie)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.symbol is not None and not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        if not isinstance(self.contains_constructs, list):
            self.contains_constructs = [self.contains_constructs] if self.contains_constructs is not None else []
        self.contains_constructs = [v if isinstance(v, ConstructCurie) else ConstructCurie(v) for v in self.contains_constructs]

        if not isinstance(self.molecular_mutations, list):
            self.molecular_mutations = [self.molecular_mutations] if self.molecular_mutations is not None else []
        self.molecular_mutations = [v if isinstance(v, str) else str(v) for v in self.molecular_mutations]

        if self.functional_impact is not None and not isinstance(self.functional_impact, str):
            self.functional_impact = str(self.functional_impact)

        if self.generation_method is not None and not isinstance(self.generation_method, str):
            self.generation_method = str(self.generation_method)

        self._normalize_inlined_as_dict(slot_name="associated_references", slot_type=AssociatedReference, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="related_notes", slot_type=Note, key_name="internal", keyed=False)

        if self.germline_transmission_status is not None and not isinstance(self.germline_transmission_status, VocabularyTermName):
            self.germline_transmission_status = VocabularyTermName(self.germline_transmission_status)

        if self.parent_cell_line is not None and not isinstance(self.parent_cell_line, CellLine):
            self.parent_cell_line = CellLine(**as_dict(self.parent_cell_line))

        self._normalize_inlined_as_dict(slot_name="mutant_cell_lines", slot_type=CellLine, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="embryonic_stem_cell_lines", slot_type=CellLine, key_name="internal", keyed=False)

        if self.images is not None and not isinstance(self.images, ImageCurie):
            self.images = ImageCurie(self.images)

        if not isinstance(self.origins, list):
            self.origins = [self.origins] if self.origins is not None else []
        self.origins = [v if isinstance(v, AffectedGenomicModelCurie) else AffectedGenomicModelCurie(v) for v in self.origins]

        if self.database_status is not None and not isinstance(self.database_status, VocabularyTermName):
            self.database_status = VocabularyTermName(self.database_status)

        if self.inheritence_mode is not None and not isinstance(self.inheritence_mode, VocabularyTermName):
            self.inheritence_mode = VocabularyTermName(self.inheritence_mode)

        if self.in_collection is not None and not isinstance(self.in_collection, VocabularyTermName):
            self.in_collection = VocabularyTermName(self.in_collection)

        if self.transposon_insertion is not None and not isinstance(self.transposon_insertion, str):
            self.transposon_insertion = str(self.transposon_insertion)

        if self.aberration is not None and not isinstance(self.aberration, str):
            self.aberration = str(self.aberration)

        if self.is_extinct is not None and not isinstance(self.is_extinct, Bool):
            self.is_extinct = Bool(self.is_extinct)

        if self.sequencing_status is not None and not isinstance(self.sequencing_status, VocabularyTermName):
            self.sequencing_status = VocabularyTermName(self.sequencing_status)

        self._normalize_inlined_as_dict(slot_name="synonyms", slot_type=Synonym, key_name="internal", keyed=False)

        if self.embryonic_cell_lines is not None and not isinstance(self.embryonic_cell_lines, str):
            self.embryonic_cell_lines = str(self.embryonic_cell_lines)

        super().__post_init__(**kwargs)


@dataclass
class AlleleGenomicEntityAssociation(Association):
    """
    Association between an allele and a genomic entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/AlleleGenomicEntityAssociation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AlleleGenomicEntityAssociation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/AlleleGenomicEntityAssociation")

    internal: Union[bool, Bool] = None
    subject: Union[str, AlleleCurie] = None
    predicate: Union[str, ROTermCurie] = None
    object: Union[str, GenomicEntityCurie] = None
    table_key: Optional[int] = None
    created_by: Optional[Union[str, PersonUniqueId]] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    modified_by: Optional[Union[str, PersonUniqueId]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None
    single_reference: Optional[Union[str, ReferenceCurie]] = None
    evidence_code: Optional[Union[str, ECOTermCurie]] = None
    related_note: Optional[Union[dict, Note]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.internal):
            self.MissingRequiredField("internal")
        if not isinstance(self.internal, Bool):
            self.internal = Bool(self.internal)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, AlleleCurie):
            self.subject = AlleleCurie(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, ROTermCurie):
            self.predicate = ROTermCurie(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GenomicEntityCurie):
            self.object = GenomicEntityCurie(self.object)

        if self.table_key is not None and not isinstance(self.table_key, int):
            self.table_key = int(self.table_key)

        if self.created_by is not None and not isinstance(self.created_by, PersonUniqueId):
            self.created_by = PersonUniqueId(self.created_by)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.modified_by is not None and not isinstance(self.modified_by, PersonUniqueId):
            self.modified_by = PersonUniqueId(self.modified_by)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

        if self.single_reference is not None and not isinstance(self.single_reference, ReferenceCurie):
            self.single_reference = ReferenceCurie(self.single_reference)

        if self.evidence_code is not None and not isinstance(self.evidence_code, ECOTermCurie):
            self.evidence_code = ECOTermCurie(self.evidence_code)

        if self.related_note is not None and not isinstance(self.related_note, Note):
            self.related_note = Note(**as_dict(self.related_note))

        super().__post_init__(**kwargs)


@dataclass
class AlleleGeneAssociation(AlleleGenomicEntityAssociation):
    """
    Association between an allele and a gene
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/AlleleGeneAssociation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AlleleGeneAssociation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/AlleleGeneAssociation")

    internal: Union[bool, Bool] = None
    subject: Union[str, AlleleCurie] = None
    predicate: Union[str, ROTermCurie] = None
    object: Union[str, GeneCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GeneCurie):
            self.object = GeneCurie(self.object)

        super().__post_init__(**kwargs)


@dataclass
class AlleleTranscriptAssociation(AlleleGenomicEntityAssociation):
    """
    Association between an allele and a transcript
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/AlleleTranscriptAssociation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AlleleTranscriptAssociation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/AlleleTranscriptAssociation")

    internal: Union[bool, Bool] = None
    subject: Union[str, AlleleCurie] = None
    predicate: Union[str, ROTermCurie] = None
    object: Union[str, TranscriptCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, TranscriptCurie):
            self.object = TranscriptCurie(self.object)

        super().__post_init__(**kwargs)


@dataclass
class AlleleProteinAssociation(AlleleGenomicEntityAssociation):
    """
    Association between an allele and a protein
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/AlleleProteinAssociation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AlleleProteinAssociation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/AlleleProteinAssociation")

    internal: Union[bool, Bool] = None
    subject: Union[str, AlleleCurie] = None
    predicate: Union[str, ROTermCurie] = None
    object: Union[str, ProteinCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ProteinCurie):
            self.object = ProteinCurie(self.object)

        super().__post_init__(**kwargs)


@dataclass
class AlleleVariantAssociation(AlleleGenomicEntityAssociation):
    """
    The relationship between an allele and a variant is many to many. An Allele may have many variants and a variant
    can be present in many alleles.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/AlleleVariantAssociation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AlleleVariantAssociation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/AlleleVariantAssociation")

    internal: Union[bool, Bool] = None
    predicate: Union[str, ROTermCurie] = None
    subject: Union[str, AlleleCurie] = None
    object: Union[str, VariantCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, AlleleCurie):
            self.subject = AlleleCurie(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, VariantCurie):
            self.object = VariantCurie(self.object)

        super().__post_init__(**kwargs)


@dataclass
class AssociatedReference(AuditedObject):
    """
    Describes the relation between a reference and an object
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/AssociatedReference")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AssociatedReference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/AssociatedReference")

    internal: Union[bool, Bool] = None
    reference_type: Union[str, VocabularyTermName] = None
    single_reference: Optional[Union[str, ReferenceCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.reference_type):
            self.MissingRequiredField("reference_type")
        if not isinstance(self.reference_type, VocabularyTermName):
            self.reference_type = VocabularyTermName(self.reference_type)

        if self.single_reference is not None and not isinstance(self.single_reference, ReferenceCurie):
            self.single_reference = ReferenceCurie(self.single_reference)

        super().__post_init__(**kwargs)


@dataclass
class Construct(GenomicEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/Construct")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Construct"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/Construct")

    curie: Union[str, ConstructCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None
    name: str = None
    construct_components: Optional[Union[Union[str, GenomicEntityCurie], List[Union[str, GenomicEntityCurie]]]] = empty_list()
    references: Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ConstructCurie):
            self.curie = ConstructCurie(self.curie)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.construct_components, list):
            self.construct_components = [self.construct_components] if self.construct_components is not None else []
        self.construct_components = [v if isinstance(v, GenomicEntityCurie) else GenomicEntityCurie(v) for v in self.construct_components]

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, ReferenceCurie) else ReferenceCurie(v) for v in self.references]

        super().__post_init__(**kwargs)


@dataclass
class CellLine(AuditedObject):
    """
    Dummy cell line class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/CellLine")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CellLine"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/CellLine")

    internal: Union[bool, Bool] = None

@dataclass
class SequenceTargetingReagent(GenomicEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/SequenceTargetingReagent")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SequenceTargetingReagent"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/SequenceTargetingReagent")

    curie: Union[str, SequenceTargetingReagentCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None
    name: str = None
    references: Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, SequenceTargetingReagentCurie):
            self.curie = SequenceTargetingReagentCurie(self.curie)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, ReferenceCurie) else ReferenceCurie(v) for v in self.references]

        super().__post_init__(**kwargs)


@dataclass
class SequenceTargetingReagentToGeneAssociation(Association):
    """
    the relationship between a Sequence Targeting Reagent and its targeted genes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/SequenceTargetingReagentToGeneAssociation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SequenceTargetingReagentToGeneAssociation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/SequenceTargetingReagentToGeneAssociation")

    internal: Union[bool, Bool] = None
    predicate: Union[str, "SqtrRelationEnum"] = None
    subject: Union[str, SequenceTargetingReagentCurie] = None
    object: Union[str, GeneCurie] = None
    references: Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, SqtrRelationEnum):
            self.predicate = SqtrRelationEnum(self.predicate)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, SequenceTargetingReagentCurie):
            self.subject = SequenceTargetingReagentCurie(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GeneCurie):
            self.object = GeneCurie(self.object)

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, ReferenceCurie) else ReferenceCurie(v) for v in self.references]

        super().__post_init__(**kwargs)


@dataclass
class ConstructComponentAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/ConstructComponentAssociation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ConstructComponentAssociation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/ConstructComponentAssociation")

    internal: Union[bool, Bool] = None
    predicate: Union[str, "ConstructComponentRelationEnum"] = None
    subject: Union[str, ConstructCurie] = None
    object: Union[str, ConstructComponentCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, ConstructComponentRelationEnum):
            self.predicate = ConstructComponentRelationEnum(self.predicate)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ConstructCurie):
            self.subject = ConstructCurie(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ConstructComponentCurie):
            self.object = ConstructComponentCurie(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ConstructComponent(GenomicEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/ConstructComponent")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ConstructComponent"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/ConstructComponent")

    curie: Union[str, ConstructComponentCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None
    symbol: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ConstructComponentCurie):
            self.curie = ConstructComponentCurie(self.curie)

        if self.symbol is not None and not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        super().__post_init__(**kwargs)


@dataclass
class AffectedGenomicModel(GenomicEntity):
    """
    Includes inbred strains, stocks, disease models and mutant genotypes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/affectedGenomicModel/AffectedGenomicModel")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AffectedGenomicModel"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/AffectedGenomicModel")

    curie: Union[str, AffectedGenomicModelCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None
    subtype: Union[str, "SubtypeValues"] = None
    components: Optional[Union[Union[dict, "AffectedGenomicModelComponent"], List[Union[dict, "AffectedGenomicModelComponent"]]]] = empty_list()
    sequence_targeting_reagents: Optional[Union[Union[str, SequenceTargetingReagentCurie], List[Union[str, SequenceTargetingReagentCurie]]]] = empty_list()
    parental_populations: Optional[Union[str, URIorCURIE]] = None
    data_provider: Optional[str] = None
    references: Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, AffectedGenomicModelCurie):
            self.curie = AffectedGenomicModelCurie(self.curie)

        if self._is_empty(self.subtype):
            self.MissingRequiredField("subtype")
        if not isinstance(self.subtype, SubtypeValues):
            self.subtype = SubtypeValues(self.subtype)

        self._normalize_inlined_as_dict(slot_name="components", slot_type=AffectedGenomicModelComponent, key_name="internal", keyed=False)

        if not isinstance(self.sequence_targeting_reagents, list):
            self.sequence_targeting_reagents = [self.sequence_targeting_reagents] if self.sequence_targeting_reagents is not None else []
        self.sequence_targeting_reagents = [v if isinstance(v, SequenceTargetingReagentCurie) else SequenceTargetingReagentCurie(v) for v in self.sequence_targeting_reagents]

        if self.parental_populations is not None and not isinstance(self.parental_populations, URIorCURIE):
            self.parental_populations = URIorCURIE(self.parental_populations)

        if self.data_provider is not None and not isinstance(self.data_provider, str):
            self.data_provider = str(self.data_provider)

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, ReferenceCurie) else ReferenceCurie(v) for v in self.references]

        super().__post_init__(**kwargs)


@dataclass
class AffectedGenomicModelComponent(AuditedObject):
    """
    Allele that affects the model and its zygosity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/affectedGenomicModel/AffectedGenomicModelComponent")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AffectedGenomicModelComponent"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/AffectedGenomicModelComponent")

    internal: Union[bool, Bool] = None
    has_allele: Optional[Union[str, AlleleCurie]] = None
    zygosity: Optional[Union[str, "ZygosityValues"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_allele is not None and not isinstance(self.has_allele, AlleleCurie):
            self.has_allele = AlleleCurie(self.has_allele)

        if self.zygosity is not None and not isinstance(self.zygosity, ZygosityValues):
            self.zygosity = ZygosityValues(self.zygosity)

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

class EntitySynonymTypeSet(EnumDefinitionImpl):

    current = PermissibleValue(text="current",
                                     description="The synonym is an officially accepted synonym for an entity. An entity should have only one current synonym of a give type. For example, only one current symbol and one current full name.")
    alias = PermissibleValue(text="alias",
                                 description="The synonym is an alternate symbol or name for the entity. It is not the currently preferred symbol/name for the entity.")

    _defn = EnumDefinition(
        name="EntitySynonymTypeSet",
    )

class VariantStatusEnum(EnumDefinitionImpl):

    public = PermissibleValue(text="public")
    private = PermissibleValue(text="private")

    _defn = EnumDefinition(
        name="VariantStatusEnum",
    )

class PubmedPublicationStatusEnum(EnumDefinitionImpl):

    ppublish = PermissibleValue(text="ppublish")
    epublish = PermissibleValue(text="epublish")
    aheadofprint = PermissibleValue(text="aheadofprint")

    _defn = EnumDefinition(
        name="PubmedPublicationStatusEnum",
    )

class PubmedTypeEnum(EnumDefinitionImpl):

    Address = PermissibleValue(text="Address")
    Autobiography = PermissibleValue(text="Autobiography")
    Bibliography = PermissibleValue(text="Bibliography")
    Biography = PermissibleValue(text="Biography")
    Comment = PermissibleValue(text="Comment")
    Congress = PermissibleValue(text="Congress")
    Dataset = PermissibleValue(text="Dataset")
    Dictionary = PermissibleValue(text="Dictionary")
    Directory = PermissibleValue(text="Directory")
    Editorial = PermissibleValue(text="Editorial")
    Festschrift = PermissibleValue(text="Festschrift")
    Guideline = PermissibleValue(text="Guideline")
    Interview = PermissibleValue(text="Interview")
    Lecture = PermissibleValue(text="Lecture")
    Legislation = PermissibleValue(text="Legislation")
    Letter = PermissibleValue(text="Letter")
    News = PermissibleValue(text="News")
    Overall = PermissibleValue(text="Overall")
    Portrait = PermissibleValue(text="Portrait")
    Preprint = PermissibleValue(text="Preprint")
    Review = PermissibleValue(text="Review")
    Webcast = PermissibleValue(text="Webcast")

    _defn = EnumDefinition(
        name="PubmedTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Adaptive Clinical Trial",
                PermissibleValue(text="Adaptive Clinical Trial") )
        setattr(cls, "Case Reports",
                PermissibleValue(text="Case Reports") )
        setattr(cls, "Classical Article",
                PermissibleValue(text="Classical Article") )
        setattr(cls, "Clinical Conference",
                PermissibleValue(text="Clinical Conference") )
        setattr(cls, "Clinical Study",
                PermissibleValue(text="Clinical Study") )
        setattr(cls, "Clinical Trial",
                PermissibleValue(text="Clinical Trial") )
        setattr(cls, "Clinical Trial, Phase I",
                PermissibleValue(text="Clinical Trial, Phase I") )
        setattr(cls, "Clinical Trial, Phase II",
                PermissibleValue(text="Clinical Trial, Phase II") )
        setattr(cls, "Clinical Trial, Phase III",
                PermissibleValue(text="Clinical Trial, Phase III") )
        setattr(cls, "Clinical Trial, Phase IV",
                PermissibleValue(text="Clinical Trial, Phase IV") )
        setattr(cls, "Clinical Trial Protocol",
                PermissibleValue(text="Clinical Trial Protocol") )
        setattr(cls, "Clinical Trial, Veterinary",
                PermissibleValue(text="Clinical Trial, Veterinary") )
        setattr(cls, "Collected Work",
                PermissibleValue(text="Collected Work") )
        setattr(cls, "Comparative Study",
                PermissibleValue(text="Comparative Study") )
        setattr(cls, "Consensus Development Conference",
                PermissibleValue(text="Consensus Development Conference") )
        setattr(cls, "Consensus Development Conference, NIH",
                PermissibleValue(text="Consensus Development Conference, NIH") )
        setattr(cls, "Controlled Clinical Trial",
                PermissibleValue(text="Controlled Clinical Trial") )
        setattr(cls, "Corrected and Republished Article",
                PermissibleValue(text="Corrected and Republished Article") )
        setattr(cls, "Duplicate Publication",
                PermissibleValue(text="Duplicate Publication") )
        setattr(cls, "Electronic Supplementary Materials",
                PermissibleValue(text="Electronic Supplementary Materials") )
        setattr(cls, "English Abstract",
                PermissibleValue(text="English Abstract") )
        setattr(cls, "Equivalence Trial",
                PermissibleValue(text="Equivalence Trial") )
        setattr(cls, "Evaluation Study",
                PermissibleValue(text="Evaluation Study") )
        setattr(cls, "Expression of Concern",
                PermissibleValue(text="Expression of Concern") )
        setattr(cls, "Government Publication",
                PermissibleValue(text="Government Publication") )
        setattr(cls, "Historical Article",
                PermissibleValue(text="Historical Article") )
        setattr(cls, "Interactive Tutorial",
                PermissibleValue(text="Interactive Tutorial") )
        setattr(cls, "Introductory Journal Article",
                PermissibleValue(text="Introductory Journal Article") )
        setattr(cls, "Journal Article",
                PermissibleValue(text="Journal Article") )
        setattr(cls, "Legal Case",
                PermissibleValue(text="Legal Case") )
        setattr(cls, "Meta-Analysis",
                PermissibleValue(text="Meta-Analysis") )
        setattr(cls, "Multicenter Study",
                PermissibleValue(text="Multicenter Study") )
        setattr(cls, "Newspaper Article",
                PermissibleValue(text="Newspaper Article") )
        setattr(cls, "Observational Study",
                PermissibleValue(text="Observational Study") )
        setattr(cls, "Observational Study, Veterinary",
                PermissibleValue(text="Observational Study, Veterinary") )
        setattr(cls, "Patient Education Handout",
                PermissibleValue(text="Patient Education Handout") )
        setattr(cls, "Periodical Index",
                PermissibleValue(text="Periodical Index") )
        setattr(cls, "Personal Narrative",
                PermissibleValue(text="Personal Narrative") )
        setattr(cls, "Practice Guideline",
                PermissibleValue(text="Practice Guideline") )
        setattr(cls, "Pragmatic Clinical Trial",
                PermissibleValue(text="Pragmatic Clinical Trial") )
        setattr(cls, "Published Erratum",
                PermissibleValue(text="Published Erratum") )
        setattr(cls, "Randomized Controlled Trial",
                PermissibleValue(text="Randomized Controlled Trial") )
        setattr(cls, "Randomized Controlled Trial, Veterinary",
                PermissibleValue(text="Randomized Controlled Trial, Veterinary") )
        setattr(cls, "Research Support, American Recovery and Reinvestment Act",
                PermissibleValue(text="Research Support, American Recovery and Reinvestment Act") )
        setattr(cls, "Research Support, N.I.H., Extramural",
                PermissibleValue(text="Research Support, N.I.H., Extramural") )
        setattr(cls, "Research Support, N.I.H., Intramural",
                PermissibleValue(text="Research Support, N.I.H., Intramural") )
        setattr(cls, "Research Support, Non-U.S. Gov't",
                PermissibleValue(text="Research Support, Non-U.S. Gov't") )
        setattr(cls, "Research Support, U.S. Gov't, Non-P.H.S.",
                PermissibleValue(text="Research Support, U.S. Gov't, Non-P.H.S.") )
        setattr(cls, "Research Support, U.S. Gov't, P.H.S.",
                PermissibleValue(text="Research Support, U.S. Gov't, P.H.S.") )
        setattr(cls, "Retracted Publication",
                PermissibleValue(text="Retracted Publication") )
        setattr(cls, "Retraction of Publication",
                PermissibleValue(text="Retraction of Publication") )
        setattr(cls, "Scientific Integrity Review",
                PermissibleValue(text="Scientific Integrity Review") )
        setattr(cls, "Systematic Review",
                PermissibleValue(text="Systematic Review") )
        setattr(cls, "Technical Report",
                PermissibleValue(text="Technical Report") )
        setattr(cls, "Twin Study",
                PermissibleValue(text="Twin Study") )
        setattr(cls, "Validation Study",
                PermissibleValue(text="Validation Study") )
        setattr(cls, "Video-Audio Media",
                PermissibleValue(text="Video-Audio Media") )

class ReferenceCategoryEnum(EnumDefinitionImpl):

    Research_Article = PermissibleValue(text="Research_Article")
    Review_Article = PermissibleValue(text="Review_Article")
    Thesis = PermissibleValue(text="Thesis")
    Book = PermissibleValue(text="Book")
    Other = PermissibleValue(text="Other")
    Preprint = PermissibleValue(text="Preprint")
    Conference_Publication = PermissibleValue(text="Conference_Publication")
    Personal_Communication = PermissibleValue(text="Personal_Communication")
    Direct_Data_Submission = PermissibleValue(text="Direct_Data_Submission")
    Internal_Process_Reference = PermissibleValue(text="Internal_Process_Reference")
    Unknown = PermissibleValue(text="Unknown")
    Retraction = PermissibleValue(text="Retraction")

    _defn = EnumDefinition(
        name="ReferenceCategoryEnum",
    )

class ConstructComponentRelationEnum(EnumDefinitionImpl):

    expresses = PermissibleValue(text="expresses",
                                         meaning=RO["0002292"])
    is_regulated_by = PermissibleValue(text="is_regulated_by",
                                                     meaning=RO["0002334"])
    targets = PermissibleValue(text="targets",
                                     meaning=RO["0002436"])

    _defn = EnumDefinition(
        name="ConstructComponentRelationEnum",
    )

class SqtrRelationEnum(EnumDefinitionImpl):

    targets = PermissibleValue(text="targets")

    _defn = EnumDefinition(
        name="SqtrRelationEnum",
    )

class SubtypeValues(EnumDefinitionImpl):

    strain = PermissibleValue(text="strain")
    genotype = PermissibleValue(text="genotype")
    fish = PermissibleValue(text="fish")

    _defn = EnumDefinition(
        name="SubtypeValues",
    )

class ZygosityValues(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ZygosityValues",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "GENO:0000602",
                PermissibleValue(text="GENO:0000602") )
        setattr(cls, "GENO:0000603",
                PermissibleValue(text="GENO:0000603") )
        setattr(cls, "GENO:0000604",
                PermissibleValue(text="GENO:0000604") )
        setattr(cls, "GENO:0000605",
                PermissibleValue(text="GENO:0000605") )
        setattr(cls, "GENO:0000606",
                PermissibleValue(text="GENO:0000606") )
        setattr(cls, "GENO:0000135",
                PermissibleValue(text="GENO:0000135") )
        setattr(cls, "GENO:0000136",
                PermissibleValue(text="GENO:0000136") )
        setattr(cls, "GENO:0000137",
                PermissibleValue(text="GENO:0000137") )
        setattr(cls, "GENO:0000134",
                PermissibleValue(text="GENO:0000134") )

# Slots
class slots:
    pass

slots.vep_impact = Slot(uri=DEFAULT_.vep_impact, name="vep_impact", curie=DEFAULT_.curie('vep_impact'),
                   model_uri=DEFAULT_.vep_impact, domain=None, range=Optional[str])

slots.vep_consequence = Slot(uri=DEFAULT_.vep_consequence, name="vep_consequence", curie=DEFAULT_.curie('vep_consequence'),
                   model_uri=DEFAULT_.vep_consequence, domain=None, range=Optional[Union[str, "VepConsequenceLevels"]])

slots.polyphen_score = Slot(uri=DEFAULT_.polyphen_score, name="polyphen_score", curie=DEFAULT_.curie('polyphen_score'),
                   model_uri=DEFAULT_.polyphen_score, domain=VariantGeneConsequence, range=Optional[float])

slots.polyphen_prediction = Slot(uri=DEFAULT_.polyphen_prediction, name="polyphen_prediction", curie=DEFAULT_.curie('polyphen_prediction'),
                   model_uri=DEFAULT_.polyphen_prediction, domain=None, range=Optional[Union[str, "PolyphenPredictionLevels"]])

slots.sift_score = Slot(uri=DEFAULT_.sift_score, name="sift_score", curie=DEFAULT_.curie('sift_score'),
                   model_uri=DEFAULT_.sift_score, domain=VariantGeneConsequence, range=Optional[float])

slots.sift_prediction = Slot(uri=DEFAULT_.sift_prediction, name="sift_prediction", curie=DEFAULT_.curie('sift_prediction'),
                   model_uri=DEFAULT_.sift_prediction, domain=None, range=Optional[Union[str, "SiftPredictionLevels"]])

slots.amino_acid_reference = Slot(uri=DEFAULT_.amino_acid_reference, name="amino_acid_reference", curie=DEFAULT_.curie('amino_acid_reference'),
                   model_uri=DEFAULT_.amino_acid_reference, domain=VariantTranscriptConsequence, range=Optional[str])

slots.amino_acid_variant = Slot(uri=DEFAULT_.amino_acid_variant, name="amino_acid_variant", curie=DEFAULT_.curie('amino_acid_variant'),
                   model_uri=DEFAULT_.amino_acid_variant, domain=VariantTranscriptConsequence, range=Optional[str])

slots.codon_reference = Slot(uri=DEFAULT_.codon_reference, name="codon_reference", curie=DEFAULT_.curie('codon_reference'),
                   model_uri=DEFAULT_.codon_reference, domain=VariantTranscriptConsequence, range=Optional[str])

slots.codon_variant = Slot(uri=DEFAULT_.codon_variant, name="codon_variant", curie=DEFAULT_.curie('codon_variant'),
                   model_uri=DEFAULT_.codon_variant, domain=VariantTranscriptConsequence, range=Optional[str])

slots.cdna_start = Slot(uri=DEFAULT_.cdna_start, name="cdna_start", curie=DEFAULT_.curie('cdna_start'),
                   model_uri=DEFAULT_.cdna_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.cdna_end = Slot(uri=DEFAULT_.cdna_end, name="cdna_end", curie=DEFAULT_.curie('cdna_end'),
                   model_uri=DEFAULT_.cdna_end, domain=VariantTranscriptConsequence, range=Optional[int])

slots.cds_start = Slot(uri=DEFAULT_.cds_start, name="cds_start", curie=DEFAULT_.curie('cds_start'),
                   model_uri=DEFAULT_.cds_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.cds_end = Slot(uri=DEFAULT_.cds_end, name="cds_end", curie=DEFAULT_.curie('cds_end'),
                   model_uri=DEFAULT_.cds_end, domain=VariantTranscriptConsequence, range=Optional[int])

slots.protein_start = Slot(uri=DEFAULT_.protein_start, name="protein_start", curie=DEFAULT_.curie('protein_start'),
                   model_uri=DEFAULT_.protein_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.protein_end = Slot(uri=DEFAULT_.protein_end, name="protein_end", curie=DEFAULT_.curie('protein_end'),
                   model_uri=DEFAULT_.protein_end, domain=VariantTranscriptConsequence, range=Optional[int])

slots.hgvs_protein_nomenclature = Slot(uri=DEFAULT_.hgvs_protein_nomenclature, name="hgvs_protein_nomenclature", curie=DEFAULT_.curie('hgvs_protein_nomenclature'),
                   model_uri=DEFAULT_.hgvs_protein_nomenclature, domain=VariantTranscriptConsequence, range=Optional[str])

slots.hgvs_coding_nomenclature = Slot(uri=DEFAULT_.hgvs_coding_nomenclature, name="hgvs_coding_nomenclature", curie=DEFAULT_.curie('hgvs_coding_nomenclature'),
                   model_uri=DEFAULT_.hgvs_coding_nomenclature, domain=VariantTranscriptConsequence, range=Optional[str])

slots.synonym = Slot(uri=ALLIANCE.synonym, name="synonym", curie=ALLIANCE.curie('synonym'),
                   model_uri=DEFAULT_.synonym, domain=None, range=Optional[str])

slots.start = Slot(uri=ALLIANCE.start, name="start", curie=ALLIANCE.curie('start'),
                   model_uri=DEFAULT_.start, domain=None, range=Optional[str])

slots.end = Slot(uri=ALLIANCE.end, name="end", curie=ALLIANCE.curie('end'),
                   model_uri=DEFAULT_.end, domain=None, range=Optional[str])

slots.has_assembly = Slot(uri=ALLIANCE.has_assembly, name="has_assembly", curie=ALLIANCE.curie('has_assembly'),
                   model_uri=DEFAULT_.has_assembly, domain=GenomicEntity, range=Union[str, ChromosomeCurie])

slots.prefix = Slot(uri=ALLIANCE.prefix, name="prefix", curie=ALLIANCE.curie('prefix'),
                   model_uri=DEFAULT_.prefix, domain=None, range=str)

slots.page_areas = Slot(uri=ALLIANCE.page_areas, name="page_areas", curie=ALLIANCE.curie('page_areas'),
                   model_uri=DEFAULT_.page_areas, domain=None, range=Union[str, List[str]])

slots.display_name = Slot(uri=ALLIANCE.display_name, name="display_name", curie=ALLIANCE.curie('display_name'),
                   model_uri=DEFAULT_.display_name, domain=None, range=str)

slots.curator_comment = Slot(uri=ALLIANCE.curator_comment, name="curator_comment", curie=ALLIANCE.curie('curator_comment'),
                   model_uri=DEFAULT_.curator_comment, domain=None, range=Optional[str])

slots.url_prefix = Slot(uri=ALLIANCE.url_prefix, name="url_prefix", curie=ALLIANCE.curie('url_prefix'),
                   model_uri=DEFAULT_.url_prefix, domain=None, range=Optional[str])

slots.url_suffix = Slot(uri=ALLIANCE.url_suffix, name="url_suffix", curie=ALLIANCE.curie('url_suffix'),
                   model_uri=DEFAULT_.url_suffix, domain=None, range=Optional[str])

slots.prefix_order = Slot(uri=ALLIANCE.prefix_order, name="prefix_order", curie=ALLIANCE.curie('prefix_order'),
                   model_uri=DEFAULT_.prefix_order, domain=None, range=Optional[str])

slots.prefix_page = Slot(uri=ALLIANCE.prefix_page, name="prefix_page", curie=ALLIANCE.curie('prefix_page'),
                   model_uri=DEFAULT_.prefix_page, domain=None, range=Optional[str])

slots.private_comment = Slot(uri=ALLIANCE.private_comment, name="private_comment", curie=ALLIANCE.curie('private_comment'),
                   model_uri=DEFAULT_.private_comment, domain=None, range=Optional[str])

slots.uncertain = Slot(uri=ALLIANCE.uncertain, name="uncertain", curie=ALLIANCE.curie('uncertain'),
                   model_uri=DEFAULT_.uncertain, domain=None, range=Optional[Union[bool, Bool]])

slots.free_text = Slot(uri=ALLIANCE.free_text, name="free_text", curie=ALLIANCE.curie('free_text'),
                   model_uri=DEFAULT_.free_text, domain=None, range=Optional[str])

slots.note_type = Slot(uri=ALLIANCE.note_type, name="note_type", curie=ALLIANCE.curie('note_type'),
                   model_uri=DEFAULT_.note_type, domain=None, range=Optional[Union[str, VocabularyTermName]])

slots.internal = Slot(uri=ALLIANCE.internal, name="internal", curie=ALLIANCE.curie('internal'),
                   model_uri=DEFAULT_.internal, domain=None, range=Union[bool, Bool])

slots.related_notes = Slot(uri=ALLIANCE.related_notes, name="related_notes", curie=ALLIANCE.curie('related_notes'),
                   model_uri=DEFAULT_.related_notes, domain=None, range=Optional[Union[Union[dict, Note], List[Union[dict, Note]]]])

slots.related_note = Slot(uri=ALLIANCE.related_note, name="related_note", curie=ALLIANCE.curie('related_note'),
                   model_uri=DEFAULT_.related_note, domain=None, range=Optional[Union[dict, Note]])

slots.statement_subject = Slot(uri=ALLIANCE.statement_subject, name="statement_subject", curie=ALLIANCE.curie('statement_subject'),
                   model_uri=DEFAULT_.statement_subject, domain=EntityStatement, range=Optional[str])

slots.statement_type = Slot(uri=ALLIANCE.statement_type, name="statement_type", curie=ALLIANCE.curie('statement_type'),
                   model_uri=DEFAULT_.statement_type, domain=EntityStatement, range=Optional[str])

slots.statement_text = Slot(uri=ALLIANCE.statement_text, name="statement_text", curie=ALLIANCE.curie('statement_text'),
                   model_uri=DEFAULT_.statement_text, domain=EntityStatement, range=Optional[str])

slots.generated_by = Slot(uri=ALLIANCE.generated_by, name="generated_by", curie=ALLIANCE.curie('generated_by'),
                   model_uri=DEFAULT_.generated_by, domain=None, range=Optional[Union[Union[dict, Agent], List[Union[dict, Agent]]]])

slots.manufactured_by = Slot(uri=ALLIANCE.manufactured_by, name="manufactured_by", curie=ALLIANCE.curie('manufactured_by'),
                   model_uri=DEFAULT_.manufactured_by, domain=None, range=Optional[Union[Union[dict, Agent], List[Union[dict, Agent]]]])

slots.current = Slot(uri=ALLIANCE.current, name="current", curie=ALLIANCE.curie('current'),
                   model_uri=DEFAULT_.current, domain=None, range=Optional[Union[bool, Bool]])

slots.curie = Slot(uri=ALLIANCE.curie, name="curie", curie=ALLIANCE.curie('curie'),
                   model_uri=DEFAULT_.curie, domain=None, range=URIRef)

slots.unique_id = Slot(uri=ALLIANCE.unique_id, name="unique_id", curie=ALLIANCE.curie('unique_id'),
                   model_uri=DEFAULT_.unique_id, domain=None, range=Optional[str])

slots.dbkey = Slot(uri=ALLIANCE.dbkey, name="dbkey", curie=ALLIANCE.curie('dbkey'),
                   model_uri=DEFAULT_.dbkey, domain=None, range=Optional[str])

slots.taxon = Slot(uri=ALLIANCE.taxon, name="taxon", curie=ALLIANCE.curie('taxon'),
                   model_uri=DEFAULT_.taxon, domain=None, range=Optional[Union[str, NCBITaxonTermCurie]])

slots.secondary_identifiers = Slot(uri=ALLIANCE.secondary_identifiers, name="secondary_identifiers", curie=ALLIANCE.curie('secondary_identifiers'),
                   model_uri=DEFAULT_.secondary_identifiers, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.gene_synopsis = Slot(uri=ALLIANCE.gene_synopsis, name="gene_synopsis", curie=ALLIANCE.curie('gene_synopsis'),
                   model_uri=DEFAULT_.gene_synopsis, domain=None, range=Optional[str])

slots.gene_synopsis_URL = Slot(uri=ALLIANCE.gene_synopsis_URL, name="gene_synopsis_URL", curie=ALLIANCE.curie('gene_synopsis_URL'),
                   model_uri=DEFAULT_.gene_synopsis_URL, domain=None, range=Optional[str])

slots.automated_gene_description = Slot(uri=ALLIANCE.automated_gene_description, name="automated_gene_description", curie=ALLIANCE.curie('automated_gene_description'),
                   model_uri=DEFAULT_.automated_gene_description, domain=None, range=Optional[str])

slots.genomic_locations = Slot(uri=ALLIANCE.genomic_locations, name="genomic_locations", curie=ALLIANCE.curie('genomic_locations'),
                   model_uri=DEFAULT_.genomic_locations, domain=GenomicEntity, range=Optional[Union[Union[dict, "GeneGenomicLocation"], List[Union[dict, "GeneGenomicLocation"]]]])

slots.table_key = Slot(uri=ALLIANCE.table_key, name="table_key", curie=ALLIANCE.curie('table_key'),
                   model_uri=DEFAULT_.table_key, domain=None, range=Optional[int])

slots.creation_date = Slot(uri=ALLIANCE.creation_date, name="creation_date", curie=ALLIANCE.curie('creation_date'),
                   model_uri=DEFAULT_.creation_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.date_last_modified = Slot(uri=ALLIANCE.date_last_modified, name="date_last_modified", curie=ALLIANCE.curie('date_last_modified'),
                   model_uri=DEFAULT_.date_last_modified, domain=None, range=Optional[Union[str, XSDDate]])

slots.created_by = Slot(uri=ALLIANCE.created_by, name="created_by", curie=ALLIANCE.curie('created_by'),
                   model_uri=DEFAULT_.created_by, domain=AuditedObject, range=Optional[Union[str, PersonUniqueId]])

slots.modified_by = Slot(uri=ALLIANCE.modified_by, name="modified_by", curie=ALLIANCE.curie('modified_by'),
                   model_uri=DEFAULT_.modified_by, domain=AuditedObject, range=Optional[Union[str, PersonUniqueId]])

slots.release = Slot(uri=ALLIANCE.release, name="release", curie=ALLIANCE.curie('release'),
                   model_uri=DEFAULT_.release, domain=None, range=Optional[str])

slots.data_provider = Slot(uri=ALLIANCE.data_provider, name="data_provider", curie=ALLIANCE.curie('data_provider'),
                   model_uri=DEFAULT_.data_provider, domain=None, range=Optional[str])

slots.secondary_data_provider = Slot(uri=ALLIANCE.secondary_data_provider, name="secondary_data_provider", curie=ALLIANCE.curie('secondary_data_provider'),
                   model_uri=DEFAULT_.secondary_data_provider, domain=None, range=Optional[str])

slots.association_slot = Slot(uri=ALLIANCE.association_slot, name="association_slot", curie=ALLIANCE.curie('association_slot'),
                   model_uri=DEFAULT_.association_slot, domain=None, range=Optional[str])

slots.description = Slot(uri=ALLIANCE.description, name="description", curie=ALLIANCE.curie('description'),
                   model_uri=DEFAULT_.description, domain=None, range=Optional[str])

slots.name = Slot(uri=ALLIANCE.name, name="name", curie=ALLIANCE.curie('name'),
                   model_uri=DEFAULT_.name, domain=None, range=Optional[str])

slots.cross_references = Slot(uri=ALLIANCE.cross_references, name="cross_references", curie=ALLIANCE.curie('cross_references'),
                   model_uri=DEFAULT_.cross_references, domain=None, range=Optional[Union[Dict[Union[str, CrossReferenceCurie], Union[dict, CrossReference]], List[Union[dict, CrossReference]]]])

slots.symbol = Slot(uri=ALLIANCE.symbol, name="symbol", curie=ALLIANCE.curie('symbol'),
                   model_uri=DEFAULT_.symbol, domain=None, range=Optional[str])

slots.synonyms = Slot(uri=ALLIANCE.synonyms, name="synonyms", curie=ALLIANCE.curie('synonyms'),
                   model_uri=DEFAULT_.synonyms, domain=None, range=Optional[Union[Union[dict, Synonym], List[Union[dict, Synonym]]]])

slots.negated = Slot(uri=ALLIANCE.negated, name="negated", curie=ALLIANCE.curie('negated'),
                   model_uri=DEFAULT_.negated, domain=None, range=Optional[Union[bool, Bool]])

slots.qualifiers = Slot(uri=ALLIANCE.qualifiers, name="qualifiers", curie=ALLIANCE.curie('qualifiers'),
                   model_uri=DEFAULT_.qualifiers, domain=None, range=Optional[str])

slots.type = Slot(uri=ALLIANCE.type, name="type", curie=ALLIANCE.curie('type'),
                   model_uri=DEFAULT_.type, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.gene_type = Slot(uri=ALLIANCE.gene_type, name="gene_type", curie=ALLIANCE.curie('gene_type'),
                   model_uri=DEFAULT_.gene_type, domain=Gene, range=Optional[Union[str, SOTermCurie]])

slots.references = Slot(uri=ALLIANCE.references, name="references", curie=ALLIANCE.curie('references'),
                   model_uri=DEFAULT_.references, domain=None, range=Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]])

slots.single_reference = Slot(uri=ALLIANCE.single_reference, name="single_reference", curie=ALLIANCE.curie('single_reference'),
                   model_uri=DEFAULT_.single_reference, domain=None, range=Optional[Union[str, ReferenceCurie]])

slots.original_reference = Slot(uri=ALLIANCE.original_reference, name="original_reference", curie=ALLIANCE.curie('original_reference'),
                   model_uri=DEFAULT_.original_reference, domain=None, range=Optional[Union[str, ReferenceCurie]])

slots.is_obsolete = Slot(uri=ALLIANCE.is_obsolete, name="is_obsolete", curie=ALLIANCE.curie('is_obsolete'),
                   model_uri=DEFAULT_.is_obsolete, domain=None, range=Optional[Union[bool, Bool]])

slots.abbreviation = Slot(uri=ALLIANCE.abbreviation, name="abbreviation", curie=ALLIANCE.curie('abbreviation'),
                   model_uri=DEFAULT_.abbreviation, domain=None, range=Optional[str])

slots.mod_entity_id = Slot(uri=ALLIANCE.mod_entity_id, name="mod_entity_id", curie=ALLIANCE.curie('mod_entity_id'),
                   model_uri=DEFAULT_.mod_entity_id, domain=None, range=Optional[str])

slots.first_name = Slot(uri=ALLIANCE.first_name, name="first_name", curie=ALLIANCE.curie('first_name'),
                   model_uri=DEFAULT_.first_name, domain=None, range=Optional[str])

slots.middle_name = Slot(uri=ALLIANCE.middle_name, name="middle_name", curie=ALLIANCE.curie('middle_name'),
                   model_uri=DEFAULT_.middle_name, domain=None, range=Optional[str])

slots.last_name = Slot(uri=ALLIANCE.last_name, name="last_name", curie=ALLIANCE.curie('last_name'),
                   model_uri=DEFAULT_.last_name, domain=None, range=Optional[str])

slots.evidence_codes = Slot(uri=ALLIANCE.evidence_codes, name="evidence_codes", curie=ALLIANCE.curie('evidence_codes'),
                   model_uri=DEFAULT_.evidence_codes, domain=None, range=Optional[Union[Union[str, ECOTermCurie], List[Union[str, ECOTermCurie]]]])

slots.evidence_code = Slot(uri=ALLIANCE.evidence_code, name="evidence_code", curie=ALLIANCE.curie('evidence_code'),
                   model_uri=DEFAULT_.evidence_code, domain=None, range=Optional[Union[str, ECOTermCurie]])

slots.subject = Slot(uri=ALLIANCE.subject, name="subject", curie=ALLIANCE.curie('subject'),
                   model_uri=DEFAULT_.subject, domain=None, range=str)

slots.object = Slot(uri=ALLIANCE.object, name="object", curie=ALLIANCE.curie('object'),
                   model_uri=DEFAULT_.object, domain=None, range=str)

slots.predicate = Slot(uri=ALLIANCE.predicate, name="predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=DEFAULT_.predicate, domain=None, range=str)

slots.related_to = Slot(uri=ALLIANCE.related_to, name="related_to", curie=ALLIANCE.curie('related_to'),
                   model_uri=DEFAULT_.related_to, domain=None, range=Optional[Union[str, List[str]]])

slots.variant_status = Slot(uri="str(uriorcurie)", name="variant_status", curie=None,
                   model_uri=DEFAULT_.variant_status, domain=None, range=Optional[Union[str, "VariantStatusEnum"]])

slots.variant_type = Slot(uri="str(uriorcurie)", name="variant_type", curie=None,
                   model_uri=DEFAULT_.variant_type, domain=Variant, range=Union[str, SOTermCurie])

slots.source_general_consequence = Slot(uri="str(uriorcurie)", name="source_general_consequence", curie=None,
                   model_uri=DEFAULT_.source_general_consequence, domain=Variant, range=Optional[Union[str, SOTermCurie]])

slots.consequence = Slot(uri="str(uriorcurie)", name="consequence", curie=None,
                   model_uri=DEFAULT_.consequence, domain=VariantLocation, range=Optional[Union[str, SOTermCurie]])

slots.curated_consequence = Slot(uri="str(uriorcurie)", name="curated_consequence", curie=None,
                   model_uri=DEFAULT_.curated_consequence, domain=VariantLocation, range=Optional[Union[str, SOTermCurie]])

slots.variant_locations = Slot(uri="str(uriorcurie)", name="variant_locations", curie=None,
                   model_uri=DEFAULT_.variant_locations, domain=Variant, range=Union[Union[dict, "VariantLocation"], List[Union[dict, "VariantLocation"]]])

slots.variant_genome_locations = Slot(uri="str(uriorcurie)", name="variant_genome_locations", curie=None,
                   model_uri=DEFAULT_.variant_genome_locations, domain=Variant, range=Union[Union[dict, "VariantGenomeLocation"], List[Union[dict, "VariantGenomeLocation"]]])

slots.variant_polypeptide_locations = Slot(uri="str(uriorcurie)", name="variant_polypeptide_locations", curie=None,
                   model_uri=DEFAULT_.variant_polypeptide_locations, domain=Variant, range=Optional[Union[Union[dict, "VariantPolypeptideLocation"], List[Union[dict, "VariantPolypeptideLocation"]]]])

slots.variant_transcript_locations = Slot(uri="str(uriorcurie)", name="variant_transcript_locations", curie=None,
                   model_uri=DEFAULT_.variant_transcript_locations, domain=Variant, range=Optional[Union[Union[dict, "VariantTranscriptLocation"], List[Union[dict, "VariantTranscriptLocation"]]]])

slots.source_variant_locations = Slot(uri="str(uriorcurie)", name="source_variant_locations", curie=None,
                   model_uri=DEFAULT_.source_variant_locations, domain=Variant, range=Optional[Union[Union[dict, "SourceVariantLocation"], List[Union[dict, "SourceVariantLocation"]]]])

slots.hgvs = Slot(uri="str(uriorcurie)", name="hgvs", curie=None,
                   model_uri=DEFAULT_.hgvs, domain=VariantLocation, range=str)

slots.assembly = Slot(uri="str(uriorcurie)", name="assembly", curie=None,
                   model_uri=DEFAULT_.assembly, domain=VariantLocation, range=Optional[Union[str, AssemblyCurie]])

slots.chromosome = Slot(uri="str(uriorcurie)", name="chromosome", curie=None,
                   model_uri=DEFAULT_.chromosome, domain=VariantLocation, range=Optional[Union[str, ChromosomeCurie]])

slots.start_position = Slot(uri="str(uriorcurie)", name="start_position", curie=None,
                   model_uri=DEFAULT_.start_position, domain=VariantLocation, range=Optional[int])

slots.end_position = Slot(uri="str(uriorcurie)", name="end_position", curie=None,
                   model_uri=DEFAULT_.end_position, domain=VariantLocation, range=Optional[int])

slots.reference_sequence = Slot(uri="str(uriorcurie)", name="reference_sequence", curie=None,
                   model_uri=DEFAULT_.reference_sequence, domain=VariantLocation, range=Optional[Union[str, BiologicalSequence]])

slots.variant_sequence = Slot(uri="str(uriorcurie)", name="variant_sequence", curie=None,
                   model_uri=DEFAULT_.variant_sequence, domain=VariantLocation, range=Optional[Union[str, BiologicalSequence]])

slots.transcript = Slot(uri="str(uriorcurie)", name="transcript", curie=None,
                   model_uri=DEFAULT_.transcript, domain=VariantTranscriptLocation, range=Optional[Union[str, TranscriptCurie]])

slots.polypeptide = Slot(uri="str(uriorcurie)", name="polypeptide", curie=None,
                   model_uri=DEFAULT_.polypeptide, domain=VariantTranscriptLocation, range=Union[str, TranscriptCurie])

slots.associated_transcripts = Slot(uri="str(uriorcurie)", name="associated_transcripts", curie=None,
                   model_uri=DEFAULT_.associated_transcripts, domain=VariantPolypeptideLocation, range=Optional[Union[Union[str, TranscriptCurie], List[Union[str, TranscriptCurie]]]])

slots.reference_id = Slot(uri="str(uriorcurie)", name="reference_id", curie=None,
                   model_uri=DEFAULT_.reference_id, domain=None, range=int)

slots.mesh_detail_id = Slot(uri="str(uriorcurie)", name="mesh_detail_id", curie=None,
                   model_uri=DEFAULT_.mesh_detail_id, domain=MeshDetail, range=int)

slots.resource_id = Slot(uri="str(uriorcurie)", name="resource_id", curie=None,
                   model_uri=DEFAULT_.resource_id, domain=Reference, range=Optional[int])

slots.heading_term = Slot(uri="str(uriorcurie)", name="heading_term", curie=None,
                   model_uri=DEFAULT_.heading_term, domain=MeshDetail, range=str)

slots.qualifier_term = Slot(uri="str(uriorcurie)", name="qualifier_term", curie=None,
                   model_uri=DEFAULT_.qualifier_term, domain=MeshDetail, range=Optional[str])

slots.pubmed_type = Slot(uri="str(uriorcurie)", name="pubmed_type", curie=None,
                   model_uri=DEFAULT_.pubmed_type, domain=Reference, range=Optional[Union[Union[str, "PubmedTypeEnum"], List[Union[str, "PubmedTypeEnum"]]]])

slots.date_published = Slot(uri="str(uriorcurie)", name="date_published", curie=None,
                   model_uri=DEFAULT_.date_published, domain=None, range=Optional[str])

slots.date_created = Slot(uri="str(uriorcurie)", name="date_created", curie=None,
                   model_uri=DEFAULT_.date_created, domain=None, range=Optional[Union[str, XSDDate]])

slots.date_updated = Slot(uri="str(uriorcurie)", name="date_updated", curie=None,
                   model_uri=DEFAULT_.date_updated, domain=None, range=Optional[Union[str, XSDDate]])

slots.date_arrived_in_pubmed = Slot(uri="str(uriorcurie)", name="date_arrived_in_pubmed", curie=None,
                   model_uri=DEFAULT_.date_arrived_in_pubmed, domain=Reference, range=Optional[Union[str, List[str]]])

slots.date_last_modified_in_pubmed = Slot(uri="str(uriorcurie)", name="date_last_modified_in_pubmed", curie=None,
                   model_uri=DEFAULT_.date_last_modified_in_pubmed, domain=Reference, range=Optional[str])

slots.issue_date = Slot(uri="str(uriorcurie)", name="issue_date", curie=None,
                   model_uri=DEFAULT_.issue_date, domain=None, range=Optional[str])

slots.open_access = Slot(uri="str(uriorcurie)", name="open_access", curie=None,
                   model_uri=DEFAULT_.open_access, domain=Reference, range=Optional[Union[bool, Bool]])

slots.pages = Slot(uri="str(uriorcurie)", name="pages", curie=None,
                   model_uri=DEFAULT_.pages, domain=None, range=Optional[str])

slots.plain_language_abstract = Slot(uri="str(uriorcurie)", name="plain_language_abstract", curie=None,
                   model_uri=DEFAULT_.plain_language_abstract, domain=Reference, range=Optional[str])

slots.pubmed_abstract_languages = Slot(uri="str(uriorcurie)", name="pubmed_abstract_languages", curie=None,
                   model_uri=DEFAULT_.pubmed_abstract_languages, domain=Reference, range=Optional[Union[str, List[str]]])

slots.pubmed_publication_status = Slot(uri="str(uriorcurie)", name="pubmed_publication_status", curie=None,
                   model_uri=DEFAULT_.pubmed_publication_status, domain=Reference, range=Optional[Union[str, "PubmedPublicationStatusEnum"]])

slots.abstract = Slot(uri="str(uriorcurie)", name="abstract", curie=None,
                   model_uri=DEFAULT_.abstract, domain=Reference, range=Optional[str])

slots.citation = Slot(uri="str(uriorcurie)", name="citation", curie=None,
                   model_uri=DEFAULT_.citation, domain=Reference, range=Optional[str])

slots.issue_name = Slot(uri="str(uriorcurie)", name="issue_name", curie=None,
                   model_uri=DEFAULT_.issue_name, domain=Reference, range=Optional[str])

slots.category = Slot(uri="str(uriorcurie)", name="category", curie=None,
                   model_uri=DEFAULT_.category, domain=Reference, range=Optional[Union[str, "ReferenceCategoryEnum"]])

slots.keywords = Slot(uri="str(uriorcurie)", name="keywords", curie=None,
                   model_uri=DEFAULT_.keywords, domain=None, range=Optional[Union[str, List[str]]])

slots.language = Slot(uri="str(uriorcurie)", name="language", curie=None,
                   model_uri=DEFAULT_.language, domain=Reference, range=Optional[str])

slots.merged_into_id = Slot(uri="str(uriorcurie)", name="merged_into_id", curie=None,
                   model_uri=DEFAULT_.merged_into_id, domain=Reference, range=Optional[Union[str, URIorCURIE]])

slots.summary = Slot(uri="str(uriorcurie)", name="summary", curie=None,
                   model_uri=DEFAULT_.summary, domain=Reference, range=Optional[str])

slots.copyright_date = Slot(uri="str(uriorcurie)", name="copyright_date", curie=None,
                   model_uri=DEFAULT_.copyright_date, domain=Reference, range=Optional[Union[str, XSDDate]])

slots.authors = Slot(uri="str(uriorcurie)", name="authors", curie=None,
                   model_uri=DEFAULT_.authors, domain=Reference, range=Optional[Union[Union[dict, AuthorReference], List[Union[dict, AuthorReference]]]])

slots.corresponding_author = Slot(uri="str(uriorcurie)", name="corresponding_author", curie=None,
                   model_uri=DEFAULT_.corresponding_author, domain=Reference, range=Optional[Union[str, ReferenceCurie]])

slots.initials = Slot(uri="str(uriorcurie)", name="initials", curie=None,
                   model_uri=DEFAULT_.initials, domain=Reference, range=Optional[Union[str, ReferenceCurie]])

slots.title = Slot(uri="str(uriorcurie)", name="title", curie=None,
                   model_uri=DEFAULT_.title, domain=Reference, range=Optional[str])

slots.volume = Slot(uri="str(uriorcurie)", name="volume", curie=None,
                   model_uri=DEFAULT_.volume, domain=Reference, range=Optional[str])

slots.publisher = Slot(uri="str(uriorcurie)", name="publisher", curie=None,
                   model_uri=DEFAULT_.publisher, domain=Reference, range=Optional[str])

slots.address = Slot(uri="str(uriorcurie)", name="address", curie=None,
                   model_uri=DEFAULT_.address, domain=None, range=Optional[str])

slots.iso_abbreviation = Slot(uri="str(uriorcurie)", name="iso_abbreviation", curie=None,
                   model_uri=DEFAULT_.iso_abbreviation, domain=Resource, range=Optional[str])

slots.medline_abbreviation = Slot(uri="str(uriorcurie)", name="medline_abbreviation", curie=None,
                   model_uri=DEFAULT_.medline_abbreviation, domain=Resource, range=Optional[str])

slots.print_issn = Slot(uri="str(uriorcurie)", name="print_issn", curie=None,
                   model_uri=DEFAULT_.print_issn, domain=Resource, range=Optional[str])

slots.online_issn = Slot(uri="str(uriorcurie)", name="online_issn", curie=None,
                   model_uri=DEFAULT_.online_issn, domain=Resource, range=Optional[str])

slots.editors = Slot(uri="str(uriorcurie)", name="editors", curie=None,
                   model_uri=DEFAULT_.editors, domain=Resource, range=Optional[Union[Union[dict, AuthorReference], List[Union[dict, AuthorReference]]]])

slots.orcid = Slot(uri=ALLIANCE.orcid, name="orcid", curie=ALLIANCE.curie('orcid'),
                   model_uri=DEFAULT_.orcid, domain=Person, range=Optional[Union[str, URIorCURIE]])

slots.emails = Slot(uri=ALLIANCE.emails, name="emails", curie=ALLIANCE.curie('emails'),
                   model_uri=DEFAULT_.emails, domain=None, range=Optional[Union[str, List[str]]])

slots.old_emails = Slot(uri=ALLIANCE.old_emails, name="old_emails", curie=ALLIANCE.curie('old_emails'),
                   model_uri=DEFAULT_.old_emails, domain=None, range=Optional[Union[str, List[str]]])

slots.okta_id = Slot(uri=ALLIANCE.okta_id, name="okta_id", curie=ALLIANCE.curie('okta_id'),
                   model_uri=DEFAULT_.okta_id, domain=LoggedInPerson, range=Optional[str])

slots.okta_email = Slot(uri=ALLIANCE.okta_email, name="okta_email", curie=ALLIANCE.curie('okta_email'),
                   model_uri=DEFAULT_.okta_email, domain=LoggedInPerson, range=Optional[str])

slots.caption = Slot(uri="str(uriorcurie)", name="caption", curie=None,
                   model_uri=DEFAULT_.caption, domain=Figure, range=Optional[str])

slots.cropped_from = Slot(uri="str(uriorcurie)", name="cropped_from", curie=None,
                   model_uri=DEFAULT_.cropped_from, domain=Image, range=Optional[Union[str, ImageCurie]])

slots.associated_with_figure = Slot(uri="str(uriorcurie)", name="associated_with_figure", curie=None,
                   model_uri=DEFAULT_.associated_with_figure, domain=None, range=Optional[Union[str, FigureCurie]])

slots.from_image = Slot(uri="str(uriorcurie)", name="from_image", curie=None,
                   model_uri=DEFAULT_.from_image, domain=ImagePane, range=Optional[Union[str, ImageCurie]])

slots.height = Slot(uri="str(uriorcurie)", name="height", curie=None,
                   model_uri=DEFAULT_.height, domain=Image, range=int)

slots.image_file = Slot(uri="str(uriorcurie)", name="image_file", curie=None,
                   model_uri=DEFAULT_.image_file, domain=Image, range=Union[dict, File])

slots.image_medium_file = Slot(uri="str(uriorcurie)", name="image_medium_file", curie=None,
                   model_uri=DEFAULT_.image_medium_file, domain=Image, range=Union[dict, File])

slots.image_thumbnail_file = Slot(uri="str(uriorcurie)", name="image_thumbnail_file", curie=None,
                   model_uri=DEFAULT_.image_thumbnail_file, domain=Image, range=Union[dict, File])

slots.image_x_origin = Slot(uri="str(uriorcurie)", name="image_x_origin", curie=None,
                   model_uri=DEFAULT_.image_x_origin, domain=None, range=Optional[int])

slots.image_y_origin = Slot(uri="str(uriorcurie)", name="image_y_origin", curie=None,
                   model_uri=DEFAULT_.image_y_origin, domain=None, range=Optional[int])

slots.images = Slot(uri="str(uriorcurie)", name="images", curie=None,
                   model_uri=DEFAULT_.images, domain=None, range=Optional[Union[str, ImageCurie]])

slots.label = Slot(uri="str(uriorcurie)", name="label", curie=None,
                   model_uri=DEFAULT_.label, domain=None, range=Optional[str])

slots.video_still = Slot(uri="str(uriorcurie)", name="video_still", curie=None,
                   model_uri=DEFAULT_.video_still, domain=Image, range=Optional[Union[bool, Bool]])

slots.width = Slot(uri="str(uriorcurie)", name="width", curie=None,
                   model_uri=DEFAULT_.width, domain=Image, range=int)

slots.definition = Slot(uri="str(uriorcurie)", name="definition", curie=None,
                   model_uri=DEFAULT_.definition, domain=None, range=Optional[str])

slots.display_synonym = Slot(uri="str(uriorcurie)", name="display_synonym", curie=None,
                   model_uri=DEFAULT_.display_synonym, domain=None, range=Optional[str])

slots.namespace = Slot(uri="str(uriorcurie)", name="namespace", curie=None,
                   model_uri=DEFAULT_.namespace, domain=None, range=Optional[str])

slots.subsets = Slot(uri="str(uriorcurie)", name="subsets", curie=None,
                   model_uri=DEFAULT_.subsets, domain=None, range=Optional[Union[str, List[str]]])

slots.definition_urls = Slot(uri="str(uriorcurie)", name="definition_urls", curie=None,
                   model_uri=DEFAULT_.definition_urls, domain=None, range=Optional[Union[str, List[str]]])

slots.inchi = Slot(uri="str(uriorcurie)", name="inchi", curie=None,
                   model_uri=DEFAULT_.inchi, domain=Molecule, range=Optional[str])

slots.inchi_key = Slot(uri="str(uriorcurie)", name="inchi_key", curie=None,
                   model_uri=DEFAULT_.inchi_key, domain=Molecule, range=Optional[str])

slots.iupac = Slot(uri="str(uriorcurie)", name="iupac", curie=None,
                   model_uri=DEFAULT_.iupac, domain=Molecule, range=Optional[str])

slots.formula = Slot(uri="str(uriorcurie)", name="formula", curie=None,
                   model_uri=DEFAULT_.formula, domain=Molecule, range=Optional[str])

slots.smiles = Slot(uri="str(uriorcurie)", name="smiles", curie=None,
                   model_uri=DEFAULT_.smiles, domain=Molecule, range=Optional[str])

slots.text_synonyms = Slot(uri="str(uriorcurie)", name="text_synonyms", curie=None,
                   model_uri=DEFAULT_.text_synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.member_terms = Slot(uri="str(uriorcurie)", name="member_terms", curie=None,
                   model_uri=DEFAULT_.member_terms, domain=None, range=Optional[Union[Union[str, VocabularyTermName], List[Union[str, VocabularyTermName]]]])

slots.vocabulary_description = Slot(uri="str(uriorcurie)", name="vocabulary_description", curie=None,
                   model_uri=DEFAULT_.vocabulary_description, domain=None, range=Optional[str])

slots.construct_components = Slot(uri="str(uriorcurie)", name="construct_components", curie=None,
                   model_uri=DEFAULT_.construct_components, domain=Construct, range=Optional[Union[Union[str, GenomicEntityCurie], List[Union[str, GenomicEntityCurie]]]])

slots.contains_constructs = Slot(uri="str(uriorcurie)", name="contains_constructs", curie=None,
                   model_uri=DEFAULT_.contains_constructs, domain=Allele, range=Optional[Union[Union[str, ConstructCurie], List[Union[str, ConstructCurie]]]])

slots.molecular_mutations = Slot(uri="str(uriorcurie)", name="molecular_mutations", curie=None,
                   model_uri=DEFAULT_.molecular_mutations, domain=Allele, range=Optional[Union[str, List[str]]])

slots.mutation_type = Slot(uri="str(uriorcurie)", name="mutation_type", curie=None,
                   model_uri=DEFAULT_.mutation_type, domain=Allele, range=Optional[Union[str, SOTermCurie]])

slots.mutation_description = Slot(uri="str(uriorcurie)", name="mutation_description", curie=None,
                   model_uri=DEFAULT_.mutation_description, domain=None, range=Optional[str])

slots.functional_impact = Slot(uri="str(uriorcurie)", name="functional_impact", curie=None,
                   model_uri=DEFAULT_.functional_impact, domain=Allele, range=Optional[str])

slots.generation_method = Slot(uri="str(uriorcurie)", name="generation_method", curie=None,
                   model_uri=DEFAULT_.generation_method, domain=Allele, range=Optional[str])

slots.associated_references = Slot(uri="str(uriorcurie)", name="associated_references", curie=None,
                   model_uri=DEFAULT_.associated_references, domain=None, range=Optional[Union[Union[dict, AssociatedReference], List[Union[dict, AssociatedReference]]]])

slots.reference_type = Slot(uri="str(uriorcurie)", name="reference_type", curie=None,
                   model_uri=DEFAULT_.reference_type, domain=AssociatedReference, range=Union[str, VocabularyTermName])

slots.origins = Slot(uri="str(uriorcurie)", name="origins", curie=None,
                   model_uri=DEFAULT_.origins, domain=Allele, range=Optional[Union[Union[str, AffectedGenomicModelCurie], List[Union[str, AffectedGenomicModelCurie]]]])

slots.germline_transmission_status = Slot(uri="str(uriorcurie)", name="germline_transmission_status", curie=None,
                   model_uri=DEFAULT_.germline_transmission_status, domain=Allele, range=Optional[Union[str, VocabularyTermName]])

slots.parent_cell_line = Slot(uri="str(uriorcurie)", name="parent_cell_line", curie=None,
                   model_uri=DEFAULT_.parent_cell_line, domain=Allele, range=Optional[Union[dict, "CellLine"]])

slots.mutant_cell_lines = Slot(uri="str(uriorcurie)", name="mutant_cell_lines", curie=None,
                   model_uri=DEFAULT_.mutant_cell_lines, domain=Allele, range=Optional[Union[Union[dict, "CellLine"], List[Union[dict, "CellLine"]]]])

slots.embryonic_stem_cell_lines = Slot(uri="str(uriorcurie)", name="embryonic_stem_cell_lines", curie=None,
                   model_uri=DEFAULT_.embryonic_stem_cell_lines, domain=Allele, range=Optional[Union[Union[dict, "CellLine"], List[Union[dict, "CellLine"]]]])

slots.database_status = Slot(uri="str(uriorcurie)", name="database_status", curie=None,
                   model_uri=DEFAULT_.database_status, domain=None, range=Optional[Union[str, VocabularyTermName]])

slots.inheritence_mode = Slot(uri="str(uriorcurie)", name="inheritence_mode", curie=None,
                   model_uri=DEFAULT_.inheritence_mode, domain=Allele, range=Optional[Union[str, VocabularyTermName]])

slots.in_collection = Slot(uri="str(uriorcurie)", name="in_collection", curie=None,
                   model_uri=DEFAULT_.in_collection, domain=Allele, range=Optional[Union[str, VocabularyTermName]])

slots.transposon_insertion = Slot(uri="str(uriorcurie)", name="transposon_insertion", curie=None,
                   model_uri=DEFAULT_.transposon_insertion, domain=Allele, range=Optional[str])

slots.aberration = Slot(uri="str(uriorcurie)", name="aberration", curie=None,
                   model_uri=DEFAULT_.aberration, domain=Allele, range=Optional[str])

slots.is_extinct = Slot(uri="str(uriorcurie)", name="is_extinct", curie=None,
                   model_uri=DEFAULT_.is_extinct, domain=Allele, range=Optional[Union[bool, Bool]])

slots.sequencing_status = Slot(uri="str(uriorcurie)", name="sequencing_status", curie=None,
                   model_uri=DEFAULT_.sequencing_status, domain=Variant, range=Optional[Union[str, VocabularyTermName]])

slots.subtype = Slot(uri="str(uriorcurie)", name="subtype", curie=None,
                   model_uri=DEFAULT_.subtype, domain=AffectedGenomicModel, range=Union[str, "SubtypeValues"])

slots.components = Slot(uri="str(uriorcurie)", name="components", curie=None,
                   model_uri=DEFAULT_.components, domain=AffectedGenomicModel, range=Optional[Union[Union[dict, "AffectedGenomicModelComponent"], List[Union[dict, "AffectedGenomicModelComponent"]]]])

slots.has_allele = Slot(uri="str(uriorcurie)", name="has_allele", curie=None,
                   model_uri=DEFAULT_.has_allele, domain=AffectedGenomicModelComponent, range=Optional[Union[str, AlleleCurie]])

slots.zygosity = Slot(uri="str(uriorcurie)", name="zygosity", curie=None,
                   model_uri=DEFAULT_.zygosity, domain=AffectedGenomicModelComponent, range=Optional[Union[str, "ZygosityValues"]])

slots.sequence_targeting_reagents = Slot(uri="str(uriorcurie)", name="sequence_targeting_reagents", curie=None,
                   model_uri=DEFAULT_.sequence_targeting_reagents, domain=AffectedGenomicModel, range=Optional[Union[Union[str, SequenceTargetingReagentCurie], List[Union[str, SequenceTargetingReagentCurie]]]])

slots.parental_populations = Slot(uri="str(uriorcurie)", name="parental_populations", curie=None,
                   model_uri=DEFAULT_.parental_populations, domain=AffectedGenomicModel, range=Optional[Union[str, URIorCURIE]])

slots.cnda_end = Slot(uri=DEFAULT_.cnda_end, name="cnda_end", curie=DEFAULT_.curie('cnda_end'),
                   model_uri=DEFAULT_.cnda_end, domain=None, range=Optional[str])

slots.id = Slot(uri=DEFAULT_.id, name="id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.id, domain=None, range=Optional[str])

slots.embryonic_cell_lines = Slot(uri=DEFAULT_.embryonic_cell_lines, name="embryonic_cell_lines", curie=DEFAULT_.curie('embryonic_cell_lines'),
                   model_uri=DEFAULT_.embryonic_cell_lines, domain=None, range=Optional[str])

slots.VariantGeneConsequence_object = Slot(uri=ALLIANCE.object, name="VariantGeneConsequence_object", curie=ALLIANCE.curie('object'),
                   model_uri=DEFAULT_.VariantGeneConsequence_object, domain=VariantGeneConsequence, range=Union[str, GeneCurie])

slots.VariantGeneConsequence_subject = Slot(uri=ALLIANCE.subject, name="VariantGeneConsequence_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=DEFAULT_.VariantGeneConsequence_subject, domain=VariantGeneConsequence, range=Union[dict, "VariantGenomeLocation"])

slots.VariantTranscriptConsequence_object = Slot(uri=ALLIANCE.object, name="VariantTranscriptConsequence_object", curie=ALLIANCE.curie('object'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_object, domain=VariantTranscriptConsequence, range=Union[str, TranscriptCurie])

slots.VariantTranscriptConsequence_subject = Slot(uri=ALLIANCE.subject, name="VariantTranscriptConsequence_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_subject, domain=VariantTranscriptConsequence, range=Union[dict, "VariantTranscriptLocation"])

slots.VariantTranscriptConsequence_amino_acid_reference = Slot(uri=DEFAULT_.amino_acid_reference, name="VariantTranscriptConsequence_amino_acid_reference", curie=DEFAULT_.curie('amino_acid_reference'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_amino_acid_reference, domain=VariantTranscriptConsequence, range=Optional[str])

slots.VariantTranscriptConsequence_amino_acid_variant = Slot(uri=DEFAULT_.amino_acid_variant, name="VariantTranscriptConsequence_amino_acid_variant", curie=DEFAULT_.curie('amino_acid_variant'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_amino_acid_variant, domain=VariantTranscriptConsequence, range=Optional[str])

slots.VariantTranscriptConsequence_codon_reference = Slot(uri=DEFAULT_.codon_reference, name="VariantTranscriptConsequence_codon_reference", curie=DEFAULT_.curie('codon_reference'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_codon_reference, domain=VariantTranscriptConsequence, range=Optional[str])

slots.VariantTranscriptConsequence_codon_variant = Slot(uri=DEFAULT_.codon_variant, name="VariantTranscriptConsequence_codon_variant", curie=DEFAULT_.curie('codon_variant'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_codon_variant, domain=VariantTranscriptConsequence, range=Optional[str])

slots.VariantTranscriptConsequence_cdna_start = Slot(uri=DEFAULT_.cdna_start, name="VariantTranscriptConsequence_cdna_start", curie=DEFAULT_.curie('cdna_start'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_cdna_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.VariantTranscriptConsequence_cnda_end = Slot(uri=DEFAULT_.cnda_end, name="VariantTranscriptConsequence_cnda_end", curie=DEFAULT_.curie('cnda_end'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_cnda_end, domain=VariantTranscriptConsequence, range=Optional[str])

slots.VariantTranscriptConsequence_cds_start = Slot(uri=DEFAULT_.cds_start, name="VariantTranscriptConsequence_cds_start", curie=DEFAULT_.curie('cds_start'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_cds_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.VariantTranscriptConsequence_cds_end = Slot(uri=DEFAULT_.cds_end, name="VariantTranscriptConsequence_cds_end", curie=DEFAULT_.curie('cds_end'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_cds_end, domain=VariantTranscriptConsequence, range=Optional[int])

slots.VariantTranscriptConsequence_protein_start = Slot(uri=DEFAULT_.protein_start, name="VariantTranscriptConsequence_protein_start", curie=DEFAULT_.curie('protein_start'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_protein_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.VariantTranscriptConsequence_protein_end = Slot(uri=DEFAULT_.protein_end, name="VariantTranscriptConsequence_protein_end", curie=DEFAULT_.curie('protein_end'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_protein_end, domain=VariantTranscriptConsequence, range=Optional[int])

slots.VariantTranscriptConsequence_hgvs_protein_nomenclature = Slot(uri=DEFAULT_.hgvs_protein_nomenclature, name="VariantTranscriptConsequence_hgvs_protein_nomenclature", curie=DEFAULT_.curie('hgvs_protein_nomenclature'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_hgvs_protein_nomenclature, domain=VariantTranscriptConsequence, range=Optional[str])

slots.VariantTranscriptConsequence_hgvs_coding_nomenclature = Slot(uri=DEFAULT_.hgvs_coding_nomenclature, name="VariantTranscriptConsequence_hgvs_coding_nomenclature", curie=DEFAULT_.curie('hgvs_coding_nomenclature'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_hgvs_coding_nomenclature, domain=VariantTranscriptConsequence, range=Optional[str])

slots.BiologicalEntity_taxon = Slot(uri=ALLIANCE.taxon, name="BiologicalEntity_taxon", curie=ALLIANCE.curie('taxon'),
                   model_uri=DEFAULT_.BiologicalEntity_taxon, domain=BiologicalEntity, range=Union[str, NCBITaxonTermCurie])

slots.Gene_symbol = Slot(uri=ALLIANCE.symbol, name="Gene_symbol", curie=ALLIANCE.curie('symbol'),
                   model_uri=DEFAULT_.Gene_symbol, domain=Gene, range=str)

slots.Note_free_text = Slot(uri=ALLIANCE.free_text, name="Note_free_text", curie=ALLIANCE.curie('free_text'),
                   model_uri=DEFAULT_.Note_free_text, domain=Note, range=str)

slots.Note_note_type = Slot(uri=ALLIANCE.note_type, name="Note_note_type", curie=ALLIANCE.curie('note_type'),
                   model_uri=DEFAULT_.Note_note_type, domain=Note, range=Union[str, VocabularyTermName])

slots.EntitySynonym_object = Slot(uri=ALLIANCE.object, name="EntitySynonym_object", curie=ALLIANCE.curie('object'),
                   model_uri=DEFAULT_.EntitySynonym_object, domain=EntitySynonym, range=Union[dict, Synonym])

slots.EntitySynonym_predicate = Slot(uri=ALLIANCE.predicate, name="EntitySynonym_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=DEFAULT_.EntitySynonym_predicate, domain=EntitySynonym, range=Union[str, "EntitySynonymTypeSet"])

slots.EntitySynonym_references = Slot(uri=ALLIANCE.references, name="EntitySynonym_references", curie=ALLIANCE.curie('references'),
                   model_uri=DEFAULT_.EntitySynonym_references, domain=EntitySynonym, range=Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]])

slots.GeneGenomicLocation_subject = Slot(uri=ALLIANCE.subject, name="GeneGenomicLocation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=DEFAULT_.GeneGenomicLocation_subject, domain=GeneGenomicLocation, range=Union[str, VariantCurie])

slots.GeneGenomicLocation_object = Slot(uri=ALLIANCE.object, name="GeneGenomicLocation_object", curie=ALLIANCE.curie('object'),
                   model_uri=DEFAULT_.GeneGenomicLocation_object, domain=GeneGenomicLocation, range=Union[str, ChromosomeCurie])

slots.SourceVariantLocation_single_reference = Slot(uri=ALLIANCE.single_reference, name="SourceVariantLocation_single_reference", curie=ALLIANCE.curie('single_reference'),
                   model_uri=DEFAULT_.SourceVariantLocation_single_reference, domain=SourceVariantLocation, range=Union[str, ReferenceCurie])

slots.VariantLocation_evidence_code = Slot(uri=ALLIANCE.evidence_code, name="VariantLocation_evidence_code", curie=ALLIANCE.curie('evidence_code'),
                   model_uri=DEFAULT_.VariantLocation_evidence_code, domain=VariantLocation, range=Optional[Union[str, ECOTermCurie]])

slots.Reference_reference_id = Slot(uri="str(uriorcurie)", name="Reference_reference_id", curie=None,
                   model_uri=DEFAULT_.Reference_reference_id, domain=Reference, range=int)

slots.Reference_date_last_modified = Slot(uri=ALLIANCE.date_last_modified, name="Reference_date_last_modified", curie=ALLIANCE.curie('date_last_modified'),
                   model_uri=DEFAULT_.Reference_date_last_modified, domain=Reference, range=Optional[Union[str, XSDDate]])

slots.MeshDetail_reference_id = Slot(uri="str(uriorcurie)", name="MeshDetail_reference_id", curie=None,
                   model_uri=DEFAULT_.MeshDetail_reference_id, domain=MeshDetail, range=int)

slots.Resource_id = Slot(uri=DEFAULT_.id, name="Resource_id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.Resource_id, domain=Resource, range=Optional[str])

slots.Resource_title = Slot(uri="str(uriorcurie)", name="Resource_title", curie=None,
                   model_uri=DEFAULT_.Resource_title, domain=Resource, range=Optional[str])

slots.Person_unique_id = Slot(uri=ALLIANCE.unique_id, name="Person_unique_id", curie=ALLIANCE.curie('unique_id'),
                   model_uri=DEFAULT_.Person_unique_id, domain=Person, range=Union[str, PersonUniqueId])

slots.LoggedInPerson_okta_id = Slot(uri=ALLIANCE.okta_id, name="LoggedInPerson_okta_id", curie=ALLIANCE.curie('okta_id'),
                   model_uri=DEFAULT_.LoggedInPerson_okta_id, domain=LoggedInPerson, range=str)

slots.LoggedInPerson_okta_email = Slot(uri=ALLIANCE.okta_email, name="LoggedInPerson_okta_email", curie=ALLIANCE.curie('okta_email'),
                   model_uri=DEFAULT_.LoggedInPerson_okta_email, domain=LoggedInPerson, range=str)

slots.Figure_single_reference = Slot(uri=ALLIANCE.single_reference, name="Figure_single_reference", curie=ALLIANCE.curie('single_reference'),
                   model_uri=DEFAULT_.Figure_single_reference, domain=Figure, range=Union[str, ReferenceCurie])

slots.Image_associated_with_figure = Slot(uri="str(uriorcurie)", name="Image_associated_with_figure", curie=None,
                   model_uri=DEFAULT_.Image_associated_with_figure, domain=Image, range=Union[str, FigureCurie])

slots.Image_image_x_origin = Slot(uri="str(uriorcurie)", name="Image_image_x_origin", curie=None,
                   model_uri=DEFAULT_.Image_image_x_origin, domain=Image, range=Optional[int])

slots.Image_image_y_origin = Slot(uri="str(uriorcurie)", name="Image_image_y_origin", curie=None,
                   model_uri=DEFAULT_.Image_image_y_origin, domain=Image, range=Optional[int])

slots.ImagePane_from_image = Slot(uri="str(uriorcurie)", name="ImagePane_from_image", curie=None,
                   model_uri=DEFAULT_.ImagePane_from_image, domain=ImagePane, range=Union[str, ImageCurie])

slots.ImagePane_image_x_origin = Slot(uri="str(uriorcurie)", name="ImagePane_image_x_origin", curie=None,
                   model_uri=DEFAULT_.ImagePane_image_x_origin, domain=ImagePane, range=Optional[int])

slots.ImagePane_image_y_origin = Slot(uri="str(uriorcurie)", name="ImagePane_image_y_origin", curie=None,
                   model_uri=DEFAULT_.ImagePane_image_y_origin, domain=ImagePane, range=Optional[int])

slots.OntologyTerm_definition = Slot(uri="str(uriorcurie)", name="OntologyTerm_definition", curie=None,
                   model_uri=DEFAULT_.OntologyTerm_definition, domain=OntologyTerm, range=Optional[str])

slots.ECOTerm_abbreviation = Slot(uri=ALLIANCE.abbreviation, name="ECOTerm_abbreviation", curie=ALLIANCE.curie('abbreviation'),
                   model_uri=DEFAULT_.ECOTerm_abbreviation, domain=ECOTerm, range=Optional[str])

slots.VocabularyTerm_name = Slot(uri=ALLIANCE.name, name="VocabularyTerm_name", curie=ALLIANCE.curie('name'),
                   model_uri=DEFAULT_.VocabularyTerm_name, domain=VocabularyTerm, range=Union[str, VocabularyTermName])

slots.Vocabulary_name = Slot(uri=ALLIANCE.name, name="Vocabulary_name", curie=ALLIANCE.curie('name'),
                   model_uri=DEFAULT_.Vocabulary_name, domain=Vocabulary, range=Union[str, VocabularyName])

slots.Allele_synonyms = Slot(uri=ALLIANCE.synonyms, name="Allele_synonyms", curie=ALLIANCE.curie('synonyms'),
                   model_uri=DEFAULT_.Allele_synonyms, domain=Allele, range=Optional[Union[Union[dict, Synonym], List[Union[dict, Synonym]]]])

slots.Allele_germline_transmission_status = Slot(uri="str(uriorcurie)", name="Allele_germline_transmission_status", curie=None,
                   model_uri=DEFAULT_.Allele_germline_transmission_status, domain=Allele, range=Optional[Union[str, VocabularyTermName]])

slots.Allele_parent_cell_line = Slot(uri="str(uriorcurie)", name="Allele_parent_cell_line", curie=None,
                   model_uri=DEFAULT_.Allele_parent_cell_line, domain=Allele, range=Optional[Union[dict, "CellLine"]])

slots.Allele_mutant_cell_lines = Slot(uri="str(uriorcurie)", name="Allele_mutant_cell_lines", curie=None,
                   model_uri=DEFAULT_.Allele_mutant_cell_lines, domain=Allele, range=Optional[Union[Union[dict, "CellLine"], List[Union[dict, "CellLine"]]]])

slots.Allele_embryonic_cell_lines = Slot(uri=DEFAULT_.embryonic_cell_lines, name="Allele_embryonic_cell_lines", curie=DEFAULT_.curie('embryonic_cell_lines'),
                   model_uri=DEFAULT_.Allele_embryonic_cell_lines, domain=Allele, range=Optional[str])

slots.Allele_transposon_insertion = Slot(uri="str(uriorcurie)", name="Allele_transposon_insertion", curie=None,
                   model_uri=DEFAULT_.Allele_transposon_insertion, domain=Allele, range=Optional[str])

slots.Allele_aberration = Slot(uri="str(uriorcurie)", name="Allele_aberration", curie=None,
                   model_uri=DEFAULT_.Allele_aberration, domain=Allele, range=Optional[str])

slots.Allele_name = Slot(uri=ALLIANCE.name, name="Allele_name", curie=ALLIANCE.curie('name'),
                   model_uri=DEFAULT_.Allele_name, domain=Allele, range=str)

slots.AlleleGenomicEntityAssociation_subject = Slot(uri=ALLIANCE.subject, name="AlleleGenomicEntityAssociation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=DEFAULT_.AlleleGenomicEntityAssociation_subject, domain=AlleleGenomicEntityAssociation, range=Union[str, AlleleCurie])

slots.AlleleGenomicEntityAssociation_predicate = Slot(uri=ALLIANCE.predicate, name="AlleleGenomicEntityAssociation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=DEFAULT_.AlleleGenomicEntityAssociation_predicate, domain=AlleleGenomicEntityAssociation, range=Union[str, ROTermCurie])

slots.AlleleGenomicEntityAssociation_object = Slot(uri=ALLIANCE.object, name="AlleleGenomicEntityAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=DEFAULT_.AlleleGenomicEntityAssociation_object, domain=AlleleGenomicEntityAssociation, range=Union[str, GenomicEntityCurie])

slots.AlleleGeneAssociation_object = Slot(uri=ALLIANCE.object, name="AlleleGeneAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=DEFAULT_.AlleleGeneAssociation_object, domain=AlleleGeneAssociation, range=Union[str, GeneCurie])

slots.AlleleTranscriptAssociation_object = Slot(uri=ALLIANCE.object, name="AlleleTranscriptAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=DEFAULT_.AlleleTranscriptAssociation_object, domain=AlleleTranscriptAssociation, range=Union[str, TranscriptCurie])

slots.AlleleProteinAssociation_object = Slot(uri=ALLIANCE.object, name="AlleleProteinAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=DEFAULT_.AlleleProteinAssociation_object, domain=AlleleProteinAssociation, range=Union[str, ProteinCurie])

slots.AlleleVariantAssociation_subject = Slot(uri=ALLIANCE.subject, name="AlleleVariantAssociation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=DEFAULT_.AlleleVariantAssociation_subject, domain=AlleleVariantAssociation, range=Union[str, AlleleCurie])

slots.AlleleVariantAssociation_object = Slot(uri=ALLIANCE.object, name="AlleleVariantAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=DEFAULT_.AlleleVariantAssociation_object, domain=AlleleVariantAssociation, range=Union[str, VariantCurie])

slots.Construct_curie = Slot(uri=ALLIANCE.curie, name="Construct_curie", curie=ALLIANCE.curie('curie'),
                   model_uri=DEFAULT_.Construct_curie, domain=Construct, range=Union[str, ConstructCurie])

slots.Construct_name = Slot(uri=ALLIANCE.name, name="Construct_name", curie=ALLIANCE.curie('name'),
                   model_uri=DEFAULT_.Construct_name, domain=Construct, range=str)

slots.SequenceTargetingReagent_curie = Slot(uri=ALLIANCE.curie, name="SequenceTargetingReagent_curie", curie=ALLIANCE.curie('curie'),
                   model_uri=DEFAULT_.SequenceTargetingReagent_curie, domain=SequenceTargetingReagent, range=Union[str, SequenceTargetingReagentCurie])

slots.SequenceTargetingReagent_name = Slot(uri=ALLIANCE.name, name="SequenceTargetingReagent_name", curie=ALLIANCE.curie('name'),
                   model_uri=DEFAULT_.SequenceTargetingReagent_name, domain=SequenceTargetingReagent, range=str)

slots.SequenceTargetingReagentToGeneAssociation_predicate = Slot(uri=ALLIANCE.predicate, name="SequenceTargetingReagentToGeneAssociation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=DEFAULT_.SequenceTargetingReagentToGeneAssociation_predicate, domain=SequenceTargetingReagentToGeneAssociation, range=Union[str, "SqtrRelationEnum"])

slots.SequenceTargetingReagentToGeneAssociation_subject = Slot(uri=ALLIANCE.subject, name="SequenceTargetingReagentToGeneAssociation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=DEFAULT_.SequenceTargetingReagentToGeneAssociation_subject, domain=SequenceTargetingReagentToGeneAssociation, range=Union[str, SequenceTargetingReagentCurie])

slots.SequenceTargetingReagentToGeneAssociation_object = Slot(uri=ALLIANCE.object, name="SequenceTargetingReagentToGeneAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=DEFAULT_.SequenceTargetingReagentToGeneAssociation_object, domain=SequenceTargetingReagentToGeneAssociation, range=Union[str, GeneCurie])

slots.ConstructComponentAssociation_predicate = Slot(uri=ALLIANCE.predicate, name="ConstructComponentAssociation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=DEFAULT_.ConstructComponentAssociation_predicate, domain=ConstructComponentAssociation, range=Union[str, "ConstructComponentRelationEnum"])

slots.ConstructComponentAssociation_subject = Slot(uri=ALLIANCE.subject, name="ConstructComponentAssociation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=DEFAULT_.ConstructComponentAssociation_subject, domain=ConstructComponentAssociation, range=Union[str, ConstructCurie])

slots.ConstructComponentAssociation_object = Slot(uri=ALLIANCE.object, name="ConstructComponentAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=DEFAULT_.ConstructComponentAssociation_object, domain=ConstructComponentAssociation, range=Union[str, ConstructComponentCurie])
