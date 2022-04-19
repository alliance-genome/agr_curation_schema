# Auto generated from geneInteraction.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-04-19T13:13:34
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
from linkml_runtime.linkml_model.types import Boolean, Date, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate

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
ALLIANCE = CurieNamespace('alliance', 'http://alliancegenome.org')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
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


class TranscriptCurie(GenomicEntityCurie):
    pass


class GeneCurie(GenomicEntityCurie):
    pass


class CrossReferenceCurie(URIorCURIE):
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


class DAOTermCurie(AnatomicalTermCurie):
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


class ChemicalTermCurie(OntologyTermCurie):
    pass


class CHEBITermCurie(ChemicalTermCurie):
    pass


class MoleculeCurie(ChemicalTermCurie):
    pass


class VocabularyTermName(extended_str):
    pass


class VocabularyName(extended_str):
    pass


class AlleleCurie(GenomicEntityCurie):
    pass


class VariantCurie(GenomicEntityCurie):
    pass


class AffectedGenomicModelCurie(GenomicEntityCurie):
    pass


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
    taxon: Union[str, NCBITaxonTermCurie] = None
    created_by: Union[str, PersonUniqueId] = None
    modified_by: Union[str, PersonUniqueId] = None
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
        if not isinstance(self.taxon, NCBITaxonTermCurie):
            self.taxon = NCBITaxonTermCurie(self.taxon)

        if self._is_empty(self.created_by):
            self.MissingRequiredField("created_by")
        if not isinstance(self.created_by, PersonUniqueId):
            self.created_by = PersonUniqueId(self.created_by)

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, PersonUniqueId):
            self.modified_by = PersonUniqueId(self.modified_by)

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
    taxon: Union[str, NCBITaxonTermCurie] = None
    created_by: Union[str, PersonUniqueId] = None
    modified_by: Union[str, PersonUniqueId] = None
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
    taxon: Union[str, NCBITaxonTermCurie] = None
    created_by: Union[str, PersonUniqueId] = None
    modified_by: Union[str, PersonUniqueId] = None

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
    taxon: Union[str, NCBITaxonTermCurie] = None
    created_by: Union[str, PersonUniqueId] = None
    modified_by: Union[str, PersonUniqueId] = None
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


@dataclass
class CrossReference(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.CrossReference
    class_class_curie: ClassVar[str] = "alliance:CrossReference"
    class_name: ClassVar[str] = "CrossReference"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.CrossReference

    curie: Union[str, CrossReferenceCurie] = None
    page_areas: Union[str, List[str]] = None
    display_name: str = None
    prefix: str = None
    created_by: Union[str, PersonUniqueId] = None
    modified_by: Union[str, PersonUniqueId] = None
    table_key: Optional[int] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None

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

        if self._is_empty(self.created_by):
            self.MissingRequiredField("created_by")
        if not isinstance(self.created_by, PersonUniqueId):
            self.created_by = PersonUniqueId(self.created_by)

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, PersonUniqueId):
            self.modified_by = PersonUniqueId(self.modified_by)

        if self.table_key is not None and not isinstance(self.table_key, int):
            self.table_key = int(self.table_key)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

        super().__post_init__(**kwargs)


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

    created_by: Union[str, PersonUniqueId] = None
    modified_by: Union[str, PersonUniqueId] = None
    table_key: Optional[int] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.created_by):
            self.MissingRequiredField("created_by")
        if not isinstance(self.created_by, PersonUniqueId):
            self.created_by = PersonUniqueId(self.created_by)

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, PersonUniqueId):
            self.modified_by = PersonUniqueId(self.modified_by)

        if self.table_key is not None and not isinstance(self.table_key, int):
            self.table_key = int(self.table_key)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

        super().__post_init__(**kwargs)


@dataclass
class Note(YAMLRoot):
    """
    Note object for capturing free-text describing some attribute of an entity, coupled with a 'note type', internal
    boolean, and an optional list of references. Permissible values for 'note_type' currently = disease_summary,
    disease_note
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Note
    class_class_curie: ClassVar[str] = "alliance:Note"
    class_name: ClassVar[str] = "Note"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Note

    free_text: str = None
    note_type: Union[str, VocabularyTermName] = None
    internal: Union[bool, Bool] = None
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

        if self._is_empty(self.internal):
            self.MissingRequiredField("internal")
        if not isinstance(self.internal, Bool):
            self.internal = Bool(self.internal)

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, ReferenceCurie) else ReferenceCurie(v) for v in self.references]

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
    cross_references: Optional[Union[Dict[Union[str, CrossReferenceCurie], Union[dict, "CrossReference"]], List[Union[dict, "CrossReference"]]]] = empty_dict()
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
class Protein(GenomicEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Protein
    class_class_curie: ClassVar[str] = "alliance:Protein"
    class_name: ClassVar[str] = "Protein"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Protein

    curie: Union[str, ProteinCurie] = None
    taxon: Union[str, NCBITaxonTermCurie] = None
    created_by: Union[str, PersonUniqueId] = None
    modified_by: Union[str, PersonUniqueId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ProteinCurie):
            self.curie = ProteinCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class AuthorReference(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/reference/AuthorReference")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AuthorReference"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AuthorReference

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
class Reference(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/reference/Reference")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Reference"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Reference

    curie: Union[str, ReferenceCurie] = None
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
class MeshDetail(YAMLRoot):
    """
    Medical Subject Headings information coming from PubMed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/reference/MeshDetail")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "MeshDetail"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.MeshDetail

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
class Resource(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/resource/Resource")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Resource

    curie: Union[str, ResourceCurie] = None
    created_by: Union[str, PersonUniqueId] = None
    modified_by: Union[str, PersonUniqueId] = None
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
    table_key: Optional[int] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ResourceCurie):
            self.curie = ResourceCurie(self.curie)

        if self._is_empty(self.created_by):
            self.MissingRequiredField("created_by")
        if not isinstance(self.created_by, PersonUniqueId):
            self.created_by = PersonUniqueId(self.created_by)

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, PersonUniqueId):
            self.modified_by = PersonUniqueId(self.modified_by)

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
        self.synonyms = [v if isinstance(v, Synonym) else Synonym(**as_dict(v)) for v in self.synonyms]

        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, AuthorReference) else AuthorReference(**as_dict(v)) for v in self.authors]

        if not isinstance(self.editors, list):
            self.editors = [self.editors] if self.editors is not None else []
        self.editors = [v if isinstance(v, AuthorReference) else AuthorReference(**as_dict(v)) for v in self.editors]

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.table_key is not None and not isinstance(self.table_key, int):
            self.table_key = int(self.table_key)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

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

    unique_id: Union[str, PersonUniqueId] = None
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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.LoggedInPerson

    unique_id: Union[str, LoggedInPersonUniqueId] = None
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
    single_reference: Union[str, ReferenceCurie] = None
    created_by: Union[str, PersonUniqueId] = None
    modified_by: Union[str, PersonUniqueId] = None
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

        if self._is_empty(self.single_reference):
            self.MissingRequiredField("single_reference")
        if not isinstance(self.single_reference, ReferenceCurie):
            self.single_reference = ReferenceCurie(self.single_reference)

        if self._is_empty(self.created_by):
            self.MissingRequiredField("created_by")
        if not isinstance(self.created_by, PersonUniqueId):
            self.created_by = PersonUniqueId(self.created_by)

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, PersonUniqueId):
            self.modified_by = PersonUniqueId(self.modified_by)

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
    associated_with_figure: Union[str, FigureCurie] = None
    width: int = None
    height: int = None
    image_file: Union[dict, File] = None
    image_medium_file: Union[dict, File] = None
    image_thumbnail_file: Union[dict, File] = None
    created_by: Union[str, PersonUniqueId] = None
    modified_by: Union[str, PersonUniqueId] = None
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
        if not isinstance(self.created_by, PersonUniqueId):
            self.created_by = PersonUniqueId(self.created_by)

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, PersonUniqueId):
            self.modified_by = PersonUniqueId(self.modified_by)

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

    from_image: Union[str, ImageCurie] = None
    width: int = None
    height: int = None
    created_by: Union[str, PersonUniqueId] = None
    modified_by: Union[str, PersonUniqueId] = None
    label: Optional[str] = None
    image_x_origin: Optional[int] = None
    image_y_origin: Optional[int] = None
    table_key: Optional[int] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None

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

        if self._is_empty(self.created_by):
            self.MissingRequiredField("created_by")
        if not isinstance(self.created_by, PersonUniqueId):
            self.created_by = PersonUniqueId(self.created_by)

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, PersonUniqueId):
            self.modified_by = PersonUniqueId(self.modified_by)

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
class NCBITaxonTerm(OntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/NCBITaxonTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "NCBITaxonTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.NCBITaxonTerm

    curie: Union[str, NCBITaxonTermCurie] = None

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
class ROTerm(OntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/ROTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ROTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ROTerm

    curie: Union[str, ROTermCurie] = None

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
class DAOTerm(AnatomicalTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/DAOTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DAOTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.DAOTerm

    curie: Union[str, DAOTermCurie] = None

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
class ChemicalTerm(OntologyTerm):
    """
    An ontology term representing a chemical or molecule
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/ChemicalTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ChemicalTerm"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ChemicalTerm

    curie: Union[str, ChemicalTermCurie] = None
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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.CHEBITerm

    curie: Union[str, CHEBITermCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, CHEBITermCurie):
            self.curie = CHEBITermCurie(self.curie)

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Molecule

    curie: Union[str, MoleculeCurie] = None
    created_by: Union[str, PersonUniqueId] = None
    modified_by: Union[str, PersonUniqueId] = None
    table_key: Optional[int] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, MoleculeCurie):
            self.curie = MoleculeCurie(self.curie)

        if self._is_empty(self.created_by):
            self.MissingRequiredField("created_by")
        if not isinstance(self.created_by, PersonUniqueId):
            self.created_by = PersonUniqueId(self.created_by)

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, PersonUniqueId):
            self.modified_by = PersonUniqueId(self.modified_by)

        if self.table_key is not None and not isinstance(self.table_key, int):
            self.table_key = int(self.table_key)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

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

    name: Union[str, VocabularyTermName] = None
    created_by: Union[str, PersonUniqueId] = None
    modified_by: Union[str, PersonUniqueId] = None
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
        if not isinstance(self.name, VocabularyTermName):
            self.name = VocabularyTermName(self.name)

        if self._is_empty(self.created_by):
            self.MissingRequiredField("created_by")
        if not isinstance(self.created_by, PersonUniqueId):
            self.created_by = PersonUniqueId(self.created_by)

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, PersonUniqueId):
            self.modified_by = PersonUniqueId(self.modified_by)

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
    created_by: Union[str, PersonUniqueId] = None
    modified_by: Union[str, PersonUniqueId] = None
    vocabulary_description: Optional[str] = None
    is_obsolete: Optional[Union[bool, Bool]] = None
    member_terms: Optional[Union[Union[str, VocabularyTermName], List[Union[str, VocabularyTermName]]]] = empty_list()
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
        if not isinstance(self.created_by, PersonUniqueId):
            self.created_by = PersonUniqueId(self.created_by)

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, PersonUniqueId):
            self.modified_by = PersonUniqueId(self.modified_by)

        if self.vocabulary_description is not None and not isinstance(self.vocabulary_description, str):
            self.vocabulary_description = str(self.vocabulary_description)

        if self.is_obsolete is not None and not isinstance(self.is_obsolete, Bool):
            self.is_obsolete = Bool(self.is_obsolete)

        if not isinstance(self.member_terms, list):
            self.member_terms = [self.member_terms] if self.member_terms is not None else []
        self.member_terms = [v if isinstance(v, VocabularyTermName) else VocabularyTermName(v) for v in self.member_terms]

        if self.table_key is not None and not isinstance(self.table_key, int):
            self.table_key = int(self.table_key)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

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
    taxon: Union[str, NCBITaxonTermCurie] = None
    created_by: Union[str, PersonUniqueId] = None
    modified_by: Union[str, PersonUniqueId] = None
    symbol: Optional[str] = None
    contains_constructs: Optional[Union[Union[dict, "Construct"], List[Union[dict, "Construct"]]]] = empty_list()
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

        if self.symbol is not None and not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        if not isinstance(self.contains_constructs, list):
            self.contains_constructs = [self.contains_constructs] if self.contains_constructs is not None else []
        self.contains_constructs = [v if isinstance(v, Construct) else Construct(**as_dict(v)) for v in self.contains_constructs]

        if not isinstance(self.molecular_mutations, list):
            self.molecular_mutations = [self.molecular_mutations] if self.molecular_mutations is not None else []
        self.molecular_mutations = [v if isinstance(v, str) else str(v) for v in self.molecular_mutations]

        if self.functional_impact is not None and not isinstance(self.functional_impact, str):
            self.functional_impact = str(self.functional_impact)

        if self.generation_method is not None and not isinstance(self.generation_method, str):
            self.generation_method = str(self.generation_method)

        self._normalize_inlined_as_dict(slot_name="associated_references", slot_type=AssociatedReference, key_name="reference_type", keyed=False)

        self._normalize_inlined_as_dict(slot_name="related_notes", slot_type=Note, key_name="free_text", keyed=False)

        if self.germline_transmission_status is not None and not isinstance(self.germline_transmission_status, VocabularyTermName):
            self.germline_transmission_status = VocabularyTermName(self.germline_transmission_status)

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

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, Synonym) else Synonym(**as_dict(v)) for v in self.synonyms]

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleGenomicEntityAssociation

    subject: Union[str, AlleleCurie] = None
    predicate: Union[str, ROTermCurie] = None
    object: Union[str, GenomicEntityCurie] = None
    created_by: Union[str, PersonUniqueId] = None
    modified_by: Union[str, PersonUniqueId] = None
    single_reference: Optional[Union[str, ReferenceCurie]] = None
    evidence_code: Optional[Union[str, ECOTermCurie]] = None
    related_note: Optional[Union[dict, Note]] = None
    table_key: Optional[int] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        if self._is_empty(self.created_by):
            self.MissingRequiredField("created_by")
        if not isinstance(self.created_by, PersonUniqueId):
            self.created_by = PersonUniqueId(self.created_by)

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, PersonUniqueId):
            self.modified_by = PersonUniqueId(self.modified_by)

        if self.single_reference is not None and not isinstance(self.single_reference, ReferenceCurie):
            self.single_reference = ReferenceCurie(self.single_reference)

        if self.evidence_code is not None and not isinstance(self.evidence_code, ECOTermCurie):
            self.evidence_code = ECOTermCurie(self.evidence_code)

        if self.related_note is not None and not isinstance(self.related_note, Note):
            self.related_note = Note(**as_dict(self.related_note))

        if self.table_key is not None and not isinstance(self.table_key, int):
            self.table_key = int(self.table_key)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleGeneAssociation

    subject: Union[str, AlleleCurie] = None
    predicate: Union[str, ROTermCurie] = None
    created_by: Union[str, PersonUniqueId] = None
    modified_by: Union[str, PersonUniqueId] = None
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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleTranscriptAssociation

    subject: Union[str, AlleleCurie] = None
    predicate: Union[str, ROTermCurie] = None
    created_by: Union[str, PersonUniqueId] = None
    modified_by: Union[str, PersonUniqueId] = None
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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleProteinAssociation

    subject: Union[str, AlleleCurie] = None
    predicate: Union[str, ROTermCurie] = None
    created_by: Union[str, PersonUniqueId] = None
    modified_by: Union[str, PersonUniqueId] = None
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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleVariantAssociation

    predicate: Union[str, ROTermCurie] = None
    created_by: Union[str, PersonUniqueId] = None
    modified_by: Union[str, PersonUniqueId] = None
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
class AssociatedReference(YAMLRoot):
    """
    Describes the relation between a reference and an object
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/AssociatedReference")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AssociatedReference"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AssociatedReference

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


class Construct(YAMLRoot):
    """
    Dummy construct class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/Construct")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Construct"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Construct


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
class Variant(GenomicEntity):
    """
    A DNA, RNA or protein/polypeptide sequence that differs relative to a designated reference sequence. The sequence
    occurs at a single position or in a range of contiguous nucleotides or amino acids.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variation/Variant")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Variant"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Variant

    curie: Union[str, VariantCurie] = None
    taxon: Union[str, NCBITaxonTermCurie] = None
    created_by: Union[str, PersonUniqueId] = None
    modified_by: Union[str, PersonUniqueId] = None
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

        self._normalize_inlined_as_dict(slot_name="related_notes", slot_type=Note, key_name="free_text", keyed=False)

        if self.source_general_consequence is not None and not isinstance(self.source_general_consequence, SOTermCurie):
            self.source_general_consequence = SOTermCurie(self.source_general_consequence)

        self._normalize_inlined_as_dict(slot_name="variant_polypeptide_locations", slot_type=VariantPolypeptideLocation, key_name="polypeptide", keyed=False)

        if not isinstance(self.variant_transcript_locations, list):
            self.variant_transcript_locations = [self.variant_transcript_locations] if self.variant_transcript_locations is not None else []
        self.variant_transcript_locations = [v if isinstance(v, VariantTranscriptLocation) else VariantTranscriptLocation(**as_dict(v)) for v in self.variant_transcript_locations]

        self._normalize_inlined_as_dict(slot_name="source_variant_locations", slot_type=SourceVariantLocation, key_name="variant_locations", keyed=False)

        if self.variant_status is not None and not isinstance(self.variant_status, VariantStatusEnum):
            self.variant_status = VariantStatusEnum(self.variant_status)

        super().__post_init__(**kwargs)


@dataclass
class SourceVariantLocation(YAMLRoot):
    """
    Links a paper to the variant locations described in that paper
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variation/SourceVariantLocation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SourceVariantLocation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.SourceVariantLocation

    variant_locations: Union[Union[dict, "VariantLocation"], List[Union[dict, "VariantLocation"]]] = None
    single_reference: Union[str, ReferenceCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.variant_locations):
            self.MissingRequiredField("variant_locations")
        if not isinstance(self.variant_locations, list):
            self.variant_locations = [self.variant_locations] if self.variant_locations is not None else []
        self.variant_locations = [v if isinstance(v, VariantLocation) else VariantLocation(**as_dict(v)) for v in self.variant_locations]

        if self._is_empty(self.single_reference):
            self.MissingRequiredField("single_reference")
        if not isinstance(self.single_reference, ReferenceCurie):
            self.single_reference = ReferenceCurie(self.single_reference)

        super().__post_init__(**kwargs)


@dataclass
class VariantLocation(YAMLRoot):
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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.VariantLocation

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.VariantGenomeLocation

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.VariantTranscriptLocation

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.VariantPolypeptideLocation

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
    taxon: Union[str, NCBITaxonTermCurie] = None
    created_by: Union[str, PersonUniqueId] = None
    modified_by: Union[str, PersonUniqueId] = None
    subtype: Optional[Union[str, "SubtypeValues"]] = None
    components: Optional[Union[Union[dict, "AffectedGenomicModelComponent"], List[Union[dict, "AffectedGenomicModelComponent"]]]] = empty_list()
    sequence_targeting_reagents: Optional[Union[Union[dict, SequenceTargetingReagent], List[Union[dict, SequenceTargetingReagent]]]] = empty_list()
    parental_populations: Optional[Union[str, URIorCURIE]] = None
    data_provider: Optional[str] = None

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

        if self.data_provider is not None and not isinstance(self.data_provider, str):
            self.data_provider = str(self.data_provider)

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

class EntitySynonymTypeSet(EnumDefinitionImpl):

    current = PermissibleValue(text="current",
                                     description="The synonym is an officially accepted synonym for an entity. An entity should have only one current synonym of a give type. For example, only one current symbol and one current full name.")
    alias = PermissibleValue(text="alias",
                                 description="The synonym is an alternate symbol or name for the entity. It is not the currently preferred symbol/name for the entity.")

    _defn = EnumDefinition(
        name="EntitySynonymTypeSet",
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

class VariantStatusEnum(EnumDefinitionImpl):

    public = PermissibleValue(text="public")
    private = PermissibleValue(text="private")

    _defn = EnumDefinition(
        name="VariantStatusEnum",
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

slots.free_text = Slot(uri=ALLIANCE.free_text, name="free_text", curie=ALLIANCE.curie('free_text'),
                   model_uri=ALLIANCE.free_text, domain=None, range=Optional[str])

slots.note_type = Slot(uri=ALLIANCE.note_type, name="note_type", curie=ALLIANCE.curie('note_type'),
                   model_uri=ALLIANCE.note_type, domain=None, range=Optional[Union[str, VocabularyTermName]])

slots.internal = Slot(uri=ALLIANCE.internal, name="internal", curie=ALLIANCE.curie('internal'),
                   model_uri=ALLIANCE.internal, domain=None, range=Optional[Union[bool, Bool]])

slots.related_notes = Slot(uri=ALLIANCE.related_notes, name="related_notes", curie=ALLIANCE.curie('related_notes'),
                   model_uri=ALLIANCE.related_notes, domain=None, range=Optional[Union[Union[dict, Note], List[Union[dict, Note]]]])

slots.related_note = Slot(uri=ALLIANCE.related_note, name="related_note", curie=ALLIANCE.curie('related_note'),
                   model_uri=ALLIANCE.related_note, domain=None, range=Optional[Union[dict, Note]])

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
                   model_uri=ALLIANCE.taxon, domain=None, range=Optional[Union[str, NCBITaxonTermCurie]])

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
                   model_uri=ALLIANCE.created_by, domain=None, range=Union[str, PersonUniqueId])

slots.modified_by = Slot(uri=ALLIANCE.modified_by, name="modified_by", curie=ALLIANCE.curie('modified_by'),
                   model_uri=ALLIANCE.modified_by, domain=None, range=Union[str, PersonUniqueId])

slots.release = Slot(uri=ALLIANCE.release, name="release", curie=ALLIANCE.curie('release'),
                   model_uri=ALLIANCE.release, domain=None, range=Optional[str])

slots.data_provider = Slot(uri=ALLIANCE.data_provider, name="data_provider", curie=ALLIANCE.curie('data_provider'),
                   model_uri=ALLIANCE.data_provider, domain=None, range=Optional[str])

slots.secondary_data_provider = Slot(uri=ALLIANCE.secondary_data_provider, name="secondary_data_provider", curie=ALLIANCE.curie('secondary_data_provider'),
                   model_uri=ALLIANCE.secondary_data_provider, domain=None, range=Optional[str])

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

slots.references = Slot(uri=ALLIANCE.references, name="references", curie=ALLIANCE.curie('references'),
                   model_uri=ALLIANCE.references, domain=None, range=Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]])

slots.single_reference = Slot(uri=ALLIANCE.single_reference, name="single_reference", curie=ALLIANCE.curie('single_reference'),
                   model_uri=ALLIANCE.single_reference, domain=None, range=Optional[Union[str, ReferenceCurie]])

slots.original_reference = Slot(uri=ALLIANCE.original_reference, name="original_reference", curie=ALLIANCE.curie('original_reference'),
                   model_uri=ALLIANCE.original_reference, domain=None, range=Optional[Union[str, ReferenceCurie]])

slots.is_obsolete = Slot(uri=ALLIANCE.is_obsolete, name="is_obsolete", curie=ALLIANCE.curie('is_obsolete'),
                   model_uri=ALLIANCE.is_obsolete, domain=None, range=Optional[Union[bool, Bool]])

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

slots.subject = Slot(uri=ALLIANCE.subject, name="subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.subject, domain=None, range=str)

slots.object = Slot(uri=ALLIANCE.object, name="object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.object, domain=None, range=str)

slots.predicate = Slot(uri=ALLIANCE.predicate, name="predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.predicate, domain=None, range=str)

slots.related_to = Slot(uri=ALLIANCE.related_to, name="related_to", curie=ALLIANCE.curie('related_to'),
                   model_uri=ALLIANCE.related_to, domain=None, range=Optional[Union[str, List[str]]])

slots.reference_id = Slot(uri="str(uriorcurie)", name="reference_id", curie=None,
                   model_uri=ALLIANCE.reference_id, domain=None, range=int)

slots.mesh_detail_id = Slot(uri="str(uriorcurie)", name="mesh_detail_id", curie=None,
                   model_uri=ALLIANCE.mesh_detail_id, domain=MeshDetail, range=int)

slots.resource_id = Slot(uri="str(uriorcurie)", name="resource_id", curie=None,
                   model_uri=ALLIANCE.resource_id, domain=Reference, range=Optional[int])

slots.heading_term = Slot(uri="str(uriorcurie)", name="heading_term", curie=None,
                   model_uri=ALLIANCE.heading_term, domain=MeshDetail, range=str)

slots.qualifier_term = Slot(uri="str(uriorcurie)", name="qualifier_term", curie=None,
                   model_uri=ALLIANCE.qualifier_term, domain=MeshDetail, range=Optional[str])

slots.pubmed_type = Slot(uri="str(uriorcurie)", name="pubmed_type", curie=None,
                   model_uri=ALLIANCE.pubmed_type, domain=Reference, range=Optional[Union[Union[str, "PubmedTypeEnum"], List[Union[str, "PubmedTypeEnum"]]]])

slots.date_published = Slot(uri="str(uriorcurie)", name="date_published", curie=None,
                   model_uri=ALLIANCE.date_published, domain=None, range=Optional[str])

slots.date_created = Slot(uri="str(uriorcurie)", name="date_created", curie=None,
                   model_uri=ALLIANCE.date_created, domain=None, range=Optional[Union[str, XSDDate]])

slots.date_updated = Slot(uri="str(uriorcurie)", name="date_updated", curie=None,
                   model_uri=ALLIANCE.date_updated, domain=None, range=Optional[Union[str, XSDDate]])

slots.date_arrived_in_pubmed = Slot(uri="str(uriorcurie)", name="date_arrived_in_pubmed", curie=None,
                   model_uri=ALLIANCE.date_arrived_in_pubmed, domain=Reference, range=Optional[Union[str, List[str]]])

slots.date_last_modified_in_pubmed = Slot(uri="str(uriorcurie)", name="date_last_modified_in_pubmed", curie=None,
                   model_uri=ALLIANCE.date_last_modified_in_pubmed, domain=Reference, range=Optional[str])

slots.issue_date = Slot(uri="str(uriorcurie)", name="issue_date", curie=None,
                   model_uri=ALLIANCE.issue_date, domain=None, range=Optional[str])

slots.open_access = Slot(uri="str(uriorcurie)", name="open_access", curie=None,
                   model_uri=ALLIANCE.open_access, domain=Reference, range=Optional[Union[bool, Bool]])

slots.pages = Slot(uri="str(uriorcurie)", name="pages", curie=None,
                   model_uri=ALLIANCE.pages, domain=None, range=Optional[str])

slots.plain_language_abstract = Slot(uri="str(uriorcurie)", name="plain_language_abstract", curie=None,
                   model_uri=ALLIANCE.plain_language_abstract, domain=Reference, range=Optional[str])

slots.pubmed_abstract_languages = Slot(uri="str(uriorcurie)", name="pubmed_abstract_languages", curie=None,
                   model_uri=ALLIANCE.pubmed_abstract_languages, domain=Reference, range=Optional[Union[str, List[str]]])

slots.pubmed_publication_status = Slot(uri="str(uriorcurie)", name="pubmed_publication_status", curie=None,
                   model_uri=ALLIANCE.pubmed_publication_status, domain=Reference, range=Optional[Union[str, "PubmedPublicationStatusEnum"]])

slots.abstract = Slot(uri="str(uriorcurie)", name="abstract", curie=None,
                   model_uri=ALLIANCE.abstract, domain=Reference, range=Optional[str])

slots.citation = Slot(uri="str(uriorcurie)", name="citation", curie=None,
                   model_uri=ALLIANCE.citation, domain=Reference, range=Optional[str])

slots.issue_name = Slot(uri="str(uriorcurie)", name="issue_name", curie=None,
                   model_uri=ALLIANCE.issue_name, domain=Reference, range=Optional[str])

slots.category = Slot(uri="str(uriorcurie)", name="category", curie=None,
                   model_uri=ALLIANCE.category, domain=Reference, range=Optional[Union[str, "ReferenceCategoryEnum"]])

slots.keywords = Slot(uri="str(uriorcurie)", name="keywords", curie=None,
                   model_uri=ALLIANCE.keywords, domain=None, range=Optional[Union[str, List[str]]])

slots.language = Slot(uri="str(uriorcurie)", name="language", curie=None,
                   model_uri=ALLIANCE.language, domain=Reference, range=Optional[str])

slots.merged_into_id = Slot(uri="str(uriorcurie)", name="merged_into_id", curie=None,
                   model_uri=ALLIANCE.merged_into_id, domain=Reference, range=Optional[Union[str, URIorCURIE]])

slots.summary = Slot(uri="str(uriorcurie)", name="summary", curie=None,
                   model_uri=ALLIANCE.summary, domain=Reference, range=Optional[str])

slots.copyright_date = Slot(uri="str(uriorcurie)", name="copyright_date", curie=None,
                   model_uri=ALLIANCE.copyright_date, domain=Reference, range=Optional[Union[str, XSDDate]])

slots.authors = Slot(uri="str(uriorcurie)", name="authors", curie=None,
                   model_uri=ALLIANCE.authors, domain=Reference, range=Optional[Union[Union[dict, AuthorReference], List[Union[dict, AuthorReference]]]])

slots.corresponding_author = Slot(uri="str(uriorcurie)", name="corresponding_author", curie=None,
                   model_uri=ALLIANCE.corresponding_author, domain=Reference, range=Optional[Union[str, ReferenceCurie]])

slots.initials = Slot(uri="str(uriorcurie)", name="initials", curie=None,
                   model_uri=ALLIANCE.initials, domain=Reference, range=Optional[Union[str, ReferenceCurie]])

slots.title = Slot(uri="str(uriorcurie)", name="title", curie=None,
                   model_uri=ALLIANCE.title, domain=Reference, range=Optional[str])

slots.volume = Slot(uri="str(uriorcurie)", name="volume", curie=None,
                   model_uri=ALLIANCE.volume, domain=Reference, range=Optional[str])

slots.publisher = Slot(uri="str(uriorcurie)", name="publisher", curie=None,
                   model_uri=ALLIANCE.publisher, domain=Reference, range=Optional[str])

slots.address = Slot(uri="str(uriorcurie)", name="address", curie=None,
                   model_uri=ALLIANCE.address, domain=None, range=Optional[str])

slots.iso_abbreviation = Slot(uri="str(uriorcurie)", name="iso_abbreviation", curie=None,
                   model_uri=ALLIANCE.iso_abbreviation, domain=Resource, range=Optional[str])

slots.medline_abbreviation = Slot(uri="str(uriorcurie)", name="medline_abbreviation", curie=None,
                   model_uri=ALLIANCE.medline_abbreviation, domain=Resource, range=Optional[str])

slots.print_issn = Slot(uri="str(uriorcurie)", name="print_issn", curie=None,
                   model_uri=ALLIANCE.print_issn, domain=Resource, range=Optional[str])

slots.online_issn = Slot(uri="str(uriorcurie)", name="online_issn", curie=None,
                   model_uri=ALLIANCE.online_issn, domain=Resource, range=Optional[str])

slots.editors = Slot(uri="str(uriorcurie)", name="editors", curie=None,
                   model_uri=ALLIANCE.editors, domain=Resource, range=Optional[Union[Union[dict, AuthorReference], List[Union[dict, AuthorReference]]]])

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

slots.caption = Slot(uri="str(uriorcurie)", name="caption", curie=None,
                   model_uri=ALLIANCE.caption, domain=Figure, range=Optional[str])

slots.cropped_from = Slot(uri="str(uriorcurie)", name="cropped_from", curie=None,
                   model_uri=ALLIANCE.cropped_from, domain=Image, range=Optional[Union[str, ImageCurie]])

slots.associated_with_figure = Slot(uri="str(uriorcurie)", name="associated_with_figure", curie=None,
                   model_uri=ALLIANCE.associated_with_figure, domain=None, range=Optional[Union[str, FigureCurie]])

slots.from_image = Slot(uri="str(uriorcurie)", name="from_image", curie=None,
                   model_uri=ALLIANCE.from_image, domain=ImagePane, range=Optional[Union[str, ImageCurie]])

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

slots.inchi = Slot(uri="str(uriorcurie)", name="inchi", curie=None,
                   model_uri=ALLIANCE.inchi, domain=Molecule, range=Optional[str])

slots.inchi_key = Slot(uri="str(uriorcurie)", name="inchi_key", curie=None,
                   model_uri=ALLIANCE.inchi_key, domain=Molecule, range=Optional[str])

slots.iupac = Slot(uri="str(uriorcurie)", name="iupac", curie=None,
                   model_uri=ALLIANCE.iupac, domain=Molecule, range=Optional[str])

slots.formula = Slot(uri="str(uriorcurie)", name="formula", curie=None,
                   model_uri=ALLIANCE.formula, domain=Molecule, range=Optional[str])

slots.smiles = Slot(uri="str(uriorcurie)", name="smiles", curie=None,
                   model_uri=ALLIANCE.smiles, domain=Molecule, range=Optional[str])

slots.text_synonyms = Slot(uri="str(uriorcurie)", name="text_synonyms", curie=None,
                   model_uri=ALLIANCE.text_synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.member_terms = Slot(uri="str(uriorcurie)", name="member_terms", curie=None,
                   model_uri=ALLIANCE.member_terms, domain=None, range=Optional[Union[Union[str, VocabularyTermName], List[Union[str, VocabularyTermName]]]])

slots.vocabulary_description = Slot(uri="str(uriorcurie)", name="vocabulary_description", curie=None,
                   model_uri=ALLIANCE.vocabulary_description, domain=None, range=Optional[str])

slots.contains_constructs = Slot(uri="str(uriorcurie)", name="contains_constructs", curie=None,
                   model_uri=ALLIANCE.contains_constructs, domain=Allele, range=Optional[Union[Union[dict, "Construct"], List[Union[dict, "Construct"]]]])

slots.molecular_mutations = Slot(uri="str(uriorcurie)", name="molecular_mutations", curie=None,
                   model_uri=ALLIANCE.molecular_mutations, domain=Allele, range=Optional[Union[str, List[str]]])

slots.mutation_type = Slot(uri="str(uriorcurie)", name="mutation_type", curie=None,
                   model_uri=ALLIANCE.mutation_type, domain=Allele, range=Optional[Union[str, SOTermCurie]])

slots.mutation_description = Slot(uri="str(uriorcurie)", name="mutation_description", curie=None,
                   model_uri=ALLIANCE.mutation_description, domain=None, range=Optional[str])

slots.functional_impact = Slot(uri="str(uriorcurie)", name="functional_impact", curie=None,
                   model_uri=ALLIANCE.functional_impact, domain=Allele, range=Optional[str])

slots.generation_method = Slot(uri="str(uriorcurie)", name="generation_method", curie=None,
                   model_uri=ALLIANCE.generation_method, domain=Allele, range=Optional[str])

slots.associated_references = Slot(uri="str(uriorcurie)", name="associated_references", curie=None,
                   model_uri=ALLIANCE.associated_references, domain=None, range=Optional[Union[Union[dict, AssociatedReference], List[Union[dict, AssociatedReference]]]])

slots.reference_type = Slot(uri="str(uriorcurie)", name="reference_type", curie=None,
                   model_uri=ALLIANCE.reference_type, domain=AssociatedReference, range=Union[str, VocabularyTermName])

slots.origins = Slot(uri="str(uriorcurie)", name="origins", curie=None,
                   model_uri=ALLIANCE.origins, domain=Allele, range=Optional[Union[Union[str, AffectedGenomicModelCurie], List[Union[str, AffectedGenomicModelCurie]]]])

slots.germline_transmission_status = Slot(uri="str(uriorcurie)", name="germline_transmission_status", curie=None,
                   model_uri=ALLIANCE.germline_transmission_status, domain=Allele, range=Optional[Union[str, VocabularyTermName]])

slots.parent_cell_line = Slot(uri="str(uriorcurie)", name="parent_cell_line", curie=None,
                   model_uri=ALLIANCE.parent_cell_line, domain=Allele, range=Optional[Union[dict, "CellLine"]])

slots.mutant_cell_lines = Slot(uri="str(uriorcurie)", name="mutant_cell_lines", curie=None,
                   model_uri=ALLIANCE.mutant_cell_lines, domain=Allele, range=Optional[Union[Union[dict, "CellLine"], List[Union[dict, "CellLine"]]]])

slots.embryonic_stem_cell_lines = Slot(uri="str(uriorcurie)", name="embryonic_stem_cell_lines", curie=None,
                   model_uri=ALLIANCE.embryonic_stem_cell_lines, domain=Allele, range=Optional[Union[Union[dict, "CellLine"], List[Union[dict, "CellLine"]]]])

slots.database_status = Slot(uri="str(uriorcurie)", name="database_status", curie=None,
                   model_uri=ALLIANCE.database_status, domain=None, range=Optional[Union[str, VocabularyTermName]])

slots.inheritence_mode = Slot(uri="str(uriorcurie)", name="inheritence_mode", curie=None,
                   model_uri=ALLIANCE.inheritence_mode, domain=Allele, range=Optional[Union[str, VocabularyTermName]])

slots.in_collection = Slot(uri="str(uriorcurie)", name="in_collection", curie=None,
                   model_uri=ALLIANCE.in_collection, domain=Allele, range=Optional[Union[str, VocabularyTermName]])

slots.transposon_insertion = Slot(uri="str(uriorcurie)", name="transposon_insertion", curie=None,
                   model_uri=ALLIANCE.transposon_insertion, domain=Allele, range=Optional[str])

slots.aberration = Slot(uri="str(uriorcurie)", name="aberration", curie=None,
                   model_uri=ALLIANCE.aberration, domain=Allele, range=Optional[str])

slots.is_extinct = Slot(uri="str(uriorcurie)", name="is_extinct", curie=None,
                   model_uri=ALLIANCE.is_extinct, domain=Allele, range=Optional[Union[bool, Bool]])

slots.sequencing_status = Slot(uri="str(uriorcurie)", name="sequencing_status", curie=None,
                   model_uri=ALLIANCE.sequencing_status, domain=Variant, range=Optional[Union[str, VocabularyTermName]])

slots.variant_status = Slot(uri="str(uriorcurie)", name="variant_status", curie=None,
                   model_uri=ALLIANCE.variant_status, domain=None, range=Optional[Union[str, "VariantStatusEnum"]])

slots.variant_type = Slot(uri="str(uriorcurie)", name="variant_type", curie=None,
                   model_uri=ALLIANCE.variant_type, domain=Variant, range=Union[str, SOTermCurie])

slots.source_general_consequence = Slot(uri="str(uriorcurie)", name="source_general_consequence", curie=None,
                   model_uri=ALLIANCE.source_general_consequence, domain=Variant, range=Optional[Union[str, SOTermCurie]])

slots.consequence = Slot(uri="str(uriorcurie)", name="consequence", curie=None,
                   model_uri=ALLIANCE.consequence, domain=VariantLocation, range=Optional[Union[str, SOTermCurie]])

slots.curated_consequence = Slot(uri="str(uriorcurie)", name="curated_consequence", curie=None,
                   model_uri=ALLIANCE.curated_consequence, domain=VariantLocation, range=Optional[Union[str, SOTermCurie]])

slots.variant_locations = Slot(uri="str(uriorcurie)", name="variant_locations", curie=None,
                   model_uri=ALLIANCE.variant_locations, domain=Variant, range=Union[Union[dict, "VariantLocation"], List[Union[dict, "VariantLocation"]]])

slots.variant_genome_locations = Slot(uri="str(uriorcurie)", name="variant_genome_locations", curie=None,
                   model_uri=ALLIANCE.variant_genome_locations, domain=Variant, range=Union[Union[dict, "VariantGenomeLocation"], List[Union[dict, "VariantGenomeLocation"]]])

slots.variant_polypeptide_locations = Slot(uri="str(uriorcurie)", name="variant_polypeptide_locations", curie=None,
                   model_uri=ALLIANCE.variant_polypeptide_locations, domain=Variant, range=Optional[Union[Union[dict, "VariantPolypeptideLocation"], List[Union[dict, "VariantPolypeptideLocation"]]]])

slots.variant_transcript_locations = Slot(uri="str(uriorcurie)", name="variant_transcript_locations", curie=None,
                   model_uri=ALLIANCE.variant_transcript_locations, domain=Variant, range=Optional[Union[Union[dict, "VariantTranscriptLocation"], List[Union[dict, "VariantTranscriptLocation"]]]])

slots.source_variant_locations = Slot(uri="str(uriorcurie)", name="source_variant_locations", curie=None,
                   model_uri=ALLIANCE.source_variant_locations, domain=Variant, range=Optional[Union[Union[dict, "SourceVariantLocation"], List[Union[dict, "SourceVariantLocation"]]]])

slots.hgvs = Slot(uri="str(uriorcurie)", name="hgvs", curie=None,
                   model_uri=ALLIANCE.hgvs, domain=VariantLocation, range=str)

slots.assembly = Slot(uri="str(uriorcurie)", name="assembly", curie=None,
                   model_uri=ALLIANCE.assembly, domain=VariantLocation, range=Optional[Union[str, AssemblyCurie]])

slots.chromosome = Slot(uri="str(uriorcurie)", name="chromosome", curie=None,
                   model_uri=ALLIANCE.chromosome, domain=VariantLocation, range=Optional[Union[str, ChromosomeCurie]])

slots.start_position = Slot(uri="str(uriorcurie)", name="start_position", curie=None,
                   model_uri=ALLIANCE.start_position, domain=VariantLocation, range=Optional[int])

slots.end_position = Slot(uri="str(uriorcurie)", name="end_position", curie=None,
                   model_uri=ALLIANCE.end_position, domain=VariantLocation, range=Optional[int])

slots.reference_sequence = Slot(uri="str(uriorcurie)", name="reference_sequence", curie=None,
                   model_uri=ALLIANCE.reference_sequence, domain=VariantLocation, range=Optional[Union[str, BiologicalSequence]])

slots.variant_sequence = Slot(uri="str(uriorcurie)", name="variant_sequence", curie=None,
                   model_uri=ALLIANCE.variant_sequence, domain=VariantLocation, range=Optional[Union[str, BiologicalSequence]])

slots.transcript = Slot(uri="str(uriorcurie)", name="transcript", curie=None,
                   model_uri=ALLIANCE.transcript, domain=VariantTranscriptLocation, range=Optional[Union[str, TranscriptCurie]])

slots.polypeptide = Slot(uri="str(uriorcurie)", name="polypeptide", curie=None,
                   model_uri=ALLIANCE.polypeptide, domain=VariantTranscriptLocation, range=Union[str, TranscriptCurie])

slots.associated_transcripts = Slot(uri="str(uriorcurie)", name="associated_transcripts", curie=None,
                   model_uri=ALLIANCE.associated_transcripts, domain=VariantPolypeptideLocation, range=Optional[Union[Union[str, TranscriptCurie], List[Union[str, TranscriptCurie]]]])

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

slots.id = Slot(uri=ALLIANCE.id, name="id", curie=ALLIANCE.curie('id'),
                   model_uri=ALLIANCE.id, domain=None, range=Optional[str])

slots.embryonic_cell_lines = Slot(uri=ALLIANCE.embryonic_cell_lines, name="embryonic_cell_lines", curie=ALLIANCE.curie('embryonic_cell_lines'),
                   model_uri=ALLIANCE.embryonic_cell_lines, domain=None, range=Optional[str])

slots.GeneToGeneAssociation_subject = Slot(uri=ALLIANCE.subject, name="GeneToGeneAssociation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.GeneToGeneAssociation_subject, domain=GeneToGeneAssociation, range=Union[str, GeneCurie])

slots.GeneToGeneAssociation_object = Slot(uri=ALLIANCE.object, name="GeneToGeneAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.GeneToGeneAssociation_object, domain=GeneToGeneAssociation, range=Union[str, GeneCurie])

slots.GeneInteraction_curie = Slot(uri=ALLIANCE.curie, name="GeneInteraction_curie", curie=ALLIANCE.curie('curie'),
                   model_uri=ALLIANCE.GeneInteraction_curie, domain=GeneInteraction, range=Union[str, GeneInteractionCurie])

slots.GeneInteraction_cross_references = Slot(uri=ALLIANCE.cross_references, name="GeneInteraction_cross_references", curie=ALLIANCE.curie('cross_references'),
                   model_uri=ALLIANCE.GeneInteraction_cross_references, domain=GeneInteraction, range=Optional[Union[Dict[Union[str, CrossReferenceCurie], Union[dict, "CrossReference"]], List[Union[dict, "CrossReference"]]]])

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

slots.BiologicalEntity_taxon = Slot(uri=ALLIANCE.taxon, name="BiologicalEntity_taxon", curie=ALLIANCE.curie('taxon'),
                   model_uri=ALLIANCE.BiologicalEntity_taxon, domain=BiologicalEntity, range=Union[str, NCBITaxonTermCurie])

slots.Gene_symbol = Slot(uri=ALLIANCE.symbol, name="Gene_symbol", curie=ALLIANCE.curie('symbol'),
                   model_uri=ALLIANCE.Gene_symbol, domain=Gene, range=str)

slots.Note_free_text = Slot(uri=ALLIANCE.free_text, name="Note_free_text", curie=ALLIANCE.curie('free_text'),
                   model_uri=ALLIANCE.Note_free_text, domain=Note, range=str)

slots.Note_note_type = Slot(uri=ALLIANCE.note_type, name="Note_note_type", curie=ALLIANCE.curie('note_type'),
                   model_uri=ALLIANCE.Note_note_type, domain=Note, range=Union[str, VocabularyTermName])

slots.Note_internal = Slot(uri=ALLIANCE.internal, name="Note_internal", curie=ALLIANCE.curie('internal'),
                   model_uri=ALLIANCE.Note_internal, domain=Note, range=Union[bool, Bool])

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

slots.Reference_reference_id = Slot(uri="str(uriorcurie)", name="Reference_reference_id", curie=None,
                   model_uri=ALLIANCE.Reference_reference_id, domain=Reference, range=int)

slots.Reference_date_last_modified = Slot(uri=ALLIANCE.date_last_modified, name="Reference_date_last_modified", curie=ALLIANCE.curie('date_last_modified'),
                   model_uri=ALLIANCE.Reference_date_last_modified, domain=Reference, range=Optional[Union[str, XSDDate]])

slots.MeshDetail_reference_id = Slot(uri="str(uriorcurie)", name="MeshDetail_reference_id", curie=None,
                   model_uri=ALLIANCE.MeshDetail_reference_id, domain=MeshDetail, range=int)

slots.Resource_id = Slot(uri=ALLIANCE.id, name="Resource_id", curie=ALLIANCE.curie('id'),
                   model_uri=ALLIANCE.Resource_id, domain=Resource, range=Optional[str])

slots.Resource_title = Slot(uri="str(uriorcurie)", name="Resource_title", curie=None,
                   model_uri=ALLIANCE.Resource_title, domain=Resource, range=Optional[str])

slots.Person_unique_id = Slot(uri=ALLIANCE.unique_id, name="Person_unique_id", curie=ALLIANCE.curie('unique_id'),
                   model_uri=ALLIANCE.Person_unique_id, domain=Person, range=Union[str, PersonUniqueId])

slots.LoggedInPerson_okta_id = Slot(uri=ALLIANCE.okta_id, name="LoggedInPerson_okta_id", curie=ALLIANCE.curie('okta_id'),
                   model_uri=ALLIANCE.LoggedInPerson_okta_id, domain=LoggedInPerson, range=str)

slots.LoggedInPerson_okta_email = Slot(uri=ALLIANCE.okta_email, name="LoggedInPerson_okta_email", curie=ALLIANCE.curie('okta_email'),
                   model_uri=ALLIANCE.LoggedInPerson_okta_email, domain=LoggedInPerson, range=str)

slots.Figure_single_reference = Slot(uri=ALLIANCE.single_reference, name="Figure_single_reference", curie=ALLIANCE.curie('single_reference'),
                   model_uri=ALLIANCE.Figure_single_reference, domain=Figure, range=Union[str, ReferenceCurie])

slots.Image_associated_with_figure = Slot(uri="str(uriorcurie)", name="Image_associated_with_figure", curie=None,
                   model_uri=ALLIANCE.Image_associated_with_figure, domain=Image, range=Union[str, FigureCurie])

slots.Image_image_x_origin = Slot(uri="str(uriorcurie)", name="Image_image_x_origin", curie=None,
                   model_uri=ALLIANCE.Image_image_x_origin, domain=Image, range=Optional[int])

slots.Image_image_y_origin = Slot(uri="str(uriorcurie)", name="Image_image_y_origin", curie=None,
                   model_uri=ALLIANCE.Image_image_y_origin, domain=Image, range=Optional[int])

slots.ImagePane_from_image = Slot(uri="str(uriorcurie)", name="ImagePane_from_image", curie=None,
                   model_uri=ALLIANCE.ImagePane_from_image, domain=ImagePane, range=Union[str, ImageCurie])

slots.ImagePane_image_x_origin = Slot(uri="str(uriorcurie)", name="ImagePane_image_x_origin", curie=None,
                   model_uri=ALLIANCE.ImagePane_image_x_origin, domain=ImagePane, range=Optional[int])

slots.ImagePane_image_y_origin = Slot(uri="str(uriorcurie)", name="ImagePane_image_y_origin", curie=None,
                   model_uri=ALLIANCE.ImagePane_image_y_origin, domain=ImagePane, range=Optional[int])

slots.OntologyTerm_definition = Slot(uri="str(uriorcurie)", name="OntologyTerm_definition", curie=None,
                   model_uri=ALLIANCE.OntologyTerm_definition, domain=OntologyTerm, range=Optional[str])

slots.ECOTerm_abbreviation = Slot(uri=ALLIANCE.abbreviation, name="ECOTerm_abbreviation", curie=ALLIANCE.curie('abbreviation'),
                   model_uri=ALLIANCE.ECOTerm_abbreviation, domain=ECOTerm, range=Optional[str])

slots.VocabularyTerm_name = Slot(uri=ALLIANCE.name, name="VocabularyTerm_name", curie=ALLIANCE.curie('name'),
                   model_uri=ALLIANCE.VocabularyTerm_name, domain=VocabularyTerm, range=Union[str, VocabularyTermName])

slots.Vocabulary_name = Slot(uri=ALLIANCE.name, name="Vocabulary_name", curie=ALLIANCE.curie('name'),
                   model_uri=ALLIANCE.Vocabulary_name, domain=Vocabulary, range=Union[str, VocabularyName])

slots.Allele_synonyms = Slot(uri=ALLIANCE.synonyms, name="Allele_synonyms", curie=ALLIANCE.curie('synonyms'),
                   model_uri=ALLIANCE.Allele_synonyms, domain=Allele, range=Optional[Union[Union[dict, Synonym], List[Union[dict, Synonym]]]])

slots.Allele_germline_transmission_status = Slot(uri="str(uriorcurie)", name="Allele_germline_transmission_status", curie=None,
                   model_uri=ALLIANCE.Allele_germline_transmission_status, domain=Allele, range=Optional[Union[str, VocabularyTermName]])

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

slots.AlleleGenomicEntityAssociation_subject = Slot(uri=ALLIANCE.subject, name="AlleleGenomicEntityAssociation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.AlleleGenomicEntityAssociation_subject, domain=AlleleGenomicEntityAssociation, range=Union[str, AlleleCurie])

slots.AlleleGenomicEntityAssociation_predicate = Slot(uri=ALLIANCE.predicate, name="AlleleGenomicEntityAssociation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.AlleleGenomicEntityAssociation_predicate, domain=AlleleGenomicEntityAssociation, range=Union[str, ROTermCurie])

slots.AlleleGenomicEntityAssociation_object = Slot(uri=ALLIANCE.object, name="AlleleGenomicEntityAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.AlleleGenomicEntityAssociation_object, domain=AlleleGenomicEntityAssociation, range=Union[str, GenomicEntityCurie])

slots.AlleleGeneAssociation_object = Slot(uri=ALLIANCE.object, name="AlleleGeneAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.AlleleGeneAssociation_object, domain=AlleleGeneAssociation, range=Union[str, GeneCurie])

slots.AlleleTranscriptAssociation_object = Slot(uri=ALLIANCE.object, name="AlleleTranscriptAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.AlleleTranscriptAssociation_object, domain=AlleleTranscriptAssociation, range=Union[str, TranscriptCurie])

slots.AlleleProteinAssociation_object = Slot(uri=ALLIANCE.object, name="AlleleProteinAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.AlleleProteinAssociation_object, domain=AlleleProteinAssociation, range=Union[str, ProteinCurie])

slots.AlleleVariantAssociation_subject = Slot(uri=ALLIANCE.subject, name="AlleleVariantAssociation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.AlleleVariantAssociation_subject, domain=AlleleVariantAssociation, range=Union[str, AlleleCurie])

slots.AlleleVariantAssociation_object = Slot(uri=ALLIANCE.object, name="AlleleVariantAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.AlleleVariantAssociation_object, domain=AlleleVariantAssociation, range=Union[str, VariantCurie])

slots.SourceVariantLocation_single_reference = Slot(uri=ALLIANCE.single_reference, name="SourceVariantLocation_single_reference", curie=ALLIANCE.curie('single_reference'),
                   model_uri=ALLIANCE.SourceVariantLocation_single_reference, domain=SourceVariantLocation, range=Union[str, ReferenceCurie])

slots.VariantLocation_evidence_code = Slot(uri=ALLIANCE.evidence_code, name="VariantLocation_evidence_code", curie=ALLIANCE.curie('evidence_code'),
                   model_uri=ALLIANCE.VariantLocation_evidence_code, domain=VariantLocation, range=Optional[Union[str, ECOTermCurie]])
