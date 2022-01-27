# Auto generated from allianceModel.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-01-26T16:28:33
# Schema: Alliance-Schema-Prototype
#
# id: https://github.com/alliance-genome/agr_curation_schema/alliance_schema
# description: Alliance Schema Prototype
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

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOGRID = CurieNamespace('BIOGRID', 'http://identifiers.org/biogrid/')
DIP = CurieNamespace('DIP', 'http://identifiers.org/dip/')
DOI = CurieNamespace('DOI', 'http://identifiers.org/doi/')
EMDB = CurieNamespace('EMDB', 'http://identifiers.org/emdb/')
ENSEMBL = CurieNamespace('ENSEMBL', 'http://identifiers.org/ensembl/')
FB = CurieNamespace('FB', 'http://identifiers.org/fb/')
HGNC = CurieNamespace('HGNC', 'http://identifiers.org/hgnc/')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
IMEX = CurieNamespace('IMEX', 'http://identifiers.org/imex/')
INTACT = CurieNamespace('INTACT', 'http://identifiers.org/intact/')
MGI = CurieNamespace('MGI', 'http://identifiers.org/mgi/')
MINT = CurieNamespace('MINT', 'http://identifiers.org/mint/')
NLMID = CurieNamespace('NLMID', 'https://www.ncbi.nlm.nih.gov/nlmcatalog/?term=')
PDBE = CurieNamespace('PDBE', 'https://www.ebi.ac.uk/pdbe/entry/pdb/')
PMC = CurieNamespace('PMC', 'http://identifiers.org/pmc/')
PMID = CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/')
RCSB_PDB = CurieNamespace('RCSB_PDB', 'https://www.rcsb.org/structure/')
RGD = CurieNamespace('RGD', 'http://identifiers.org/rgd/')
SGD = CurieNamespace('SGD', 'http://identifiers.org/sgd/')
SO = CurieNamespace('SO', 'http://purl.obolibrary.org/obo/SO_')
WB = CurieNamespace('WB', 'http://identifiers.org/wb/')
WIKIDATA_PROPERTY = CurieNamespace('WIKIDATA_PROPERTY', 'https://www.wikidata.org/wiki/Property:')
WWPDB = CurieNamespace('WWPDB', 'https://www.rcsb.org/structure/')
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
DEFAULT_ = ALLIANCE


# Types
class BiologicalSequence(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "biological_sequence"
    type_model_uri = ALLIANCE.BiologicalSequence


# Class references
class BiologicalEntityCurie(URIorCURIE):
    pass


class GenomicEntityCurie(BiologicalEntityCurie):
    pass


class VariantCurie(GenomicEntityCurie):
    pass


class TranscriptCurie(GenomicEntityCurie):
    pass


class GeneCurie(GenomicEntityCurie):
    pass


class ChromosomeCurie(URIorCURIE):
    pass


class AssemblyCurie(URIorCURIE):
    pass


class InformationContentEntityCurie(URIorCURIE):
    pass


class ReferenceCurie(InformationContentEntityCurie):
    pass


class ResourceCurie(InformationContentEntityCurie):
    pass


class CrossReferenceCurie(InformationContentEntityCurie):
    pass


class PersonPersonId(extended_str):
    pass


class AlleleCurie(GenomicEntityCurie):
    pass


class ConstructCurie(GenomicEntityCurie):
    pass


class ConstructComponentCurie(GenomicEntityCurie):
    pass


class AffectedGenomicModelCurie(GenomicEntityCurie):
    pass


class AntibodyCurie(BiologicalEntityCurie):
    pass


class GeneInteractionCurie(URIorCURIE):
    pass


class GeneMolecularInteractionCurie(GeneInteractionCurie):
    pass


class GeneGeneticInteractionCurie(GeneInteractionCurie):
    pass


class OntologyTermCurie(URIorCURIE):
    pass


class DOTermCurie(OntologyTermCurie):
    pass


class ECOTermCurie(OntologyTermCurie):
    pass


class FBCVTermCurie(OntologyTermCurie):
    pass


class GOTermCurie(OntologyTermCurie):
    pass


class MITermCurie(OntologyTermCurie):
    pass


class MMOTermCurie(OntologyTermCurie):
    pass


class MMUSDVTermCurie(OntologyTermCurie):
    pass


class SOTermCurie(OntologyTermCurie):
    pass


class CHEBITermCurie(OntologyTermCurie):
    pass


class StageTermCurie(OntologyTermCurie):
    pass


class FBDVTermCurie(StageTermCurie):
    pass


class WBLSTermCurie(StageTermCurie):
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


class FBBTTermCurie(AnatomicalTermCurie):
    pass


class MATermCurie(AnatomicalTermCurie):
    pass


class UBERONTermCurie(AnatomicalTermCurie):
    pass


class WBBTTermCurie(AnatomicalTermCurie):
    pass


class ZFATermCurie(AnatomicalTermCurie):
    pass


class PhenotypeTermCurie(OntologyTermCurie):
    pass


class PhenotypeAnnotationCurie(URIorCURIE):
    pass


class GenePhenotypeAnnotationCurie(PhenotypeAnnotationCurie):
    pass


class AllelePhenotypeAnnotationCurie(PhenotypeAnnotationCurie):
    pass


class AGMPhenotypeAnnotationCurie(PhenotypeAnnotationCurie):
    pass


class MoleculeCurie(URIorCURIE):
    pass


class VocabularyName(extended_str):
    pass


class FigureCurie(URIorCURIE):
    pass


class ImageCurie(URIorCURIE):
    pass


@dataclass
class VariantConsequence(YAMLRoot):
    """
    Parent class for gene- and transcript-level consequences
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantConsequence/VariantConsequence")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "VariantConsequence"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.VariantConsequence

    subject: Union[str, VariantCurie] = None
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
        if not isinstance(self.subject, VariantCurie):
            self.subject = VariantCurie(self.subject)

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.VariantGeneConsequence

    subject: Union[str, VariantCurie] = None
    object: Union[str, GeneCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GeneCurie):
            self.object = GeneCurie(self.object)

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.VariantTranscriptConsequence

    subject: Union[str, VariantCurie] = None
    object: Union[str, TranscriptCurie] = None
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
class VariantGenomicLocation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variantGenomicLocation/VariantGenomicLocation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "VariantGenomicLocation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.VariantGenomicLocation

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


class Entity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Entity
    class_class_curie: ClassVar[str] = "alliance:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Entity


@dataclass
class BiologicalEntity(YAMLRoot):
    """
    A high-level entity comprising .
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.BiologicalEntity
    class_class_curie: ClassVar[str] = "alliance:BiologicalEntity"
    class_name: ClassVar[str] = "BiologicalEntity"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.BiologicalEntity

    curie: Union[str, BiologicalEntityCurie] = None
    taxon: Union[str, URIorCURIE] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    table_key: Optional[int] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, BiologicalEntityCurie):
            self.curie = BiologicalEntityCurie(self.curie)

        if self._is_empty(self.taxon):
            self.MissingRequiredField("taxon")
        if not isinstance(self.taxon, URIorCURIE):
            self.taxon = URIorCURIE(self.taxon)

        if self._is_empty(self.created_by):
            self.MissingRequiredField("created_by")
        if not isinstance(self.created_by, PersonPersonId):
            self.created_by = PersonPersonId(self.created_by)

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, PersonPersonId):
            self.modified_by = PersonPersonId(self.modified_by)

        if self.table_key is not None and not isinstance(self.table_key, int):
            self.table_key = int(self.table_key)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

        super().__post_init__(**kwargs)


@dataclass
class GenomicEntity(BiologicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GenomicEntity
    class_class_curie: ClassVar[str] = "alliance:GenomicEntity"
    class_name: ClassVar[str] = "GenomicEntity"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GenomicEntity

    curie: Union[str, GenomicEntityCurie] = None
    taxon: Union[str, URIorCURIE] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
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

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, Synonym) else Synonym(**as_dict(v)) for v in self.synonyms]

        self._normalize_inlined_as_list(slot_name="cross_references", slot_type=CrossReference, key_name="curie", keyed=True)

        if not isinstance(self.secondary_identifiers, list):
            self.secondary_identifiers = [self.secondary_identifiers] if self.secondary_identifiers is not None else []
        self.secondary_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.secondary_identifiers]

        super().__post_init__(**kwargs)


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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Variant

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
    synonyms: Optional[Union[Union[dict, "Synonym"], List[Union[dict, "Synonym"]]]] = empty_list()
    type: Optional[Union[str, URIorCURIE]] = None
    references: Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]] = empty_list()
    notes: Optional[Union[str, List[str]]] = empty_list()
    protein_sequence: Optional[str] = None
    cross_references: Optional[Union[Dict[Union[str, CrossReferenceCurie], Union[dict, "CrossReference"]], List[Union[dict, "CrossReference"]]]] = empty_dict()

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

        self._normalize_inlined_as_list(slot_name="cross_references", slot_type=CrossReference, key_name="curie", keyed=True)

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Transcript

    curie: Union[str, TranscriptCurie] = None
    taxon: Union[str, URIorCURIE] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Gene

    curie: Union[str, GeneCurie] = None
    taxon: Union[str, URIorCURIE] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
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

        self._normalize_inlined_as_dict(slot_name="genomic_locations", slot_type=GeneGenomicLocation, key_name="subject", keyed=False)

        if self.gene_synopsis is not None and not isinstance(self.gene_synopsis, str):
            self.gene_synopsis = str(self.gene_synopsis)

        if self.gene_synopsis_URL is not None and not isinstance(self.gene_synopsis_URL, str):
            self.gene_synopsis_URL = str(self.gene_synopsis_URL)

        if self.gene_type is not None and not isinstance(self.gene_type, SOTermCurie):
            self.gene_type = SOTermCurie(self.gene_type)

        if self.automated_gene_description is not None and not isinstance(self.automated_gene_description, str):
            self.automated_gene_description = str(self.automated_gene_description)

        super().__post_init__(**kwargs)


class Species(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Species
    class_class_curie: ClassVar[str] = "alliance:Species"
    class_name: ClassVar[str] = "Species"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Species


class Synonym(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Synonym
    class_class_curie: ClassVar[str] = "alliance:Synonym"
    class_name: ClassVar[str] = "Synonym"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Synonym


@dataclass
class AuditedObject(YAMLRoot):
    """
    Some entity for which changes are tracked, including date/time of change and the agent responsible for the change.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AuditedObject
    class_class_curie: ClassVar[str] = "alliance:AuditedObject"
    class_name: ClassVar[str] = "AuditedObject"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AuditedObject

    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    table_key: Optional[int] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.created_by):
            self.MissingRequiredField("created_by")
        if not isinstance(self.created_by, PersonPersonId):
            self.created_by = PersonPersonId(self.created_by)

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, PersonPersonId):
            self.modified_by = PersonPersonId(self.modified_by)

        if self.table_key is not None and not isinstance(self.table_key, int):
            self.table_key = int(self.table_key)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

        super().__post_init__(**kwargs)


@dataclass
class Reagent(YAMLRoot):
    """
    A material entity used in experiments.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Reagent
    class_class_curie: ClassVar[str] = "alliance:Reagent"
    class_name: ClassVar[str] = "Reagent"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Reagent

    generated_by: Optional[Union[Union[dict, "Agent"], List[Union[dict, "Agent"]]]] = empty_list()
    manufactured_by: Optional[Union[Union[dict, "Agent"], List[Union[dict, "Agent"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.generated_by, list):
            self.generated_by = [self.generated_by] if self.generated_by is not None else []
        self.generated_by = [v if isinstance(v, Agent) else Agent(**as_dict(v)) for v in self.generated_by]

        if not isinstance(self.manufactured_by, list):
            self.manufactured_by = [self.manufactured_by] if self.manufactured_by is not None else []
        self.manufactured_by = [v if isinstance(v, Agent) else Agent(**as_dict(v)) for v in self.manufactured_by]

        super().__post_init__(**kwargs)


@dataclass
class EntityStatement(YAMLRoot):
    """
    Free-text describing some aspect of an entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.EntityStatement
    class_class_curie: ClassVar[str] = "alliance:EntityStatement"
    class_name: ClassVar[str] = "EntityStatement"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.EntityStatement

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
class Association(YAMLRoot):
    """
    A typed association between two entities, supported by evidence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Association
    class_class_curie: ClassVar[str] = "alliance:Association"
    class_name: ClassVar[str] = "Association"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Association

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.EntitySynonym

    subject: str = None
    object: Union[dict, Synonym] = None
    predicate: Union[str, "EntitySynonymTypeSet"] = None
    references: Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, Synonym):
            self.object = Synonym()

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, EntitySynonymTypeSet):
            self.predicate = EntitySynonymTypeSet(self.predicate)

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, ReferenceCurie) else ReferenceCurie(v) for v in self.references]

        super().__post_init__(**kwargs)


@dataclass
class ExternalDatabaseLink(YAMLRoot):
    """
    Base relation that holds the identifier prefix, base url and url suffix to help in generating URLs in
    crossReferences.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ExternalDatabaseLink
    class_class_curie: ClassVar[str] = "alliance:ExternalDatabaseLink"
    class_name: ClassVar[str] = "ExternalDatabaseLink"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ExternalDatabaseLink

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
class Chromosome(YAMLRoot):
    """
    The ID of the landmark used to establish the coordinate system for the current feature.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Chromosome
    class_class_curie: ClassVar[str] = "alliance:Chromosome"
    class_name: ClassVar[str] = "Chromosome"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Chromosome

    curie: Union[str, ChromosomeCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ChromosomeCurie):
            self.curie = ChromosomeCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class Assembly(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Assembly
    class_class_curie: ClassVar[str] = "alliance:Assembly"
    class_name: ClassVar[str] = "Assembly"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Assembly

    curie: Union[str, AssemblyCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, AssemblyCurie):
            self.curie = AssemblyCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class GeneGenomicLocation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GeneGenomicLocation
    class_class_curie: ClassVar[str] = "alliance:GeneGenomicLocation"
    class_name: ClassVar[str] = "GeneGenomicLocation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GeneGenomicLocation

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

    curie: Union[str, InformationContentEntityCurie] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    table_key: Optional[int] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, InformationContentEntityCurie):
            self.curie = InformationContentEntityCurie(self.curie)

        if self._is_empty(self.created_by):
            self.MissingRequiredField("created_by")
        if not isinstance(self.created_by, PersonPersonId):
            self.created_by = PersonPersonId(self.created_by)

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, PersonPersonId):
            self.modified_by = PersonPersonId(self.modified_by)

        if self.table_key is not None and not isinstance(self.table_key, int):
            self.table_key = int(self.table_key)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

        super().__post_init__(**kwargs)


@dataclass
class Reference(InformationContentEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/reference/Reference")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Reference"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Reference

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
    authors: Optional[Union[Union[dict, "AuthorReference"], List[Union[dict, "AuthorReference"]]]] = empty_list()
    tags: Optional[Union[Union[str, "TagSet"], List[Union[str, "TagSet"]]]] = empty_list()
    topics: Optional[Union[str, URIorCURIE]] = None
    cross_references: Optional[Union[Dict[Union[str, CrossReferenceCurie], Union[dict, "CrossReference"]], List[Union[dict, "CrossReference"]]]] = empty_dict()
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

        self._normalize_inlined_as_list(slot_name="cross_references", slot_type=CrossReference, key_name="curie", keyed=True)

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


@dataclass
class Resource(InformationContentEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/resource/Resource")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Resource

    curie: Union[str, ResourceCurie] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    title: Optional[str] = None
    iso_abbreviation: Optional[str] = None
    medline_abbreviation: Optional[str] = None
    copyright_date: Optional[Union[str, XSDDate]] = None
    print_issn: Optional[str] = None
    online_issn: Optional[str] = None
    publisher: Optional[Union[str, InformationContentEntityCurie]] = None
    volumes: Optional[str] = None
    summary: Optional[str] = None
    synonyms: Optional[Union[Union[dict, "Synonym"], List[Union[dict, "Synonym"]]]] = empty_list()
    authors: Optional[Union[Union[dict, "AuthorReference"], List[Union[dict, "AuthorReference"]]]] = empty_list()
    editors: Optional[Union[Union[dict, "AuthorReference"], List[Union[dict, "AuthorReference"]]]] = empty_list()
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

        if self.publisher is not None and not isinstance(self.publisher, InformationContentEntityCurie):
            self.publisher = InformationContentEntityCurie(self.publisher)

        if self.volumes is not None and not isinstance(self.volumes, str):
            self.volumes = str(self.volumes)

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, Synonym) else Synonym(**as_dict(v)) for v in self.synonyms]

        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, AuthorReference) else AuthorReference(**as_dict(v)) for v in self.authors]

        if not isinstance(self.editors, list):
            self.editors = [self.editors] if self.editors is not None else []
        self.editors = [v if isinstance(v, AuthorReference) else AuthorReference(**as_dict(v)) for v in self.editors]

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        super().__post_init__(**kwargs)


@dataclass
class CrossReference(InformationContentEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.CrossReference
    class_class_curie: ClassVar[str] = "alliance:CrossReference"
    class_name: ClassVar[str] = "CrossReference"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.CrossReference

    curie: Union[str, CrossReferenceCurie] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
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
class AuthorReference(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AuthorReference
    class_class_curie: ClassVar[str] = "alliance:AuthorReference"
    class_name: ClassVar[str] = "AuthorReference"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AuthorReference

    corresponding_author: Optional[Union[str, InformationContentEntityCurie]] = None
    first_name: Optional[Union[str, InformationContentEntityCurie]] = None
    middle_names: Optional[Union[str, InformationContentEntityCurie]] = None
    last_name: Optional[Union[str, InformationContentEntityCurie]] = None
    initials: Optional[Union[str, InformationContentEntityCurie]] = None
    cross_references: Optional[Union[Dict[Union[str, CrossReferenceCurie], Union[dict, CrossReference]], List[Union[dict, CrossReference]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.corresponding_author is not None and not isinstance(self.corresponding_author, InformationContentEntityCurie):
            self.corresponding_author = InformationContentEntityCurie(self.corresponding_author)

        if self.first_name is not None and not isinstance(self.first_name, InformationContentEntityCurie):
            self.first_name = InformationContentEntityCurie(self.first_name)

        if self.middle_names is not None and not isinstance(self.middle_names, InformationContentEntityCurie):
            self.middle_names = InformationContentEntityCurie(self.middle_names)

        if self.last_name is not None and not isinstance(self.last_name, InformationContentEntityCurie):
            self.last_name = InformationContentEntityCurie(self.last_name)

        if self.initials is not None and not isinstance(self.initials, InformationContentEntityCurie):
            self.initials = InformationContentEntityCurie(self.initials)

        self._normalize_inlined_as_list(slot_name="cross_references", slot_type=CrossReference, key_name="curie", keyed=True)

        super().__post_init__(**kwargs)


class Agent(YAMLRoot):
    """
    An individual, group, organization or project that provides information and/or materials.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Agent
    class_class_curie: ClassVar[str] = "alliance:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Agent


class Organization(Agent):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Organization
    class_class_curie: ClassVar[str] = "alliance:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Organization


class Laboratory(Organization):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Laboratory
    class_class_curie: ClassVar[str] = "alliance:Laboratory"
    class_name: ClassVar[str] = "Laboratory"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Laboratory


class Company(Organization):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Company
    class_class_curie: ClassVar[str] = "alliance:Company"
    class_name: ClassVar[str] = "Company"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Company


@dataclass
class Person(Agent):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Person
    class_class_curie: ClassVar[str] = "alliance:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Person

    person_id: Union[str, PersonPersonId] = None
    last_name: Optional[Union[str, InformationContentEntityCurie]] = None
    first_name: Optional[Union[str, InformationContentEntityCurie]] = None
    orcid: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.person_id):
            self.MissingRequiredField("person_id")
        if not isinstance(self.person_id, PersonPersonId):
            self.person_id = PersonPersonId(self.person_id)

        if self.last_name is not None and not isinstance(self.last_name, InformationContentEntityCurie):
            self.last_name = InformationContentEntityCurie(self.last_name)

        if self.first_name is not None and not isinstance(self.first_name, InformationContentEntityCurie):
            self.first_name = InformationContentEntityCurie(self.first_name)

        if self.orcid is not None and not isinstance(self.orcid, str):
            self.orcid = str(self.orcid)

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Allele

    curie: Union[str, AlleleCurie] = None
    taxon: Union[str, URIorCURIE] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    symbol: Optional[str] = None
    affected_entities: Optional[Union[Union[str, BiologicalEntityCurie], List[Union[str, BiologicalEntityCurie]]]] = empty_list()
    contains_construct: Optional[Union[str, ConstructCurie]] = None
    molecular_mutation: Optional[Union[dict, "MolecularMutation"]] = None
    functional_impact: Optional[str] = None
    generation_method: Optional[str] = None
    associated_references: Optional[Union[Union[dict, "ReferenceType"], List[Union[dict, "ReferenceType"]]]] = empty_list()
    associated_notes: Optional[Union[dict, "NoteType"]] = None
    germline_transmission_status: Optional[str] = None
    parent_cell_line: Optional[Union[dict, "CellLine"]] = None
    mutant_cell_lines: Optional[Union[Union[dict, "CellLine"], List[Union[dict, "CellLine"]]]] = empty_list()
    embryonic_stem_cell_lines: Optional[Union[Union[dict, "CellLine"], List[Union[dict, "CellLine"]]]] = empty_list()
    images: Optional[Union[str, ImageCurie]] = None
    origins: Optional[Union[Union[str, AffectedGenomicModelCurie], List[Union[str, AffectedGenomicModelCurie]]]] = empty_list()
    database_status: Optional[Union[str, "DatabaseStatuses"]] = None
    inheritence_mode: Optional[Union[str, "ModesOfInheritence"]] = None
    in_collection: Optional[str] = None
    transposon_insertion: Optional[str] = None
    aberration: Optional[str] = None
    is_extinct: Optional[Union[bool, Bool]] = None
    synonyms: Optional[Union[Union[dict, Synonym], List[Union[dict, Synonym]]]] = empty_list()
    embryonic_cell_lines: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, AlleleCurie):
            self.curie = AlleleCurie(self.curie)

        if self.symbol is not None and not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        if not isinstance(self.affected_entities, list):
            self.affected_entities = [self.affected_entities] if self.affected_entities is not None else []
        self.affected_entities = [v if isinstance(v, BiologicalEntityCurie) else BiologicalEntityCurie(v) for v in self.affected_entities]

        if self.contains_construct is not None and not isinstance(self.contains_construct, ConstructCurie):
            self.contains_construct = ConstructCurie(self.contains_construct)

        if self.molecular_mutation is not None and not isinstance(self.molecular_mutation, MolecularMutation):
            self.molecular_mutation = MolecularMutation(**as_dict(self.molecular_mutation))

        if self.functional_impact is not None and not isinstance(self.functional_impact, str):
            self.functional_impact = str(self.functional_impact)

        if self.generation_method is not None and not isinstance(self.generation_method, str):
            self.generation_method = str(self.generation_method)

        if not isinstance(self.associated_references, list):
            self.associated_references = [self.associated_references] if self.associated_references is not None else []
        self.associated_references = [v if isinstance(v, ReferenceType) else ReferenceType(**as_dict(v)) for v in self.associated_references]

        if self.associated_notes is not None and not isinstance(self.associated_notes, NoteType):
            self.associated_notes = NoteType(**as_dict(self.associated_notes))

        if self.germline_transmission_status is not None and not isinstance(self.germline_transmission_status, str):
            self.germline_transmission_status = str(self.germline_transmission_status)

        if self.parent_cell_line is not None and not isinstance(self.parent_cell_line, CellLine):
            self.parent_cell_line = CellLine()

        if not isinstance(self.mutant_cell_lines, list):
            self.mutant_cell_lines = [self.mutant_cell_lines] if self.mutant_cell_lines is not None else []
        self.mutant_cell_lines = [v if isinstance(v, CellLine) else CellLine(**as_dict(v)) for v in self.mutant_cell_lines]

        if not isinstance(self.embryonic_stem_cell_lines, list):
            self.embryonic_stem_cell_lines = [self.embryonic_stem_cell_lines] if self.embryonic_stem_cell_lines is not None else []
        self.embryonic_stem_cell_lines = [v if isinstance(v, CellLine) else CellLine(**as_dict(v)) for v in self.embryonic_stem_cell_lines]

        if self.images is not None and not isinstance(self.images, ImageCurie):
            self.images = ImageCurie(self.images)

        if not isinstance(self.origins, list):
            self.origins = [self.origins] if self.origins is not None else []
        self.origins = [v if isinstance(v, AffectedGenomicModelCurie) else AffectedGenomicModelCurie(v) for v in self.origins]

        if self.database_status is not None and not isinstance(self.database_status, DatabaseStatuses):
            self.database_status = DatabaseStatuses(self.database_status)

        if self.inheritence_mode is not None and not isinstance(self.inheritence_mode, ModesOfInheritence):
            self.inheritence_mode = ModesOfInheritence(self.inheritence_mode)

        if self.in_collection is not None and not isinstance(self.in_collection, str):
            self.in_collection = str(self.in_collection)

        if self.transposon_insertion is not None and not isinstance(self.transposon_insertion, str):
            self.transposon_insertion = str(self.transposon_insertion)

        if self.aberration is not None and not isinstance(self.aberration, str):
            self.aberration = str(self.aberration)

        if self.is_extinct is not None and not isinstance(self.is_extinct, Bool):
            self.is_extinct = Bool(self.is_extinct)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, Synonym) else Synonym(**as_dict(v)) for v in self.synonyms]

        if self.embryonic_cell_lines is not None and not isinstance(self.embryonic_cell_lines, str):
            self.embryonic_cell_lines = str(self.embryonic_cell_lines)

        super().__post_init__(**kwargs)


@dataclass
class ReferenceType(YAMLRoot):
    """
    Describes the relation between a reference and an object
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/ReferenceType")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ReferenceType"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ReferenceType

    reference_association: Optional[Union[str, "ReferenceAssociationTypes"]] = None
    references: Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.reference_association is not None and not isinstance(self.reference_association, ReferenceAssociationTypes):
            self.reference_association = ReferenceAssociationTypes(self.reference_association)

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, ReferenceCurie) else ReferenceCurie(v) for v in self.references]

        super().__post_init__(**kwargs)


@dataclass
class NoteType(YAMLRoot):
    """
    Describes the relation between a note and an object
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/NoteType")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "NoteType"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.NoteType

    note_association: Optional[Union[str, "NoteAssociationTypes"]] = None
    notes: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.note_association is not None and not isinstance(self.note_association, NoteAssociationTypes):
            self.note_association = NoteAssociationTypes(self.note_association)

        if not isinstance(self.notes, list):
            self.notes = [self.notes] if self.notes is not None else []
        self.notes = [v if isinstance(v, str) else str(v) for v in self.notes]

        super().__post_init__(**kwargs)


@dataclass
class Construct(GenomicEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/Construct")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Construct"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Construct

    curie: Union[str, ConstructCurie] = None
    taxon: Union[str, URIorCURIE] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    construct_components: Optional[Union[Union[str, ConstructComponentCurie], List[Union[str, ConstructComponentCurie]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ConstructCurie):
            self.curie = ConstructCurie(self.curie)

        if not isinstance(self.construct_components, list):
            self.construct_components = [self.construct_components] if self.construct_components is not None else []
        self.construct_components = [v if isinstance(v, ConstructComponentCurie) else ConstructComponentCurie(v) for v in self.construct_components]

        super().__post_init__(**kwargs)


@dataclass
class ConstructComponent(GenomicEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/ConstructComponent")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ConstructComponent"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ConstructComponent

    curie: Union[str, ConstructComponentCurie] = None
    taxon: Union[str, URIorCURIE] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    component_relation: Optional[Union[str, "ComponentRelationsEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ConstructComponentCurie):
            self.curie = ConstructComponentCurie(self.curie)

        if self.component_relation is not None and not isinstance(self.component_relation, ComponentRelationsEnum):
            self.component_relation = ComponentRelationsEnum(self.component_relation)

        super().__post_init__(**kwargs)


@dataclass
class MolecularMutation(YAMLRoot):
    """
    Description of the DNA changes with unknown precise genomic location
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/MolecularMutation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "MolecularMutation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.MolecularMutation

    mutation_type: Union[str, SOTermCurie] = None
    mutation_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.mutation_type):
            self.MissingRequiredField("mutation_type")
        if not isinstance(self.mutation_type, SOTermCurie):
            self.mutation_type = SOTermCurie(self.mutation_type)

        if self.mutation_description is not None and not isinstance(self.mutation_description, str):
            self.mutation_description = str(self.mutation_description)

        super().__post_init__(**kwargs)


class CellLine(YAMLRoot):
    """
    Dummy cell line class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/CellLine")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CellLine"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.CellLine


class SequenceTargetingReagent(YAMLRoot):
    """
    Dummy sequence targeting reagent class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/SequenceTargetingReagent")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SequenceTargetingReagent"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.SequenceTargetingReagent


@dataclass
class AffectedGenomicModel(GenomicEntity):
    """
    Includes inbred strains, stocks, disease models and mutant genotypes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/affectedGenomicModel/AffectedGenomicModel")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AffectedGenomicModel"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AffectedGenomicModel

    curie: Union[str, AffectedGenomicModelCurie] = None
    taxon: Union[str, URIorCURIE] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    subtype: Optional[Union[str, "SubtypeValues"]] = None
    components: Optional[Union[Union[dict, "AffectedGenomicModelComponent"], List[Union[dict, "AffectedGenomicModelComponent"]]]] = empty_list()
    sequence_targeting_reagents: Optional[Union[Union[dict, SequenceTargetingReagent], List[Union[dict, SequenceTargetingReagent]]]] = empty_list()
    parental_populations: Optional[Union[str, URIorCURIE]] = None
    data_provider: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, AffectedGenomicModelCurie):
            self.curie = AffectedGenomicModelCurie(self.curie)

        if self.subtype is not None and not isinstance(self.subtype, SubtypeValues):
            self.subtype = SubtypeValues(self.subtype)

        if not isinstance(self.components, list):
            self.components = [self.components] if self.components is not None else []
        self.components = [v if isinstance(v, AffectedGenomicModelComponent) else AffectedGenomicModelComponent(**as_dict(v)) for v in self.components]

        if not isinstance(self.sequence_targeting_reagents, list):
            self.sequence_targeting_reagents = [self.sequence_targeting_reagents] if self.sequence_targeting_reagents is not None else []
        self.sequence_targeting_reagents = [v if isinstance(v, SequenceTargetingReagent) else SequenceTargetingReagent(**as_dict(v)) for v in self.sequence_targeting_reagents]

        if self.parental_populations is not None and not isinstance(self.parental_populations, URIorCURIE):
            self.parental_populations = URIorCURIE(self.parental_populations)

        if not isinstance(self.data_provider, list):
            self.data_provider = [self.data_provider] if self.data_provider is not None else []
        self.data_provider = [v if isinstance(v, str) else str(v) for v in self.data_provider]

        super().__post_init__(**kwargs)


@dataclass
class AffectedGenomicModelComponent(YAMLRoot):
    """
    Allele that affects the model and its zygosity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/affectedGenomicModel/AffectedGenomicModelComponent")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AffectedGenomicModelComponent"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AffectedGenomicModelComponent

    has_allele: Optional[Union[str, AlleleCurie]] = None
    zygosity: Optional[Union[str, "ZygosityValues"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_allele is not None and not isinstance(self.has_allele, AlleleCurie):
            self.has_allele = AlleleCurie(self.has_allele)

        if self.zygosity is not None and not isinstance(self.zygosity, ZygosityValues):
            self.zygosity = ZygosityValues(self.zygosity)

        super().__post_init__(**kwargs)


@dataclass
class Antibody(BiologicalEntity):
    """
    Immunoglobulin proteins that bind specific molecule(s). Can be used experimentally for the purposes of detection
    or purification.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/antibody.yaml/Antibody")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Antibody"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Antibody

    curie: Union[str, AntibodyCurie] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    name: str = None
    clonality: Union[str, "AntibodyClonalitySet"] = None
    table_key: Optional[int] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None
    antigen_taxon: Optional[Union[str, URIorCURIE]] = None
    heavy_chain_isotype: Optional[Union[str, "HeavyChainIsotypeSet"]] = None
    light_chain_isotype: Optional[Union[str, "LightChainIsotypeSet"]] = None
    antibody_target_genes: Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]] = empty_list()
    cross_references: Optional[Union[Dict[Union[str, CrossReferenceCurie], Union[dict, CrossReference]], List[Union[dict, CrossReference]]]] = empty_dict()
    secondary_identifiers: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    references: Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]] = empty_list()
    original_reference: Optional[Union[str, ReferenceCurie]] = None
    taxon: Optional[Union[str, URIorCURIE]] = None
    generated_by: Optional[Union[Union[dict, Agent], List[Union[dict, Agent]]]] = empty_list()
    manufactured_by: Optional[Union[Union[dict, Agent], List[Union[dict, Agent]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, AntibodyCurie):
            self.curie = AntibodyCurie(self.curie)

        if self._is_empty(self.created_by):
            self.MissingRequiredField("created_by")
        if not isinstance(self.created_by, PersonPersonId):
            self.created_by = PersonPersonId(self.created_by)

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, PersonPersonId):
            self.modified_by = PersonPersonId(self.modified_by)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.clonality):
            self.MissingRequiredField("clonality")
        if not isinstance(self.clonality, AntibodyClonalitySet):
            self.clonality = AntibodyClonalitySet(self.clonality)

        if self.table_key is not None and not isinstance(self.table_key, int):
            self.table_key = int(self.table_key)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

        if self.antigen_taxon is not None and not isinstance(self.antigen_taxon, URIorCURIE):
            self.antigen_taxon = URIorCURIE(self.antigen_taxon)

        if self.heavy_chain_isotype is not None and not isinstance(self.heavy_chain_isotype, HeavyChainIsotypeSet):
            self.heavy_chain_isotype = HeavyChainIsotypeSet(self.heavy_chain_isotype)

        if self.light_chain_isotype is not None and not isinstance(self.light_chain_isotype, LightChainIsotypeSet):
            self.light_chain_isotype = LightChainIsotypeSet(self.light_chain_isotype)

        if not isinstance(self.antibody_target_genes, list):
            self.antibody_target_genes = [self.antibody_target_genes] if self.antibody_target_genes is not None else []
        self.antibody_target_genes = [v if isinstance(v, GeneCurie) else GeneCurie(v) for v in self.antibody_target_genes]

        self._normalize_inlined_as_list(slot_name="cross_references", slot_type=CrossReference, key_name="curie", keyed=True)

        if not isinstance(self.secondary_identifiers, list):
            self.secondary_identifiers = [self.secondary_identifiers] if self.secondary_identifiers is not None else []
        self.secondary_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.secondary_identifiers]

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, ReferenceCurie) else ReferenceCurie(v) for v in self.references]

        if self.original_reference is not None and not isinstance(self.original_reference, ReferenceCurie):
            self.original_reference = ReferenceCurie(self.original_reference)

        if self.taxon is not None and not isinstance(self.taxon, URIorCURIE):
            self.taxon = URIorCURIE(self.taxon)

        if not isinstance(self.generated_by, list):
            self.generated_by = [self.generated_by] if self.generated_by is not None else []
        self.generated_by = [v if isinstance(v, Agent) else Agent(**as_dict(v)) for v in self.generated_by]

        if not isinstance(self.manufactured_by, list):
            self.manufactured_by = [self.manufactured_by] if self.manufactured_by is not None else []
        self.manufactured_by = [v if isinstance(v, Agent) else Agent(**as_dict(v)) for v in self.manufactured_by]

        super().__post_init__(**kwargs)


@dataclass
class AntibodyNote(EntityStatement):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/antibody.yaml/AntibodyNote")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AntibodyNote"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AntibodyNote

    note_type: Optional[Union[str, "AntibodyNoteTypeSet"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.note_type is not None and not isinstance(self.note_type, AntibodyNoteTypeSet):
            self.note_type = AntibodyNoteTypeSet(self.note_type)

        super().__post_init__(**kwargs)


@dataclass
class GeneToGeneAssociation(Association):
    """
    abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes
    homology and interaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GeneToGeneAssociation
    class_class_curie: ClassVar[str] = "alliance:GeneToGeneAssociation"
    class_name: ClassVar[str] = "GeneToGeneAssociation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GeneToGeneAssociation

    predicate: str = None
    subject: Union[str, GeneCurie] = None
    object: Union[str, GeneCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GeneCurie):
            self.subject = GeneCurie(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GeneCurie):
            self.object = GeneCurie(self.object)

        super().__post_init__(**kwargs)


@dataclass
class GeneInteraction(GeneToGeneAssociation):
    """
    An interaction between two genes or gene products; this may be a physical molecular interaction between gene
    products (e.g. protein-protein interactions), or may be a genetic interaction between genes (e.g. phenotypic
    suppression)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GeneInteraction
    class_class_curie: ClassVar[str] = "alliance:GeneInteraction"
    class_name: ClassVar[str] = "GeneInteraction"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GeneInteraction

    curie: Union[str, GeneInteractionCurie] = None
    interaction_data_provider: Union[str, "InteractionSourceEnum"] = None
    interaction_type: Union[str, "InteractionTypeEnum"] = None
    interactor_A_type: Union[str, "InteractorTypeEnum"] = None
    interactor_B_type: Union[str, "InteractorTypeEnum"] = None
    subject: Union[str, GeneCurie] = None
    predicate: str = None
    object: Union[str, GeneCurie] = None
    cross_references: Optional[Union[Dict[Union[str, CrossReferenceCurie], Union[dict, CrossReference]], List[Union[dict, CrossReference]]]] = empty_dict()
    interactor_A_role: Optional[Union[Union[str, "InteractorARoleEnum"], List[Union[str, "InteractorARoleEnum"]]]] = empty_list()
    interactor_B_role: Optional[Union[Union[str, "InteractorBRoleEnum"], List[Union[str, "InteractorBRoleEnum"]]]] = empty_list()
    references: Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, GeneInteractionCurie):
            self.curie = GeneInteractionCurie(self.curie)

        if self._is_empty(self.interaction_data_provider):
            self.MissingRequiredField("interaction_data_provider")
        if not isinstance(self.interaction_data_provider, InteractionSourceEnum):
            self.interaction_data_provider = InteractionSourceEnum(self.interaction_data_provider)

        if self._is_empty(self.interaction_type):
            self.MissingRequiredField("interaction_type")
        if not isinstance(self.interaction_type, InteractionTypeEnum):
            self.interaction_type = InteractionTypeEnum(self.interaction_type)

        if self._is_empty(self.interactor_A_type):
            self.MissingRequiredField("interactor_A_type")
        if not isinstance(self.interactor_A_type, InteractorTypeEnum):
            self.interactor_A_type = InteractorTypeEnum(self.interactor_A_type)

        if self._is_empty(self.interactor_B_type):
            self.MissingRequiredField("interactor_B_type")
        if not isinstance(self.interactor_B_type, InteractorTypeEnum):
            self.interactor_B_type = InteractorTypeEnum(self.interactor_B_type)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GeneCurie):
            self.subject = GeneCurie(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GeneCurie):
            self.object = GeneCurie(self.object)

        self._normalize_inlined_as_list(slot_name="cross_references", slot_type=CrossReference, key_name="curie", keyed=True)

        if not isinstance(self.interactor_A_role, list):
            self.interactor_A_role = [self.interactor_A_role] if self.interactor_A_role is not None else []
        self.interactor_A_role = [v if isinstance(v, InteractorARoleEnum) else InteractorARoleEnum(v) for v in self.interactor_A_role]

        if not isinstance(self.interactor_B_role, list):
            self.interactor_B_role = [self.interactor_B_role] if self.interactor_B_role is not None else []
        self.interactor_B_role = [v if isinstance(v, InteractorBRoleEnum) else InteractorBRoleEnum(v) for v in self.interactor_B_role]

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, ReferenceCurie) else ReferenceCurie(v) for v in self.references]

        super().__post_init__(**kwargs)


@dataclass
class GeneMolecularInteraction(GeneInteraction):
    """
    A physical molecular interaction between gene products (e.g. protein-protein interactions or protein-RNA
    interactions) or between genes and DNA-binding factors (e.g. protein-DNA interactions)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GeneMolecularInteraction
    class_class_curie: ClassVar[str] = "alliance:GeneMolecularInteraction"
    class_name: ClassVar[str] = "GeneMolecularInteraction"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GeneMolecularInteraction

    curie: Union[str, GeneMolecularInteractionCurie] = None
    interaction_data_provider: Union[str, "InteractionSourceEnum"] = None
    interaction_type: Union[str, "InteractionTypeEnum"] = None
    interactor_A_type: Union[str, "InteractorTypeEnum"] = None
    interactor_B_type: Union[str, "InteractorTypeEnum"] = None
    subject: Union[str, GeneCurie] = None
    object: Union[str, GeneCurie] = None
    predicate: str = None
    aggregation_database: Optional[Union[str, "AggregationDatabaseEnum"]] = None
    detection_method: Optional[Union[str, "DetectionMethodsEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, GeneMolecularInteractionCurie):
            self.curie = GeneMolecularInteractionCurie(self.curie)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self.aggregation_database is not None and not isinstance(self.aggregation_database, AggregationDatabaseEnum):
            self.aggregation_database = AggregationDatabaseEnum(self.aggregation_database)

        if self.detection_method is not None and not isinstance(self.detection_method, DetectionMethodsEnum):
            self.detection_method = DetectionMethodsEnum(self.detection_method)

        super().__post_init__(**kwargs)


@dataclass
class GeneGeneticInteraction(GeneInteraction):
    """
    A genetic interaction between genes (e.g. phenotypic suppression)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GeneGeneticInteraction
    class_class_curie: ClassVar[str] = "alliance:GeneGeneticInteraction"
    class_name: ClassVar[str] = "GeneGeneticInteraction"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GeneGeneticInteraction

    curie: Union[str, GeneGeneticInteractionCurie] = None
    interaction_data_provider: Union[str, "InteractionSourceEnum"] = None
    interaction_type: Union[str, "InteractionTypeEnum"] = None
    interactor_A_type: Union[str, "InteractorTypeEnum"] = None
    interactor_B_type: Union[str, "InteractorTypeEnum"] = None
    subject: Union[str, GeneCurie] = None
    object: Union[str, GeneCurie] = None
    predicate: str = None
    interactor_A_genetic_perturbation: Optional[Union[str, AlleleCurie]] = None
    interactor_B_genetic_perturbation: Optional[Union[str, AlleleCurie]] = None
    phenotype_or_trait: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, GeneGeneticInteractionCurie):
            self.curie = GeneGeneticInteractionCurie(self.curie)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self.interactor_A_genetic_perturbation is not None and not isinstance(self.interactor_A_genetic_perturbation, AlleleCurie):
            self.interactor_A_genetic_perturbation = AlleleCurie(self.interactor_A_genetic_perturbation)

        if self.interactor_B_genetic_perturbation is not None and not isinstance(self.interactor_B_genetic_perturbation, AlleleCurie):
            self.interactor_B_genetic_perturbation = AlleleCurie(self.interactor_B_genetic_perturbation)

        if not isinstance(self.phenotype_or_trait, list):
            self.phenotype_or_trait = [self.phenotype_or_trait] if self.phenotype_or_trait is not None else []
        self.phenotype_or_trait = [v if isinstance(v, str) else str(v) for v in self.phenotype_or_trait]

        super().__post_init__(**kwargs)


@dataclass
class OntologyTerm(YAMLRoot):
    """
    A concept or class in an ontology, vocabulary or thesaurus. Note, ontology terms can be found in multiple
    ontologies (ie: mireoting). defining_slots helps define an alternative key for ontology terms.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/OntologyTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "OntologyTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.OntologyTerm

    curie: Union[str, OntologyTermCurie] = None
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

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, Synonym) else Synonym(**as_dict(v)) for v in self.synonyms]

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.DOTerm

    curie: Union[str, DOTermCurie] = None

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ECOTerm

    curie: Union[str, ECOTermCurie] = None
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
class FBCVTerm(OntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/FBCVTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "FBCVTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.FBCVTerm

    curie: Union[str, FBCVTermCurie] = None

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GOTerm

    curie: Union[str, GOTermCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, GOTermCurie):
            self.curie = GOTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class MITerm(OntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/MITerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "MITerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.MITerm

    curie: Union[str, MITermCurie] = None

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.MMOTerm

    curie: Union[str, MMOTermCurie] = None

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.MMUSDVTerm

    curie: Union[str, MMUSDVTermCurie] = None

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.SOTerm

    curie: Union[str, SOTermCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, SOTermCurie):
            self.curie = SOTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class CHEBITerm(OntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/CHEBITerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CHEBITerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.CHEBITerm

    curie: Union[str, CHEBITermCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, CHEBITermCurie):
            self.curie = CHEBITermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class StageTerm(OntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/StageTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "StageTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.StageTerm

    curie: Union[str, StageTermCurie] = None

@dataclass
class FBDVTerm(StageTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/FBDVTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "FBDVTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.FBDVTerm

    curie: Union[str, FBDVTermCurie] = None

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.WBLSTerm

    curie: Union[str, WBLSTermCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, WBLSTermCurie):
            self.curie = WBLSTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class ZFSTerm(StageTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/ZFSTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ZFSTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ZFSTerm

    curie: Union[str, ZFSTermCurie] = None

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ExperimentalConditionOntologyTerm

    curie: Union[str, ExperimentalConditionOntologyTermCurie] = None

@dataclass
class ZECOTerm(ExperimentalConditionOntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/ZECOTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ZECOTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ZECOTerm

    curie: Union[str, ZECOTermCurie] = None

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.XCOTerm

    curie: Union[str, XCOTermCurie] = None

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AnatomicalTerm

    curie: Union[str, AnatomicalTermCurie] = None

@dataclass
class CLTerm(AnatomicalTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/CLTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CLTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.CLTerm

    curie: Union[str, CLTermCurie] = None

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.EMAPATerm

    curie: Union[str, EMAPATermCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, EMAPATermCurie):
            self.curie = EMAPATermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class FBBTTerm(AnatomicalTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/FBBTTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "FBBTTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.FBBTTerm

    curie: Union[str, FBBTTermCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, FBBTTermCurie):
            self.curie = FBBTTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class MATerm(AnatomicalTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/MATerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "MATerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.MATerm

    curie: Union[str, MATermCurie] = None

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.UBERONTerm

    curie: Union[str, UBERONTermCurie] = None

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.WBBTTerm

    curie: Union[str, WBBTTermCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, WBBTTermCurie):
            self.curie = WBBTTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class ZFATerm(AnatomicalTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/ZFATerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ZFATerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ZFATerm

    curie: Union[str, ZFATermCurie] = None

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.PhenotypeTerm

    curie: Union[str, PhenotypeTermCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, PhenotypeTermCurie):
            self.curie = PhenotypeTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class PhenotypeAnnotation(Association):
    """
    An annotation asserting an association between a biological entity and a phenotype supported by evidence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.PhenotypeAnnotation
    class_class_curie: ClassVar[str] = "alliance:PhenotypeAnnotation"
    class_name: ClassVar[str] = "PhenotypeAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.PhenotypeAnnotation

    curie: Union[str, PhenotypeAnnotationCurie] = None
    predicate: str = None
    subject: Union[str, BiologicalEntityCurie] = None
    object: str = None
    creation_date: Union[str, XSDDate] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    reference: Optional[Union[str, ReferenceCurie]] = None
    phenotype_term: Optional[Union[str, PhenotypeTermCurie]] = None
    condition_relations: Optional[Union[Union[dict, "ConditionRelation"], List[Union[dict, "ConditionRelation"]]]] = empty_list()
    table_key: Optional[int] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, PhenotypeAnnotationCurie):
            self.curie = PhenotypeAnnotationCurie(self.curie)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, BiologicalEntityCurie):
            self.subject = BiologicalEntityCurie(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, str):
            self.object = str(self.object)

        if self._is_empty(self.creation_date):
            self.MissingRequiredField("creation_date")
        if not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self._is_empty(self.created_by):
            self.MissingRequiredField("created_by")
        if not isinstance(self.created_by, PersonPersonId):
            self.created_by = PersonPersonId(self.created_by)

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, PersonPersonId):
            self.modified_by = PersonPersonId(self.modified_by)

        if self.reference is not None and not isinstance(self.reference, ReferenceCurie):
            self.reference = ReferenceCurie(self.reference)

        if self.phenotype_term is not None and not isinstance(self.phenotype_term, PhenotypeTermCurie):
            self.phenotype_term = PhenotypeTermCurie(self.phenotype_term)

        if not isinstance(self.condition_relations, list):
            self.condition_relations = [self.condition_relations] if self.condition_relations is not None else []
        self.condition_relations = [v if isinstance(v, ConditionRelation) else ConditionRelation(**as_dict(v)) for v in self.condition_relations]

        if self.table_key is not None and not isinstance(self.table_key, int):
            self.table_key = int(self.table_key)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

        super().__post_init__(**kwargs)


@dataclass
class GenePhenotypeAnnotation(PhenotypeAnnotation):
    """
    An annotation asserting an association between a gene and a phenotype supported by evidence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GenePhenotypeAnnotation
    class_class_curie: ClassVar[str] = "alliance:GenePhenotypeAnnotation"
    class_name: ClassVar[str] = "GenePhenotypeAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GenePhenotypeAnnotation

    curie: Union[str, GenePhenotypeAnnotationCurie] = None
    predicate: str = None
    object: str = None
    creation_date: Union[str, XSDDate] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    subject: Union[str, GeneCurie] = None
    sgd_strain_background: Optional[Union[str, AffectedGenomicModelCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, GenePhenotypeAnnotationCurie):
            self.curie = GenePhenotypeAnnotationCurie(self.curie)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GeneCurie):
            self.subject = GeneCurie(self.subject)

        if self.sgd_strain_background is not None and not isinstance(self.sgd_strain_background, AffectedGenomicModelCurie):
            self.sgd_strain_background = AffectedGenomicModelCurie(self.sgd_strain_background)

        super().__post_init__(**kwargs)


@dataclass
class AllelePhenotypeAnnotation(PhenotypeAnnotation):
    """
    An annotation asserting an association between an allele and a phenotype supported by evidence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AllelePhenotypeAnnotation
    class_class_curie: ClassVar[str] = "alliance:AllelePhenotypeAnnotation"
    class_name: ClassVar[str] = "AllelePhenotypeAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AllelePhenotypeAnnotation

    curie: Union[str, AllelePhenotypeAnnotationCurie] = None
    predicate: str = None
    object: str = None
    creation_date: Union[str, XSDDate] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    subject: Union[str, AlleleCurie] = None
    inferred_gene: Optional[Union[str, GeneCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, AllelePhenotypeAnnotationCurie):
            self.curie = AllelePhenotypeAnnotationCurie(self.curie)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, AlleleCurie):
            self.subject = AlleleCurie(self.subject)

        if self.inferred_gene is not None and not isinstance(self.inferred_gene, GeneCurie):
            self.inferred_gene = GeneCurie(self.inferred_gene)

        super().__post_init__(**kwargs)


@dataclass
class AGMPhenotypeAnnotation(PhenotypeAnnotation):
    """
    An annotation asserting an association between an AGM and a phenotype supported by evidence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AGMPhenotypeAnnotation
    class_class_curie: ClassVar[str] = "alliance:AGMPhenotypeAnnotation"
    class_name: ClassVar[str] = "AGMPhenotypeAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AGMPhenotypeAnnotation

    curie: Union[str, AGMPhenotypeAnnotationCurie] = None
    predicate: str = None
    object: str = None
    creation_date: Union[str, XSDDate] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    subject: Union[str, AffectedGenomicModelCurie] = None
    inferred_allele: Optional[Union[str, AlleleCurie]] = None
    inferred_gene: Optional[Union[str, GeneCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, AGMPhenotypeAnnotationCurie):
            self.curie = AGMPhenotypeAnnotationCurie(self.curie)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, AffectedGenomicModelCurie):
            self.subject = AffectedGenomicModelCurie(self.subject)

        if self.inferred_allele is not None and not isinstance(self.inferred_allele, AlleleCurie):
            self.inferred_allele = AlleleCurie(self.inferred_allele)

        if self.inferred_gene is not None and not isinstance(self.inferred_gene, GeneCurie):
            self.inferred_gene = GeneCurie(self.inferred_gene)

        super().__post_init__(**kwargs)


@dataclass
class DiseaseAnnotation(Association):
    """
    An annotation asserting an association between a biological entity and a disease supported by evidence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.DiseaseAnnotation
    class_class_curie: ClassVar[str] = "alliance:DiseaseAnnotation"
    class_name: ClassVar[str] = "DiseaseAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.DiseaseAnnotation

    evidence_codes: Union[Union[str, ECOTermCurie], List[Union[str, ECOTermCurie]]] = None
    reference: Union[str, ReferenceCurie] = None
    data_provider: Union[str, List[str]] = None
    subject: Union[str, BiologicalEntityCurie] = None
    predicate: str = None
    object: Union[str, DOTermCurie] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    unique_id: Optional[str] = None
    mod_id: Optional[str] = None
    negated: Optional[Union[bool, Bool]] = None
    annotation_type: Optional[Union[str, "AnnotationTypeEnum"]] = None
    with: Optional[Union[str, GeneCurie]] = None
    disease_qualifiers: Optional[Union[str, "DiseaseAnnotationQualifierEnum"]] = None
    condition_relations: Optional[Union[Union[dict, "ConditionRelation"], List[Union[dict, "ConditionRelation"]]]] = empty_list()
    genetic_sex: Optional[Union[str, "GeneticSexEnum"]] = None
    private_note: Optional[str] = None
    disease_annotation_note: Optional[str] = None
    disease_annotation_summary: Optional[str] = None
    disease_genetic_modifier: Optional[Union[str, BiologicalEntityCurie]] = None
    disease_genetic_modifier_relation: Optional[Union[str, "GeneticModifierRelationEnum"]] = None
    table_key: Optional[int] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.evidence_codes):
            self.MissingRequiredField("evidence_codes")
        if not isinstance(self.evidence_codes, list):
            self.evidence_codes = [self.evidence_codes] if self.evidence_codes is not None else []
        self.evidence_codes = [v if isinstance(v, ECOTermCurie) else ECOTermCurie(v) for v in self.evidence_codes]

        if self._is_empty(self.reference):
            self.MissingRequiredField("reference")
        if not isinstance(self.reference, ReferenceCurie):
            self.reference = ReferenceCurie(self.reference)

        if self._is_empty(self.data_provider):
            self.MissingRequiredField("data_provider")
        if not isinstance(self.data_provider, list):
            self.data_provider = [self.data_provider] if self.data_provider is not None else []
        self.data_provider = [v if isinstance(v, str) else str(v) for v in self.data_provider]

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, BiologicalEntityCurie):
            self.subject = BiologicalEntityCurie(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, DOTermCurie):
            self.object = DOTermCurie(self.object)

        if self._is_empty(self.created_by):
            self.MissingRequiredField("created_by")
        if not isinstance(self.created_by, PersonPersonId):
            self.created_by = PersonPersonId(self.created_by)

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, PersonPersonId):
            self.modified_by = PersonPersonId(self.modified_by)

        if self.unique_id is not None and not isinstance(self.unique_id, str):
            self.unique_id = str(self.unique_id)

        if self.mod_id is not None and not isinstance(self.mod_id, str):
            self.mod_id = str(self.mod_id)

        if self.negated is not None and not isinstance(self.negated, Bool):
            self.negated = Bool(self.negated)

        if self.annotation_type is not None and not isinstance(self.annotation_type, AnnotationTypeEnum):
            self.annotation_type = AnnotationTypeEnum(self.annotation_type)

        if self.with is not None and not isinstance(self.with, GeneCurie):
            self.with = GeneCurie(self.with)

        if self.disease_qualifiers is not None and not isinstance(self.disease_qualifiers, DiseaseAnnotationQualifierEnum):
            self.disease_qualifiers = DiseaseAnnotationQualifierEnum(self.disease_qualifiers)

        if not isinstance(self.condition_relations, list):
            self.condition_relations = [self.condition_relations] if self.condition_relations is not None else []
        self.condition_relations = [v if isinstance(v, ConditionRelation) else ConditionRelation(**as_dict(v)) for v in self.condition_relations]

        if self.genetic_sex is not None and not isinstance(self.genetic_sex, GeneticSexEnum):
            self.genetic_sex = GeneticSexEnum(self.genetic_sex)

        if self.private_note is not None and not isinstance(self.private_note, str):
            self.private_note = str(self.private_note)

        if self.disease_annotation_note is not None and not isinstance(self.disease_annotation_note, str):
            self.disease_annotation_note = str(self.disease_annotation_note)

        if self.disease_annotation_summary is not None and not isinstance(self.disease_annotation_summary, str):
            self.disease_annotation_summary = str(self.disease_annotation_summary)

        if self.disease_genetic_modifier is not None and not isinstance(self.disease_genetic_modifier, BiologicalEntityCurie):
            self.disease_genetic_modifier = BiologicalEntityCurie(self.disease_genetic_modifier)

        if self.disease_genetic_modifier_relation is not None and not isinstance(self.disease_genetic_modifier_relation, GeneticModifierRelationEnum):
            self.disease_genetic_modifier_relation = GeneticModifierRelationEnum(self.disease_genetic_modifier_relation)

        if self.table_key is not None and not isinstance(self.table_key, int):
            self.table_key = int(self.table_key)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

        super().__post_init__(**kwargs)


@dataclass
class GeneDiseaseAnnotation(DiseaseAnnotation):
    """
    An annotation asserting an association between a gene and a disease supported by evidence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GeneDiseaseAnnotation
    class_class_curie: ClassVar[str] = "alliance:GeneDiseaseAnnotation"
    class_name: ClassVar[str] = "GeneDiseaseAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GeneDiseaseAnnotation

    evidence_codes: Union[Union[str, ECOTermCurie], List[Union[str, ECOTermCurie]]] = None
    reference: Union[str, ReferenceCurie] = None
    data_provider: Union[str, List[str]] = None
    object: Union[str, DOTermCurie] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    subject: Union[str, GeneCurie] = None
    predicate: Union[str, "GeneDiseaseRelationEnum"] = None
    sgd_strain_background: Optional[Union[str, AffectedGenomicModelCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GeneCurie):
            self.subject = GeneCurie(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, GeneDiseaseRelationEnum):
            self.predicate = GeneDiseaseRelationEnum(self.predicate)

        if self.sgd_strain_background is not None and not isinstance(self.sgd_strain_background, AffectedGenomicModelCurie):
            self.sgd_strain_background = AffectedGenomicModelCurie(self.sgd_strain_background)

        super().__post_init__(**kwargs)


@dataclass
class AlleleDiseaseAnnotation(DiseaseAnnotation):
    """
    An annotation asserting an association between an allele and a disease supported by evidence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleDiseaseAnnotation
    class_class_curie: ClassVar[str] = "alliance:AlleleDiseaseAnnotation"
    class_name: ClassVar[str] = "AlleleDiseaseAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleDiseaseAnnotation

    evidence_codes: Union[Union[str, ECOTermCurie], List[Union[str, ECOTermCurie]]] = None
    reference: Union[str, ReferenceCurie] = None
    data_provider: Union[str, List[str]] = None
    object: Union[str, DOTermCurie] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    subject: Union[str, AlleleCurie] = None
    predicate: Union[str, "AlleleDiseaseRelationEnum"] = None
    inferred_gene: Optional[Union[str, GeneCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, AlleleCurie):
            self.subject = AlleleCurie(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, AlleleDiseaseRelationEnum):
            self.predicate = AlleleDiseaseRelationEnum(self.predicate)

        if self.inferred_gene is not None and not isinstance(self.inferred_gene, GeneCurie):
            self.inferred_gene = GeneCurie(self.inferred_gene)

        super().__post_init__(**kwargs)


@dataclass
class AGMDiseaseAnnotation(DiseaseAnnotation):
    """
    An annotation asserting an association between an AGM and a disease supported by evidence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AGMDiseaseAnnotation
    class_class_curie: ClassVar[str] = "alliance:AGMDiseaseAnnotation"
    class_name: ClassVar[str] = "AGMDiseaseAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AGMDiseaseAnnotation

    evidence_codes: Union[Union[str, ECOTermCurie], List[Union[str, ECOTermCurie]]] = None
    reference: Union[str, ReferenceCurie] = None
    data_provider: Union[str, List[str]] = None
    object: Union[str, DOTermCurie] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    subject: Union[str, AffectedGenomicModelCurie] = None
    predicate: Union[str, "AgmDiseaseRelationEnum"] = None
    inferred_allele: Optional[Union[str, AlleleCurie]] = None
    inferred_gene: Optional[Union[str, GeneCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, AffectedGenomicModelCurie):
            self.subject = AffectedGenomicModelCurie(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, AgmDiseaseRelationEnum):
            self.predicate = AgmDiseaseRelationEnum(self.predicate)

        if self.inferred_allele is not None and not isinstance(self.inferred_allele, AlleleCurie):
            self.inferred_allele = AlleleCurie(self.inferred_allele)

        if self.inferred_gene is not None and not isinstance(self.inferred_gene, GeneCurie):
            self.inferred_gene = GeneCurie(self.inferred_gene)

        super().__post_init__(**kwargs)


@dataclass
class ExperimentalCondition(YAMLRoot):
    """
    The environmental context in which an experiment is carried out. This may (e.g. drug treatment) or may not (e.g.
    standard conditions) directly influence the outcome of the experiment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ExperimentalCondition
    class_class_curie: ClassVar[str] = "alliance:ExperimentalCondition"
    class_name: ClassVar[str] = "ExperimentalCondition"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ExperimentalCondition

    condition_class: Union[str, ZECOTermCurie] = None
    condition_statement: str = None
    unique_id: Optional[str] = None
    condition_id: Optional[Union[str, ExperimentalConditionOntologyTermCurie]] = None
    condition_quantity: Optional[str] = None
    condition_anatomy: Optional[Union[str, AnatomicalTermCurie]] = None
    condition_gene_ontology: Optional[Union[str, GOTermCurie]] = None
    condition_taxon: Optional[Union[str, OntologyTermCurie]] = None
    condition_chemical: Optional[Union[str, OntologyTermCurie]] = None
    paper_handles: Optional[Union[Union[dict, "PaperHandle"], List[Union[dict, "PaperHandle"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.condition_class):
            self.MissingRequiredField("condition_class")
        if not isinstance(self.condition_class, ZECOTermCurie):
            self.condition_class = ZECOTermCurie(self.condition_class)

        if self._is_empty(self.condition_statement):
            self.MissingRequiredField("condition_statement")
        if not isinstance(self.condition_statement, str):
            self.condition_statement = str(self.condition_statement)

        if self.unique_id is not None and not isinstance(self.unique_id, str):
            self.unique_id = str(self.unique_id)

        if self.condition_id is not None and not isinstance(self.condition_id, ExperimentalConditionOntologyTermCurie):
            self.condition_id = ExperimentalConditionOntologyTermCurie(self.condition_id)

        if self.condition_quantity is not None and not isinstance(self.condition_quantity, str):
            self.condition_quantity = str(self.condition_quantity)

        if self.condition_anatomy is not None and not isinstance(self.condition_anatomy, AnatomicalTermCurie):
            self.condition_anatomy = AnatomicalTermCurie(self.condition_anatomy)

        if self.condition_gene_ontology is not None and not isinstance(self.condition_gene_ontology, GOTermCurie):
            self.condition_gene_ontology = GOTermCurie(self.condition_gene_ontology)

        if self.condition_taxon is not None and not isinstance(self.condition_taxon, OntologyTermCurie):
            self.condition_taxon = OntologyTermCurie(self.condition_taxon)

        if self.condition_chemical is not None and not isinstance(self.condition_chemical, OntologyTermCurie):
            self.condition_chemical = OntologyTermCurie(self.condition_chemical)

        self._normalize_inlined_as_dict(slot_name="paper_handles", slot_type=PaperHandle, key_name="reference", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class ConditionRelation(YAMLRoot):
    """
    A pairing of an experimental condition relation (i.e. has_condition) with a list of 1 or more
    ExperimentalCondition objects. Annotation objects can connect directly to a set of 0 or more of these
    ConditionRelation objects via a 'condition_relations' slot to express the experimental conditions relevant to the
    annotation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ConditionRelation
    class_class_curie: ClassVar[str] = "alliance:ConditionRelation"
    class_name: ClassVar[str] = "ConditionRelation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ConditionRelation

    condition_relation_type: Union[str, "ConditionRelationEnum"] = None
    unique_id: Optional[str] = None
    conditions: Optional[Union[Union[dict, ExperimentalCondition], List[Union[dict, ExperimentalCondition]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.condition_relation_type):
            self.MissingRequiredField("condition_relation_type")
        if not isinstance(self.condition_relation_type, ConditionRelationEnum):
            self.condition_relation_type = ConditionRelationEnum(self.condition_relation_type)

        if self.unique_id is not None and not isinstance(self.unique_id, str):
            self.unique_id = str(self.unique_id)

        if not isinstance(self.conditions, list):
            self.conditions = [self.conditions] if self.conditions is not None else []
        self.conditions = [v if isinstance(v, ExperimentalCondition) else ExperimentalCondition(**as_dict(v)) for v in self.conditions]

        super().__post_init__(**kwargs)


@dataclass
class Molecule(YAMLRoot):
    """
    Molecules as described by WormBase
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Molecule
    class_class_curie: ClassVar[str] = "alliance:Molecule"
    class_name: ClassVar[str] = "Molecule"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Molecule

    curie: Union[str, MoleculeCurie] = None
    name: str = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    inchi: Optional[str] = None
    inchi_key: Optional[str] = None
    iupac: Optional[str] = None
    formula: Optional[str] = None
    smiles: Optional[str] = None
    synonyms: Optional[Union[Union[dict, Synonym], List[Union[dict, Synonym]]]] = empty_list()
    cross_references: Optional[Union[Dict[Union[str, CrossReferenceCurie], Union[dict, CrossReference]], List[Union[dict, CrossReference]]]] = empty_dict()
    table_key: Optional[int] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, MoleculeCurie):
            self.curie = MoleculeCurie(self.curie)

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

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, Synonym) else Synonym(**as_dict(v)) for v in self.synonyms]

        self._normalize_inlined_as_list(slot_name="cross_references", slot_type=CrossReference, key_name="curie", keyed=True)

        if self.table_key is not None and not isinstance(self.table_key, int):
            self.table_key = int(self.table_key)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

        super().__post_init__(**kwargs)


@dataclass
class PaperHandle(YAMLRoot):
    """
    A pairing of a reference and a free text string that allows an object to have a reference-specific alias (or
    handle). For example, used for experimental conditions from ZFIN to label (in a reference-specific manner)
    individual experimental conditions when curating a particular reference.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.PaperHandle
    class_class_curie: ClassVar[str] = "alliance:PaperHandle"
    class_name: ClassVar[str] = "PaperHandle"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.PaperHandle

    reference: Union[str, ReferenceCurie] = None
    handle: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.reference):
            self.MissingRequiredField("reference")
        if not isinstance(self.reference, ReferenceCurie):
            self.reference = ReferenceCurie(self.reference)

        if self._is_empty(self.handle):
            self.MissingRequiredField("handle")
        if not isinstance(self.handle, str):
            self.handle = str(self.handle)

        super().__post_init__(**kwargs)


@dataclass
class VocabularyTerm(YAMLRoot):
    """
    A concept or class in a simple vocabulary.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/controlledVocabulary.yaml/VocabularyTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "VocabularyTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.VocabularyTerm

    name: str = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    abbreviation: Optional[str] = None
    definition: Optional[str] = None
    is_obsolete: Optional[Union[bool, Bool]] = None
    text_synonyms: Optional[Union[str, List[str]]] = empty_list()
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

        if self.abbreviation is not None and not isinstance(self.abbreviation, str):
            self.abbreviation = str(self.abbreviation)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.is_obsolete is not None and not isinstance(self.is_obsolete, Bool):
            self.is_obsolete = Bool(self.is_obsolete)

        if not isinstance(self.text_synonyms, list):
            self.text_synonyms = [self.text_synonyms] if self.text_synonyms is not None else []
        self.text_synonyms = [v if isinstance(v, str) else str(v) for v in self.text_synonyms]

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Vocabulary

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


@dataclass
class Ingest(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/ingest/Ingest")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Ingest"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Ingest

    allele_ingest_set: Optional[Union[Union[str, AlleleCurie], List[Union[str, AlleleCurie]]]] = empty_list()
    disease_annotation_ingest_set: Optional[Union[Union[dict, DiseaseAnnotation], List[Union[dict, DiseaseAnnotation]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.allele_ingest_set, list):
            self.allele_ingest_set = [self.allele_ingest_set] if self.allele_ingest_set is not None else []
        self.allele_ingest_set = [v if isinstance(v, AlleleCurie) else AlleleCurie(v) for v in self.allele_ingest_set]

        self._normalize_inlined_as_dict(slot_name="disease_annotation_ingest_set", slot_type=DiseaseAnnotation, key_name="evidence_codes", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class Figure(YAMLRoot):
    """
    An entity representing a figure or table in a publication.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/image.yaml/Figure")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Figure"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Figure

    curie: Union[str, FigureCurie] = None
    has_reference: Union[str, ReferenceCurie] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    label: Optional[str] = None
    caption: Optional[str] = None
    secondary_identifiers: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    table_key: Optional[int] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, FigureCurie):
            self.curie = FigureCurie(self.curie)

        if self._is_empty(self.has_reference):
            self.MissingRequiredField("has_reference")
        if not isinstance(self.has_reference, ReferenceCurie):
            self.has_reference = ReferenceCurie(self.has_reference)

        if self._is_empty(self.created_by):
            self.MissingRequiredField("created_by")
        if not isinstance(self.created_by, PersonPersonId):
            self.created_by = PersonPersonId(self.created_by)

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, PersonPersonId):
            self.modified_by = PersonPersonId(self.modified_by)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.caption is not None and not isinstance(self.caption, str):
            self.caption = str(self.caption)

        if not isinstance(self.secondary_identifiers, list):
            self.secondary_identifiers = [self.secondary_identifiers] if self.secondary_identifiers is not None else []
        self.secondary_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.secondary_identifiers]

        if self.table_key is not None and not isinstance(self.table_key, int):
            self.table_key = int(self.table_key)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

        super().__post_init__(**kwargs)


class File(YAMLRoot):
    """
    A dummy object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/image.yaml/File")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "File"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.File


@dataclass
class Image(YAMLRoot):
    """
    The set of files and metadata that constitute an image.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/image.yaml/Image")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Image"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Image

    curie: Union[str, ImageCurie] = None
    has_figure: Union[str, FigureCurie] = None
    width: int = None
    height: int = None
    image_file: Union[dict, File] = None
    image_medium_file: Union[dict, File] = None
    image_thumbnail_file: Union[dict, File] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    cropped_from: Optional[Union[str, ImageCurie]] = None
    image_x_origin: Optional[int] = None
    image_y_origin: Optional[int] = None
    video_still: Optional[Union[bool, Bool]] = None
    secondary_identifiers: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    table_key: Optional[int] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ImageCurie):
            self.curie = ImageCurie(self.curie)

        if self._is_empty(self.has_figure):
            self.MissingRequiredField("has_figure")
        if not isinstance(self.has_figure, FigureCurie):
            self.has_figure = FigureCurie(self.has_figure)

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
            self.image_file = File()

        if self._is_empty(self.image_medium_file):
            self.MissingRequiredField("image_medium_file")
        if not isinstance(self.image_medium_file, File):
            self.image_medium_file = File()

        if self._is_empty(self.image_thumbnail_file):
            self.MissingRequiredField("image_thumbnail_file")
        if not isinstance(self.image_thumbnail_file, File):
            self.image_thumbnail_file = File()

        if self._is_empty(self.created_by):
            self.MissingRequiredField("created_by")
        if not isinstance(self.created_by, PersonPersonId):
            self.created_by = PersonPersonId(self.created_by)

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, PersonPersonId):
            self.modified_by = PersonPersonId(self.modified_by)

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

        if self.table_key is not None and not isinstance(self.table_key, int):
            self.table_key = int(self.table_key)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

        super().__post_init__(**kwargs)


@dataclass
class ImagePane(YAMLRoot):
    """
    Part of an Image that is relevant to some annotation. An annotation may reference many panes of an Image.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/image.yaml/ImagePane")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ImagePane"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ImagePane

    images: Union[str, ImageCurie] = None
    width: int = None
    height: int = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    label: Optional[str] = None
    image_x_origin: Optional[int] = None
    image_y_origin: Optional[int] = None
    table_key: Optional[int] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.images):
            self.MissingRequiredField("images")
        if not isinstance(self.images, ImageCurie):
            self.images = ImageCurie(self.images)

        if self._is_empty(self.width):
            self.MissingRequiredField("width")
        if not isinstance(self.width, int):
            self.width = int(self.width)

        if self._is_empty(self.height):
            self.MissingRequiredField("height")
        if not isinstance(self.height, int):
            self.height = int(self.height)

        if self._is_empty(self.created_by):
            self.MissingRequiredField("created_by")
        if not isinstance(self.created_by, PersonPersonId):
            self.created_by = PersonPersonId(self.created_by)

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, PersonPersonId):
            self.modified_by = PersonPersonId(self.modified_by)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.image_x_origin is not None and not isinstance(self.image_x_origin, int):
            self.image_x_origin = int(self.image_x_origin)

        if self.image_y_origin is not None and not isinstance(self.image_y_origin, int):
            self.image_y_origin = int(self.image_y_origin)

        if self.table_key is not None and not isinstance(self.table_key, int):
            self.table_key = int(self.table_key)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

        super().__post_init__(**kwargs)


# Enumerations
class TagSet(EnumDefinitionImpl):

    image = PermissibleValue(text="image")
    test = PermissibleValue(text="test")

    _defn = EnumDefinition(
        name="TagSet",
    )

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

class ComponentRelationsEnum(EnumDefinitionImpl):

    expresses = PermissibleValue(text="expresses")
    is_regulated_by = PermissibleValue(text="is_regulated_by")
    targets = PermissibleValue(text="targets")

    _defn = EnumDefinition(
        name="ComponentRelationsEnum",
    )

class DatabaseStatuses(EnumDefinitionImpl):

    live = PermissibleValue(text="live")
    dead = PermissibleValue(text="dead")
    suppressed = PermissibleValue(text="suppressed")
    history = PermissibleValue(text="history")
    private = PermissibleValue(text="private")
    approved = PermissibleValue(text="approved")

    _defn = EnumDefinition(
        name="DatabaseStatuses",
    )

class ReferenceAssociationTypes(EnumDefinitionImpl):

    molecular = PermissibleValue(text="molecular")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="ReferenceAssociationTypes",
    )

class NoteAssociationTypes(EnumDefinitionImpl):

    molecular = PermissibleValue(text="molecular")
    origin = PermissibleValue(text="origin")
    cytology = PermissibleValue(text="cytology")
    private = PermissibleValue(text="private")
    curator_comments = PermissibleValue(text="curator_comments")

    _defn = EnumDefinition(
        name="NoteAssociationTypes",
    )

class ModesOfInheritence(EnumDefinitionImpl):

    dominant = PermissibleValue(text="dominant")
    recessive = PermissibleValue(text="recessive")
    semi_dominant = PermissibleValue(text="semi_dominant")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="ModesOfInheritence",
    )

class SubtypeValues(EnumDefinitionImpl):

    strain = PermissibleValue(text="strain")
    genotype = PermissibleValue(text="genotype")

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

class AntibodyClonalitySet(EnumDefinitionImpl):

    monoclonal = PermissibleValue(text="monoclonal")
    polyclonal = PermissibleValue(text="polyclonal")
    unspecified = PermissibleValue(text="unspecified")

    _defn = EnumDefinition(
        name="AntibodyClonalitySet",
    )

class HeavyChainIsotypeSet(EnumDefinitionImpl):

    IgA = PermissibleValue(text="IgA")
    IgA1 = PermissibleValue(text="IgA1")
    IgA2 = PermissibleValue(text="IgA2")
    IgD = PermissibleValue(text="IgD")
    IgE = PermissibleValue(text="IgE")
    IgG = PermissibleValue(text="IgG")
    IgG1 = PermissibleValue(text="IgG1")
    IgG2 = PermissibleValue(text="IgG2")
    IgG2a = PermissibleValue(text="IgG2a")
    IgG2b = PermissibleValue(text="IgG2b")
    IgG2c = PermissibleValue(text="IgG2c")
    IgG3 = PermissibleValue(text="IgG3")
    IgG4 = PermissibleValue(text="IgG4")
    IgM = PermissibleValue(text="IgM")
    IgN = PermissibleValue(text="IgN")
    IgR = PermissibleValue(text="IgR")
    IgW = PermissibleValue(text="IgW")
    IgX = PermissibleValue(text="IgX")
    IgY = PermissibleValue(text="IgY")

    _defn = EnumDefinition(
        name="HeavyChainIsotypeSet",
    )

class LightChainIsotypeSet(EnumDefinitionImpl):

    k = PermissibleValue(text="k")
    l = PermissibleValue(text="l")
    l1 = PermissibleValue(text="l1")
    l2 = PermissibleValue(text="l2")
    l3 = PermissibleValue(text="l3")
    l4 = PermissibleValue(text="l4")
    r = PermissibleValue(text="r")
    s = PermissibleValue(text="s")
    i = PermissibleValue(text="i")
    i1 = PermissibleValue(text="i1")
    i2 = PermissibleValue(text="i2")
    i3 = PermissibleValue(text="i3")
    i4 = PermissibleValue(text="i4")

    _defn = EnumDefinition(
        name="LightChainIsotypeSet",
    )

class AntibodyNoteTypeSet(EnumDefinitionImpl):

    antibody_description = PermissibleValue(text="antibody_description",
                                                               description="A high level summary of the antibody intended for prominent display e.g., Antibodies against SEIP-1 were raised by injection of the peptide 261KKEEPGLLDLRKRK, corresponding to the C-terminus of SEIP-1, into rabbits.")
    antigen_description = PermissibleValue(text="antigen_description",
                                                             description="A description about the antigen used to generate the antibody e.g., N-terminal peptide (SQFRPEKKEKSTCSIC) full length ceKDM1A (amino acids 1-897).")
    remark = PermissibleValue(text="remark",
                                   description="Information pertaining to the antibody that is not covered by other fields e.g., Possible pseudonym 7G1, High level of background, Works well for immunoprecipitation.")
    private = PermissibleValue(text="private",
                                     description="Information intended for internal use, generally regarding aspects of curation.")

    _defn = EnumDefinition(
        name="AntibodyNoteTypeSet",
    )

class AggregationDatabaseEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AggregationDatabaseEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "mi:0670",
                PermissibleValue(text="mi:0670") )

class InteractorTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="InteractorTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "mi:0250",
                PermissibleValue(text="mi:0250") )
        setattr(cls, "mi:0318",
                PermissibleValue(text="mi:0318") )
        setattr(cls, "mi:0319",
                PermissibleValue(text="mi:0319") )
        setattr(cls, "mi:0320",
                PermissibleValue(text="mi:0320") )
        setattr(cls, "mi:0324",
                PermissibleValue(text="mi:0324") )
        setattr(cls, "mi:0326",
                PermissibleValue(text="mi:0326") )
        setattr(cls, "mi:0327",
                PermissibleValue(text="mi:0327") )
        setattr(cls, "mi:0681",
                PermissibleValue(text="mi:0681") )
        setattr(cls, "mi:2190",
                PermissibleValue(text="mi:2190") )

class InteractorARoleEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="InteractorARoleEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "mi:2352",
                PermissibleValue(text="mi:2352") )
        setattr(cls, "mi:0496",
                PermissibleValue(text="mi:0496") )
        setattr(cls, "mi:0584",
                PermissibleValue(text="mi:0584") )
        setattr(cls, "mi:2334",
                PermissibleValue(text="mi:2334") )
        setattr(cls, "mi:0497",
                PermissibleValue(text="mi:0497") )
        setattr(cls, "mi:0684",
                PermissibleValue(text="mi:0684") )
        setattr(cls, "mi:0582",
                PermissibleValue(text="mi:0582") )
        setattr(cls, "mi:2354",
                PermissibleValue(text="mi:2354") )
        setattr(cls, "mi:0583",
                PermissibleValue(text="mi:0583") )
        setattr(cls, "mi:0498",
                PermissibleValue(text="mi:0498") )
        setattr(cls, "mi:0499",
                PermissibleValue(text="mi:0499") )
        setattr(cls, "mi:2335",
                PermissibleValue(text="mi:2335") )
        setattr(cls, "mi:0898",
                PermissibleValue(text="mi:0898") )
        setattr(cls, "mi:0865",
                PermissibleValue(text="mi:0865") )
        setattr(cls, "mi:0503",
                PermissibleValue(text="mi:0503") )

class InteractorBRoleEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="InteractorBRoleEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "mi:2351",
                PermissibleValue(text="mi:2351") )
        setattr(cls, "mi:0581",
                PermissibleValue(text="mi:0581") )
        setattr(cls, "mi:0496",
                PermissibleValue(text="mi:0496") )
        setattr(cls, "mi:0584",
                PermissibleValue(text="mi:0584") )
        setattr(cls, "mi:2334",
                PermissibleValue(text="mi:2334") )
        setattr(cls, "mi:0497",
                PermissibleValue(text="mi:0497") )
        setattr(cls, "mi:0684",
                PermissibleValue(text="mi:0684") )
        setattr(cls, "mi:2353",
                PermissibleValue(text="mi:2353") )
        setattr(cls, "mi:0583",
                PermissibleValue(text="mi:0583") )
        setattr(cls, "mi:0498",
                PermissibleValue(text="mi:0498") )
        setattr(cls, "mi:0499",
                PermissibleValue(text="mi:0499") )
        setattr(cls, "mi:2335",
                PermissibleValue(text="mi:2335") )
        setattr(cls, "mi:0898",
                PermissibleValue(text="mi:0898") )
        setattr(cls, "mi:0865",
                PermissibleValue(text="mi:0865") )
        setattr(cls, "mi:0503",
                PermissibleValue(text="mi:0503") )

class InteractionSourceEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="InteractionSourceEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "mi:1263",
                PermissibleValue(text="mi:1263") )
        setattr(cls, "mi:0471",
                PermissibleValue(text="mi:0471") )
        setattr(cls, "mi:1262",
                PermissibleValue(text="mi:1262") )
        setattr(cls, "mi:0463",
                PermissibleValue(text="mi:0463") )
        setattr(cls, "mi:0486",
                PermissibleValue(text="mi:0486") )
        setattr(cls, "mi:1222",
                PermissibleValue(text="mi:1222") )
        setattr(cls, "mi:1332",
                PermissibleValue(text="mi:1332") )
        setattr(cls, "mi:1264",
                PermissibleValue(text="mi:1264") )
        setattr(cls, "mi:0903",
                PermissibleValue(text="mi:0903") )
        setattr(cls, "mi:0917",
                PermissibleValue(text="mi:0917") )
        setattr(cls, "mi:0478",
                PermissibleValue(text="mi:0478") )
        setattr(cls, "mi:0974",
                PermissibleValue(text="mi:0974") )
        setattr(cls, "mi:0487",
                PermissibleValue(text="mi:0487") )
        setattr(cls, "mi:0465",
                PermissibleValue(text="mi:0465") )
        setattr(cls, "mi:1335",
                PermissibleValue(text="mi:1335") )
        setattr(cls, "mi:0469",
                PermissibleValue(text="mi:0469") )

class DetectionMethodsEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="DetectionMethodsEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "mi:0084",
                PermissibleValue(text="mi:0084") )
        setattr(cls, "mi:0364",
                PermissibleValue(text="mi:0364") )
        setattr(cls, "mi:0089",
                PermissibleValue(text="mi:0089") )
        setattr(cls, "mi:0001",
                PermissibleValue(text="mi:0001") )
        setattr(cls, "mi:0363",
                PermissibleValue(text="mi:0363") )
        setattr(cls, "mi:0880",
                PermissibleValue(text="mi:0880") )
        setattr(cls, "mi:0081",
                PermissibleValue(text="mi:0081") )
        setattr(cls, "mi:0115",
                PermissibleValue(text="mi:0115") )
        setattr(cls, "mi:0512",
                PermissibleValue(text="mi:0512") )
        setattr(cls, "mi:1204",
                PermissibleValue(text="mi:1204") )
        setattr(cls, "mi:1203",
                PermissibleValue(text="mi:1203") )
        setattr(cls, "mi:0872",
                PermissibleValue(text="mi:0872") )
        setattr(cls, "mi:0114",
                PermissibleValue(text="mi:0114") )
        setattr(cls, "mi:0510",
                PermissibleValue(text="mi:0510") )
        setattr(cls, "mi:0515",
                PermissibleValue(text="mi:0515") )
        setattr(cls, "mi:0516",
                PermissibleValue(text="mi:0516") )
        setattr(cls, "mi:0998",
                PermissibleValue(text="mi:0998") )
        setattr(cls, "mi:0073",
                PermissibleValue(text="mi:0073") )
        setattr(cls, "mi:0232",
                PermissibleValue(text="mi:0232") )
        setattr(cls, "mi:0111",
                PermissibleValue(text="mi:0111") )
        setattr(cls, "mi:0870",
                PermissibleValue(text="mi:0870") )
        setattr(cls, "mi:0991",
                PermissibleValue(text="mi:0991") )
        setattr(cls, "mi:0112",
                PermissibleValue(text="mi:0112") )
        setattr(cls, "mi:0077",
                PermissibleValue(text="mi:0077") )
        setattr(cls, "mi:0990",
                PermissibleValue(text="mi:0990") )
        setattr(cls, "mi:0231",
                PermissibleValue(text="mi:0231") )
        setattr(cls, "mi:0071",
                PermissibleValue(text="mi:0071") )
        setattr(cls, "mi:0905",
                PermissibleValue(text="mi:0905") )
        setattr(cls, "mi:0588",
                PermissibleValue(text="mi:0588") )
        setattr(cls, "mi:0104",
                PermissibleValue(text="mi:0104") )
        setattr(cls, "mi:0225",
                PermissibleValue(text="mi:0225") )
        setattr(cls, "mi:0984",
                PermissibleValue(text="mi:0984") )
        setattr(cls, "mi:0226",
                PermissibleValue(text="mi:0226") )
        setattr(cls, "mi:1314",
                PermissibleValue(text="mi:1314") )
        setattr(cls, "mi:0069",
                PermissibleValue(text="mi:0069") )
        setattr(cls, "mi:0982",
                PermissibleValue(text="mi:0982") )
        setattr(cls, "mi:1313",
                PermissibleValue(text="mi:1313") )
        setattr(cls, "mi:1038",
                PermissibleValue(text="mi:1038") )
        setattr(cls, "mi:1037",
                PermissibleValue(text="mi:1037") )
        setattr(cls, "mi:1312",
                PermissibleValue(text="mi:1312") )
        setattr(cls, "mi:0108",
                PermissibleValue(text="mi:0108") )
        setattr(cls, "mi:0900",
                PermissibleValue(text="mi:0900") )
        setattr(cls, "mi:0227",
                PermissibleValue(text="mi:0227") )
        setattr(cls, "mi:0107",
                PermissibleValue(text="mi:0107") )
        setattr(cls, "mi:0067",
                PermissibleValue(text="mi:0067") )
        setattr(cls, "mi:1311",
                PermissibleValue(text="mi:1311") )
        setattr(cls, "mi:0101",
                PermissibleValue(text="mi:0101") )
        setattr(cls, "mi:0065",
                PermissibleValue(text="mi:0065") )
        setattr(cls, "mi:0066",
                PermissibleValue(text="mi:0066") )
        setattr(cls, "mi:0858",
                PermissibleValue(text="mi:0858") )
        setattr(cls, "mi:0979",
                PermissibleValue(text="mi:0979") )
        setattr(cls, "mi:0859",
                PermissibleValue(text="mi:0859") )
        setattr(cls, "mi:1309",
                PermissibleValue(text="mi:1309") )
        setattr(cls, "mi:1147",
                PermissibleValue(text="mi:1147") )
        setattr(cls, "mi:0052",
                PermissibleValue(text="mi:0052") )
        setattr(cls, "mi:0053",
                PermissibleValue(text="mi:0053") )
        setattr(cls, "mi:0051",
                PermissibleValue(text="mi:0051") )
        setattr(cls, "mi:1024",
                PermissibleValue(text="mi:1024") )
        setattr(cls, "mi:0695",
                PermissibleValue(text="mi:0695") )
        setattr(cls, "mi:0054",
                PermissibleValue(text="mi:0054") )
        setattr(cls, "mi:0055",
                PermissibleValue(text="mi:0055") )
        setattr(cls, "mi:1022",
                PermissibleValue(text="mi:1022") )
        setattr(cls, "mi:2193",
                PermissibleValue(text="mi:2193") )
        setattr(cls, "mi:2192",
                PermissibleValue(text="mi:2192") )
        setattr(cls, "mi:2191",
                PermissibleValue(text="mi:2191") )
        setattr(cls, "mi:0728",
                PermissibleValue(text="mi:0728") )
        setattr(cls, "mi:0729",
                PermissibleValue(text="mi:0729") )
        setattr(cls, "mi:0605",
                PermissibleValue(text="mi:0605") )
        setattr(cls, "mi:0968",
                PermissibleValue(text="mi:0968") )
        setattr(cls, "mi:0606",
                PermissibleValue(text="mi:0606") )
        setattr(cls, "mi:0969",
                PermissibleValue(text="mi:0969") )
        setattr(cls, "mi:0727",
                PermissibleValue(text="mi:0727") )
        setattr(cls, "mi:0049",
                PermissibleValue(text="mi:0049") )
        setattr(cls, "mi:0841",
                PermissibleValue(text="mi:0841") )
        setattr(cls, "mi:0047",
                PermissibleValue(text="mi:0047") )
        setattr(cls, "mi:1016",
                PermissibleValue(text="mi:1016") )
        setattr(cls, "mi:1137",
                PermissibleValue(text="mi:1137") )
        setattr(cls, "mi:0686",
                PermissibleValue(text="mi:0686") )
        setattr(cls, "mi:0048",
                PermissibleValue(text="mi:0048") )
        setattr(cls, "mi:0964",
                PermissibleValue(text="mi:0964") )
        setattr(cls, "mi:1019",
                PermissibleValue(text="mi:1019") )
        setattr(cls, "mi:0042",
                PermissibleValue(text="mi:0042") )
        setattr(cls, "mi:2340",
                PermissibleValue(text="mi:2340") )
        setattr(cls, "mi:0040",
                PermissibleValue(text="mi:0040") )
        setattr(cls, "mi:0045",
                PermissibleValue(text="mi:0045") )
        setattr(cls, "mi:0046",
                PermissibleValue(text="mi:0046") )
        setattr(cls, "mi:2189",
                PermissibleValue(text="mi:2189") )
        setattr(cls, "mi:0440",
                PermissibleValue(text="mi:0440") )
        setattr(cls, "mi:0676",
                PermissibleValue(text="mi:0676") )
        setattr(cls, "mi:0038",
                PermissibleValue(text="mi:0038") )
        setattr(cls, "mi:0434",
                PermissibleValue(text="mi:0434") )
        setattr(cls, "mi:1007",
                PermissibleValue(text="mi:1007") )
        setattr(cls, "mi:0435",
                PermissibleValue(text="mi:0435") )
        setattr(cls, "mi:0432",
                PermissibleValue(text="mi:0432") )
        setattr(cls, "mi:1247",
                PermissibleValue(text="mi:1247") )
        setattr(cls, "mi:0399",
                PermissibleValue(text="mi:0399") )
        setattr(cls, "mi:1005",
                PermissibleValue(text="mi:1005") )
        setattr(cls, "mi:1246",
                PermissibleValue(text="mi:1246") )
        setattr(cls, "mi:0438",
                PermissibleValue(text="mi:0438") )
        setattr(cls, "mi:0953",
                PermissibleValue(text="mi:0953") )
        setattr(cls, "mi:0678",
                PermissibleValue(text="mi:0678") )
        setattr(cls, "mi:0437",
                PermissibleValue(text="mi:0437") )
        setattr(cls, "mi:1008",
                PermissibleValue(text="mi:1008") )
        setattr(cls, "mi:2339",
                PermissibleValue(text="mi:2339") )
        setattr(cls, "mi:0030",
                PermissibleValue(text="mi:0030") )
        setattr(cls, "mi:0031",
                PermissibleValue(text="mi:0031") )
        setattr(cls, "mi:0276",
                PermissibleValue(text="mi:0276") )
        setattr(cls, "mi:0397",
                PermissibleValue(text="mi:0397") )
        setattr(cls, "mi:0430",
                PermissibleValue(text="mi:0430") )
        setattr(cls, "mi:2213",
                PermissibleValue(text="mi:2213") )
        setattr(cls, "mi:0398",
                PermissibleValue(text="mi:0398") )
        setattr(cls, "mi:1088",
                PermissibleValue(text="mi:1088") )
        setattr(cls, "mi:1000",
                PermissibleValue(text="mi:1000") )
        setattr(cls, "mi:0949",
                PermissibleValue(text="mi:0949") )
        setattr(cls, "mi:0825",
                PermissibleValue(text="mi:0825") )
        setattr(cls, "mi:0946",
                PermissibleValue(text="mi:0946") )
        setattr(cls, "mi:0826",
                PermissibleValue(text="mi:0826") )
        setattr(cls, "mi:0947",
                PermissibleValue(text="mi:0947") )
        setattr(cls, "mi:0027",
                PermissibleValue(text="mi:0027") )
        setattr(cls, "mi:0423",
                PermissibleValue(text="mi:0423") )
        setattr(cls, "mi:0424",
                PermissibleValue(text="mi:0424") )
        setattr(cls, "mi:0028",
                PermissibleValue(text="mi:0028") )
        setattr(cls, "mi:0663",
                PermissibleValue(text="mi:0663") )
        setattr(cls, "mi:1235",
                PermissibleValue(text="mi:1235") )
        setattr(cls, "mi:1356",
                PermissibleValue(text="mi:1356") )
        setattr(cls, "mi:0944",
                PermissibleValue(text="mi:0944") )
        setattr(cls, "mi:0428",
                PermissibleValue(text="mi:0428") )
        setattr(cls, "mi:0824",
                PermissibleValue(text="mi:0824") )
        setattr(cls, "mi:0029",
                PermissibleValue(text="mi:0029") )
        setattr(cls, "mi:0425",
                PermissibleValue(text="mi:0425") )
        setattr(cls, "mi:0426",
                PermissibleValue(text="mi:0426") )
        setattr(cls, "mi:0943",
                PermissibleValue(text="mi:0943") )
        setattr(cls, "mi:0020",
                PermissibleValue(text="mi:0020") )
        setattr(cls, "mi:2169",
                PermissibleValue(text="mi:2169") )
        setattr(cls, "mi:0420",
                PermissibleValue(text="mi:0420") )
        setattr(cls, "mi:1232",
                PermissibleValue(text="mi:1232") )
        setattr(cls, "mi:1352",
                PermissibleValue(text="mi:1352") )
        setattr(cls, "mi:0814",
                PermissibleValue(text="mi:0814") )
        setattr(cls, "mi:0419",
                PermissibleValue(text="mi:0419") )
        setattr(cls, "mi:0412",
                PermissibleValue(text="mi:0412") )
        setattr(cls, "mi:0016",
                PermissibleValue(text="mi:0016") )
        setattr(cls, "mi:0413",
                PermissibleValue(text="mi:0413") )
        setattr(cls, "mi:0017",
                PermissibleValue(text="mi:0017") )
        setattr(cls, "mi:0655",
                PermissibleValue(text="mi:0655") )
        setattr(cls, "mi:0410",
                PermissibleValue(text="mi:0410") )
        setattr(cls, "mi:1104",
                PermissibleValue(text="mi:1104") )
        setattr(cls, "mi:0014",
                PermissibleValue(text="mi:0014") )
        setattr(cls, "mi:0894",
                PermissibleValue(text="mi:0894") )
        setattr(cls, "mi:0411",
                PermissibleValue(text="mi:0411") )
        setattr(cls, "mi:1103",
                PermissibleValue(text="mi:1103") )
        setattr(cls, "mi:0416",
                PermissibleValue(text="mi:0416") )
        setattr(cls, "mi:0813",
                PermissibleValue(text="mi:0813") )
        setattr(cls, "mi:0417",
                PermissibleValue(text="mi:0417") )
        setattr(cls, "mi:0018",
                PermissibleValue(text="mi:0018") )
        setattr(cls, "mi:0415",
                PermissibleValue(text="mi:0415") )
        setattr(cls, "mi:0019",
                PermissibleValue(text="mi:0019") )
        setattr(cls, "mi:0657",
                PermissibleValue(text="mi:0657") )
        setattr(cls, "mi:0096",
                PermissibleValue(text="mi:0096") )
        setattr(cls, "mi:0097",
                PermissibleValue(text="mi:0097") )
        setattr(cls, "mi:1183",
                PermissibleValue(text="mi:1183") )
        setattr(cls, "mi:0370",
                PermissibleValue(text="mi:0370") )
        setattr(cls, "mi:0892",
                PermissibleValue(text="mi:0892") )
        setattr(cls, "mi:0012",
                PermissibleValue(text="mi:0012") )
        setattr(cls, "mi:0254",
                PermissibleValue(text="mi:0254") )
        setattr(cls, "mi:0013",
                PermissibleValue(text="mi:0013") )
        setattr(cls, "mi:0010",
                PermissibleValue(text="mi:0010") )
        setattr(cls, "mi:0011",
                PermissibleValue(text="mi:0011") )
        setattr(cls, "mi:0099",
                PermissibleValue(text="mi:0099") )
        setattr(cls, "mi:0090",
                PermissibleValue(text="mi:0090") )
        setattr(cls, "mi:0091",
                PermissibleValue(text="mi:0091") )
        setattr(cls, "mi:0809",
                PermissibleValue(text="mi:0809") )
        setattr(cls, "mi:0807",
                PermissibleValue(text="mi:0807") )
        setattr(cls, "mi:0928",
                PermissibleValue(text="mi:0928") )
        setattr(cls, "mi:0808",
                PermissibleValue(text="mi:0808") )
        setattr(cls, "mi:0401",
                PermissibleValue(text="mi:0401") )
        setattr(cls, "mi:0402",
                PermissibleValue(text="mi:0402") )
        setattr(cls, "mi:0006",
                PermissibleValue(text="mi:0006") )
        setattr(cls, "mi:0369",
                PermissibleValue(text="mi:0369") )
        setattr(cls, "mi:0004",
                PermissibleValue(text="mi:0004") )
        setattr(cls, "mi:0400",
                PermissibleValue(text="mi:0400") )
        setattr(cls, "mi:0405",
                PermissibleValue(text="mi:0405") )
        setattr(cls, "mi:0889",
                PermissibleValue(text="mi:0889") )
        setattr(cls, "mi:0406",
                PermissibleValue(text="mi:0406") )
        setattr(cls, "mi:0007",
                PermissibleValue(text="mi:0007") )
        setattr(cls, "mi:0887",
                PermissibleValue(text="mi:0887") )
        setattr(cls, "mi:0920",
                PermissibleValue(text="mi:0920") )
        setattr(cls, "mi:1218",
                PermissibleValue(text="mi:1218") )
        setattr(cls, "mi:0404",
                PermissibleValue(text="mi:0404") )
        setattr(cls, "mi:0008",
                PermissibleValue(text="mi:0008") )
        setattr(cls, "mi:0888",
                PermissibleValue(text="mi:0888") )
        setattr(cls, "mi:0921",
                PermissibleValue(text="mi:0921") )

class InteractionTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="InteractionTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "mi:1294",
                PermissibleValue(text="mi:1294") )
        setattr(cls, "mi:1250",
                PermissibleValue(text="mi:1250") )
        setattr(cls, "mi:1293",
                PermissibleValue(text="mi:1293") )
        setattr(cls, "mi:2388",
                PermissibleValue(text="mi:2388") )
        setattr(cls, "mi:1292",
                PermissibleValue(text="mi:1292") )
        setattr(cls, "mi:2380",
                PermissibleValue(text="mi:2380") )
        setattr(cls, "mi:1291",
                PermissibleValue(text="mi:1291") )
        setattr(cls, "mi:1290",
                PermissibleValue(text="mi:1290") )
        setattr(cls, "mi:0915",
                PermissibleValue(text="mi:0915") )
        setattr(cls, "mi:0914",
                PermissibleValue(text="mi:0914") )
        setattr(cls, "mi:0797",
                PermissibleValue(text="mi:0797") )
        setattr(cls, "mi:1127",
                PermissibleValue(text="mi:1127") )
        setattr(cls, "mi:0795",
                PermissibleValue(text="mi:0795") )
        setattr(cls, "mi:1126",
                PermissibleValue(text="mi:1126") )
        setattr(cls, "mi:2379",
                PermissibleValue(text="mi:2379") )
        setattr(cls, "mi:0559",
                PermissibleValue(text="mi:0559") )
        setattr(cls, "mi:0557",
                PermissibleValue(text="mi:0557") )
        setattr(cls, "mi:2374",
                PermissibleValue(text="mi:2374") )
        setattr(cls, "mi:0195",
                PermissibleValue(text="mi:0195") )
        setattr(cls, "mi:2373",
                PermissibleValue(text="mi:2373") )
        setattr(cls, "mi:1283",
                PermissibleValue(text="mi:1283") )
        setattr(cls, "mi:2372",
                PermissibleValue(text="mi:2372") )
        setattr(cls, "mi:2371",
                PermissibleValue(text="mi:2371") )
        setattr(cls, "mi:0194",
                PermissibleValue(text="mi:0194") )
        setattr(cls, "mi:2378",
                PermissibleValue(text="mi:2378") )
        setattr(cls, "mi:0199",
                PermissibleValue(text="mi:0199") )
        setattr(cls, "mi:0794",
                PermissibleValue(text="mi:0794") )
        setattr(cls, "mi:1288",
                PermissibleValue(text="mi:1288") )
        setattr(cls, "mi:2377",
                PermissibleValue(text="mi:2377") )
        setattr(cls, "mi:0871",
                PermissibleValue(text="mi:0871") )
        setattr(cls, "mi:1287",
                PermissibleValue(text="mi:1287") )
        setattr(cls, "mi:2376",
                PermissibleValue(text="mi:2376") )
        setattr(cls, "mi:0197",
                PermissibleValue(text="mi:0197") )
        setattr(cls, "mi:2375",
                PermissibleValue(text="mi:2375") )
        setattr(cls, "mi:2370",
                PermissibleValue(text="mi:2370") )
        setattr(cls, "mi:1280",
                PermissibleValue(text="mi:1280") )
        setattr(cls, "mi:0192",
                PermissibleValue(text="mi:0192") )
        setattr(cls, "mi:1237",
                PermissibleValue(text="mi:1237") )
        setattr(cls, "mi:2402",
                PermissibleValue(text="mi:2402") )
        setattr(cls, "mi:2369",
                PermissibleValue(text="mi:2369") )
        setattr(cls, "mi:1279",
                PermissibleValue(text="mi:1279") )
        setattr(cls, "mi:2401",
                PermissibleValue(text="mi:2401") )
        setattr(cls, "mi:2368",
                PermissibleValue(text="mi:2368") )
        setattr(cls, "mi:0945",
                PermissibleValue(text="mi:0945") )
        setattr(cls, "mi:1274",
                PermissibleValue(text="mi:1274") )
        setattr(cls, "mi:1273",
                PermissibleValue(text="mi:1273") )
        setattr(cls, "mi:1278",
                PermissibleValue(text="mi:1278") )
        setattr(cls, "mi:1310",
                PermissibleValue(text="mi:1310") )
        setattr(cls, "mi:1276",
                PermissibleValue(text="mi:1276") )
        setattr(cls, "mi:1110",
                PermissibleValue(text="mi:1110") )
        setattr(cls, "mi:0220",
                PermissibleValue(text="mi:0220") )
        setattr(cls, "mi:2364",
                PermissibleValue(text="mi:2364") )
        setattr(cls, "mi:0212",
                PermissibleValue(text="mi:0212") )
        setattr(cls, "mi:1148",
                PermissibleValue(text="mi:1148") )
        setattr(cls, "mi:0213",
                PermissibleValue(text="mi:0213") )
        setattr(cls, "mi:0216",
                PermissibleValue(text="mi:0216") )
        setattr(cls, "mi:0414",
                PermissibleValue(text="mi:0414") )
        setattr(cls, "mi:0217",
                PermissibleValue(text="mi:0217") )
        setattr(cls, "mi:2396",
                PermissibleValue(text="mi:2396") )
        setattr(cls, "mi:0570",
                PermissibleValue(text="mi:0570") )
        setattr(cls, "mi:0210",
                PermissibleValue(text="mi:0210") )
        setattr(cls, "mi:2397",
                PermissibleValue(text="mi:2397") )
        setattr(cls, "mi:2391",
                PermissibleValue(text="mi:2391") )
        setattr(cls, "mi:2390",
                PermissibleValue(text="mi:2390") )
        setattr(cls, "mi:0407",
                PermissibleValue(text="mi:0407") )
        setattr(cls, "mi:0408",
                PermissibleValue(text="mi:0408") )
        setattr(cls, "mi:0203",
                PermissibleValue(text="mi:0203") )
        setattr(cls, "mi:0566",
                PermissibleValue(text="mi:0566") )
        setattr(cls, "mi:0204",
                PermissibleValue(text="mi:0204") )
        setattr(cls, "mi:0403",
                PermissibleValue(text="mi:0403") )
        setattr(cls, "mi:0569",
                PermissibleValue(text="mi:0569") )
        setattr(cls, "mi:0844",
                PermissibleValue(text="mi:0844") )

class ConditionRelationEnum(EnumDefinitionImpl):

    has_condition = PermissibleValue(text="has_condition")
    induced_by = PermissibleValue(text="induced_by")
    not_induced_by = PermissibleValue(text="not_induced_by")
    ameliorated_by = PermissibleValue(text="ameliorated_by")
    not_ameliorated_by = PermissibleValue(text="not_ameliorated_by")
    exacerbated_by = PermissibleValue(text="exacerbated_by")
    not_exacerbated_by = PermissibleValue(text="not_exacerbated_by")

    _defn = EnumDefinition(
        name="ConditionRelationEnum",
    )

class GeneDiseaseRelationEnum(EnumDefinitionImpl):
    """
    Permissible values describing the relationship between gene and disease.
    """
    is_implicated_in = PermissibleValue(text="is_implicated_in")
    is_marker_for = PermissibleValue(text="is_marker_for")

    _defn = EnumDefinition(
        name="GeneDiseaseRelationEnum",
        description="Permissible values describing the relationship between gene and disease.",
    )

class AlleleDiseaseRelationEnum(EnumDefinitionImpl):
    """
    Permissible values describing the relationship between allele and disease.
    """
    is_implicated_in = PermissibleValue(text="is_implicated_in")

    _defn = EnumDefinition(
        name="AlleleDiseaseRelationEnum",
        description="Permissible values describing the relationship between allele and disease.",
    )

class AgmDiseaseRelationEnum(EnumDefinitionImpl):
    """
    Permissible values describing the relationship between gene and disease.
    """
    is_model_of = PermissibleValue(text="is_model_of")

    _defn = EnumDefinition(
        name="AgmDiseaseRelationEnum",
        description="Permissible values describing the relationship between gene and disease.",
    )

class GeneticSexEnum(EnumDefinitionImpl):
    """
    Permissible values for the genetic sex.
    """
    male = PermissibleValue(text="male")
    female = PermissibleValue(text="female")
    hermaphrodite = PermissibleValue(text="hermaphrodite")

    _defn = EnumDefinition(
        name="GeneticSexEnum",
        description="Permissible values for the genetic sex.",
    )

class GeneticModifierRelationEnum(EnumDefinitionImpl):
    """
    Permissible values for describing how a genetic object modifies the disease model.
    """
    ameliorated_by = PermissibleValue(text="ameliorated_by")
    not_ameliorated_by = PermissibleValue(text="not_ameliorated_by")
    exacerbated_by = PermissibleValue(text="exacerbated_by")
    not_exacerbated_by = PermissibleValue(text="not_exacerbated_by")

    _defn = EnumDefinition(
        name="GeneticModifierRelationEnum",
        description="Permissible values for describing how a genetic object modifies the disease model.",
    )

class DiseaseAnnotationQualifierEnum(EnumDefinitionImpl):

    susceptibility = PermissibleValue(text="susceptibility")
    disease_progression = PermissibleValue(text="disease_progression")
    severity = PermissibleValue(text="severity")
    onset = PermissibleValue(text="onset")
    sexual_dimorphism = PermissibleValue(text="sexual_dimorphism")
    resistance = PermissibleValue(text="resistance")
    penetrance = PermissibleValue(text="penetrance")

    _defn = EnumDefinition(
        name="DiseaseAnnotationQualifierEnum",
    )

class AnnotationTypeEnum(EnumDefinitionImpl):

    manually_curated = PermissibleValue(text="manually_curated")
    computational = PermissibleValue(text="computational")

    _defn = EnumDefinition(
        name="AnnotationTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "high-throughput",
                PermissibleValue(text="high-throughput") )

# Slots
class slots:
    pass

slots.topics = Slot(uri="str(uriorcurie)", name="topics", curie=None,
                   model_uri=ALLIANCE.topics, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.PubMed_type = Slot(uri="str(uriorcurie)", name="PubMed_type", curie=None,
                   model_uri=ALLIANCE.PubMed_type, domain=InformationContentEntity, range=Optional[str])

slots.date_published = Slot(uri="str(uriorcurie)", name="date_published", curie=None,
                   model_uri=ALLIANCE.date_published, domain=InformationContentEntity, range=Optional[Union[str, XSDDate]])

slots.date_last_modified_in_PubMed = Slot(uri="str(uriorcurie)", name="date_last_modified_in_PubMed", curie=None,
                   model_uri=ALLIANCE.date_last_modified_in_PubMed, domain=InformationContentEntity, range=Optional[Union[str, XSDDate]])

slots.year_published = Slot(uri="str(uriorcurie)", name="year_published", curie=None,
                   model_uri=ALLIANCE.year_published, domain=InformationContentEntity, range=Optional[str])

slots.month_published = Slot(uri="str(uriorcurie)", name="month_published", curie=None,
                   model_uri=ALLIANCE.month_published, domain=InformationContentEntity, range=Optional[str])

slots.day_published = Slot(uri="str(uriorcurie)", name="day_published", curie=None,
                   model_uri=ALLIANCE.day_published, domain=InformationContentEntity, range=Optional[str])

slots.date_arrived_in_PubMed = Slot(uri="str(uriorcurie)", name="date_arrived_in_PubMed", curie=None,
                   model_uri=ALLIANCE.date_arrived_in_PubMed, domain=InformationContentEntity, range=Optional[Union[str, XSDDate]])

slots.mod_reference_types = Slot(uri="str(uriorcurie)", name="mod_reference_types", curie=None,
                   model_uri=ALLIANCE.mod_reference_types, domain=None, range=Optional[Union[str, List[str]]])

slots.tags = Slot(uri="str(uriorcurie)", name="tags", curie=None,
                   model_uri=ALLIANCE.tags, domain=None, range=Optional[Union[Union[str, "TagSet"], List[Union[str, "TagSet"]]]])

slots.issue_date = Slot(uri="str(uriorcurie)", name="issue_date", curie=None,
                   model_uri=ALLIANCE.issue_date, domain=InformationContentEntity, range=Optional[Union[str, XSDDate]])

slots.volume = Slot(uri="str(uriorcurie)", name="volume", curie=None,
                   model_uri=ALLIANCE.volume, domain=InformationContentEntity, range=Optional[str])

slots.pages = Slot(uri="str(uriorcurie)", name="pages", curie=None,
                   model_uri=ALLIANCE.pages, domain=InformationContentEntity, range=Optional[Union[str, List[str]]])

slots.abstract = Slot(uri="str(uriorcurie)", name="abstract", curie=None,
                   model_uri=ALLIANCE.abstract, domain=Reference, range=Optional[str])

slots.citation = Slot(uri="str(uriorcurie)", name="citation", curie=None,
                   model_uri=ALLIANCE.citation, domain=Reference, range=Optional[str])

slots.issue_name = Slot(uri="str(uriorcurie)", name="issue_name", curie=None,
                   model_uri=ALLIANCE.issue_name, domain=Reference, range=Optional[str])

slots.alliance_category = Slot(uri="str(uriorcurie)", name="alliance_category", curie=None,
                   model_uri=ALLIANCE.alliance_category, domain=Reference, range=Optional[str])

slots.keywords = Slot(uri="str(uriorcurie)", name="keywords", curie=None,
                   model_uri=ALLIANCE.keywords, domain=InformationContentEntity, range=Optional[Union[str, List[str]]])

slots.from_resource = Slot(uri="str(uriorcurie)", name="from_resource", curie=None,
                   model_uri=ALLIANCE.from_resource, domain=Reference, range=Optional[Union[str, ResourceCurie]])

slots.iso_abbreviation = Slot(uri="str(uriorcurie)", name="iso_abbreviation", curie=None,
                   model_uri=ALLIANCE.iso_abbreviation, domain=Resource, range=Optional[str])

slots.medline_abbreviation = Slot(uri="str(uriorcurie)", name="medline_abbreviation", curie=None,
                   model_uri=ALLIANCE.medline_abbreviation, domain=Resource, range=Optional[str])

slots.print_issn = Slot(uri="str(uriorcurie)", name="print_issn", curie=None,
                   model_uri=ALLIANCE.print_issn, domain=Resource, range=Optional[str])

slots.online_issn = Slot(uri="str(uriorcurie)", name="online_issn", curie=None,
                   model_uri=ALLIANCE.online_issn, domain=Resource, range=Optional[str])

slots.editors = Slot(uri="str(uriorcurie)", name="editors", curie=None,
                   model_uri=ALLIANCE.editors, domain=Resource, range=Optional[Union[Union[dict, "AuthorReference"], List[Union[dict, "AuthorReference"]]]])

slots.notes = Slot(uri="str(uriorcurie)", name="notes", curie=None,
                   model_uri=ALLIANCE.notes, domain=None, range=Optional[Union[str, List[str]]])

slots.hgvs_nomenclature = Slot(uri="str(uriorcurie)", name="hgvs_nomenclature", curie=None,
                   model_uri=ALLIANCE.hgvs_nomenclature, domain=Variant, range=Optional[str])

slots.genomic_reference_sequence = Slot(uri="str(uriorcurie)", name="genomic_reference_sequence", curie=None,
                   model_uri=ALLIANCE.genomic_reference_sequence, domain=Variant, range=Optional[str])

slots.genomic_variant_sequence = Slot(uri="str(uriorcurie)", name="genomic_variant_sequence", curie=None,
                   model_uri=ALLIANCE.genomic_variant_sequence, domain=Variant, range=Optional[str])

slots.padding_left = Slot(uri="str(uriorcurie)", name="padding_left", curie=None,
                   model_uri=ALLIANCE.padding_left, domain=Variant, range=Optional[str])

slots.padding_right = Slot(uri="str(uriorcurie)", name="padding_right", curie=None,
                   model_uri=ALLIANCE.padding_right, domain=Variant, range=Optional[Union[str, BiologicalSequence]])

slots.protein_sequence = Slot(uri="str(uriorcurie)", name="protein_sequence", curie=None,
                   model_uri=ALLIANCE.protein_sequence, domain=Variant, range=Optional[str])

slots.computed_gene = Slot(uri="str(uriorcurie)", name="computed_gene", curie=None,
                   model_uri=ALLIANCE.computed_gene, domain=Variant, range=Optional[Union[str, GeneCurie]])

slots.variant_of_transcript = Slot(uri="str(uriorcurie)", name="variant_of_transcript", curie=None,
                   model_uri=ALLIANCE.variant_of_transcript, domain=Variant, range=Optional[Union[str, TranscriptCurie]])

slots.variant_of_allele = Slot(uri="str(uriorcurie)", name="variant_of_allele", curie=None,
                   model_uri=ALLIANCE.variant_of_allele, domain=Variant, range=Optional[Union[str, AlleleCurie]])

slots.vep_impact = Slot(uri="str(uriorcurie)", name="vep_impact", curie=None,
                   model_uri=ALLIANCE.vep_impact, domain=None, range=Optional[str])

slots.vep_consequence = Slot(uri="str(uriorcurie)", name="vep_consequence", curie=None,
                   model_uri=ALLIANCE.vep_consequence, domain=None, range=Optional[Union[str, "VepConsequenceLevels"]])

slots.polyphen_score = Slot(uri="str(uriorcurie)", name="polyphen_score", curie=None,
                   model_uri=ALLIANCE.polyphen_score, domain=VariantGeneConsequence, range=Optional[float])

slots.polyphen_prediction = Slot(uri="str(uriorcurie)", name="polyphen_prediction", curie=None,
                   model_uri=ALLIANCE.polyphen_prediction, domain=None, range=Optional[Union[str, "PolyphenPredictionLevels"]])

slots.sift_score = Slot(uri="str(uriorcurie)", name="sift_score", curie=None,
                   model_uri=ALLIANCE.sift_score, domain=VariantGeneConsequence, range=Optional[float])

slots.sift_prediction = Slot(uri="str(uriorcurie)", name="sift_prediction", curie=None,
                   model_uri=ALLIANCE.sift_prediction, domain=None, range=Optional[Union[str, "SiftPredictionLevels"]])

slots.amino_acid_reference = Slot(uri="str(uriorcurie)", name="amino_acid_reference", curie=None,
                   model_uri=ALLIANCE.amino_acid_reference, domain=VariantTranscriptConsequence, range=Optional[str])

slots.amino_acid_variant = Slot(uri="str(uriorcurie)", name="amino_acid_variant", curie=None,
                   model_uri=ALLIANCE.amino_acid_variant, domain=VariantTranscriptConsequence, range=Optional[str])

slots.codon_reference = Slot(uri="str(uriorcurie)", name="codon_reference", curie=None,
                   model_uri=ALLIANCE.codon_reference, domain=VariantTranscriptConsequence, range=Optional[str])

slots.codon_variant = Slot(uri="str(uriorcurie)", name="codon_variant", curie=None,
                   model_uri=ALLIANCE.codon_variant, domain=VariantTranscriptConsequence, range=Optional[str])

slots.cdna_start = Slot(uri="str(uriorcurie)", name="cdna_start", curie=None,
                   model_uri=ALLIANCE.cdna_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.cdna_end = Slot(uri="str(uriorcurie)", name="cdna_end", curie=None,
                   model_uri=ALLIANCE.cdna_end, domain=VariantTranscriptConsequence, range=Optional[int])

slots.cds_start = Slot(uri="str(uriorcurie)", name="cds_start", curie=None,
                   model_uri=ALLIANCE.cds_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.cds_end = Slot(uri="str(uriorcurie)", name="cds_end", curie=None,
                   model_uri=ALLIANCE.cds_end, domain=VariantTranscriptConsequence, range=Optional[int])

slots.protein_start = Slot(uri="str(uriorcurie)", name="protein_start", curie=None,
                   model_uri=ALLIANCE.protein_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.protein_end = Slot(uri="str(uriorcurie)", name="protein_end", curie=None,
                   model_uri=ALLIANCE.protein_end, domain=VariantTranscriptConsequence, range=Optional[int])

slots.hgvs_protein_nomenclature = Slot(uri="str(uriorcurie)", name="hgvs_protein_nomenclature", curie=None,
                   model_uri=ALLIANCE.hgvs_protein_nomenclature, domain=VariantTranscriptConsequence, range=Optional[str])

slots.hgvs_coding_nomenclature = Slot(uri="str(uriorcurie)", name="hgvs_coding_nomenclature", curie=None,
                   model_uri=ALLIANCE.hgvs_coding_nomenclature, domain=VariantTranscriptConsequence, range=Optional[str])

slots.located_on = Slot(uri="str(uriorcurie)", name="located on", curie=None,
                   model_uri=ALLIANCE.located_on, domain=None, range=Optional[Union[str, ChromosomeCurie]])

slots.start = Slot(uri=ALLIANCE.start, name="start", curie=ALLIANCE.curie('start'),
                   model_uri=ALLIANCE.start, domain=None, range=Optional[str])

slots.end = Slot(uri=ALLIANCE.end, name="end", curie=ALLIANCE.curie('end'),
                   model_uri=ALLIANCE.end, domain=None, range=Optional[str])

slots.has_assembly = Slot(uri=ALLIANCE.has_assembly, name="has_assembly", curie=ALLIANCE.curie('has_assembly'),
                   model_uri=ALLIANCE.has_assembly, domain=GenomicEntity, range=Union[str, ChromosomeCurie])

slots.prefix = Slot(uri=ALLIANCE.prefix, name="prefix", curie=ALLIANCE.curie('prefix'),
                   model_uri=ALLIANCE.prefix, domain=None, range=str)

slots.page_areas = Slot(uri=ALLIANCE.page_areas, name="page_areas", curie=ALLIANCE.curie('page_areas'),
                   model_uri=ALLIANCE.page_areas, domain=None, range=Union[str, List[str]])

slots.display_name = Slot(uri=ALLIANCE.display_name, name="display_name", curie=ALLIANCE.curie('display_name'),
                   model_uri=ALLIANCE.display_name, domain=None, range=str)

slots.curator_comment = Slot(uri=ALLIANCE.curator_comment, name="curator_comment", curie=ALLIANCE.curie('curator_comment'),
                   model_uri=ALLIANCE.curator_comment, domain=None, range=Optional[str])

slots.url_prefix = Slot(uri=ALLIANCE.url_prefix, name="url_prefix", curie=ALLIANCE.curie('url_prefix'),
                   model_uri=ALLIANCE.url_prefix, domain=None, range=Optional[str])

slots.url_suffix = Slot(uri=ALLIANCE.url_suffix, name="url_suffix", curie=ALLIANCE.curie('url_suffix'),
                   model_uri=ALLIANCE.url_suffix, domain=None, range=Optional[str])

slots.prefix_order = Slot(uri=ALLIANCE.prefix_order, name="prefix_order", curie=ALLIANCE.curie('prefix_order'),
                   model_uri=ALLIANCE.prefix_order, domain=None, range=Optional[str])

slots.prefix_page = Slot(uri=ALLIANCE.prefix_page, name="prefix_page", curie=ALLIANCE.curie('prefix_page'),
                   model_uri=ALLIANCE.prefix_page, domain=None, range=Optional[str])

slots.private_comment = Slot(uri=ALLIANCE.private_comment, name="private_comment", curie=ALLIANCE.curie('private_comment'),
                   model_uri=ALLIANCE.private_comment, domain=None, range=Optional[str])

slots.uncertain = Slot(uri=ALLIANCE.uncertain, name="uncertain", curie=ALLIANCE.curie('uncertain'),
                   model_uri=ALLIANCE.uncertain, domain=None, range=Optional[Union[bool, Bool]])

slots.statement_subject = Slot(uri=ALLIANCE.statement_subject, name="statement_subject", curie=ALLIANCE.curie('statement_subject'),
                   model_uri=ALLIANCE.statement_subject, domain=EntityStatement, range=Optional[str])

slots.statement_type = Slot(uri=ALLIANCE.statement_type, name="statement_type", curie=ALLIANCE.curie('statement_type'),
                   model_uri=ALLIANCE.statement_type, domain=EntityStatement, range=Optional[str])

slots.statement_text = Slot(uri=ALLIANCE.statement_text, name="statement_text", curie=ALLIANCE.curie('statement_text'),
                   model_uri=ALLIANCE.statement_text, domain=EntityStatement, range=Optional[str])

slots.generated_by = Slot(uri=ALLIANCE.generated_by, name="generated_by", curie=ALLIANCE.curie('generated_by'),
                   model_uri=ALLIANCE.generated_by, domain=None, range=Optional[Union[Union[dict, Agent], List[Union[dict, Agent]]]])

slots.manufactured_by = Slot(uri=ALLIANCE.manufactured_by, name="manufactured_by", curie=ALLIANCE.curie('manufactured_by'),
                   model_uri=ALLIANCE.manufactured_by, domain=None, range=Optional[Union[Union[dict, Agent], List[Union[dict, Agent]]]])

slots.current = Slot(uri=ALLIANCE.current, name="current", curie=ALLIANCE.curie('current'),
                   model_uri=ALLIANCE.current, domain=None, range=Optional[Union[bool, Bool]])

slots.curie = Slot(uri=ALLIANCE.curie, name="curie", curie=ALLIANCE.curie('curie'),
                   model_uri=ALLIANCE.curie, domain=None, range=URIRef)

slots.unique_id = Slot(uri=ALLIANCE.unique_id, name="unique_id", curie=ALLIANCE.curie('unique_id'),
                   model_uri=ALLIANCE.unique_id, domain=None, range=Optional[str])

slots.dbkey = Slot(uri=ALLIANCE.dbkey, name="dbkey", curie=ALLIANCE.curie('dbkey'),
                   model_uri=ALLIANCE.dbkey, domain=None, range=Optional[str])

slots.taxon = Slot(uri=ALLIANCE.taxon, name="taxon", curie=ALLIANCE.curie('taxon'),
                   model_uri=ALLIANCE.taxon, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.secondary_identifiers = Slot(uri=ALLIANCE.secondary_identifiers, name="secondary_identifiers", curie=ALLIANCE.curie('secondary_identifiers'),
                   model_uri=ALLIANCE.secondary_identifiers, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.gene_synopsis = Slot(uri=ALLIANCE.gene_synopsis, name="gene_synopsis", curie=ALLIANCE.curie('gene_synopsis'),
                   model_uri=ALLIANCE.gene_synopsis, domain=None, range=Optional[str])

slots.gene_synopsis_URL = Slot(uri=ALLIANCE.gene_synopsis_URL, name="gene_synopsis_URL", curie=ALLIANCE.curie('gene_synopsis_URL'),
                   model_uri=ALLIANCE.gene_synopsis_URL, domain=None, range=Optional[str])

slots.automated_gene_description = Slot(uri=ALLIANCE.automated_gene_description, name="automated_gene_description", curie=ALLIANCE.curie('automated_gene_description'),
                   model_uri=ALLIANCE.automated_gene_description, domain=None, range=Optional[str])

slots.genomic_locations = Slot(uri=ALLIANCE.genomic_locations, name="genomic_locations", curie=ALLIANCE.curie('genomic_locations'),
                   model_uri=ALLIANCE.genomic_locations, domain=GenomicEntity, range=Optional[Union[Union[dict, "GeneGenomicLocation"], List[Union[dict, "GeneGenomicLocation"]]]])

slots.table_key = Slot(uri=ALLIANCE.table_key, name="table_key", curie=ALLIANCE.curie('table_key'),
                   model_uri=ALLIANCE.table_key, domain=None, range=Optional[int])

slots.creation_date = Slot(uri=ALLIANCE.creation_date, name="creation_date", curie=ALLIANCE.curie('creation_date'),
                   model_uri=ALLIANCE.creation_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.date_last_modified = Slot(uri=ALLIANCE.date_last_modified, name="date_last_modified", curie=ALLIANCE.curie('date_last_modified'),
                   model_uri=ALLIANCE.date_last_modified, domain=None, range=Optional[Union[str, XSDDate]])

slots.created_by = Slot(uri=ALLIANCE.created_by, name="created_by", curie=ALLIANCE.curie('created_by'),
                   model_uri=ALLIANCE.created_by, domain=None, range=Union[str, PersonPersonId])

slots.modified_by = Slot(uri=ALLIANCE.modified_by, name="modified_by", curie=ALLIANCE.curie('modified_by'),
                   model_uri=ALLIANCE.modified_by, domain=None, range=Union[str, PersonPersonId])

slots.release = Slot(uri=ALLIANCE.release, name="release", curie=ALLIANCE.curie('release'),
                   model_uri=ALLIANCE.release, domain=None, range=Optional[str])

slots.data_provider = Slot(uri=ALLIANCE.data_provider, name="data_provider", curie=ALLIANCE.curie('data_provider'),
                   model_uri=ALLIANCE.data_provider, domain=None, range=Optional[Union[str, List[str]]])

slots.association_slot = Slot(uri=ALLIANCE.association_slot, name="association_slot", curie=ALLIANCE.curie('association_slot'),
                   model_uri=ALLIANCE.association_slot, domain=None, range=Optional[str])

slots.description = Slot(uri=ALLIANCE.description, name="description", curie=ALLIANCE.curie('description'),
                   model_uri=ALLIANCE.description, domain=None, range=Optional[str])

slots.name = Slot(uri=ALLIANCE.name, name="name", curie=ALLIANCE.curie('name'),
                   model_uri=ALLIANCE.name, domain=None, range=Optional[str])

slots.cross_references = Slot(uri=ALLIANCE.cross_references, name="cross_references", curie=ALLIANCE.curie('cross_references'),
                   model_uri=ALLIANCE.cross_references, domain=None, range=Optional[Union[Dict[Union[str, CrossReferenceCurie], Union[dict, CrossReference]], List[Union[dict, CrossReference]]]])

slots.symbol = Slot(uri=ALLIANCE.symbol, name="symbol", curie=ALLIANCE.curie('symbol'),
                   model_uri=ALLIANCE.symbol, domain=None, range=Optional[str])

slots.from_species = Slot(uri=ALLIANCE.from_species, name="from_species", curie=ALLIANCE.curie('from_species'),
                   model_uri=ALLIANCE.from_species, domain=None, range=Optional[Union[dict, Species]])

slots.synonyms = Slot(uri=ALLIANCE.synonyms, name="synonyms", curie=ALLIANCE.curie('synonyms'),
                   model_uri=ALLIANCE.synonyms, domain=None, range=Optional[Union[Union[dict, Synonym], List[Union[dict, Synonym]]]])

slots.negated = Slot(uri=ALLIANCE.negated, name="negated", curie=ALLIANCE.curie('negated'),
                   model_uri=ALLIANCE.negated, domain=None, range=Optional[Union[bool, Bool]])

slots.qualifiers = Slot(uri=ALLIANCE.qualifiers, name="qualifiers", curie=ALLIANCE.curie('qualifiers'),
                   model_uri=ALLIANCE.qualifiers, domain=None, range=Optional[str])

slots.type = Slot(uri=ALLIANCE.type, name="type", curie=ALLIANCE.curie('type'),
                   model_uri=ALLIANCE.type, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.gene_type = Slot(uri=ALLIANCE.gene_type, name="gene_type", curie=ALLIANCE.curie('gene_type'),
                   model_uri=ALLIANCE.gene_type, domain=Gene, range=Optional[Union[str, SOTermCurie]])

slots.taxon_id = Slot(uri=ALLIANCE.taxon_id, name="taxon_id", curie=ALLIANCE.curie('taxon_id'),
                   model_uri=ALLIANCE.taxon_id, domain=None, range=Optional[int])

slots.references = Slot(uri=ALLIANCE.references, name="references", curie=ALLIANCE.curie('references'),
                   model_uri=ALLIANCE.references, domain=None, range=Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]])

slots.reference = Slot(uri=ALLIANCE.reference, name="reference", curie=ALLIANCE.curie('reference'),
                   model_uri=ALLIANCE.reference, domain=None, range=Optional[Union[str, ReferenceCurie]])

slots.original_reference = Slot(uri=ALLIANCE.original_reference, name="original_reference", curie=ALLIANCE.curie('original_reference'),
                   model_uri=ALLIANCE.original_reference, domain=None, range=Optional[Union[str, ReferenceCurie]])

slots.is_obsolete = Slot(uri=ALLIANCE.is_obsolete, name="is_obsolete", curie=ALLIANCE.curie('is_obsolete'),
                   model_uri=ALLIANCE.is_obsolete, domain=None, range=Optional[Union[bool, Bool]])

slots.abbreviation = Slot(uri=ALLIANCE.abbreviation, name="abbreviation", curie=ALLIANCE.curie('abbreviation'),
                   model_uri=ALLIANCE.abbreviation, domain=None, range=Optional[str])

slots.subject = Slot(uri=ALLIANCE.subject, name="subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.subject, domain=None, range=str)

slots.object = Slot(uri=ALLIANCE.object, name="object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.object, domain=None, range=str)

slots.predicate = Slot(uri=ALLIANCE.predicate, name="predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.predicate, domain=None, range=str)

slots.related_to = Slot(uri=ALLIANCE.related_to, name="related_to", curie=ALLIANCE.curie('related_to'),
                   model_uri=ALLIANCE.related_to, domain=None, range=Optional[Union[str, List[str]]])

slots.summary = Slot(uri=ALLIANCE.summary, name="summary", curie=ALLIANCE.curie('summary'),
                   model_uri=ALLIANCE.summary, domain=InformationContentEntity, range=Optional[str])

slots.copyright_date = Slot(uri=ALLIANCE.copyright_date, name="copyright_date", curie=ALLIANCE.curie('copyright_date'),
                   model_uri=ALLIANCE.copyright_date, domain=InformationContentEntity, range=Optional[Union[str, XSDDate]])

slots.authors = Slot(uri=ALLIANCE.authors, name="authors", curie=ALLIANCE.curie('authors'),
                   model_uri=ALLIANCE.authors, domain=InformationContentEntity, range=Optional[Union[Union[dict, "AuthorReference"], List[Union[dict, "AuthorReference"]]]])

slots.corresponding_author = Slot(uri=ALLIANCE.corresponding_author, name="corresponding_author", curie=ALLIANCE.curie('corresponding_author'),
                   model_uri=ALLIANCE.corresponding_author, domain=InformationContentEntity, range=Optional[Union[str, InformationContentEntityCurie]])

slots.first_name = Slot(uri=ALLIANCE.first_name, name="first_name", curie=ALLIANCE.curie('first_name'),
                   model_uri=ALLIANCE.first_name, domain=InformationContentEntity, range=Optional[Union[str, InformationContentEntityCurie]])

slots.middle_names = Slot(uri=ALLIANCE.middle_names, name="middle_names", curie=ALLIANCE.curie('middle_names'),
                   model_uri=ALLIANCE.middle_names, domain=InformationContentEntity, range=Optional[Union[str, InformationContentEntityCurie]])

slots.last_name = Slot(uri=ALLIANCE.last_name, name="last_name", curie=ALLIANCE.curie('last_name'),
                   model_uri=ALLIANCE.last_name, domain=InformationContentEntity, range=Optional[Union[str, InformationContentEntityCurie]])

slots.initials = Slot(uri=ALLIANCE.initials, name="initials", curie=ALLIANCE.curie('initials'),
                   model_uri=ALLIANCE.initials, domain=InformationContentEntity, range=Optional[Union[str, InformationContentEntityCurie]])

slots.title = Slot(uri=ALLIANCE.title, name="title", curie=ALLIANCE.curie('title'),
                   model_uri=ALLIANCE.title, domain=InformationContentEntity, range=Optional[str])

slots.volumes = Slot(uri=ALLIANCE.volumes, name="volumes", curie=ALLIANCE.curie('volumes'),
                   model_uri=ALLIANCE.volumes, domain=InformationContentEntity, range=Optional[str])

slots.publisher = Slot(uri=ALLIANCE.publisher, name="publisher", curie=ALLIANCE.curie('publisher'),
                   model_uri=ALLIANCE.publisher, domain=InformationContentEntity, range=Optional[Union[str, InformationContentEntityCurie]])

slots.address = Slot(uri=ALLIANCE.address, name="address", curie=ALLIANCE.curie('address'),
                   model_uri=ALLIANCE.address, domain=None, range=Optional[str])

slots.orcid = Slot(uri=ALLIANCE.orcid, name="orcid", curie=ALLIANCE.curie('orcid'),
                   model_uri=ALLIANCE.orcid, domain=InformationContentEntity, range=Optional[str])

slots.component_relation = Slot(uri="str(uriorcurie)", name="component_relation", curie=None,
                   model_uri=ALLIANCE.component_relation, domain=None, range=Optional[Union[str, "ComponentRelationsEnum"]])

slots.construct_components = Slot(uri="str(uriorcurie)", name="construct_components", curie=None,
                   model_uri=ALLIANCE.construct_components, domain=None, range=Optional[Union[Union[str, ConstructComponentCurie], List[Union[str, ConstructComponentCurie]]]])

slots.affected_entities = Slot(uri="str(uriorcurie)", name="affected_entities", curie=None,
                   model_uri=ALLIANCE.affected_entities, domain=Allele, range=Optional[Union[Union[str, BiologicalEntityCurie], List[Union[str, BiologicalEntityCurie]]]])

slots.contains_construct = Slot(uri="str(uriorcurie)", name="contains_construct", curie=None,
                   model_uri=ALLIANCE.contains_construct, domain=Allele, range=Optional[Union[str, ConstructCurie]])

slots.molecular_mutation = Slot(uri="str(uriorcurie)", name="molecular_mutation", curie=None,
                   model_uri=ALLIANCE.molecular_mutation, domain=Allele, range=Optional[Union[dict, "MolecularMutation"]])

slots.mutation_type = Slot(uri="str(uriorcurie)", name="mutation_type", curie=None,
                   model_uri=ALLIANCE.mutation_type, domain=MolecularMutation, range=Optional[Union[str, SOTermCurie]])

slots.mutation_description = Slot(uri="str(uriorcurie)", name="mutation_description", curie=None,
                   model_uri=ALLIANCE.mutation_description, domain=None, range=Optional[str])

slots.functional_impact = Slot(uri="str(uriorcurie)", name="functional_impact", curie=None,
                   model_uri=ALLIANCE.functional_impact, domain=Allele, range=Optional[str])

slots.generation_method = Slot(uri="str(uriorcurie)", name="generation_method", curie=None,
                   model_uri=ALLIANCE.generation_method, domain=Allele, range=Optional[str])

slots.associated_references = Slot(uri="str(uriorcurie)", name="associated_references", curie=None,
                   model_uri=ALLIANCE.associated_references, domain=None, range=Optional[Union[Union[dict, ReferenceType], List[Union[dict, ReferenceType]]]])

slots.reference_association = Slot(uri="str(uriorcurie)", name="reference_association", curie=None,
                   model_uri=ALLIANCE.reference_association, domain=ReferenceType, range=Optional[Union[str, "ReferenceAssociationTypes"]])

slots.has_reference = Slot(uri="str(uriorcurie)", name="has_reference", curie=None,
                   model_uri=ALLIANCE.has_reference, domain=ReferenceType, range=Optional[Union[str, ReferenceCurie]])

slots.associated_notes = Slot(uri="str(uriorcurie)", name="associated_notes", curie=None,
                   model_uri=ALLIANCE.associated_notes, domain=None, range=Optional[Union[dict, NoteType]])

slots.note_association = Slot(uri="str(uriorcurie)", name="note_association", curie=None,
                   model_uri=ALLIANCE.note_association, domain=NoteType, range=Optional[Union[str, "NoteAssociationTypes"]])

slots.origins = Slot(uri="str(uriorcurie)", name="origins", curie=None,
                   model_uri=ALLIANCE.origins, domain=Allele, range=Optional[Union[Union[str, AffectedGenomicModelCurie], List[Union[str, AffectedGenomicModelCurie]]]])

slots.germline_transmission_status = Slot(uri="str(uriorcurie)", name="germline_transmission_status", curie=None,
                   model_uri=ALLIANCE.germline_transmission_status, domain=Allele, range=Optional[str])

slots.parent_cell_line = Slot(uri="str(uriorcurie)", name="parent_cell_line", curie=None,
                   model_uri=ALLIANCE.parent_cell_line, domain=Allele, range=Optional[Union[dict, "CellLine"]])

slots.mutant_cell_lines = Slot(uri="str(uriorcurie)", name="mutant_cell_lines", curie=None,
                   model_uri=ALLIANCE.mutant_cell_lines, domain=Allele, range=Optional[Union[Union[dict, "CellLine"], List[Union[dict, "CellLine"]]]])

slots.embryonic_stem_cell_lines = Slot(uri="str(uriorcurie)", name="embryonic_stem_cell_lines", curie=None,
                   model_uri=ALLIANCE.embryonic_stem_cell_lines, domain=Allele, range=Optional[Union[Union[dict, "CellLine"], List[Union[dict, "CellLine"]]]])

slots.database_status = Slot(uri="str(uriorcurie)", name="database_status", curie=None,
                   model_uri=ALLIANCE.database_status, domain=None, range=Optional[Union[str, "DatabaseStatuses"]])

slots.inheritence_mode = Slot(uri="str(uriorcurie)", name="inheritence_mode", curie=None,
                   model_uri=ALLIANCE.inheritence_mode, domain=Allele, range=Optional[Union[str, "ModesOfInheritence"]])

slots.in_collection = Slot(uri="str(uriorcurie)", name="in_collection", curie=None,
                   model_uri=ALLIANCE.in_collection, domain=Allele, range=Optional[str])

slots.transposon_insertion = Slot(uri="str(uriorcurie)", name="transposon_insertion", curie=None,
                   model_uri=ALLIANCE.transposon_insertion, domain=Allele, range=Optional[str])

slots.aberration = Slot(uri="str(uriorcurie)", name="aberration", curie=None,
                   model_uri=ALLIANCE.aberration, domain=Allele, range=Optional[str])

slots.is_extinct = Slot(uri="str(uriorcurie)", name="is_extinct", curie=None,
                   model_uri=ALLIANCE.is_extinct, domain=Allele, range=Optional[Union[bool, Bool]])

slots.subtype = Slot(uri="str(uriorcurie)", name="subtype", curie=None,
                   model_uri=ALLIANCE.subtype, domain=AffectedGenomicModel, range=Optional[Union[str, "SubtypeValues"]])

slots.components = Slot(uri="str(uriorcurie)", name="components", curie=None,
                   model_uri=ALLIANCE.components, domain=AffectedGenomicModel, range=Optional[Union[Union[dict, "AffectedGenomicModelComponent"], List[Union[dict, "AffectedGenomicModelComponent"]]]])

slots.has_allele = Slot(uri="str(uriorcurie)", name="has_allele", curie=None,
                   model_uri=ALLIANCE.has_allele, domain=AffectedGenomicModelComponent, range=Optional[Union[str, AlleleCurie]])

slots.zygosity = Slot(uri="str(uriorcurie)", name="zygosity", curie=None,
                   model_uri=ALLIANCE.zygosity, domain=AffectedGenomicModelComponent, range=Optional[Union[str, "ZygosityValues"]])

slots.sequence_targeting_reagents = Slot(uri="str(uriorcurie)", name="sequence_targeting_reagents", curie=None,
                   model_uri=ALLIANCE.sequence_targeting_reagents, domain=AffectedGenomicModel, range=Optional[Union[Union[dict, SequenceTargetingReagent], List[Union[dict, SequenceTargetingReagent]]]])

slots.parental_populations = Slot(uri="str(uriorcurie)", name="parental_populations", curie=None,
                   model_uri=ALLIANCE.parental_populations, domain=AffectedGenomicModel, range=Optional[Union[str, URIorCURIE]])

slots.antibody_target_genes = Slot(uri="str(uriorcurie)", name="antibody_target_genes", curie=None,
                   model_uri=ALLIANCE.antibody_target_genes, domain=Antibody, range=Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]])

slots.antigen_taxon = Slot(uri="str(uriorcurie)", name="antigen_taxon", curie=None,
                   model_uri=ALLIANCE.antigen_taxon, domain=Antibody, range=Optional[Union[str, URIorCURIE]])

slots.clonality = Slot(uri="str(uriorcurie)", name="clonality", curie=None,
                   model_uri=ALLIANCE.clonality, domain=Antibody, range=Union[str, "AntibodyClonalitySet"])

slots.heavy_chain_isotype = Slot(uri="str(uriorcurie)", name="heavy_chain_isotype", curie=None,
                   model_uri=ALLIANCE.heavy_chain_isotype, domain=Antibody, range=Optional[Union[str, "HeavyChainIsotypeSet"]])

slots.light_chain_isotype = Slot(uri="str(uriorcurie)", name="light_chain_isotype", curie=None,
                   model_uri=ALLIANCE.light_chain_isotype, domain=Antibody, range=Optional[Union[str, "LightChainIsotypeSet"]])

slots.aggregation_database = Slot(uri=ALLIANCE.aggregation_database, name="aggregation_database", curie=ALLIANCE.curie('aggregation_database'),
                   model_uri=ALLIANCE.aggregation_database, domain=None, range=Optional[str])

slots.interaction_data_provider = Slot(uri=ALLIANCE.interaction_data_provider, name="interaction_data_provider", curie=ALLIANCE.curie('interaction_data_provider'),
                   model_uri=ALLIANCE.interaction_data_provider, domain=None, range=Optional[Union[str, "InteractionSourceEnum"]])

slots.interaction_type = Slot(uri=ALLIANCE.interaction_type, name="interaction_type", curie=ALLIANCE.curie('interaction_type'),
                   model_uri=ALLIANCE.interaction_type, domain=GeneInteraction, range=Union[str, "InteractionTypeEnum"])

slots.interactor_A_role = Slot(uri=ALLIANCE.interactor_A_role, name="interactor_A_role", curie=ALLIANCE.curie('interactor_A_role'),
                   model_uri=ALLIANCE.interactor_A_role, domain=GeneInteraction, range=Optional[Union[Union[str, "InteractorARoleEnum"], List[Union[str, "InteractorARoleEnum"]]]])

slots.interactor_B_role = Slot(uri=ALLIANCE.interactor_B_role, name="interactor_B_role", curie=ALLIANCE.curie('interactor_B_role'),
                   model_uri=ALLIANCE.interactor_B_role, domain=GeneInteraction, range=Optional[Union[Union[str, "InteractorBRoleEnum"], List[Union[str, "InteractorBRoleEnum"]]]])

slots.interactor_A_type = Slot(uri=ALLIANCE.interactor_A_type, name="interactor_A_type", curie=ALLIANCE.curie('interactor_A_type'),
                   model_uri=ALLIANCE.interactor_A_type, domain=GeneInteraction, range=Union[str, "InteractorTypeEnum"])

slots.interactor_B_type = Slot(uri=ALLIANCE.interactor_B_type, name="interactor_B_type", curie=ALLIANCE.curie('interactor_B_type'),
                   model_uri=ALLIANCE.interactor_B_type, domain=GeneInteraction, range=Union[str, "InteractorTypeEnum"])

slots.detection_method = Slot(uri=ALLIANCE.detection_method, name="detection_method", curie=ALLIANCE.curie('detection_method'),
                   model_uri=ALLIANCE.detection_method, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.interactor_A_genetic_perturbation = Slot(uri=ALLIANCE.interactor_A_genetic_perturbation, name="interactor_A_genetic_perturbation", curie=ALLIANCE.curie('interactor_A_genetic_perturbation'),
                   model_uri=ALLIANCE.interactor_A_genetic_perturbation, domain=GeneGeneticInteraction, range=Optional[Union[str, AlleleCurie]])

slots.interactor_B_genetic_perturbation = Slot(uri=ALLIANCE.interactor_B_genetic_perturbation, name="interactor_B_genetic_perturbation", curie=ALLIANCE.curie('interactor_B_genetic_perturbation'),
                   model_uri=ALLIANCE.interactor_B_genetic_perturbation, domain=GeneGeneticInteraction, range=Optional[Union[str, AlleleCurie]])

slots.phenotype_or_trait = Slot(uri=ALLIANCE.phenotype_or_trait, name="phenotype_or_trait", curie=ALLIANCE.curie('phenotype_or_trait'),
                   model_uri=ALLIANCE.phenotype_or_trait, domain=GeneGeneticInteraction, range=Optional[Union[str, List[str]]])

slots.interacts_with = Slot(uri=ALLIANCE.interacts_with, name="interacts_with", curie=ALLIANCE.curie('interacts_with'),
                   model_uri=ALLIANCE.interacts_with, domain=BiologicalEntity, range=Optional[Union[Union[str, BiologicalEntityCurie], List[Union[str, BiologicalEntityCurie]]]])

slots.physically_interacts_with = Slot(uri=ALLIANCE.physically_interacts_with, name="physically_interacts_with", curie=ALLIANCE.curie('physically_interacts_with'),
                   model_uri=ALLIANCE.physically_interacts_with, domain=BiologicalEntity, range=Optional[Union[Union[str, BiologicalEntityCurie], List[Union[str, BiologicalEntityCurie]]]])

slots.genetically_interacts_with = Slot(uri=ALLIANCE.genetically_interacts_with, name="genetically_interacts_with", curie=ALLIANCE.curie('genetically_interacts_with'),
                   model_uri=ALLIANCE.genetically_interacts_with, domain=Gene, range=Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]])

slots.definition = Slot(uri="str(uriorcurie)", name="definition", curie=None,
                   model_uri=ALLIANCE.definition, domain=None, range=Optional[str])

slots.display_synonym = Slot(uri="str(uriorcurie)", name="display_synonym", curie=None,
                   model_uri=ALLIANCE.display_synonym, domain=None, range=Optional[str])

slots.namespace = Slot(uri="str(uriorcurie)", name="namespace", curie=None,
                   model_uri=ALLIANCE.namespace, domain=None, range=Optional[str])

slots.subsets = Slot(uri="str(uriorcurie)", name="subsets", curie=None,
                   model_uri=ALLIANCE.subsets, domain=None, range=Optional[Union[str, List[str]]])

slots.definition_urls = Slot(uri="str(uriorcurie)", name="definition_urls", curie=None,
                   model_uri=ALLIANCE.definition_urls, domain=None, range=Optional[Union[str, List[str]]])

slots.condition_anatomy = Slot(uri=ALLIANCE.condition_anatomy, name="condition_anatomy", curie=ALLIANCE.curie('condition_anatomy'),
                   model_uri=ALLIANCE.condition_anatomy, domain=ExperimentalCondition, range=Optional[Union[str, AnatomicalTermCurie]])

slots.condition_chemical = Slot(uri=ALLIANCE.condition_chemical, name="condition_chemical", curie=ALLIANCE.curie('condition_chemical'),
                   model_uri=ALLIANCE.condition_chemical, domain=ExperimentalCondition, range=Optional[Union[str, URIorCURIE]])

slots.condition_class = Slot(uri=ALLIANCE.condition_class, name="condition_class", curie=ALLIANCE.curie('condition_class'),
                   model_uri=ALLIANCE.condition_class, domain=ExperimentalCondition, range=Optional[Union[str, ZECOTermCurie]])

slots.condition_gene_ontology = Slot(uri=ALLIANCE.condition_gene_ontology, name="condition_gene_ontology", curie=ALLIANCE.curie('condition_gene_ontology'),
                   model_uri=ALLIANCE.condition_gene_ontology, domain=ExperimentalCondition, range=Optional[Union[str, GOTermCurie]])

slots.condition_id = Slot(uri=ALLIANCE.condition_id, name="condition_id", curie=ALLIANCE.curie('condition_id'),
                   model_uri=ALLIANCE.condition_id, domain=ExperimentalCondition, range=Optional[Union[str, ExperimentalConditionOntologyTermCurie]])

slots.condition_quantity = Slot(uri=ALLIANCE.condition_quantity, name="condition_quantity", curie=ALLIANCE.curie('condition_quantity'),
                   model_uri=ALLIANCE.condition_quantity, domain=ExperimentalCondition, range=Optional[str])

slots.condition_statement = Slot(uri=ALLIANCE.condition_statement, name="condition_statement", curie=ALLIANCE.curie('condition_statement'),
                   model_uri=ALLIANCE.condition_statement, domain=ExperimentalCondition, range=Optional[str])

slots.condition_taxon = Slot(uri=ALLIANCE.condition_taxon, name="condition_taxon", curie=ALLIANCE.curie('condition_taxon'),
                   model_uri=ALLIANCE.condition_taxon, domain=ExperimentalCondition, range=Optional[Union[str, URIorCURIE]])

slots.condition_relations = Slot(uri=ALLIANCE.condition_relations, name="condition_relations", curie=ALLIANCE.curie('condition_relations'),
                   model_uri=ALLIANCE.condition_relations, domain=None, range=Optional[Union[Union[dict, ConditionRelation], List[Union[dict, ConditionRelation]]]])

slots.condition_relation_type = Slot(uri=ALLIANCE.condition_relation_type, name="condition_relation_type", curie=ALLIANCE.curie('condition_relation_type'),
                   model_uri=ALLIANCE.condition_relation_type, domain=None, range=Optional[Union[str, "ConditionRelationEnum"]])

slots.conditions = Slot(uri=ALLIANCE.conditions, name="conditions", curie=ALLIANCE.curie('conditions'),
                   model_uri=ALLIANCE.conditions, domain=None, range=Optional[Union[Union[dict, ExperimentalCondition], List[Union[dict, ExperimentalCondition]]]])

slots.evidence_codes = Slot(uri=ALLIANCE.evidence_codes, name="evidence_codes", curie=ALLIANCE.curie('evidence_codes'),
                   model_uri=ALLIANCE.evidence_codes, domain=None, range=Optional[Union[Union[str, ECOTermCurie], List[Union[str, ECOTermCurie]]]])

slots.inferred_gene = Slot(uri=ALLIANCE.inferred_gene, name="inferred_gene", curie=ALLIANCE.curie('inferred_gene'),
                   model_uri=ALLIANCE.inferred_gene, domain=None, range=Optional[Union[str, GeneCurie]])

slots.inferred_allele = Slot(uri=ALLIANCE.inferred_allele, name="inferred_allele", curie=ALLIANCE.curie('inferred_allele'),
                   model_uri=ALLIANCE.inferred_allele, domain=None, range=Optional[Union[str, AlleleCurie]])

slots.disease_qualifiers = Slot(uri=ALLIANCE.disease_qualifiers, name="disease_qualifiers", curie=ALLIANCE.curie('disease_qualifiers'),
                   model_uri=ALLIANCE.disease_qualifiers, domain=None, range=Optional[Union[str, "DiseaseAnnotationQualifierEnum"]])

slots.genetic_sex = Slot(uri=ALLIANCE.genetic_sex, name="genetic_sex", curie=ALLIANCE.curie('genetic_sex'),
                   model_uri=ALLIANCE.genetic_sex, domain=None, range=Optional[Union[str, "GeneticSexEnum"]])

slots.private_note = Slot(uri=ALLIANCE.private_note, name="private_note", curie=ALLIANCE.curie('private_note'),
                   model_uri=ALLIANCE.private_note, domain=None, range=Optional[str])

slots.disease_annotation_note = Slot(uri=ALLIANCE.disease_annotation_note, name="disease_annotation_note", curie=ALLIANCE.curie('disease_annotation_note'),
                   model_uri=ALLIANCE.disease_annotation_note, domain=None, range=Optional[str])

slots.disease_annotation_summary = Slot(uri=ALLIANCE.disease_annotation_summary, name="disease_annotation_summary", curie=ALLIANCE.curie('disease_annotation_summary'),
                   model_uri=ALLIANCE.disease_annotation_summary, domain=None, range=Optional[str])

slots.sgd_strain_background = Slot(uri=ALLIANCE.sgd_strain_background, name="sgd_strain_background", curie=ALLIANCE.curie('sgd_strain_background'),
                   model_uri=ALLIANCE.sgd_strain_background, domain=None, range=Optional[Union[str, AffectedGenomicModelCurie]])

slots.annotation_type = Slot(uri=ALLIANCE.annotation_type, name="annotation_type", curie=ALLIANCE.curie('annotation_type'),
                   model_uri=ALLIANCE.annotation_type, domain=None, range=Optional[Union[str, "AnnotationTypeEnum"]])

slots.disease_genetic_modifier = Slot(uri=ALLIANCE.disease_genetic_modifier, name="disease_genetic_modifier", curie=ALLIANCE.curie('disease_genetic_modifier'),
                   model_uri=ALLIANCE.disease_genetic_modifier, domain=None, range=Optional[Union[str, BiologicalEntityCurie]])

slots.disease_genetic_modifier_relation = Slot(uri=ALLIANCE.disease_genetic_modifier_relation, name="disease_genetic_modifier_relation", curie=ALLIANCE.curie('disease_genetic_modifier_relation'),
                   model_uri=ALLIANCE.disease_genetic_modifier_relation, domain=None, range=Optional[Union[str, "GeneticModifierRelationEnum"]])

slots.phenotype_term = Slot(uri=ALLIANCE.phenotype_term, name="phenotype_term", curie=ALLIANCE.curie('phenotype_term'),
                   model_uri=ALLIANCE.phenotype_term, domain=None, range=Optional[Union[str, PhenotypeTermCurie]])

slots.with = Slot(uri=ALLIANCE.with, name="with", curie=ALLIANCE.curie('with'),
                   model_uri=ALLIANCE.with, domain=None, range=Optional[Union[str, GeneCurie]])

slots.mod_id = Slot(uri=ALLIANCE.mod_id, name="mod_id", curie=ALLIANCE.curie('mod_id'),
                   model_uri=ALLIANCE.mod_id, domain=None, range=Optional[str])

slots.paper_handles = Slot(uri=ALLIANCE.paper_handles, name="paper_handles", curie=ALLIANCE.curie('paper_handles'),
                   model_uri=ALLIANCE.paper_handles, domain=None, range=Optional[Union[Union[dict, PaperHandle], List[Union[dict, PaperHandle]]]])

slots.handle = Slot(uri=ALLIANCE.handle, name="handle", curie=ALLIANCE.curie('handle'),
                   model_uri=ALLIANCE.handle, domain=None, range=Optional[str])

slots.has_condition = Slot(uri=ALLIANCE.has_condition, name="has_condition", curie=ALLIANCE.curie('has_condition'),
                   model_uri=ALLIANCE.has_condition, domain=Entity, range=Optional[Union[Union[dict, "ExperimentalCondition"], List[Union[dict, "ExperimentalCondition"]]]])

slots.is_condition_in = Slot(uri=ALLIANCE.is_condition_in, name="is_condition_in", curie=ALLIANCE.curie('is_condition_in'),
                   model_uri=ALLIANCE.is_condition_in, domain=ExperimentalCondition, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.induced_by = Slot(uri=ALLIANCE.induced_by, name="induced_by", curie=ALLIANCE.curie('induced_by'),
                   model_uri=ALLIANCE.induced_by, domain=Entity, range=Optional[Union[Union[dict, "ExperimentalCondition"], List[Union[dict, "ExperimentalCondition"]]]])

slots.induces = Slot(uri=ALLIANCE.induces, name="induces", curie=ALLIANCE.curie('induces'),
                   model_uri=ALLIANCE.induces, domain=ExperimentalCondition, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.ameliorated_by = Slot(uri=ALLIANCE.ameliorated_by, name="ameliorated_by", curie=ALLIANCE.curie('ameliorated_by'),
                   model_uri=ALLIANCE.ameliorated_by, domain=Entity, range=Optional[Union[Union[dict, "ExperimentalCondition"], List[Union[dict, "ExperimentalCondition"]]]])

slots.ameliorates = Slot(uri=ALLIANCE.ameliorates, name="ameliorates", curie=ALLIANCE.curie('ameliorates'),
                   model_uri=ALLIANCE.ameliorates, domain=ExperimentalCondition, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.exacerbated_by = Slot(uri=ALLIANCE.exacerbated_by, name="exacerbated_by", curie=ALLIANCE.curie('exacerbated_by'),
                   model_uri=ALLIANCE.exacerbated_by, domain=Entity, range=Optional[Union[Union[dict, "ExperimentalCondition"], List[Union[dict, "ExperimentalCondition"]]]])

slots.exacerbates = Slot(uri=ALLIANCE.exacerbates, name="exacerbates", curie=ALLIANCE.curie('exacerbates'),
                   model_uri=ALLIANCE.exacerbates, domain=ExperimentalCondition, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.inchi = Slot(uri=ALLIANCE.inchi, name="inchi", curie=ALLIANCE.curie('inchi'),
                   model_uri=ALLIANCE.inchi, domain=Molecule, range=Optional[str])

slots.inchi_key = Slot(uri=ALLIANCE.inchi_key, name="inchi_key", curie=ALLIANCE.curie('inchi_key'),
                   model_uri=ALLIANCE.inchi_key, domain=Molecule, range=Optional[str])

slots.iupac = Slot(uri=ALLIANCE.iupac, name="iupac", curie=ALLIANCE.curie('iupac'),
                   model_uri=ALLIANCE.iupac, domain=Molecule, range=Optional[str])

slots.formula = Slot(uri=ALLIANCE.formula, name="formula", curie=ALLIANCE.curie('formula'),
                   model_uri=ALLIANCE.formula, domain=Molecule, range=Optional[str])

slots.smiles = Slot(uri=ALLIANCE.smiles, name="smiles", curie=ALLIANCE.curie('smiles'),
                   model_uri=ALLIANCE.smiles, domain=Molecule, range=Optional[str])

slots.text_synonyms = Slot(uri="str(uriorcurie)", name="text_synonyms", curie=None,
                   model_uri=ALLIANCE.text_synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.member_terms = Slot(uri="str(uriorcurie)", name="member_terms", curie=None,
                   model_uri=ALLIANCE.member_terms, domain=None, range=Optional[Union[Union[dict, VocabularyTerm], List[Union[dict, VocabularyTerm]]]])

slots.vocabulary_description = Slot(uri="str(uriorcurie)", name="vocabulary_description", curie=None,
                   model_uri=ALLIANCE.vocabulary_description, domain=None, range=Optional[str])

slots.allele_ingest_set = Slot(uri="str(uriorcurie)", name="allele ingest set", curie=None,
                   model_uri=ALLIANCE.allele_ingest_set, domain=Ingest, range=Optional[Union[Union[str, AlleleCurie], List[Union[str, AlleleCurie]]]])

slots.disease_annotation_ingest_set = Slot(uri="str(uriorcurie)", name="disease annotation ingest set", curie=None,
                   model_uri=ALLIANCE.disease_annotation_ingest_set, domain=Ingest, range=Optional[Union[Union[dict, DiseaseAnnotation], List[Union[dict, DiseaseAnnotation]]]])

slots.caption = Slot(uri="str(uriorcurie)", name="caption", curie=None,
                   model_uri=ALLIANCE.caption, domain=Figure, range=Optional[str])

slots.cropped_from = Slot(uri="str(uriorcurie)", name="cropped_from", curie=None,
                   model_uri=ALLIANCE.cropped_from, domain=Image, range=Optional[Union[str, ImageCurie]])

slots.has_figure = Slot(uri="str(uriorcurie)", name="has_figure", curie=None,
                   model_uri=ALLIANCE.has_figure, domain=None, range=Optional[Union[str, FigureCurie]])

slots.height = Slot(uri="str(uriorcurie)", name="height", curie=None,
                   model_uri=ALLIANCE.height, domain=Image, range=int)

slots.image_file = Slot(uri="str(uriorcurie)", name="image_file", curie=None,
                   model_uri=ALLIANCE.image_file, domain=Image, range=Union[dict, File])

slots.image_medium_file = Slot(uri="str(uriorcurie)", name="image_medium_file", curie=None,
                   model_uri=ALLIANCE.image_medium_file, domain=Image, range=Union[dict, File])

slots.image_thumbnail_file = Slot(uri="str(uriorcurie)", name="image_thumbnail_file", curie=None,
                   model_uri=ALLIANCE.image_thumbnail_file, domain=Image, range=Union[dict, File])

slots.image_x_origin = Slot(uri="str(uriorcurie)", name="image_x_origin", curie=None,
                   model_uri=ALLIANCE.image_x_origin, domain=None, range=Optional[int])

slots.image_y_origin = Slot(uri="str(uriorcurie)", name="image_y_origin", curie=None,
                   model_uri=ALLIANCE.image_y_origin, domain=None, range=Optional[int])

slots.images = Slot(uri="str(uriorcurie)", name="images", curie=None,
                   model_uri=ALLIANCE.images, domain=None, range=Optional[Union[str, ImageCurie]])

slots.label = Slot(uri="str(uriorcurie)", name="label", curie=None,
                   model_uri=ALLIANCE.label, domain=None, range=Optional[str])

slots.video_still = Slot(uri="str(uriorcurie)", name="video_still", curie=None,
                   model_uri=ALLIANCE.video_still, domain=Image, range=Optional[Union[bool, Bool]])

slots.width = Slot(uri="str(uriorcurie)", name="width", curie=None,
                   model_uri=ALLIANCE.width, domain=Image, range=int)

slots.id = Slot(uri=ALLIANCE.id, name="id", curie=ALLIANCE.curie('id'),
                   model_uri=ALLIANCE.id, domain=None, range=Optional[str])

slots.cnda_end = Slot(uri=ALLIANCE.cnda_end, name="cnda_end", curie=ALLIANCE.curie('cnda_end'),
                   model_uri=ALLIANCE.cnda_end, domain=None, range=Optional[str])

slots.person_id = Slot(uri=ALLIANCE.person_id, name="person id", curie=ALLIANCE.curie('person_id'),
                   model_uri=ALLIANCE.person_id, domain=None, range=URIRef)

slots.embryonic_cell_lines = Slot(uri=ALLIANCE.embryonic_cell_lines, name="embryonic_cell_lines", curie=ALLIANCE.curie('embryonic_cell_lines'),
                   model_uri=ALLIANCE.embryonic_cell_lines, domain=None, range=Optional[str])

slots.note_type = Slot(uri=ALLIANCE.note_type, name="note_type", curie=ALLIANCE.curie('note_type'),
                   model_uri=ALLIANCE.note_type, domain=None, range=Optional[Union[str, "AntibodyNoteTypeSet"]])

slots.Reference_id = Slot(uri=ALLIANCE.id, name="Reference_id", curie=ALLIANCE.curie('id'),
                   model_uri=ALLIANCE.Reference_id, domain=Reference, range=Optional[str])

slots.Resource_id = Slot(uri=ALLIANCE.id, name="Resource_id", curie=ALLIANCE.curie('id'),
                   model_uri=ALLIANCE.Resource_id, domain=Resource, range=Optional[str])

slots.Resource_title = Slot(uri=ALLIANCE.title, name="Resource_title", curie=ALLIANCE.curie('title'),
                   model_uri=ALLIANCE.Resource_title, domain=Resource, range=Optional[str])

slots.VariantConsequence_subject = Slot(uri=ALLIANCE.subject, name="VariantConsequence_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.VariantConsequence_subject, domain=VariantConsequence, range=Union[str, VariantCurie])

slots.VariantGeneConsequence_object = Slot(uri=ALLIANCE.object, name="VariantGeneConsequence_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.VariantGeneConsequence_object, domain=VariantGeneConsequence, range=Union[str, GeneCurie])

slots.VariantTranscriptConsequence_object = Slot(uri=ALLIANCE.object, name="VariantTranscriptConsequence_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.VariantTranscriptConsequence_object, domain=VariantTranscriptConsequence, range=Union[str, TranscriptCurie])

slots.VariantTranscriptConsequence_amino_acid_reference = Slot(uri="str(uriorcurie)", name="VariantTranscriptConsequence_amino_acid_reference", curie=None,
                   model_uri=ALLIANCE.VariantTranscriptConsequence_amino_acid_reference, domain=VariantTranscriptConsequence, range=Optional[str])

slots.VariantTranscriptConsequence_amino_acid_variant = Slot(uri="str(uriorcurie)", name="VariantTranscriptConsequence_amino_acid_variant", curie=None,
                   model_uri=ALLIANCE.VariantTranscriptConsequence_amino_acid_variant, domain=VariantTranscriptConsequence, range=Optional[str])

slots.VariantTranscriptConsequence_codon_reference = Slot(uri="str(uriorcurie)", name="VariantTranscriptConsequence_codon_reference", curie=None,
                   model_uri=ALLIANCE.VariantTranscriptConsequence_codon_reference, domain=VariantTranscriptConsequence, range=Optional[str])

slots.VariantTranscriptConsequence_codon_variant = Slot(uri="str(uriorcurie)", name="VariantTranscriptConsequence_codon_variant", curie=None,
                   model_uri=ALLIANCE.VariantTranscriptConsequence_codon_variant, domain=VariantTranscriptConsequence, range=Optional[str])

slots.VariantTranscriptConsequence_cdna_start = Slot(uri="str(uriorcurie)", name="VariantTranscriptConsequence_cdna_start", curie=None,
                   model_uri=ALLIANCE.VariantTranscriptConsequence_cdna_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.VariantTranscriptConsequence_cnda_end = Slot(uri=ALLIANCE.cnda_end, name="VariantTranscriptConsequence_cnda_end", curie=ALLIANCE.curie('cnda_end'),
                   model_uri=ALLIANCE.VariantTranscriptConsequence_cnda_end, domain=VariantTranscriptConsequence, range=Optional[str])

slots.VariantTranscriptConsequence_cds_start = Slot(uri="str(uriorcurie)", name="VariantTranscriptConsequence_cds_start", curie=None,
                   model_uri=ALLIANCE.VariantTranscriptConsequence_cds_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.VariantTranscriptConsequence_cds_end = Slot(uri="str(uriorcurie)", name="VariantTranscriptConsequence_cds_end", curie=None,
                   model_uri=ALLIANCE.VariantTranscriptConsequence_cds_end, domain=VariantTranscriptConsequence, range=Optional[int])

slots.VariantTranscriptConsequence_protein_start = Slot(uri="str(uriorcurie)", name="VariantTranscriptConsequence_protein_start", curie=None,
                   model_uri=ALLIANCE.VariantTranscriptConsequence_protein_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.VariantTranscriptConsequence_protein_end = Slot(uri="str(uriorcurie)", name="VariantTranscriptConsequence_protein_end", curie=None,
                   model_uri=ALLIANCE.VariantTranscriptConsequence_protein_end, domain=VariantTranscriptConsequence, range=Optional[int])

slots.VariantTranscriptConsequence_hgvs_protein_nomenclature = Slot(uri="str(uriorcurie)", name="VariantTranscriptConsequence_hgvs_protein_nomenclature", curie=None,
                   model_uri=ALLIANCE.VariantTranscriptConsequence_hgvs_protein_nomenclature, domain=VariantTranscriptConsequence, range=Optional[str])

slots.VariantTranscriptConsequence_hgvs_coding_nomenclature = Slot(uri="str(uriorcurie)", name="VariantTranscriptConsequence_hgvs_coding_nomenclature", curie=None,
                   model_uri=ALLIANCE.VariantTranscriptConsequence_hgvs_coding_nomenclature, domain=VariantTranscriptConsequence, range=Optional[str])

slots.VariantGenomicLocation_subject = Slot(uri=ALLIANCE.subject, name="VariantGenomicLocation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.VariantGenomicLocation_subject, domain=VariantGenomicLocation, range=Union[str, VariantCurie])

slots.VariantGenomicLocation_object = Slot(uri=ALLIANCE.object, name="VariantGenomicLocation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.VariantGenomicLocation_object, domain=VariantGenomicLocation, range=Union[str, ChromosomeCurie])

slots.BiologicalEntity_taxon = Slot(uri=ALLIANCE.taxon, name="BiologicalEntity_taxon", curie=ALLIANCE.curie('taxon'),
                   model_uri=ALLIANCE.BiologicalEntity_taxon, domain=BiologicalEntity, range=Union[str, URIorCURIE])

slots.Gene_symbol = Slot(uri=ALLIANCE.symbol, name="Gene_symbol", curie=ALLIANCE.curie('symbol'),
                   model_uri=ALLIANCE.Gene_symbol, domain=Gene, range=str)

slots.EntitySynonym_object = Slot(uri=ALLIANCE.object, name="EntitySynonym_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.EntitySynonym_object, domain=EntitySynonym, range=Union[dict, Synonym])

slots.EntitySynonym_predicate = Slot(uri=ALLIANCE.predicate, name="EntitySynonym_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.EntitySynonym_predicate, domain=EntitySynonym, range=Union[str, "EntitySynonymTypeSet"])

slots.EntitySynonym_references = Slot(uri=ALLIANCE.references, name="EntitySynonym_references", curie=ALLIANCE.curie('references'),
                   model_uri=ALLIANCE.EntitySynonym_references, domain=EntitySynonym, range=Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]])

slots.GeneGenomicLocation_subject = Slot(uri=ALLIANCE.subject, name="GeneGenomicLocation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.GeneGenomicLocation_subject, domain=GeneGenomicLocation, range=Union[str, VariantCurie])

slots.GeneGenomicLocation_object = Slot(uri=ALLIANCE.object, name="GeneGenomicLocation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.GeneGenomicLocation_object, domain=GeneGenomicLocation, range=Union[str, ChromosomeCurie])

slots.Person_person_id = Slot(uri=ALLIANCE.person_id, name="Person_person id", curie=ALLIANCE.curie('person_id'),
                   model_uri=ALLIANCE.Person_person_id, domain=Person, range=Union[str, PersonPersonId])

slots.Allele_synonyms = Slot(uri=ALLIANCE.synonyms, name="Allele_synonyms", curie=ALLIANCE.curie('synonyms'),
                   model_uri=ALLIANCE.Allele_synonyms, domain=Allele, range=Optional[Union[Union[dict, Synonym], List[Union[dict, Synonym]]]])

slots.Allele_germline_transmission_status = Slot(uri="str(uriorcurie)", name="Allele_germline_transmission_status", curie=None,
                   model_uri=ALLIANCE.Allele_germline_transmission_status, domain=Allele, range=Optional[str])

slots.Allele_parent_cell_line = Slot(uri="str(uriorcurie)", name="Allele_parent_cell_line", curie=None,
                   model_uri=ALLIANCE.Allele_parent_cell_line, domain=Allele, range=Optional[Union[dict, "CellLine"]])

slots.Allele_mutant_cell_lines = Slot(uri="str(uriorcurie)", name="Allele_mutant_cell_lines", curie=None,
                   model_uri=ALLIANCE.Allele_mutant_cell_lines, domain=Allele, range=Optional[Union[Union[dict, "CellLine"], List[Union[dict, "CellLine"]]]])

slots.Allele_embryonic_cell_lines = Slot(uri=ALLIANCE.embryonic_cell_lines, name="Allele_embryonic_cell_lines", curie=ALLIANCE.curie('embryonic_cell_lines'),
                   model_uri=ALLIANCE.Allele_embryonic_cell_lines, domain=Allele, range=Optional[str])

slots.Allele_transposon_insertion = Slot(uri="str(uriorcurie)", name="Allele_transposon_insertion", curie=None,
                   model_uri=ALLIANCE.Allele_transposon_insertion, domain=Allele, range=Optional[str])

slots.Allele_aberration = Slot(uri="str(uriorcurie)", name="Allele_aberration", curie=None,
                   model_uri=ALLIANCE.Allele_aberration, domain=Allele, range=Optional[str])

slots.MolecularMutation_mutation_type = Slot(uri="str(uriorcurie)", name="MolecularMutation_mutation_type", curie=None,
                   model_uri=ALLIANCE.MolecularMutation_mutation_type, domain=MolecularMutation, range=Union[str, SOTermCurie])

slots.Antibody_curie = Slot(uri=ALLIANCE.curie, name="Antibody_curie", curie=ALLIANCE.curie('curie'),
                   model_uri=ALLIANCE.Antibody_curie, domain=Antibody, range=Union[str, AntibodyCurie])

slots.Antibody_name = Slot(uri=ALLIANCE.name, name="Antibody_name", curie=ALLIANCE.curie('name'),
                   model_uri=ALLIANCE.Antibody_name, domain=Antibody, range=str)

slots.Antibody_taxon = Slot(uri=ALLIANCE.taxon, name="Antibody_taxon", curie=ALLIANCE.curie('taxon'),
                   model_uri=ALLIANCE.Antibody_taxon, domain=Antibody, range=Optional[Union[str, URIorCURIE]])

slots.Antibody_original_reference = Slot(uri=ALLIANCE.original_reference, name="Antibody_original_reference", curie=ALLIANCE.curie('original_reference'),
                   model_uri=ALLIANCE.Antibody_original_reference, domain=Antibody, range=Optional[Union[str, ReferenceCurie]])

slots.AntibodyNote_note_type = Slot(uri=ALLIANCE.note_type, name="AntibodyNote_note_type", curie=ALLIANCE.curie('note_type'),
                   model_uri=ALLIANCE.AntibodyNote_note_type, domain=AntibodyNote, range=Optional[Union[str, "AntibodyNoteTypeSet"]])

slots.GeneToGeneAssociation_subject = Slot(uri=ALLIANCE.subject, name="GeneToGeneAssociation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.GeneToGeneAssociation_subject, domain=GeneToGeneAssociation, range=Union[str, GeneCurie])

slots.GeneToGeneAssociation_object = Slot(uri=ALLIANCE.object, name="GeneToGeneAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.GeneToGeneAssociation_object, domain=GeneToGeneAssociation, range=Union[str, GeneCurie])

slots.GeneInteraction_curie = Slot(uri=ALLIANCE.curie, name="GeneInteraction_curie", curie=ALLIANCE.curie('curie'),
                   model_uri=ALLIANCE.GeneInteraction_curie, domain=GeneInteraction, range=Union[str, GeneInteractionCurie])

slots.GeneInteraction_cross_references = Slot(uri=ALLIANCE.cross_references, name="GeneInteraction_cross_references", curie=ALLIANCE.curie('cross_references'),
                   model_uri=ALLIANCE.GeneInteraction_cross_references, domain=GeneInteraction, range=Optional[Union[Dict[Union[str, CrossReferenceCurie], Union[dict, CrossReference]], List[Union[dict, CrossReference]]]])

slots.GeneInteraction_subject = Slot(uri=ALLIANCE.subject, name="GeneInteraction_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.GeneInteraction_subject, domain=GeneInteraction, range=Union[str, GeneCurie])

slots.GeneInteraction_predicate = Slot(uri=ALLIANCE.predicate, name="GeneInteraction_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.GeneInteraction_predicate, domain=GeneInteraction, range=str)

slots.GeneInteraction_object = Slot(uri=ALLIANCE.object, name="GeneInteraction_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.GeneInteraction_object, domain=GeneInteraction, range=Union[str, GeneCurie])

slots.GeneInteraction_interaction_data_provider = Slot(uri=ALLIANCE.interaction_data_provider, name="GeneInteraction_interaction_data_provider", curie=ALLIANCE.curie('interaction_data_provider'),
                   model_uri=ALLIANCE.GeneInteraction_interaction_data_provider, domain=GeneInteraction, range=Union[str, "InteractionSourceEnum"])

slots.GeneInteraction_references = Slot(uri=ALLIANCE.references, name="GeneInteraction_references", curie=ALLIANCE.curie('references'),
                   model_uri=ALLIANCE.GeneInteraction_references, domain=GeneInteraction, range=Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]])

slots.GeneMolecularInteraction_aggregation_database = Slot(uri=ALLIANCE.aggregation_database, name="GeneMolecularInteraction_aggregation_database", curie=ALLIANCE.curie('aggregation_database'),
                   model_uri=ALLIANCE.GeneMolecularInteraction_aggregation_database, domain=GeneMolecularInteraction, range=Optional[Union[str, "AggregationDatabaseEnum"]])

slots.GeneMolecularInteraction_detection_method = Slot(uri=ALLIANCE.detection_method, name="GeneMolecularInteraction_detection_method", curie=ALLIANCE.curie('detection_method'),
                   model_uri=ALLIANCE.GeneMolecularInteraction_detection_method, domain=GeneMolecularInteraction, range=Optional[Union[str, "DetectionMethodsEnum"]])

slots.GeneMolecularInteraction_predicate = Slot(uri=ALLIANCE.predicate, name="GeneMolecularInteraction_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.GeneMolecularInteraction_predicate, domain=GeneMolecularInteraction, range=str)

slots.GeneGeneticInteraction_predicate = Slot(uri=ALLIANCE.predicate, name="GeneGeneticInteraction_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.GeneGeneticInteraction_predicate, domain=GeneGeneticInteraction, range=str)

slots.OntologyTerm_definition = Slot(uri="str(uriorcurie)", name="OntologyTerm_definition", curie=None,
                   model_uri=ALLIANCE.OntologyTerm_definition, domain=OntologyTerm, range=Optional[str])

slots.ECOTerm_abbreviation = Slot(uri=ALLIANCE.abbreviation, name="ECOTerm_abbreviation", curie=ALLIANCE.curie('abbreviation'),
                   model_uri=ALLIANCE.ECOTerm_abbreviation, domain=ECOTerm, range=Optional[str])

slots.PhenotypeAnnotation_subject = Slot(uri=ALLIANCE.subject, name="PhenotypeAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.PhenotypeAnnotation_subject, domain=PhenotypeAnnotation, range=Union[str, BiologicalEntityCurie])

slots.PhenotypeAnnotation_phenotype_term = Slot(uri=ALLIANCE.phenotype_term, name="PhenotypeAnnotation_phenotype_term", curie=ALLIANCE.curie('phenotype_term'),
                   model_uri=ALLIANCE.PhenotypeAnnotation_phenotype_term, domain=PhenotypeAnnotation, range=Optional[Union[str, PhenotypeTermCurie]])

slots.PhenotypeAnnotation_object = Slot(uri=ALLIANCE.object, name="PhenotypeAnnotation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.PhenotypeAnnotation_object, domain=PhenotypeAnnotation, range=str)

slots.PhenotypeAnnotation_reference = Slot(uri=ALLIANCE.reference, name="PhenotypeAnnotation_reference", curie=ALLIANCE.curie('reference'),
                   model_uri=ALLIANCE.PhenotypeAnnotation_reference, domain=PhenotypeAnnotation, range=Optional[Union[str, ReferenceCurie]])

slots.PhenotypeAnnotation_creation_date = Slot(uri=ALLIANCE.creation_date, name="PhenotypeAnnotation_creation_date", curie=ALLIANCE.curie('creation_date'),
                   model_uri=ALLIANCE.PhenotypeAnnotation_creation_date, domain=PhenotypeAnnotation, range=Union[str, XSDDate])

slots.GenePhenotypeAnnotation_subject = Slot(uri=ALLIANCE.subject, name="GenePhenotypeAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.GenePhenotypeAnnotation_subject, domain=GenePhenotypeAnnotation, range=Union[str, GeneCurie])

slots.AllelePhenotypeAnnotation_subject = Slot(uri=ALLIANCE.subject, name="AllelePhenotypeAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.AllelePhenotypeAnnotation_subject, domain=AllelePhenotypeAnnotation, range=Union[str, AlleleCurie])

slots.AllelePhenotypeAnnotation_inferred_gene = Slot(uri=ALLIANCE.inferred_gene, name="AllelePhenotypeAnnotation_inferred_gene", curie=ALLIANCE.curie('inferred_gene'),
                   model_uri=ALLIANCE.AllelePhenotypeAnnotation_inferred_gene, domain=AllelePhenotypeAnnotation, range=Optional[Union[str, GeneCurie]])

slots.AGMPhenotypeAnnotation_subject = Slot(uri=ALLIANCE.subject, name="AGMPhenotypeAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.AGMPhenotypeAnnotation_subject, domain=AGMPhenotypeAnnotation, range=Union[str, AffectedGenomicModelCurie])

slots.AGMPhenotypeAnnotation_inferred_gene = Slot(uri=ALLIANCE.inferred_gene, name="AGMPhenotypeAnnotation_inferred_gene", curie=ALLIANCE.curie('inferred_gene'),
                   model_uri=ALLIANCE.AGMPhenotypeAnnotation_inferred_gene, domain=AGMPhenotypeAnnotation, range=Optional[Union[str, GeneCurie]])

slots.AGMPhenotypeAnnotation_inferred_allele = Slot(uri=ALLIANCE.inferred_allele, name="AGMPhenotypeAnnotation_inferred_allele", curie=ALLIANCE.curie('inferred_allele'),
                   model_uri=ALLIANCE.AGMPhenotypeAnnotation_inferred_allele, domain=AGMPhenotypeAnnotation, range=Optional[Union[str, AlleleCurie]])

slots.DiseaseAnnotation_unique_id = Slot(uri=ALLIANCE.unique_id, name="DiseaseAnnotation_unique_id", curie=ALLIANCE.curie('unique_id'),
                   model_uri=ALLIANCE.DiseaseAnnotation_unique_id, domain=DiseaseAnnotation, range=Optional[str])

slots.DiseaseAnnotation_mod_id = Slot(uri=ALLIANCE.mod_id, name="DiseaseAnnotation_mod_id", curie=ALLIANCE.curie('mod_id'),
                   model_uri=ALLIANCE.DiseaseAnnotation_mod_id, domain=DiseaseAnnotation, range=Optional[str])

slots.DiseaseAnnotation_subject = Slot(uri=ALLIANCE.subject, name="DiseaseAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.DiseaseAnnotation_subject, domain=DiseaseAnnotation, range=Union[str, BiologicalEntityCurie])

slots.DiseaseAnnotation_predicate = Slot(uri=ALLIANCE.predicate, name="DiseaseAnnotation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.DiseaseAnnotation_predicate, domain=DiseaseAnnotation, range=str)

slots.DiseaseAnnotation_negated = Slot(uri=ALLIANCE.negated, name="DiseaseAnnotation_negated", curie=ALLIANCE.curie('negated'),
                   model_uri=ALLIANCE.DiseaseAnnotation_negated, domain=DiseaseAnnotation, range=Optional[Union[bool, Bool]])

slots.DiseaseAnnotation_object = Slot(uri=ALLIANCE.object, name="DiseaseAnnotation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.DiseaseAnnotation_object, domain=DiseaseAnnotation, range=Union[str, DOTermCurie])

slots.DiseaseAnnotation_data_provider = Slot(uri=ALLIANCE.data_provider, name="DiseaseAnnotation_data_provider", curie=ALLIANCE.curie('data_provider'),
                   model_uri=ALLIANCE.DiseaseAnnotation_data_provider, domain=DiseaseAnnotation, range=Union[str, List[str]])

slots.DiseaseAnnotation_annotation_type = Slot(uri=ALLIANCE.annotation_type, name="DiseaseAnnotation_annotation_type", curie=ALLIANCE.curie('annotation_type'),
                   model_uri=ALLIANCE.DiseaseAnnotation_annotation_type, domain=DiseaseAnnotation, range=Optional[Union[str, "AnnotationTypeEnum"]])

slots.DiseaseAnnotation_with = Slot(uri=ALLIANCE.with, name="DiseaseAnnotation_with", curie=ALLIANCE.curie('with'),
                   model_uri=ALLIANCE.DiseaseAnnotation_with, domain=DiseaseAnnotation, range=Optional[Union[str, GeneCurie]])

slots.DiseaseAnnotation_reference = Slot(uri=ALLIANCE.reference, name="DiseaseAnnotation_reference", curie=ALLIANCE.curie('reference'),
                   model_uri=ALLIANCE.DiseaseAnnotation_reference, domain=DiseaseAnnotation, range=Union[str, ReferenceCurie])

slots.DiseaseAnnotation_evidence_codes = Slot(uri=ALLIANCE.evidence_codes, name="DiseaseAnnotation_evidence_codes", curie=ALLIANCE.curie('evidence_codes'),
                   model_uri=ALLIANCE.DiseaseAnnotation_evidence_codes, domain=DiseaseAnnotation, range=Union[Union[str, ECOTermCurie], List[Union[str, ECOTermCurie]]])

slots.DiseaseAnnotation_genetic_sex = Slot(uri=ALLIANCE.genetic_sex, name="DiseaseAnnotation_genetic_sex", curie=ALLIANCE.curie('genetic_sex'),
                   model_uri=ALLIANCE.DiseaseAnnotation_genetic_sex, domain=DiseaseAnnotation, range=Optional[Union[str, "GeneticSexEnum"]])

slots.GeneDiseaseAnnotation_subject = Slot(uri=ALLIANCE.subject, name="GeneDiseaseAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.GeneDiseaseAnnotation_subject, domain=GeneDiseaseAnnotation, range=Union[str, GeneCurie])

slots.GeneDiseaseAnnotation_predicate = Slot(uri=ALLIANCE.predicate, name="GeneDiseaseAnnotation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.GeneDiseaseAnnotation_predicate, domain=GeneDiseaseAnnotation, range=Union[str, "GeneDiseaseRelationEnum"])

slots.AlleleDiseaseAnnotation_subject = Slot(uri=ALLIANCE.subject, name="AlleleDiseaseAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.AlleleDiseaseAnnotation_subject, domain=AlleleDiseaseAnnotation, range=Union[str, AlleleCurie])

slots.AlleleDiseaseAnnotation_predicate = Slot(uri=ALLIANCE.predicate, name="AlleleDiseaseAnnotation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.AlleleDiseaseAnnotation_predicate, domain=AlleleDiseaseAnnotation, range=Union[str, "AlleleDiseaseRelationEnum"])

slots.AlleleDiseaseAnnotation_inferred_gene = Slot(uri=ALLIANCE.inferred_gene, name="AlleleDiseaseAnnotation_inferred_gene", curie=ALLIANCE.curie('inferred_gene'),
                   model_uri=ALLIANCE.AlleleDiseaseAnnotation_inferred_gene, domain=AlleleDiseaseAnnotation, range=Optional[Union[str, GeneCurie]])

slots.AGMDiseaseAnnotation_subject = Slot(uri=ALLIANCE.subject, name="AGMDiseaseAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.AGMDiseaseAnnotation_subject, domain=AGMDiseaseAnnotation, range=Union[str, AffectedGenomicModelCurie])

slots.AGMDiseaseAnnotation_predicate = Slot(uri=ALLIANCE.predicate, name="AGMDiseaseAnnotation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.AGMDiseaseAnnotation_predicate, domain=AGMDiseaseAnnotation, range=Union[str, "AgmDiseaseRelationEnum"])

slots.AGMDiseaseAnnotation_inferred_gene = Slot(uri=ALLIANCE.inferred_gene, name="AGMDiseaseAnnotation_inferred_gene", curie=ALLIANCE.curie('inferred_gene'),
                   model_uri=ALLIANCE.AGMDiseaseAnnotation_inferred_gene, domain=AGMDiseaseAnnotation, range=Optional[Union[str, GeneCurie]])

slots.AGMDiseaseAnnotation_inferred_allele = Slot(uri=ALLIANCE.inferred_allele, name="AGMDiseaseAnnotation_inferred_allele", curie=ALLIANCE.curie('inferred_allele'),
                   model_uri=ALLIANCE.AGMDiseaseAnnotation_inferred_allele, domain=AGMDiseaseAnnotation, range=Optional[Union[str, AlleleCurie]])

slots.ExperimentalCondition_unique_id = Slot(uri=ALLIANCE.unique_id, name="ExperimentalCondition_unique_id", curie=ALLIANCE.curie('unique_id'),
                   model_uri=ALLIANCE.ExperimentalCondition_unique_id, domain=ExperimentalCondition, range=Optional[str])

slots.ExperimentalCondition_condition_class = Slot(uri=ALLIANCE.condition_class, name="ExperimentalCondition_condition_class", curie=ALLIANCE.curie('condition_class'),
                   model_uri=ALLIANCE.ExperimentalCondition_condition_class, domain=ExperimentalCondition, range=Union[str, ZECOTermCurie])

slots.ExperimentalCondition_condition_statement = Slot(uri=ALLIANCE.condition_statement, name="ExperimentalCondition_condition_statement", curie=ALLIANCE.curie('condition_statement'),
                   model_uri=ALLIANCE.ExperimentalCondition_condition_statement, domain=ExperimentalCondition, range=str)

slots.ExperimentalCondition_condition_id = Slot(uri=ALLIANCE.condition_id, name="ExperimentalCondition_condition_id", curie=ALLIANCE.curie('condition_id'),
                   model_uri=ALLIANCE.ExperimentalCondition_condition_id, domain=ExperimentalCondition, range=Optional[Union[str, ExperimentalConditionOntologyTermCurie]])

slots.ExperimentalCondition_condition_quantity = Slot(uri=ALLIANCE.condition_quantity, name="ExperimentalCondition_condition_quantity", curie=ALLIANCE.curie('condition_quantity'),
                   model_uri=ALLIANCE.ExperimentalCondition_condition_quantity, domain=ExperimentalCondition, range=Optional[str])

slots.ExperimentalCondition_condition_anatomy = Slot(uri=ALLIANCE.condition_anatomy, name="ExperimentalCondition_condition_anatomy", curie=ALLIANCE.curie('condition_anatomy'),
                   model_uri=ALLIANCE.ExperimentalCondition_condition_anatomy, domain=ExperimentalCondition, range=Optional[Union[str, AnatomicalTermCurie]])

slots.ExperimentalCondition_condition_gene_ontology = Slot(uri=ALLIANCE.condition_gene_ontology, name="ExperimentalCondition_condition_gene_ontology", curie=ALLIANCE.curie('condition_gene_ontology'),
                   model_uri=ALLIANCE.ExperimentalCondition_condition_gene_ontology, domain=ExperimentalCondition, range=Optional[Union[str, GOTermCurie]])

slots.ExperimentalCondition_condition_taxon = Slot(uri=ALLIANCE.condition_taxon, name="ExperimentalCondition_condition_taxon", curie=ALLIANCE.curie('condition_taxon'),
                   model_uri=ALLIANCE.ExperimentalCondition_condition_taxon, domain=ExperimentalCondition, range=Optional[Union[str, OntologyTermCurie]])

slots.ExperimentalCondition_condition_chemical = Slot(uri=ALLIANCE.condition_chemical, name="ExperimentalCondition_condition_chemical", curie=ALLIANCE.curie('condition_chemical'),
                   model_uri=ALLIANCE.ExperimentalCondition_condition_chemical, domain=ExperimentalCondition, range=Optional[Union[str, OntologyTermCurie]])

slots.ExperimentalCondition_paper_handles = Slot(uri=ALLIANCE.paper_handles, name="ExperimentalCondition_paper_handles", curie=ALLIANCE.curie('paper_handles'),
                   model_uri=ALLIANCE.ExperimentalCondition_paper_handles, domain=ExperimentalCondition, range=Optional[Union[Union[dict, "PaperHandle"], List[Union[dict, "PaperHandle"]]]])

slots.ConditionRelation_unique_id = Slot(uri=ALLIANCE.unique_id, name="ConditionRelation_unique_id", curie=ALLIANCE.curie('unique_id'),
                   model_uri=ALLIANCE.ConditionRelation_unique_id, domain=ConditionRelation, range=Optional[str])

slots.ConditionRelation_condition_relation_type = Slot(uri=ALLIANCE.condition_relation_type, name="ConditionRelation_condition_relation_type", curie=ALLIANCE.curie('condition_relation_type'),
                   model_uri=ALLIANCE.ConditionRelation_condition_relation_type, domain=ConditionRelation, range=Union[str, "ConditionRelationEnum"])

slots.Molecule_name = Slot(uri=ALLIANCE.name, name="Molecule_name", curie=ALLIANCE.curie('name'),
                   model_uri=ALLIANCE.Molecule_name, domain=Molecule, range=str)

slots.PaperHandle_reference = Slot(uri=ALLIANCE.reference, name="PaperHandle_reference", curie=ALLIANCE.curie('reference'),
                   model_uri=ALLIANCE.PaperHandle_reference, domain=PaperHandle, range=Union[str, ReferenceCurie])

slots.PaperHandle_handle = Slot(uri=ALLIANCE.handle, name="PaperHandle_handle", curie=ALLIANCE.curie('handle'),
                   model_uri=ALLIANCE.PaperHandle_handle, domain=PaperHandle, range=str)

slots.VocabularyTerm_name = Slot(uri=ALLIANCE.name, name="VocabularyTerm_name", curie=ALLIANCE.curie('name'),
                   model_uri=ALLIANCE.VocabularyTerm_name, domain=VocabularyTerm, range=str)

slots.Vocabulary_name = Slot(uri=ALLIANCE.name, name="Vocabulary_name", curie=ALLIANCE.curie('name'),
                   model_uri=ALLIANCE.Vocabulary_name, domain=Vocabulary, range=Union[str, VocabularyName])

slots.Figure_has_reference = Slot(uri="str(uriorcurie)", name="Figure_has_reference", curie=None,
                   model_uri=ALLIANCE.Figure_has_reference, domain=Figure, range=Union[str, ReferenceCurie])

slots.Image_has_figure = Slot(uri="str(uriorcurie)", name="Image_has_figure", curie=None,
                   model_uri=ALLIANCE.Image_has_figure, domain=Image, range=Union[str, FigureCurie])

slots.Image_image_x_origin = Slot(uri="str(uriorcurie)", name="Image_image_x_origin", curie=None,
                   model_uri=ALLIANCE.Image_image_x_origin, domain=Image, range=Optional[int])

slots.Image_image_y_origin = Slot(uri="str(uriorcurie)", name="Image_image_y_origin", curie=None,
                   model_uri=ALLIANCE.Image_image_y_origin, domain=Image, range=Optional[int])

slots.ImagePane_images = Slot(uri="str(uriorcurie)", name="ImagePane_images", curie=None,
                   model_uri=ALLIANCE.ImagePane_images, domain=ImagePane, range=Union[str, ImageCurie])

slots.ImagePane_image_x_origin = Slot(uri="str(uriorcurie)", name="ImagePane_image_x_origin", curie=None,
                   model_uri=ALLIANCE.ImagePane_image_x_origin, domain=ImagePane, range=Optional[int])

slots.ImagePane_image_y_origin = Slot(uri="str(uriorcurie)", name="ImagePane_image_y_origin", curie=None,
                   model_uri=ALLIANCE.ImagePane_image_y_origin, domain=ImagePane, range=Optional[int])
