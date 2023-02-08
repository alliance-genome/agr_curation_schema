# Auto generated from geneInteraction.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-02-08T15:05:33
# Schema: Alliance-Gene-Interaction-Schema-Prototype
#
# id: https://github.com/alliance-genome/agr_persistent_schema/geneInteraction.yaml
# description: Alliance Gene Interaction Schema Prototype with LinkML
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
from linkml_runtime.linkml_model.types import Boolean, Date, Datetime, Float, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URI, URIorCURIE, XSDDate, XSDDateTime

metamodel_version = "1.7.0"
version = None

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
ALLIANCE = CurieNamespace('alliance', 'http://alliancegenome.org/')
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


class BiologicalEntityDTOCurie(URIorCURIE):
    pass


class GenomicEntityCurie(BiologicalEntityCurie):
    pass


class AlleleCurie(GenomicEntityCurie):
    pass


class CellLineCurie(GenomicEntityCurie):
    pass


class ConstructCurie(GenomicEntityCurie):
    pass


class ConstructComponentCurie(GenomicEntityCurie):
    pass


class SequenceTargetingReagentCurie(GenomicEntityCurie):
    pass


class GenomicEntityDTOCurie(BiologicalEntityDTOCurie):
    pass


class TranscriptCurie(GenomicEntityCurie):
    pass


class GeneInteractionCurie(URIorCURIE):
    pass


class GeneMolecularInteractionCurie(GeneInteractionCurie):
    pass


class GeneGeneticInteractionCurie(GeneInteractionCurie):
    pass


class ChromosomeCurie(URIorCURIE):
    pass


class AssemblyCurie(URIorCURIE):
    pass


class ProteinCurie(GenomicEntityCurie):
    pass


class IdentifierCurie(URIorCURIE):
    pass


class GeneCurie(GenomicEntityCurie):
    pass


class GeneDTOCurie(GenomicEntityDTOCurie):
    pass


class GeneticMapPositionCurie(GenomicEntityCurie):
    pass


class InformationContentEntityCurie(URIorCURIE):
    pass


class ReferenceCurie(InformationContentEntityCurie):
    pass


class PersonalCommunicationCurie(InformationContentEntityCurie):
    pass


class AffectedGenomicModelCurie(GenomicEntityCurie):
    pass


class AffectedGenomicModelDTOCurie(GenomicEntityDTOCurie):
    pass


class LaboratoryCurie(URIorCURIE):
    pass


class PersonUniqueId(extended_str):
    pass


class LoggedInPersonUniqueId(PersonUniqueId):
    pass


class FigureCurie(URIorCURIE):
    pass


class ImageCurie(URIorCURIE):
    pass


class VocabularyTermName(extended_str):
    pass


class VocabularyName(extended_str):
    pass


class VocabularyTermSetName(extended_str):
    pass


class VariantCurie(GenomicEntityCurie):
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


class MPTermCurie(PhenotypeTermCurie):
    pass


class ATPTermCurie(OntologyTermCurie):
    pass


class ChemicalTermCurie(OntologyTermCurie):
    pass


class CHEBITermCurie(ChemicalTermCurie):
    pass


class XSMOTermCurie(ChemicalTermCurie):
    pass


class MoleculeCurie(ChemicalTermCurie):
    pass


class PhenotypeAnnotationCurie(URIorCURIE):
    pass


class GenePhenotypeAnnotationCurie(PhenotypeAnnotationCurie):
    pass


class AllelePhenotypeAnnotationCurie(PhenotypeAnnotationCurie):
    pass


class AGMPhenotypeAnnotationCurie(PhenotypeAnnotationCurie):
    pass


class DiseaseAnnotationCurie(URIorCURIE):
    pass


class GeneDiseaseAnnotationCurie(DiseaseAnnotationCurie):
    pass


class AlleleDiseaseAnnotationCurie(DiseaseAnnotationCurie):
    pass


class AGMDiseaseAnnotationCurie(DiseaseAnnotationCurie):
    pass


class ResourceCurie(URIorCURIE):
    pass


class AlleleDTOCurie(GenomicEntityDTOCurie):
    pass


class CellLineDTOCurie(GenomicEntityDTOCurie):
    pass


class ConstructDTOCurie(GenomicEntityDTOCurie):
    pass


class SequenceTargetingReagentDTOCurie(GenomicEntityDTOCurie):
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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AuditedObject

    internal: Union[bool, Bool] = None
    created_by: Optional[Union[str, PersonUniqueId]] = None
    date_created: Optional[Union[str, XSDDateTime]] = None
    updated_by: Optional[Union[str, PersonUniqueId]] = None
    date_updated: Optional[Union[str, XSDDateTime]] = None
    db_date_created: Optional[Union[str, XSDDateTime]] = None
    db_date_updated: Optional[Union[str, XSDDateTime]] = None
    obsolete: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.internal):
            self.MissingRequiredField("internal")
        if not isinstance(self.internal, Bool):
            self.internal = Bool(self.internal)

        if self.created_by is not None and not isinstance(self.created_by, PersonUniqueId):
            self.created_by = PersonUniqueId(self.created_by)

        if self.date_created is not None and not isinstance(self.date_created, XSDDateTime):
            self.date_created = XSDDateTime(self.date_created)

        if self.updated_by is not None and not isinstance(self.updated_by, PersonUniqueId):
            self.updated_by = PersonUniqueId(self.updated_by)

        if self.date_updated is not None and not isinstance(self.date_updated, XSDDateTime):
            self.date_updated = XSDDateTime(self.date_updated)

        if self.db_date_created is not None and not isinstance(self.db_date_created, XSDDateTime):
            self.db_date_created = XSDDateTime(self.db_date_created)

        if self.db_date_updated is not None and not isinstance(self.db_date_updated, XSDDateTime):
            self.db_date_updated = XSDDateTime(self.db_date_updated)

        if self.obsolete is not None and not isinstance(self.obsolete, Bool):
            self.obsolete = Bool(self.obsolete)

        super().__post_init__(**kwargs)


@dataclass
class GenerationMethod(AuditedObject):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GenerationMethod
    class_class_curie: ClassVar[str] = "alliance:GenerationMethod"
    class_name: ClassVar[str] = "GenerationMethod"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GenerationMethod

    internal: Union[bool, Bool] = None
    mutagenesis_methods: Optional[Union[Union[str, VocabularyTermName], List[Union[str, VocabularyTermName]]]] = empty_list()
    mutagenesis_target: Optional[str] = None
    integration_method: Optional[Union[str, VocabularyTermName]] = None
    chemical_mutagen: Optional[Union[str, VocabularyTermName]] = None
    irradiation_mutagen: Optional[Union[str, VocabularyTermName]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.mutagenesis_methods, list):
            self.mutagenesis_methods = [self.mutagenesis_methods] if self.mutagenesis_methods is not None else []
        self.mutagenesis_methods = [v if isinstance(v, VocabularyTermName) else VocabularyTermName(v) for v in self.mutagenesis_methods]

        if self.mutagenesis_target is not None and not isinstance(self.mutagenesis_target, str):
            self.mutagenesis_target = str(self.mutagenesis_target)

        if self.integration_method is not None and not isinstance(self.integration_method, VocabularyTermName):
            self.integration_method = VocabularyTermName(self.integration_method)

        if self.chemical_mutagen is not None and not isinstance(self.chemical_mutagen, VocabularyTermName):
            self.chemical_mutagen = VocabularyTermName(self.chemical_mutagen)

        if self.irradiation_mutagen is not None and not isinstance(self.irradiation_mutagen, VocabularyTermName):
            self.irradiation_mutagen = VocabularyTermName(self.irradiation_mutagen)

        super().__post_init__(**kwargs)


@dataclass
class AuditedObjectDTO(YAMLRoot):
    """
    Base class for all other LinkML DTO classes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AuditedObjectDTO
    class_class_curie: ClassVar[str] = "alliance:AuditedObjectDTO"
    class_name: ClassVar[str] = "AuditedObjectDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AuditedObjectDTO

    internal: Union[bool, Bool] = None
    created_by_curie: Optional[str] = None
    date_created: Optional[Union[str, XSDDateTime]] = None
    updated_by_curie: Optional[str] = None
    date_updated: Optional[Union[str, XSDDateTime]] = None
    db_date_created: Optional[Union[str, XSDDateTime]] = None
    db_date_updated: Optional[Union[str, XSDDateTime]] = None
    obsolete: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.internal):
            self.MissingRequiredField("internal")
        if not isinstance(self.internal, Bool):
            self.internal = Bool(self.internal)

        if self.created_by_curie is not None and not isinstance(self.created_by_curie, str):
            self.created_by_curie = str(self.created_by_curie)

        if self.date_created is not None and not isinstance(self.date_created, XSDDateTime):
            self.date_created = XSDDateTime(self.date_created)

        if self.updated_by_curie is not None and not isinstance(self.updated_by_curie, str):
            self.updated_by_curie = str(self.updated_by_curie)

        if self.date_updated is not None and not isinstance(self.date_updated, XSDDateTime):
            self.date_updated = XSDDateTime(self.date_updated)

        if self.db_date_created is not None and not isinstance(self.db_date_created, XSDDateTime):
            self.db_date_created = XSDDateTime(self.db_date_created)

        if self.db_date_updated is not None and not isinstance(self.db_date_updated, XSDDateTime):
            self.db_date_updated = XSDDateTime(self.db_date_updated)

        if self.obsolete is not None and not isinstance(self.obsolete, Bool):
            self.obsolete = Bool(self.obsolete)

        super().__post_init__(**kwargs)


@dataclass
class BiologicalEntity(AuditedObject):
    """
    An entity of biological origin that can be unambiguously attributed to a single species.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.BiologicalEntity
    class_class_curie: ClassVar[str] = "alliance:BiologicalEntity"
    class_name: ClassVar[str] = "BiologicalEntity"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.BiologicalEntity

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
class BiologicalEntityDTO(AuditedObjectDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.BiologicalEntityDTO
    class_class_curie: ClassVar[str] = "alliance:BiologicalEntityDTO"
    class_name: ClassVar[str] = "BiologicalEntityDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.BiologicalEntityDTO

    curie: Union[str, BiologicalEntityDTOCurie] = None
    internal: Union[bool, Bool] = None
    taxon_curie: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, BiologicalEntityDTOCurie):
            self.curie = BiologicalEntityDTOCurie(self.curie)

        if self._is_empty(self.taxon_curie):
            self.MissingRequiredField("taxon_curie")
        if not isinstance(self.taxon_curie, str):
            self.taxon_curie = str(self.taxon_curie)

        super().__post_init__(**kwargs)


@dataclass
class GenomicEntity(BiologicalEntity):
    """
    An entity that is part of a genome (i.e. segment of the DNA molecule), is derived directly from the genome (i.e.
    RNA transcript molecule), or is derived indirectly from the genome (i.e. polypeptide or protein via RNA transcript
    translation).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GenomicEntity
    class_class_curie: ClassVar[str] = "alliance:GenomicEntity"
    class_name: ClassVar[str] = "GenomicEntity"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GenomicEntity

    curie: Union[str, GenomicEntityCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None
    cross_references: Optional[Union[Union[dict, "CrossReference"], List[Union[dict, "CrossReference"]]]] = empty_list()
    secondary_identifiers: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    genomic_location_associations: Optional[Union[Union[dict, "GenomicLocationAssociation"], List[Union[dict, "GenomicLocationAssociation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, GenomicEntityCurie):
            self.curie = GenomicEntityCurie(self.curie)

        self._normalize_inlined_as_dict(slot_name="cross_references", slot_type=CrossReference, key_name="internal", keyed=False)

        if not isinstance(self.secondary_identifiers, list):
            self.secondary_identifiers = [self.secondary_identifiers] if self.secondary_identifiers is not None else []
        self.secondary_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.secondary_identifiers]

        self._normalize_inlined_as_dict(slot_name="genomic_location_associations", slot_type=GenomicLocationAssociation, key_name="internal", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class Allele(GenomicEntity):
    """
    One of multiple possible forms of a functional genomic element (most often described as a locus or gene),
    differing from the reference DNA sequence. The genomic element can be endogenous or constructed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Allele
    class_class_curie: ClassVar[str] = "alliance:Allele"
    class_name: ClassVar[str] = "Allele"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Allele

    curie: Union[str, AlleleCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None
    allele_symbol: Union[dict, "AlleleSymbolSlotAnnotation"] = None
    allele_full_name: Optional[Union[dict, "AlleleFullNameSlotAnnotation"]] = None
    references: Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]] = empty_list()
    in_collection: Optional[Union[str, VocabularyTermName]] = None
    laboratory_of_origin: Optional[Union[str, LaboratoryCurie]] = None
    is_extinct: Optional[Union[bool, Bool]] = None
    is_extrachromosomal: Optional[Union[bool, Bool]] = None
    is_integrated: Optional[Union[bool, Bool]] = None
    transgene_chromosome_location: Optional[Union[str, ChromosomeCurie]] = None
    allele_mutation_types: Optional[Union[Union[dict, "AlleleMutationTypeSlotAnnotation"], List[Union[dict, "AlleleMutationTypeSlotAnnotation"]]]] = empty_list()
    allele_inheritance_modes: Optional[Union[Union[dict, "AlleleInheritanceModeSlotAnnotation"], List[Union[dict, "AlleleInheritanceModeSlotAnnotation"]]]] = empty_list()
    allele_germline_transmission_status: Optional[Union[dict, "AlleleGermlineTransmissionStatusSlotAnnotation"]] = None
    allele_functional_impacts: Optional[Union[Union[dict, "AlleleFunctionalImpactSlotAnnotation"], List[Union[dict, "AlleleFunctionalImpactSlotAnnotation"]]]] = empty_list()
    allele_molecular_mutations: Optional[Union[Union[dict, "AlleleMolecularMutationSlotAnnotation"], List[Union[dict, "AlleleMolecularMutationSlotAnnotation"]]]] = empty_list()
    allele_database_status: Optional[Union[dict, "AlleleDatabaseStatusSlotAnnotation"]] = None
    allele_secondary_ids: Optional[Union[Union[dict, "AlleleSecondaryIdSlotAnnotation"], List[Union[dict, "AlleleSecondaryIdSlotAnnotation"]]]] = empty_list()
    allele_nomenclature_events: Optional[Union[Union[dict, "AlleleNomenclatureEventSlotAnnotation"], List[Union[dict, "AlleleNomenclatureEventSlotAnnotation"]]]] = empty_list()
    allele_notes: Optional[Union[Union[dict, "AlleleNoteSlotAnnotation"], List[Union[dict, "AlleleNoteSlotAnnotation"]]]] = empty_list()
    allele_synonyms: Optional[Union[Union[dict, "AlleleSynonymSlotAnnotation"], List[Union[dict, "AlleleSynonymSlotAnnotation"]]]] = empty_list()
    allele_gene_associations: Optional[Union[Union[dict, "AlleleGeneAssociation"], List[Union[dict, "AlleleGeneAssociation"]]]] = empty_list()
    allele_transcript_associations: Optional[Union[Union[dict, "AlleleTranscriptAssociation"], List[Union[dict, "AlleleTranscriptAssociation"]]]] = empty_list()
    allele_protein_associations: Optional[Union[Union[dict, "AlleleProteinAssociation"], List[Union[dict, "AlleleProteinAssociation"]]]] = empty_list()
    allele_allele_associations: Optional[Union[Union[dict, "AlleleAlleleAssociation"], List[Union[dict, "AlleleAlleleAssociation"]]]] = empty_list()
    allele_variant_associations: Optional[Union[Union[dict, "AlleleVariantAssociation"], List[Union[dict, "AlleleVariantAssociation"]]]] = empty_list()
    allele_construct_associations: Optional[Union[Union[dict, "AlleleConstructAssociation"], List[Union[dict, "AlleleConstructAssociation"]]]] = empty_list()
    allele_cell_line_associations: Optional[Union[Union[dict, "AlleleCellLineAssociation"], List[Union[dict, "AlleleCellLineAssociation"]]]] = empty_list()
    allele_image_associations: Optional[Union[Union[dict, "AlleleImageAssociation"], List[Union[dict, "AlleleImageAssociation"]]]] = empty_list()
    allele_origin_associations: Optional[Union[Union[dict, "AlleleOriginAssociation"], List[Union[dict, "AlleleOriginAssociation"]]]] = empty_list()
    allele_generation_method_associations: Optional[Union[Union[dict, "AlleleGenerationMethodAssociation"], List[Union[dict, "AlleleGenerationMethodAssociation"]]]] = empty_list()
    aberration: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, AlleleCurie):
            self.curie = AlleleCurie(self.curie)

        if self._is_empty(self.allele_symbol):
            self.MissingRequiredField("allele_symbol")
        if not isinstance(self.allele_symbol, AlleleSymbolSlotAnnotation):
            self.allele_symbol = AlleleSymbolSlotAnnotation(**as_dict(self.allele_symbol))

        if self.allele_full_name is not None and not isinstance(self.allele_full_name, AlleleFullNameSlotAnnotation):
            self.allele_full_name = AlleleFullNameSlotAnnotation(**as_dict(self.allele_full_name))

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, ReferenceCurie) else ReferenceCurie(v) for v in self.references]

        if self.in_collection is not None and not isinstance(self.in_collection, VocabularyTermName):
            self.in_collection = VocabularyTermName(self.in_collection)

        if self.laboratory_of_origin is not None and not isinstance(self.laboratory_of_origin, LaboratoryCurie):
            self.laboratory_of_origin = LaboratoryCurie(self.laboratory_of_origin)

        if self.is_extinct is not None and not isinstance(self.is_extinct, Bool):
            self.is_extinct = Bool(self.is_extinct)

        if self.is_extrachromosomal is not None and not isinstance(self.is_extrachromosomal, Bool):
            self.is_extrachromosomal = Bool(self.is_extrachromosomal)

        if self.is_integrated is not None and not isinstance(self.is_integrated, Bool):
            self.is_integrated = Bool(self.is_integrated)

        if self.transgene_chromosome_location is not None and not isinstance(self.transgene_chromosome_location, ChromosomeCurie):
            self.transgene_chromosome_location = ChromosomeCurie(self.transgene_chromosome_location)

        self._normalize_inlined_as_dict(slot_name="allele_mutation_types", slot_type=AlleleMutationTypeSlotAnnotation, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="allele_inheritance_modes", slot_type=AlleleInheritanceModeSlotAnnotation, key_name="internal", keyed=False)

        if self.allele_germline_transmission_status is not None and not isinstance(self.allele_germline_transmission_status, AlleleGermlineTransmissionStatusSlotAnnotation):
            self.allele_germline_transmission_status = AlleleGermlineTransmissionStatusSlotAnnotation(**as_dict(self.allele_germline_transmission_status))

        self._normalize_inlined_as_dict(slot_name="allele_functional_impacts", slot_type=AlleleFunctionalImpactSlotAnnotation, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="allele_molecular_mutations", slot_type=AlleleMolecularMutationSlotAnnotation, key_name="internal", keyed=False)

        if self.allele_database_status is not None and not isinstance(self.allele_database_status, AlleleDatabaseStatusSlotAnnotation):
            self.allele_database_status = AlleleDatabaseStatusSlotAnnotation(**as_dict(self.allele_database_status))

        self._normalize_inlined_as_dict(slot_name="allele_secondary_ids", slot_type=AlleleSecondaryIdSlotAnnotation, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="allele_nomenclature_events", slot_type=AlleleNomenclatureEventSlotAnnotation, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="allele_notes", slot_type=AlleleNoteSlotAnnotation, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="allele_synonyms", slot_type=AlleleSynonymSlotAnnotation, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="allele_gene_associations", slot_type=AlleleGeneAssociation, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="allele_transcript_associations", slot_type=AlleleTranscriptAssociation, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="allele_protein_associations", slot_type=AlleleProteinAssociation, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="allele_allele_associations", slot_type=AlleleAlleleAssociation, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="allele_variant_associations", slot_type=AlleleVariantAssociation, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="allele_construct_associations", slot_type=AlleleConstructAssociation, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="allele_cell_line_associations", slot_type=AlleleCellLineAssociation, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="allele_image_associations", slot_type=AlleleImageAssociation, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="allele_origin_associations", slot_type=AlleleOriginAssociation, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="allele_generation_method_associations", slot_type=AlleleGenerationMethodAssociation, key_name="internal", keyed=False)

        if self.aberration is not None and not isinstance(self.aberration, str):
            self.aberration = str(self.aberration)

        super().__post_init__(**kwargs)


@dataclass
class CellLine(GenomicEntity):
    """
    Dummy cell line class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.CellLine
    class_class_curie: ClassVar[str] = "alliance:CellLine"
    class_name: ClassVar[str] = "CellLine"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.CellLine

    curie: Union[str, CellLineCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, CellLineCurie):
            self.curie = CellLineCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class Construct(GenomicEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Construct
    class_class_curie: ClassVar[str] = "alliance:Construct"
    class_name: ClassVar[str] = "Construct"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Construct

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
class ConstructComponent(GenomicEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ConstructComponent
    class_class_curie: ClassVar[str] = "alliance:ConstructComponent"
    class_name: ClassVar[str] = "ConstructComponent"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ConstructComponent

    curie: Union[str, ConstructComponentCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ConstructComponentCurie):
            self.curie = ConstructComponentCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class SequenceTargetingReagent(GenomicEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.SequenceTargetingReagent
    class_class_curie: ClassVar[str] = "alliance:SequenceTargetingReagent"
    class_name: ClassVar[str] = "SequenceTargetingReagent"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.SequenceTargetingReagent

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
class GenomicEntityDTO(BiologicalEntityDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GenomicEntityDTO
    class_class_curie: ClassVar[str] = "alliance:GenomicEntityDTO"
    class_name: ClassVar[str] = "GenomicEntityDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GenomicEntityDTO

    curie: Union[str, GenomicEntityDTOCurie] = None
    internal: Union[bool, Bool] = None
    taxon_curie: str = None
    cross_reference_dtos: Optional[Union[Union[dict, "CrossReferenceDTO"], List[Union[dict, "CrossReferenceDTO"]]]] = empty_list()
    secondary_identifiers: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    genomic_location_association_dtos: Optional[Union[Union[dict, "GenomicLocationAssociationDTO"], List[Union[dict, "GenomicLocationAssociationDTO"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, GenomicEntityDTOCurie):
            self.curie = GenomicEntityDTOCurie(self.curie)

        if not isinstance(self.cross_reference_dtos, list):
            self.cross_reference_dtos = [self.cross_reference_dtos] if self.cross_reference_dtos is not None else []
        self.cross_reference_dtos = [v if isinstance(v, CrossReferenceDTO) else CrossReferenceDTO(**as_dict(v)) for v in self.cross_reference_dtos]

        if not isinstance(self.secondary_identifiers, list):
            self.secondary_identifiers = [self.secondary_identifiers] if self.secondary_identifiers is not None else []
        self.secondary_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.secondary_identifiers]

        if not isinstance(self.genomic_location_association_dtos, list):
            self.genomic_location_association_dtos = [self.genomic_location_association_dtos] if self.genomic_location_association_dtos is not None else []
        self.genomic_location_association_dtos = [v if isinstance(v, GenomicLocationAssociationDTO) else GenomicLocationAssociationDTO(**as_dict(v)) for v in self.genomic_location_association_dtos]

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
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, TranscriptCurie):
            self.curie = TranscriptCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class CrossReference(AuditedObject):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.CrossReference
    class_class_curie: ClassVar[str] = "alliance:CrossReference"
    class_name: ClassVar[str] = "CrossReference"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.CrossReference

    internal: Union[bool, Bool] = None
    referenced_curie: Union[str, URIorCURIE] = None
    display_name: str = None
    resource_descriptor_page: Optional[Union[dict, "ResourceDescriptorPage"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.referenced_curie):
            self.MissingRequiredField("referenced_curie")
        if not isinstance(self.referenced_curie, URIorCURIE):
            self.referenced_curie = URIorCURIE(self.referenced_curie)

        if self._is_empty(self.display_name):
            self.MissingRequiredField("display_name")
        if not isinstance(self.display_name, str):
            self.display_name = str(self.display_name)

        if self.resource_descriptor_page is not None and not isinstance(self.resource_descriptor_page, ResourceDescriptorPage):
            self.resource_descriptor_page = ResourceDescriptorPage(**as_dict(self.resource_descriptor_page))

        super().__post_init__(**kwargs)


@dataclass
class CrossReferenceDTO(AuditedObjectDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.CrossReferenceDTO
    class_class_curie: ClassVar[str] = "alliance:CrossReferenceDTO"
    class_name: ClassVar[str] = "CrossReferenceDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.CrossReferenceDTO

    internal: Union[bool, Bool] = None
    referenced_curie: Union[str, URIorCURIE] = None
    page_area: str = None
    display_name: str = None
    prefix: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.referenced_curie):
            self.MissingRequiredField("referenced_curie")
        if not isinstance(self.referenced_curie, URIorCURIE):
            self.referenced_curie = URIorCURIE(self.referenced_curie)

        if self._is_empty(self.page_area):
            self.MissingRequiredField("page_area")
        if not isinstance(self.page_area, str):
            self.page_area = str(self.page_area)

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
class DataProvider(AuditedObject):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.DataProvider
    class_class_curie: ClassVar[str] = "alliance:DataProvider"
    class_name: ClassVar[str] = "DataProvider"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.DataProvider

    internal: Union[bool, Bool] = None
    source_organization: Union[dict, "Organization"] = None
    cross_reference: Optional[Union[dict, CrossReference]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.source_organization):
            self.MissingRequiredField("source_organization")
        if not isinstance(self.source_organization, Organization):
            self.source_organization = Organization(**as_dict(self.source_organization))

        if self.cross_reference is not None and not isinstance(self.cross_reference, CrossReference):
            self.cross_reference = CrossReference(**as_dict(self.cross_reference))

        super().__post_init__(**kwargs)


@dataclass
class DataProviderDTO(AuditedObjectDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.DataProviderDTO
    class_class_curie: ClassVar[str] = "alliance:DataProviderDTO"
    class_name: ClassVar[str] = "DataProviderDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.DataProviderDTO

    internal: Union[bool, Bool] = None
    source_organization_abbreviation: str = None
    cross_reference_dto: Optional[Union[dict, CrossReferenceDTO]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.source_organization_abbreviation):
            self.MissingRequiredField("source_organization_abbreviation")
        if not isinstance(self.source_organization_abbreviation, str):
            self.source_organization_abbreviation = str(self.source_organization_abbreviation)

        if self.cross_reference_dto is not None and not isinstance(self.cross_reference_dto, CrossReferenceDTO):
            self.cross_reference_dto = CrossReferenceDTO(**as_dict(self.cross_reference_dto))

        super().__post_init__(**kwargs)


@dataclass
class Note(AuditedObject):
    """
    Note object for capturing free-text describing some attribute of an entity, coupled with a 'note type', internal
    boolean, and an optional list of references. Permissible values for note_type can be viewed and managed in the
    A-Team curation UI Controlled Vocabulary Terms Table.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Note
    class_class_curie: ClassVar[str] = "alliance:Note"
    class_name: ClassVar[str] = "Note"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Note

    internal: Union[bool, Bool] = None
    free_text: str = None
    note_type: Union[str, VocabularyTermName] = None
    evidence: Optional[Union[Union[str, InformationContentEntityCurie], List[Union[str, InformationContentEntityCurie]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.free_text):
            self.MissingRequiredField("free_text")
        if not isinstance(self.free_text, str):
            self.free_text = str(self.free_text)

        if self._is_empty(self.note_type):
            self.MissingRequiredField("note_type")
        if not isinstance(self.note_type, VocabularyTermName):
            self.note_type = VocabularyTermName(self.note_type)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, InformationContentEntityCurie) else InformationContentEntityCurie(v) for v in self.evidence]

        super().__post_init__(**kwargs)


@dataclass
class NoteDTO(AuditedObjectDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.NoteDTO
    class_class_curie: ClassVar[str] = "alliance:NoteDTO"
    class_name: ClassVar[str] = "NoteDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.NoteDTO

    internal: Union[bool, Bool] = None
    free_text: str = None
    note_type_name: str = None
    evidence_curies: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.free_text):
            self.MissingRequiredField("free_text")
        if not isinstance(self.free_text, str):
            self.free_text = str(self.free_text)

        if self._is_empty(self.note_type_name):
            self.MissingRequiredField("note_type_name")
        if not isinstance(self.note_type_name, str):
            self.note_type_name = str(self.note_type_name)

        if not isinstance(self.evidence_curies, list):
            self.evidence_curies = [self.evidence_curies] if self.evidence_curies is not None else []
        self.evidence_curies = [v if isinstance(v, str) else str(v) for v in self.evidence_curies]

        super().__post_init__(**kwargs)


@dataclass
class SlotAnnotation(AuditedObject):
    """
    SlotAnnotation classes should be used when we need to attach metadata (in particular evidence and provenance) to a
    slot in the context of its referencing class, that can not be fully captured using an Association between the full
    class itself, and an InformationContentEntity. Evidence and provenance can exist here in the form of an evidence
    code, a publication, a personal communication or any other kind of InformationContentEntity. SlotAnnotation
    classes are used where the slot is not referencing a class in and of itself, and often has a scalar range.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.SlotAnnotation
    class_class_curie: ClassVar[str] = "alliance:SlotAnnotation"
    class_name: ClassVar[str] = "SlotAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.SlotAnnotation

    internal: Union[bool, Bool] = None
    evidence: Optional[Union[Union[str, InformationContentEntityCurie], List[Union[str, InformationContentEntityCurie]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, InformationContentEntityCurie) else InformationContentEntityCurie(v) for v in self.evidence]

        super().__post_init__(**kwargs)


@dataclass
class AlleleDatabaseStatusSlotAnnotation(SlotAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleDatabaseStatusSlotAnnotation
    class_class_curie: ClassVar[str] = "alliance:AlleleDatabaseStatusSlotAnnotation"
    class_name: ClassVar[str] = "AlleleDatabaseStatusSlotAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleDatabaseStatusSlotAnnotation

    internal: Union[bool, Bool] = None
    single_allele: Union[str, AlleleCurie] = None
    database_status: Union[str, VocabularyTermName] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.single_allele):
            self.MissingRequiredField("single_allele")
        if not isinstance(self.single_allele, AlleleCurie):
            self.single_allele = AlleleCurie(self.single_allele)

        if self._is_empty(self.database_status):
            self.MissingRequiredField("database_status")
        if not isinstance(self.database_status, VocabularyTermName):
            self.database_status = VocabularyTermName(self.database_status)

        super().__post_init__(**kwargs)


@dataclass
class AlleleFunctionalImpactSlotAnnotation(SlotAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleFunctionalImpactSlotAnnotation
    class_class_curie: ClassVar[str] = "alliance:AlleleFunctionalImpactSlotAnnotation"
    class_name: ClassVar[str] = "AlleleFunctionalImpactSlotAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleFunctionalImpactSlotAnnotation

    internal: Union[bool, Bool] = None
    single_allele: Union[str, AlleleCurie] = None
    functional_impacts: Union[Union[str, VocabularyTermName], List[Union[str, VocabularyTermName]]] = None
    phenotype_term: Optional[Union[str, PhenotypeTermCurie]] = None
    phenotype_statement: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.single_allele):
            self.MissingRequiredField("single_allele")
        if not isinstance(self.single_allele, AlleleCurie):
            self.single_allele = AlleleCurie(self.single_allele)

        if self._is_empty(self.functional_impacts):
            self.MissingRequiredField("functional_impacts")
        if not isinstance(self.functional_impacts, list):
            self.functional_impacts = [self.functional_impacts] if self.functional_impacts is not None else []
        self.functional_impacts = [v if isinstance(v, VocabularyTermName) else VocabularyTermName(v) for v in self.functional_impacts]

        if self.phenotype_term is not None and not isinstance(self.phenotype_term, PhenotypeTermCurie):
            self.phenotype_term = PhenotypeTermCurie(self.phenotype_term)

        if self.phenotype_statement is not None and not isinstance(self.phenotype_statement, str):
            self.phenotype_statement = str(self.phenotype_statement)

        super().__post_init__(**kwargs)


@dataclass
class AlleleGermlineTransmissionStatusSlotAnnotation(SlotAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleGermlineTransmissionStatusSlotAnnotation
    class_class_curie: ClassVar[str] = "alliance:AlleleGermlineTransmissionStatusSlotAnnotation"
    class_name: ClassVar[str] = "AlleleGermlineTransmissionStatusSlotAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleGermlineTransmissionStatusSlotAnnotation

    internal: Union[bool, Bool] = None
    single_allele: Union[str, AlleleCurie] = None
    germline_transmission_status: Union[str, VocabularyTermName] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.single_allele):
            self.MissingRequiredField("single_allele")
        if not isinstance(self.single_allele, AlleleCurie):
            self.single_allele = AlleleCurie(self.single_allele)

        if self._is_empty(self.germline_transmission_status):
            self.MissingRequiredField("germline_transmission_status")
        if not isinstance(self.germline_transmission_status, VocabularyTermName):
            self.germline_transmission_status = VocabularyTermName(self.germline_transmission_status)

        super().__post_init__(**kwargs)


@dataclass
class AlleleInheritanceModeSlotAnnotation(SlotAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleInheritanceModeSlotAnnotation
    class_class_curie: ClassVar[str] = "alliance:AlleleInheritanceModeSlotAnnotation"
    class_name: ClassVar[str] = "AlleleInheritanceModeSlotAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleInheritanceModeSlotAnnotation

    internal: Union[bool, Bool] = None
    single_allele: Union[str, AlleleCurie] = None
    inheritance_mode: Union[str, VocabularyTermName] = None
    phenotype_term: Optional[Union[str, PhenotypeTermCurie]] = None
    phenotype_statement: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.single_allele):
            self.MissingRequiredField("single_allele")
        if not isinstance(self.single_allele, AlleleCurie):
            self.single_allele = AlleleCurie(self.single_allele)

        if self._is_empty(self.inheritance_mode):
            self.MissingRequiredField("inheritance_mode")
        if not isinstance(self.inheritance_mode, VocabularyTermName):
            self.inheritance_mode = VocabularyTermName(self.inheritance_mode)

        if self.phenotype_term is not None and not isinstance(self.phenotype_term, PhenotypeTermCurie):
            self.phenotype_term = PhenotypeTermCurie(self.phenotype_term)

        if self.phenotype_statement is not None and not isinstance(self.phenotype_statement, str):
            self.phenotype_statement = str(self.phenotype_statement)

        super().__post_init__(**kwargs)


@dataclass
class AlleleMolecularMutationSlotAnnotation(SlotAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleMolecularMutationSlotAnnotation
    class_class_curie: ClassVar[str] = "alliance:AlleleMolecularMutationSlotAnnotation"
    class_name: ClassVar[str] = "AlleleMolecularMutationSlotAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleMolecularMutationSlotAnnotation

    internal: Union[bool, Bool] = None
    single_allele: Union[str, AlleleCurie] = None
    molecular_mutations: Union[str, List[str]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.single_allele):
            self.MissingRequiredField("single_allele")
        if not isinstance(self.single_allele, AlleleCurie):
            self.single_allele = AlleleCurie(self.single_allele)

        if self._is_empty(self.molecular_mutations):
            self.MissingRequiredField("molecular_mutations")
        if not isinstance(self.molecular_mutations, list):
            self.molecular_mutations = [self.molecular_mutations] if self.molecular_mutations is not None else []
        self.molecular_mutations = [v if isinstance(v, str) else str(v) for v in self.molecular_mutations]

        super().__post_init__(**kwargs)


@dataclass
class AlleleMutationTypeSlotAnnotation(SlotAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleMutationTypeSlotAnnotation
    class_class_curie: ClassVar[str] = "alliance:AlleleMutationTypeSlotAnnotation"
    class_name: ClassVar[str] = "AlleleMutationTypeSlotAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleMutationTypeSlotAnnotation

    internal: Union[bool, Bool] = None
    single_allele: Union[str, AlleleCurie] = None
    mutation_types: Union[Union[str, SOTermCurie], List[Union[str, SOTermCurie]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.single_allele):
            self.MissingRequiredField("single_allele")
        if not isinstance(self.single_allele, AlleleCurie):
            self.single_allele = AlleleCurie(self.single_allele)

        if self._is_empty(self.mutation_types):
            self.MissingRequiredField("mutation_types")
        if not isinstance(self.mutation_types, list):
            self.mutation_types = [self.mutation_types] if self.mutation_types is not None else []
        self.mutation_types = [v if isinstance(v, SOTermCurie) else SOTermCurie(v) for v in self.mutation_types]

        super().__post_init__(**kwargs)


@dataclass
class AlleleNomenclatureEventSlotAnnotation(SlotAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleNomenclatureEventSlotAnnotation
    class_class_curie: ClassVar[str] = "alliance:AlleleNomenclatureEventSlotAnnotation"
    class_name: ClassVar[str] = "AlleleNomenclatureEventSlotAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleNomenclatureEventSlotAnnotation

    internal: Union[bool, Bool] = None
    single_allele: Union[str, AlleleCurie] = None
    nomenclature_event: Union[str, VocabularyTermName] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.single_allele):
            self.MissingRequiredField("single_allele")
        if not isinstance(self.single_allele, AlleleCurie):
            self.single_allele = AlleleCurie(self.single_allele)

        if self._is_empty(self.nomenclature_event):
            self.MissingRequiredField("nomenclature_event")
        if not isinstance(self.nomenclature_event, VocabularyTermName):
            self.nomenclature_event = VocabularyTermName(self.nomenclature_event)

        super().__post_init__(**kwargs)


@dataclass
class AlleleNoteSlotAnnotation(SlotAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleNoteSlotAnnotation
    class_class_curie: ClassVar[str] = "alliance:AlleleNoteSlotAnnotation"
    class_name: ClassVar[str] = "AlleleNoteSlotAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleNoteSlotAnnotation

    internal: Union[bool, Bool] = None
    single_allele: Union[str, AlleleCurie] = None
    related_note: Union[dict, "Note"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.single_allele):
            self.MissingRequiredField("single_allele")
        if not isinstance(self.single_allele, AlleleCurie):
            self.single_allele = AlleleCurie(self.single_allele)

        if self._is_empty(self.related_note):
            self.MissingRequiredField("related_note")
        if not isinstance(self.related_note, Note):
            self.related_note = Note(**as_dict(self.related_note))

        super().__post_init__(**kwargs)


@dataclass
class AlleleSecondaryIdSlotAnnotation(SlotAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleSecondaryIdSlotAnnotation
    class_class_curie: ClassVar[str] = "alliance:AlleleSecondaryIdSlotAnnotation"
    class_name: ClassVar[str] = "AlleleSecondaryIdSlotAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleSecondaryIdSlotAnnotation

    internal: Union[bool, Bool] = None
    single_allele: Union[str, AlleleCurie] = None
    secondary_id: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.single_allele):
            self.MissingRequiredField("single_allele")
        if not isinstance(self.single_allele, AlleleCurie):
            self.single_allele = AlleleCurie(self.single_allele)

        if self._is_empty(self.secondary_id):
            self.MissingRequiredField("secondary_id")
        if not isinstance(self.secondary_id, URIorCURIE):
            self.secondary_id = URIorCURIE(self.secondary_id)

        super().__post_init__(**kwargs)


@dataclass
class SlotAnnotationDTO(AuditedObjectDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.SlotAnnotationDTO
    class_class_curie: ClassVar[str] = "alliance:SlotAnnotationDTO"
    class_name: ClassVar[str] = "SlotAnnotationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.SlotAnnotationDTO

    internal: Union[bool, Bool] = None
    evidence_curies: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.evidence_curies, list):
            self.evidence_curies = [self.evidence_curies] if self.evidence_curies is not None else []
        self.evidence_curies = [v if isinstance(v, str) else str(v) for v in self.evidence_curies]

        super().__post_init__(**kwargs)


@dataclass
class NameSlotAnnotation(SlotAnnotation):
    """
    Some symbol or name for an object, including current names as well as aliases, with accompanying metadata. The
    entity to which the symbol/name applies is specified in objects that inherit from this object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.NameSlotAnnotation
    class_class_curie: ClassVar[str] = "alliance:NameSlotAnnotation"
    class_name: ClassVar[str] = "NameSlotAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.NameSlotAnnotation

    internal: Union[bool, Bool] = None
    name_type: Union[str, VocabularyTermName] = None
    format_text: str = None
    display_text: str = None
    synonym_url: Optional[Union[str, URI]] = None
    synonym_scope: Optional[Union[str, VocabularyTermName]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name_type):
            self.MissingRequiredField("name_type")
        if not isinstance(self.name_type, VocabularyTermName):
            self.name_type = VocabularyTermName(self.name_type)

        if self._is_empty(self.format_text):
            self.MissingRequiredField("format_text")
        if not isinstance(self.format_text, str):
            self.format_text = str(self.format_text)

        if self._is_empty(self.display_text):
            self.MissingRequiredField("display_text")
        if not isinstance(self.display_text, str):
            self.display_text = str(self.display_text)

        if self.synonym_url is not None and not isinstance(self.synonym_url, URI):
            self.synonym_url = URI(self.synonym_url)

        if self.synonym_scope is not None and not isinstance(self.synonym_scope, VocabularyTermName):
            self.synonym_scope = VocabularyTermName(self.synonym_scope)

        super().__post_init__(**kwargs)


@dataclass
class AlleleFullNameSlotAnnotation(NameSlotAnnotation):
    """
    The one current full name for the allele.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleFullNameSlotAnnotation
    class_class_curie: ClassVar[str] = "alliance:AlleleFullNameSlotAnnotation"
    class_name: ClassVar[str] = "AlleleFullNameSlotAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleFullNameSlotAnnotation

    internal: Union[bool, Bool] = None
    format_text: str = None
    display_text: str = None
    single_allele: Union[str, AlleleCurie] = None
    name_type: Union[str, VocabularyTermName] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.single_allele):
            self.MissingRequiredField("single_allele")
        if not isinstance(self.single_allele, AlleleCurie):
            self.single_allele = AlleleCurie(self.single_allele)

        if self._is_empty(self.name_type):
            self.MissingRequiredField("name_type")
        if not isinstance(self.name_type, VocabularyTermName):
            self.name_type = VocabularyTermName(self.name_type)

        super().__post_init__(**kwargs)


@dataclass
class AlleleSymbolSlotAnnotation(NameSlotAnnotation):
    """
    The one current symbol for the allele.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleSymbolSlotAnnotation
    class_class_curie: ClassVar[str] = "alliance:AlleleSymbolSlotAnnotation"
    class_name: ClassVar[str] = "AlleleSymbolSlotAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleSymbolSlotAnnotation

    internal: Union[bool, Bool] = None
    format_text: str = None
    display_text: str = None
    single_allele: Union[str, AlleleCurie] = None
    name_type: Union[str, VocabularyTermName] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.single_allele):
            self.MissingRequiredField("single_allele")
        if not isinstance(self.single_allele, AlleleCurie):
            self.single_allele = AlleleCurie(self.single_allele)

        if self._is_empty(self.name_type):
            self.MissingRequiredField("name_type")
        if not isinstance(self.name_type, VocabularyTermName):
            self.name_type = VocabularyTermName(self.name_type)

        super().__post_init__(**kwargs)


@dataclass
class AlleleSynonymSlotAnnotation(NameSlotAnnotation):
    """
    All aliases (non-preferred names) for the allele. Any type of synonym is acceptable.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleSynonymSlotAnnotation
    class_class_curie: ClassVar[str] = "alliance:AlleleSynonymSlotAnnotation"
    class_name: ClassVar[str] = "AlleleSynonymSlotAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleSynonymSlotAnnotation

    internal: Union[bool, Bool] = None
    name_type: Union[str, VocabularyTermName] = None
    format_text: str = None
    display_text: str = None
    single_allele: Union[str, AlleleCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.single_allele):
            self.MissingRequiredField("single_allele")
        if not isinstance(self.single_allele, AlleleCurie):
            self.single_allele = AlleleCurie(self.single_allele)

        super().__post_init__(**kwargs)


@dataclass
class NameSlotAnnotationDTO(SlotAnnotationDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.NameSlotAnnotationDTO
    class_class_curie: ClassVar[str] = "alliance:NameSlotAnnotationDTO"
    class_name: ClassVar[str] = "NameSlotAnnotationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.NameSlotAnnotationDTO

    internal: Union[bool, Bool] = None
    name_type_name: str = None
    format_text: str = None
    display_text: str = None
    synonym_url: Optional[Union[str, URI]] = None
    synonym_scope_name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name_type_name):
            self.MissingRequiredField("name_type_name")
        if not isinstance(self.name_type_name, str):
            self.name_type_name = str(self.name_type_name)

        if self._is_empty(self.format_text):
            self.MissingRequiredField("format_text")
        if not isinstance(self.format_text, str):
            self.format_text = str(self.format_text)

        if self._is_empty(self.display_text):
            self.MissingRequiredField("display_text")
        if not isinstance(self.display_text, str):
            self.display_text = str(self.display_text)

        if self.synonym_url is not None and not isinstance(self.synonym_url, URI):
            self.synonym_url = URI(self.synonym_url)

        if self.synonym_scope_name is not None and not isinstance(self.synonym_scope_name, str):
            self.synonym_scope_name = str(self.synonym_scope_name)

        super().__post_init__(**kwargs)


@dataclass
class SymbolSlotAnnotationDTO(NameSlotAnnotationDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.SymbolSlotAnnotationDTO
    class_class_curie: ClassVar[str] = "alliance:SymbolSlotAnnotationDTO"
    class_name: ClassVar[str] = "SymbolSlotAnnotationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.SymbolSlotAnnotationDTO

    internal: Union[bool, Bool] = None
    format_text: str = None
    display_text: str = None
    name_type_name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name_type_name):
            self.MissingRequiredField("name_type_name")
        if not isinstance(self.name_type_name, str):
            self.name_type_name = str(self.name_type_name)

        super().__post_init__(**kwargs)


@dataclass
class FullNameSlotAnnotationDTO(NameSlotAnnotationDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.FullNameSlotAnnotationDTO
    class_class_curie: ClassVar[str] = "alliance:FullNameSlotAnnotationDTO"
    class_name: ClassVar[str] = "FullNameSlotAnnotationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.FullNameSlotAnnotationDTO

    internal: Union[bool, Bool] = None
    format_text: str = None
    display_text: str = None
    name_type_name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name_type_name):
            self.MissingRequiredField("name_type_name")
        if not isinstance(self.name_type_name, str):
            self.name_type_name = str(self.name_type_name)

        super().__post_init__(**kwargs)


@dataclass
class SystematicNameSlotAnnotationDTO(NameSlotAnnotationDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.SystematicNameSlotAnnotationDTO
    class_class_curie: ClassVar[str] = "alliance:SystematicNameSlotAnnotationDTO"
    class_name: ClassVar[str] = "SystematicNameSlotAnnotationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.SystematicNameSlotAnnotationDTO

    internal: Union[bool, Bool] = None
    format_text: str = None
    display_text: str = None
    name_type_name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name_type_name):
            self.MissingRequiredField("name_type_name")
        if not isinstance(self.name_type_name, str):
            self.name_type_name = str(self.name_type_name)

        super().__post_init__(**kwargs)


@dataclass
class Association(AuditedObject):
    """
    A typed association between two entities, supported by evidence. Associations have three base slots: subject,
    object, and predicate, but they can have any number of additional attributes that help qualify the relationship
    between the subject and the object. The subject is the curie (or identifier) of the class that is the subject of
    the association, and likewise the object is the curie (or identifier of the class that is the object. The
    relationship between subject and object is defined by the predicate slot (which can also be constrained using the
    range of the predicate).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Association
    class_class_curie: ClassVar[str] = "alliance:Association"
    class_name: ClassVar[str] = "Association"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Association

    internal: Union[bool, Bool] = None
    subject: str = None
    predicate: str = None
    object: str = None
    evidence: Optional[Union[Union[str, InformationContentEntityCurie], List[Union[str, InformationContentEntityCurie]]]] = empty_list()

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

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, InformationContentEntityCurie) else InformationContentEntityCurie(v) for v in self.evidence]

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

    internal: Union[bool, Bool] = None
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
    internal: Union[bool, Bool] = None
    interaction_data_provider: Union[str, "InteractionSourceEnum"] = None
    interaction_type: Union[str, "InteractionTypeEnum"] = None
    interactor_A_type: Union[str, "InteractorTypeEnum"] = None
    interactor_B_type: Union[str, "InteractorTypeEnum"] = None
    subject: Union[str, GeneCurie] = None
    predicate: str = None
    object: Union[str, GeneCurie] = None
    cross_references: Optional[Union[Union[dict, "CrossReference"], List[Union[dict, "CrossReference"]]]] = empty_list()
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

        self._normalize_inlined_as_dict(slot_name="cross_references", slot_type=CrossReference, key_name="internal", keyed=False)

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
    internal: Union[bool, Bool] = None
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
    internal: Union[bool, Bool] = None
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
class ConstructComponentAssociation(Association):
    """
    The predicate should be a VocabularyTerm with one of the following values - expresses (RO:0002292) /
    is_regulated_by (RO:0002334) / targets (RO:0002436)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ConstructComponentAssociation
    class_class_curie: ClassVar[str] = "alliance:ConstructComponentAssociation"
    class_name: ClassVar[str] = "ConstructComponentAssociation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ConstructComponentAssociation

    internal: Union[bool, Bool] = None
    predicate: Union[str, VocabularyTermName] = None
    subject: Union[str, ConstructCurie] = None
    object: Union[str, ConstructComponentCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, VocabularyTermName):
            self.predicate = VocabularyTermName(self.predicate)

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
class SequenceTargetingReagentToGeneAssociation(Association):
    """
    the relationship between a Sequence Targeting Reagent and its targeted genes. The predicate should be a
    VocabularyTerm with one of the following values - targets
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.SequenceTargetingReagentToGeneAssociation
    class_class_curie: ClassVar[str] = "alliance:SequenceTargetingReagentToGeneAssociation"
    class_name: ClassVar[str] = "SequenceTargetingReagentToGeneAssociation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.SequenceTargetingReagentToGeneAssociation

    internal: Union[bool, Bool] = None
    predicate: Union[str, VocabularyTermName] = None
    subject: Union[str, SequenceTargetingReagentCurie] = None
    object: Union[str, GeneCurie] = None
    references: Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, VocabularyTermName):
            self.predicate = VocabularyTermName(self.predicate)

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
class AlleleCellLineAssociation(Association):
    """
    The relationship between an allele and a cell line. Includes mutant/ embryonic stem cell lines known to carry the
    allele, and parental cell line of alleles made in embryonic stem cells.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleCellLineAssociation
    class_class_curie: ClassVar[str] = "alliance:AlleleCellLineAssociation"
    class_name: ClassVar[str] = "AlleleCellLineAssociation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleCellLineAssociation

    internal: Union[bool, Bool] = None
    subject: Union[str, AlleleCurie] = None
    predicate: Union[str, VocabularyTermName] = None
    object: Union[str, CellLineCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, AlleleCurie):
            self.subject = AlleleCurie(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, VocabularyTermName):
            self.predicate = VocabularyTermName(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, CellLineCurie):
            self.object = CellLineCurie(self.object)

        super().__post_init__(**kwargs)


@dataclass
class AlleleGenerationMethodAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleGenerationMethodAssociation
    class_class_curie: ClassVar[str] = "alliance:AlleleGenerationMethodAssociation"
    class_name: ClassVar[str] = "AlleleGenerationMethodAssociation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleGenerationMethodAssociation

    internal: Union[bool, Bool] = None
    subject: Union[str, AlleleCurie] = None
    predicate: str = None
    object: Union[dict, GenerationMethod] = None
    evidence: Optional[Union[Union[str, InformationContentEntityCurie], List[Union[str, InformationContentEntityCurie]]]] = empty_list()
    mutation_target_strain: Optional[Union[str, AffectedGenomicModelCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, AlleleCurie):
            self.subject = AlleleCurie(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GenerationMethod):
            self.object = GenerationMethod(**as_dict(self.object))

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, InformationContentEntityCurie) else InformationContentEntityCurie(v) for v in self.evidence]

        if self.mutation_target_strain is not None and not isinstance(self.mutation_target_strain, AffectedGenomicModelCurie):
            self.mutation_target_strain = AffectedGenomicModelCurie(self.mutation_target_strain)

        super().__post_init__(**kwargs)


@dataclass
class AlleleGenomicEntityAssociation(Association):
    """
    Association between an allele and a genomic entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleGenomicEntityAssociation
    class_class_curie: ClassVar[str] = "alliance:AlleleGenomicEntityAssociation"
    class_name: ClassVar[str] = "AlleleGenomicEntityAssociation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleGenomicEntityAssociation

    internal: Union[bool, Bool] = None
    subject: Union[str, AlleleCurie] = None
    predicate: Union[str, VocabularyTermName] = None
    object: Union[str, GenomicEntityCurie] = None
    evidence_code: Optional[Union[str, ECOTermCurie]] = None
    related_note: Optional[Union[dict, "Note"]] = None
    evidence: Optional[Union[Union[str, InformationContentEntityCurie], List[Union[str, InformationContentEntityCurie]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, AlleleCurie):
            self.subject = AlleleCurie(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, VocabularyTermName):
            self.predicate = VocabularyTermName(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GenomicEntityCurie):
            self.object = GenomicEntityCurie(self.object)

        if self.evidence_code is not None and not isinstance(self.evidence_code, ECOTermCurie):
            self.evidence_code = ECOTermCurie(self.evidence_code)

        if self.related_note is not None and not isinstance(self.related_note, Note):
            self.related_note = Note(**as_dict(self.related_note))

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, InformationContentEntityCurie) else InformationContentEntityCurie(v) for v in self.evidence]

        super().__post_init__(**kwargs)


@dataclass
class AlleleAlleleAssociation(AlleleGenomicEntityAssociation):
    """
    Association between an allele and another allele
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleAlleleAssociation
    class_class_curie: ClassVar[str] = "alliance:AlleleAlleleAssociation"
    class_name: ClassVar[str] = "AlleleAlleleAssociation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleAlleleAssociation

    internal: Union[bool, Bool] = None
    subject: Union[str, AlleleCurie] = None
    predicate: str = None
    object: Union[str, AlleleCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, AlleleCurie):
            self.object = AlleleCurie(self.object)

        super().__post_init__(**kwargs)


@dataclass
class AlleleConstructAssociation(AlleleGenomicEntityAssociation):
    """
    The relationship between an allele and constructs contained in that allele.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleConstructAssociation
    class_class_curie: ClassVar[str] = "alliance:AlleleConstructAssociation"
    class_name: ClassVar[str] = "AlleleConstructAssociation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleConstructAssociation

    internal: Union[bool, Bool] = None
    subject: Union[str, AlleleCurie] = None
    predicate: Union[str, VocabularyTermName] = None
    object: Union[str, ConstructCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, AlleleCurie):
            self.subject = AlleleCurie(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, VocabularyTermName):
            self.predicate = VocabularyTermName(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ConstructCurie):
            self.object = ConstructCurie(self.object)

        super().__post_init__(**kwargs)


@dataclass
class AlleleGeneAssociation(AlleleGenomicEntityAssociation):
    """
    Association between an allele and a gene
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleGeneAssociation
    class_class_curie: ClassVar[str] = "alliance:AlleleGeneAssociation"
    class_name: ClassVar[str] = "AlleleGeneAssociation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleGeneAssociation

    internal: Union[bool, Bool] = None
    subject: Union[str, AlleleCurie] = None
    predicate: Union[str, VocabularyTermName] = None
    object: Union[str, GeneCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, GeneCurie):
            self.object = GeneCurie(self.object)

        super().__post_init__(**kwargs)


@dataclass
class AlleleImageAssociation(Association):
    """
    The relationship between an allele and an image.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleImageAssociation
    class_class_curie: ClassVar[str] = "alliance:AlleleImageAssociation"
    class_name: ClassVar[str] = "AlleleImageAssociation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleImageAssociation

    internal: Union[bool, Bool] = None
    subject: Union[str, AlleleCurie] = None
    predicate: Union[str, VocabularyTermName] = None
    object: Union[str, ImageCurie] = None
    primary_image: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, AlleleCurie):
            self.subject = AlleleCurie(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, VocabularyTermName):
            self.predicate = VocabularyTermName(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ImageCurie):
            self.object = ImageCurie(self.object)

        if self.primary_image is not None and not isinstance(self.primary_image, Bool):
            self.primary_image = Bool(self.primary_image)

        super().__post_init__(**kwargs)


@dataclass
class AlleleOriginAssociation(Association):
    """
    The relationship between an allele and the origin of the allele.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleOriginAssociation
    class_class_curie: ClassVar[str] = "alliance:AlleleOriginAssociation"
    class_name: ClassVar[str] = "AlleleOriginAssociation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleOriginAssociation

    internal: Union[bool, Bool] = None
    predicate: str = None
    subject: Union[str, AlleleCurie] = None
    object: Union[str, AffectedGenomicModelCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, AlleleCurie):
            self.subject = AlleleCurie(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, AffectedGenomicModelCurie):
            self.object = AffectedGenomicModelCurie(self.object)

        super().__post_init__(**kwargs)


@dataclass
class AlleleProteinAssociation(AlleleGenomicEntityAssociation):
    """
    Association between an allele and a protein
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleProteinAssociation
    class_class_curie: ClassVar[str] = "alliance:AlleleProteinAssociation"
    class_name: ClassVar[str] = "AlleleProteinAssociation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleProteinAssociation

    internal: Union[bool, Bool] = None
    subject: Union[str, AlleleCurie] = None
    predicate: Union[str, VocabularyTermName] = None
    object: Union[str, ProteinCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ProteinCurie):
            self.object = ProteinCurie(self.object)

        super().__post_init__(**kwargs)


@dataclass
class AlleleTranscriptAssociation(AlleleGenomicEntityAssociation):
    """
    Association between an allele and a transcript
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleTranscriptAssociation
    class_class_curie: ClassVar[str] = "alliance:AlleleTranscriptAssociation"
    class_name: ClassVar[str] = "AlleleTranscriptAssociation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleTranscriptAssociation

    internal: Union[bool, Bool] = None
    subject: Union[str, AlleleCurie] = None
    predicate: Union[str, VocabularyTermName] = None
    object: Union[str, TranscriptCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, TranscriptCurie):
            self.object = TranscriptCurie(self.object)

        super().__post_init__(**kwargs)


@dataclass
class AlleleVariantAssociation(AlleleGenomicEntityAssociation):
    """
    The relationship between an allele and a variant is many to many. An Allele may have many variants and a variant
    can be present in many alleles.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleVariantAssociation
    class_class_curie: ClassVar[str] = "alliance:AlleleVariantAssociation"
    class_name: ClassVar[str] = "AlleleVariantAssociation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleVariantAssociation

    internal: Union[bool, Bool] = None
    predicate: Union[str, VocabularyTermName] = None
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
class ExternalDatabaseLink(AuditedObject):
    """
    Base relation that holds the identifier prefix, base url and url suffix to help in generating URLs in
    crossReferences.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ExternalDatabaseLink
    class_class_curie: ClassVar[str] = "alliance:ExternalDatabaseLink"
    class_name: ClassVar[str] = "ExternalDatabaseLink"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ExternalDatabaseLink

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Chromosome

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Assembly

    curie: Union[str, AssemblyCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, AssemblyCurie):
            self.curie = AssemblyCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class GenomicLocationAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GenomicLocationAssociation
    class_class_curie: ClassVar[str] = "alliance:GenomicLocationAssociation"
    class_name: ClassVar[str] = "GenomicLocationAssociation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GenomicLocationAssociation

    internal: Union[bool, Bool] = None
    has_assembly: Union[str, AssemblyCurie] = None
    subject: Union[str, GenomicEntityCurie] = None
    object: Union[str, ChromosomeCurie] = None
    predicate: str = None
    start: Optional[int] = None
    end: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.has_assembly):
            self.MissingRequiredField("has_assembly")
        if not isinstance(self.has_assembly, AssemblyCurie):
            self.has_assembly = AssemblyCurie(self.has_assembly)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GenomicEntityCurie):
            self.subject = GenomicEntityCurie(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ChromosomeCurie):
            self.object = ChromosomeCurie(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self.start is not None and not isinstance(self.start, int):
            self.start = int(self.start)

        if self.end is not None and not isinstance(self.end, int):
            self.end = int(self.end)

        super().__post_init__(**kwargs)


@dataclass
class GenomicLocationAssociationDTO(AuditedObjectDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GenomicLocationAssociationDTO
    class_class_curie: ClassVar[str] = "alliance:GenomicLocationAssociationDTO"
    class_name: ClassVar[str] = "GenomicLocationAssociationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GenomicLocationAssociationDTO

    internal: Union[bool, Bool] = None
    genomic_entity_curie: str = None
    predicate_name: str = None
    chromosome_curie: str = None
    assembly_curie: str = None
    start: int = None
    end: int = None
    evidence_curies: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.genomic_entity_curie):
            self.MissingRequiredField("genomic_entity_curie")
        if not isinstance(self.genomic_entity_curie, str):
            self.genomic_entity_curie = str(self.genomic_entity_curie)

        if self._is_empty(self.predicate_name):
            self.MissingRequiredField("predicate_name")
        if not isinstance(self.predicate_name, str):
            self.predicate_name = str(self.predicate_name)

        if self._is_empty(self.chromosome_curie):
            self.MissingRequiredField("chromosome_curie")
        if not isinstance(self.chromosome_curie, str):
            self.chromosome_curie = str(self.chromosome_curie)

        if self._is_empty(self.assembly_curie):
            self.MissingRequiredField("assembly_curie")
        if not isinstance(self.assembly_curie, str):
            self.assembly_curie = str(self.assembly_curie)

        if self._is_empty(self.start):
            self.MissingRequiredField("start")
        if not isinstance(self.start, int):
            self.start = int(self.start)

        if self._is_empty(self.end):
            self.MissingRequiredField("end")
        if not isinstance(self.end, int):
            self.end = int(self.end)

        if not isinstance(self.evidence_curies, list):
            self.evidence_curies = [self.evidence_curies] if self.evidence_curies is not None else []
        self.evidence_curies = [v if isinstance(v, str) else str(v) for v in self.evidence_curies]

        super().__post_init__(**kwargs)


@dataclass
class Protein(GenomicEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Protein
    class_class_curie: ClassVar[str] = "alliance:Protein"
    class_name: ClassVar[str] = "Protein"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Protein

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
class Identifier(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Identifier
    class_class_curie: ClassVar[str] = "alliance:Identifier"
    class_name: ClassVar[str] = "Identifier"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Identifier

    curie: Union[str, IdentifierCurie] = None
    counter: Optional[int] = None
    subdomain_code: Optional[str] = None
    subdomain_name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, IdentifierCurie):
            self.curie = IdentifierCurie(self.curie)

        if self.counter is not None and not isinstance(self.counter, int):
            self.counter = int(self.counter)

        if self.subdomain_code is not None and not isinstance(self.subdomain_code, str):
            self.subdomain_code = str(self.subdomain_code)

        if self.subdomain_name is not None and not isinstance(self.subdomain_name, str):
            self.subdomain_name = str(self.subdomain_name)

        super().__post_init__(**kwargs)


@dataclass
class IdentifiersRange(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.IdentifiersRange
    class_class_curie: ClassVar[str] = "alliance:IdentifiersRange"
    class_name: ClassVar[str] = "IdentifiersRange"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.IdentifiersRange

    first: Optional[Union[str, IdentifierCurie]] = None
    last: Optional[Union[str, IdentifierCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.first is not None and not isinstance(self.first, IdentifierCurie):
            self.first = IdentifierCurie(self.first)

        if self.last is not None and not isinstance(self.last, IdentifierCurie):
            self.last = IdentifierCurie(self.last)

        super().__post_init__(**kwargs)


@dataclass
class Gene(GenomicEntity):
    """
    A DNA genomic entity from which one or more functional* RNA transcript molecules are transcribed, along with
    cis-regulatory elements responsible for regulating expression (transcription) of the gene. * A functional RNA
    molecule here can mean one that is directly responsible for the gene's function (e.g. catalysis, structure, etc.)
    or one that is translated to produce a functional polypeptide/protein. A pseudogene may be considered a gene under
    this definition, albeit no longer functional.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Gene
    class_class_curie: ClassVar[str] = "alliance:Gene"
    class_name: ClassVar[str] = "Gene"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Gene

    curie: Union[str, GeneCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None
    gene_symbol: Union[dict, "GeneSymbolSlotAnnotation"] = None
    gene_full_name: Optional[Union[dict, "GeneFullNameSlotAnnotation"]] = None
    gene_systematic_name: Optional[Union[dict, "GeneSystematicNameSlotAnnotation"]] = None
    gene_synonyms: Optional[Union[Union[dict, "GeneSynonymSlotAnnotation"], List[Union[dict, "GeneSynonymSlotAnnotation"]]]] = empty_list()
    related_notes: Optional[Union[Union[dict, Note], List[Union[dict, Note]]]] = empty_list()
    gene_type: Optional[Union[str, SOTermCurie]] = None
    gene_types_secondary: Optional[Union[Union[str, SOTermCurie], List[Union[str, SOTermCurie]]]] = empty_list()
    designating_laboratories: Optional[Union[Union[str, LaboratoryCurie], List[Union[str, LaboratoryCurie]]]] = empty_list()
    designating_persons: Optional[Union[str, List[str]]] = empty_list()
    trans_splice_leaders: Optional[Union[str, List[str]]] = empty_list()
    contig: Optional[Union[str, List[str]]] = empty_list()
    anatomy_function: Optional[Union[str, List[str]]] = empty_list()
    product_binds_matrix: Optional[Union[str, List[str]]] = empty_list()
    wbprocess: Optional[Union[str, List[str]]] = empty_list()
    transposon_origin: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, GeneCurie):
            self.curie = GeneCurie(self.curie)

        if self._is_empty(self.gene_symbol):
            self.MissingRequiredField("gene_symbol")
        if not isinstance(self.gene_symbol, GeneSymbolSlotAnnotation):
            self.gene_symbol = GeneSymbolSlotAnnotation(**as_dict(self.gene_symbol))

        if self.gene_full_name is not None and not isinstance(self.gene_full_name, GeneFullNameSlotAnnotation):
            self.gene_full_name = GeneFullNameSlotAnnotation(**as_dict(self.gene_full_name))

        if self.gene_systematic_name is not None and not isinstance(self.gene_systematic_name, GeneSystematicNameSlotAnnotation):
            self.gene_systematic_name = GeneSystematicNameSlotAnnotation(**as_dict(self.gene_systematic_name))

        self._normalize_inlined_as_dict(slot_name="gene_synonyms", slot_type=GeneSynonymSlotAnnotation, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="related_notes", slot_type=Note, key_name="internal", keyed=False)

        if self.gene_type is not None and not isinstance(self.gene_type, SOTermCurie):
            self.gene_type = SOTermCurie(self.gene_type)

        if not isinstance(self.gene_types_secondary, list):
            self.gene_types_secondary = [self.gene_types_secondary] if self.gene_types_secondary is not None else []
        self.gene_types_secondary = [v if isinstance(v, SOTermCurie) else SOTermCurie(v) for v in self.gene_types_secondary]

        if not isinstance(self.designating_laboratories, list):
            self.designating_laboratories = [self.designating_laboratories] if self.designating_laboratories is not None else []
        self.designating_laboratories = [v if isinstance(v, LaboratoryCurie) else LaboratoryCurie(v) for v in self.designating_laboratories]

        if not isinstance(self.designating_persons, list):
            self.designating_persons = [self.designating_persons] if self.designating_persons is not None else []
        self.designating_persons = [v if isinstance(v, str) else str(v) for v in self.designating_persons]

        if not isinstance(self.trans_splice_leaders, list):
            self.trans_splice_leaders = [self.trans_splice_leaders] if self.trans_splice_leaders is not None else []
        self.trans_splice_leaders = [v if isinstance(v, str) else str(v) for v in self.trans_splice_leaders]

        if not isinstance(self.contig, list):
            self.contig = [self.contig] if self.contig is not None else []
        self.contig = [v if isinstance(v, str) else str(v) for v in self.contig]

        if not isinstance(self.anatomy_function, list):
            self.anatomy_function = [self.anatomy_function] if self.anatomy_function is not None else []
        self.anatomy_function = [v if isinstance(v, str) else str(v) for v in self.anatomy_function]

        if not isinstance(self.product_binds_matrix, list):
            self.product_binds_matrix = [self.product_binds_matrix] if self.product_binds_matrix is not None else []
        self.product_binds_matrix = [v if isinstance(v, str) else str(v) for v in self.product_binds_matrix]

        if not isinstance(self.wbprocess, list):
            self.wbprocess = [self.wbprocess] if self.wbprocess is not None else []
        self.wbprocess = [v if isinstance(v, str) else str(v) for v in self.wbprocess]

        if self.transposon_origin is not None and not isinstance(self.transposon_origin, Bool):
            self.transposon_origin = Bool(self.transposon_origin)

        super().__post_init__(**kwargs)


@dataclass
class GeneDTO(GenomicEntityDTO):
    """
    Ingest class for genes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GeneDTO
    class_class_curie: ClassVar[str] = "alliance:GeneDTO"
    class_name: ClassVar[str] = "GeneDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GeneDTO

    curie: Union[str, GeneDTOCurie] = None
    internal: Union[bool, Bool] = None
    taxon_curie: str = None
    gene_symbol_dto: Union[dict, SymbolSlotAnnotationDTO] = None
    gene_full_name_dto: Optional[Union[dict, FullNameSlotAnnotationDTO]] = None
    gene_systematic_name_dto: Optional[Union[dict, SystematicNameSlotAnnotationDTO]] = None
    gene_synonym_dtos: Optional[Union[Union[dict, NameSlotAnnotationDTO], List[Union[dict, NameSlotAnnotationDTO]]]] = empty_list()
    gene_type_curie: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, GeneDTOCurie):
            self.curie = GeneDTOCurie(self.curie)

        if self._is_empty(self.gene_symbol_dto):
            self.MissingRequiredField("gene_symbol_dto")
        if not isinstance(self.gene_symbol_dto, SymbolSlotAnnotationDTO):
            self.gene_symbol_dto = SymbolSlotAnnotationDTO(**as_dict(self.gene_symbol_dto))

        if self.gene_full_name_dto is not None and not isinstance(self.gene_full_name_dto, FullNameSlotAnnotationDTO):
            self.gene_full_name_dto = FullNameSlotAnnotationDTO(**as_dict(self.gene_full_name_dto))

        if self.gene_systematic_name_dto is not None and not isinstance(self.gene_systematic_name_dto, SystematicNameSlotAnnotationDTO):
            self.gene_systematic_name_dto = SystematicNameSlotAnnotationDTO(**as_dict(self.gene_systematic_name_dto))

        if not isinstance(self.gene_synonym_dtos, list):
            self.gene_synonym_dtos = [self.gene_synonym_dtos] if self.gene_synonym_dtos is not None else []
        self.gene_synonym_dtos = [v if isinstance(v, NameSlotAnnotationDTO) else NameSlotAnnotationDTO(**as_dict(v)) for v in self.gene_synonym_dtos]

        if self.gene_type_curie is not None and not isinstance(self.gene_type_curie, str):
            self.gene_type_curie = str(self.gene_type_curie)

        super().__post_init__(**kwargs)


@dataclass
class GeneSymbolSlotAnnotation(NameSlotAnnotation):
    """
    The one current symbol for the gene.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GeneSymbolSlotAnnotation
    class_class_curie: ClassVar[str] = "alliance:GeneSymbolSlotAnnotation"
    class_name: ClassVar[str] = "GeneSymbolSlotAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GeneSymbolSlotAnnotation

    internal: Union[bool, Bool] = None
    format_text: str = None
    display_text: str = None
    single_gene: Union[str, GeneCurie] = None
    name_type: Union[str, VocabularyTermName] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.single_gene):
            self.MissingRequiredField("single_gene")
        if not isinstance(self.single_gene, GeneCurie):
            self.single_gene = GeneCurie(self.single_gene)

        if self._is_empty(self.name_type):
            self.MissingRequiredField("name_type")
        if not isinstance(self.name_type, VocabularyTermName):
            self.name_type = VocabularyTermName(self.name_type)

        super().__post_init__(**kwargs)


@dataclass
class GeneFullNameSlotAnnotation(NameSlotAnnotation):
    """
    The one current full name for the gene.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GeneFullNameSlotAnnotation
    class_class_curie: ClassVar[str] = "alliance:GeneFullNameSlotAnnotation"
    class_name: ClassVar[str] = "GeneFullNameSlotAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GeneFullNameSlotAnnotation

    internal: Union[bool, Bool] = None
    format_text: str = None
    display_text: str = None
    single_gene: Union[str, GeneCurie] = None
    name_type: Union[str, VocabularyTermName] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.single_gene):
            self.MissingRequiredField("single_gene")
        if not isinstance(self.single_gene, GeneCurie):
            self.single_gene = GeneCurie(self.single_gene)

        if self._is_empty(self.name_type):
            self.MissingRequiredField("name_type")
        if not isinstance(self.name_type, VocabularyTermName):
            self.name_type = VocabularyTermName(self.name_type)

        super().__post_init__(**kwargs)


@dataclass
class GeneSystematicNameSlotAnnotation(NameSlotAnnotation):
    """
    The one current systematic name for the gene.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GeneSystematicNameSlotAnnotation
    class_class_curie: ClassVar[str] = "alliance:GeneSystematicNameSlotAnnotation"
    class_name: ClassVar[str] = "GeneSystematicNameSlotAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GeneSystematicNameSlotAnnotation

    internal: Union[bool, Bool] = None
    format_text: str = None
    display_text: str = None
    single_gene: Union[str, GeneCurie] = None
    name_type: Union[str, VocabularyTermName] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.single_gene):
            self.MissingRequiredField("single_gene")
        if not isinstance(self.single_gene, GeneCurie):
            self.single_gene = GeneCurie(self.single_gene)

        if self._is_empty(self.name_type):
            self.MissingRequiredField("name_type")
        if not isinstance(self.name_type, VocabularyTermName):
            self.name_type = VocabularyTermName(self.name_type)

        super().__post_init__(**kwargs)


@dataclass
class GeneSynonymSlotAnnotation(NameSlotAnnotation):
    """
    All aliases (non-preferred names) for the gene. Any type of synonym is acceptable.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GeneSynonymSlotAnnotation
    class_class_curie: ClassVar[str] = "alliance:GeneSynonymSlotAnnotation"
    class_name: ClassVar[str] = "GeneSynonymSlotAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GeneSynonymSlotAnnotation

    internal: Union[bool, Bool] = None
    name_type: Union[str, VocabularyTermName] = None
    format_text: str = None
    display_text: str = None
    single_gene: Union[str, GeneCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.single_gene):
            self.MissingRequiredField("single_gene")
        if not isinstance(self.single_gene, GeneCurie):
            self.single_gene = GeneCurie(self.single_gene)

        super().__post_init__(**kwargs)


@dataclass
class GeneticMapPosition(GenomicEntity):
    """
    A genetic map position.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GeneticMapPosition
    class_class_curie: ClassVar[str] = "alliance:GeneticMapPosition"
    class_name: ClassVar[str] = "GeneticMapPosition"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GeneticMapPosition

    curie: Union[str, GeneticMapPositionCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None
    genetic_map_chromosome: Optional[Union[str, ChromosomeCurie]] = None
    genetic_map_band: Optional[str] = None
    genetic_map_position_centimorgan: Optional[Union[float, List[float]]] = empty_list()
    genetic_map_position_centimorgan_error: Optional[Union[float, List[float]]] = empty_list()
    genetic_map_position_radiation: Optional[Union[float, List[float]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, GeneticMapPositionCurie):
            self.curie = GeneticMapPositionCurie(self.curie)

        if self.genetic_map_chromosome is not None and not isinstance(self.genetic_map_chromosome, ChromosomeCurie):
            self.genetic_map_chromosome = ChromosomeCurie(self.genetic_map_chromosome)

        if self.genetic_map_band is not None and not isinstance(self.genetic_map_band, str):
            self.genetic_map_band = str(self.genetic_map_band)

        if not isinstance(self.genetic_map_position_centimorgan, list):
            self.genetic_map_position_centimorgan = [self.genetic_map_position_centimorgan] if self.genetic_map_position_centimorgan is not None else []
        self.genetic_map_position_centimorgan = [v if isinstance(v, float) else float(v) for v in self.genetic_map_position_centimorgan]

        if not isinstance(self.genetic_map_position_centimorgan_error, list):
            self.genetic_map_position_centimorgan_error = [self.genetic_map_position_centimorgan_error] if self.genetic_map_position_centimorgan_error is not None else []
        self.genetic_map_position_centimorgan_error = [v if isinstance(v, float) else float(v) for v in self.genetic_map_position_centimorgan_error]

        if not isinstance(self.genetic_map_position_radiation, list):
            self.genetic_map_position_radiation = [self.genetic_map_position_radiation] if self.genetic_map_position_radiation is not None else []
        self.genetic_map_position_radiation = [v if isinstance(v, float) else float(v) for v in self.genetic_map_position_radiation]

        super().__post_init__(**kwargs)


@dataclass
class GeneHistory(AuditedObject):
    """
    The history of a gene
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GeneHistory
    class_class_curie: ClassVar[str] = "alliance:GeneHistory"
    class_name: ClassVar[str] = "GeneHistory"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GeneHistory

    internal: Union[bool, Bool] = None
    current_status: Optional[Union[str, List[str]]] = empty_list()
    current_version: Optional[int] = None
    merged_into: Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]] = empty_list()
    acquires_merge: Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]] = empty_list()
    split_from: Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]] = empty_list()
    split_into: Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.current_status, list):
            self.current_status = [self.current_status] if self.current_status is not None else []
        self.current_status = [v if isinstance(v, str) else str(v) for v in self.current_status]

        if self.current_version is not None and not isinstance(self.current_version, int):
            self.current_version = int(self.current_version)

        if not isinstance(self.merged_into, list):
            self.merged_into = [self.merged_into] if self.merged_into is not None else []
        self.merged_into = [v if isinstance(v, GeneCurie) else GeneCurie(v) for v in self.merged_into]

        if not isinstance(self.acquires_merge, list):
            self.acquires_merge = [self.acquires_merge] if self.acquires_merge is not None else []
        self.acquires_merge = [v if isinstance(v, GeneCurie) else GeneCurie(v) for v in self.acquires_merge]

        if not isinstance(self.split_from, list):
            self.split_from = [self.split_from] if self.split_from is not None else []
        self.split_from = [v if isinstance(v, GeneCurie) else GeneCurie(v) for v in self.split_from]

        if not isinstance(self.split_into, list):
            self.split_into = [self.split_into] if self.split_into is not None else []
        self.split_into = [v if isinstance(v, GeneCurie) else GeneCurie(v) for v in self.split_into]

        super().__post_init__(**kwargs)


@dataclass
class InformationContentEntity(AuditedObject):
    """
    a piece of information that typically is used as support for an assertion or annotation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.InformationContentEntity
    class_class_curie: ClassVar[str] = "alliance:InformationContentEntity"
    class_name: ClassVar[str] = "InformationContentEntity"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.InformationContentEntity

    curie: Union[str, InformationContentEntityCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, InformationContentEntityCurie):
            self.curie = InformationContentEntityCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class AuthorReference(AuditedObject):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AuthorReference
    class_class_curie: ClassVar[str] = "alliance:AuthorReference"
    class_name: ClassVar[str] = "AuthorReference"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AuthorReference

    internal: Union[bool, Bool] = None
    corresponding_author: Optional[Union[bool, Bool]] = None
    first_author: Optional[Union[bool, Bool]] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    cross_references: Optional[Union[Union[dict, CrossReference], List[Union[dict, CrossReference]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.corresponding_author is not None and not isinstance(self.corresponding_author, Bool):
            self.corresponding_author = Bool(self.corresponding_author)

        if self.first_author is not None and not isinstance(self.first_author, Bool):
            self.first_author = Bool(self.first_author)

        if self.first_name is not None and not isinstance(self.first_name, str):
            self.first_name = str(self.first_name)

        if self.last_name is not None and not isinstance(self.last_name, str):
            self.last_name = str(self.last_name)

        self._normalize_inlined_as_dict(slot_name="cross_references", slot_type=CrossReference, key_name="internal", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class Reference(InformationContentEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Reference
    class_class_curie: ClassVar[str] = "alliance:Reference"
    class_name: ClassVar[str] = "Reference"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Reference

    curie: Union[str, ReferenceCurie] = None
    internal: Union[bool, Bool] = None
    reference_id: int = None
    abstract: Optional[str] = None
    authors: Optional[Union[Union[dict, AuthorReference], List[Union[dict, AuthorReference]]]] = empty_list()
    category: Optional[Union[str, "ReferenceCategoryEnum"]] = None
    date_arrived_in_pubmed: Optional[Union[str, List[str]]] = empty_list()
    date_last_modified_in_pubmed: Optional[str] = None
    date_published: Optional[str] = None
    issue_name: Optional[str] = None
    keywords: Optional[Union[str, List[str]]] = empty_list()
    language: Optional[str] = None
    merged_into_id: Optional[Union[str, URIorCURIE]] = None
    open_access: Optional[Union[bool, Bool]] = None
    page_range: Optional[str] = None
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

        self._normalize_inlined_as_dict(slot_name="authors", slot_type=AuthorReference, key_name="internal", keyed=False)

        if self.category is not None and not isinstance(self.category, ReferenceCategoryEnum):
            self.category = ReferenceCategoryEnum(self.category)

        if not isinstance(self.date_arrived_in_pubmed, list):
            self.date_arrived_in_pubmed = [self.date_arrived_in_pubmed] if self.date_arrived_in_pubmed is not None else []
        self.date_arrived_in_pubmed = [v if isinstance(v, str) else str(v) for v in self.date_arrived_in_pubmed]

        if self.date_last_modified_in_pubmed is not None and not isinstance(self.date_last_modified_in_pubmed, str):
            self.date_last_modified_in_pubmed = str(self.date_last_modified_in_pubmed)

        if self.date_published is not None and not isinstance(self.date_published, str):
            self.date_published = str(self.date_published)

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

        if self.page_range is not None and not isinstance(self.page_range, str):
            self.page_range = str(self.page_range)

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
class PersonalCommunication(InformationContentEntity):
    """
    a piece of information that is used to support an assertion or annotation, where the information comes from a
    person other than the author of the assertion or annotation, or the author of the reference.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.PersonalCommunication
    class_class_curie: ClassVar[str] = "alliance:PersonalCommunication"
    class_name: ClassVar[str] = "PersonalCommunication"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.PersonalCommunication

    curie: Union[str, PersonalCommunicationCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, PersonalCommunicationCurie):
            self.curie = PersonalCommunicationCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class MeshDetail(AuditedObject):
    """
    Medical Subject Headings information coming from PubMed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.MeshDetail
    class_class_curie: ClassVar[str] = "alliance:MeshDetail"
    class_name: ClassVar[str] = "MeshDetail"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.MeshDetail

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
class AffectedGenomicModel(GenomicEntity):
    """
    Includes inbred strains, stocks, disease models and mutant genotypes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AffectedGenomicModel
    class_class_curie: ClassVar[str] = "alliance:AffectedGenomicModel"
    class_name: ClassVar[str] = "AffectedGenomicModel"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AffectedGenomicModel

    curie: Union[str, AffectedGenomicModelCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None
    subtype: Union[str, VocabularyTermName] = None
    name: Optional[str] = None
    components: Optional[Union[Union[dict, "AffectedGenomicModelComponent"], List[Union[dict, "AffectedGenomicModelComponent"]]]] = empty_list()
    sequence_targeting_reagents: Optional[Union[Union[str, SequenceTargetingReagentCurie], List[Union[str, SequenceTargetingReagentCurie]]]] = empty_list()
    parental_populations: Optional[Union[str, URIorCURIE]] = None
    data_provider: Optional[Union[dict, DataProvider]] = None
    references: Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, AffectedGenomicModelCurie):
            self.curie = AffectedGenomicModelCurie(self.curie)

        if self._is_empty(self.subtype):
            self.MissingRequiredField("subtype")
        if not isinstance(self.subtype, VocabularyTermName):
            self.subtype = VocabularyTermName(self.subtype)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        self._normalize_inlined_as_dict(slot_name="components", slot_type=AffectedGenomicModelComponent, key_name="internal", keyed=False)

        if not isinstance(self.sequence_targeting_reagents, list):
            self.sequence_targeting_reagents = [self.sequence_targeting_reagents] if self.sequence_targeting_reagents is not None else []
        self.sequence_targeting_reagents = [v if isinstance(v, SequenceTargetingReagentCurie) else SequenceTargetingReagentCurie(v) for v in self.sequence_targeting_reagents]

        if self.parental_populations is not None and not isinstance(self.parental_populations, URIorCURIE):
            self.parental_populations = URIorCURIE(self.parental_populations)

        if self.data_provider is not None and not isinstance(self.data_provider, DataProvider):
            self.data_provider = DataProvider(**as_dict(self.data_provider))

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, ReferenceCurie) else ReferenceCurie(v) for v in self.references]

        super().__post_init__(**kwargs)


@dataclass
class AffectedGenomicModelDTO(GenomicEntityDTO):
    """
    Ingest class for AGMs
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AffectedGenomicModelDTO
    class_class_curie: ClassVar[str] = "alliance:AffectedGenomicModelDTO"
    class_name: ClassVar[str] = "AffectedGenomicModelDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AffectedGenomicModelDTO

    curie: Union[str, AffectedGenomicModelDTOCurie] = None
    internal: Union[bool, Bool] = None
    taxon_curie: str = None
    subtype_name: str = None
    name: Optional[str] = None
    reference_curies: Optional[Union[str, List[str]]] = empty_list()
    data_provider_dto: Optional[Union[dict, DataProviderDTO]] = None
    sequence_targeting_reagent_curies: Optional[Union[str, List[str]]] = empty_list()
    component_dtos: Optional[Union[Union[dict, "AffectedGenomicModelComponentDTO"], List[Union[dict, "AffectedGenomicModelComponentDTO"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, AffectedGenomicModelDTOCurie):
            self.curie = AffectedGenomicModelDTOCurie(self.curie)

        if self._is_empty(self.subtype_name):
            self.MissingRequiredField("subtype_name")
        if not isinstance(self.subtype_name, str):
            self.subtype_name = str(self.subtype_name)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.reference_curies, list):
            self.reference_curies = [self.reference_curies] if self.reference_curies is not None else []
        self.reference_curies = [v if isinstance(v, str) else str(v) for v in self.reference_curies]

        if self.data_provider_dto is not None and not isinstance(self.data_provider_dto, DataProviderDTO):
            self.data_provider_dto = DataProviderDTO(**as_dict(self.data_provider_dto))

        if not isinstance(self.sequence_targeting_reagent_curies, list):
            self.sequence_targeting_reagent_curies = [self.sequence_targeting_reagent_curies] if self.sequence_targeting_reagent_curies is not None else []
        self.sequence_targeting_reagent_curies = [v if isinstance(v, str) else str(v) for v in self.sequence_targeting_reagent_curies]

        if not isinstance(self.component_dtos, list):
            self.component_dtos = [self.component_dtos] if self.component_dtos is not None else []
        self.component_dtos = [v if isinstance(v, AffectedGenomicModelComponentDTO) else AffectedGenomicModelComponentDTO(**as_dict(v)) for v in self.component_dtos]

        super().__post_init__(**kwargs)


@dataclass
class AffectedGenomicModelComponent(AuditedObject):
    """
    Allele that affects the model and its zygosity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AffectedGenomicModelComponent
    class_class_curie: ClassVar[str] = "alliance:AffectedGenomicModelComponent"
    class_name: ClassVar[str] = "AffectedGenomicModelComponent"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AffectedGenomicModelComponent

    internal: Union[bool, Bool] = None
    single_allele: Optional[Union[str, AlleleCurie]] = None
    zygosity: Optional[Union[str, "ZygosityValues"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.single_allele is not None and not isinstance(self.single_allele, AlleleCurie):
            self.single_allele = AlleleCurie(self.single_allele)

        if self.zygosity is not None and not isinstance(self.zygosity, ZygosityValues):
            self.zygosity = ZygosityValues(self.zygosity)

        super().__post_init__(**kwargs)


@dataclass
class AffectedGenomicModelComponentDTO(AuditedObjectDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AffectedGenomicModelComponentDTO
    class_class_curie: ClassVar[str] = "alliance:AffectedGenomicModelComponentDTO"
    class_name: ClassVar[str] = "AffectedGenomicModelComponentDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AffectedGenomicModelComponentDTO

    internal: Union[bool, Bool] = None
    allele_curie: str = None
    zygosity_curie: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.allele_curie):
            self.MissingRequiredField("allele_curie")
        if not isinstance(self.allele_curie, str):
            self.allele_curie = str(self.allele_curie)

        if self.zygosity_curie is not None and not isinstance(self.zygosity_curie, str):
            self.zygosity_curie = str(self.zygosity_curie)

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Agent

    internal: Union[bool, Bool] = None

@dataclass
class Organization(Agent):
    """
    An organization that provides information and/or materials to the Alliance. This includes Alliance member
    organizations (see AllianceMember subclass).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Organization
    class_class_curie: ClassVar[str] = "alliance:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Organization

    internal: Union[bool, Bool] = None
    full_name: str = None
    short_name: str = None
    abbreviation: Optional[str] = None
    homepage_resource_descriptor_page: Optional[Union[dict, "ResourceDescriptorPage"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.full_name):
            self.MissingRequiredField("full_name")
        if not isinstance(self.full_name, str):
            self.full_name = str(self.full_name)

        if self._is_empty(self.short_name):
            self.MissingRequiredField("short_name")
        if not isinstance(self.short_name, str):
            self.short_name = str(self.short_name)

        if self.abbreviation is not None and not isinstance(self.abbreviation, str):
            self.abbreviation = str(self.abbreviation)

        if self.homepage_resource_descriptor_page is not None and not isinstance(self.homepage_resource_descriptor_page, ResourceDescriptorPage):
            self.homepage_resource_descriptor_page = ResourceDescriptorPage(**as_dict(self.homepage_resource_descriptor_page))

        super().__post_init__(**kwargs)


@dataclass
class Laboratory(Organization):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Laboratory
    class_class_curie: ClassVar[str] = "alliance:Laboratory"
    class_name: ClassVar[str] = "Laboratory"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Laboratory

    curie: Union[str, LaboratoryCurie] = None
    internal: Union[bool, Bool] = None
    full_name: str = None
    short_name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, LaboratoryCurie):
            self.curie = LaboratoryCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class Company(Organization):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Company
    class_class_curie: ClassVar[str] = "alliance:Company"
    class_name: ClassVar[str] = "Company"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Company

    internal: Union[bool, Bool] = None
    full_name: str = None
    short_name: str = None

@dataclass
class Person(Agent):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Person
    class_class_curie: ClassVar[str] = "alliance:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Person

    unique_id: Union[str, PersonUniqueId] = None
    internal: Union[bool, Bool] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    first_name: Optional[str] = None
    orcid: Optional[Union[str, URIorCURIE]] = None
    emails: Optional[Union[str, List[str]]] = empty_list()
    old_emails: Optional[Union[str, List[str]]] = empty_list()
    mod_entity_id: Optional[str] = None
    affiliated_alliance_member: Optional[Union[dict, "AllianceMember"]] = None

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

        if self.affiliated_alliance_member is not None and not isinstance(self.affiliated_alliance_member, AllianceMember):
            self.affiliated_alliance_member = AllianceMember(**as_dict(self.affiliated_alliance_member))

        super().__post_init__(**kwargs)


@dataclass
class LoggedInPerson(Person):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.LoggedInPerson
    class_class_curie: ClassVar[str] = "alliance:LoggedInPerson"
    class_name: ClassVar[str] = "LoggedInPerson"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.LoggedInPerson

    unique_id: Union[str, LoggedInPersonUniqueId] = None
    internal: Union[bool, Bool] = None
    okta_id: str = None
    okta_email: str = None
    user_settings: Optional[str] = None
    api_token: Optional[str] = None

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

        if self.user_settings is not None and not isinstance(self.user_settings, str):
            self.user_settings = str(self.user_settings)

        if self.api_token is not None and not isinstance(self.api_token, str):
            self.api_token = str(self.api_token)

        super().__post_init__(**kwargs)


@dataclass
class Figure(AuditedObject):
    """
    An entity representing a figure or table in a publication.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Figure
    class_class_curie: ClassVar[str] = "alliance:Figure"
    class_name: ClassVar[str] = "Figure"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Figure

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.File
    class_class_curie: ClassVar[str] = "alliance:File"
    class_name: ClassVar[str] = "File"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.File

    internal: Union[bool, Bool] = None

@dataclass
class Image(AuditedObject):
    """
    The set of files and metadata that constitute an image.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Image
    class_class_curie: ClassVar[str] = "alliance:Image"
    class_name: ClassVar[str] = "Image"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Image

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ImagePane
    class_class_curie: ClassVar[str] = "alliance:ImagePane"
    class_name: ClassVar[str] = "ImagePane"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ImagePane

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
class VocabularyTerm(AuditedObject):
    """
    A concept or class in a simple vocabulary.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.VocabularyTerm
    class_class_curie: ClassVar[str] = "alliance:VocabularyTerm"
    class_name: ClassVar[str] = "VocabularyTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.VocabularyTerm

    name: Union[str, VocabularyTermName] = None
    internal: Union[bool, Bool] = None
    abbreviation: Optional[str] = None
    definition: Optional[str] = None
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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Vocabulary
    class_class_curie: ClassVar[str] = "alliance:Vocabulary"
    class_name: ClassVar[str] = "Vocabulary"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Vocabulary

    name: Union[str, VocabularyName] = None
    internal: Union[bool, Bool] = None
    vocabulary_description: Optional[str] = None
    member_terms: Optional[Union[Union[str, VocabularyTermName], List[Union[str, VocabularyTermName]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, VocabularyName):
            self.name = VocabularyName(self.name)

        if self.vocabulary_description is not None and not isinstance(self.vocabulary_description, str):
            self.vocabulary_description = str(self.vocabulary_description)

        if not isinstance(self.member_terms, list):
            self.member_terms = [self.member_terms] if self.member_terms is not None else []
        self.member_terms = [v if isinstance(v, VocabularyTermName) else VocabularyTermName(v) for v in self.member_terms]

        super().__post_init__(**kwargs)


@dataclass
class VocabularyTermSet(AuditedObject):
    """
    A subset of terms from a Vocabulary that are valid for particular applications
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.VocabularyTermSet
    class_class_curie: ClassVar[str] = "alliance:VocabularyTermSet"
    class_name: ClassVar[str] = "VocabularyTermSet"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.VocabularyTermSet

    name: Union[str, VocabularyTermSetName] = None
    internal: Union[bool, Bool] = None
    vocabulary_term_set_vocabulary: Union[str, VocabularyName] = None
    vocabulary_term_set_description: Optional[str] = None
    member_terms: Optional[Union[Union[str, VocabularyTermName], List[Union[str, VocabularyTermName]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, VocabularyTermSetName):
            self.name = VocabularyTermSetName(self.name)

        if self._is_empty(self.vocabulary_term_set_vocabulary):
            self.MissingRequiredField("vocabulary_term_set_vocabulary")
        if not isinstance(self.vocabulary_term_set_vocabulary, VocabularyName):
            self.vocabulary_term_set_vocabulary = VocabularyName(self.vocabulary_term_set_vocabulary)

        if self.vocabulary_term_set_description is not None and not isinstance(self.vocabulary_term_set_description, str):
            self.vocabulary_term_set_description = str(self.vocabulary_term_set_description)

        if not isinstance(self.member_terms, list):
            self.member_terms = [self.member_terms] if self.member_terms is not None else []
        self.member_terms = [v if isinstance(v, VocabularyTermName) else VocabularyTermName(v) for v in self.member_terms]

        super().__post_init__(**kwargs)


@dataclass
class Variant(GenomicEntity):
    """
    A DNA, RNA or protein/polypeptide sequence that differs relative to a designated reference sequence. The sequence
    occurs at a single position or in a range of contiguous nucleotides or amino acids.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Variant
    class_class_curie: ClassVar[str] = "alliance:Variant"
    class_name: ClassVar[str] = "Variant"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Variant

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
        if not isinstance(self.variant_genome_locations, list):
            self.variant_genome_locations = [self.variant_genome_locations] if self.variant_genome_locations is not None else []
        self.variant_genome_locations = [v if isinstance(v, VariantGenomeLocation) else VariantGenomeLocation(**as_dict(v)) for v in self.variant_genome_locations]

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.SourceVariantLocation
    class_class_curie: ClassVar[str] = "alliance:SourceVariantLocation"
    class_name: ClassVar[str] = "SourceVariantLocation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.SourceVariantLocation

    internal: Union[bool, Bool] = None
    single_reference: Union[str, ReferenceCurie] = None
    variant_locations: Optional[Union[Union[dict, "VariantLocation"], List[Union[dict, "VariantLocation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.single_reference):
            self.MissingRequiredField("single_reference")
        if not isinstance(self.single_reference, ReferenceCurie):
            self.single_reference = ReferenceCurie(self.single_reference)

        self._normalize_inlined_as_dict(slot_name="variant_locations", slot_type=VariantLocation, key_name="internal", keyed=False)

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.VariantLocation
    class_class_curie: ClassVar[str] = "alliance:VariantLocation"
    class_name: ClassVar[str] = "VariantLocation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.VariantLocation

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.VariantGenomeLocation
    class_class_curie: ClassVar[str] = "alliance:VariantGenomeLocation"
    class_name: ClassVar[str] = "VariantGenomeLocation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.VariantGenomeLocation

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.VariantTranscriptLocation
    class_class_curie: ClassVar[str] = "alliance:VariantTranscriptLocation"
    class_name: ClassVar[str] = "VariantTranscriptLocation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.VariantTranscriptLocation

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.VariantPolypeptideLocation
    class_class_curie: ClassVar[str] = "alliance:VariantPolypeptideLocation"
    class_name: ClassVar[str] = "VariantPolypeptideLocation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.VariantPolypeptideLocation

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
class OntologyTerm(AuditedObject):
    """
    A concept or class in an ontology, vocabulary or thesaurus. Note, ontology terms can be found in multiple
    ontologies (ie: mireoting). defining_slots helps define an alternative key for ontology terms.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.OntologyTerm
    class_class_curie: ClassVar[str] = "alliance:OntologyTerm"
    class_name: ClassVar[str] = "OntologyTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.OntologyTerm

    curie: Union[str, OntologyTermCurie] = None
    internal: Union[bool, Bool] = None
    dbkey: Optional[str] = None
    name: Optional[str] = None
    definition: Optional[str] = None
    definition_urls: Optional[Union[str, List[str]]] = empty_list()
    type: Optional[Union[str, URIorCURIE]] = None
    cross_references: Optional[Union[Union[dict, CrossReference], List[Union[dict, CrossReference]]]] = empty_list()
    synonyms: Optional[Union[str, List[str]]] = empty_list()
    namespace: Optional[str] = None
    subsets: Optional[Union[str, List[str]]] = empty_list()
    secondary_identifiers: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    ancestors: Optional[Union[Union[dict, "OntologyTermClosure"], List[Union[dict, "OntologyTermClosure"]]]] = empty_list()
    descendants: Optional[Union[Union[dict, "OntologyTermClosure"], List[Union[dict, "OntologyTermClosure"]]]] = empty_list()

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

        self._normalize_inlined_as_dict(slot_name="cross_references", slot_type=CrossReference, key_name="internal", keyed=False)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if self.namespace is not None and not isinstance(self.namespace, str):
            self.namespace = str(self.namespace)

        if not isinstance(self.subsets, list):
            self.subsets = [self.subsets] if self.subsets is not None else []
        self.subsets = [v if isinstance(v, str) else str(v) for v in self.subsets]

        if not isinstance(self.secondary_identifiers, list):
            self.secondary_identifiers = [self.secondary_identifiers] if self.secondary_identifiers is not None else []
        self.secondary_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.secondary_identifiers]

        self._normalize_inlined_as_dict(slot_name="ancestors", slot_type=OntologyTermClosure, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="descendants", slot_type=OntologyTermClosure, key_name="internal", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class OntologyTermClosure(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.OntologyTermClosure
    class_class_curie: ClassVar[str] = "alliance:OntologyTermClosure"
    class_name: ClassVar[str] = "OntologyTermClosure"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.OntologyTermClosure

    internal: Union[bool, Bool] = None
    predicate: str = None
    subject: Union[str, OntologyTermCurie] = None
    object: Union[str, OntologyTermCurie] = None
    relationship_type: Optional[Union[str, List[str]]] = empty_list()
    distance_between: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, OntologyTermCurie):
            self.subject = OntologyTermCurie(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, OntologyTermCurie):
            self.object = OntologyTermCurie(self.object)

        if not isinstance(self.relationship_type, list):
            self.relationship_type = [self.relationship_type] if self.relationship_type is not None else []
        self.relationship_type = [v if isinstance(v, str) else str(v) for v in self.relationship_type]

        if self.distance_between is not None and not isinstance(self.distance_between, int):
            self.distance_between = int(self.distance_between)

        super().__post_init__(**kwargs)


@dataclass
class DOTerm(OntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.DOTerm
    class_class_curie: ClassVar[str] = "alliance:DOTerm"
    class_name: ClassVar[str] = "DOTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.DOTerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ECOTerm
    class_class_curie: ClassVar[str] = "alliance:ECOTerm"
    class_name: ClassVar[str] = "ECOTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ECOTerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.NCBITaxonTerm
    class_class_curie: ClassVar[str] = "alliance:NCBITaxonTerm"
    class_name: ClassVar[str] = "NCBITaxonTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.NCBITaxonTerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.FBCVTerm
    class_class_curie: ClassVar[str] = "alliance:FBCVTerm"
    class_name: ClassVar[str] = "FBCVTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.FBCVTerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GOTerm
    class_class_curie: ClassVar[str] = "alliance:GOTerm"
    class_name: ClassVar[str] = "GOTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GOTerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ROTerm
    class_class_curie: ClassVar[str] = "alliance:ROTerm"
    class_name: ClassVar[str] = "ROTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ROTerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.MITerm
    class_class_curie: ClassVar[str] = "alliance:MITerm"
    class_name: ClassVar[str] = "MITerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.MITerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.MMOTerm
    class_class_curie: ClassVar[str] = "alliance:MMOTerm"
    class_name: ClassVar[str] = "MMOTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.MMOTerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.MMUSDVTerm
    class_class_curie: ClassVar[str] = "alliance:MMUSDVTerm"
    class_name: ClassVar[str] = "MMUSDVTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.MMUSDVTerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.SOTerm
    class_class_curie: ClassVar[str] = "alliance:SOTerm"
    class_name: ClassVar[str] = "SOTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.SOTerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.XBEDTerm
    class_class_curie: ClassVar[str] = "alliance:XBEDTerm"
    class_name: ClassVar[str] = "XBEDTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.XBEDTerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.StageTerm
    class_class_curie: ClassVar[str] = "alliance:StageTerm"
    class_name: ClassVar[str] = "StageTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.StageTerm

    curie: Union[str, StageTermCurie] = None
    internal: Union[bool, Bool] = None

@dataclass
class FBDVTerm(StageTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.FBDVTerm
    class_class_curie: ClassVar[str] = "alliance:FBDVTerm"
    class_name: ClassVar[str] = "FBDVTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.FBDVTerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.WBLSTerm
    class_class_curie: ClassVar[str] = "alliance:WBLSTerm"
    class_name: ClassVar[str] = "WBLSTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.WBLSTerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.XBSTerm
    class_class_curie: ClassVar[str] = "alliance:XBSTerm"
    class_name: ClassVar[str] = "XBSTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.XBSTerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ZFSTerm
    class_class_curie: ClassVar[str] = "alliance:ZFSTerm"
    class_name: ClassVar[str] = "ZFSTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ZFSTerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ExperimentalConditionOntologyTerm
    class_class_curie: ClassVar[str] = "alliance:ExperimentalConditionOntologyTerm"
    class_name: ClassVar[str] = "ExperimentalConditionOntologyTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ExperimentalConditionOntologyTerm

    curie: Union[str, ExperimentalConditionOntologyTermCurie] = None
    internal: Union[bool, Bool] = None

@dataclass
class ZECOTerm(ExperimentalConditionOntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ZECOTerm
    class_class_curie: ClassVar[str] = "alliance:ZECOTerm"
    class_name: ClassVar[str] = "ZECOTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ZECOTerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.XCOTerm
    class_class_curie: ClassVar[str] = "alliance:XCOTerm"
    class_name: ClassVar[str] = "XCOTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.XCOTerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AnatomicalTerm
    class_class_curie: ClassVar[str] = "alliance:AnatomicalTerm"
    class_name: ClassVar[str] = "AnatomicalTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AnatomicalTerm

    curie: Union[str, AnatomicalTermCurie] = None
    internal: Union[bool, Bool] = None

@dataclass
class CLTerm(AnatomicalTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.CLTerm
    class_class_curie: ClassVar[str] = "alliance:CLTerm"
    class_name: ClassVar[str] = "CLTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.CLTerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.EMAPATerm
    class_class_curie: ClassVar[str] = "alliance:EMAPATerm"
    class_name: ClassVar[str] = "EMAPATerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.EMAPATerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.DAOTerm
    class_class_curie: ClassVar[str] = "alliance:DAOTerm"
    class_name: ClassVar[str] = "DAOTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.DAOTerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.MATerm
    class_class_curie: ClassVar[str] = "alliance:MATerm"
    class_name: ClassVar[str] = "MATerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.MATerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.UBERONTerm
    class_class_curie: ClassVar[str] = "alliance:UBERONTerm"
    class_name: ClassVar[str] = "UBERONTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.UBERONTerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.WBBTTerm
    class_class_curie: ClassVar[str] = "alliance:WBBTTerm"
    class_name: ClassVar[str] = "WBBTTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.WBBTTerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.XBATerm
    class_class_curie: ClassVar[str] = "alliance:XBATerm"
    class_name: ClassVar[str] = "XBATerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.XBATerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ZFATerm
    class_class_curie: ClassVar[str] = "alliance:ZFATerm"
    class_name: ClassVar[str] = "ZFATerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ZFATerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.PhenotypeTerm
    class_class_curie: ClassVar[str] = "alliance:PhenotypeTerm"
    class_name: ClassVar[str] = "PhenotypeTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.PhenotypeTerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.XPOTerm
    class_class_curie: ClassVar[str] = "alliance:XPOTerm"
    class_name: ClassVar[str] = "XPOTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.XPOTerm

    curie: Union[str, XPOTermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, XPOTermCurie):
            self.curie = XPOTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class MPTerm(PhenotypeTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.MPTerm
    class_class_curie: ClassVar[str] = "alliance:MPTerm"
    class_name: ClassVar[str] = "MPTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.MPTerm

    curie: Union[str, MPTermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, MPTermCurie):
            self.curie = MPTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class ATPTerm(OntologyTerm):
    """
    An ontology term from the Alliance Tags for Papers ontology (ATP)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ATPTerm
    class_class_curie: ClassVar[str] = "alliance:ATPTerm"
    class_name: ClassVar[str] = "ATPTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ATPTerm

    curie: Union[str, ATPTermCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ATPTermCurie):
            self.curie = ATPTermCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalTerm(OntologyTerm):
    """
    An ontology term representing a chemical or molecule
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ChemicalTerm
    class_class_curie: ClassVar[str] = "alliance:ChemicalTerm"
    class_name: ClassVar[str] = "ChemicalTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ChemicalTerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.CHEBITerm
    class_class_curie: ClassVar[str] = "alliance:CHEBITerm"
    class_name: ClassVar[str] = "CHEBITerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.CHEBITerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.XSMOTerm
    class_class_curie: ClassVar[str] = "alliance:XSMOTerm"
    class_name: ClassVar[str] = "XSMOTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.XSMOTerm

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Molecule
    class_class_curie: ClassVar[str] = "alliance:Molecule"
    class_name: ClassVar[str] = "Molecule"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Molecule

    curie: Union[str, MoleculeCurie] = None
    internal: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, MoleculeCurie):
            self.curie = MoleculeCurie(self.curie)

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
    internal: Union[bool, Bool] = None
    predicate: str = None
    subject: Union[str, BiologicalEntityCurie] = None
    object: str = None
    date_created: Union[str, XSDDateTime] = None
    single_reference: Optional[Union[str, ReferenceCurie]] = None
    phenotype_term: Optional[Union[str, PhenotypeTermCurie]] = None
    condition_relations: Optional[Union[Union[dict, "ConditionRelation"], List[Union[dict, "ConditionRelation"]]]] = empty_list()

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

        if self._is_empty(self.date_created):
            self.MissingRequiredField("date_created")
        if not isinstance(self.date_created, XSDDateTime):
            self.date_created = XSDDateTime(self.date_created)

        if self.single_reference is not None and not isinstance(self.single_reference, ReferenceCurie):
            self.single_reference = ReferenceCurie(self.single_reference)

        if self.phenotype_term is not None and not isinstance(self.phenotype_term, PhenotypeTermCurie):
            self.phenotype_term = PhenotypeTermCurie(self.phenotype_term)

        self._normalize_inlined_as_dict(slot_name="condition_relations", slot_type=ConditionRelation, key_name="internal", keyed=False)

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
    internal: Union[bool, Bool] = None
    predicate: str = None
    object: str = None
    date_created: Union[str, XSDDateTime] = None
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
    internal: Union[bool, Bool] = None
    predicate: str = None
    object: str = None
    date_created: Union[str, XSDDateTime] = None
    subject: Union[str, AlleleCurie] = None
    inferred_gene: Optional[Union[str, GeneCurie]] = None
    asserted_genes: Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]] = empty_list()
    asserted_allele: Optional[Union[str, AlleleCurie]] = None

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

        if not isinstance(self.asserted_genes, list):
            self.asserted_genes = [self.asserted_genes] if self.asserted_genes is not None else []
        self.asserted_genes = [v if isinstance(v, GeneCurie) else GeneCurie(v) for v in self.asserted_genes]

        if self.asserted_allele is not None and not isinstance(self.asserted_allele, AlleleCurie):
            self.asserted_allele = AlleleCurie(self.asserted_allele)

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
    internal: Union[bool, Bool] = None
    predicate: str = None
    object: str = None
    date_created: Union[str, XSDDateTime] = None
    subject: Union[str, AffectedGenomicModelCurie] = None
    inferred_allele: Optional[Union[str, AlleleCurie]] = None
    inferred_gene: Optional[Union[str, GeneCurie]] = None
    asserted_genes: Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]] = empty_list()
    asserted_allele: Optional[Union[str, AlleleCurie]] = None

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

        if not isinstance(self.asserted_genes, list):
            self.asserted_genes = [self.asserted_genes] if self.asserted_genes is not None else []
        self.asserted_genes = [v if isinstance(v, GeneCurie) else GeneCurie(v) for v in self.asserted_genes]

        if self.asserted_allele is not None and not isinstance(self.asserted_allele, AlleleCurie):
            self.asserted_allele = AlleleCurie(self.asserted_allele)

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

    curie: Union[str, DiseaseAnnotationCurie] = None
    internal: Union[bool, Bool] = None
    evidence_codes: Union[Union[str, ECOTermCurie], List[Union[str, ECOTermCurie]]] = None
    single_reference: Union[str, ReferenceCurie] = None
    data_provider: Union[dict, DataProvider] = None
    subject: Union[str, BiologicalEntityCurie] = None
    predicate: str = None
    object: Union[str, DOTermCurie] = None
    unique_id: Optional[str] = None
    mod_entity_id: Optional[str] = None
    negated: Optional[Union[bool, Bool]] = None
    annotation_type: Optional[Union[str, VocabularyTermName]] = None
    with_or_from: Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]] = empty_list()
    disease_qualifiers: Optional[Union[Union[str, VocabularyTermName], List[Union[str, VocabularyTermName]]]] = empty_list()
    condition_relations: Optional[Union[Union[dict, "ConditionRelation"], List[Union[dict, "ConditionRelation"]]]] = empty_list()
    genetic_sex: Optional[Union[str, VocabularyTermName]] = None
    related_notes: Optional[Union[Union[dict, Note], List[Union[dict, Note]]]] = empty_list()
    secondary_data_provider: Optional[Union[dict, DataProvider]] = None
    disease_genetic_modifier: Optional[str] = None
    disease_genetic_modifier_relation: Optional[Union[str, VocabularyTermName]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, DiseaseAnnotationCurie):
            self.curie = DiseaseAnnotationCurie(self.curie)

        if self._is_empty(self.evidence_codes):
            self.MissingRequiredField("evidence_codes")
        if not isinstance(self.evidence_codes, list):
            self.evidence_codes = [self.evidence_codes] if self.evidence_codes is not None else []
        self.evidence_codes = [v if isinstance(v, ECOTermCurie) else ECOTermCurie(v) for v in self.evidence_codes]

        if self._is_empty(self.single_reference):
            self.MissingRequiredField("single_reference")
        if not isinstance(self.single_reference, ReferenceCurie):
            self.single_reference = ReferenceCurie(self.single_reference)

        if self._is_empty(self.data_provider):
            self.MissingRequiredField("data_provider")
        if not isinstance(self.data_provider, DataProvider):
            self.data_provider = DataProvider(**as_dict(self.data_provider))

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

        if self.unique_id is not None and not isinstance(self.unique_id, str):
            self.unique_id = str(self.unique_id)

        if self.mod_entity_id is not None and not isinstance(self.mod_entity_id, str):
            self.mod_entity_id = str(self.mod_entity_id)

        if self.negated is not None and not isinstance(self.negated, Bool):
            self.negated = Bool(self.negated)

        if self.annotation_type is not None and not isinstance(self.annotation_type, VocabularyTermName):
            self.annotation_type = VocabularyTermName(self.annotation_type)

        if not isinstance(self.with_or_from, list):
            self.with_or_from = [self.with_or_from] if self.with_or_from is not None else []
        self.with_or_from = [v if isinstance(v, GeneCurie) else GeneCurie(v) for v in self.with_or_from]

        if not isinstance(self.disease_qualifiers, list):
            self.disease_qualifiers = [self.disease_qualifiers] if self.disease_qualifiers is not None else []
        self.disease_qualifiers = [v if isinstance(v, VocabularyTermName) else VocabularyTermName(v) for v in self.disease_qualifiers]

        self._normalize_inlined_as_dict(slot_name="condition_relations", slot_type=ConditionRelation, key_name="internal", keyed=False)

        if self.genetic_sex is not None and not isinstance(self.genetic_sex, VocabularyTermName):
            self.genetic_sex = VocabularyTermName(self.genetic_sex)

        self._normalize_inlined_as_dict(slot_name="related_notes", slot_type=Note, key_name="internal", keyed=False)

        if self.secondary_data_provider is not None and not isinstance(self.secondary_data_provider, DataProvider):
            self.secondary_data_provider = DataProvider(**as_dict(self.secondary_data_provider))

        if self.disease_genetic_modifier is not None and not isinstance(self.disease_genetic_modifier, str):
            self.disease_genetic_modifier = str(self.disease_genetic_modifier)

        if self.disease_genetic_modifier_relation is not None and not isinstance(self.disease_genetic_modifier_relation, VocabularyTermName):
            self.disease_genetic_modifier_relation = VocabularyTermName(self.disease_genetic_modifier_relation)

        super().__post_init__(**kwargs)


@dataclass
class DiseaseAnnotationDTO(AuditedObjectDTO):
    """
    Ingest class for association between a biological entity and a disease
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.DiseaseAnnotationDTO
    class_class_curie: ClassVar[str] = "alliance:DiseaseAnnotationDTO"
    class_name: ClassVar[str] = "DiseaseAnnotationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.DiseaseAnnotationDTO

    internal: Union[bool, Bool] = None
    disease_relation_name: str = None
    do_term_curie: str = None
    data_provider_dto: Union[dict, DataProviderDTO] = None
    mod_entity_id: Optional[str] = None
    negated: Optional[Union[bool, Bool]] = None
    evidence_curies: Optional[Union[str, List[str]]] = empty_list()
    evidence_code_curies: Optional[Union[str, List[str]]] = empty_list()
    reference_curie: Optional[str] = None
    annotation_type_name: Optional[str] = None
    with_gene_curies: Optional[Union[str, List[str]]] = empty_list()
    disease_qualifier_names: Optional[Union[str, List[str]]] = empty_list()
    condition_relation_dtos: Optional[Union[Union[dict, "ConditionRelationDTO"], List[Union[dict, "ConditionRelationDTO"]]]] = empty_list()
    genetic_sex_name: Optional[str] = None
    note_dtos: Optional[Union[Union[dict, NoteDTO], List[Union[dict, NoteDTO]]]] = empty_list()
    secondary_data_provider_dto: Optional[Union[dict, DataProviderDTO]] = None
    disease_genetic_modifier_curie: Optional[str] = None
    disease_genetic_modifier_relation_name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.disease_relation_name):
            self.MissingRequiredField("disease_relation_name")
        if not isinstance(self.disease_relation_name, str):
            self.disease_relation_name = str(self.disease_relation_name)

        if self._is_empty(self.do_term_curie):
            self.MissingRequiredField("do_term_curie")
        if not isinstance(self.do_term_curie, str):
            self.do_term_curie = str(self.do_term_curie)

        if self._is_empty(self.data_provider_dto):
            self.MissingRequiredField("data_provider_dto")
        if not isinstance(self.data_provider_dto, DataProviderDTO):
            self.data_provider_dto = DataProviderDTO(**as_dict(self.data_provider_dto))

        if self.mod_entity_id is not None and not isinstance(self.mod_entity_id, str):
            self.mod_entity_id = str(self.mod_entity_id)

        if self.negated is not None and not isinstance(self.negated, Bool):
            self.negated = Bool(self.negated)

        if not isinstance(self.evidence_curies, list):
            self.evidence_curies = [self.evidence_curies] if self.evidence_curies is not None else []
        self.evidence_curies = [v if isinstance(v, str) else str(v) for v in self.evidence_curies]

        if not isinstance(self.evidence_code_curies, list):
            self.evidence_code_curies = [self.evidence_code_curies] if self.evidence_code_curies is not None else []
        self.evidence_code_curies = [v if isinstance(v, str) else str(v) for v in self.evidence_code_curies]

        if self.reference_curie is not None and not isinstance(self.reference_curie, str):
            self.reference_curie = str(self.reference_curie)

        if self.annotation_type_name is not None and not isinstance(self.annotation_type_name, str):
            self.annotation_type_name = str(self.annotation_type_name)

        if not isinstance(self.with_gene_curies, list):
            self.with_gene_curies = [self.with_gene_curies] if self.with_gene_curies is not None else []
        self.with_gene_curies = [v if isinstance(v, str) else str(v) for v in self.with_gene_curies]

        if not isinstance(self.disease_qualifier_names, list):
            self.disease_qualifier_names = [self.disease_qualifier_names] if self.disease_qualifier_names is not None else []
        self.disease_qualifier_names = [v if isinstance(v, str) else str(v) for v in self.disease_qualifier_names]

        if not isinstance(self.condition_relation_dtos, list):
            self.condition_relation_dtos = [self.condition_relation_dtos] if self.condition_relation_dtos is not None else []
        self.condition_relation_dtos = [v if isinstance(v, ConditionRelationDTO) else ConditionRelationDTO(**as_dict(v)) for v in self.condition_relation_dtos]

        if self.genetic_sex_name is not None and not isinstance(self.genetic_sex_name, str):
            self.genetic_sex_name = str(self.genetic_sex_name)

        if not isinstance(self.note_dtos, list):
            self.note_dtos = [self.note_dtos] if self.note_dtos is not None else []
        self.note_dtos = [v if isinstance(v, NoteDTO) else NoteDTO(**as_dict(v)) for v in self.note_dtos]

        if self.secondary_data_provider_dto is not None and not isinstance(self.secondary_data_provider_dto, DataProviderDTO):
            self.secondary_data_provider_dto = DataProviderDTO(**as_dict(self.secondary_data_provider_dto))

        if self.disease_genetic_modifier_curie is not None and not isinstance(self.disease_genetic_modifier_curie, str):
            self.disease_genetic_modifier_curie = str(self.disease_genetic_modifier_curie)

        if self.disease_genetic_modifier_relation_name is not None and not isinstance(self.disease_genetic_modifier_relation_name, str):
            self.disease_genetic_modifier_relation_name = str(self.disease_genetic_modifier_relation_name)

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

    curie: Union[str, GeneDiseaseAnnotationCurie] = None
    internal: Union[bool, Bool] = None
    evidence_codes: Union[Union[str, ECOTermCurie], List[Union[str, ECOTermCurie]]] = None
    single_reference: Union[str, ReferenceCurie] = None
    data_provider: Union[dict, DataProvider] = None
    object: Union[str, DOTermCurie] = None
    subject: Union[str, GeneCurie] = None
    predicate: Union[str, VocabularyTermName] = None
    sgd_strain_background: Optional[Union[str, AffectedGenomicModelCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, GeneDiseaseAnnotationCurie):
            self.curie = GeneDiseaseAnnotationCurie(self.curie)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GeneCurie):
            self.subject = GeneCurie(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, VocabularyTermName):
            self.predicate = VocabularyTermName(self.predicate)

        if self.sgd_strain_background is not None and not isinstance(self.sgd_strain_background, AffectedGenomicModelCurie):
            self.sgd_strain_background = AffectedGenomicModelCurie(self.sgd_strain_background)

        super().__post_init__(**kwargs)


@dataclass
class GeneDiseaseAnnotationDTO(DiseaseAnnotationDTO):
    """
    Ingest class for an association between a gene and a disease
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GeneDiseaseAnnotationDTO
    class_class_curie: ClassVar[str] = "alliance:GeneDiseaseAnnotationDTO"
    class_name: ClassVar[str] = "GeneDiseaseAnnotationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GeneDiseaseAnnotationDTO

    internal: Union[bool, Bool] = None
    disease_relation_name: str = None
    do_term_curie: str = None
    data_provider_dto: Union[dict, DataProviderDTO] = None
    gene_curie: str = None
    sgd_strain_background_curie: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.gene_curie):
            self.MissingRequiredField("gene_curie")
        if not isinstance(self.gene_curie, str):
            self.gene_curie = str(self.gene_curie)

        if self.sgd_strain_background_curie is not None and not isinstance(self.sgd_strain_background_curie, str):
            self.sgd_strain_background_curie = str(self.sgd_strain_background_curie)

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

    curie: Union[str, AlleleDiseaseAnnotationCurie] = None
    internal: Union[bool, Bool] = None
    evidence_codes: Union[Union[str, ECOTermCurie], List[Union[str, ECOTermCurie]]] = None
    single_reference: Union[str, ReferenceCurie] = None
    data_provider: Union[dict, DataProvider] = None
    object: Union[str, DOTermCurie] = None
    subject: Union[str, AlleleCurie] = None
    predicate: Union[str, VocabularyTermName] = None
    inferred_gene: Optional[Union[str, GeneCurie]] = None
    asserted_genes: Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, AlleleDiseaseAnnotationCurie):
            self.curie = AlleleDiseaseAnnotationCurie(self.curie)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, AlleleCurie):
            self.subject = AlleleCurie(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, VocabularyTermName):
            self.predicate = VocabularyTermName(self.predicate)

        if self.inferred_gene is not None and not isinstance(self.inferred_gene, GeneCurie):
            self.inferred_gene = GeneCurie(self.inferred_gene)

        if not isinstance(self.asserted_genes, list):
            self.asserted_genes = [self.asserted_genes] if self.asserted_genes is not None else []
        self.asserted_genes = [v if isinstance(v, GeneCurie) else GeneCurie(v) for v in self.asserted_genes]

        super().__post_init__(**kwargs)


@dataclass
class AlleleDiseaseAnnotationDTO(DiseaseAnnotationDTO):
    """
    Ingest class for an association between an allele and a disease
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleDiseaseAnnotationDTO
    class_class_curie: ClassVar[str] = "alliance:AlleleDiseaseAnnotationDTO"
    class_name: ClassVar[str] = "AlleleDiseaseAnnotationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleDiseaseAnnotationDTO

    internal: Union[bool, Bool] = None
    disease_relation_name: str = None
    do_term_curie: str = None
    data_provider_dto: Union[dict, DataProviderDTO] = None
    allele_curie: str = None
    inferred_gene_curie: Optional[str] = None
    asserted_gene_curies: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.allele_curie):
            self.MissingRequiredField("allele_curie")
        if not isinstance(self.allele_curie, str):
            self.allele_curie = str(self.allele_curie)

        if self.inferred_gene_curie is not None and not isinstance(self.inferred_gene_curie, str):
            self.inferred_gene_curie = str(self.inferred_gene_curie)

        if not isinstance(self.asserted_gene_curies, list):
            self.asserted_gene_curies = [self.asserted_gene_curies] if self.asserted_gene_curies is not None else []
        self.asserted_gene_curies = [v if isinstance(v, str) else str(v) for v in self.asserted_gene_curies]

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

    curie: Union[str, AGMDiseaseAnnotationCurie] = None
    internal: Union[bool, Bool] = None
    evidence_codes: Union[Union[str, ECOTermCurie], List[Union[str, ECOTermCurie]]] = None
    single_reference: Union[str, ReferenceCurie] = None
    data_provider: Union[dict, DataProvider] = None
    object: Union[str, DOTermCurie] = None
    subject: Union[str, AffectedGenomicModelCurie] = None
    predicate: Union[str, VocabularyTermName] = None
    inferred_allele: Optional[Union[str, AlleleCurie]] = None
    inferred_gene: Optional[Union[str, GeneCurie]] = None
    asserted_genes: Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]] = empty_list()
    asserted_allele: Optional[Union[str, AlleleCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, AGMDiseaseAnnotationCurie):
            self.curie = AGMDiseaseAnnotationCurie(self.curie)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, AffectedGenomicModelCurie):
            self.subject = AffectedGenomicModelCurie(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, VocabularyTermName):
            self.predicate = VocabularyTermName(self.predicate)

        if self.inferred_allele is not None and not isinstance(self.inferred_allele, AlleleCurie):
            self.inferred_allele = AlleleCurie(self.inferred_allele)

        if self.inferred_gene is not None and not isinstance(self.inferred_gene, GeneCurie):
            self.inferred_gene = GeneCurie(self.inferred_gene)

        if not isinstance(self.asserted_genes, list):
            self.asserted_genes = [self.asserted_genes] if self.asserted_genes is not None else []
        self.asserted_genes = [v if isinstance(v, GeneCurie) else GeneCurie(v) for v in self.asserted_genes]

        if self.asserted_allele is not None and not isinstance(self.asserted_allele, AlleleCurie):
            self.asserted_allele = AlleleCurie(self.asserted_allele)

        super().__post_init__(**kwargs)


@dataclass
class AGMDiseaseAnnotationDTO(DiseaseAnnotationDTO):
    """
    Ingest class for an association between an AGM and a disease
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AGMDiseaseAnnotationDTO
    class_class_curie: ClassVar[str] = "alliance:AGMDiseaseAnnotationDTO"
    class_name: ClassVar[str] = "AGMDiseaseAnnotationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AGMDiseaseAnnotationDTO

    internal: Union[bool, Bool] = None
    disease_relation_name: str = None
    do_term_curie: str = None
    data_provider_dto: Union[dict, DataProviderDTO] = None
    agm_curie: str = None
    inferred_gene_curie: Optional[str] = None
    asserted_gene_curies: Optional[Union[str, List[str]]] = empty_list()
    inferred_allele_curie: Optional[str] = None
    asserted_allele_curie: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.agm_curie):
            self.MissingRequiredField("agm_curie")
        if not isinstance(self.agm_curie, str):
            self.agm_curie = str(self.agm_curie)

        if self.inferred_gene_curie is not None and not isinstance(self.inferred_gene_curie, str):
            self.inferred_gene_curie = str(self.inferred_gene_curie)

        if not isinstance(self.asserted_gene_curies, list):
            self.asserted_gene_curies = [self.asserted_gene_curies] if self.asserted_gene_curies is not None else []
        self.asserted_gene_curies = [v if isinstance(v, str) else str(v) for v in self.asserted_gene_curies]

        if self.inferred_allele_curie is not None and not isinstance(self.inferred_allele_curie, str):
            self.inferred_allele_curie = str(self.inferred_allele_curie)

        if self.asserted_allele_curie is not None and not isinstance(self.asserted_allele_curie, str):
            self.asserted_allele_curie = str(self.asserted_allele_curie)

        super().__post_init__(**kwargs)


@dataclass
class ExperimentalCondition(AuditedObject):
    """
    The environmental context in which an experiment is carried out. This may (e.g. drug treatment) or may not (e.g.
    standard conditions) directly influence the outcome of the experiment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ExperimentalCondition
    class_class_curie: ClassVar[str] = "alliance:ExperimentalCondition"
    class_name: ClassVar[str] = "ExperimentalCondition"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ExperimentalCondition

    internal: Union[bool, Bool] = None
    condition_class: Union[str, ZECOTermCurie] = None
    unique_id: Optional[str] = None
    condition_summary: Optional[str] = None
    condition_id: Optional[Union[str, ExperimentalConditionOntologyTermCurie]] = None
    condition_free_text: Optional[str] = None
    condition_quantity: Optional[str] = None
    condition_anatomy: Optional[Union[str, AnatomicalTermCurie]] = None
    condition_gene_ontology: Optional[Union[str, GOTermCurie]] = None
    condition_taxon: Optional[Union[str, NCBITaxonTermCurie]] = None
    condition_chemical: Optional[Union[str, ChemicalTermCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.condition_class):
            self.MissingRequiredField("condition_class")
        if not isinstance(self.condition_class, ZECOTermCurie):
            self.condition_class = ZECOTermCurie(self.condition_class)

        if self.unique_id is not None and not isinstance(self.unique_id, str):
            self.unique_id = str(self.unique_id)

        if self.condition_summary is not None and not isinstance(self.condition_summary, str):
            self.condition_summary = str(self.condition_summary)

        if self.condition_id is not None and not isinstance(self.condition_id, ExperimentalConditionOntologyTermCurie):
            self.condition_id = ExperimentalConditionOntologyTermCurie(self.condition_id)

        if self.condition_free_text is not None and not isinstance(self.condition_free_text, str):
            self.condition_free_text = str(self.condition_free_text)

        if self.condition_quantity is not None and not isinstance(self.condition_quantity, str):
            self.condition_quantity = str(self.condition_quantity)

        if self.condition_anatomy is not None and not isinstance(self.condition_anatomy, AnatomicalTermCurie):
            self.condition_anatomy = AnatomicalTermCurie(self.condition_anatomy)

        if self.condition_gene_ontology is not None and not isinstance(self.condition_gene_ontology, GOTermCurie):
            self.condition_gene_ontology = GOTermCurie(self.condition_gene_ontology)

        if self.condition_taxon is not None and not isinstance(self.condition_taxon, NCBITaxonTermCurie):
            self.condition_taxon = NCBITaxonTermCurie(self.condition_taxon)

        if self.condition_chemical is not None and not isinstance(self.condition_chemical, ChemicalTermCurie):
            self.condition_chemical = ChemicalTermCurie(self.condition_chemical)

        super().__post_init__(**kwargs)


@dataclass
class ExperimentalConditionDTO(AuditedObjectDTO):
    """
    Ingest class for describing the environmental context in which an experiment is carried out
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ExperimentalConditionDTO
    class_class_curie: ClassVar[str] = "alliance:ExperimentalConditionDTO"
    class_name: ClassVar[str] = "ExperimentalConditionDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ExperimentalConditionDTO

    internal: Union[bool, Bool] = None
    condition_class_curie: str = None
    condition_id_curie: Optional[str] = None
    condition_free_text: Optional[str] = None
    condition_quantity: Optional[str] = None
    condition_anatomy_curie: Optional[str] = None
    condition_gene_ontology_curie: Optional[str] = None
    condition_taxon_curie: Optional[str] = None
    condition_chemical_curie: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.condition_class_curie):
            self.MissingRequiredField("condition_class_curie")
        if not isinstance(self.condition_class_curie, str):
            self.condition_class_curie = str(self.condition_class_curie)

        if self.condition_id_curie is not None and not isinstance(self.condition_id_curie, str):
            self.condition_id_curie = str(self.condition_id_curie)

        if self.condition_free_text is not None and not isinstance(self.condition_free_text, str):
            self.condition_free_text = str(self.condition_free_text)

        if self.condition_quantity is not None and not isinstance(self.condition_quantity, str):
            self.condition_quantity = str(self.condition_quantity)

        if self.condition_anatomy_curie is not None and not isinstance(self.condition_anatomy_curie, str):
            self.condition_anatomy_curie = str(self.condition_anatomy_curie)

        if self.condition_gene_ontology_curie is not None and not isinstance(self.condition_gene_ontology_curie, str):
            self.condition_gene_ontology_curie = str(self.condition_gene_ontology_curie)

        if self.condition_taxon_curie is not None and not isinstance(self.condition_taxon_curie, str):
            self.condition_taxon_curie = str(self.condition_taxon_curie)

        if self.condition_chemical_curie is not None and not isinstance(self.condition_chemical_curie, str):
            self.condition_chemical_curie = str(self.condition_chemical_curie)

        super().__post_init__(**kwargs)


@dataclass
class ConditionRelation(AuditedObject):
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

    internal: Union[bool, Bool] = None
    condition_relation_type: Union[str, VocabularyTermName] = None
    unique_id: Optional[str] = None
    handle: Optional[str] = None
    single_reference: Optional[Union[str, ReferenceCurie]] = None
    conditions: Optional[Union[Union[dict, ExperimentalCondition], List[Union[dict, ExperimentalCondition]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.condition_relation_type):
            self.MissingRequiredField("condition_relation_type")
        if not isinstance(self.condition_relation_type, VocabularyTermName):
            self.condition_relation_type = VocabularyTermName(self.condition_relation_type)

        if self.unique_id is not None and not isinstance(self.unique_id, str):
            self.unique_id = str(self.unique_id)

        if self.handle is not None and not isinstance(self.handle, str):
            self.handle = str(self.handle)

        if self.single_reference is not None and not isinstance(self.single_reference, ReferenceCurie):
            self.single_reference = ReferenceCurie(self.single_reference)

        self._normalize_inlined_as_dict(slot_name="conditions", slot_type=ExperimentalCondition, key_name="internal", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class ConditionRelationDTO(AuditedObjectDTO):
    """
    Ingest class for the pairing of an experimental condition relation with a list of one or more conditions
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ConditionRelationDTO
    class_class_curie: ClassVar[str] = "alliance:ConditionRelationDTO"
    class_name: ClassVar[str] = "ConditionRelationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ConditionRelationDTO

    internal: Union[bool, Bool] = None
    condition_relation_type_name: str = None
    condition_dtos: Union[Union[dict, ExperimentalConditionDTO], List[Union[dict, ExperimentalConditionDTO]]] = None
    handle: Optional[str] = None
    reference_curie: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.condition_relation_type_name):
            self.MissingRequiredField("condition_relation_type_name")
        if not isinstance(self.condition_relation_type_name, str):
            self.condition_relation_type_name = str(self.condition_relation_type_name)

        if self._is_empty(self.condition_dtos):
            self.MissingRequiredField("condition_dtos")
        if not isinstance(self.condition_dtos, list):
            self.condition_dtos = [self.condition_dtos] if self.condition_dtos is not None else []
        self.condition_dtos = [v if isinstance(v, ExperimentalConditionDTO) else ExperimentalConditionDTO(**as_dict(v)) for v in self.condition_dtos]

        if self.handle is not None and not isinstance(self.handle, str):
            self.handle = str(self.handle)

        if self.reference_curie is not None and not isinstance(self.reference_curie, str):
            self.reference_curie = str(self.reference_curie)

        super().__post_init__(**kwargs)


@dataclass
class Resource(AuditedObject):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Resource
    class_class_curie: ClassVar[str] = "alliance:Resource"
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Resource

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
    synonyms: Optional[Union[str, List[str]]] = empty_list()
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

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        self._normalize_inlined_as_dict(slot_name="authors", slot_type=AuthorReference, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="editors", slot_type=AuthorReference, key_name="internal", keyed=False)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ResourceDescriptor(AuditedObject):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ResourceDescriptor
    class_class_curie: ClassVar[str] = "alliance:ResourceDescriptor"
    class_name: ClassVar[str] = "ResourceDescriptor"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ResourceDescriptor

    internal: Union[bool, Bool] = None
    prefix: str = None
    name: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()
    id_pattern: Optional[str] = None
    id_example: Optional[str] = None
    default_url_template: Optional[str] = None
    resource_pages: Optional[Union[Union[dict, "ResourceDescriptorPage"], List[Union[dict, "ResourceDescriptorPage"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.prefix):
            self.MissingRequiredField("prefix")
        if not isinstance(self.prefix, str):
            self.prefix = str(self.prefix)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if self.id_pattern is not None and not isinstance(self.id_pattern, str):
            self.id_pattern = str(self.id_pattern)

        if self.id_example is not None and not isinstance(self.id_example, str):
            self.id_example = str(self.id_example)

        if self.default_url_template is not None and not isinstance(self.default_url_template, str):
            self.default_url_template = str(self.default_url_template)

        self._normalize_inlined_as_dict(slot_name="resource_pages", slot_type=ResourceDescriptorPage, key_name="internal", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class ResourceDescriptorPage(AuditedObject):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ResourceDescriptorPage
    class_class_curie: ClassVar[str] = "alliance:ResourceDescriptorPage"
    class_name: ClassVar[str] = "ResourceDescriptorPage"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ResourceDescriptorPage

    internal: Union[bool, Bool] = None
    name: str = None
    url_template: Optional[str] = None
    page_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.url_template is not None and not isinstance(self.url_template, str):
            self.url_template = str(self.url_template)

        if self.page_description is not None and not isinstance(self.page_description, str):
            self.page_description = str(self.page_description)

        super().__post_init__(**kwargs)


@dataclass
class AlleleDTO(GenomicEntityDTO):
    """
    Ingest class for an Allele object
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleDTO
    class_class_curie: ClassVar[str] = "alliance:AlleleDTO"
    class_name: ClassVar[str] = "AlleleDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleDTO

    curie: Union[str, AlleleDTOCurie] = None
    internal: Union[bool, Bool] = None
    taxon_curie: str = None
    allele_symbol_dto: Union[dict, SymbolSlotAnnotationDTO] = None
    allele_full_name_dto: Optional[Union[dict, FullNameSlotAnnotationDTO]] = None
    reference_curies: Optional[Union[str, List[str]]] = empty_list()
    in_collection_name: Optional[str] = None
    laboratory_of_origin_curie: Optional[str] = None
    is_extinct: Optional[Union[bool, Bool]] = None
    is_extrachromosomal: Optional[Union[bool, Bool]] = None
    is_integrated: Optional[Union[bool, Bool]] = None
    transgene_chromosome_location_curie: Optional[str] = None
    allele_mutation_type_dtos: Optional[Union[Union[dict, "AlleleMutationTypeSlotAnnotationDTO"], List[Union[dict, "AlleleMutationTypeSlotAnnotationDTO"]]]] = empty_list()
    allele_inheritance_mode_dtos: Optional[Union[Union[dict, "AlleleInheritanceModeSlotAnnotationDTO"], List[Union[dict, "AlleleInheritanceModeSlotAnnotationDTO"]]]] = empty_list()
    allele_germline_transmission_status_dto: Optional[Union[dict, "AlleleGermlineTransmissionStatusSlotAnnotationDTO"]] = None
    allele_functional_impact_dtos: Optional[Union[Union[dict, "AlleleFunctionalImpactSlotAnnotationDTO"], List[Union[dict, "AlleleFunctionalImpactSlotAnnotationDTO"]]]] = empty_list()
    allele_molecular_mutation_dtos: Optional[Union[Union[dict, "AlleleMolecularMutationSlotAnnotationDTO"], List[Union[dict, "AlleleMolecularMutationSlotAnnotationDTO"]]]] = empty_list()
    allele_database_status_dto: Optional[Union[dict, "AlleleDatabaseStatusSlotAnnotationDTO"]] = None
    allele_secondary_id_dtos: Optional[Union[Union[dict, "AlleleSecondaryIdSlotAnnotationDTO"], List[Union[dict, "AlleleSecondaryIdSlotAnnotationDTO"]]]] = empty_list()
    allele_nomenclature_event_dtos: Optional[Union[Union[dict, "AlleleNomenclatureEventSlotAnnotationDTO"], List[Union[dict, "AlleleNomenclatureEventSlotAnnotationDTO"]]]] = empty_list()
    allele_note_dtos: Optional[Union[Union[dict, "AlleleNoteSlotAnnotationDTO"], List[Union[dict, "AlleleNoteSlotAnnotationDTO"]]]] = empty_list()
    allele_synonym_dtos: Optional[Union[Union[dict, NameSlotAnnotationDTO], List[Union[dict, NameSlotAnnotationDTO]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, AlleleDTOCurie):
            self.curie = AlleleDTOCurie(self.curie)

        if self._is_empty(self.allele_symbol_dto):
            self.MissingRequiredField("allele_symbol_dto")
        if not isinstance(self.allele_symbol_dto, SymbolSlotAnnotationDTO):
            self.allele_symbol_dto = SymbolSlotAnnotationDTO(**as_dict(self.allele_symbol_dto))

        if self.allele_full_name_dto is not None and not isinstance(self.allele_full_name_dto, FullNameSlotAnnotationDTO):
            self.allele_full_name_dto = FullNameSlotAnnotationDTO(**as_dict(self.allele_full_name_dto))

        if not isinstance(self.reference_curies, list):
            self.reference_curies = [self.reference_curies] if self.reference_curies is not None else []
        self.reference_curies = [v if isinstance(v, str) else str(v) for v in self.reference_curies]

        if self.in_collection_name is not None and not isinstance(self.in_collection_name, str):
            self.in_collection_name = str(self.in_collection_name)

        if self.laboratory_of_origin_curie is not None and not isinstance(self.laboratory_of_origin_curie, str):
            self.laboratory_of_origin_curie = str(self.laboratory_of_origin_curie)

        if self.is_extinct is not None and not isinstance(self.is_extinct, Bool):
            self.is_extinct = Bool(self.is_extinct)

        if self.is_extrachromosomal is not None and not isinstance(self.is_extrachromosomal, Bool):
            self.is_extrachromosomal = Bool(self.is_extrachromosomal)

        if self.is_integrated is not None and not isinstance(self.is_integrated, Bool):
            self.is_integrated = Bool(self.is_integrated)

        if self.transgene_chromosome_location_curie is not None and not isinstance(self.transgene_chromosome_location_curie, str):
            self.transgene_chromosome_location_curie = str(self.transgene_chromosome_location_curie)

        if not isinstance(self.allele_mutation_type_dtos, list):
            self.allele_mutation_type_dtos = [self.allele_mutation_type_dtos] if self.allele_mutation_type_dtos is not None else []
        self.allele_mutation_type_dtos = [v if isinstance(v, AlleleMutationTypeSlotAnnotationDTO) else AlleleMutationTypeSlotAnnotationDTO(**as_dict(v)) for v in self.allele_mutation_type_dtos]

        if not isinstance(self.allele_inheritance_mode_dtos, list):
            self.allele_inheritance_mode_dtos = [self.allele_inheritance_mode_dtos] if self.allele_inheritance_mode_dtos is not None else []
        self.allele_inheritance_mode_dtos = [v if isinstance(v, AlleleInheritanceModeSlotAnnotationDTO) else AlleleInheritanceModeSlotAnnotationDTO(**as_dict(v)) for v in self.allele_inheritance_mode_dtos]

        if self.allele_germline_transmission_status_dto is not None and not isinstance(self.allele_germline_transmission_status_dto, AlleleGermlineTransmissionStatusSlotAnnotationDTO):
            self.allele_germline_transmission_status_dto = AlleleGermlineTransmissionStatusSlotAnnotationDTO(**as_dict(self.allele_germline_transmission_status_dto))

        if not isinstance(self.allele_functional_impact_dtos, list):
            self.allele_functional_impact_dtos = [self.allele_functional_impact_dtos] if self.allele_functional_impact_dtos is not None else []
        self.allele_functional_impact_dtos = [v if isinstance(v, AlleleFunctionalImpactSlotAnnotationDTO) else AlleleFunctionalImpactSlotAnnotationDTO(**as_dict(v)) for v in self.allele_functional_impact_dtos]

        if not isinstance(self.allele_molecular_mutation_dtos, list):
            self.allele_molecular_mutation_dtos = [self.allele_molecular_mutation_dtos] if self.allele_molecular_mutation_dtos is not None else []
        self.allele_molecular_mutation_dtos = [v if isinstance(v, AlleleMolecularMutationSlotAnnotationDTO) else AlleleMolecularMutationSlotAnnotationDTO(**as_dict(v)) for v in self.allele_molecular_mutation_dtos]

        if self.allele_database_status_dto is not None and not isinstance(self.allele_database_status_dto, AlleleDatabaseStatusSlotAnnotationDTO):
            self.allele_database_status_dto = AlleleDatabaseStatusSlotAnnotationDTO(**as_dict(self.allele_database_status_dto))

        if not isinstance(self.allele_secondary_id_dtos, list):
            self.allele_secondary_id_dtos = [self.allele_secondary_id_dtos] if self.allele_secondary_id_dtos is not None else []
        self.allele_secondary_id_dtos = [v if isinstance(v, AlleleSecondaryIdSlotAnnotationDTO) else AlleleSecondaryIdSlotAnnotationDTO(**as_dict(v)) for v in self.allele_secondary_id_dtos]

        if not isinstance(self.allele_nomenclature_event_dtos, list):
            self.allele_nomenclature_event_dtos = [self.allele_nomenclature_event_dtos] if self.allele_nomenclature_event_dtos is not None else []
        self.allele_nomenclature_event_dtos = [v if isinstance(v, AlleleNomenclatureEventSlotAnnotationDTO) else AlleleNomenclatureEventSlotAnnotationDTO(**as_dict(v)) for v in self.allele_nomenclature_event_dtos]

        if not isinstance(self.allele_note_dtos, list):
            self.allele_note_dtos = [self.allele_note_dtos] if self.allele_note_dtos is not None else []
        self.allele_note_dtos = [v if isinstance(v, AlleleNoteSlotAnnotationDTO) else AlleleNoteSlotAnnotationDTO(**as_dict(v)) for v in self.allele_note_dtos]

        if not isinstance(self.allele_synonym_dtos, list):
            self.allele_synonym_dtos = [self.allele_synonym_dtos] if self.allele_synonym_dtos is not None else []
        self.allele_synonym_dtos = [v if isinstance(v, NameSlotAnnotationDTO) else NameSlotAnnotationDTO(**as_dict(v)) for v in self.allele_synonym_dtos]

        super().__post_init__(**kwargs)


@dataclass
class CellLineDTO(GenomicEntityDTO):
    """
    Dummy cell line DTO class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.CellLineDTO
    class_class_curie: ClassVar[str] = "alliance:CellLineDTO"
    class_name: ClassVar[str] = "CellLineDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.CellLineDTO

    curie: Union[str, CellLineDTOCurie] = None
    internal: Union[bool, Bool] = None
    taxon_curie: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, CellLineDTOCurie):
            self.curie = CellLineDTOCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class ConstructDTO(GenomicEntityDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ConstructDTO
    class_class_curie: ClassVar[str] = "alliance:ConstructDTO"
    class_name: ClassVar[str] = "ConstructDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ConstructDTO

    curie: Union[str, ConstructDTOCurie] = None
    internal: Union[bool, Bool] = None
    taxon_curie: str = None
    construct_component_dtos: Optional[Union[Union[str, GenomicEntityDTOCurie], List[Union[str, GenomicEntityDTOCurie]]]] = empty_list()
    reference_curies: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ConstructDTOCurie):
            self.curie = ConstructDTOCurie(self.curie)

        if not isinstance(self.construct_component_dtos, list):
            self.construct_component_dtos = [self.construct_component_dtos] if self.construct_component_dtos is not None else []
        self.construct_component_dtos = [v if isinstance(v, GenomicEntityDTOCurie) else GenomicEntityDTOCurie(v) for v in self.construct_component_dtos]

        if not isinstance(self.reference_curies, list):
            self.reference_curies = [self.reference_curies] if self.reference_curies is not None else []
        self.reference_curies = [v if isinstance(v, str) else str(v) for v in self.reference_curies]

        super().__post_init__(**kwargs)


@dataclass
class GenerationMethodDTO(AuditedObjectDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GenerationMethodDTO
    class_class_curie: ClassVar[str] = "alliance:GenerationMethodDTO"
    class_name: ClassVar[str] = "GenerationMethodDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GenerationMethodDTO

    internal: Union[bool, Bool] = None
    mutagenesis_method_names: Optional[Union[str, List[str]]] = empty_list()
    mutagenesis_target: Optional[str] = None
    integration_method_name: Optional[str] = None
    chemical_mutagen_name: Optional[str] = None
    irradiation_mutagen_name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.mutagenesis_method_names, list):
            self.mutagenesis_method_names = [self.mutagenesis_method_names] if self.mutagenesis_method_names is not None else []
        self.mutagenesis_method_names = [v if isinstance(v, str) else str(v) for v in self.mutagenesis_method_names]

        if self.mutagenesis_target is not None and not isinstance(self.mutagenesis_target, str):
            self.mutagenesis_target = str(self.mutagenesis_target)

        if self.integration_method_name is not None and not isinstance(self.integration_method_name, str):
            self.integration_method_name = str(self.integration_method_name)

        if self.chemical_mutagen_name is not None and not isinstance(self.chemical_mutagen_name, str):
            self.chemical_mutagen_name = str(self.chemical_mutagen_name)

        if self.irradiation_mutagen_name is not None and not isinstance(self.irradiation_mutagen_name, str):
            self.irradiation_mutagen_name = str(self.irradiation_mutagen_name)

        super().__post_init__(**kwargs)


@dataclass
class SequenceTargetingReagentDTO(GenomicEntityDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.SequenceTargetingReagentDTO
    class_class_curie: ClassVar[str] = "alliance:SequenceTargetingReagentDTO"
    class_name: ClassVar[str] = "SequenceTargetingReagentDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.SequenceTargetingReagentDTO

    curie: Union[str, SequenceTargetingReagentDTOCurie] = None
    internal: Union[bool, Bool] = None
    taxon_curie: str = None
    reference_curies: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, SequenceTargetingReagentDTOCurie):
            self.curie = SequenceTargetingReagentDTOCurie(self.curie)

        if not isinstance(self.reference_curies, list):
            self.reference_curies = [self.reference_curies] if self.reference_curies is not None else []
        self.reference_curies = [v if isinstance(v, str) else str(v) for v in self.reference_curies]

        super().__post_init__(**kwargs)


@dataclass
class AlleleDatabaseStatusSlotAnnotationDTO(SlotAnnotationDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleDatabaseStatusSlotAnnotationDTO
    class_class_curie: ClassVar[str] = "alliance:AlleleDatabaseStatusSlotAnnotationDTO"
    class_name: ClassVar[str] = "AlleleDatabaseStatusSlotAnnotationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleDatabaseStatusSlotAnnotationDTO

    internal: Union[bool, Bool] = None
    database_status_name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.database_status_name):
            self.MissingRequiredField("database_status_name")
        if not isinstance(self.database_status_name, str):
            self.database_status_name = str(self.database_status_name)

        super().__post_init__(**kwargs)


@dataclass
class AlleleFunctionalImpactSlotAnnotationDTO(SlotAnnotationDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleFunctionalImpactSlotAnnotationDTO
    class_class_curie: ClassVar[str] = "alliance:AlleleFunctionalImpactSlotAnnotationDTO"
    class_name: ClassVar[str] = "AlleleFunctionalImpactSlotAnnotationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleFunctionalImpactSlotAnnotationDTO

    internal: Union[bool, Bool] = None
    functional_impact_names: Union[str, List[str]] = None
    phenotype_term_curie: Optional[str] = None
    phenotype_statement: Optional[str] = None
    phenotype_term: Optional[Union[str, PhenotypeTermCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.functional_impact_names):
            self.MissingRequiredField("functional_impact_names")
        if not isinstance(self.functional_impact_names, list):
            self.functional_impact_names = [self.functional_impact_names] if self.functional_impact_names is not None else []
        self.functional_impact_names = [v if isinstance(v, str) else str(v) for v in self.functional_impact_names]

        if self.phenotype_term_curie is not None and not isinstance(self.phenotype_term_curie, str):
            self.phenotype_term_curie = str(self.phenotype_term_curie)

        if self.phenotype_statement is not None and not isinstance(self.phenotype_statement, str):
            self.phenotype_statement = str(self.phenotype_statement)

        if self.phenotype_term is not None and not isinstance(self.phenotype_term, PhenotypeTermCurie):
            self.phenotype_term = PhenotypeTermCurie(self.phenotype_term)

        super().__post_init__(**kwargs)


@dataclass
class AlleleGermlineTransmissionStatusSlotAnnotationDTO(SlotAnnotationDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleGermlineTransmissionStatusSlotAnnotationDTO
    class_class_curie: ClassVar[str] = "alliance:AlleleGermlineTransmissionStatusSlotAnnotationDTO"
    class_name: ClassVar[str] = "AlleleGermlineTransmissionStatusSlotAnnotationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleGermlineTransmissionStatusSlotAnnotationDTO

    internal: Union[bool, Bool] = None
    germline_transmission_status_name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.germline_transmission_status_name):
            self.MissingRequiredField("germline_transmission_status_name")
        if not isinstance(self.germline_transmission_status_name, str):
            self.germline_transmission_status_name = str(self.germline_transmission_status_name)

        super().__post_init__(**kwargs)


@dataclass
class AlleleInheritanceModeSlotAnnotationDTO(SlotAnnotationDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleInheritanceModeSlotAnnotationDTO
    class_class_curie: ClassVar[str] = "alliance:AlleleInheritanceModeSlotAnnotationDTO"
    class_name: ClassVar[str] = "AlleleInheritanceModeSlotAnnotationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleInheritanceModeSlotAnnotationDTO

    internal: Union[bool, Bool] = None
    inheritance_mode_name: str = None
    phenotype_term_curie: Optional[str] = None
    phenotype_statement: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.inheritance_mode_name):
            self.MissingRequiredField("inheritance_mode_name")
        if not isinstance(self.inheritance_mode_name, str):
            self.inheritance_mode_name = str(self.inheritance_mode_name)

        if self.phenotype_term_curie is not None and not isinstance(self.phenotype_term_curie, str):
            self.phenotype_term_curie = str(self.phenotype_term_curie)

        if self.phenotype_statement is not None and not isinstance(self.phenotype_statement, str):
            self.phenotype_statement = str(self.phenotype_statement)

        super().__post_init__(**kwargs)


@dataclass
class AlleleMolecularMutationSlotAnnotationDTO(SlotAnnotationDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleMolecularMutationSlotAnnotationDTO
    class_class_curie: ClassVar[str] = "alliance:AlleleMolecularMutationSlotAnnotationDTO"
    class_name: ClassVar[str] = "AlleleMolecularMutationSlotAnnotationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleMolecularMutationSlotAnnotationDTO

    internal: Union[bool, Bool] = None
    molecular_mutation_names: Union[str, List[str]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.molecular_mutation_names):
            self.MissingRequiredField("molecular_mutation_names")
        if not isinstance(self.molecular_mutation_names, list):
            self.molecular_mutation_names = [self.molecular_mutation_names] if self.molecular_mutation_names is not None else []
        self.molecular_mutation_names = [v if isinstance(v, str) else str(v) for v in self.molecular_mutation_names]

        super().__post_init__(**kwargs)


@dataclass
class AlleleMutationTypeSlotAnnotationDTO(SlotAnnotationDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleMutationTypeSlotAnnotationDTO
    class_class_curie: ClassVar[str] = "alliance:AlleleMutationTypeSlotAnnotationDTO"
    class_name: ClassVar[str] = "AlleleMutationTypeSlotAnnotationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleMutationTypeSlotAnnotationDTO

    internal: Union[bool, Bool] = None
    mutation_type_curies: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.mutation_type_curies, list):
            self.mutation_type_curies = [self.mutation_type_curies] if self.mutation_type_curies is not None else []
        self.mutation_type_curies = [v if isinstance(v, str) else str(v) for v in self.mutation_type_curies]

        super().__post_init__(**kwargs)


@dataclass
class AlleleNomenclatureEventSlotAnnotationDTO(SlotAnnotationDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleNomenclatureEventSlotAnnotationDTO
    class_class_curie: ClassVar[str] = "alliance:AlleleNomenclatureEventSlotAnnotationDTO"
    class_name: ClassVar[str] = "AlleleNomenclatureEventSlotAnnotationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleNomenclatureEventSlotAnnotationDTO

    internal: Union[bool, Bool] = None
    nomenclature_event_name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.nomenclature_event_name):
            self.MissingRequiredField("nomenclature_event_name")
        if not isinstance(self.nomenclature_event_name, str):
            self.nomenclature_event_name = str(self.nomenclature_event_name)

        super().__post_init__(**kwargs)


@dataclass
class AlleleNoteSlotAnnotationDTO(SlotAnnotationDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleNoteSlotAnnotationDTO
    class_class_curie: ClassVar[str] = "alliance:AlleleNoteSlotAnnotationDTO"
    class_name: ClassVar[str] = "AlleleNoteSlotAnnotationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleNoteSlotAnnotationDTO

    internal: Union[bool, Bool] = None
    note_dto: Union[dict, NoteDTO] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.note_dto):
            self.MissingRequiredField("note_dto")
        if not isinstance(self.note_dto, NoteDTO):
            self.note_dto = NoteDTO(**as_dict(self.note_dto))

        super().__post_init__(**kwargs)


@dataclass
class AlleleSecondaryIdSlotAnnotationDTO(SlotAnnotationDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleSecondaryIdSlotAnnotationDTO
    class_class_curie: ClassVar[str] = "alliance:AlleleSecondaryIdSlotAnnotationDTO"
    class_name: ClassVar[str] = "AlleleSecondaryIdSlotAnnotationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleSecondaryIdSlotAnnotationDTO

    internal: Union[bool, Bool] = None
    secondary_id: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.secondary_id):
            self.MissingRequiredField("secondary_id")
        if not isinstance(self.secondary_id, URIorCURIE):
            self.secondary_id = URIorCURIE(self.secondary_id)

        super().__post_init__(**kwargs)


@dataclass
class AlleleCellLineAssociationDTO(AuditedObjectDTO):
    """
    The relationship between an allele and a cell line. Includes mutant/ embryonic stem cell lines known to carry the
    allele, and parental cell line of alleles made in embryonic stem cells.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleCellLineAssociationDTO
    class_class_curie: ClassVar[str] = "alliance:AlleleCellLineAssociationDTO"
    class_name: ClassVar[str] = "AlleleCellLineAssociationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleCellLineAssociationDTO

    internal: Union[bool, Bool] = None
    allele_curie: str = None
    predicate_name: str = None
    cell_line_curie: str = None
    evidence_curies: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.allele_curie):
            self.MissingRequiredField("allele_curie")
        if not isinstance(self.allele_curie, str):
            self.allele_curie = str(self.allele_curie)

        if self._is_empty(self.predicate_name):
            self.MissingRequiredField("predicate_name")
        if not isinstance(self.predicate_name, str):
            self.predicate_name = str(self.predicate_name)

        if self._is_empty(self.cell_line_curie):
            self.MissingRequiredField("cell_line_curie")
        if not isinstance(self.cell_line_curie, str):
            self.cell_line_curie = str(self.cell_line_curie)

        if not isinstance(self.evidence_curies, list):
            self.evidence_curies = [self.evidence_curies] if self.evidence_curies is not None else []
        self.evidence_curies = [v if isinstance(v, str) else str(v) for v in self.evidence_curies]

        super().__post_init__(**kwargs)


@dataclass
class AlleleGenerationMethodAssociationDTO(AuditedObjectDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleGenerationMethodAssociationDTO
    class_class_curie: ClassVar[str] = "alliance:AlleleGenerationMethodAssociationDTO"
    class_name: ClassVar[str] = "AlleleGenerationMethodAssociationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleGenerationMethodAssociationDTO

    internal: Union[bool, Bool] = None
    allele_curie: str = None
    predicate_name: str = None
    generation_method_dto: Optional[Union[dict, GenerationMethodDTO]] = None
    evidence_curies: Optional[Union[str, List[str]]] = empty_list()
    mutation_target_strain_curie: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.allele_curie):
            self.MissingRequiredField("allele_curie")
        if not isinstance(self.allele_curie, str):
            self.allele_curie = str(self.allele_curie)

        if self._is_empty(self.predicate_name):
            self.MissingRequiredField("predicate_name")
        if not isinstance(self.predicate_name, str):
            self.predicate_name = str(self.predicate_name)

        if self.generation_method_dto is not None and not isinstance(self.generation_method_dto, GenerationMethodDTO):
            self.generation_method_dto = GenerationMethodDTO(**as_dict(self.generation_method_dto))

        if not isinstance(self.evidence_curies, list):
            self.evidence_curies = [self.evidence_curies] if self.evidence_curies is not None else []
        self.evidence_curies = [v if isinstance(v, str) else str(v) for v in self.evidence_curies]

        if self.mutation_target_strain_curie is not None and not isinstance(self.mutation_target_strain_curie, str):
            self.mutation_target_strain_curie = str(self.mutation_target_strain_curie)

        super().__post_init__(**kwargs)


@dataclass
class AlleleGenomicEntityAssociationDTO(AuditedObjectDTO):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleGenomicEntityAssociationDTO
    class_class_curie: ClassVar[str] = "alliance:AlleleGenomicEntityAssociationDTO"
    class_name: ClassVar[str] = "AlleleGenomicEntityAssociationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleGenomicEntityAssociationDTO

    internal: Union[bool, Bool] = None
    allele_curie: str = None
    predicate_name: str = None
    evidence_curies: Union[str, List[str]] = None
    evidence_code_curie: Optional[str] = None
    note_dto: Optional[Union[dict, NoteDTO]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.allele_curie):
            self.MissingRequiredField("allele_curie")
        if not isinstance(self.allele_curie, str):
            self.allele_curie = str(self.allele_curie)

        if self._is_empty(self.predicate_name):
            self.MissingRequiredField("predicate_name")
        if not isinstance(self.predicate_name, str):
            self.predicate_name = str(self.predicate_name)

        if self._is_empty(self.evidence_curies):
            self.MissingRequiredField("evidence_curies")
        if not isinstance(self.evidence_curies, list):
            self.evidence_curies = [self.evidence_curies] if self.evidence_curies is not None else []
        self.evidence_curies = [v if isinstance(v, str) else str(v) for v in self.evidence_curies]

        if self.evidence_code_curie is not None and not isinstance(self.evidence_code_curie, str):
            self.evidence_code_curie = str(self.evidence_code_curie)

        if self.note_dto is not None and not isinstance(self.note_dto, NoteDTO):
            self.note_dto = NoteDTO(**as_dict(self.note_dto))

        super().__post_init__(**kwargs)


@dataclass
class AlleleAlleleAssociationDTO(AlleleGenomicEntityAssociationDTO):
    """
    Association between an allele and another allele
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleAlleleAssociationDTO
    class_class_curie: ClassVar[str] = "alliance:AlleleAlleleAssociationDTO"
    class_name: ClassVar[str] = "AlleleAlleleAssociationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleAlleleAssociationDTO

    internal: Union[bool, Bool] = None
    allele_curie: str = None
    predicate_name: str = None
    evidence_curies: Union[str, List[str]] = None
    object_allele_curie: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.object_allele_curie is not None and not isinstance(self.object_allele_curie, str):
            self.object_allele_curie = str(self.object_allele_curie)

        super().__post_init__(**kwargs)


@dataclass
class AlleleConstructAssociationDTO(AlleleGenomicEntityAssociationDTO):
    """
    The relationship between an allele and constructs contained in that allele.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleConstructAssociationDTO
    class_class_curie: ClassVar[str] = "alliance:AlleleConstructAssociationDTO"
    class_name: ClassVar[str] = "AlleleConstructAssociationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleConstructAssociationDTO

    internal: Union[bool, Bool] = None
    allele_curie: str = None
    evidence_curies: Union[str, List[str]] = None
    construct_curie: str = None
    predicate_name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.construct_curie):
            self.MissingRequiredField("construct_curie")
        if not isinstance(self.construct_curie, str):
            self.construct_curie = str(self.construct_curie)

        if self._is_empty(self.predicate_name):
            self.MissingRequiredField("predicate_name")
        if not isinstance(self.predicate_name, str):
            self.predicate_name = str(self.predicate_name)

        super().__post_init__(**kwargs)


@dataclass
class AlleleGeneAssociationDTO(AlleleGenomicEntityAssociationDTO):
    """
    Association between an allele and a gene
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleGeneAssociationDTO
    class_class_curie: ClassVar[str] = "alliance:AlleleGeneAssociationDTO"
    class_name: ClassVar[str] = "AlleleGeneAssociationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleGeneAssociationDTO

    internal: Union[bool, Bool] = None
    allele_curie: str = None
    predicate_name: str = None
    evidence_curies: Union[str, List[str]] = None
    gene_curie: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.gene_curie):
            self.MissingRequiredField("gene_curie")
        if not isinstance(self.gene_curie, str):
            self.gene_curie = str(self.gene_curie)

        super().__post_init__(**kwargs)


@dataclass
class AlleleImageAssociationDTO(AuditedObjectDTO):
    """
    The relationship between an allele and an image.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleImageAssociationDTO
    class_class_curie: ClassVar[str] = "alliance:AlleleImageAssociationDTO"
    class_name: ClassVar[str] = "AlleleImageAssociationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleImageAssociationDTO

    internal: Union[bool, Bool] = None
    allele_curie: str = None
    predicate_name: str = None
    image_curie: str = None
    primary_image: Optional[Union[bool, Bool]] = None
    evidence_curies: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.allele_curie):
            self.MissingRequiredField("allele_curie")
        if not isinstance(self.allele_curie, str):
            self.allele_curie = str(self.allele_curie)

        if self._is_empty(self.predicate_name):
            self.MissingRequiredField("predicate_name")
        if not isinstance(self.predicate_name, str):
            self.predicate_name = str(self.predicate_name)

        if self._is_empty(self.image_curie):
            self.MissingRequiredField("image_curie")
        if not isinstance(self.image_curie, str):
            self.image_curie = str(self.image_curie)

        if self.primary_image is not None and not isinstance(self.primary_image, Bool):
            self.primary_image = Bool(self.primary_image)

        if not isinstance(self.evidence_curies, list):
            self.evidence_curies = [self.evidence_curies] if self.evidence_curies is not None else []
        self.evidence_curies = [v if isinstance(v, str) else str(v) for v in self.evidence_curies]

        super().__post_init__(**kwargs)


@dataclass
class AlleleOriginAssociationDTO(AuditedObjectDTO):
    """
    The relationship between an allele and the AGM origin of the allele.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleOriginAssociationDTO
    class_class_curie: ClassVar[str] = "alliance:AlleleOriginAssociationDTO"
    class_name: ClassVar[str] = "AlleleOriginAssociationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleOriginAssociationDTO

    internal: Union[bool, Bool] = None
    allele_curie: str = None
    predicate_name: str = None
    agm_curie: str = None
    evidence_curies: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.allele_curie):
            self.MissingRequiredField("allele_curie")
        if not isinstance(self.allele_curie, str):
            self.allele_curie = str(self.allele_curie)

        if self._is_empty(self.predicate_name):
            self.MissingRequiredField("predicate_name")
        if not isinstance(self.predicate_name, str):
            self.predicate_name = str(self.predicate_name)

        if self._is_empty(self.agm_curie):
            self.MissingRequiredField("agm_curie")
        if not isinstance(self.agm_curie, str):
            self.agm_curie = str(self.agm_curie)

        if not isinstance(self.evidence_curies, list):
            self.evidence_curies = [self.evidence_curies] if self.evidence_curies is not None else []
        self.evidence_curies = [v if isinstance(v, str) else str(v) for v in self.evidence_curies]

        super().__post_init__(**kwargs)


@dataclass
class AlleleProteinAssociationDTO(AlleleGenomicEntityAssociationDTO):
    """
    Association between an allele and a protein
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleProteinAssociationDTO
    class_class_curie: ClassVar[str] = "alliance:AlleleProteinAssociationDTO"
    class_name: ClassVar[str] = "AlleleProteinAssociationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleProteinAssociationDTO

    internal: Union[bool, Bool] = None
    allele_curie: str = None
    predicate_name: str = None
    evidence_curies: Union[str, List[str]] = None
    protein_curie: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.protein_curie):
            self.MissingRequiredField("protein_curie")
        if not isinstance(self.protein_curie, str):
            self.protein_curie = str(self.protein_curie)

        super().__post_init__(**kwargs)


@dataclass
class AlleleTranscriptAssociationDTO(AlleleGenomicEntityAssociationDTO):
    """
    Association between an allele and a transcript
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleTranscriptAssociationDTO
    class_class_curie: ClassVar[str] = "alliance:AlleleTranscriptAssociationDTO"
    class_name: ClassVar[str] = "AlleleTranscriptAssociationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleTranscriptAssociationDTO

    internal: Union[bool, Bool] = None
    allele_curie: str = None
    predicate_name: str = None
    evidence_curies: Union[str, List[str]] = None
    transcript_curie: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.transcript_curie):
            self.MissingRequiredField("transcript_curie")
        if not isinstance(self.transcript_curie, str):
            self.transcript_curie = str(self.transcript_curie)

        super().__post_init__(**kwargs)


@dataclass
class AlleleVariantAssociationDTO(AlleleGenomicEntityAssociationDTO):
    """
    The relationship between an allele and a variant is many to many. An Allele may have many variants and a variant
    can be present in many alleles.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleVariantAssociationDTO
    class_class_curie: ClassVar[str] = "alliance:AlleleVariantAssociationDTO"
    class_name: ClassVar[str] = "AlleleVariantAssociationDTO"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleVariantAssociationDTO

    internal: Union[bool, Bool] = None
    allele_curie: str = None
    predicate_name: str = None
    evidence_curies: Union[str, List[str]] = None
    variant_curie: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.variant_curie is not None and not isinstance(self.variant_curie, str):
            self.variant_curie = str(self.variant_curie)

        super().__post_init__(**kwargs)


@dataclass
class AllianceMember(Organization):
    """
    An organization that is a member of the Alliance of Genome Resources.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AllianceMember
    class_class_curie: ClassVar[str] = "alliance:AllianceMember"
    class_name: ClassVar[str] = "AllianceMember"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AllianceMember

    internal: Union[bool, Bool] = None
    full_name: str = None
    short_name: str = None
    alliance_member_id: int = None
    abbreviation: str = None
    date_created: Union[str, XSDDateTime] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.alliance_member_id):
            self.MissingRequiredField("alliance_member_id")
        if not isinstance(self.alliance_member_id, int):
            self.alliance_member_id = int(self.alliance_member_id)

        if self._is_empty(self.abbreviation):
            self.MissingRequiredField("abbreviation")
        if not isinstance(self.abbreviation, str):
            self.abbreviation = str(self.abbreviation)

        if self._is_empty(self.date_created):
            self.MissingRequiredField("date_created")
        if not isinstance(self.date_created, XSDDateTime):
            self.date_created = XSDDateTime(self.date_created)

        super().__post_init__(**kwargs)


# Enumerations
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

class NomenclatureEventEnum(EnumDefinitionImpl):

    named = PermissibleValue(text="named")
    renamed = PermissibleValue(text="renamed")

    _defn = EnumDefinition(
        name="NomenclatureEventEnum",
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

class VariantStatusEnum(EnumDefinitionImpl):

    public = PermissibleValue(text="public")
    private = PermissibleValue(text="private")

    _defn = EnumDefinition(
        name="VariantStatusEnum",
    )

# Slots
class slots:
    pass

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

slots.aberration = Slot(uri=ALLIANCE.aberration, name="aberration", curie=ALLIANCE.curie('aberration'),
                   model_uri=ALLIANCE.aberration, domain=Allele, range=Optional[str])

slots.allele_allele_associations = Slot(uri=ALLIANCE.allele_allele_associations, name="allele_allele_associations", curie=ALLIANCE.curie('allele_allele_associations'),
                   model_uri=ALLIANCE.allele_allele_associations, domain=Allele, range=Optional[Union[Union[dict, "AlleleAlleleAssociation"], List[Union[dict, "AlleleAlleleAssociation"]]]])

slots.allele_cell_line_associations = Slot(uri=ALLIANCE.allele_cell_line_associations, name="allele_cell_line_associations", curie=ALLIANCE.curie('allele_cell_line_associations'),
                   model_uri=ALLIANCE.allele_cell_line_associations, domain=Allele, range=Optional[Union[Union[dict, "AlleleCellLineAssociation"], List[Union[dict, "AlleleCellLineAssociation"]]]])

slots.allele_construct_associations = Slot(uri=ALLIANCE.allele_construct_associations, name="allele_construct_associations", curie=ALLIANCE.curie('allele_construct_associations'),
                   model_uri=ALLIANCE.allele_construct_associations, domain=Allele, range=Optional[Union[Union[dict, "AlleleConstructAssociation"], List[Union[dict, "AlleleConstructAssociation"]]]])

slots.allele_database_status = Slot(uri=ALLIANCE.allele_database_status, name="allele_database_status", curie=ALLIANCE.curie('allele_database_status'),
                   model_uri=ALLIANCE.allele_database_status, domain=Allele, range=Optional[Union[dict, "AlleleDatabaseStatusSlotAnnotation"]])

slots.allele_full_name = Slot(uri=ALLIANCE.allele_full_name, name="allele_full_name", curie=ALLIANCE.curie('allele_full_name'),
                   model_uri=ALLIANCE.allele_full_name, domain=Allele, range=Optional[Union[dict, "AlleleFullNameSlotAnnotation"]])

slots.allele_functional_impacts = Slot(uri=ALLIANCE.allele_functional_impacts, name="allele_functional_impacts", curie=ALLIANCE.curie('allele_functional_impacts'),
                   model_uri=ALLIANCE.allele_functional_impacts, domain=Allele, range=Optional[Union[Union[dict, "AlleleFunctionalImpactSlotAnnotation"], List[Union[dict, "AlleleFunctionalImpactSlotAnnotation"]]]])

slots.allele_gene_associations = Slot(uri=ALLIANCE.allele_gene_associations, name="allele_gene_associations", curie=ALLIANCE.curie('allele_gene_associations'),
                   model_uri=ALLIANCE.allele_gene_associations, domain=Allele, range=Optional[Union[Union[dict, "AlleleGeneAssociation"], List[Union[dict, "AlleleGeneAssociation"]]]])

slots.allele_generation_method_associations = Slot(uri=ALLIANCE.allele_generation_method_associations, name="allele_generation_method_associations", curie=ALLIANCE.curie('allele_generation_method_associations'),
                   model_uri=ALLIANCE.allele_generation_method_associations, domain=Allele, range=Optional[Union[Union[dict, "AlleleGenerationMethodAssociation"], List[Union[dict, "AlleleGenerationMethodAssociation"]]]])

slots.allele_germline_transmission_status = Slot(uri=ALLIANCE.allele_germline_transmission_status, name="allele_germline_transmission_status", curie=ALLIANCE.curie('allele_germline_transmission_status'),
                   model_uri=ALLIANCE.allele_germline_transmission_status, domain=Allele, range=Optional[Union[dict, "AlleleGermlineTransmissionStatusSlotAnnotation"]])

slots.allele_image_associations = Slot(uri=ALLIANCE.allele_image_associations, name="allele_image_associations", curie=ALLIANCE.curie('allele_image_associations'),
                   model_uri=ALLIANCE.allele_image_associations, domain=Allele, range=Optional[Union[Union[dict, "AlleleImageAssociation"], List[Union[dict, "AlleleImageAssociation"]]]])

slots.allele_inheritance_modes = Slot(uri=ALLIANCE.allele_inheritance_modes, name="allele_inheritance_modes", curie=ALLIANCE.curie('allele_inheritance_modes'),
                   model_uri=ALLIANCE.allele_inheritance_modes, domain=Allele, range=Optional[Union[Union[dict, "AlleleInheritanceModeSlotAnnotation"], List[Union[dict, "AlleleInheritanceModeSlotAnnotation"]]]])

slots.allele_molecular_mutations = Slot(uri=ALLIANCE.allele_molecular_mutations, name="allele_molecular_mutations", curie=ALLIANCE.curie('allele_molecular_mutations'),
                   model_uri=ALLIANCE.allele_molecular_mutations, domain=Allele, range=Optional[Union[Union[dict, "AlleleMolecularMutationSlotAnnotation"], List[Union[dict, "AlleleMolecularMutationSlotAnnotation"]]]])

slots.allele_mutation_types = Slot(uri=ALLIANCE.allele_mutation_types, name="allele_mutation_types", curie=ALLIANCE.curie('allele_mutation_types'),
                   model_uri=ALLIANCE.allele_mutation_types, domain=Allele, range=Optional[Union[Union[dict, "AlleleMutationTypeSlotAnnotation"], List[Union[dict, "AlleleMutationTypeSlotAnnotation"]]]])

slots.allele_nomenclature_events = Slot(uri=ALLIANCE.allele_nomenclature_events, name="allele_nomenclature_events", curie=ALLIANCE.curie('allele_nomenclature_events'),
                   model_uri=ALLIANCE.allele_nomenclature_events, domain=Allele, range=Optional[Union[Union[dict, "AlleleNomenclatureEventSlotAnnotation"], List[Union[dict, "AlleleNomenclatureEventSlotAnnotation"]]]])

slots.allele_notes = Slot(uri=ALLIANCE.allele_notes, name="allele_notes", curie=ALLIANCE.curie('allele_notes'),
                   model_uri=ALLIANCE.allele_notes, domain=Allele, range=Optional[Union[Union[dict, "AlleleNoteSlotAnnotation"], List[Union[dict, "AlleleNoteSlotAnnotation"]]]])

slots.allele_origin_associations = Slot(uri=ALLIANCE.allele_origin_associations, name="allele_origin_associations", curie=ALLIANCE.curie('allele_origin_associations'),
                   model_uri=ALLIANCE.allele_origin_associations, domain=Allele, range=Optional[Union[Union[dict, "AlleleOriginAssociation"], List[Union[dict, "AlleleOriginAssociation"]]]])

slots.allele_protein_associations = Slot(uri=ALLIANCE.allele_protein_associations, name="allele_protein_associations", curie=ALLIANCE.curie('allele_protein_associations'),
                   model_uri=ALLIANCE.allele_protein_associations, domain=Allele, range=Optional[Union[Union[dict, "AlleleProteinAssociation"], List[Union[dict, "AlleleProteinAssociation"]]]])

slots.allele_secondary_ids = Slot(uri=ALLIANCE.allele_secondary_ids, name="allele_secondary_ids", curie=ALLIANCE.curie('allele_secondary_ids'),
                   model_uri=ALLIANCE.allele_secondary_ids, domain=Allele, range=Optional[Union[Union[dict, "AlleleSecondaryIdSlotAnnotation"], List[Union[dict, "AlleleSecondaryIdSlotAnnotation"]]]])

slots.allele_symbol = Slot(uri=ALLIANCE.allele_symbol, name="allele_symbol", curie=ALLIANCE.curie('allele_symbol'),
                   model_uri=ALLIANCE.allele_symbol, domain=Allele, range=Union[dict, "AlleleSymbolSlotAnnotation"])

slots.allele_synonyms = Slot(uri=ALLIANCE.allele_synonyms, name="allele_synonyms", curie=ALLIANCE.curie('allele_synonyms'),
                   model_uri=ALLIANCE.allele_synonyms, domain=None, range=Optional[Union[Union[dict, AlleleSynonymSlotAnnotation], List[Union[dict, AlleleSynonymSlotAnnotation]]]])

slots.allele_transcript_associations = Slot(uri=ALLIANCE.allele_transcript_associations, name="allele_transcript_associations", curie=ALLIANCE.curie('allele_transcript_associations'),
                   model_uri=ALLIANCE.allele_transcript_associations, domain=Allele, range=Optional[Union[Union[dict, "AlleleTranscriptAssociation"], List[Union[dict, "AlleleTranscriptAssociation"]]]])

slots.allele_variant_associations = Slot(uri=ALLIANCE.allele_variant_associations, name="allele_variant_associations", curie=ALLIANCE.curie('allele_variant_associations'),
                   model_uri=ALLIANCE.allele_variant_associations, domain=Allele, range=Optional[Union[Union[dict, "AlleleVariantAssociation"], List[Union[dict, "AlleleVariantAssociation"]]]])

slots.analyses = Slot(uri=ALLIANCE.analyses, name="analyses", curie=ALLIANCE.curie('analyses'),
                   model_uri=ALLIANCE.analyses, domain=None, range=Optional[str])

slots.chemical_mutagen = Slot(uri=ALLIANCE.chemical_mutagen, name="chemical_mutagen", curie=ALLIANCE.curie('chemical_mutagen'),
                   model_uri=ALLIANCE.chemical_mutagen, domain=GenerationMethod, range=Optional[Union[str, VocabularyTermName]])

slots.construct_components = Slot(uri=ALLIANCE.construct_components, name="construct_components", curie=ALLIANCE.curie('construct_components'),
                   model_uri=ALLIANCE.construct_components, domain=Construct, range=Optional[Union[Union[str, GenomicEntityCurie], List[Union[str, GenomicEntityCurie]]]])

slots.database_status = Slot(uri=ALLIANCE.database_status, name="database_status", curie=ALLIANCE.curie('database_status'),
                   model_uri=ALLIANCE.database_status, domain=AlleleDatabaseStatusSlotAnnotation, range=Union[str, VocabularyTermName])

slots.functional_impacts = Slot(uri=ALLIANCE.functional_impacts, name="functional_impacts", curie=ALLIANCE.curie('functional_impacts'),
                   model_uri=ALLIANCE.functional_impacts, domain=AlleleFunctionalImpactSlotAnnotation, range=Union[Union[str, VocabularyTermName], List[Union[str, VocabularyTermName]]])

slots.germline_transmission_status = Slot(uri=ALLIANCE.germline_transmission_status, name="germline_transmission_status", curie=ALLIANCE.curie('germline_transmission_status'),
                   model_uri=ALLIANCE.germline_transmission_status, domain=AlleleGermlineTransmissionStatusSlotAnnotation, range=Union[str, VocabularyTermName])

slots.in_collection = Slot(uri=ALLIANCE.in_collection, name="in_collection", curie=ALLIANCE.curie('in_collection'),
                   model_uri=ALLIANCE.in_collection, domain=Allele, range=Optional[Union[str, VocabularyTermName]])

slots.inheritance_mode = Slot(uri=ALLIANCE.inheritance_mode, name="inheritance_mode", curie=ALLIANCE.curie('inheritance_mode'),
                   model_uri=ALLIANCE.inheritance_mode, domain=AlleleInheritanceModeSlotAnnotation, range=Optional[Union[str, VocabularyTermName]])

slots.integration_method = Slot(uri=ALLIANCE.integration_method, name="integration_method", curie=ALLIANCE.curie('integration_method'),
                   model_uri=ALLIANCE.integration_method, domain=GenerationMethod, range=Optional[Union[str, VocabularyTermName]])

slots.irradiation_mutagen = Slot(uri=ALLIANCE.irradiation_mutagen, name="irradiation_mutagen", curie=ALLIANCE.curie('irradiation_mutagen'),
                   model_uri=ALLIANCE.irradiation_mutagen, domain=GenerationMethod, range=Optional[Union[str, VocabularyTermName]])

slots.is_extinct = Slot(uri=ALLIANCE.is_extinct, name="is_extinct", curie=ALLIANCE.curie('is_extinct'),
                   model_uri=ALLIANCE.is_extinct, domain=Allele, range=Optional[Union[bool, Bool]])

slots.is_extrachromosomal = Slot(uri=ALLIANCE.is_extrachromosomal, name="is_extrachromosomal", curie=ALLIANCE.curie('is_extrachromosomal'),
                   model_uri=ALLIANCE.is_extrachromosomal, domain=Allele, range=Optional[Union[bool, Bool]])

slots.is_integrated = Slot(uri=ALLIANCE.is_integrated, name="is_integrated", curie=ALLIANCE.curie('is_integrated'),
                   model_uri=ALLIANCE.is_integrated, domain=Allele, range=Optional[Union[bool, Bool]])

slots.laboratory_of_origin = Slot(uri=ALLIANCE.laboratory_of_origin, name="laboratory_of_origin", curie=ALLIANCE.curie('laboratory_of_origin'),
                   model_uri=ALLIANCE.laboratory_of_origin, domain=Allele, range=Optional[Union[str, LaboratoryCurie]])

slots.molecular_mutations = Slot(uri=ALLIANCE.molecular_mutations, name="molecular_mutations", curie=ALLIANCE.curie('molecular_mutations'),
                   model_uri=ALLIANCE.molecular_mutations, domain=AlleleMolecularMutationSlotAnnotation, range=Union[str, List[str]])

slots.mutagenesis_methods = Slot(uri=ALLIANCE.mutagenesis_methods, name="mutagenesis_methods", curie=ALLIANCE.curie('mutagenesis_methods'),
                   model_uri=ALLIANCE.mutagenesis_methods, domain=None, range=Optional[Union[Union[str, VocabularyTermName], List[Union[str, VocabularyTermName]]]])

slots.mutagenesis_target = Slot(uri=ALLIANCE.mutagenesis_target, name="mutagenesis_target", curie=ALLIANCE.curie('mutagenesis_target'),
                   model_uri=ALLIANCE.mutagenesis_target, domain=None, range=Optional[str])

slots.mutation_target_strain = Slot(uri=ALLIANCE.mutation_target_strain, name="mutation_target_strain", curie=ALLIANCE.curie('mutation_target_strain'),
                   model_uri=ALLIANCE.mutation_target_strain, domain=None, range=Optional[Union[str, AffectedGenomicModelCurie]])

slots.mutation_types = Slot(uri=ALLIANCE.mutation_types, name="mutation_types", curie=ALLIANCE.curie('mutation_types'),
                   model_uri=ALLIANCE.mutation_types, domain=AlleleMutationTypeSlotAnnotation, range=Union[Union[str, SOTermCurie], List[Union[str, SOTermCurie]]])

slots.nomenclature_event = Slot(uri=ALLIANCE.nomenclature_event, name="nomenclature_event", curie=ALLIANCE.curie('nomenclature_event'),
                   model_uri=ALLIANCE.nomenclature_event, domain=AlleleNomenclatureEventSlotAnnotation, range=Union[str, VocabularyTermName])

slots.primary_image = Slot(uri=ALLIANCE.primary_image, name="primary_image", curie=ALLIANCE.curie('primary_image'),
                   model_uri=ALLIANCE.primary_image, domain=None, range=Optional[Union[bool, Bool]])

slots.single_allele = Slot(uri=ALLIANCE.single_allele, name="single_allele", curie=ALLIANCE.curie('single_allele'),
                   model_uri=ALLIANCE.single_allele, domain=None, range=Optional[Union[str, AlleleCurie]])

slots.transgene_chromosome_location = Slot(uri=ALLIANCE.transgene_chromosome_location, name="transgene_chromosome_location", curie=ALLIANCE.curie('transgene_chromosome_location'),
                   model_uri=ALLIANCE.transgene_chromosome_location, domain=Allele, range=Optional[Union[str, ChromosomeCurie]])

slots.transposon_insertion = Slot(uri=ALLIANCE.transposon_insertion, name="transposon_insertion", curie=ALLIANCE.curie('transposon_insertion'),
                   model_uri=ALLIANCE.transposon_insertion, domain=Allele, range=Optional[str])

slots.name_type = Slot(uri=ALLIANCE.name_type, name="name_type", curie=ALLIANCE.curie('name_type'),
                   model_uri=ALLIANCE.name_type, domain=NameSlotAnnotation, range=Union[str, VocabularyTermName])

slots.name_type_name = Slot(uri=ALLIANCE.name_type_name, name="name_type_name", curie=ALLIANCE.curie('name_type_name'),
                   model_uri=ALLIANCE.name_type_name, domain=NameSlotAnnotationDTO, range=str)

slots.format_text = Slot(uri=ALLIANCE.format_text, name="format_text", curie=ALLIANCE.curie('format_text'),
                   model_uri=ALLIANCE.format_text, domain=None, range=str)

slots.display_text = Slot(uri=ALLIANCE.display_text, name="display_text", curie=ALLIANCE.curie('display_text'),
                   model_uri=ALLIANCE.display_text, domain=None, range=str)

slots.synonym_url = Slot(uri=ALLIANCE.synonym_url, name="synonym_url", curie=ALLIANCE.curie('synonym_url'),
                   model_uri=ALLIANCE.synonym_url, domain=None, range=Optional[Union[str, URI]])

slots.synonym_scope = Slot(uri=ALLIANCE.synonym_scope, name="synonym_scope", curie=ALLIANCE.curie('synonym_scope'),
                   model_uri=ALLIANCE.synonym_scope, domain=NameSlotAnnotation, range=Optional[Union[str, VocabularyTermName]])

slots.synonym_scope_name = Slot(uri=ALLIANCE.synonym_scope_name, name="synonym_scope_name", curie=ALLIANCE.curie('synonym_scope_name'),
                   model_uri=ALLIANCE.synonym_scope_name, domain=NameSlotAnnotationDTO, range=Optional[str])

slots.start = Slot(uri=ALLIANCE.start, name="start", curie=ALLIANCE.curie('start'),
                   model_uri=ALLIANCE.start, domain=None, range=Optional[int])

slots.end = Slot(uri=ALLIANCE.end, name="end", curie=ALLIANCE.curie('end'),
                   model_uri=ALLIANCE.end, domain=None, range=Optional[int])

slots.has_assembly = Slot(uri=ALLIANCE.has_assembly, name="has_assembly", curie=ALLIANCE.curie('has_assembly'),
                   model_uri=ALLIANCE.has_assembly, domain=GenomicLocationAssociation, range=Union[str, AssemblyCurie])

slots.prefix = Slot(uri=ALLIANCE.prefix, name="prefix", curie=ALLIANCE.curie('prefix'),
                   model_uri=ALLIANCE.prefix, domain=None, range=str)

slots.page_area = Slot(uri=ALLIANCE.page_area, name="page_area", curie=ALLIANCE.curie('page_area'),
                   model_uri=ALLIANCE.page_area, domain=None, range=str)

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

slots.uncertain = Slot(uri=ALLIANCE.uncertain, name="uncertain", curie=ALLIANCE.curie('uncertain'),
                   model_uri=ALLIANCE.uncertain, domain=None, range=Optional[Union[bool, Bool]])

slots.free_text = Slot(uri=ALLIANCE.free_text, name="free_text", curie=ALLIANCE.curie('free_text'),
                   model_uri=ALLIANCE.free_text, domain=None, range=Optional[str])

slots.note_type = Slot(uri=ALLIANCE.note_type, name="note_type", curie=ALLIANCE.curie('note_type'),
                   model_uri=ALLIANCE.note_type, domain=None, range=Optional[Union[str, VocabularyTermName]])

slots.note_type_name = Slot(uri=ALLIANCE.note_type_name, name="note_type_name", curie=ALLIANCE.curie('note_type_name'),
                   model_uri=ALLIANCE.note_type_name, domain=NoteDTO, range=Optional[str])

slots.internal = Slot(uri=ALLIANCE.internal, name="internal", curie=ALLIANCE.curie('internal'),
                   model_uri=ALLIANCE.internal, domain=None, range=Union[bool, Bool])

slots.related_notes = Slot(uri=ALLIANCE.related_notes, name="related_notes", curie=ALLIANCE.curie('related_notes'),
                   model_uri=ALLIANCE.related_notes, domain=None, range=Optional[Union[Union[dict, Note], List[Union[dict, Note]]]])

slots.related_note = Slot(uri=ALLIANCE.related_note, name="related_note", curie=ALLIANCE.curie('related_note'),
                   model_uri=ALLIANCE.related_note, domain=None, range=Optional[Union[dict, Note]])

slots.note_dto = Slot(uri=ALLIANCE.note_dto, name="note_dto", curie=ALLIANCE.curie('note_dto'),
                   model_uri=ALLIANCE.note_dto, domain=None, range=Optional[Union[dict, NoteDTO]])

slots.note_dtos = Slot(uri=ALLIANCE.note_dtos, name="note_dtos", curie=ALLIANCE.curie('note_dtos'),
                   model_uri=ALLIANCE.note_dtos, domain=None, range=Optional[Union[Union[dict, NoteDTO], List[Union[dict, NoteDTO]]]])

slots.generated_by = Slot(uri=ALLIANCE.generated_by, name="generated_by", curie=ALLIANCE.curie('generated_by'),
                   model_uri=ALLIANCE.generated_by, domain=None, range=Optional[Union[Union[dict, Agent], List[Union[dict, Agent]]]])

slots.manufactured_by = Slot(uri=ALLIANCE.manufactured_by, name="manufactured_by", curie=ALLIANCE.curie('manufactured_by'),
                   model_uri=ALLIANCE.manufactured_by, domain=None, range=Optional[Union[Union[dict, Agent], List[Union[dict, Agent]]]])

slots.current = Slot(uri=ALLIANCE.current, name="current", curie=ALLIANCE.curie('current'),
                   model_uri=ALLIANCE.current, domain=None, range=Optional[Union[bool, Bool]])

slots.curie = Slot(uri=ALLIANCE.curie, name="curie", curie=ALLIANCE.curie('curie'),
                   model_uri=ALLIANCE.curie, domain=None, range=URIRef)

slots.referenced_curie = Slot(uri=ALLIANCE.referenced_curie, name="referenced_curie", curie=ALLIANCE.curie('referenced_curie'),
                   model_uri=ALLIANCE.referenced_curie, domain=None, range=Union[str, URIorCURIE])

slots.unique_id = Slot(uri=ALLIANCE.unique_id, name="unique_id", curie=ALLIANCE.curie('unique_id'),
                   model_uri=ALLIANCE.unique_id, domain=None, range=Optional[str])

slots.dbkey = Slot(uri=ALLIANCE.dbkey, name="dbkey", curie=ALLIANCE.curie('dbkey'),
                   model_uri=ALLIANCE.dbkey, domain=None, range=Optional[str])

slots.taxon = Slot(uri=ALLIANCE.taxon, name="taxon", curie=ALLIANCE.curie('taxon'),
                   model_uri=ALLIANCE.taxon, domain=None, range=Optional[Union[str, NCBITaxonTermCurie]])

slots.taxon_curie = Slot(uri=ALLIANCE.taxon_curie, name="taxon_curie", curie=ALLIANCE.curie('taxon_curie'),
                   model_uri=ALLIANCE.taxon_curie, domain=None, range=Optional[str])

slots.secondary_identifiers = Slot(uri=ALLIANCE.secondary_identifiers, name="secondary_identifiers", curie=ALLIANCE.curie('secondary_identifiers'),
                   model_uri=ALLIANCE.secondary_identifiers, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.secondary_id = Slot(uri=ALLIANCE.secondary_id, name="secondary_id", curie=ALLIANCE.curie('secondary_id'),
                   model_uri=ALLIANCE.secondary_id, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.genomic_location_associations = Slot(uri=ALLIANCE.genomic_location_associations, name="genomic_location_associations", curie=ALLIANCE.curie('genomic_location_associations'),
                   model_uri=ALLIANCE.genomic_location_associations, domain=GenomicEntity, range=Optional[Union[Union[dict, "GenomicLocationAssociation"], List[Union[dict, "GenomicLocationAssociation"]]]])

slots.genomic_location_association_dtos = Slot(uri=ALLIANCE.genomic_location_association_dtos, name="genomic_location_association_dtos", curie=ALLIANCE.curie('genomic_location_association_dtos'),
                   model_uri=ALLIANCE.genomic_location_association_dtos, domain=GenomicEntityDTO, range=Optional[Union[Union[dict, "GenomicLocationAssociationDTO"], List[Union[dict, "GenomicLocationAssociationDTO"]]]])

slots.table_key = Slot(uri=ALLIANCE.table_key, name="table_key", curie=ALLIANCE.curie('table_key'),
                   model_uri=ALLIANCE.table_key, domain=None, range=Optional[int])

slots.date_created = Slot(uri=ALLIANCE.date_created, name="date_created", curie=ALLIANCE.curie('date_created'),
                   model_uri=ALLIANCE.date_created, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.date_updated = Slot(uri=ALLIANCE.date_updated, name="date_updated", curie=ALLIANCE.curie('date_updated'),
                   model_uri=ALLIANCE.date_updated, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.db_date_created = Slot(uri=ALLIANCE.db_date_created, name="db_date_created", curie=ALLIANCE.curie('db_date_created'),
                   model_uri=ALLIANCE.db_date_created, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.db_date_updated = Slot(uri=ALLIANCE.db_date_updated, name="db_date_updated", curie=ALLIANCE.curie('db_date_updated'),
                   model_uri=ALLIANCE.db_date_updated, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.created_by = Slot(uri=ALLIANCE.created_by, name="created_by", curie=ALLIANCE.curie('created_by'),
                   model_uri=ALLIANCE.created_by, domain=AuditedObject, range=Optional[Union[str, PersonUniqueId]])

slots.created_by_curie = Slot(uri=ALLIANCE.created_by_curie, name="created_by_curie", curie=ALLIANCE.curie('created_by_curie'),
                   model_uri=ALLIANCE.created_by_curie, domain=AuditedObjectDTO, range=Optional[str])

slots.updated_by = Slot(uri=ALLIANCE.updated_by, name="updated_by", curie=ALLIANCE.curie('updated_by'),
                   model_uri=ALLIANCE.updated_by, domain=AuditedObject, range=Optional[Union[str, PersonUniqueId]])

slots.updated_by_curie = Slot(uri=ALLIANCE.updated_by_curie, name="updated_by_curie", curie=ALLIANCE.curie('updated_by_curie'),
                   model_uri=ALLIANCE.updated_by_curie, domain=AuditedObjectDTO, range=Optional[str])

slots.release = Slot(uri=ALLIANCE.release, name="release", curie=ALLIANCE.curie('release'),
                   model_uri=ALLIANCE.release, domain=None, range=Optional[str])

slots.data_provider = Slot(uri=ALLIANCE.data_provider, name="data_provider", curie=ALLIANCE.curie('data_provider'),
                   model_uri=ALLIANCE.data_provider, domain=None, range=Optional[Union[dict, DataProvider]])

slots.data_provider_dto = Slot(uri=ALLIANCE.data_provider_dto, name="data_provider_dto", curie=ALLIANCE.curie('data_provider_dto'),
                   model_uri=ALLIANCE.data_provider_dto, domain=None, range=Optional[Union[dict, DataProviderDTO]])

slots.secondary_data_provider = Slot(uri=ALLIANCE.secondary_data_provider, name="secondary_data_provider", curie=ALLIANCE.curie('secondary_data_provider'),
                   model_uri=ALLIANCE.secondary_data_provider, domain=None, range=Optional[Union[dict, DataProvider]])

slots.secondary_data_provider_dto = Slot(uri=ALLIANCE.secondary_data_provider_dto, name="secondary_data_provider_dto", curie=ALLIANCE.curie('secondary_data_provider_dto'),
                   model_uri=ALLIANCE.secondary_data_provider_dto, domain=None, range=Optional[Union[dict, DataProviderDTO]])

slots.association_slot = Slot(uri=ALLIANCE.association_slot, name="association_slot", curie=ALLIANCE.curie('association_slot'),
                   model_uri=ALLIANCE.association_slot, domain=None, range=Optional[str])

slots.description = Slot(uri=ALLIANCE.description, name="description", curie=ALLIANCE.curie('description'),
                   model_uri=ALLIANCE.description, domain=None, range=Optional[str])

slots.cross_reference = Slot(uri=ALLIANCE.cross_reference, name="cross_reference", curie=ALLIANCE.curie('cross_reference'),
                   model_uri=ALLIANCE.cross_reference, domain=None, range=Optional[Union[dict, CrossReference]])

slots.cross_references = Slot(uri=ALLIANCE.cross_references, name="cross_references", curie=ALLIANCE.curie('cross_references'),
                   model_uri=ALLIANCE.cross_references, domain=None, range=Optional[Union[Union[dict, CrossReference], List[Union[dict, CrossReference]]]])

slots.cross_reference_dto = Slot(uri=ALLIANCE.cross_reference_dto, name="cross_reference_dto", curie=ALLIANCE.curie('cross_reference_dto'),
                   model_uri=ALLIANCE.cross_reference_dto, domain=None, range=Optional[Union[dict, CrossReferenceDTO]])

slots.cross_reference_dtos = Slot(uri=ALLIANCE.cross_reference_dtos, name="cross_reference_dtos", curie=ALLIANCE.curie('cross_reference_dtos'),
                   model_uri=ALLIANCE.cross_reference_dtos, domain=None, range=Optional[Union[Union[dict, CrossReferenceDTO], List[Union[dict, CrossReferenceDTO]]]])

slots.synonyms = Slot(uri=ALLIANCE.synonyms, name="synonyms", curie=ALLIANCE.curie('synonyms'),
                   model_uri=ALLIANCE.synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.negated = Slot(uri=ALLIANCE.negated, name="negated", curie=ALLIANCE.curie('negated'),
                   model_uri=ALLIANCE.negated, domain=None, range=Optional[Union[bool, Bool]])

slots.qualifiers = Slot(uri=ALLIANCE.qualifiers, name="qualifiers", curie=ALLIANCE.curie('qualifiers'),
                   model_uri=ALLIANCE.qualifiers, domain=None, range=Optional[str])

slots.type = Slot(uri=ALLIANCE.type, name="type", curie=ALLIANCE.curie('type'),
                   model_uri=ALLIANCE.type, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.references = Slot(uri=ALLIANCE.references, name="references", curie=ALLIANCE.curie('references'),
                   model_uri=ALLIANCE.references, domain=None, range=Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]])

slots.single_reference = Slot(uri=ALLIANCE.single_reference, name="single_reference", curie=ALLIANCE.curie('single_reference'),
                   model_uri=ALLIANCE.single_reference, domain=None, range=Optional[Union[str, ReferenceCurie]])

slots.original_reference = Slot(uri=ALLIANCE.original_reference, name="original_reference", curie=ALLIANCE.curie('original_reference'),
                   model_uri=ALLIANCE.original_reference, domain=None, range=Optional[Union[str, ReferenceCurie]])

slots.obsolete = Slot(uri=ALLIANCE.obsolete, name="obsolete", curie=ALLIANCE.curie('obsolete'),
                   model_uri=ALLIANCE.obsolete, domain=None, range=Optional[Union[bool, Bool]])

slots.abbreviation = Slot(uri=ALLIANCE.abbreviation, name="abbreviation", curie=ALLIANCE.curie('abbreviation'),
                   model_uri=ALLIANCE.abbreviation, domain=None, range=Optional[str])

slots.mod_entity_id = Slot(uri=ALLIANCE.mod_entity_id, name="mod_entity_id", curie=ALLIANCE.curie('mod_entity_id'),
                   model_uri=ALLIANCE.mod_entity_id, domain=None, range=Optional[str])

slots.first_name = Slot(uri=ALLIANCE.first_name, name="first_name", curie=ALLIANCE.curie('first_name'),
                   model_uri=ALLIANCE.first_name, domain=None, range=Optional[str])

slots.middle_name = Slot(uri=ALLIANCE.middle_name, name="middle_name", curie=ALLIANCE.curie('middle_name'),
                   model_uri=ALLIANCE.middle_name, domain=None, range=Optional[str])

slots.last_name = Slot(uri=ALLIANCE.last_name, name="last_name", curie=ALLIANCE.curie('last_name'),
                   model_uri=ALLIANCE.last_name, domain=None, range=Optional[str])

slots.evidence_codes = Slot(uri=ALLIANCE.evidence_codes, name="evidence_codes", curie=ALLIANCE.curie('evidence_codes'),
                   model_uri=ALLIANCE.evidence_codes, domain=None, range=Optional[Union[Union[str, ECOTermCurie], List[Union[str, ECOTermCurie]]]])

slots.evidence_code = Slot(uri=ALLIANCE.evidence_code, name="evidence_code", curie=ALLIANCE.curie('evidence_code'),
                   model_uri=ALLIANCE.evidence_code, domain=None, range=Optional[Union[str, ECOTermCurie]])

slots.cron_schedule = Slot(uri=ALLIANCE.cron_schedule, name="cron_schedule", curie=ALLIANCE.curie('cron_schedule'),
                   model_uri=ALLIANCE.cron_schedule, domain=None, range=Optional[str])

slots.schedule_active = Slot(uri=ALLIANCE.schedule_active, name="schedule_active", curie=ALLIANCE.curie('schedule_active'),
                   model_uri=ALLIANCE.schedule_active, domain=None, range=Optional[Union[bool, Bool]])

slots.counter = Slot(uri=ALLIANCE.counter, name="counter", curie=ALLIANCE.curie('counter'),
                   model_uri=ALLIANCE.counter, domain=None, range=Optional[int])

slots.subdomain_code = Slot(uri=ALLIANCE.subdomain_code, name="subdomain_code", curie=ALLIANCE.curie('subdomain_code'),
                   model_uri=ALLIANCE.subdomain_code, domain=None, range=Optional[str])

slots.subdomain_name = Slot(uri=ALLIANCE.subdomain_name, name="subdomain_name", curie=ALLIANCE.curie('subdomain_name'),
                   model_uri=ALLIANCE.subdomain_name, domain=None, range=Optional[str])

slots.first = Slot(uri=ALLIANCE.first, name="first", curie=ALLIANCE.curie('first'),
                   model_uri=ALLIANCE.first, domain=None, range=Optional[Union[str, IdentifierCurie]])

slots.last = Slot(uri=ALLIANCE.last, name="last", curie=ALLIANCE.curie('last'),
                   model_uri=ALLIANCE.last, domain=None, range=Optional[Union[str, IdentifierCurie]])

slots.genomic_entity_curie = Slot(uri=ALLIANCE.genomic_entity_curie, name="genomic_entity_curie", curie=ALLIANCE.curie('genomic_entity_curie'),
                   model_uri=ALLIANCE.genomic_entity_curie, domain=None, range=Optional[str])

slots.assembly_curie = Slot(uri=ALLIANCE.assembly_curie, name="assembly_curie", curie=ALLIANCE.curie('assembly_curie'),
                   model_uri=ALLIANCE.assembly_curie, domain=None, range=Optional[str])

slots.chromosome_curie = Slot(uri=ALLIANCE.chromosome_curie, name="chromosome_curie", curie=ALLIANCE.curie('chromosome_curie'),
                   model_uri=ALLIANCE.chromosome_curie, domain=None, range=Optional[str])

slots.transcript_curie = Slot(uri=ALLIANCE.transcript_curie, name="transcript_curie", curie=ALLIANCE.curie('transcript_curie'),
                   model_uri=ALLIANCE.transcript_curie, domain=None, range=str)

slots.protein_curie = Slot(uri=ALLIANCE.protein_curie, name="protein_curie", curie=ALLIANCE.curie('protein_curie'),
                   model_uri=ALLIANCE.protein_curie, domain=None, range=str)

slots.source_organization = Slot(uri=ALLIANCE.source_organization, name="source_organization", curie=ALLIANCE.curie('source_organization'),
                   model_uri=ALLIANCE.source_organization, domain=DataProvider, range=Union[dict, "Organization"])

slots.source_organization_abbreviation = Slot(uri=ALLIANCE.source_organization_abbreviation, name="source_organization_abbreviation", curie=ALLIANCE.curie('source_organization_abbreviation'),
                   model_uri=ALLIANCE.source_organization_abbreviation, domain=DataProviderDTO, range=str)

slots.resource_descriptor_page = Slot(uri=ALLIANCE.resource_descriptor_page, name="resource_descriptor_page", curie=ALLIANCE.curie('resource_descriptor_page'),
                   model_uri=ALLIANCE.resource_descriptor_page, domain=CrossReference, range=Optional[Union[dict, "ResourceDescriptorPage"]])

slots.subject = Slot(uri=ALLIANCE.subject, name="subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.subject, domain=None, range=str)

slots.object = Slot(uri=ALLIANCE.object, name="object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.object, domain=None, range=str)

slots.predicate = Slot(uri=ALLIANCE.predicate, name="predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.predicate, domain=None, range=str)

slots.predicate_name = Slot(uri=ALLIANCE.predicate_name, name="predicate_name", curie=ALLIANCE.curie('predicate_name'),
                   model_uri=ALLIANCE.predicate_name, domain=None, range=str)

slots.related_to = Slot(uri=ALLIANCE.related_to, name="related_to", curie=ALLIANCE.curie('related_to'),
                   model_uri=ALLIANCE.related_to, domain=None, range=Optional[Union[str, List[str]]])

slots.single_gene = Slot(uri=ALLIANCE.single_gene, name="single_gene", curie=ALLIANCE.curie('single_gene'),
                   model_uri=ALLIANCE.single_gene, domain=None, range=Optional[Union[str, GeneCurie]])

slots.gene_symbol = Slot(uri=ALLIANCE.gene_symbol, name="gene_symbol", curie=ALLIANCE.curie('gene_symbol'),
                   model_uri=ALLIANCE.gene_symbol, domain=Gene, range=Union[dict, "GeneSymbolSlotAnnotation"])

slots.gene_symbol_dto = Slot(uri=ALLIANCE.gene_symbol_dto, name="gene_symbol_dto", curie=ALLIANCE.curie('gene_symbol_dto'),
                   model_uri=ALLIANCE.gene_symbol_dto, domain=GeneDTO, range=Union[dict, SymbolSlotAnnotationDTO])

slots.gene_full_name = Slot(uri=ALLIANCE.gene_full_name, name="gene_full_name", curie=ALLIANCE.curie('gene_full_name'),
                   model_uri=ALLIANCE.gene_full_name, domain=Gene, range=Optional[Union[dict, "GeneFullNameSlotAnnotation"]])

slots.gene_full_name_dto = Slot(uri=ALLIANCE.gene_full_name_dto, name="gene_full_name_dto", curie=ALLIANCE.curie('gene_full_name_dto'),
                   model_uri=ALLIANCE.gene_full_name_dto, domain=GeneDTO, range=Optional[Union[dict, FullNameSlotAnnotationDTO]])

slots.gene_systematic_name = Slot(uri=ALLIANCE.gene_systematic_name, name="gene_systematic_name", curie=ALLIANCE.curie('gene_systematic_name'),
                   model_uri=ALLIANCE.gene_systematic_name, domain=Gene, range=Optional[Union[dict, "GeneSystematicNameSlotAnnotation"]])

slots.gene_systematic_name_dto = Slot(uri=ALLIANCE.gene_systematic_name_dto, name="gene_systematic_name_dto", curie=ALLIANCE.curie('gene_systematic_name_dto'),
                   model_uri=ALLIANCE.gene_systematic_name_dto, domain=GeneDTO, range=Optional[Union[dict, SystematicNameSlotAnnotationDTO]])

slots.gene_synonyms = Slot(uri=ALLIANCE.gene_synonyms, name="gene_synonyms", curie=ALLIANCE.curie('gene_synonyms'),
                   model_uri=ALLIANCE.gene_synonyms, domain=Gene, range=Optional[Union[Union[dict, "GeneSynonymSlotAnnotation"], List[Union[dict, "GeneSynonymSlotAnnotation"]]]])

slots.gene_synonym_dtos = Slot(uri=ALLIANCE.gene_synonym_dtos, name="gene_synonym_dtos", curie=ALLIANCE.curie('gene_synonym_dtos'),
                   model_uri=ALLIANCE.gene_synonym_dtos, domain=GeneDTO, range=Optional[Union[Union[dict, NameSlotAnnotationDTO], List[Union[dict, NameSlotAnnotationDTO]]]])

slots.gene_curie = Slot(uri=ALLIANCE.gene_curie, name="gene_curie", curie=ALLIANCE.curie('gene_curie'),
                   model_uri=ALLIANCE.gene_curie, domain=None, range=str)

slots.gene_type = Slot(uri=ALLIANCE.gene_type, name="gene_type", curie=ALLIANCE.curie('gene_type'),
                   model_uri=ALLIANCE.gene_type, domain=Gene, range=Optional[Union[str, SOTermCurie]])

slots.gene_type_curie = Slot(uri=ALLIANCE.gene_type_curie, name="gene_type_curie", curie=ALLIANCE.curie('gene_type_curie'),
                   model_uri=ALLIANCE.gene_type_curie, domain=GeneDTO, range=Optional[str])

slots.gene_types_secondary = Slot(uri=ALLIANCE.gene_types_secondary, name="gene_types_secondary", curie=ALLIANCE.curie('gene_types_secondary'),
                   model_uri=ALLIANCE.gene_types_secondary, domain=Gene, range=Optional[Union[Union[str, SOTermCurie], List[Union[str, SOTermCurie]]]])

slots.designating_laboratories = Slot(uri=ALLIANCE.designating_laboratories, name="designating_laboratories", curie=ALLIANCE.curie('designating_laboratories'),
                   model_uri=ALLIANCE.designating_laboratories, domain=Gene, range=Optional[Union[Union[str, LaboratoryCurie], List[Union[str, LaboratoryCurie]]]])

slots.designating_persons = Slot(uri=ALLIANCE.designating_persons, name="designating_persons", curie=ALLIANCE.curie('designating_persons'),
                   model_uri=ALLIANCE.designating_persons, domain=Gene, range=Optional[Union[str, List[str]]])

slots.trans_splice_leaders = Slot(uri=ALLIANCE.trans_splice_leaders, name="trans_splice_leaders", curie=ALLIANCE.curie('trans_splice_leaders'),
                   model_uri=ALLIANCE.trans_splice_leaders, domain=Gene, range=Optional[Union[str, List[str]]])

slots.contig = Slot(uri=ALLIANCE.contig, name="contig", curie=ALLIANCE.curie('contig'),
                   model_uri=ALLIANCE.contig, domain=Gene, range=Optional[Union[str, List[str]]])

slots.anatomy_function = Slot(uri=ALLIANCE.anatomy_function, name="anatomy_function", curie=ALLIANCE.curie('anatomy_function'),
                   model_uri=ALLIANCE.anatomy_function, domain=Gene, range=Optional[Union[str, List[str]]])

slots.product_binds_matrix = Slot(uri=ALLIANCE.product_binds_matrix, name="product_binds_matrix", curie=ALLIANCE.curie('product_binds_matrix'),
                   model_uri=ALLIANCE.product_binds_matrix, domain=Gene, range=Optional[Union[str, List[str]]])

slots.wbprocess = Slot(uri=ALLIANCE.wbprocess, name="wbprocess", curie=ALLIANCE.curie('wbprocess'),
                   model_uri=ALLIANCE.wbprocess, domain=Gene, range=Optional[Union[str, List[str]]])

slots.transposon_origin = Slot(uri=ALLIANCE.transposon_origin, name="transposon_origin", curie=ALLIANCE.curie('transposon_origin'),
                   model_uri=ALLIANCE.transposon_origin, domain=Gene, range=Optional[Union[bool, Bool]])

slots.genetic_map_chromosome = Slot(uri=ALLIANCE.genetic_map_chromosome, name="genetic_map_chromosome", curie=ALLIANCE.curie('genetic_map_chromosome'),
                   model_uri=ALLIANCE.genetic_map_chromosome, domain=GeneticMapPosition, range=Optional[Union[str, ChromosomeCurie]])

slots.genetic_map_band = Slot(uri=ALLIANCE.genetic_map_band, name="genetic_map_band", curie=ALLIANCE.curie('genetic_map_band'),
                   model_uri=ALLIANCE.genetic_map_band, domain=GeneticMapPosition, range=Optional[str])

slots.genetic_map_position_centimorgan = Slot(uri=ALLIANCE.genetic_map_position_centimorgan, name="genetic_map_position_centimorgan", curie=ALLIANCE.curie('genetic_map_position_centimorgan'),
                   model_uri=ALLIANCE.genetic_map_position_centimorgan, domain=GeneticMapPosition, range=Optional[Union[float, List[float]]])

slots.genetic_map_position_centimorgan_error = Slot(uri=ALLIANCE.genetic_map_position_centimorgan_error, name="genetic_map_position_centimorgan_error", curie=ALLIANCE.curie('genetic_map_position_centimorgan_error'),
                   model_uri=ALLIANCE.genetic_map_position_centimorgan_error, domain=GeneticMapPosition, range=Optional[Union[float, List[float]]])

slots.genetic_map_position_radiation = Slot(uri=ALLIANCE.genetic_map_position_radiation, name="genetic_map_position_radiation", curie=ALLIANCE.curie('genetic_map_position_radiation'),
                   model_uri=ALLIANCE.genetic_map_position_radiation, domain=GeneticMapPosition, range=Optional[Union[float, List[float]]])

slots.current_status = Slot(uri=ALLIANCE.current_status, name="current_status", curie=ALLIANCE.curie('current_status'),
                   model_uri=ALLIANCE.current_status, domain=GeneHistory, range=Optional[Union[str, List[str]]])

slots.current_version = Slot(uri=ALLIANCE.current_version, name="current_version", curie=ALLIANCE.curie('current_version'),
                   model_uri=ALLIANCE.current_version, domain=GeneHistory, range=Optional[int])

slots.merged_into = Slot(uri=ALLIANCE.merged_into, name="merged_into", curie=ALLIANCE.curie('merged_into'),
                   model_uri=ALLIANCE.merged_into, domain=GeneHistory, range=Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]])

slots.acquires_merge = Slot(uri=ALLIANCE.acquires_merge, name="acquires_merge", curie=ALLIANCE.curie('acquires_merge'),
                   model_uri=ALLIANCE.acquires_merge, domain=GeneHistory, range=Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]])

slots.split_from = Slot(uri=ALLIANCE.split_from, name="split_from", curie=ALLIANCE.curie('split_from'),
                   model_uri=ALLIANCE.split_from, domain=GeneHistory, range=Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]])

slots.split_into = Slot(uri=ALLIANCE.split_into, name="split_into", curie=ALLIANCE.curie('split_into'),
                   model_uri=ALLIANCE.split_into, domain=GeneHistory, range=Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]])

slots.evidence = Slot(uri=ALLIANCE.evidence, name="evidence", curie=ALLIANCE.curie('evidence'),
                   model_uri=ALLIANCE.evidence, domain=None, range=Optional[Union[Union[str, InformationContentEntityCurie], List[Union[str, InformationContentEntityCurie]]]])

slots.evidence_curies = Slot(uri=ALLIANCE.evidence_curies, name="evidence_curies", curie=ALLIANCE.curie('evidence_curies'),
                   model_uri=ALLIANCE.evidence_curies, domain=None, range=Optional[Union[str, List[str]]])

slots.reference_id = Slot(uri=ALLIANCE.reference_id, name="reference_id", curie=ALLIANCE.curie('reference_id'),
                   model_uri=ALLIANCE.reference_id, domain=None, range=int)

slots.mesh_detail_id = Slot(uri=ALLIANCE.mesh_detail_id, name="mesh_detail_id", curie=ALLIANCE.curie('mesh_detail_id'),
                   model_uri=ALLIANCE.mesh_detail_id, domain=MeshDetail, range=int)

slots.resource_id = Slot(uri=ALLIANCE.resource_id, name="resource_id", curie=ALLIANCE.curie('resource_id'),
                   model_uri=ALLIANCE.resource_id, domain=Reference, range=Optional[int])

slots.heading_term = Slot(uri=ALLIANCE.heading_term, name="heading_term", curie=ALLIANCE.curie('heading_term'),
                   model_uri=ALLIANCE.heading_term, domain=MeshDetail, range=str)

slots.qualifier_term = Slot(uri=ALLIANCE.qualifier_term, name="qualifier_term", curie=ALLIANCE.curie('qualifier_term'),
                   model_uri=ALLIANCE.qualifier_term, domain=MeshDetail, range=Optional[str])

slots.pubmed_type = Slot(uri=ALLIANCE.pubmed_type, name="pubmed_type", curie=ALLIANCE.curie('pubmed_type'),
                   model_uri=ALLIANCE.pubmed_type, domain=Reference, range=Optional[Union[Union[str, "PubmedTypeEnum"], List[Union[str, "PubmedTypeEnum"]]]])

slots.date_published = Slot(uri=ALLIANCE.date_published, name="date_published", curie=ALLIANCE.curie('date_published'),
                   model_uri=ALLIANCE.date_published, domain=None, range=Optional[str])

slots.date_arrived_in_pubmed = Slot(uri=ALLIANCE.date_arrived_in_pubmed, name="date_arrived_in_pubmed", curie=ALLIANCE.curie('date_arrived_in_pubmed'),
                   model_uri=ALLIANCE.date_arrived_in_pubmed, domain=Reference, range=Optional[Union[str, List[str]]])

slots.date_last_modified_in_pubmed = Slot(uri=ALLIANCE.date_last_modified_in_pubmed, name="date_last_modified_in_pubmed", curie=ALLIANCE.curie('date_last_modified_in_pubmed'),
                   model_uri=ALLIANCE.date_last_modified_in_pubmed, domain=Reference, range=Optional[str])

slots.open_access = Slot(uri=ALLIANCE.open_access, name="open_access", curie=ALLIANCE.curie('open_access'),
                   model_uri=ALLIANCE.open_access, domain=Reference, range=Optional[Union[bool, Bool]])

slots.page_range = Slot(uri=ALLIANCE.page_range, name="page_range", curie=ALLIANCE.curie('page_range'),
                   model_uri=ALLIANCE.page_range, domain=None, range=Optional[str])

slots.plain_language_abstract = Slot(uri=ALLIANCE.plain_language_abstract, name="plain_language_abstract", curie=ALLIANCE.curie('plain_language_abstract'),
                   model_uri=ALLIANCE.plain_language_abstract, domain=Reference, range=Optional[str])

slots.pubmed_abstract_languages = Slot(uri=ALLIANCE.pubmed_abstract_languages, name="pubmed_abstract_languages", curie=ALLIANCE.curie('pubmed_abstract_languages'),
                   model_uri=ALLIANCE.pubmed_abstract_languages, domain=Reference, range=Optional[Union[str, List[str]]])

slots.pubmed_publication_status = Slot(uri=ALLIANCE.pubmed_publication_status, name="pubmed_publication_status", curie=ALLIANCE.curie('pubmed_publication_status'),
                   model_uri=ALLIANCE.pubmed_publication_status, domain=Reference, range=Optional[Union[str, "PubmedPublicationStatusEnum"]])

slots.abstract = Slot(uri=ALLIANCE.abstract, name="abstract", curie=ALLIANCE.curie('abstract'),
                   model_uri=ALLIANCE.abstract, domain=Reference, range=Optional[str])

slots.issue_name = Slot(uri=ALLIANCE.issue_name, name="issue_name", curie=ALLIANCE.curie('issue_name'),
                   model_uri=ALLIANCE.issue_name, domain=Reference, range=Optional[str])

slots.category = Slot(uri=ALLIANCE.category, name="category", curie=ALLIANCE.curie('category'),
                   model_uri=ALLIANCE.category, domain=Reference, range=Optional[Union[str, "ReferenceCategoryEnum"]])

slots.keywords = Slot(uri=ALLIANCE.keywords, name="keywords", curie=ALLIANCE.curie('keywords'),
                   model_uri=ALLIANCE.keywords, domain=None, range=Optional[Union[str, List[str]]])

slots.language = Slot(uri=ALLIANCE.language, name="language", curie=ALLIANCE.curie('language'),
                   model_uri=ALLIANCE.language, domain=Reference, range=Optional[str])

slots.merged_into_id = Slot(uri=ALLIANCE.merged_into_id, name="merged_into_id", curie=ALLIANCE.curie('merged_into_id'),
                   model_uri=ALLIANCE.merged_into_id, domain=Reference, range=Optional[Union[str, URIorCURIE]])

slots.authors = Slot(uri=ALLIANCE.authors, name="authors", curie=ALLIANCE.curie('authors'),
                   model_uri=ALLIANCE.authors, domain=Reference, range=Optional[Union[Union[dict, AuthorReference], List[Union[dict, AuthorReference]]]])

slots.corresponding_author = Slot(uri=ALLIANCE.corresponding_author, name="corresponding_author", curie=ALLIANCE.curie('corresponding_author'),
                   model_uri=ALLIANCE.corresponding_author, domain=AuthorReference, range=Optional[Union[bool, Bool]])

slots.first_author = Slot(uri=ALLIANCE.first_author, name="first_author", curie=ALLIANCE.curie('first_author'),
                   model_uri=ALLIANCE.first_author, domain=AuthorReference, range=Optional[Union[bool, Bool]])

slots.title = Slot(uri=ALLIANCE.title, name="title", curie=ALLIANCE.curie('title'),
                   model_uri=ALLIANCE.title, domain=Reference, range=Optional[str])

slots.volume = Slot(uri=ALLIANCE.volume, name="volume", curie=ALLIANCE.curie('volume'),
                   model_uri=ALLIANCE.volume, domain=Reference, range=Optional[str])

slots.publisher = Slot(uri=ALLIANCE.publisher, name="publisher", curie=ALLIANCE.curie('publisher'),
                   model_uri=ALLIANCE.publisher, domain=Reference, range=Optional[str])

slots.reference_curie = Slot(uri=ALLIANCE.reference_curie, name="reference_curie", curie=ALLIANCE.curie('reference_curie'),
                   model_uri=ALLIANCE.reference_curie, domain=None, range=Optional[str])

slots.reference_curies = Slot(uri=ALLIANCE.reference_curies, name="reference_curies", curie=ALLIANCE.curie('reference_curies'),
                   model_uri=ALLIANCE.reference_curies, domain=None, range=Optional[Union[str, List[str]]])

slots.name = Slot(uri=ALLIANCE.name, name="name", curie=ALLIANCE.curie('name'),
                   model_uri=ALLIANCE.name, domain=None, range=Optional[str])

slots.agm_curie = Slot(uri=ALLIANCE.agm_curie, name="agm_curie", curie=ALLIANCE.curie('agm_curie'),
                   model_uri=ALLIANCE.agm_curie, domain=None, range=str)

slots.subtype = Slot(uri=ALLIANCE.subtype, name="subtype", curie=ALLIANCE.curie('subtype'),
                   model_uri=ALLIANCE.subtype, domain=AffectedGenomicModel, range=Union[str, VocabularyTermName])

slots.subtype_name = Slot(uri=ALLIANCE.subtype_name, name="subtype_name", curie=ALLIANCE.curie('subtype_name'),
                   model_uri=ALLIANCE.subtype_name, domain=AffectedGenomicModelDTO, range=str)

slots.components = Slot(uri=ALLIANCE.components, name="components", curie=ALLIANCE.curie('components'),
                   model_uri=ALLIANCE.components, domain=AffectedGenomicModel, range=Optional[Union[Union[dict, "AffectedGenomicModelComponent"], List[Union[dict, "AffectedGenomicModelComponent"]]]])

slots.component_dtos = Slot(uri=ALLIANCE.component_dtos, name="component_dtos", curie=ALLIANCE.curie('component_dtos'),
                   model_uri=ALLIANCE.component_dtos, domain=AffectedGenomicModelDTO, range=Optional[Union[Union[dict, "AffectedGenomicModelComponentDTO"], List[Union[dict, "AffectedGenomicModelComponentDTO"]]]])

slots.has_allele = Slot(uri=ALLIANCE.has_allele, name="has_allele", curie=ALLIANCE.curie('has_allele'),
                   model_uri=ALLIANCE.has_allele, domain=AffectedGenomicModelComponent, range=Optional[Union[str, AlleleCurie]])

slots.zygosity = Slot(uri=ALLIANCE.zygosity, name="zygosity", curie=ALLIANCE.curie('zygosity'),
                   model_uri=ALLIANCE.zygosity, domain=AffectedGenomicModelComponent, range=Optional[Union[str, "ZygosityValues"]])

slots.zygosity_curie = Slot(uri=ALLIANCE.zygosity_curie, name="zygosity_curie", curie=ALLIANCE.curie('zygosity_curie'),
                   model_uri=ALLIANCE.zygosity_curie, domain=AffectedGenomicModelComponentDTO, range=Optional[str])

slots.sequence_targeting_reagents = Slot(uri=ALLIANCE.sequence_targeting_reagents, name="sequence_targeting_reagents", curie=ALLIANCE.curie('sequence_targeting_reagents'),
                   model_uri=ALLIANCE.sequence_targeting_reagents, domain=AffectedGenomicModel, range=Optional[Union[Union[str, SequenceTargetingReagentCurie], List[Union[str, SequenceTargetingReagentCurie]]]])

slots.sequence_targeting_reagent_curies = Slot(uri=ALLIANCE.sequence_targeting_reagent_curies, name="sequence_targeting_reagent_curies", curie=ALLIANCE.curie('sequence_targeting_reagent_curies'),
                   model_uri=ALLIANCE.sequence_targeting_reagent_curies, domain=AffectedGenomicModelDTO, range=Optional[Union[str, List[str]]])

slots.parental_populations = Slot(uri=ALLIANCE.parental_populations, name="parental_populations", curie=ALLIANCE.curie('parental_populations'),
                   model_uri=ALLIANCE.parental_populations, domain=AffectedGenomicModel, range=Optional[Union[str, URIorCURIE]])

slots.affiliated_alliance_member = Slot(uri=ALLIANCE.affiliated_alliance_member, name="affiliated_alliance_member", curie=ALLIANCE.curie('affiliated_alliance_member'),
                   model_uri=ALLIANCE.affiliated_alliance_member, domain=Person, range=Optional[Union[dict, "AllianceMember"]])

slots.orcid = Slot(uri=ALLIANCE.orcid, name="orcid", curie=ALLIANCE.curie('orcid'),
                   model_uri=ALLIANCE.orcid, domain=Person, range=Optional[Union[str, URIorCURIE]])

slots.emails = Slot(uri=ALLIANCE.emails, name="emails", curie=ALLIANCE.curie('emails'),
                   model_uri=ALLIANCE.emails, domain=None, range=Optional[Union[str, List[str]]])

slots.old_emails = Slot(uri=ALLIANCE.old_emails, name="old_emails", curie=ALLIANCE.curie('old_emails'),
                   model_uri=ALLIANCE.old_emails, domain=None, range=Optional[Union[str, List[str]]])

slots.okta_id = Slot(uri=ALLIANCE.okta_id, name="okta_id", curie=ALLIANCE.curie('okta_id'),
                   model_uri=ALLIANCE.okta_id, domain=LoggedInPerson, range=Optional[str])

slots.okta_email = Slot(uri=ALLIANCE.okta_email, name="okta_email", curie=ALLIANCE.curie('okta_email'),
                   model_uri=ALLIANCE.okta_email, domain=LoggedInPerson, range=Optional[str])

slots.user_settings = Slot(uri=ALLIANCE.user_settings, name="user_settings", curie=ALLIANCE.curie('user_settings'),
                   model_uri=ALLIANCE.user_settings, domain=LoggedInPerson, range=Optional[str])

slots.api_token = Slot(uri=ALLIANCE.api_token, name="api_token", curie=ALLIANCE.curie('api_token'),
                   model_uri=ALLIANCE.api_token, domain=LoggedInPerson, range=Optional[str])

slots.short_name = Slot(uri=ALLIANCE.short_name, name="short_name", curie=ALLIANCE.curie('short_name'),
                   model_uri=ALLIANCE.short_name, domain=Organization, range=str)

slots.full_name = Slot(uri=ALLIANCE.full_name, name="full_name", curie=ALLIANCE.curie('full_name'),
                   model_uri=ALLIANCE.full_name, domain=Organization, range=str)

slots.homepage_resource_descriptor_page = Slot(uri=ALLIANCE.homepage_resource_descriptor_page, name="homepage_resource_descriptor_page", curie=ALLIANCE.curie('homepage_resource_descriptor_page'),
                   model_uri=ALLIANCE.homepage_resource_descriptor_page, domain=Organization, range=Optional[Union[dict, "ResourceDescriptorPage"]])

slots.caption = Slot(uri=ALLIANCE.caption, name="caption", curie=ALLIANCE.curie('caption'),
                   model_uri=ALLIANCE.caption, domain=Figure, range=Optional[str])

slots.cropped_from = Slot(uri=ALLIANCE.cropped_from, name="cropped_from", curie=ALLIANCE.curie('cropped_from'),
                   model_uri=ALLIANCE.cropped_from, domain=Image, range=Optional[Union[str, ImageCurie]])

slots.associated_with_figure = Slot(uri=ALLIANCE.associated_with_figure, name="associated_with_figure", curie=ALLIANCE.curie('associated_with_figure'),
                   model_uri=ALLIANCE.associated_with_figure, domain=None, range=Optional[Union[str, FigureCurie]])

slots.from_image = Slot(uri=ALLIANCE.from_image, name="from_image", curie=ALLIANCE.curie('from_image'),
                   model_uri=ALLIANCE.from_image, domain=ImagePane, range=Optional[Union[str, ImageCurie]])

slots.height = Slot(uri=ALLIANCE.height, name="height", curie=ALLIANCE.curie('height'),
                   model_uri=ALLIANCE.height, domain=Image, range=int)

slots.image_file = Slot(uri=ALLIANCE.image_file, name="image_file", curie=ALLIANCE.curie('image_file'),
                   model_uri=ALLIANCE.image_file, domain=Image, range=Union[dict, File])

slots.image_medium_file = Slot(uri=ALLIANCE.image_medium_file, name="image_medium_file", curie=ALLIANCE.curie('image_medium_file'),
                   model_uri=ALLIANCE.image_medium_file, domain=Image, range=Union[dict, File])

slots.image_thumbnail_file = Slot(uri=ALLIANCE.image_thumbnail_file, name="image_thumbnail_file", curie=ALLIANCE.curie('image_thumbnail_file'),
                   model_uri=ALLIANCE.image_thumbnail_file, domain=Image, range=Union[dict, File])

slots.image_x_origin = Slot(uri=ALLIANCE.image_x_origin, name="image_x_origin", curie=ALLIANCE.curie('image_x_origin'),
                   model_uri=ALLIANCE.image_x_origin, domain=None, range=Optional[int])

slots.image_y_origin = Slot(uri=ALLIANCE.image_y_origin, name="image_y_origin", curie=ALLIANCE.curie('image_y_origin'),
                   model_uri=ALLIANCE.image_y_origin, domain=None, range=Optional[int])

slots.images = Slot(uri=ALLIANCE.images, name="images", curie=ALLIANCE.curie('images'),
                   model_uri=ALLIANCE.images, domain=None, range=Optional[Union[str, ImageCurie]])

slots.label = Slot(uri=ALLIANCE.label, name="label", curie=ALLIANCE.curie('label'),
                   model_uri=ALLIANCE.label, domain=None, range=Optional[str])

slots.video_still = Slot(uri=ALLIANCE.video_still, name="video_still", curie=ALLIANCE.curie('video_still'),
                   model_uri=ALLIANCE.video_still, domain=Image, range=Optional[Union[bool, Bool]])

slots.width = Slot(uri=ALLIANCE.width, name="width", curie=ALLIANCE.curie('width'),
                   model_uri=ALLIANCE.width, domain=Image, range=int)

slots.image_curie = Slot(uri=ALLIANCE.image_curie, name="image_curie", curie=ALLIANCE.curie('image_curie'),
                   model_uri=ALLIANCE.image_curie, domain=None, range=str)

slots.text_synonyms = Slot(uri=ALLIANCE.text_synonyms, name="text_synonyms", curie=ALLIANCE.curie('text_synonyms'),
                   model_uri=ALLIANCE.text_synonyms, domain=VocabularyTerm, range=Optional[Union[str, List[str]]])

slots.member_terms = Slot(uri=ALLIANCE.member_terms, name="member_terms", curie=ALLIANCE.curie('member_terms'),
                   model_uri=ALLIANCE.member_terms, domain=None, range=Optional[Union[Union[str, VocabularyTermName], List[Union[str, VocabularyTermName]]]])

slots.vocabulary_description = Slot(uri=ALLIANCE.vocabulary_description, name="vocabulary_description", curie=ALLIANCE.curie('vocabulary_description'),
                   model_uri=ALLIANCE.vocabulary_description, domain=None, range=Optional[str])

slots.vocabulary_term_set_description = Slot(uri=ALLIANCE.vocabulary_term_set_description, name="vocabulary_term_set_description", curie=ALLIANCE.curie('vocabulary_term_set_description'),
                   model_uri=ALLIANCE.vocabulary_term_set_description, domain=VocabularyTermSet, range=Optional[str])

slots.vocabulary_term_set_vocabulary = Slot(uri=ALLIANCE.vocabulary_term_set_vocabulary, name="vocabulary_term_set_vocabulary", curie=ALLIANCE.curie('vocabulary_term_set_vocabulary'),
                   model_uri=ALLIANCE.vocabulary_term_set_vocabulary, domain=VocabularyTermSet, range=Union[str, VocabularyName])

slots.variant_curie = Slot(uri=ALLIANCE.variant_curie, name="variant_curie", curie=ALLIANCE.curie('variant_curie'),
                   model_uri=ALLIANCE.variant_curie, domain=None, range=Optional[str])

slots.variant_status = Slot(uri=ALLIANCE.variant_status, name="variant_status", curie=ALLIANCE.curie('variant_status'),
                   model_uri=ALLIANCE.variant_status, domain=None, range=Optional[Union[str, "VariantStatusEnum"]])

slots.variant_type = Slot(uri=ALLIANCE.variant_type, name="variant_type", curie=ALLIANCE.curie('variant_type'),
                   model_uri=ALLIANCE.variant_type, domain=Variant, range=Union[str, SOTermCurie])

slots.source_general_consequence = Slot(uri=ALLIANCE.source_general_consequence, name="source_general_consequence", curie=ALLIANCE.curie('source_general_consequence'),
                   model_uri=ALLIANCE.source_general_consequence, domain=Variant, range=Optional[Union[str, SOTermCurie]])

slots.consequence = Slot(uri=ALLIANCE.consequence, name="consequence", curie=ALLIANCE.curie('consequence'),
                   model_uri=ALLIANCE.consequence, domain=VariantLocation, range=Optional[Union[str, SOTermCurie]])

slots.curated_consequence = Slot(uri=ALLIANCE.curated_consequence, name="curated_consequence", curie=ALLIANCE.curie('curated_consequence'),
                   model_uri=ALLIANCE.curated_consequence, domain=VariantLocation, range=Optional[Union[str, SOTermCurie]])

slots.variant_locations = Slot(uri=ALLIANCE.variant_locations, name="variant_locations", curie=ALLIANCE.curie('variant_locations'),
                   model_uri=ALLIANCE.variant_locations, domain=Variant, range=Optional[Union[Union[dict, "VariantLocation"], List[Union[dict, "VariantLocation"]]]])

slots.variant_genome_locations = Slot(uri=ALLIANCE.variant_genome_locations, name="variant_genome_locations", curie=ALLIANCE.curie('variant_genome_locations'),
                   model_uri=ALLIANCE.variant_genome_locations, domain=Variant, range=Union[Union[dict, "VariantGenomeLocation"], List[Union[dict, "VariantGenomeLocation"]]])

slots.variant_polypeptide_locations = Slot(uri=ALLIANCE.variant_polypeptide_locations, name="variant_polypeptide_locations", curie=ALLIANCE.curie('variant_polypeptide_locations'),
                   model_uri=ALLIANCE.variant_polypeptide_locations, domain=Variant, range=Optional[Union[Union[dict, "VariantPolypeptideLocation"], List[Union[dict, "VariantPolypeptideLocation"]]]])

slots.variant_transcript_locations = Slot(uri=ALLIANCE.variant_transcript_locations, name="variant_transcript_locations", curie=ALLIANCE.curie('variant_transcript_locations'),
                   model_uri=ALLIANCE.variant_transcript_locations, domain=Variant, range=Optional[Union[Union[dict, "VariantTranscriptLocation"], List[Union[dict, "VariantTranscriptLocation"]]]])

slots.source_variant_locations = Slot(uri=ALLIANCE.source_variant_locations, name="source_variant_locations", curie=ALLIANCE.curie('source_variant_locations'),
                   model_uri=ALLIANCE.source_variant_locations, domain=Variant, range=Optional[Union[Union[dict, "SourceVariantLocation"], List[Union[dict, "SourceVariantLocation"]]]])

slots.hgvs = Slot(uri=ALLIANCE.hgvs, name="hgvs", curie=ALLIANCE.curie('hgvs'),
                   model_uri=ALLIANCE.hgvs, domain=VariantLocation, range=str)

slots.assembly = Slot(uri=ALLIANCE.assembly, name="assembly", curie=ALLIANCE.curie('assembly'),
                   model_uri=ALLIANCE.assembly, domain=VariantLocation, range=Optional[Union[str, AssemblyCurie]])

slots.chromosome = Slot(uri=ALLIANCE.chromosome, name="chromosome", curie=ALLIANCE.curie('chromosome'),
                   model_uri=ALLIANCE.chromosome, domain=VariantLocation, range=Optional[Union[str, ChromosomeCurie]])

slots.start_position = Slot(uri=ALLIANCE.start_position, name="start_position", curie=ALLIANCE.curie('start_position'),
                   model_uri=ALLIANCE.start_position, domain=VariantLocation, range=Optional[int])

slots.end_position = Slot(uri=ALLIANCE.end_position, name="end_position", curie=ALLIANCE.curie('end_position'),
                   model_uri=ALLIANCE.end_position, domain=VariantLocation, range=Optional[int])

slots.reference_sequence = Slot(uri=ALLIANCE.reference_sequence, name="reference_sequence", curie=ALLIANCE.curie('reference_sequence'),
                   model_uri=ALLIANCE.reference_sequence, domain=VariantLocation, range=Optional[Union[str, BiologicalSequence]])

slots.variant_sequence = Slot(uri=ALLIANCE.variant_sequence, name="variant_sequence", curie=ALLIANCE.curie('variant_sequence'),
                   model_uri=ALLIANCE.variant_sequence, domain=VariantLocation, range=Optional[Union[str, BiologicalSequence]])

slots.transcript = Slot(uri=ALLIANCE.transcript, name="transcript", curie=ALLIANCE.curie('transcript'),
                   model_uri=ALLIANCE.transcript, domain=VariantTranscriptLocation, range=Optional[Union[str, TranscriptCurie]])

slots.polypeptide = Slot(uri=ALLIANCE.polypeptide, name="polypeptide", curie=ALLIANCE.curie('polypeptide'),
                   model_uri=ALLIANCE.polypeptide, domain=VariantTranscriptLocation, range=Union[str, TranscriptCurie])

slots.associated_transcripts = Slot(uri=ALLIANCE.associated_transcripts, name="associated_transcripts", curie=ALLIANCE.curie('associated_transcripts'),
                   model_uri=ALLIANCE.associated_transcripts, domain=VariantPolypeptideLocation, range=Optional[Union[Union[str, TranscriptCurie], List[Union[str, TranscriptCurie]]]])

slots.definition = Slot(uri=ALLIANCE.definition, name="definition", curie=ALLIANCE.curie('definition'),
                   model_uri=ALLIANCE.definition, domain=None, range=Optional[str])

slots.display_synonym = Slot(uri=ALLIANCE.display_synonym, name="display_synonym", curie=ALLIANCE.curie('display_synonym'),
                   model_uri=ALLIANCE.display_synonym, domain=None, range=Optional[str])

slots.namespace = Slot(uri=ALLIANCE.namespace, name="namespace", curie=ALLIANCE.curie('namespace'),
                   model_uri=ALLIANCE.namespace, domain=None, range=Optional[str])

slots.subsets = Slot(uri=ALLIANCE.subsets, name="subsets", curie=ALLIANCE.curie('subsets'),
                   model_uri=ALLIANCE.subsets, domain=None, range=Optional[Union[str, List[str]]])

slots.definition_urls = Slot(uri=ALLIANCE.definition_urls, name="definition_urls", curie=ALLIANCE.curie('definition_urls'),
                   model_uri=ALLIANCE.definition_urls, domain=None, range=Optional[Union[str, List[str]]])

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

slots.ancestors = Slot(uri=ALLIANCE.ancestors, name="ancestors", curie=ALLIANCE.curie('ancestors'),
                   model_uri=ALLIANCE.ancestors, domain=None, range=Optional[Union[Union[dict, OntologyTermClosure], List[Union[dict, OntologyTermClosure]]]])

slots.descendants = Slot(uri=ALLIANCE.descendants, name="descendants", curie=ALLIANCE.curie('descendants'),
                   model_uri=ALLIANCE.descendants, domain=None, range=Optional[Union[Union[dict, OntologyTermClosure], List[Union[dict, OntologyTermClosure]]]])

slots.relationship_type = Slot(uri=ALLIANCE.relationship_type, name="relationship_type", curie=ALLIANCE.curie('relationship_type'),
                   model_uri=ALLIANCE.relationship_type, domain=None, range=Optional[Union[str, List[str]]])

slots.distance_between = Slot(uri=ALLIANCE.distance_between, name="distance_between", curie=ALLIANCE.curie('distance_between'),
                   model_uri=ALLIANCE.distance_between, domain=None, range=Optional[int])

slots.evidence_code_curie = Slot(uri=ALLIANCE.evidence_code_curie, name="evidence_code_curie", curie=ALLIANCE.curie('evidence_code_curie'),
                   model_uri=ALLIANCE.evidence_code_curie, domain=None, range=Optional[str])

slots.evidence_code_curies = Slot(uri=ALLIANCE.evidence_code_curies, name="evidence_code_curies", curie=ALLIANCE.curie('evidence_code_curies'),
                   model_uri=ALLIANCE.evidence_code_curies, domain=None, range=Optional[Union[str, List[str]]])

slots.annotation_type = Slot(uri=ALLIANCE.annotation_type, name="annotation_type", curie=ALLIANCE.curie('annotation_type'),
                   model_uri=ALLIANCE.annotation_type, domain=None, range=Optional[Union[str, VocabularyTermName]])

slots.annotation_type_name = Slot(uri=ALLIANCE.annotation_type_name, name="annotation_type_name", curie=ALLIANCE.curie('annotation_type_name'),
                   model_uri=ALLIANCE.annotation_type_name, domain=DiseaseAnnotationDTO, range=Optional[str])

slots.asserted_allele = Slot(uri=ALLIANCE.asserted_allele, name="asserted_allele", curie=ALLIANCE.curie('asserted_allele'),
                   model_uri=ALLIANCE.asserted_allele, domain=None, range=Optional[Union[str, AlleleCurie]])

slots.asserted_allele_curie = Slot(uri=ALLIANCE.asserted_allele_curie, name="asserted_allele_curie", curie=ALLIANCE.curie('asserted_allele_curie'),
                   model_uri=ALLIANCE.asserted_allele_curie, domain=None, range=Optional[str])

slots.asserted_genes = Slot(uri=ALLIANCE.asserted_genes, name="asserted_genes", curie=ALLIANCE.curie('asserted_genes'),
                   model_uri=ALLIANCE.asserted_genes, domain=None, range=Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]])

slots.asserted_gene_curies = Slot(uri=ALLIANCE.asserted_gene_curies, name="asserted_gene_curies", curie=ALLIANCE.curie('asserted_gene_curies'),
                   model_uri=ALLIANCE.asserted_gene_curies, domain=None, range=Optional[Union[str, List[str]]])

slots.condition_anatomy = Slot(uri=ALLIANCE.condition_anatomy, name="condition_anatomy", curie=ALLIANCE.curie('condition_anatomy'),
                   model_uri=ALLIANCE.condition_anatomy, domain=ExperimentalCondition, range=Optional[Union[str, AnatomicalTermCurie]])

slots.condition_anatomy_curie = Slot(uri=ALLIANCE.condition_anatomy_curie, name="condition_anatomy_curie", curie=ALLIANCE.curie('condition_anatomy_curie'),
                   model_uri=ALLIANCE.condition_anatomy_curie, domain=ExperimentalConditionDTO, range=Optional[str])

slots.condition_chemical = Slot(uri=ALLIANCE.condition_chemical, name="condition_chemical", curie=ALLIANCE.curie('condition_chemical'),
                   model_uri=ALLIANCE.condition_chemical, domain=ExperimentalCondition, range=Optional[Union[str, ChemicalTermCurie]])

slots.condition_chemical_curie = Slot(uri=ALLIANCE.condition_chemical_curie, name="condition_chemical_curie", curie=ALLIANCE.curie('condition_chemical_curie'),
                   model_uri=ALLIANCE.condition_chemical_curie, domain=ExperimentalConditionDTO, range=Optional[str])

slots.condition_class = Slot(uri=ALLIANCE.condition_class, name="condition_class", curie=ALLIANCE.curie('condition_class'),
                   model_uri=ALLIANCE.condition_class, domain=ExperimentalCondition, range=Union[str, ZECOTermCurie])

slots.condition_class_curie = Slot(uri=ALLIANCE.condition_class_curie, name="condition_class_curie", curie=ALLIANCE.curie('condition_class_curie'),
                   model_uri=ALLIANCE.condition_class_curie, domain=ExperimentalConditionDTO, range=str)

slots.condition_free_text = Slot(uri=ALLIANCE.condition_free_text, name="condition_free_text", curie=ALLIANCE.curie('condition_free_text'),
                   model_uri=ALLIANCE.condition_free_text, domain=ExperimentalCondition, range=Optional[str])

slots.condition_gene_ontology = Slot(uri=ALLIANCE.condition_gene_ontology, name="condition_gene_ontology", curie=ALLIANCE.curie('condition_gene_ontology'),
                   model_uri=ALLIANCE.condition_gene_ontology, domain=ExperimentalCondition, range=Optional[Union[str, GOTermCurie]])

slots.condition_gene_ontology_curie = Slot(uri=ALLIANCE.condition_gene_ontology_curie, name="condition_gene_ontology_curie", curie=ALLIANCE.curie('condition_gene_ontology_curie'),
                   model_uri=ALLIANCE.condition_gene_ontology_curie, domain=ExperimentalConditionDTO, range=Optional[str])

slots.condition_id = Slot(uri=ALLIANCE.condition_id, name="condition_id", curie=ALLIANCE.curie('condition_id'),
                   model_uri=ALLIANCE.condition_id, domain=ExperimentalCondition, range=Optional[Union[str, ExperimentalConditionOntologyTermCurie]])

slots.condition_id_curie = Slot(uri=ALLIANCE.condition_id_curie, name="condition_id_curie", curie=ALLIANCE.curie('condition_id_curie'),
                   model_uri=ALLIANCE.condition_id_curie, domain=ExperimentalConditionDTO, range=Optional[str])

slots.condition_quantity = Slot(uri=ALLIANCE.condition_quantity, name="condition_quantity", curie=ALLIANCE.curie('condition_quantity'),
                   model_uri=ALLIANCE.condition_quantity, domain=ExperimentalCondition, range=Optional[str])

slots.condition_relation_type = Slot(uri=ALLIANCE.condition_relation_type, name="condition_relation_type", curie=ALLIANCE.curie('condition_relation_type'),
                   model_uri=ALLIANCE.condition_relation_type, domain=ConditionRelation, range=Optional[Union[str, VocabularyTermName]])

slots.condition_relation_type_name = Slot(uri=ALLIANCE.condition_relation_type_name, name="condition_relation_type_name", curie=ALLIANCE.curie('condition_relation_type_name'),
                   model_uri=ALLIANCE.condition_relation_type_name, domain=ConditionRelationDTO, range=str)

slots.condition_relations = Slot(uri=ALLIANCE.condition_relations, name="condition_relations", curie=ALLIANCE.curie('condition_relations'),
                   model_uri=ALLIANCE.condition_relations, domain=None, range=Optional[Union[Union[dict, ConditionRelation], List[Union[dict, ConditionRelation]]]])

slots.condition_relation_dtos = Slot(uri=ALLIANCE.condition_relation_dtos, name="condition_relation_dtos", curie=ALLIANCE.curie('condition_relation_dtos'),
                   model_uri=ALLIANCE.condition_relation_dtos, domain=None, range=Optional[Union[Union[dict, ConditionRelationDTO], List[Union[dict, ConditionRelationDTO]]]])

slots.condition_summary = Slot(uri=ALLIANCE.condition_summary, name="condition_summary", curie=ALLIANCE.curie('condition_summary'),
                   model_uri=ALLIANCE.condition_summary, domain=ExperimentalCondition, range=Optional[str])

slots.condition_taxon = Slot(uri=ALLIANCE.condition_taxon, name="condition_taxon", curie=ALLIANCE.curie('condition_taxon'),
                   model_uri=ALLIANCE.condition_taxon, domain=ExperimentalCondition, range=Optional[Union[str, NCBITaxonTermCurie]])

slots.condition_taxon_curie = Slot(uri=ALLIANCE.condition_taxon_curie, name="condition_taxon_curie", curie=ALLIANCE.curie('condition_taxon_curie'),
                   model_uri=ALLIANCE.condition_taxon_curie, domain=ExperimentalConditionDTO, range=Optional[str])

slots.conditions = Slot(uri=ALLIANCE.conditions, name="conditions", curie=ALLIANCE.curie('conditions'),
                   model_uri=ALLIANCE.conditions, domain=None, range=Optional[Union[Union[dict, ExperimentalCondition], List[Union[dict, ExperimentalCondition]]]])

slots.condition_dtos = Slot(uri=ALLIANCE.condition_dtos, name="condition_dtos", curie=ALLIANCE.curie('condition_dtos'),
                   model_uri=ALLIANCE.condition_dtos, domain=ConditionRelationDTO, range=Union[Union[dict, ExperimentalConditionDTO], List[Union[dict, ExperimentalConditionDTO]]])

slots.disease_genetic_modifier = Slot(uri=ALLIANCE.disease_genetic_modifier, name="disease_genetic_modifier", curie=ALLIANCE.curie('disease_genetic_modifier'),
                   model_uri=ALLIANCE.disease_genetic_modifier, domain=None, range=Optional[str])

slots.disease_genetic_modifier_curie = Slot(uri=ALLIANCE.disease_genetic_modifier_curie, name="disease_genetic_modifier_curie", curie=ALLIANCE.curie('disease_genetic_modifier_curie'),
                   model_uri=ALLIANCE.disease_genetic_modifier_curie, domain=DiseaseAnnotationDTO, range=Optional[str])

slots.disease_genetic_modifier_relation = Slot(uri=ALLIANCE.disease_genetic_modifier_relation, name="disease_genetic_modifier_relation", curie=ALLIANCE.curie('disease_genetic_modifier_relation'),
                   model_uri=ALLIANCE.disease_genetic_modifier_relation, domain=None, range=Optional[Union[str, VocabularyTermName]])

slots.disease_genetic_modifier_relation_name = Slot(uri=ALLIANCE.disease_genetic_modifier_relation_name, name="disease_genetic_modifier_relation_name", curie=ALLIANCE.curie('disease_genetic_modifier_relation_name'),
                   model_uri=ALLIANCE.disease_genetic_modifier_relation_name, domain=DiseaseAnnotationDTO, range=Optional[str])

slots.disease_qualifiers = Slot(uri=ALLIANCE.disease_qualifiers, name="disease_qualifiers", curie=ALLIANCE.curie('disease_qualifiers'),
                   model_uri=ALLIANCE.disease_qualifiers, domain=DiseaseAnnotation, range=Optional[Union[Union[str, VocabularyTermName], List[Union[str, VocabularyTermName]]]])

slots.disease_qualifier_names = Slot(uri=ALLIANCE.disease_qualifier_names, name="disease_qualifier_names", curie=ALLIANCE.curie('disease_qualifier_names'),
                   model_uri=ALLIANCE.disease_qualifier_names, domain=DiseaseAnnotationDTO, range=Optional[Union[str, List[str]]])

slots.genetic_sex = Slot(uri=ALLIANCE.genetic_sex, name="genetic_sex", curie=ALLIANCE.curie('genetic_sex'),
                   model_uri=ALLIANCE.genetic_sex, domain=None, range=Optional[Union[str, VocabularyTermName]])

slots.genetic_sex_name = Slot(uri=ALLIANCE.genetic_sex_name, name="genetic_sex_name", curie=ALLIANCE.curie('genetic_sex_name'),
                   model_uri=ALLIANCE.genetic_sex_name, domain=DiseaseAnnotationDTO, range=Optional[str])

slots.handle = Slot(uri=ALLIANCE.handle, name="handle", curie=ALLIANCE.curie('handle'),
                   model_uri=ALLIANCE.handle, domain=None, range=Optional[str])

slots.inferred_gene = Slot(uri=ALLIANCE.inferred_gene, name="inferred_gene", curie=ALLIANCE.curie('inferred_gene'),
                   model_uri=ALLIANCE.inferred_gene, domain=None, range=Optional[Union[str, GeneCurie]])

slots.inferred_gene_curie = Slot(uri=ALLIANCE.inferred_gene_curie, name="inferred_gene_curie", curie=ALLIANCE.curie('inferred_gene_curie'),
                   model_uri=ALLIANCE.inferred_gene_curie, domain=None, range=Optional[str])

slots.inferred_allele = Slot(uri=ALLIANCE.inferred_allele, name="inferred_allele", curie=ALLIANCE.curie('inferred_allele'),
                   model_uri=ALLIANCE.inferred_allele, domain=None, range=Optional[Union[str, AlleleCurie]])

slots.inferred_allele_curie = Slot(uri=ALLIANCE.inferred_allele_curie, name="inferred_allele_curie", curie=ALLIANCE.curie('inferred_allele_curie'),
                   model_uri=ALLIANCE.inferred_allele_curie, domain=None, range=Optional[str])

slots.phenotype_term = Slot(uri=ALLIANCE.phenotype_term, name="phenotype_term", curie=ALLIANCE.curie('phenotype_term'),
                   model_uri=ALLIANCE.phenotype_term, domain=None, range=Optional[Union[str, PhenotypeTermCurie]])

slots.phenotype_term_curie = Slot(uri=ALLIANCE.phenotype_term_curie, name="phenotype_term_curie", curie=ALLIANCE.curie('phenotype_term_curie'),
                   model_uri=ALLIANCE.phenotype_term_curie, domain=None, range=Optional[str])

slots.phenotype_statement = Slot(uri=ALLIANCE.phenotype_statement, name="phenotype_statement", curie=ALLIANCE.curie('phenotype_statement'),
                   model_uri=ALLIANCE.phenotype_statement, domain=None, range=Optional[str])

slots.sgd_strain_background = Slot(uri=ALLIANCE.sgd_strain_background, name="sgd_strain_background", curie=ALLIANCE.curie('sgd_strain_background'),
                   model_uri=ALLIANCE.sgd_strain_background, domain=None, range=Optional[Union[str, AffectedGenomicModelCurie]])

slots.sgd_strain_background_curie = Slot(uri=ALLIANCE.sgd_strain_background_curie, name="sgd_strain_background_curie", curie=ALLIANCE.curie('sgd_strain_background_curie'),
                   model_uri=ALLIANCE.sgd_strain_background_curie, domain=GeneDiseaseAnnotationDTO, range=Optional[str])

slots.with_or_from = Slot(uri=ALLIANCE.with_or_from, name="with_or_from", curie=ALLIANCE.curie('with_or_from'),
                   model_uri=ALLIANCE.with_or_from, domain=None, range=Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]])

slots.with_gene_curies = Slot(uri=ALLIANCE.with_gene_curies, name="with_gene_curies", curie=ALLIANCE.curie('with_gene_curies'),
                   model_uri=ALLIANCE.with_gene_curies, domain=None, range=Optional[Union[str, List[str]]])

slots.disease_relation_name = Slot(uri=ALLIANCE.disease_relation_name, name="disease_relation_name", curie=ALLIANCE.curie('disease_relation_name'),
                   model_uri=ALLIANCE.disease_relation_name, domain=DiseaseAnnotationDTO, range=str)

slots.do_term_curie = Slot(uri=ALLIANCE.do_term_curie, name="do_term_curie", curie=ALLIANCE.curie('do_term_curie'),
                   model_uri=ALLIANCE.do_term_curie, domain=DiseaseAnnotationDTO, range=str)

slots.id = Slot(uri=ALLIANCE.id, name="id", curie=ALLIANCE.curie('id'),
                   model_uri=ALLIANCE.id, domain=None, range=Optional[str])

slots.iso_abbreviation = Slot(uri=ALLIANCE.iso_abbreviation, name="iso_abbreviation", curie=ALLIANCE.curie('iso_abbreviation'),
                   model_uri=ALLIANCE.iso_abbreviation, domain=Resource, range=Optional[str])

slots.medline_abbreviation = Slot(uri=ALLIANCE.medline_abbreviation, name="medline_abbreviation", curie=ALLIANCE.curie('medline_abbreviation'),
                   model_uri=ALLIANCE.medline_abbreviation, domain=Resource, range=Optional[str])

slots.copyright_date = Slot(uri=ALLIANCE.copyright_date, name="copyright_date", curie=ALLIANCE.curie('copyright_date'),
                   model_uri=ALLIANCE.copyright_date, domain=Resource, range=Optional[Union[str, XSDDate]])

slots.print_issn = Slot(uri=ALLIANCE.print_issn, name="print_issn", curie=ALLIANCE.curie('print_issn'),
                   model_uri=ALLIANCE.print_issn, domain=Resource, range=Optional[str])

slots.online_issn = Slot(uri=ALLIANCE.online_issn, name="online_issn", curie=ALLIANCE.curie('online_issn'),
                   model_uri=ALLIANCE.online_issn, domain=Resource, range=Optional[str])

slots.summary = Slot(uri=ALLIANCE.summary, name="summary", curie=ALLIANCE.curie('summary'),
                   model_uri=ALLIANCE.summary, domain=Resource, range=Optional[str])

slots.editors = Slot(uri=ALLIANCE.editors, name="editors", curie=ALLIANCE.curie('editors'),
                   model_uri=ALLIANCE.editors, domain=Resource, range=Optional[Union[Union[dict, AuthorReference], List[Union[dict, AuthorReference]]]])

slots.default_url_template = Slot(uri=ALLIANCE.default_url_template, name="default_url_template", curie=ALLIANCE.curie('default_url_template'),
                   model_uri=ALLIANCE.default_url_template, domain=ResourceDescriptor, range=Optional[str])

slots.id_example = Slot(uri=ALLIANCE.id_example, name="id_example", curie=ALLIANCE.curie('id_example'),
                   model_uri=ALLIANCE.id_example, domain=ResourceDescriptor, range=Optional[str])

slots.id_pattern = Slot(uri=ALLIANCE.id_pattern, name="id_pattern", curie=ALLIANCE.curie('id_pattern'),
                   model_uri=ALLIANCE.id_pattern, domain=ResourceDescriptor, range=Optional[str])

slots.page_description = Slot(uri=ALLIANCE.page_description, name="page_description", curie=ALLIANCE.curie('page_description'),
                   model_uri=ALLIANCE.page_description, domain=ResourceDescriptorPage, range=Optional[str])

slots.resource_pages = Slot(uri=ALLIANCE.resource_pages, name="resource_pages", curie=ALLIANCE.curie('resource_pages'),
                   model_uri=ALLIANCE.resource_pages, domain=ResourceDescriptor, range=Optional[Union[Union[dict, "ResourceDescriptorPage"], List[Union[dict, "ResourceDescriptorPage"]]]])

slots.url_template = Slot(uri=ALLIANCE.url_template, name="url_template", curie=ALLIANCE.curie('url_template'),
                   model_uri=ALLIANCE.url_template, domain=ResourceDescriptor, range=Optional[str])

slots.allele_curie = Slot(uri=ALLIANCE.allele_curie, name="allele_curie", curie=ALLIANCE.curie('allele_curie'),
                   model_uri=ALLIANCE.allele_curie, domain=None, range=str)

slots.allele_database_status_dto = Slot(uri=ALLIANCE.allele_database_status_dto, name="allele_database_status_dto", curie=ALLIANCE.curie('allele_database_status_dto'),
                   model_uri=ALLIANCE.allele_database_status_dto, domain=AlleleDTO, range=Optional[Union[dict, "AlleleDatabaseStatusSlotAnnotationDTO"]])

slots.allele_full_name_dto = Slot(uri=ALLIANCE.allele_full_name_dto, name="allele_full_name_dto", curie=ALLIANCE.curie('allele_full_name_dto'),
                   model_uri=ALLIANCE.allele_full_name_dto, domain=AlleleDTO, range=Optional[Union[dict, FullNameSlotAnnotationDTO]])

slots.allele_functional_impact_dtos = Slot(uri=ALLIANCE.allele_functional_impact_dtos, name="allele_functional_impact_dtos", curie=ALLIANCE.curie('allele_functional_impact_dtos'),
                   model_uri=ALLIANCE.allele_functional_impact_dtos, domain=AlleleDTO, range=Optional[Union[Union[dict, "AlleleFunctionalImpactSlotAnnotationDTO"], List[Union[dict, "AlleleFunctionalImpactSlotAnnotationDTO"]]]])

slots.allele_germline_transmission_status_dto = Slot(uri=ALLIANCE.allele_germline_transmission_status_dto, name="allele_germline_transmission_status_dto", curie=ALLIANCE.curie('allele_germline_transmission_status_dto'),
                   model_uri=ALLIANCE.allele_germline_transmission_status_dto, domain=AlleleDTO, range=Optional[Union[dict, "AlleleGermlineTransmissionStatusSlotAnnotationDTO"]])

slots.allele_inheritance_mode_dtos = Slot(uri=ALLIANCE.allele_inheritance_mode_dtos, name="allele_inheritance_mode_dtos", curie=ALLIANCE.curie('allele_inheritance_mode_dtos'),
                   model_uri=ALLIANCE.allele_inheritance_mode_dtos, domain=AlleleDTO, range=Optional[Union[Union[dict, "AlleleInheritanceModeSlotAnnotationDTO"], List[Union[dict, "AlleleInheritanceModeSlotAnnotationDTO"]]]])

slots.allele_molecular_mutation_dtos = Slot(uri=ALLIANCE.allele_molecular_mutation_dtos, name="allele_molecular_mutation_dtos", curie=ALLIANCE.curie('allele_molecular_mutation_dtos'),
                   model_uri=ALLIANCE.allele_molecular_mutation_dtos, domain=AlleleDTO, range=Optional[Union[Union[dict, "AlleleMolecularMutationSlotAnnotationDTO"], List[Union[dict, "AlleleMolecularMutationSlotAnnotationDTO"]]]])

slots.allele_mutation_type_dtos = Slot(uri=ALLIANCE.allele_mutation_type_dtos, name="allele_mutation_type_dtos", curie=ALLIANCE.curie('allele_mutation_type_dtos'),
                   model_uri=ALLIANCE.allele_mutation_type_dtos, domain=AlleleDTO, range=Optional[Union[Union[dict, "AlleleMutationTypeSlotAnnotationDTO"], List[Union[dict, "AlleleMutationTypeSlotAnnotationDTO"]]]])

slots.allele_nomenclature_event_dtos = Slot(uri=ALLIANCE.allele_nomenclature_event_dtos, name="allele_nomenclature_event_dtos", curie=ALLIANCE.curie('allele_nomenclature_event_dtos'),
                   model_uri=ALLIANCE.allele_nomenclature_event_dtos, domain=AlleleDTO, range=Optional[Union[Union[dict, "AlleleNomenclatureEventSlotAnnotationDTO"], List[Union[dict, "AlleleNomenclatureEventSlotAnnotationDTO"]]]])

slots.allele_note_dtos = Slot(uri=ALLIANCE.allele_note_dtos, name="allele_note_dtos", curie=ALLIANCE.curie('allele_note_dtos'),
                   model_uri=ALLIANCE.allele_note_dtos, domain=AlleleDTO, range=Optional[Union[Union[dict, "AlleleNoteSlotAnnotationDTO"], List[Union[dict, "AlleleNoteSlotAnnotationDTO"]]]])

slots.allele_secondary_id_dtos = Slot(uri=ALLIANCE.allele_secondary_id_dtos, name="allele_secondary_id_dtos", curie=ALLIANCE.curie('allele_secondary_id_dtos'),
                   model_uri=ALLIANCE.allele_secondary_id_dtos, domain=AlleleDTO, range=Optional[Union[Union[dict, "AlleleSecondaryIdSlotAnnotationDTO"], List[Union[dict, "AlleleSecondaryIdSlotAnnotationDTO"]]]])

slots.allele_symbol_dto = Slot(uri=ALLIANCE.allele_symbol_dto, name="allele_symbol_dto", curie=ALLIANCE.curie('allele_symbol_dto'),
                   model_uri=ALLIANCE.allele_symbol_dto, domain=AlleleDTO, range=Union[dict, SymbolSlotAnnotationDTO])

slots.allele_synonym_dtos = Slot(uri=ALLIANCE.allele_synonym_dtos, name="allele_synonym_dtos", curie=ALLIANCE.curie('allele_synonym_dtos'),
                   model_uri=ALLIANCE.allele_synonym_dtos, domain=AlleleDTO, range=Optional[Union[Union[dict, NameSlotAnnotationDTO], List[Union[dict, NameSlotAnnotationDTO]]]])

slots.cell_line_curie = Slot(uri=ALLIANCE.cell_line_curie, name="cell_line_curie", curie=ALLIANCE.curie('cell_line_curie'),
                   model_uri=ALLIANCE.cell_line_curie, domain=None, range=str)

slots.chemical_mutagen_name = Slot(uri=ALLIANCE.chemical_mutagen_name, name="chemical_mutagen_name", curie=ALLIANCE.curie('chemical_mutagen_name'),
                   model_uri=ALLIANCE.chemical_mutagen_name, domain=GenerationMethodDTO, range=Optional[str])

slots.construct_component_dtos = Slot(uri=ALLIANCE.construct_component_dtos, name="construct_component_dtos", curie=ALLIANCE.curie('construct_component_dtos'),
                   model_uri=ALLIANCE.construct_component_dtos, domain=ConstructDTO, range=Optional[Union[Union[str, GenomicEntityDTOCurie], List[Union[str, GenomicEntityDTOCurie]]]])

slots.construct_curie = Slot(uri=ALLIANCE.construct_curie, name="construct_curie", curie=ALLIANCE.curie('construct_curie'),
                   model_uri=ALLIANCE.construct_curie, domain=None, range=str)

slots.database_status_name = Slot(uri=ALLIANCE.database_status_name, name="database_status_name", curie=ALLIANCE.curie('database_status_name'),
                   model_uri=ALLIANCE.database_status_name, domain=AlleleDatabaseStatusSlotAnnotationDTO, range=str)

slots.functional_impact_names = Slot(uri=ALLIANCE.functional_impact_names, name="functional_impact_names", curie=ALLIANCE.curie('functional_impact_names'),
                   model_uri=ALLIANCE.functional_impact_names, domain=AlleleFunctionalImpactSlotAnnotationDTO, range=Union[str, List[str]])

slots.generation_method_dto = Slot(uri=ALLIANCE.generation_method_dto, name="generation_method_dto", curie=ALLIANCE.curie('generation_method_dto'),
                   model_uri=ALLIANCE.generation_method_dto, domain=AlleleGenerationMethodAssociationDTO, range=Optional[Union[dict, GenerationMethodDTO]])

slots.germline_transmission_status_name = Slot(uri=ALLIANCE.germline_transmission_status_name, name="germline_transmission_status_name", curie=ALLIANCE.curie('germline_transmission_status_name'),
                   model_uri=ALLIANCE.germline_transmission_status_name, domain=AlleleGermlineTransmissionStatusSlotAnnotationDTO, range=str)

slots.in_collection_name = Slot(uri=ALLIANCE.in_collection_name, name="in_collection_name", curie=ALLIANCE.curie('in_collection_name'),
                   model_uri=ALLIANCE.in_collection_name, domain=AlleleDTO, range=Optional[str])

slots.inheritance_mode_name = Slot(uri=ALLIANCE.inheritance_mode_name, name="inheritance_mode_name", curie=ALLIANCE.curie('inheritance_mode_name'),
                   model_uri=ALLIANCE.inheritance_mode_name, domain=AlleleInheritanceModeSlotAnnotationDTO, range=Optional[str])

slots.integration_method_name = Slot(uri=ALLIANCE.integration_method_name, name="integration_method_name", curie=ALLIANCE.curie('integration_method_name'),
                   model_uri=ALLIANCE.integration_method_name, domain=GenerationMethodDTO, range=Optional[str])

slots.irradiation_mutagen_name = Slot(uri=ALLIANCE.irradiation_mutagen_name, name="irradiation_mutagen_name", curie=ALLIANCE.curie('irradiation_mutagen_name'),
                   model_uri=ALLIANCE.irradiation_mutagen_name, domain=GenerationMethodDTO, range=Optional[str])

slots.laboratory_of_origin_curie = Slot(uri=ALLIANCE.laboratory_of_origin_curie, name="laboratory_of_origin_curie", curie=ALLIANCE.curie('laboratory_of_origin_curie'),
                   model_uri=ALLIANCE.laboratory_of_origin_curie, domain=AlleleDTO, range=Optional[str])

slots.molecular_mutation_names = Slot(uri=ALLIANCE.molecular_mutation_names, name="molecular_mutation_names", curie=ALLIANCE.curie('molecular_mutation_names'),
                   model_uri=ALLIANCE.molecular_mutation_names, domain=AlleleMolecularMutationSlotAnnotationDTO, range=Union[str, List[str]])

slots.mutagenesis_method_names = Slot(uri=ALLIANCE.mutagenesis_method_names, name="mutagenesis_method_names", curie=ALLIANCE.curie('mutagenesis_method_names'),
                   model_uri=ALLIANCE.mutagenesis_method_names, domain=AlleleGenerationMethodAssociationDTO, range=Optional[Union[str, List[str]]])

slots.mutation_target_strain_curie = Slot(uri=ALLIANCE.mutation_target_strain_curie, name="mutation_target_strain_curie", curie=ALLIANCE.curie('mutation_target_strain_curie'),
                   model_uri=ALLIANCE.mutation_target_strain_curie, domain=AlleleGenerationMethodAssociationDTO, range=Optional[str])

slots.mutation_type_curies = Slot(uri=ALLIANCE.mutation_type_curies, name="mutation_type_curies", curie=ALLIANCE.curie('mutation_type_curies'),
                   model_uri=ALLIANCE.mutation_type_curies, domain=AlleleMutationTypeSlotAnnotationDTO, range=Optional[Union[str, List[str]]])

slots.nomenclature_event_name = Slot(uri=ALLIANCE.nomenclature_event_name, name="nomenclature_event_name", curie=ALLIANCE.curie('nomenclature_event_name'),
                   model_uri=ALLIANCE.nomenclature_event_name, domain=AlleleNomenclatureEventSlotAnnotationDTO, range=str)

slots.object_allele_curie = Slot(uri=ALLIANCE.object_allele_curie, name="object_allele_curie", curie=ALLIANCE.curie('object_allele_curie'),
                   model_uri=ALLIANCE.object_allele_curie, domain=AlleleAlleleAssociationDTO, range=Optional[str])

slots.transgene_chromosome_location_curie = Slot(uri=ALLIANCE.transgene_chromosome_location_curie, name="transgene_chromosome_location_curie", curie=ALLIANCE.curie('transgene_chromosome_location_curie'),
                   model_uri=ALLIANCE.transgene_chromosome_location_curie, domain=AlleleDTO, range=Optional[str])

slots.alliance_member_id = Slot(uri=ALLIANCE.alliance_member_id, name="alliance_member_id", curie=ALLIANCE.curie('alliance_member_id'),
                   model_uri=ALLIANCE.alliance_member_id, domain=AllianceMember, range=int)

slots.GeneToGeneAssociation_subject = Slot(uri=ALLIANCE.subject, name="GeneToGeneAssociation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.GeneToGeneAssociation_subject, domain=GeneToGeneAssociation, range=Union[str, GeneCurie])

slots.GeneToGeneAssociation_object = Slot(uri=ALLIANCE.object, name="GeneToGeneAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.GeneToGeneAssociation_object, domain=GeneToGeneAssociation, range=Union[str, GeneCurie])

slots.GeneInteraction_curie = Slot(uri=ALLIANCE.curie, name="GeneInteraction_curie", curie=ALLIANCE.curie('curie'),
                   model_uri=ALLIANCE.GeneInteraction_curie, domain=GeneInteraction, range=Union[str, GeneInteractionCurie])

slots.GeneInteraction_cross_references = Slot(uri=ALLIANCE.cross_references, name="GeneInteraction_cross_references", curie=ALLIANCE.curie('cross_references'),
                   model_uri=ALLIANCE.GeneInteraction_cross_references, domain=GeneInteraction, range=Optional[Union[Union[dict, "CrossReference"], List[Union[dict, "CrossReference"]]]])

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

slots.Allele_aberration = Slot(uri=ALLIANCE.aberration, name="Allele_aberration", curie=ALLIANCE.curie('aberration'),
                   model_uri=ALLIANCE.Allele_aberration, domain=Allele, range=Optional[str])

slots.Allele_allele_symbol = Slot(uri=ALLIANCE.allele_symbol, name="Allele_allele_symbol", curie=ALLIANCE.curie('allele_symbol'),
                   model_uri=ALLIANCE.Allele_allele_symbol, domain=Allele, range=Union[dict, "AlleleSymbolSlotAnnotation"])

slots.Allele_laboratory_of_origin = Slot(uri=ALLIANCE.laboratory_of_origin, name="Allele_laboratory_of_origin", curie=ALLIANCE.curie('laboratory_of_origin'),
                   model_uri=ALLIANCE.Allele_laboratory_of_origin, domain=Allele, range=Optional[Union[str, LaboratoryCurie]])

slots.Allele_is_extrachromosomal = Slot(uri=ALLIANCE.is_extrachromosomal, name="Allele_is_extrachromosomal", curie=ALLIANCE.curie('is_extrachromosomal'),
                   model_uri=ALLIANCE.Allele_is_extrachromosomal, domain=Allele, range=Optional[Union[bool, Bool]])

slots.Allele_is_integrated = Slot(uri=ALLIANCE.is_integrated, name="Allele_is_integrated", curie=ALLIANCE.curie('is_integrated'),
                   model_uri=ALLIANCE.Allele_is_integrated, domain=Allele, range=Optional[Union[bool, Bool]])

slots.Construct_curie = Slot(uri=ALLIANCE.curie, name="Construct_curie", curie=ALLIANCE.curie('curie'),
                   model_uri=ALLIANCE.Construct_curie, domain=Construct, range=Union[str, ConstructCurie])

slots.Construct_name = Slot(uri=ALLIANCE.name, name="Construct_name", curie=ALLIANCE.curie('name'),
                   model_uri=ALLIANCE.Construct_name, domain=Construct, range=str)

slots.ConstructComponentAssociation_predicate = Slot(uri=ALLIANCE.predicate, name="ConstructComponentAssociation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.ConstructComponentAssociation_predicate, domain=ConstructComponentAssociation, range=Union[str, VocabularyTermName])

slots.ConstructComponentAssociation_subject = Slot(uri=ALLIANCE.subject, name="ConstructComponentAssociation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.ConstructComponentAssociation_subject, domain=ConstructComponentAssociation, range=Union[str, ConstructCurie])

slots.ConstructComponentAssociation_object = Slot(uri=ALLIANCE.object, name="ConstructComponentAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.ConstructComponentAssociation_object, domain=ConstructComponentAssociation, range=Union[str, ConstructComponentCurie])

slots.SequenceTargetingReagent_curie = Slot(uri=ALLIANCE.curie, name="SequenceTargetingReagent_curie", curie=ALLIANCE.curie('curie'),
                   model_uri=ALLIANCE.SequenceTargetingReagent_curie, domain=SequenceTargetingReagent, range=Union[str, SequenceTargetingReagentCurie])

slots.SequenceTargetingReagent_name = Slot(uri=ALLIANCE.name, name="SequenceTargetingReagent_name", curie=ALLIANCE.curie('name'),
                   model_uri=ALLIANCE.SequenceTargetingReagent_name, domain=SequenceTargetingReagent, range=str)

slots.SequenceTargetingReagentToGeneAssociation_predicate = Slot(uri=ALLIANCE.predicate, name="SequenceTargetingReagentToGeneAssociation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.SequenceTargetingReagentToGeneAssociation_predicate, domain=SequenceTargetingReagentToGeneAssociation, range=Union[str, VocabularyTermName])

slots.SequenceTargetingReagentToGeneAssociation_subject = Slot(uri=ALLIANCE.subject, name="SequenceTargetingReagentToGeneAssociation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.SequenceTargetingReagentToGeneAssociation_subject, domain=SequenceTargetingReagentToGeneAssociation, range=Union[str, SequenceTargetingReagentCurie])

slots.SequenceTargetingReagentToGeneAssociation_object = Slot(uri=ALLIANCE.object, name="SequenceTargetingReagentToGeneAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.SequenceTargetingReagentToGeneAssociation_object, domain=SequenceTargetingReagentToGeneAssociation, range=Union[str, GeneCurie])

slots.AlleleDatabaseStatusSlotAnnotation_single_allele = Slot(uri=ALLIANCE.single_allele, name="AlleleDatabaseStatusSlotAnnotation_single_allele", curie=ALLIANCE.curie('single_allele'),
                   model_uri=ALLIANCE.AlleleDatabaseStatusSlotAnnotation_single_allele, domain=AlleleDatabaseStatusSlotAnnotation, range=Union[str, AlleleCurie])

slots.AlleleFullNameSlotAnnotation_single_allele = Slot(uri=ALLIANCE.single_allele, name="AlleleFullNameSlotAnnotation_single_allele", curie=ALLIANCE.curie('single_allele'),
                   model_uri=ALLIANCE.AlleleFullNameSlotAnnotation_single_allele, domain=AlleleFullNameSlotAnnotation, range=Union[str, AlleleCurie])

slots.AlleleFullNameSlotAnnotation_name_type = Slot(uri=ALLIANCE.name_type, name="AlleleFullNameSlotAnnotation_name_type", curie=ALLIANCE.curie('name_type'),
                   model_uri=ALLIANCE.AlleleFullNameSlotAnnotation_name_type, domain=AlleleFullNameSlotAnnotation, range=Union[str, VocabularyTermName])

slots.AlleleFunctionalImpactSlotAnnotation_single_allele = Slot(uri=ALLIANCE.single_allele, name="AlleleFunctionalImpactSlotAnnotation_single_allele", curie=ALLIANCE.curie('single_allele'),
                   model_uri=ALLIANCE.AlleleFunctionalImpactSlotAnnotation_single_allele, domain=AlleleFunctionalImpactSlotAnnotation, range=Union[str, AlleleCurie])

slots.AlleleFunctionalImpactSlotAnnotation_phenotype_term = Slot(uri=ALLIANCE.phenotype_term, name="AlleleFunctionalImpactSlotAnnotation_phenotype_term", curie=ALLIANCE.curie('phenotype_term'),
                   model_uri=ALLIANCE.AlleleFunctionalImpactSlotAnnotation_phenotype_term, domain=AlleleFunctionalImpactSlotAnnotation, range=Optional[Union[str, PhenotypeTermCurie]])

slots.AlleleFunctionalImpactSlotAnnotation_phenotype_statement = Slot(uri=ALLIANCE.phenotype_statement, name="AlleleFunctionalImpactSlotAnnotation_phenotype_statement", curie=ALLIANCE.curie('phenotype_statement'),
                   model_uri=ALLIANCE.AlleleFunctionalImpactSlotAnnotation_phenotype_statement, domain=AlleleFunctionalImpactSlotAnnotation, range=Optional[str])

slots.AlleleGermlineTransmissionStatusSlotAnnotation_single_allele = Slot(uri=ALLIANCE.single_allele, name="AlleleGermlineTransmissionStatusSlotAnnotation_single_allele", curie=ALLIANCE.curie('single_allele'),
                   model_uri=ALLIANCE.AlleleGermlineTransmissionStatusSlotAnnotation_single_allele, domain=AlleleGermlineTransmissionStatusSlotAnnotation, range=Union[str, AlleleCurie])

slots.AlleleInheritanceModeSlotAnnotation_single_allele = Slot(uri=ALLIANCE.single_allele, name="AlleleInheritanceModeSlotAnnotation_single_allele", curie=ALLIANCE.curie('single_allele'),
                   model_uri=ALLIANCE.AlleleInheritanceModeSlotAnnotation_single_allele, domain=AlleleInheritanceModeSlotAnnotation, range=Union[str, AlleleCurie])

slots.AlleleInheritanceModeSlotAnnotation_inheritance_mode = Slot(uri=ALLIANCE.inheritance_mode, name="AlleleInheritanceModeSlotAnnotation_inheritance_mode", curie=ALLIANCE.curie('inheritance_mode'),
                   model_uri=ALLIANCE.AlleleInheritanceModeSlotAnnotation_inheritance_mode, domain=AlleleInheritanceModeSlotAnnotation, range=Union[str, VocabularyTermName])

slots.AlleleInheritanceModeSlotAnnotation_phenotype_term = Slot(uri=ALLIANCE.phenotype_term, name="AlleleInheritanceModeSlotAnnotation_phenotype_term", curie=ALLIANCE.curie('phenotype_term'),
                   model_uri=ALLIANCE.AlleleInheritanceModeSlotAnnotation_phenotype_term, domain=AlleleInheritanceModeSlotAnnotation, range=Optional[Union[str, PhenotypeTermCurie]])

slots.AlleleInheritanceModeSlotAnnotation_phenotype_statement = Slot(uri=ALLIANCE.phenotype_statement, name="AlleleInheritanceModeSlotAnnotation_phenotype_statement", curie=ALLIANCE.curie('phenotype_statement'),
                   model_uri=ALLIANCE.AlleleInheritanceModeSlotAnnotation_phenotype_statement, domain=AlleleInheritanceModeSlotAnnotation, range=Optional[str])

slots.AlleleMolecularMutationSlotAnnotation_single_allele = Slot(uri=ALLIANCE.single_allele, name="AlleleMolecularMutationSlotAnnotation_single_allele", curie=ALLIANCE.curie('single_allele'),
                   model_uri=ALLIANCE.AlleleMolecularMutationSlotAnnotation_single_allele, domain=AlleleMolecularMutationSlotAnnotation, range=Union[str, AlleleCurie])

slots.AlleleMutationTypeSlotAnnotation_single_allele = Slot(uri=ALLIANCE.single_allele, name="AlleleMutationTypeSlotAnnotation_single_allele", curie=ALLIANCE.curie('single_allele'),
                   model_uri=ALLIANCE.AlleleMutationTypeSlotAnnotation_single_allele, domain=AlleleMutationTypeSlotAnnotation, range=Union[str, AlleleCurie])

slots.AlleleNomenclatureEventSlotAnnotation_single_allele = Slot(uri=ALLIANCE.single_allele, name="AlleleNomenclatureEventSlotAnnotation_single_allele", curie=ALLIANCE.curie('single_allele'),
                   model_uri=ALLIANCE.AlleleNomenclatureEventSlotAnnotation_single_allele, domain=AlleleNomenclatureEventSlotAnnotation, range=Union[str, AlleleCurie])

slots.AlleleNoteSlotAnnotation_single_allele = Slot(uri=ALLIANCE.single_allele, name="AlleleNoteSlotAnnotation_single_allele", curie=ALLIANCE.curie('single_allele'),
                   model_uri=ALLIANCE.AlleleNoteSlotAnnotation_single_allele, domain=AlleleNoteSlotAnnotation, range=Union[str, AlleleCurie])

slots.AlleleNoteSlotAnnotation_related_note = Slot(uri=ALLIANCE.related_note, name="AlleleNoteSlotAnnotation_related_note", curie=ALLIANCE.curie('related_note'),
                   model_uri=ALLIANCE.AlleleNoteSlotAnnotation_related_note, domain=AlleleNoteSlotAnnotation, range=Union[dict, "Note"])

slots.AlleleSecondaryIdSlotAnnotation_single_allele = Slot(uri=ALLIANCE.single_allele, name="AlleleSecondaryIdSlotAnnotation_single_allele", curie=ALLIANCE.curie('single_allele'),
                   model_uri=ALLIANCE.AlleleSecondaryIdSlotAnnotation_single_allele, domain=AlleleSecondaryIdSlotAnnotation, range=Union[str, AlleleCurie])

slots.AlleleSecondaryIdSlotAnnotation_secondary_id = Slot(uri=ALLIANCE.secondary_id, name="AlleleSecondaryIdSlotAnnotation_secondary_id", curie=ALLIANCE.curie('secondary_id'),
                   model_uri=ALLIANCE.AlleleSecondaryIdSlotAnnotation_secondary_id, domain=AlleleSecondaryIdSlotAnnotation, range=Union[str, URIorCURIE])

slots.AlleleSymbolSlotAnnotation_single_allele = Slot(uri=ALLIANCE.single_allele, name="AlleleSymbolSlotAnnotation_single_allele", curie=ALLIANCE.curie('single_allele'),
                   model_uri=ALLIANCE.AlleleSymbolSlotAnnotation_single_allele, domain=AlleleSymbolSlotAnnotation, range=Union[str, AlleleCurie])

slots.AlleleSymbolSlotAnnotation_name_type = Slot(uri=ALLIANCE.name_type, name="AlleleSymbolSlotAnnotation_name_type", curie=ALLIANCE.curie('name_type'),
                   model_uri=ALLIANCE.AlleleSymbolSlotAnnotation_name_type, domain=AlleleSymbolSlotAnnotation, range=Union[str, VocabularyTermName])

slots.AlleleSynonymSlotAnnotation_single_allele = Slot(uri=ALLIANCE.single_allele, name="AlleleSynonymSlotAnnotation_single_allele", curie=ALLIANCE.curie('single_allele'),
                   model_uri=ALLIANCE.AlleleSynonymSlotAnnotation_single_allele, domain=AlleleSynonymSlotAnnotation, range=Union[str, AlleleCurie])

slots.AlleleAlleleAssociation_predicate = Slot(uri=ALLIANCE.predicate, name="AlleleAlleleAssociation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.AlleleAlleleAssociation_predicate, domain=AlleleAlleleAssociation, range=str)

slots.AlleleAlleleAssociation_object = Slot(uri=ALLIANCE.object, name="AlleleAlleleAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.AlleleAlleleAssociation_object, domain=AlleleAlleleAssociation, range=Union[str, AlleleCurie])

slots.AlleleCellLineAssociation_subject = Slot(uri=ALLIANCE.subject, name="AlleleCellLineAssociation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.AlleleCellLineAssociation_subject, domain=AlleleCellLineAssociation, range=Union[str, AlleleCurie])

slots.AlleleCellLineAssociation_predicate = Slot(uri=ALLIANCE.predicate, name="AlleleCellLineAssociation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.AlleleCellLineAssociation_predicate, domain=AlleleCellLineAssociation, range=Union[str, VocabularyTermName])

slots.AlleleCellLineAssociation_object = Slot(uri=ALLIANCE.object, name="AlleleCellLineAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.AlleleCellLineAssociation_object, domain=AlleleCellLineAssociation, range=Union[str, CellLineCurie])

slots.AlleleConstructAssociation_subject = Slot(uri=ALLIANCE.subject, name="AlleleConstructAssociation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.AlleleConstructAssociation_subject, domain=AlleleConstructAssociation, range=Union[str, AlleleCurie])

slots.AlleleConstructAssociation_predicate = Slot(uri=ALLIANCE.predicate, name="AlleleConstructAssociation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.AlleleConstructAssociation_predicate, domain=AlleleConstructAssociation, range=Union[str, VocabularyTermName])

slots.AlleleConstructAssociation_object = Slot(uri=ALLIANCE.object, name="AlleleConstructAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.AlleleConstructAssociation_object, domain=AlleleConstructAssociation, range=Union[str, ConstructCurie])

slots.AlleleGeneAssociation_object = Slot(uri=ALLIANCE.object, name="AlleleGeneAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.AlleleGeneAssociation_object, domain=AlleleGeneAssociation, range=Union[str, GeneCurie])

slots.AlleleGenerationMethodAssociation_subject = Slot(uri=ALLIANCE.subject, name="AlleleGenerationMethodAssociation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.AlleleGenerationMethodAssociation_subject, domain=AlleleGenerationMethodAssociation, range=Union[str, AlleleCurie])

slots.AlleleGenerationMethodAssociation_predicate = Slot(uri=ALLIANCE.predicate, name="AlleleGenerationMethodAssociation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.AlleleGenerationMethodAssociation_predicate, domain=AlleleGenerationMethodAssociation, range=str)

slots.AlleleGenerationMethodAssociation_object = Slot(uri=ALLIANCE.object, name="AlleleGenerationMethodAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.AlleleGenerationMethodAssociation_object, domain=AlleleGenerationMethodAssociation, range=Union[dict, GenerationMethod])

slots.AlleleGenomicEntityAssociation_subject = Slot(uri=ALLIANCE.subject, name="AlleleGenomicEntityAssociation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.AlleleGenomicEntityAssociation_subject, domain=AlleleGenomicEntityAssociation, range=Union[str, AlleleCurie])

slots.AlleleGenomicEntityAssociation_predicate = Slot(uri=ALLIANCE.predicate, name="AlleleGenomicEntityAssociation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.AlleleGenomicEntityAssociation_predicate, domain=AlleleGenomicEntityAssociation, range=Union[str, VocabularyTermName])

slots.AlleleGenomicEntityAssociation_object = Slot(uri=ALLIANCE.object, name="AlleleGenomicEntityAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.AlleleGenomicEntityAssociation_object, domain=AlleleGenomicEntityAssociation, range=Union[str, GenomicEntityCurie])

slots.AlleleGenomicEntityAssociation_evidence = Slot(uri=ALLIANCE.evidence, name="AlleleGenomicEntityAssociation_evidence", curie=ALLIANCE.curie('evidence'),
                   model_uri=ALLIANCE.AlleleGenomicEntityAssociation_evidence, domain=AlleleGenomicEntityAssociation, range=Optional[Union[Union[str, InformationContentEntityCurie], List[Union[str, InformationContentEntityCurie]]]])

slots.AlleleImageAssociation_subject = Slot(uri=ALLIANCE.subject, name="AlleleImageAssociation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.AlleleImageAssociation_subject, domain=AlleleImageAssociation, range=Union[str, AlleleCurie])

slots.AlleleImageAssociation_predicate = Slot(uri=ALLIANCE.predicate, name="AlleleImageAssociation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.AlleleImageAssociation_predicate, domain=AlleleImageAssociation, range=Union[str, VocabularyTermName])

slots.AlleleImageAssociation_object = Slot(uri=ALLIANCE.object, name="AlleleImageAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.AlleleImageAssociation_object, domain=AlleleImageAssociation, range=Union[str, ImageCurie])

slots.AlleleImageAssociation_primary_image = Slot(uri=ALLIANCE.primary_image, name="AlleleImageAssociation_primary_image", curie=ALLIANCE.curie('primary_image'),
                   model_uri=ALLIANCE.AlleleImageAssociation_primary_image, domain=AlleleImageAssociation, range=Optional[Union[bool, Bool]])

slots.AlleleOriginAssociation_subject = Slot(uri=ALLIANCE.subject, name="AlleleOriginAssociation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.AlleleOriginAssociation_subject, domain=AlleleOriginAssociation, range=Union[str, AlleleCurie])

slots.AlleleOriginAssociation_object = Slot(uri=ALLIANCE.object, name="AlleleOriginAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.AlleleOriginAssociation_object, domain=AlleleOriginAssociation, range=Union[str, AffectedGenomicModelCurie])

slots.AlleleProteinAssociation_object = Slot(uri=ALLIANCE.object, name="AlleleProteinAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.AlleleProteinAssociation_object, domain=AlleleProteinAssociation, range=Union[str, ProteinCurie])

slots.AlleleTranscriptAssociation_object = Slot(uri=ALLIANCE.object, name="AlleleTranscriptAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.AlleleTranscriptAssociation_object, domain=AlleleTranscriptAssociation, range=Union[str, TranscriptCurie])

slots.AlleleVariantAssociation_subject = Slot(uri=ALLIANCE.subject, name="AlleleVariantAssociation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.AlleleVariantAssociation_subject, domain=AlleleVariantAssociation, range=Union[str, AlleleCurie])

slots.AlleleVariantAssociation_object = Slot(uri=ALLIANCE.object, name="AlleleVariantAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.AlleleVariantAssociation_object, domain=AlleleVariantAssociation, range=Union[str, VariantCurie])

slots.BiologicalEntity_taxon = Slot(uri=ALLIANCE.taxon, name="BiologicalEntity_taxon", curie=ALLIANCE.curie('taxon'),
                   model_uri=ALLIANCE.BiologicalEntity_taxon, domain=BiologicalEntity, range=Union[str, NCBITaxonTermCurie])

slots.BiologicalEntity_curie = Slot(uri=ALLIANCE.curie, name="BiologicalEntity_curie", curie=ALLIANCE.curie('curie'),
                   model_uri=ALLIANCE.BiologicalEntity_curie, domain=BiologicalEntity, range=Union[str, BiologicalEntityCurie])

slots.BiologicalEntityDTO_taxon_curie = Slot(uri=ALLIANCE.taxon_curie, name="BiologicalEntityDTO_taxon_curie", curie=ALLIANCE.curie('taxon_curie'),
                   model_uri=ALLIANCE.BiologicalEntityDTO_taxon_curie, domain=BiologicalEntityDTO, range=str)

slots.BiologicalEntityDTO_curie = Slot(uri=ALLIANCE.curie, name="BiologicalEntityDTO_curie", curie=ALLIANCE.curie('curie'),
                   model_uri=ALLIANCE.BiologicalEntityDTO_curie, domain=BiologicalEntityDTO, range=Union[str, BiologicalEntityDTOCurie])

slots.CrossReferenceDTO_prefix = Slot(uri=ALLIANCE.prefix, name="CrossReferenceDTO_prefix", curie=ALLIANCE.curie('prefix'),
                   model_uri=ALLIANCE.CrossReferenceDTO_prefix, domain=CrossReferenceDTO, range=str)

slots.Note_free_text = Slot(uri=ALLIANCE.free_text, name="Note_free_text", curie=ALLIANCE.curie('free_text'),
                   model_uri=ALLIANCE.Note_free_text, domain=Note, range=str)

slots.Note_note_type = Slot(uri=ALLIANCE.note_type, name="Note_note_type", curie=ALLIANCE.curie('note_type'),
                   model_uri=ALLIANCE.Note_note_type, domain=Note, range=Union[str, VocabularyTermName])

slots.NoteDTO_free_text = Slot(uri=ALLIANCE.free_text, name="NoteDTO_free_text", curie=ALLIANCE.curie('free_text'),
                   model_uri=ALLIANCE.NoteDTO_free_text, domain=NoteDTO, range=str)

slots.NoteDTO_note_type_name = Slot(uri=ALLIANCE.note_type_name, name="NoteDTO_note_type_name", curie=ALLIANCE.curie('note_type_name'),
                   model_uri=ALLIANCE.NoteDTO_note_type_name, domain=NoteDTO, range=str)

slots.SymbolSlotAnnotationDTO_name_type_name = Slot(uri=ALLIANCE.name_type_name, name="SymbolSlotAnnotationDTO_name_type_name", curie=ALLIANCE.curie('name_type_name'),
                   model_uri=ALLIANCE.SymbolSlotAnnotationDTO_name_type_name, domain=SymbolSlotAnnotationDTO, range=str)

slots.FullNameSlotAnnotationDTO_name_type_name = Slot(uri=ALLIANCE.name_type_name, name="FullNameSlotAnnotationDTO_name_type_name", curie=ALLIANCE.curie('name_type_name'),
                   model_uri=ALLIANCE.FullNameSlotAnnotationDTO_name_type_name, domain=FullNameSlotAnnotationDTO, range=str)

slots.SystematicNameSlotAnnotationDTO_name_type_name = Slot(uri=ALLIANCE.name_type_name, name="SystematicNameSlotAnnotationDTO_name_type_name", curie=ALLIANCE.curie('name_type_name'),
                   model_uri=ALLIANCE.SystematicNameSlotAnnotationDTO_name_type_name, domain=SystematicNameSlotAnnotationDTO, range=str)

slots.Association_subject = Slot(uri=ALLIANCE.subject, name="Association_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.Association_subject, domain=Association, range=str)

slots.Association_predicate = Slot(uri=ALLIANCE.predicate, name="Association_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.Association_predicate, domain=Association, range=str)

slots.Association_object = Slot(uri=ALLIANCE.object, name="Association_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.Association_object, domain=Association, range=str)

slots.Chromosome_curie = Slot(uri=ALLIANCE.curie, name="Chromosome_curie", curie=ALLIANCE.curie('curie'),
                   model_uri=ALLIANCE.Chromosome_curie, domain=Chromosome, range=Union[str, ChromosomeCurie])

slots.Assembly_curie = Slot(uri=ALLIANCE.curie, name="Assembly_curie", curie=ALLIANCE.curie('curie'),
                   model_uri=ALLIANCE.Assembly_curie, domain=Assembly, range=Union[str, AssemblyCurie])

slots.GenomicLocationAssociation_subject = Slot(uri=ALLIANCE.subject, name="GenomicLocationAssociation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.GenomicLocationAssociation_subject, domain=GenomicLocationAssociation, range=Union[str, GenomicEntityCurie])

slots.GenomicLocationAssociation_object = Slot(uri=ALLIANCE.object, name="GenomicLocationAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.GenomicLocationAssociation_object, domain=GenomicLocationAssociation, range=Union[str, ChromosomeCurie])

slots.GenomicLocationAssociation_predicate = Slot(uri=ALLIANCE.predicate, name="GenomicLocationAssociation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.GenomicLocationAssociation_predicate, domain=GenomicLocationAssociation, range=str)

slots.GenomicLocationAssociationDTO_genomic_entity_curie = Slot(uri=ALLIANCE.genomic_entity_curie, name="GenomicLocationAssociationDTO_genomic_entity_curie", curie=ALLIANCE.curie('genomic_entity_curie'),
                   model_uri=ALLIANCE.GenomicLocationAssociationDTO_genomic_entity_curie, domain=GenomicLocationAssociationDTO, range=str)

slots.GenomicLocationAssociationDTO_predicate_name = Slot(uri=ALLIANCE.predicate_name, name="GenomicLocationAssociationDTO_predicate_name", curie=ALLIANCE.curie('predicate_name'),
                   model_uri=ALLIANCE.GenomicLocationAssociationDTO_predicate_name, domain=GenomicLocationAssociationDTO, range=str)

slots.GenomicLocationAssociationDTO_chromosome_curie = Slot(uri=ALLIANCE.chromosome_curie, name="GenomicLocationAssociationDTO_chromosome_curie", curie=ALLIANCE.curie('chromosome_curie'),
                   model_uri=ALLIANCE.GenomicLocationAssociationDTO_chromosome_curie, domain=GenomicLocationAssociationDTO, range=str)

slots.GenomicLocationAssociationDTO_assembly_curie = Slot(uri=ALLIANCE.assembly_curie, name="GenomicLocationAssociationDTO_assembly_curie", curie=ALLIANCE.curie('assembly_curie'),
                   model_uri=ALLIANCE.GenomicLocationAssociationDTO_assembly_curie, domain=GenomicLocationAssociationDTO, range=str)

slots.GenomicLocationAssociationDTO_start = Slot(uri=ALLIANCE.start, name="GenomicLocationAssociationDTO_start", curie=ALLIANCE.curie('start'),
                   model_uri=ALLIANCE.GenomicLocationAssociationDTO_start, domain=GenomicLocationAssociationDTO, range=int)

slots.GenomicLocationAssociationDTO_end = Slot(uri=ALLIANCE.end, name="GenomicLocationAssociationDTO_end", curie=ALLIANCE.curie('end'),
                   model_uri=ALLIANCE.GenomicLocationAssociationDTO_end, domain=GenomicLocationAssociationDTO, range=int)

slots.Gene_related_notes = Slot(uri=ALLIANCE.related_notes, name="Gene_related_notes", curie=ALLIANCE.curie('related_notes'),
                   model_uri=ALLIANCE.Gene_related_notes, domain=Gene, range=Optional[Union[Union[dict, Note], List[Union[dict, Note]]]])

slots.GeneSymbolSlotAnnotation_single_gene = Slot(uri=ALLIANCE.single_gene, name="GeneSymbolSlotAnnotation_single_gene", curie=ALLIANCE.curie('single_gene'),
                   model_uri=ALLIANCE.GeneSymbolSlotAnnotation_single_gene, domain=GeneSymbolSlotAnnotation, range=Union[str, GeneCurie])

slots.GeneSymbolSlotAnnotation_name_type = Slot(uri=ALLIANCE.name_type, name="GeneSymbolSlotAnnotation_name_type", curie=ALLIANCE.curie('name_type'),
                   model_uri=ALLIANCE.GeneSymbolSlotAnnotation_name_type, domain=GeneSymbolSlotAnnotation, range=Union[str, VocabularyTermName])

slots.GeneFullNameSlotAnnotation_single_gene = Slot(uri=ALLIANCE.single_gene, name="GeneFullNameSlotAnnotation_single_gene", curie=ALLIANCE.curie('single_gene'),
                   model_uri=ALLIANCE.GeneFullNameSlotAnnotation_single_gene, domain=GeneFullNameSlotAnnotation, range=Union[str, GeneCurie])

slots.GeneFullNameSlotAnnotation_name_type = Slot(uri=ALLIANCE.name_type, name="GeneFullNameSlotAnnotation_name_type", curie=ALLIANCE.curie('name_type'),
                   model_uri=ALLIANCE.GeneFullNameSlotAnnotation_name_type, domain=GeneFullNameSlotAnnotation, range=Union[str, VocabularyTermName])

slots.GeneSystematicNameSlotAnnotation_single_gene = Slot(uri=ALLIANCE.single_gene, name="GeneSystematicNameSlotAnnotation_single_gene", curie=ALLIANCE.curie('single_gene'),
                   model_uri=ALLIANCE.GeneSystematicNameSlotAnnotation_single_gene, domain=GeneSystematicNameSlotAnnotation, range=Union[str, GeneCurie])

slots.GeneSystematicNameSlotAnnotation_name_type = Slot(uri=ALLIANCE.name_type, name="GeneSystematicNameSlotAnnotation_name_type", curie=ALLIANCE.curie('name_type'),
                   model_uri=ALLIANCE.GeneSystematicNameSlotAnnotation_name_type, domain=GeneSystematicNameSlotAnnotation, range=Union[str, VocabularyTermName])

slots.GeneSynonymSlotAnnotation_single_gene = Slot(uri=ALLIANCE.single_gene, name="GeneSynonymSlotAnnotation_single_gene", curie=ALLIANCE.curie('single_gene'),
                   model_uri=ALLIANCE.GeneSynonymSlotAnnotation_single_gene, domain=GeneSynonymSlotAnnotation, range=Union[str, GeneCurie])

slots.Reference_reference_id = Slot(uri=ALLIANCE.reference_id, name="Reference_reference_id", curie=ALLIANCE.curie('reference_id'),
                   model_uri=ALLIANCE.Reference_reference_id, domain=Reference, range=int)

slots.MeshDetail_reference_id = Slot(uri=ALLIANCE.reference_id, name="MeshDetail_reference_id", curie=ALLIANCE.curie('reference_id'),
                   model_uri=ALLIANCE.MeshDetail_reference_id, domain=MeshDetail, range=int)

slots.Person_unique_id = Slot(uri=ALLIANCE.unique_id, name="Person_unique_id", curie=ALLIANCE.curie('unique_id'),
                   model_uri=ALLIANCE.Person_unique_id, domain=Person, range=Union[str, PersonUniqueId])

slots.LoggedInPerson_okta_id = Slot(uri=ALLIANCE.okta_id, name="LoggedInPerson_okta_id", curie=ALLIANCE.curie('okta_id'),
                   model_uri=ALLIANCE.LoggedInPerson_okta_id, domain=LoggedInPerson, range=str)

slots.LoggedInPerson_okta_email = Slot(uri=ALLIANCE.okta_email, name="LoggedInPerson_okta_email", curie=ALLIANCE.curie('okta_email'),
                   model_uri=ALLIANCE.LoggedInPerson_okta_email, domain=LoggedInPerson, range=str)

slots.Figure_single_reference = Slot(uri=ALLIANCE.single_reference, name="Figure_single_reference", curie=ALLIANCE.curie('single_reference'),
                   model_uri=ALLIANCE.Figure_single_reference, domain=Figure, range=Union[str, ReferenceCurie])

slots.Image_associated_with_figure = Slot(uri=ALLIANCE.associated_with_figure, name="Image_associated_with_figure", curie=ALLIANCE.curie('associated_with_figure'),
                   model_uri=ALLIANCE.Image_associated_with_figure, domain=Image, range=Union[str, FigureCurie])

slots.Image_image_x_origin = Slot(uri=ALLIANCE.image_x_origin, name="Image_image_x_origin", curie=ALLIANCE.curie('image_x_origin'),
                   model_uri=ALLIANCE.Image_image_x_origin, domain=Image, range=Optional[int])

slots.Image_image_y_origin = Slot(uri=ALLIANCE.image_y_origin, name="Image_image_y_origin", curie=ALLIANCE.curie('image_y_origin'),
                   model_uri=ALLIANCE.Image_image_y_origin, domain=Image, range=Optional[int])

slots.ImagePane_from_image = Slot(uri=ALLIANCE.from_image, name="ImagePane_from_image", curie=ALLIANCE.curie('from_image'),
                   model_uri=ALLIANCE.ImagePane_from_image, domain=ImagePane, range=Union[str, ImageCurie])

slots.ImagePane_image_x_origin = Slot(uri=ALLIANCE.image_x_origin, name="ImagePane_image_x_origin", curie=ALLIANCE.curie('image_x_origin'),
                   model_uri=ALLIANCE.ImagePane_image_x_origin, domain=ImagePane, range=Optional[int])

slots.ImagePane_image_y_origin = Slot(uri=ALLIANCE.image_y_origin, name="ImagePane_image_y_origin", curie=ALLIANCE.curie('image_y_origin'),
                   model_uri=ALLIANCE.ImagePane_image_y_origin, domain=ImagePane, range=Optional[int])

slots.VocabularyTerm_name = Slot(uri=ALLIANCE.name, name="VocabularyTerm_name", curie=ALLIANCE.curie('name'),
                   model_uri=ALLIANCE.VocabularyTerm_name, domain=VocabularyTerm, range=Union[str, VocabularyTermName])

slots.Vocabulary_name = Slot(uri=ALLIANCE.name, name="Vocabulary_name", curie=ALLIANCE.curie('name'),
                   model_uri=ALLIANCE.Vocabulary_name, domain=Vocabulary, range=Union[str, VocabularyName])

slots.VocabularyTermSet_name = Slot(uri=ALLIANCE.name, name="VocabularyTermSet_name", curie=ALLIANCE.curie('name'),
                   model_uri=ALLIANCE.VocabularyTermSet_name, domain=VocabularyTermSet, range=Union[str, VocabularyTermSetName])

slots.SourceVariantLocation_single_reference = Slot(uri=ALLIANCE.single_reference, name="SourceVariantLocation_single_reference", curie=ALLIANCE.curie('single_reference'),
                   model_uri=ALLIANCE.SourceVariantLocation_single_reference, domain=SourceVariantLocation, range=Union[str, ReferenceCurie])

slots.VariantLocation_evidence_code = Slot(uri=ALLIANCE.evidence_code, name="VariantLocation_evidence_code", curie=ALLIANCE.curie('evidence_code'),
                   model_uri=ALLIANCE.VariantLocation_evidence_code, domain=VariantLocation, range=Optional[Union[str, ECOTermCurie]])

slots.OntologyTerm_definition = Slot(uri=ALLIANCE.definition, name="OntologyTerm_definition", curie=ALLIANCE.curie('definition'),
                   model_uri=ALLIANCE.OntologyTerm_definition, domain=OntologyTerm, range=Optional[str])

slots.OntologyTerm_curie = Slot(uri=ALLIANCE.curie, name="OntologyTerm_curie", curie=ALLIANCE.curie('curie'),
                   model_uri=ALLIANCE.OntologyTerm_curie, domain=OntologyTerm, range=Union[str, OntologyTermCurie])

slots.OntologyTermClosure_subject = Slot(uri=ALLIANCE.subject, name="OntologyTermClosure_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.OntologyTermClosure_subject, domain=OntologyTermClosure, range=Union[str, OntologyTermCurie])

slots.OntologyTermClosure_object = Slot(uri=ALLIANCE.object, name="OntologyTermClosure_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.OntologyTermClosure_object, domain=OntologyTermClosure, range=Union[str, OntologyTermCurie])

slots.OntologyTermClosure_distance_between = Slot(uri=ALLIANCE.distance_between, name="OntologyTermClosure_distance_between", curie=ALLIANCE.curie('distance_between'),
                   model_uri=ALLIANCE.OntologyTermClosure_distance_between, domain=OntologyTermClosure, range=Optional[int])

slots.ECOTerm_abbreviation = Slot(uri=ALLIANCE.abbreviation, name="ECOTerm_abbreviation", curie=ALLIANCE.curie('abbreviation'),
                   model_uri=ALLIANCE.ECOTerm_abbreviation, domain=ECOTerm, range=Optional[str])

slots.PhenotypeAnnotation_subject = Slot(uri=ALLIANCE.subject, name="PhenotypeAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.PhenotypeAnnotation_subject, domain=PhenotypeAnnotation, range=Union[str, BiologicalEntityCurie])

slots.PhenotypeAnnotation_phenotype_term = Slot(uri=ALLIANCE.phenotype_term, name="PhenotypeAnnotation_phenotype_term", curie=ALLIANCE.curie('phenotype_term'),
                   model_uri=ALLIANCE.PhenotypeAnnotation_phenotype_term, domain=PhenotypeAnnotation, range=Optional[Union[str, PhenotypeTermCurie]])

slots.PhenotypeAnnotation_object = Slot(uri=ALLIANCE.object, name="PhenotypeAnnotation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.PhenotypeAnnotation_object, domain=PhenotypeAnnotation, range=str)

slots.PhenotypeAnnotation_single_reference = Slot(uri=ALLIANCE.single_reference, name="PhenotypeAnnotation_single_reference", curie=ALLIANCE.curie('single_reference'),
                   model_uri=ALLIANCE.PhenotypeAnnotation_single_reference, domain=PhenotypeAnnotation, range=Optional[Union[str, ReferenceCurie]])

slots.PhenotypeAnnotation_date_created = Slot(uri=ALLIANCE.date_created, name="PhenotypeAnnotation_date_created", curie=ALLIANCE.curie('date_created'),
                   model_uri=ALLIANCE.PhenotypeAnnotation_date_created, domain=PhenotypeAnnotation, range=Union[str, XSDDateTime])

slots.GenePhenotypeAnnotation_subject = Slot(uri=ALLIANCE.subject, name="GenePhenotypeAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.GenePhenotypeAnnotation_subject, domain=GenePhenotypeAnnotation, range=Union[str, GeneCurie])

slots.AllelePhenotypeAnnotation_subject = Slot(uri=ALLIANCE.subject, name="AllelePhenotypeAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.AllelePhenotypeAnnotation_subject, domain=AllelePhenotypeAnnotation, range=Union[str, AlleleCurie])

slots.AllelePhenotypeAnnotation_inferred_gene = Slot(uri=ALLIANCE.inferred_gene, name="AllelePhenotypeAnnotation_inferred_gene", curie=ALLIANCE.curie('inferred_gene'),
                   model_uri=ALLIANCE.AllelePhenotypeAnnotation_inferred_gene, domain=AllelePhenotypeAnnotation, range=Optional[Union[str, GeneCurie]])

slots.AllelePhenotypeAnnotation_asserted_genes = Slot(uri=ALLIANCE.asserted_genes, name="AllelePhenotypeAnnotation_asserted_genes", curie=ALLIANCE.curie('asserted_genes'),
                   model_uri=ALLIANCE.AllelePhenotypeAnnotation_asserted_genes, domain=AllelePhenotypeAnnotation, range=Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]])

slots.AllelePhenotypeAnnotation_asserted_allele = Slot(uri=ALLIANCE.asserted_allele, name="AllelePhenotypeAnnotation_asserted_allele", curie=ALLIANCE.curie('asserted_allele'),
                   model_uri=ALLIANCE.AllelePhenotypeAnnotation_asserted_allele, domain=AllelePhenotypeAnnotation, range=Optional[Union[str, AlleleCurie]])

slots.AGMPhenotypeAnnotation_subject = Slot(uri=ALLIANCE.subject, name="AGMPhenotypeAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.AGMPhenotypeAnnotation_subject, domain=AGMPhenotypeAnnotation, range=Union[str, AffectedGenomicModelCurie])

slots.AGMPhenotypeAnnotation_inferred_gene = Slot(uri=ALLIANCE.inferred_gene, name="AGMPhenotypeAnnotation_inferred_gene", curie=ALLIANCE.curie('inferred_gene'),
                   model_uri=ALLIANCE.AGMPhenotypeAnnotation_inferred_gene, domain=AGMPhenotypeAnnotation, range=Optional[Union[str, GeneCurie]])

slots.AGMPhenotypeAnnotation_inferred_allele = Slot(uri=ALLIANCE.inferred_allele, name="AGMPhenotypeAnnotation_inferred_allele", curie=ALLIANCE.curie('inferred_allele'),
                   model_uri=ALLIANCE.AGMPhenotypeAnnotation_inferred_allele, domain=AGMPhenotypeAnnotation, range=Optional[Union[str, AlleleCurie]])

slots.AGMPhenotypeAnnotation_asserted_genes = Slot(uri=ALLIANCE.asserted_genes, name="AGMPhenotypeAnnotation_asserted_genes", curie=ALLIANCE.curie('asserted_genes'),
                   model_uri=ALLIANCE.AGMPhenotypeAnnotation_asserted_genes, domain=AGMPhenotypeAnnotation, range=Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]])

slots.AGMPhenotypeAnnotation_asserted_allele = Slot(uri=ALLIANCE.asserted_allele, name="AGMPhenotypeAnnotation_asserted_allele", curie=ALLIANCE.curie('asserted_allele'),
                   model_uri=ALLIANCE.AGMPhenotypeAnnotation_asserted_allele, domain=AGMPhenotypeAnnotation, range=Optional[Union[str, AlleleCurie]])

slots.DiseaseAnnotation_curie = Slot(uri=ALLIANCE.curie, name="DiseaseAnnotation_curie", curie=ALLIANCE.curie('curie'),
                   model_uri=ALLIANCE.DiseaseAnnotation_curie, domain=DiseaseAnnotation, range=Union[str, DiseaseAnnotationCurie])

slots.DiseaseAnnotation_unique_id = Slot(uri=ALLIANCE.unique_id, name="DiseaseAnnotation_unique_id", curie=ALLIANCE.curie('unique_id'),
                   model_uri=ALLIANCE.DiseaseAnnotation_unique_id, domain=DiseaseAnnotation, range=Optional[str])

slots.DiseaseAnnotation_mod_entity_id = Slot(uri=ALLIANCE.mod_entity_id, name="DiseaseAnnotation_mod_entity_id", curie=ALLIANCE.curie('mod_entity_id'),
                   model_uri=ALLIANCE.DiseaseAnnotation_mod_entity_id, domain=DiseaseAnnotation, range=Optional[str])

slots.DiseaseAnnotation_subject = Slot(uri=ALLIANCE.subject, name="DiseaseAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.DiseaseAnnotation_subject, domain=DiseaseAnnotation, range=Union[str, BiologicalEntityCurie])

slots.DiseaseAnnotation_predicate = Slot(uri=ALLIANCE.predicate, name="DiseaseAnnotation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.DiseaseAnnotation_predicate, domain=DiseaseAnnotation, range=str)

slots.DiseaseAnnotation_negated = Slot(uri=ALLIANCE.negated, name="DiseaseAnnotation_negated", curie=ALLIANCE.curie('negated'),
                   model_uri=ALLIANCE.DiseaseAnnotation_negated, domain=DiseaseAnnotation, range=Optional[Union[bool, Bool]])

slots.DiseaseAnnotation_object = Slot(uri=ALLIANCE.object, name="DiseaseAnnotation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.DiseaseAnnotation_object, domain=DiseaseAnnotation, range=Union[str, DOTermCurie])

slots.DiseaseAnnotation_data_provider = Slot(uri=ALLIANCE.data_provider, name="DiseaseAnnotation_data_provider", curie=ALLIANCE.curie('data_provider'),
                   model_uri=ALLIANCE.DiseaseAnnotation_data_provider, domain=DiseaseAnnotation, range=Union[dict, DataProvider])

slots.DiseaseAnnotation_annotation_type = Slot(uri=ALLIANCE.annotation_type, name="DiseaseAnnotation_annotation_type", curie=ALLIANCE.curie('annotation_type'),
                   model_uri=ALLIANCE.DiseaseAnnotation_annotation_type, domain=DiseaseAnnotation, range=Optional[Union[str, VocabularyTermName]])

slots.DiseaseAnnotation_with_or_from = Slot(uri=ALLIANCE.with_or_from, name="DiseaseAnnotation_with_or_from", curie=ALLIANCE.curie('with_or_from'),
                   model_uri=ALLIANCE.DiseaseAnnotation_with_or_from, domain=DiseaseAnnotation, range=Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]])

slots.DiseaseAnnotation_single_reference = Slot(uri=ALLIANCE.single_reference, name="DiseaseAnnotation_single_reference", curie=ALLIANCE.curie('single_reference'),
                   model_uri=ALLIANCE.DiseaseAnnotation_single_reference, domain=DiseaseAnnotation, range=Union[str, ReferenceCurie])

slots.DiseaseAnnotation_evidence_codes = Slot(uri=ALLIANCE.evidence_codes, name="DiseaseAnnotation_evidence_codes", curie=ALLIANCE.curie('evidence_codes'),
                   model_uri=ALLIANCE.DiseaseAnnotation_evidence_codes, domain=DiseaseAnnotation, range=Union[Union[str, ECOTermCurie], List[Union[str, ECOTermCurie]]])

slots.DiseaseAnnotation_genetic_sex = Slot(uri=ALLIANCE.genetic_sex, name="DiseaseAnnotation_genetic_sex", curie=ALLIANCE.curie('genetic_sex'),
                   model_uri=ALLIANCE.DiseaseAnnotation_genetic_sex, domain=DiseaseAnnotation, range=Optional[Union[str, VocabularyTermName]])

slots.DiseaseAnnotation_related_notes = Slot(uri=ALLIANCE.related_notes, name="DiseaseAnnotation_related_notes", curie=ALLIANCE.curie('related_notes'),
                   model_uri=ALLIANCE.DiseaseAnnotation_related_notes, domain=DiseaseAnnotation, range=Optional[Union[Union[dict, Note], List[Union[dict, Note]]]])

slots.DiseaseAnnotationDTO_data_provider_dto = Slot(uri=ALLIANCE.data_provider_dto, name="DiseaseAnnotationDTO_data_provider_dto", curie=ALLIANCE.curie('data_provider_dto'),
                   model_uri=ALLIANCE.DiseaseAnnotationDTO_data_provider_dto, domain=DiseaseAnnotationDTO, range=Union[dict, DataProviderDTO])

slots.GeneDiseaseAnnotation_subject = Slot(uri=ALLIANCE.subject, name="GeneDiseaseAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.GeneDiseaseAnnotation_subject, domain=GeneDiseaseAnnotation, range=Union[str, GeneCurie])

slots.GeneDiseaseAnnotation_predicate = Slot(uri=ALLIANCE.predicate, name="GeneDiseaseAnnotation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.GeneDiseaseAnnotation_predicate, domain=GeneDiseaseAnnotation, range=Union[str, VocabularyTermName])

slots.AlleleDiseaseAnnotation_subject = Slot(uri=ALLIANCE.subject, name="AlleleDiseaseAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.AlleleDiseaseAnnotation_subject, domain=AlleleDiseaseAnnotation, range=Union[str, AlleleCurie])

slots.AlleleDiseaseAnnotation_predicate = Slot(uri=ALLIANCE.predicate, name="AlleleDiseaseAnnotation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.AlleleDiseaseAnnotation_predicate, domain=AlleleDiseaseAnnotation, range=Union[str, VocabularyTermName])

slots.AlleleDiseaseAnnotation_inferred_gene = Slot(uri=ALLIANCE.inferred_gene, name="AlleleDiseaseAnnotation_inferred_gene", curie=ALLIANCE.curie('inferred_gene'),
                   model_uri=ALLIANCE.AlleleDiseaseAnnotation_inferred_gene, domain=AlleleDiseaseAnnotation, range=Optional[Union[str, GeneCurie]])

slots.AlleleDiseaseAnnotation_asserted_genes = Slot(uri=ALLIANCE.asserted_genes, name="AlleleDiseaseAnnotation_asserted_genes", curie=ALLIANCE.curie('asserted_genes'),
                   model_uri=ALLIANCE.AlleleDiseaseAnnotation_asserted_genes, domain=AlleleDiseaseAnnotation, range=Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]])

slots.AGMDiseaseAnnotation_subject = Slot(uri=ALLIANCE.subject, name="AGMDiseaseAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.AGMDiseaseAnnotation_subject, domain=AGMDiseaseAnnotation, range=Union[str, AffectedGenomicModelCurie])

slots.AGMDiseaseAnnotation_predicate = Slot(uri=ALLIANCE.predicate, name="AGMDiseaseAnnotation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.AGMDiseaseAnnotation_predicate, domain=AGMDiseaseAnnotation, range=Union[str, VocabularyTermName])

slots.AGMDiseaseAnnotation_inferred_gene = Slot(uri=ALLIANCE.inferred_gene, name="AGMDiseaseAnnotation_inferred_gene", curie=ALLIANCE.curie('inferred_gene'),
                   model_uri=ALLIANCE.AGMDiseaseAnnotation_inferred_gene, domain=AGMDiseaseAnnotation, range=Optional[Union[str, GeneCurie]])

slots.AGMDiseaseAnnotation_inferred_allele = Slot(uri=ALLIANCE.inferred_allele, name="AGMDiseaseAnnotation_inferred_allele", curie=ALLIANCE.curie('inferred_allele'),
                   model_uri=ALLIANCE.AGMDiseaseAnnotation_inferred_allele, domain=AGMDiseaseAnnotation, range=Optional[Union[str, AlleleCurie]])

slots.AGMDiseaseAnnotation_asserted_genes = Slot(uri=ALLIANCE.asserted_genes, name="AGMDiseaseAnnotation_asserted_genes", curie=ALLIANCE.curie('asserted_genes'),
                   model_uri=ALLIANCE.AGMDiseaseAnnotation_asserted_genes, domain=AGMDiseaseAnnotation, range=Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]])

slots.AGMDiseaseAnnotation_asserted_allele = Slot(uri=ALLIANCE.asserted_allele, name="AGMDiseaseAnnotation_asserted_allele", curie=ALLIANCE.curie('asserted_allele'),
                   model_uri=ALLIANCE.AGMDiseaseAnnotation_asserted_allele, domain=AGMDiseaseAnnotation, range=Optional[Union[str, AlleleCurie]])

slots.ExperimentalCondition_unique_id = Slot(uri=ALLIANCE.unique_id, name="ExperimentalCondition_unique_id", curie=ALLIANCE.curie('unique_id'),
                   model_uri=ALLIANCE.ExperimentalCondition_unique_id, domain=ExperimentalCondition, range=Optional[str])

slots.ExperimentalCondition_condition_class = Slot(uri=ALLIANCE.condition_class, name="ExperimentalCondition_condition_class", curie=ALLIANCE.curie('condition_class'),
                   model_uri=ALLIANCE.ExperimentalCondition_condition_class, domain=ExperimentalCondition, range=Union[str, ZECOTermCurie])

slots.ExperimentalCondition_condition_summary = Slot(uri=ALLIANCE.condition_summary, name="ExperimentalCondition_condition_summary", curie=ALLIANCE.curie('condition_summary'),
                   model_uri=ALLIANCE.ExperimentalCondition_condition_summary, domain=ExperimentalCondition, range=Optional[str])

slots.ExperimentalCondition_condition_id = Slot(uri=ALLIANCE.condition_id, name="ExperimentalCondition_condition_id", curie=ALLIANCE.curie('condition_id'),
                   model_uri=ALLIANCE.ExperimentalCondition_condition_id, domain=ExperimentalCondition, range=Optional[Union[str, ExperimentalConditionOntologyTermCurie]])

slots.ExperimentalCondition_condition_quantity = Slot(uri=ALLIANCE.condition_quantity, name="ExperimentalCondition_condition_quantity", curie=ALLIANCE.curie('condition_quantity'),
                   model_uri=ALLIANCE.ExperimentalCondition_condition_quantity, domain=ExperimentalCondition, range=Optional[str])

slots.ExperimentalCondition_condition_anatomy = Slot(uri=ALLIANCE.condition_anatomy, name="ExperimentalCondition_condition_anatomy", curie=ALLIANCE.curie('condition_anatomy'),
                   model_uri=ALLIANCE.ExperimentalCondition_condition_anatomy, domain=ExperimentalCondition, range=Optional[Union[str, AnatomicalTermCurie]])

slots.ExperimentalCondition_condition_gene_ontology = Slot(uri=ALLIANCE.condition_gene_ontology, name="ExperimentalCondition_condition_gene_ontology", curie=ALLIANCE.curie('condition_gene_ontology'),
                   model_uri=ALLIANCE.ExperimentalCondition_condition_gene_ontology, domain=ExperimentalCondition, range=Optional[Union[str, GOTermCurie]])

slots.ExperimentalCondition_condition_taxon = Slot(uri=ALLIANCE.condition_taxon, name="ExperimentalCondition_condition_taxon", curie=ALLIANCE.curie('condition_taxon'),
                   model_uri=ALLIANCE.ExperimentalCondition_condition_taxon, domain=ExperimentalCondition, range=Optional[Union[str, NCBITaxonTermCurie]])

slots.ExperimentalCondition_condition_chemical = Slot(uri=ALLIANCE.condition_chemical, name="ExperimentalCondition_condition_chemical", curie=ALLIANCE.curie('condition_chemical'),
                   model_uri=ALLIANCE.ExperimentalCondition_condition_chemical, domain=ExperimentalCondition, range=Optional[Union[str, ChemicalTermCurie]])

slots.ConditionRelation_unique_id = Slot(uri=ALLIANCE.unique_id, name="ConditionRelation_unique_id", curie=ALLIANCE.curie('unique_id'),
                   model_uri=ALLIANCE.ConditionRelation_unique_id, domain=ConditionRelation, range=Optional[str])

slots.ConditionRelation_handle = Slot(uri=ALLIANCE.handle, name="ConditionRelation_handle", curie=ALLIANCE.curie('handle'),
                   model_uri=ALLIANCE.ConditionRelation_handle, domain=ConditionRelation, range=Optional[str])

slots.ConditionRelation_single_reference = Slot(uri=ALLIANCE.single_reference, name="ConditionRelation_single_reference", curie=ALLIANCE.curie('single_reference'),
                   model_uri=ALLIANCE.ConditionRelation_single_reference, domain=ConditionRelation, range=Optional[Union[str, ReferenceCurie]])

slots.ConditionRelation_condition_relation_type = Slot(uri=ALLIANCE.condition_relation_type, name="ConditionRelation_condition_relation_type", curie=ALLIANCE.curie('condition_relation_type'),
                   model_uri=ALLIANCE.ConditionRelation_condition_relation_type, domain=ConditionRelation, range=Union[str, VocabularyTermName])

slots.ConditionRelationDTO_condition_relation_type_name = Slot(uri=ALLIANCE.condition_relation_type_name, name="ConditionRelationDTO_condition_relation_type_name", curie=ALLIANCE.curie('condition_relation_type_name'),
                   model_uri=ALLIANCE.ConditionRelationDTO_condition_relation_type_name, domain=ConditionRelationDTO, range=str)

slots.ConditionRelationDTO_condition_dtos = Slot(uri=ALLIANCE.condition_dtos, name="ConditionRelationDTO_condition_dtos", curie=ALLIANCE.curie('condition_dtos'),
                   model_uri=ALLIANCE.ConditionRelationDTO_condition_dtos, domain=ConditionRelationDTO, range=Union[Union[dict, ExperimentalConditionDTO], List[Union[dict, ExperimentalConditionDTO]]])

slots.Resource_id = Slot(uri=ALLIANCE.id, name="Resource_id", curie=ALLIANCE.curie('id'),
                   model_uri=ALLIANCE.Resource_id, domain=Resource, range=Optional[str])

slots.Resource_title = Slot(uri=ALLIANCE.title, name="Resource_title", curie=ALLIANCE.curie('title'),
                   model_uri=ALLIANCE.Resource_title, domain=Resource, range=Optional[str])

slots.ResourceDescriptorPage_name = Slot(uri=ALLIANCE.name, name="ResourceDescriptorPage_name", curie=ALLIANCE.curie('name'),
                   model_uri=ALLIANCE.ResourceDescriptorPage_name, domain=ResourceDescriptorPage, range=str)

slots.AlleleFunctionalImpactSlotAnnotationDTO_phenotype_term = Slot(uri=ALLIANCE.phenotype_term, name="AlleleFunctionalImpactSlotAnnotationDTO_phenotype_term", curie=ALLIANCE.curie('phenotype_term'),
                   model_uri=ALLIANCE.AlleleFunctionalImpactSlotAnnotationDTO_phenotype_term, domain=AlleleFunctionalImpactSlotAnnotationDTO, range=Optional[Union[str, PhenotypeTermCurie]])

slots.AlleleFunctionalImpactSlotAnnotationDTO_phenotype_statement = Slot(uri=ALLIANCE.phenotype_statement, name="AlleleFunctionalImpactSlotAnnotationDTO_phenotype_statement", curie=ALLIANCE.curie('phenotype_statement'),
                   model_uri=ALLIANCE.AlleleFunctionalImpactSlotAnnotationDTO_phenotype_statement, domain=AlleleFunctionalImpactSlotAnnotationDTO, range=Optional[str])

slots.AlleleInheritanceModeSlotAnnotationDTO_inheritance_mode_name = Slot(uri=ALLIANCE.inheritance_mode_name, name="AlleleInheritanceModeSlotAnnotationDTO_inheritance_mode_name", curie=ALLIANCE.curie('inheritance_mode_name'),
                   model_uri=ALLIANCE.AlleleInheritanceModeSlotAnnotationDTO_inheritance_mode_name, domain=AlleleInheritanceModeSlotAnnotationDTO, range=str)

slots.AlleleInheritanceModeSlotAnnotationDTO_phenotype_term_curie = Slot(uri=ALLIANCE.phenotype_term_curie, name="AlleleInheritanceModeSlotAnnotationDTO_phenotype_term_curie", curie=ALLIANCE.curie('phenotype_term_curie'),
                   model_uri=ALLIANCE.AlleleInheritanceModeSlotAnnotationDTO_phenotype_term_curie, domain=AlleleInheritanceModeSlotAnnotationDTO, range=Optional[str])

slots.AlleleInheritanceModeSlotAnnotationDTO_phenotype_statement = Slot(uri=ALLIANCE.phenotype_statement, name="AlleleInheritanceModeSlotAnnotationDTO_phenotype_statement", curie=ALLIANCE.curie('phenotype_statement'),
                   model_uri=ALLIANCE.AlleleInheritanceModeSlotAnnotationDTO_phenotype_statement, domain=AlleleInheritanceModeSlotAnnotationDTO, range=Optional[str])

slots.AlleleNoteSlotAnnotationDTO_note_dto = Slot(uri=ALLIANCE.note_dto, name="AlleleNoteSlotAnnotationDTO_note_dto", curie=ALLIANCE.curie('note_dto'),
                   model_uri=ALLIANCE.AlleleNoteSlotAnnotationDTO_note_dto, domain=AlleleNoteSlotAnnotationDTO, range=Union[dict, NoteDTO])

slots.AlleleSecondaryIdSlotAnnotationDTO_secondary_id = Slot(uri=ALLIANCE.secondary_id, name="AlleleSecondaryIdSlotAnnotationDTO_secondary_id", curie=ALLIANCE.curie('secondary_id'),
                   model_uri=ALLIANCE.AlleleSecondaryIdSlotAnnotationDTO_secondary_id, domain=AlleleSecondaryIdSlotAnnotationDTO, range=Union[str, URIorCURIE])

slots.AlleleConstructAssociationDTO_predicate_name = Slot(uri=ALLIANCE.predicate_name, name="AlleleConstructAssociationDTO_predicate_name", curie=ALLIANCE.curie('predicate_name'),
                   model_uri=ALLIANCE.AlleleConstructAssociationDTO_predicate_name, domain=AlleleConstructAssociationDTO, range=str)

slots.AlleleGenerationMethodAssociationDTO_predicate_name = Slot(uri=ALLIANCE.predicate_name, name="AlleleGenerationMethodAssociationDTO_predicate_name", curie=ALLIANCE.curie('predicate_name'),
                   model_uri=ALLIANCE.AlleleGenerationMethodAssociationDTO_predicate_name, domain=AlleleGenerationMethodAssociationDTO, range=str)

slots.AlleleGenomicEntityAssociationDTO_evidence_curies = Slot(uri=ALLIANCE.evidence_curies, name="AlleleGenomicEntityAssociationDTO_evidence_curies", curie=ALLIANCE.curie('evidence_curies'),
                   model_uri=ALLIANCE.AlleleGenomicEntityAssociationDTO_evidence_curies, domain=AlleleGenomicEntityAssociationDTO, range=Union[str, List[str]])

slots.AlleleImageAssociationDTO_primary_image = Slot(uri=ALLIANCE.primary_image, name="AlleleImageAssociationDTO_primary_image", curie=ALLIANCE.curie('primary_image'),
                   model_uri=ALLIANCE.AlleleImageAssociationDTO_primary_image, domain=AlleleImageAssociationDTO, range=Optional[Union[bool, Bool]])

slots.AllianceMember_abbreviation = Slot(uri=ALLIANCE.abbreviation, name="AllianceMember_abbreviation", curie=ALLIANCE.curie('abbreviation'),
                   model_uri=ALLIANCE.AllianceMember_abbreviation, domain=AllianceMember, range=str)

slots.AllianceMember_date_created = Slot(uri=ALLIANCE.date_created, name="AllianceMember_date_created", curie=ALLIANCE.curie('date_created'),
                   model_uri=ALLIANCE.AllianceMember_date_created, domain=AllianceMember, range=Union[str, XSDDateTime])
