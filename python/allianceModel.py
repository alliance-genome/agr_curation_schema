# Auto generated from allianceModel.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-07-18T14:37:40
# Schema: AllianceModel
#
# id: https://github.com/alliance-genome/agr_curation_schema/alliance_schema
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
version = "0.0.1"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOGRID = CurieNamespace('BIOGRID', 'http://identifiers.org/biogrid/')
DIP = CurieNamespace('DIP', 'http://identifiers.org/dip/')
DOI = CurieNamespace('DOI', 'http://identifiers.org/doi/')
EMDB = CurieNamespace('EMDB', 'http://identifiers.org/emdb/')
ENSEMBL = CurieNamespace('ENSEMBL', 'http://identifiers.org/ensembl/')
FB = CurieNamespace('FB', 'http://identifiers.org/fb/')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
HGNC = CurieNamespace('HGNC', 'http://identifiers.org/hgnc/')
IMEX = CurieNamespace('IMEX', 'http://identifiers.org/imex/')
INTACT = CurieNamespace('INTACT', 'http://identifiers.org/intact/')
KEGG = CurieNamespace('KEGG', 'http://identifiers.org/kegg/')
KEGG_PATHWAY = CurieNamespace('KEGG_PATHWAY', 'http://identifiers.org/kegg.pathway/')
MGI = CurieNamespace('MGI', 'http://identifiers.org/mgi/')
MINT = CurieNamespace('MINT', 'http://identifiers.org/mint/')
MSIGDB = CurieNamespace('MSigDB', 'http://example.org/UNKNOWN/MSigDB/')
NLMID = CurieNamespace('NLMID', 'https://www.ncbi.nlm.nih.gov/nlmcatalog/?term=')
PANTHER_PATHWAY = CurieNamespace('PANTHER_PATHWAY', 'http://identifiers.org/panther.pathway/')
PDBE = CurieNamespace('PDBE', 'https://www.ebi.ac.uk/pdbe/entry/pdb/')
PHARMGKB_PATHWAYS = CurieNamespace('PHARMGKB_PATHWAYS', 'http://identifiers.org/pharmgkb.pathways/')
PMC = CurieNamespace('PMC', 'http://identifiers.org/pmc/')
PMID = CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/')
PW = CurieNamespace('PW', 'http://purl.obolibrary.org/obo/PW_')
RCSB_PDB = CurieNamespace('RCSB_PDB', 'https://www.rcsb.org/structure/')
REACT = CurieNamespace('REACT', 'http://www.reactome.org/PathwayBrowser/#/')
RGD = CurieNamespace('RGD', 'http://identifiers.org/rgd/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
SGD = CurieNamespace('SGD', 'http://identifiers.org/sgd/')
SMPDB = CurieNamespace('SMPDB', 'http://identifiers.org/smpdb/')
SO = CurieNamespace('SO', 'http://purl.obolibrary.org/obo/SO_')
WB = CurieNamespace('WB', 'http://identifiers.org/wb/')
WIKIDATA = CurieNamespace('WIKIDATA', 'http://identifiers.org/wikidata/')
WIKIDATA_PROPERTY = CurieNamespace('WIKIDATA_PROPERTY', 'https://www.wikidata.org/wiki/Property:')
WIKIPATHWAYS = CurieNamespace('WIKIPATHWAYS', 'http://identifiers.org/wikipathways/')
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
class PersonUniqueId(extended_str):
    pass


class LoggedInPersonUniqueId(PersonUniqueId):
    pass


class GeneNomenclatureSetCurie(URIorCURIE):
    pass


class VocabularyTermName(extended_str):
    pass


class VocabularyName(extended_str):
    pass


class BiologicalEntityCurie(URIorCURIE):
    pass


class GeneClusterCurie(BiologicalEntityCurie):
    pass


class GeneCollectionCurie(BiologicalEntityCurie):
    pass


class OperonCurie(BiologicalEntityCurie):
    pass


class FunctionalGeneSetCurie(BiologicalEntityCurie):
    pass


class PathwayCurie(BiologicalEntityCurie):
    pass


class ProteinComplexCurie(BiologicalEntityCurie):
    pass


class GenomicEntityCurie(BiologicalEntityCurie):
    pass


class AffectedGenomicModelCurie(GenomicEntityCurie):
    pass


class AlleleCurie(GenomicEntityCurie):
    pass


class ConstructCurie(GenomicEntityCurie):
    pass


class SequenceTargetingReagentCurie(GenomicEntityCurie):
    pass


class ConstructComponentCurie(GenomicEntityCurie):
    pass


class TranscriptCurie(GenomicEntityCurie):
    pass


class CrossReferenceCurie(URIorCURIE):
    pass


class ChromosomeCurie(URIorCURIE):
    pass


class AssemblyCurie(URIorCURIE):
    pass


class ProteinCurie(GenomicEntityCurie):
    pass


class ExpressionExperimentCurie(URIorCURIE):
    pass


class GeneCurie(GenomicEntityCurie):
    pass


class GeneticMapPositionCurie(GenomicEntityCurie):
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


class PhenotypeAnnotationCurie(URIorCURIE):
    pass


class GenePhenotypeAnnotationCurie(PhenotypeAnnotationCurie):
    pass


class AllelePhenotypeAnnotationCurie(PhenotypeAnnotationCurie):
    pass


class AGMPhenotypeAnnotationCurie(PhenotypeAnnotationCurie):
    pass


class ReagentCurie(BiologicalEntityCurie):
    pass


class AntibodyCurie(ReagentCurie):
    pass


class DNACloneCurie(ReagentCurie):
    pass


class RNACloneCurie(ReagentCurie):
    pass


class ReferenceCurie(URIorCURIE):
    pass


class ResourceCurie(URIorCURIE):
    pass


class VariantCurie(GenomicEntityCurie):
    pass


class FigureCurie(URIorCURIE):
    pass


class ImageCurie(URIorCURIE):
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
    date_created: Optional[Union[str, XSDDate]] = None
    updated_by: Optional[Union[str, PersonUniqueId]] = None
    date_updated: Optional[Union[str, XSDDate]] = None
    obsolete: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.internal):
            self.MissingRequiredField("internal")
        if not isinstance(self.internal, Bool):
            self.internal = Bool(self.internal)

        if self.created_by is not None and not isinstance(self.created_by, PersonUniqueId):
            self.created_by = PersonUniqueId(self.created_by)

        if self.date_created is not None and not isinstance(self.date_created, XSDDate):
            self.date_created = XSDDate(self.date_created)

        if self.updated_by is not None and not isinstance(self.updated_by, PersonUniqueId):
            self.updated_by = PersonUniqueId(self.updated_by)

        if self.date_updated is not None and not isinstance(self.date_updated, XSDDate):
            self.date_updated = XSDDate(self.date_updated)

        if self.obsolete is not None and not isinstance(self.obsolete, Bool):
            self.obsolete = Bool(self.obsolete)

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
    has_allele: Optional[Union[str, AlleleCurie]] = None
    zygosity: Optional[Union[str, "ZygosityValues"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_allele is not None and not isinstance(self.has_allele, AlleleCurie):
            self.has_allele = AlleleCurie(self.has_allele)

        if self.zygosity is not None and not isinstance(self.zygosity, ZygosityValues):
            self.zygosity = ZygosityValues(self.zygosity)

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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Organization
    class_class_curie: ClassVar[str] = "alliance:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Organization

    internal: Union[bool, Bool] = None

@dataclass
class Laboratory(Organization):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Laboratory
    class_class_curie: ClassVar[str] = "alliance:Laboratory"
    class_name: ClassVar[str] = "Laboratory"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Laboratory

    internal: Union[bool, Bool] = None

@dataclass
class Company(Organization):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Company
    class_class_curie: ClassVar[str] = "alliance:Company"
    class_name: ClassVar[str] = "Company"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Company

    internal: Union[bool, Bool] = None

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
    internal: Union[bool, Bool] = None
    okta_id: str = None
    okta_email: str = None
    user_settings: Optional[str] = None

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

        super().__post_init__(**kwargs)


@dataclass
class AssociatedReference(AuditedObject):
    """
    Describes the relation between a reference and an object
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AssociatedReference
    class_class_curie: ClassVar[str] = "alliance:AssociatedReference"
    class_name: ClassVar[str] = "AssociatedReference"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AssociatedReference

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
class CellLine(AuditedObject):
    """
    Dummy cell line class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.CellLine
    class_class_curie: ClassVar[str] = "alliance:CellLine"
    class_name: ClassVar[str] = "CellLine"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.CellLine

    internal: Union[bool, Bool] = None

@dataclass
class GeneNomenclatureSet(AuditedObject):
    """
    WB specific. A gene class is a set of genes which share nomenclature, belonging to the same gene class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GeneNomenclatureSet
    class_class_curie: ClassVar[str] = "alliance:GeneNomenclatureSet"
    class_name: ClassVar[str] = "GeneNomenclatureSet"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GeneNomenclatureSet

    curie: Union[str, GeneNomenclatureSetCurie] = None
    internal: Union[bool, Bool] = None
    designating_laboratory: Union[dict, Laboratory] = None
    genes: Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]] = empty_list()
    old_members: Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]] = empty_list()
    synonym: Optional[str] = None
    related_note: Optional[Union[dict, "Note"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, GeneNomenclatureSetCurie):
            self.curie = GeneNomenclatureSetCurie(self.curie)

        if self._is_empty(self.designating_laboratory):
            self.MissingRequiredField("designating_laboratory")
        if not isinstance(self.designating_laboratory, Laboratory):
            self.designating_laboratory = Laboratory(**as_dict(self.designating_laboratory))

        if not isinstance(self.genes, list):
            self.genes = [self.genes] if self.genes is not None else []
        self.genes = [v if isinstance(v, GeneCurie) else GeneCurie(v) for v in self.genes]

        if not isinstance(self.old_members, list):
            self.old_members = [self.old_members] if self.old_members is not None else []
        self.old_members = [v if isinstance(v, GeneCurie) else GeneCurie(v) for v in self.old_members]

        if self.synonym is not None and not isinstance(self.synonym, str):
            self.synonym = str(self.synonym)

        if self.related_note is not None and not isinstance(self.related_note, Note):
            self.related_note = Note(**as_dict(self.related_note))

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
class GeneCluster(BiologicalEntity):
    """
    A gene cluster is a set of genes which have a biological significance, and which are probably clustered together
    on the genome, like histones and miRNAs
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GeneCluster
    class_class_curie: ClassVar[str] = "alliance:GeneCluster"
    class_name: ClassVar[str] = "GeneCluster"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GeneCluster

    curie: Union[str, GeneClusterCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None
    genes: Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]] = empty_list()
    related_note: Optional[Union[dict, "Note"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, GeneClusterCurie):
            self.curie = GeneClusterCurie(self.curie)

        if not isinstance(self.genes, list):
            self.genes = [self.genes] if self.genes is not None else []
        self.genes = [v if isinstance(v, GeneCurie) else GeneCurie(v) for v in self.genes]

        if self.related_note is not None and not isinstance(self.related_note, Note):
            self.related_note = Note(**as_dict(self.related_note))

        super().__post_init__(**kwargs)


@dataclass
class GeneCollection(BiologicalEntity):
    """
    A gene collection is a set of genes which have been grouped based on experimental evidence, for example a set of
    interacting genes, genes in expression cluster, or a set of ChIP binding peaks
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GeneCollection
    class_class_curie: ClassVar[str] = "alliance:GeneCollection"
    class_name: ClassVar[str] = "GeneCollection"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GeneCollection

    curie: Union[str, GeneCollectionCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None
    genes: Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]] = empty_list()
    related_note: Optional[Union[dict, "Note"]] = None
    experiment_type: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, GeneCollectionCurie):
            self.curie = GeneCollectionCurie(self.curie)

        if not isinstance(self.genes, list):
            self.genes = [self.genes] if self.genes is not None else []
        self.genes = [v if isinstance(v, GeneCurie) else GeneCurie(v) for v in self.genes]

        if self.related_note is not None and not isinstance(self.related_note, Note):
            self.related_note = Note(**as_dict(self.related_note))

        if not isinstance(self.experiment_type, list):
            self.experiment_type = [self.experiment_type] if self.experiment_type is not None else []
        self.experiment_type = [v if isinstance(v, str) else str(v) for v in self.experiment_type]

        super().__post_init__(**kwargs)


@dataclass
class Operon(BiologicalEntity):
    """
    The DNA region of a group of adjacent genes whose transcription is coordinated on one or several mutually
    overlapping transcription units transcribed in the same direction and sharing at least one gene.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Operon
    class_class_curie: ClassVar[str] = "alliance:Operon"
    class_name: ClassVar[str] = "Operon"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Operon

    curie: Union[str, OperonCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None
    genes: Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]] = empty_list()
    related_note: Optional[Union[dict, "Note"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, OperonCurie):
            self.curie = OperonCurie(self.curie)

        if not isinstance(self.genes, list):
            self.genes = [self.genes] if self.genes is not None else []
        self.genes = [v if isinstance(v, GeneCurie) else GeneCurie(v) for v in self.genes]

        if self.related_note is not None and not isinstance(self.related_note, Note):
            self.related_note = Note(**as_dict(self.related_note))

        super().__post_init__(**kwargs)


@dataclass
class FunctionalGeneSet(BiologicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.FunctionalGeneSet
    class_class_curie: ClassVar[str] = "alliance:FunctionalGeneSet"
    class_name: ClassVar[str] = "FunctionalGeneSet"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.FunctionalGeneSet

    curie: Union[str, FunctionalGeneSetCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None
    genes: Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]] = empty_list()
    single_reference: Optional[Union[str, ReferenceCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, FunctionalGeneSetCurie):
            self.curie = FunctionalGeneSetCurie(self.curie)

        if not isinstance(self.genes, list):
            self.genes = [self.genes] if self.genes is not None else []
        self.genes = [v if isinstance(v, GeneCurie) else GeneCurie(v) for v in self.genes]

        if self.single_reference is not None and not isinstance(self.single_reference, ReferenceCurie):
            self.single_reference = ReferenceCurie(self.single_reference)

        super().__post_init__(**kwargs)


@dataclass
class Pathway(BiologicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Pathway
    class_class_curie: ClassVar[str] = "alliance:Pathway"
    class_name: ClassVar[str] = "Pathway"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Pathway

    curie: Union[str, PathwayCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, PathwayCurie):
            self.curie = PathwayCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class ProteinComplex(BiologicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ProteinComplex
    class_class_curie: ClassVar[str] = "alliance:ProteinComplex"
    class_name: ClassVar[str] = "ProteinComplex"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ProteinComplex

    curie: Union[str, ProteinComplexCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None
    proteins: Optional[Union[Union[str, ProteinCurie], List[Union[str, ProteinCurie]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ProteinComplexCurie):
            self.curie = ProteinComplexCurie(self.curie)

        if not isinstance(self.proteins, list):
            self.proteins = [self.proteins] if self.proteins is not None else []
        self.proteins = [v if isinstance(v, ProteinCurie) else ProteinCurie(v) for v in self.proteins]

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
    name: Optional[str] = None
    synonyms: Optional[Union[Union[dict, "Synonym"], List[Union[dict, "Synonym"]]]] = empty_list()
    cross_references: Optional[Union[Dict[Union[str, CrossReferenceCurie], Union[dict, "CrossReference"]], List[Union[dict, "CrossReference"]]]] = empty_dict()
    secondary_identifiers: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    genomic_locations: Optional[Union[Union[dict, "GenomicLocation"], List[Union[dict, "GenomicLocation"]]]] = empty_list()

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

        self._normalize_inlined_as_dict(slot_name="genomic_locations", slot_type=GenomicLocation, key_name="internal", keyed=False)

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
    name: str = None
    symbol: Optional[str] = None
    contains_constructs: Optional[Union[Union[str, ConstructCurie], List[Union[str, ConstructCurie]]]] = empty_list()
    molecular_mutations: Optional[Union[str, List[str]]] = empty_list()
    functional_impact: Optional[str] = None
    generation_method: Optional[str] = None
    associated_references: Optional[Union[Union[dict, "AssociatedReference"], List[Union[dict, "AssociatedReference"]]]] = empty_list()
    related_notes: Optional[Union[Union[dict, "Note"], List[Union[dict, "Note"]]]] = empty_list()
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
    synonyms: Optional[Union[Union[dict, "Synonym"], List[Union[dict, "Synonym"]]]] = empty_list()

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
class ConstructComponent(GenomicEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ConstructComponent
    class_class_curie: ClassVar[str] = "alliance:ConstructComponent"
    class_name: ClassVar[str] = "ConstructComponent"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ConstructComponent

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Synonym

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.EntityStatement

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Association

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
    predicate: Union[str, ROTermCurie] = None
    object: Union[str, GenomicEntityCurie] = None
    single_reference: Optional[Union[str, ReferenceCurie]] = None
    evidence_code: Optional[Union[str, ECOTermCurie]] = None
    related_note: Optional[Union[dict, "Note"]] = None

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleGeneAssociation
    class_class_curie: ClassVar[str] = "alliance:AlleleGeneAssociation"
    class_name: ClassVar[str] = "AlleleGeneAssociation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleGeneAssociation

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleTranscriptAssociation
    class_class_curie: ClassVar[str] = "alliance:AlleleTranscriptAssociation"
    class_name: ClassVar[str] = "AlleleTranscriptAssociation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleTranscriptAssociation

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleProteinAssociation
    class_class_curie: ClassVar[str] = "alliance:AlleleProteinAssociation"
    class_name: ClassVar[str] = "AlleleProteinAssociation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleProteinAssociation

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleVariantAssociation
    class_class_curie: ClassVar[str] = "alliance:AlleleVariantAssociation"
    class_name: ClassVar[str] = "AlleleVariantAssociation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleVariantAssociation

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
class SequenceTargetingReagentToGeneAssociation(Association):
    """
    the relationship between a Sequence Targeting Reagent and its targeted genes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.SequenceTargetingReagentToGeneAssociation
    class_class_curie: ClassVar[str] = "alliance:SequenceTargetingReagentToGeneAssociation"
    class_name: ClassVar[str] = "SequenceTargetingReagentToGeneAssociation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.SequenceTargetingReagentToGeneAssociation

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ConstructComponentAssociation
    class_class_curie: ClassVar[str] = "alliance:ConstructComponentAssociation"
    class_name: ClassVar[str] = "ConstructComponentAssociation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ConstructComponentAssociation

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
class GeneToPathwayAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GeneToPathwayAssociation
    class_class_curie: ClassVar[str] = "alliance:GeneToPathwayAssociation"
    class_name: ClassVar[str] = "GeneToPathwayAssociation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GeneToPathwayAssociation

    internal: Union[bool, Bool] = None
    predicate: str = None
    subject: Union[str, GeneCurie] = None
    object: Union[str, PathwayCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GeneCurie):
            self.subject = GeneCurie(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, PathwayCurie):
            self.object = PathwayCurie(self.object)

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
class GenomicLocation(AuditedObject):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GenomicLocation
    class_class_curie: ClassVar[str] = "alliance:GenomicLocation"
    class_name: ClassVar[str] = "GenomicLocation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GenomicLocation

    internal: Union[bool, Bool] = None
    subject: Union[str, GenomicEntityCurie] = None
    predicate: str = None
    object: Union[str, ChromosomeCurie] = None
    has_assembly: Union[str, AssemblyCurie] = None
    start: Optional[str] = None
    end: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, GenomicEntityCurie):
            self.subject = GenomicEntityCurie(self.subject)

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
        if not isinstance(self.has_assembly, AssemblyCurie):
            self.has_assembly = AssemblyCurie(self.has_assembly)

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
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ProteinCurie):
            self.curie = ProteinCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class ExpressionExperiment(AuditedObject):
    """
    Defined by the gene of interest, the specimen, the assay, the reagents (Antibody, Probe), and the reference. It
    groups ExpressionAnnotations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ExpressionExperiment
    class_class_curie: ClassVar[str] = "alliance:ExpressionExperiment"
    class_name: ClassVar[str] = "ExpressionExperiment"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ExpressionExperiment

    curie: Union[str, ExpressionExperimentCurie] = None
    internal: Union[bool, Bool] = None
    single_reference: Optional[Union[str, ReferenceCurie]] = None
    biological_entity_assayed: Optional[Union[str, BiologicalEntityCurie]] = None
    assay_used: Optional[Union[str, MMOTermCurie]] = None
    reagents_used: Optional[Union[Union[str, ReagentCurie], List[Union[str, ReagentCurie]]]] = empty_list()
    specimen_genomic_model: Optional[Union[str, AffectedGenomicModelCurie]] = None
    specimen_alleles: Optional[Union[Union[str, AlleleCurie], List[Union[str, AlleleCurie]]]] = empty_list()
    condition_relations: Optional[Union[Union[dict, "ConditionRelation"], List[Union[dict, "ConditionRelation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ExpressionExperimentCurie):
            self.curie = ExpressionExperimentCurie(self.curie)

        if self.single_reference is not None and not isinstance(self.single_reference, ReferenceCurie):
            self.single_reference = ReferenceCurie(self.single_reference)

        if self.biological_entity_assayed is not None and not isinstance(self.biological_entity_assayed, BiologicalEntityCurie):
            self.biological_entity_assayed = BiologicalEntityCurie(self.biological_entity_assayed)

        if self.assay_used is not None and not isinstance(self.assay_used, MMOTermCurie):
            self.assay_used = MMOTermCurie(self.assay_used)

        if not isinstance(self.reagents_used, list):
            self.reagents_used = [self.reagents_used] if self.reagents_used is not None else []
        self.reagents_used = [v if isinstance(v, ReagentCurie) else ReagentCurie(v) for v in self.reagents_used]

        if self.specimen_genomic_model is not None and not isinstance(self.specimen_genomic_model, AffectedGenomicModelCurie):
            self.specimen_genomic_model = AffectedGenomicModelCurie(self.specimen_genomic_model)

        if not isinstance(self.specimen_alleles, list):
            self.specimen_alleles = [self.specimen_alleles] if self.specimen_alleles is not None else []
        self.specimen_alleles = [v if isinstance(v, AlleleCurie) else AlleleCurie(v) for v in self.specimen_alleles]

        if not isinstance(self.condition_relations, list):
            self.condition_relations = [self.condition_relations] if self.condition_relations is not None else []
        self.condition_relations = [v if isinstance(v, ConditionRelation) else ConditionRelation(**as_dict(v)) for v in self.condition_relations]

        super().__post_init__(**kwargs)


@dataclass
class ExpressionAnnotation(AuditedObject):
    """
    A description of when and where gene products are observed to be present, including experimental details,
    supporting evidence, and curator notes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ExpressionAnnotation
    class_class_curie: ClassVar[str] = "alliance:ExpressionAnnotation"
    class_name: ClassVar[str] = "ExpressionAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ExpressionAnnotation

    internal: Union[bool, Bool] = None
    belongs_to_expression_experiment: Union[str, ExpressionExperimentCurie] = None
    when_expressed: Optional[Union[dict, "TemporalContext"]] = None
    where_expressed: Optional[Union[dict, "AnatomicalSite"]] = None
    expression_qualifiers: Optional[Union[str, "ExpressionQualifierSet"]] = None
    negated: Optional[Union[bool, Bool]] = None
    uncertain: Optional[Union[bool, Bool]] = None
    associated_with_figure: Optional[Union[Union[str, FigureCurie], List[Union[str, FigureCurie]]]] = empty_list()
    assay_notes: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.belongs_to_expression_experiment):
            self.MissingRequiredField("belongs_to_expression_experiment")
        if not isinstance(self.belongs_to_expression_experiment, ExpressionExperimentCurie):
            self.belongs_to_expression_experiment = ExpressionExperimentCurie(self.belongs_to_expression_experiment)

        if self.when_expressed is not None and not isinstance(self.when_expressed, TemporalContext):
            self.when_expressed = TemporalContext(**as_dict(self.when_expressed))

        if self.where_expressed is not None and not isinstance(self.where_expressed, AnatomicalSite):
            self.where_expressed = AnatomicalSite(**as_dict(self.where_expressed))

        if self.expression_qualifiers is not None and not isinstance(self.expression_qualifiers, ExpressionQualifierSet):
            self.expression_qualifiers = ExpressionQualifierSet(self.expression_qualifiers)

        if self.negated is not None and not isinstance(self.negated, Bool):
            self.negated = Bool(self.negated)

        if self.uncertain is not None and not isinstance(self.uncertain, Bool):
            self.uncertain = Bool(self.uncertain)

        if not isinstance(self.associated_with_figure, list):
            self.associated_with_figure = [self.associated_with_figure] if self.associated_with_figure is not None else []
        self.associated_with_figure = [v if isinstance(v, FigureCurie) else FigureCurie(v) for v in self.associated_with_figure]

        if self.assay_notes is not None and not isinstance(self.assay_notes, str):
            self.assay_notes = str(self.assay_notes)

        super().__post_init__(**kwargs)


@dataclass
class TemporalContext(AuditedObject):
    """
    The developmental stage and/or age of the specimen in an annotation. Developmental_stage_stop is optional. Add an
    uncertainty flag here?
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.TemporalContext
    class_class_curie: ClassVar[str] = "alliance:TemporalContext"
    class_name: ClassVar[str] = "TemporalContext"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.TemporalContext

    internal: Union[bool, Bool] = None
    developmental_stage_start: Optional[Union[str, StageTermCurie]] = None
    developmental_stage_stop: Optional[Union[str, StageTermCurie]] = None
    age: Optional[str] = None
    temporal_qualifiers: Optional[Union[str, "TemporalQualifierSet"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.developmental_stage_start is not None and not isinstance(self.developmental_stage_start, StageTermCurie):
            self.developmental_stage_start = StageTermCurie(self.developmental_stage_start)

        if self.developmental_stage_stop is not None and not isinstance(self.developmental_stage_stop, StageTermCurie):
            self.developmental_stage_stop = StageTermCurie(self.developmental_stage_stop)

        if self.age is not None and not isinstance(self.age, str):
            self.age = str(self.age)

        if self.temporal_qualifiers is not None and not isinstance(self.temporal_qualifiers, TemporalQualifierSet):
            self.temporal_qualifiers = TemporalQualifierSet(self.temporal_qualifiers)

        super().__post_init__(**kwargs)


@dataclass
class AnatomicalSite(AuditedObject):
    """
    The developmental stage and/or age of the specimen in an annotation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AnatomicalSite
    class_class_curie: ClassVar[str] = "alliance:AnatomicalSite"
    class_name: ClassVar[str] = "AnatomicalSite"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AnatomicalSite

    internal: Union[bool, Bool] = None
    anatomical_structure: Optional[Union[str, AnatomicalTermCurie]] = None
    anatomical_substructure: Optional[Union[str, AnatomicalTermCurie]] = None
    cellular_component: Optional[Union[str, GOTermCurie]] = None
    spatial_qualifiers: Optional[Union[str, "SpatialQualifierSet"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.anatomical_structure is not None and not isinstance(self.anatomical_structure, AnatomicalTermCurie):
            self.anatomical_structure = AnatomicalTermCurie(self.anatomical_structure)

        if self.anatomical_substructure is not None and not isinstance(self.anatomical_substructure, AnatomicalTermCurie):
            self.anatomical_substructure = AnatomicalTermCurie(self.anatomical_substructure)

        if self.cellular_component is not None and not isinstance(self.cellular_component, GOTermCurie):
            self.cellular_component = GOTermCurie(self.cellular_component)

        if self.spatial_qualifiers is not None and not isinstance(self.spatial_qualifiers, SpatialQualifierSet):
            self.spatial_qualifiers = SpatialQualifierSet(self.spatial_qualifiers)

        super().__post_init__(**kwargs)


@dataclass
class ExpressionAnnotationImagePane(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ExpressionAnnotationImagePane
    class_class_curie: ClassVar[str] = "alliance:ExpressionAnnotationImagePane"
    class_name: ClassVar[str] = "ExpressionAnnotationImagePane"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ExpressionAnnotationImagePane

    internal: Union[bool, Bool] = None
    predicate: str = None
    subject: Union[dict, ExpressionAnnotation] = None
    object: Union[dict, "ImagePane"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ExpressionAnnotation):
            self.subject = ExpressionAnnotation(**as_dict(self.subject))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ImagePane):
            self.object = ImagePane(**as_dict(self.object))

        super().__post_init__(**kwargs)


@dataclass
class GeneExpressionStatement(EntityStatement):
    """
    Free-text describing some aspect(s) of a gene's expression, particularly nuanced information that is not readily
    captured in annotations. May summarize data from many annotations and/or many experiments.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GeneExpressionStatement
    class_class_curie: ClassVar[str] = "alliance:GeneExpressionStatement"
    class_name: ClassVar[str] = "GeneExpressionStatement"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GeneExpressionStatement

    internal: Union[bool, Bool] = None
    statement_subject: Optional[Union[str, GeneCurie]] = None
    statement_type: Optional[Union[str, "ExpressionStatementTypeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.statement_subject is not None and not isinstance(self.statement_subject, GeneCurie):
            self.statement_subject = GeneCurie(self.statement_subject)

        if self.statement_type is not None and not isinstance(self.statement_type, ExpressionStatementTypeEnum):
            self.statement_type = ExpressionStatementTypeEnum(self.statement_type)

        super().__post_init__(**kwargs)


@dataclass
class ExpressionExperimentStatement(EntityStatement):
    """
    Free-text describing some aspect(s) of a gene's expression, particularly nuanced information that is not readily
    captured in annotations. This statement's scope is limited to the associated ExpressionExperiment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ExpressionExperimentStatement
    class_class_curie: ClassVar[str] = "alliance:ExpressionExperimentStatement"
    class_name: ClassVar[str] = "ExpressionExperimentStatement"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ExpressionExperimentStatement

    internal: Union[bool, Bool] = None
    statement_subject: Optional[Union[str, ExpressionExperimentCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.statement_subject is not None and not isinstance(self.statement_subject, ExpressionExperimentCurie):
            self.statement_subject = ExpressionExperimentCurie(self.statement_subject)

        super().__post_init__(**kwargs)


@dataclass
class ExpressionAnnotationStatement(EntityStatement):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.ExpressionAnnotationStatement
    class_class_curie: ClassVar[str] = "alliance:ExpressionAnnotationStatement"
    class_name: ClassVar[str] = "ExpressionAnnotationStatement"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.ExpressionAnnotationStatement

    internal: Union[bool, Bool] = None
    statement_subject: Optional[Union[dict, ExpressionAnnotation]] = None
    statement_type: Optional[Union[str, "ExpressionStatementTypeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.statement_subject is not None and not isinstance(self.statement_subject, ExpressionAnnotation):
            self.statement_subject = ExpressionAnnotation(**as_dict(self.statement_subject))

        if self.statement_type is not None and not isinstance(self.statement_type, ExpressionStatementTypeEnum):
            self.statement_type = ExpressionStatementTypeEnum(self.statement_type)

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
    symbol: str = None
    related_notes: Optional[Union[Union[dict, Note], List[Union[dict, Note]]]] = empty_list()
    gene_type: Optional[Union[str, SOTermCurie]] = None
    gene_types_secondary: Optional[Union[Union[str, SOTermCurie], List[Union[str, SOTermCurie]]]] = empty_list()
    designating_laboratories: Optional[Union[Union[dict, Laboratory], List[Union[dict, Laboratory]]]] = empty_list()
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

        if self._is_empty(self.symbol):
            self.MissingRequiredField("symbol")
        if not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        self._normalize_inlined_as_dict(slot_name="related_notes", slot_type=Note, key_name="internal", keyed=False)

        if self.gene_type is not None and not isinstance(self.gene_type, SOTermCurie):
            self.gene_type = SOTermCurie(self.gene_type)

        if not isinstance(self.gene_types_secondary, list):
            self.gene_types_secondary = [self.gene_types_secondary] if self.gene_types_secondary is not None else []
        self.gene_types_secondary = [v if isinstance(v, SOTermCurie) else SOTermCurie(v) for v in self.gene_types_secondary]

        self._normalize_inlined_as_dict(slot_name="designating_laboratories", slot_type=Laboratory, key_name="internal", keyed=False)

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
class Ingest(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Ingest
    class_class_curie: ClassVar[str] = "alliance:Ingest"
    class_name: ClassVar[str] = "Ingest"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Ingest

    allele_ingest_set: Optional[Union[Dict[Union[str, AlleleCurie], Union[dict, Allele]], List[Union[dict, Allele]]]] = empty_dict()
    disease_allele_ingest_set: Optional[Union[Union[dict, "AlleleDiseaseAnnotation"], List[Union[dict, "AlleleDiseaseAnnotation"]]]] = empty_list()
    disease_agm_ingest_set: Optional[Union[Union[dict, "AGMDiseaseAnnotation"], List[Union[dict, "AGMDiseaseAnnotation"]]]] = empty_list()
    disease_gene_ingest_set: Optional[Union[Union[dict, "GeneDiseaseAnnotation"], List[Union[dict, "GeneDiseaseAnnotation"]]]] = empty_list()
    gene_ingest_set: Optional[Union[Dict[Union[str, GeneCurie], Union[dict, Gene]], List[Union[dict, Gene]]]] = empty_dict()
    variant_ingest_set: Optional[Union[Dict[Union[str, VariantCurie], Union[dict, "Variant"]], List[Union[dict, "Variant"]]]] = empty_dict()
    allele_variant_association_ingest_set: Optional[Union[Union[dict, AlleleVariantAssociation], List[Union[dict, AlleleVariantAssociation]]]] = empty_list()
    agm_ingest_set: Optional[Union[Dict[Union[str, AffectedGenomicModelCurie], Union[dict, AffectedGenomicModel]], List[Union[dict, AffectedGenomicModel]]]] = empty_dict()
    sqtr_ingest_set: Optional[Union[Dict[Union[str, SequenceTargetingReagentCurie], Union[dict, SequenceTargetingReagent]], List[Union[dict, SequenceTargetingReagent]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="allele_ingest_set", slot_type=Allele, key_name="curie", keyed=True)

        if not isinstance(self.disease_allele_ingest_set, list):
            self.disease_allele_ingest_set = [self.disease_allele_ingest_set] if self.disease_allele_ingest_set is not None else []
        self.disease_allele_ingest_set = [v if isinstance(v, AlleleDiseaseAnnotation) else AlleleDiseaseAnnotation(**as_dict(v)) for v in self.disease_allele_ingest_set]

        if not isinstance(self.disease_agm_ingest_set, list):
            self.disease_agm_ingest_set = [self.disease_agm_ingest_set] if self.disease_agm_ingest_set is not None else []
        self.disease_agm_ingest_set = [v if isinstance(v, AGMDiseaseAnnotation) else AGMDiseaseAnnotation(**as_dict(v)) for v in self.disease_agm_ingest_set]

        if not isinstance(self.disease_gene_ingest_set, list):
            self.disease_gene_ingest_set = [self.disease_gene_ingest_set] if self.disease_gene_ingest_set is not None else []
        self.disease_gene_ingest_set = [v if isinstance(v, GeneDiseaseAnnotation) else GeneDiseaseAnnotation(**as_dict(v)) for v in self.disease_gene_ingest_set]

        self._normalize_inlined_as_list(slot_name="gene_ingest_set", slot_type=Gene, key_name="curie", keyed=True)

        self._normalize_inlined_as_list(slot_name="variant_ingest_set", slot_type=Variant, key_name="curie", keyed=True)

        if not isinstance(self.allele_variant_association_ingest_set, list):
            self.allele_variant_association_ingest_set = [self.allele_variant_association_ingest_set] if self.allele_variant_association_ingest_set is not None else []
        self.allele_variant_association_ingest_set = [v if isinstance(v, AlleleVariantAssociation) else AlleleVariantAssociation(**as_dict(v)) for v in self.allele_variant_association_ingest_set]

        self._normalize_inlined_as_list(slot_name="agm_ingest_set", slot_type=AffectedGenomicModel, key_name="curie", keyed=True)

        self._normalize_inlined_as_list(slot_name="sqtr_ingest_set", slot_type=SequenceTargetingReagent, key_name="curie", keyed=True)

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
    date_created: Union[str, XSDDate] = None
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
        if not isinstance(self.date_created, XSDDate):
            self.date_created = XSDDate(self.date_created)

        if self.single_reference is not None and not isinstance(self.single_reference, ReferenceCurie):
            self.single_reference = ReferenceCurie(self.single_reference)

        if self.phenotype_term is not None and not isinstance(self.phenotype_term, PhenotypeTermCurie):
            self.phenotype_term = PhenotypeTermCurie(self.phenotype_term)

        if not isinstance(self.condition_relations, list):
            self.condition_relations = [self.condition_relations] if self.condition_relations is not None else []
        self.condition_relations = [v if isinstance(v, ConditionRelation) else ConditionRelation(**as_dict(v)) for v in self.condition_relations]

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
    date_created: Union[str, XSDDate] = None
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
    date_created: Union[str, XSDDate] = None
    subject: Union[str, AlleleCurie] = None
    inferred_gene: Optional[Union[str, GeneCurie]] = None
    asserted_gene: Optional[Union[str, GeneCurie]] = None
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

        if self.asserted_gene is not None and not isinstance(self.asserted_gene, GeneCurie):
            self.asserted_gene = GeneCurie(self.asserted_gene)

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
    date_created: Union[str, XSDDate] = None
    subject: Union[str, AffectedGenomicModelCurie] = None
    inferred_allele: Optional[Union[str, AlleleCurie]] = None
    inferred_gene: Optional[Union[str, GeneCurie]] = None
    asserted_gene: Optional[Union[str, GeneCurie]] = None
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

        if self.asserted_gene is not None and not isinstance(self.asserted_gene, GeneCurie):
            self.asserted_gene = GeneCurie(self.asserted_gene)

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

    internal: Union[bool, Bool] = None
    evidence_codes: Union[Union[str, ECOTermCurie], List[Union[str, ECOTermCurie]]] = None
    single_reference: Union[str, ReferenceCurie] = None
    data_provider: str = None
    subject: Union[str, BiologicalEntityCurie] = None
    predicate: str = None
    object: Union[str, DOTermCurie] = None
    unique_id: Optional[str] = None
    mod_entity_id: Optional[str] = None
    negated: Optional[Union[bool, Bool]] = None
    annotation_type: Optional[Union[str, VocabularyTermName]] = None
    with: Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]] = empty_list()
    disease_qualifiers: Optional[Union[Union[str, VocabularyTermName], List[Union[str, VocabularyTermName]]]] = empty_list()
    condition_relations: Optional[Union[Union[dict, "ConditionRelation"], List[Union[dict, "ConditionRelation"]]]] = empty_list()
    genetic_sex: Optional[Union[str, VocabularyTermName]] = None
    related_notes: Optional[Union[Union[dict, Note], List[Union[dict, Note]]]] = empty_list()
    secondary_data_provider: Optional[str] = None
    disease_genetic_modifier: Optional[Union[str, BiologicalEntityCurie]] = None
    disease_genetic_modifier_relation: Optional[Union[str, VocabularyTermName]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
        if not isinstance(self.data_provider, str):
            self.data_provider = str(self.data_provider)

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

        if not isinstance(self.with, list):
            self.with = [self.with] if self.with is not None else []
        self.with = [v if isinstance(v, GeneCurie) else GeneCurie(v) for v in self.with]

        if not isinstance(self.disease_qualifiers, list):
            self.disease_qualifiers = [self.disease_qualifiers] if self.disease_qualifiers is not None else []
        self.disease_qualifiers = [v if isinstance(v, VocabularyTermName) else VocabularyTermName(v) for v in self.disease_qualifiers]

        if not isinstance(self.condition_relations, list):
            self.condition_relations = [self.condition_relations] if self.condition_relations is not None else []
        self.condition_relations = [v if isinstance(v, ConditionRelation) else ConditionRelation(**as_dict(v)) for v in self.condition_relations]

        if self.genetic_sex is not None and not isinstance(self.genetic_sex, VocabularyTermName):
            self.genetic_sex = VocabularyTermName(self.genetic_sex)

        self._normalize_inlined_as_dict(slot_name="related_notes", slot_type=Note, key_name="internal", keyed=False)

        if self.secondary_data_provider is not None and not isinstance(self.secondary_data_provider, str):
            self.secondary_data_provider = str(self.secondary_data_provider)

        if self.disease_genetic_modifier is not None and not isinstance(self.disease_genetic_modifier, BiologicalEntityCurie):
            self.disease_genetic_modifier = BiologicalEntityCurie(self.disease_genetic_modifier)

        if self.disease_genetic_modifier_relation is not None and not isinstance(self.disease_genetic_modifier_relation, VocabularyTermName):
            self.disease_genetic_modifier_relation = VocabularyTermName(self.disease_genetic_modifier_relation)

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

    internal: Union[bool, Bool] = None
    evidence_codes: Union[Union[str, ECOTermCurie], List[Union[str, ECOTermCurie]]] = None
    single_reference: Union[str, ReferenceCurie] = None
    data_provider: str = None
    object: Union[str, DOTermCurie] = None
    subject: Union[str, GeneCurie] = None
    predicate: Union[str, VocabularyTermName] = None
    sgd_strain_background: Optional[Union[str, AffectedGenomicModelCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
class AlleleDiseaseAnnotation(DiseaseAnnotation):
    """
    An annotation asserting an association between an allele and a disease supported by evidence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AlleleDiseaseAnnotation
    class_class_curie: ClassVar[str] = "alliance:AlleleDiseaseAnnotation"
    class_name: ClassVar[str] = "AlleleDiseaseAnnotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AlleleDiseaseAnnotation

    internal: Union[bool, Bool] = None
    evidence_codes: Union[Union[str, ECOTermCurie], List[Union[str, ECOTermCurie]]] = None
    single_reference: Union[str, ReferenceCurie] = None
    data_provider: str = None
    object: Union[str, DOTermCurie] = None
    subject: Union[str, AlleleCurie] = None
    predicate: Union[str, VocabularyTermName] = None
    inferred_gene: Optional[Union[str, GeneCurie]] = None
    asserted_gene: Optional[Union[str, GeneCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        if self.asserted_gene is not None and not isinstance(self.asserted_gene, GeneCurie):
            self.asserted_gene = GeneCurie(self.asserted_gene)

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

    internal: Union[bool, Bool] = None
    evidence_codes: Union[Union[str, ECOTermCurie], List[Union[str, ECOTermCurie]]] = None
    single_reference: Union[str, ReferenceCurie] = None
    data_provider: str = None
    object: Union[str, DOTermCurie] = None
    subject: Union[str, AffectedGenomicModelCurie] = None
    predicate: Union[str, VocabularyTermName] = None
    inferred_allele: Optional[Union[str, AlleleCurie]] = None
    inferred_gene: Optional[Union[str, GeneCurie]] = None
    asserted_gene: Optional[Union[str, GeneCurie]] = None
    asserted_allele: Optional[Union[str, AlleleCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        if self.asserted_gene is not None and not isinstance(self.asserted_gene, GeneCurie):
            self.asserted_gene = GeneCurie(self.asserted_gene)

        if self.asserted_allele is not None and not isinstance(self.asserted_allele, AlleleCurie):
            self.asserted_allele = AlleleCurie(self.asserted_allele)

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
    condition_statement: str = None
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

        if self._is_empty(self.condition_statement):
            self.MissingRequiredField("condition_statement")
        if not isinstance(self.condition_statement, str):
            self.condition_statement = str(self.condition_statement)

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

        if not isinstance(self.conditions, list):
            self.conditions = [self.conditions] if self.conditions is not None else []
        self.conditions = [v if isinstance(v, ExperimentalCondition) else ExperimentalCondition(**as_dict(v)) for v in self.conditions]

        super().__post_init__(**kwargs)


@dataclass
class Reagent(BiologicalEntity):
    """
    A material entity used in experiments.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Reagent
    class_class_curie: ClassVar[str] = "alliance:Reagent"
    class_name: ClassVar[str] = "Reagent"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Reagent

    curie: Union[str, ReagentCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None
    generated_by: Optional[Union[Union[dict, Agent], List[Union[dict, Agent]]]] = empty_list()
    manufactured_by: Optional[Union[Union[dict, Agent], List[Union[dict, Agent]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ReagentCurie):
            self.curie = ReagentCurie(self.curie)

        self._normalize_inlined_as_dict(slot_name="generated_by", slot_type=Agent, key_name="internal", keyed=False)

        self._normalize_inlined_as_dict(slot_name="manufactured_by", slot_type=Agent, key_name="internal", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class Antibody(Reagent):
    """
    Immunoglobulin proteins that bind specific molecule(s). Can be used experimentally for the purposes of detection
    or purification.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Antibody
    class_class_curie: ClassVar[str] = "alliance:Antibody"
    class_name: ClassVar[str] = "Antibody"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Antibody

    curie: Union[str, AntibodyCurie] = None
    internal: Union[bool, Bool] = None
    name: str = None
    clonality: Union[str, "AntibodyClonalitySet"] = None
    antigen_taxon: Optional[Union[str, NCBITaxonTermCurie]] = None
    heavy_chain_isotype: Optional[Union[str, "HeavyChainIsotypeSet"]] = None
    light_chain_isotype: Optional[Union[str, "LightChainIsotypeSet"]] = None
    antibody_target_genes: Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]] = empty_list()
    cross_references: Optional[Union[Dict[Union[str, CrossReferenceCurie], Union[dict, CrossReference]], List[Union[dict, CrossReference]]]] = empty_dict()
    secondary_identifiers: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    references: Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]] = empty_list()
    original_reference: Optional[Union[str, ReferenceCurie]] = None
    related_notes: Optional[Union[Union[dict, Note], List[Union[dict, Note]]]] = empty_list()
    taxon: Optional[Union[str, NCBITaxonTermCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, AntibodyCurie):
            self.curie = AntibodyCurie(self.curie)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.clonality):
            self.MissingRequiredField("clonality")
        if not isinstance(self.clonality, AntibodyClonalitySet):
            self.clonality = AntibodyClonalitySet(self.clonality)

        if self.antigen_taxon is not None and not isinstance(self.antigen_taxon, NCBITaxonTermCurie):
            self.antigen_taxon = NCBITaxonTermCurie(self.antigen_taxon)

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

        self._normalize_inlined_as_dict(slot_name="related_notes", slot_type=Note, key_name="internal", keyed=False)

        if self.taxon is not None and not isinstance(self.taxon, NCBITaxonTermCurie):
            self.taxon = NCBITaxonTermCurie(self.taxon)

        super().__post_init__(**kwargs)


@dataclass
class DNAClone(Reagent):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.DNAClone
    class_class_curie: ClassVar[str] = "alliance:DNAClone"
    class_name: ClassVar[str] = "DNAClone"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.DNAClone

    curie: Union[str, DNACloneCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, DNACloneCurie):
            self.curie = DNACloneCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class RNAClone(Reagent):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.RNAClone
    class_class_curie: ClassVar[str] = "alliance:RNAClone"
    class_name: ClassVar[str] = "RNAClone"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.RNAClone

    curie: Union[str, RNACloneCurie] = None
    internal: Union[bool, Bool] = None
    taxon: Union[str, NCBITaxonTermCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, RNACloneCurie):
            self.curie = RNACloneCurie(self.curie)

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
    cross_references: Optional[Union[Dict[Union[str, CrossReferenceCurie], Union[dict, CrossReference]], List[Union[dict, CrossReference]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.corresponding_author is not None and not isinstance(self.corresponding_author, Bool):
            self.corresponding_author = Bool(self.corresponding_author)

        if self.first_author is not None and not isinstance(self.first_author, Bool):
            self.first_author = Bool(self.first_author)

        if self.first_name is not None and not isinstance(self.first_name, str):
            self.first_name = str(self.first_name)

        if self.last_name is not None and not isinstance(self.last_name, str):
            self.last_name = str(self.last_name)

        self._normalize_inlined_as_list(slot_name="cross_references", slot_type=CrossReference, key_name="curie", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Reference(AuditedObject):
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
class VariantConsequence(AuditedObject):
    """
    Parent class for gene- and transcript-level consequences
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.VariantConsequence
    class_class_curie: ClassVar[str] = "alliance:VariantConsequence"
    class_name: ClassVar[str] = "VariantConsequence"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.VariantConsequence

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.VariantGeneConsequence
    class_class_curie: ClassVar[str] = "alliance:VariantGeneConsequence"
    class_name: ClassVar[str] = "VariantGeneConsequence"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.VariantGeneConsequence

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.VariantTranscriptConsequence
    class_class_curie: ClassVar[str] = "alliance:VariantTranscriptConsequence"
    class_name: ClassVar[str] = "VariantTranscriptConsequence"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.VariantTranscriptConsequence

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

    class_class_uri: ClassVar[URIRef] = ALLIANCE.SourceVariantLocation
    class_class_curie: ClassVar[str] = "alliance:SourceVariantLocation"
    class_name: ClassVar[str] = "SourceVariantLocation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.SourceVariantLocation

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


# Enumerations
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

class EntitySynonymTypeSet(EnumDefinitionImpl):

    current = PermissibleValue(text="current",
                                     description="The synonym is an officially accepted synonym for an entity. An entity should have only one current synonym of a give type. For example, only one current symbol and one current full name.")
    alias = PermissibleValue(text="alias",
                                 description="The synonym is an alternate symbol or name for the entity. It is not the currently preferred symbol/name for the entity.")

    _defn = EnumDefinition(
        name="EntitySynonymTypeSet",
    )

class SpatialQualifierSet(EnumDefinitionImpl):

    anterior = PermissibleValue(text="anterior")
    anterior_posterior_gradient = PermissibleValue(text="anterior_posterior_gradient")
    apical = PermissibleValue(text="apical")
    basal = PermissibleValue(text="basal")
    central = PermissibleValue(text="central")
    distal = PermissibleValue(text="distal")
    dorsal = PermissibleValue(text="dorsal")
    egg_length = PermissibleValue(text="egg_length")
    gap_expression_pattern = PermissibleValue(text="gap_expression_pattern")
    pair_rule_expression_pattern = PermissibleValue(text="pair_rule_expression_pattern")
    segment_polarity_expression_pattern = PermissibleValue(text="segment_polarity_expression_pattern")
    terminal_expression_pattern = PermissibleValue(text="terminal_expression_pattern")
    gradient = PermissibleValue(text="gradient")

    _defn = EnumDefinition(
        name="SpatialQualifierSet",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "dorso-lateral",
                PermissibleValue(text="dorso-lateral") )

class ExpressionQualifierSet(EnumDefinitionImpl):

    strong = PermissibleValue(text="strong")
    moderate = PermissibleValue(text="moderate")
    faint = PermissibleValue(text="faint")
    endogenous = PermissibleValue(text="endogenous")
    granular = PermissibleValue(text="granular")
    intense = PermissibleValue(text="intense")
    punctate = PermissibleValue(text="punctate")
    uniform = PermissibleValue(text="uniform")
    variable = PermissibleValue(text="variable")
    clusters = PermissibleValue(text="clusters")
    diffuse = PermissibleValue(text="diffuse")
    graded = PermissibleValue(text="graded")
    not_specified = PermissibleValue(text="not_specified")
    patchy = PermissibleValue(text="patchy")
    regionally_restricted = PermissibleValue(text="regionally_restricted")
    scattered = PermissibleValue(text="scattered")
    single_cells = PermissibleValue(text="single_cells")
    spotted = PermissibleValue(text="spotted")
    ubiquitous = PermissibleValue(text="ubiquitous")
    widespread = PermissibleValue(text="widespread")

    _defn = EnumDefinition(
        name="ExpressionQualifierSet",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "non-uniform",
                PermissibleValue(text="non-uniform") )

class TemporalQualifierSet(EnumDefinitionImpl):

    throughout = PermissibleValue(text="throughout",
                                           description="An event that happens from start to end times included in the annotation")
    sometime_during = PermissibleValue(text="sometime_during",
                                                     description="An event that happens during some of the stages included in the annotation, but maybe not all")

    _defn = EnumDefinition(
        name="TemporalQualifierSet",
    )

class ExpressionConditionRelationEnum(EnumDefinitionImpl):

    has_condition = PermissibleValue(text="has_condition")
    induced_by = PermissibleValue(text="induced_by")

    _defn = EnumDefinition(
        name="ExpressionConditionRelationEnum",
    )

class ExpressionStatementTypeEnum(EnumDefinitionImpl):

    expression_summary = PermissibleValue(text="expression_summary",
                                                           description="Free-text that summarizes expression across many annotations, experiments or publictaions.")
    where_expressed_note = PermissibleValue(text="where_expressed_note",
                                                               description="Additional free-text describing the anatomical site of expression in an expression annotation.")
    expression_annotation_note = PermissibleValue(text="expression_annotation_note",
                                                                           description="Additional free-text describing other aspects of an expression annotation. For example, only in the head neurons, only when JNK is activated, etc. Corresponds to note type #1 of AGR-1407.")

    _defn = EnumDefinition(
        name="ExpressionStatementTypeEnum",
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

class VariantStatusEnum(EnumDefinitionImpl):

    public = PermissibleValue(text="public")
    private = PermissibleValue(text="private")

    _defn = EnumDefinition(
        name="VariantStatusEnum",
    )

# Slots
class slots:
    pass

slots.subtype = Slot(uri=ALLIANCE.subtype, name="subtype", curie=ALLIANCE.curie('subtype'),
                   model_uri=ALLIANCE.subtype, domain=AffectedGenomicModel, range=Union[str, "SubtypeValues"])

slots.components = Slot(uri=ALLIANCE.components, name="components", curie=ALLIANCE.curie('components'),
                   model_uri=ALLIANCE.components, domain=AffectedGenomicModel, range=Optional[Union[Union[dict, "AffectedGenomicModelComponent"], List[Union[dict, "AffectedGenomicModelComponent"]]]])

slots.has_allele = Slot(uri=ALLIANCE.has_allele, name="has_allele", curie=ALLIANCE.curie('has_allele'),
                   model_uri=ALLIANCE.has_allele, domain=AffectedGenomicModelComponent, range=Optional[Union[str, AlleleCurie]])

slots.zygosity = Slot(uri=ALLIANCE.zygosity, name="zygosity", curie=ALLIANCE.curie('zygosity'),
                   model_uri=ALLIANCE.zygosity, domain=AffectedGenomicModelComponent, range=Optional[Union[str, "ZygosityValues"]])

slots.sequence_targeting_reagents = Slot(uri=ALLIANCE.sequence_targeting_reagents, name="sequence_targeting_reagents", curie=ALLIANCE.curie('sequence_targeting_reagents'),
                   model_uri=ALLIANCE.sequence_targeting_reagents, domain=AffectedGenomicModel, range=Optional[Union[Union[str, SequenceTargetingReagentCurie], List[Union[str, SequenceTargetingReagentCurie]]]])

slots.parental_populations = Slot(uri=ALLIANCE.parental_populations, name="parental_populations", curie=ALLIANCE.curie('parental_populations'),
                   model_uri=ALLIANCE.parental_populations, domain=AffectedGenomicModel, range=Optional[Union[str, URIorCURIE]])

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

slots.construct_components = Slot(uri=ALLIANCE.construct_components, name="construct_components", curie=ALLIANCE.curie('construct_components'),
                   model_uri=ALLIANCE.construct_components, domain=Construct, range=Optional[Union[Union[str, GenomicEntityCurie], List[Union[str, GenomicEntityCurie]]]])

slots.contains_constructs = Slot(uri=ALLIANCE.contains_constructs, name="contains_constructs", curie=ALLIANCE.curie('contains_constructs'),
                   model_uri=ALLIANCE.contains_constructs, domain=Allele, range=Optional[Union[Union[str, ConstructCurie], List[Union[str, ConstructCurie]]]])

slots.molecular_mutations = Slot(uri=ALLIANCE.molecular_mutations, name="molecular_mutations", curie=ALLIANCE.curie('molecular_mutations'),
                   model_uri=ALLIANCE.molecular_mutations, domain=Allele, range=Optional[Union[str, List[str]]])

slots.mutation_type = Slot(uri=ALLIANCE.mutation_type, name="mutation_type", curie=ALLIANCE.curie('mutation_type'),
                   model_uri=ALLIANCE.mutation_type, domain=Allele, range=Optional[Union[str, SOTermCurie]])

slots.mutation_description = Slot(uri=ALLIANCE.mutation_description, name="mutation_description", curie=ALLIANCE.curie('mutation_description'),
                   model_uri=ALLIANCE.mutation_description, domain=None, range=Optional[str])

slots.functional_impact = Slot(uri=ALLIANCE.functional_impact, name="functional_impact", curie=ALLIANCE.curie('functional_impact'),
                   model_uri=ALLIANCE.functional_impact, domain=Allele, range=Optional[str])

slots.generation_method = Slot(uri=ALLIANCE.generation_method, name="generation_method", curie=ALLIANCE.curie('generation_method'),
                   model_uri=ALLIANCE.generation_method, domain=Allele, range=Optional[str])

slots.associated_references = Slot(uri=ALLIANCE.associated_references, name="associated_references", curie=ALLIANCE.curie('associated_references'),
                   model_uri=ALLIANCE.associated_references, domain=None, range=Optional[Union[Union[dict, AssociatedReference], List[Union[dict, AssociatedReference]]]])

slots.reference_type = Slot(uri=ALLIANCE.reference_type, name="reference_type", curie=ALLIANCE.curie('reference_type'),
                   model_uri=ALLIANCE.reference_type, domain=AssociatedReference, range=Union[str, VocabularyTermName])

slots.origins = Slot(uri=ALLIANCE.origins, name="origins", curie=ALLIANCE.curie('origins'),
                   model_uri=ALLIANCE.origins, domain=Allele, range=Optional[Union[Union[str, AffectedGenomicModelCurie], List[Union[str, AffectedGenomicModelCurie]]]])

slots.germline_transmission_status = Slot(uri=ALLIANCE.germline_transmission_status, name="germline_transmission_status", curie=ALLIANCE.curie('germline_transmission_status'),
                   model_uri=ALLIANCE.germline_transmission_status, domain=Allele, range=Optional[Union[str, VocabularyTermName]])

slots.parent_cell_line = Slot(uri=ALLIANCE.parent_cell_line, name="parent_cell_line", curie=ALLIANCE.curie('parent_cell_line'),
                   model_uri=ALLIANCE.parent_cell_line, domain=Allele, range=Optional[Union[dict, "CellLine"]])

slots.mutant_cell_lines = Slot(uri=ALLIANCE.mutant_cell_lines, name="mutant_cell_lines", curie=ALLIANCE.curie('mutant_cell_lines'),
                   model_uri=ALLIANCE.mutant_cell_lines, domain=Allele, range=Optional[Union[Union[dict, "CellLine"], List[Union[dict, "CellLine"]]]])

slots.embryonic_stem_cell_lines = Slot(uri=ALLIANCE.embryonic_stem_cell_lines, name="embryonic_stem_cell_lines", curie=ALLIANCE.curie('embryonic_stem_cell_lines'),
                   model_uri=ALLIANCE.embryonic_stem_cell_lines, domain=Allele, range=Optional[Union[Union[dict, "CellLine"], List[Union[dict, "CellLine"]]]])

slots.database_status = Slot(uri=ALLIANCE.database_status, name="database_status", curie=ALLIANCE.curie('database_status'),
                   model_uri=ALLIANCE.database_status, domain=None, range=Optional[Union[str, VocabularyTermName]])

slots.inheritence_mode = Slot(uri=ALLIANCE.inheritence_mode, name="inheritence_mode", curie=ALLIANCE.curie('inheritence_mode'),
                   model_uri=ALLIANCE.inheritence_mode, domain=Allele, range=Optional[Union[str, VocabularyTermName]])

slots.in_collection = Slot(uri=ALLIANCE.in_collection, name="in_collection", curie=ALLIANCE.curie('in_collection'),
                   model_uri=ALLIANCE.in_collection, domain=Allele, range=Optional[Union[str, VocabularyTermName]])

slots.transposon_insertion = Slot(uri=ALLIANCE.transposon_insertion, name="transposon_insertion", curie=ALLIANCE.curie('transposon_insertion'),
                   model_uri=ALLIANCE.transposon_insertion, domain=Allele, range=Optional[str])

slots.aberration = Slot(uri=ALLIANCE.aberration, name="aberration", curie=ALLIANCE.curie('aberration'),
                   model_uri=ALLIANCE.aberration, domain=Allele, range=Optional[str])

slots.is_extinct = Slot(uri=ALLIANCE.is_extinct, name="is_extinct", curie=ALLIANCE.curie('is_extinct'),
                   model_uri=ALLIANCE.is_extinct, domain=Allele, range=Optional[Union[bool, Bool]])

slots.sequencing_status = Slot(uri=ALLIANCE.sequencing_status, name="sequencing_status", curie=ALLIANCE.curie('sequencing_status'),
                   model_uri=ALLIANCE.sequencing_status, domain=Variant, range=Optional[Union[str, VocabularyTermName]])

slots.proteins = Slot(uri=ALLIANCE.proteins, name="proteins", curie=ALLIANCE.curie('proteins'),
                   model_uri=ALLIANCE.proteins, domain=None, range=Optional[Union[Union[str, ProteinCurie], List[Union[str, ProteinCurie]]]])

slots.genes = Slot(uri=ALLIANCE.genes, name="genes", curie=ALLIANCE.curie('genes'),
                   model_uri=ALLIANCE.genes, domain=None, range=Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]])

slots.paralogous_genes = Slot(uri=ALLIANCE.paralogous_genes, name="paralogous_genes", curie=ALLIANCE.curie('paralogous_genes'),
                   model_uri=ALLIANCE.paralogous_genes, domain=None, range=Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]])

slots.has_participant = Slot(uri=ALLIANCE.has_participant, name="has_participant", curie=ALLIANCE.curie('has_participant'),
                   model_uri=ALLIANCE.has_participant, domain=None, range=Optional[str])

slots.has_input = Slot(uri=ALLIANCE.has_input, name="has_input", curie=ALLIANCE.curie('has_input'),
                   model_uri=ALLIANCE.has_input, domain=None, range=Optional[str])

slots.has_output = Slot(uri=ALLIANCE.has_output, name="has_output", curie=ALLIANCE.curie('has_output'),
                   model_uri=ALLIANCE.has_output, domain=None, range=Optional[str])

slots.enables = Slot(uri=ALLIANCE.enables, name="enables", curie=ALLIANCE.curie('enables'),
                   model_uri=ALLIANCE.enables, domain=None, range=Optional[str])

slots.designating_laboratory = Slot(uri=ALLIANCE.designating_laboratory, name="designating_laboratory", curie=ALLIANCE.curie('designating_laboratory'),
                   model_uri=ALLIANCE.designating_laboratory, domain=Gene, range=Union[dict, Laboratory])

slots.old_members = Slot(uri=ALLIANCE.old_members, name="old_members", curie=ALLIANCE.curie('old_members'),
                   model_uri=ALLIANCE.old_members, domain=GeneNomenclatureSet, range=Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]])

slots.experiment_type = Slot(uri=ALLIANCE.experiment_type, name="experiment_type", curie=ALLIANCE.curie('experiment_type'),
                   model_uri=ALLIANCE.experiment_type, domain=GeneCollection, range=Optional[Union[str, List[str]]])

slots.text_synonyms = Slot(uri=ALLIANCE.text_synonyms, name="text_synonyms", curie=ALLIANCE.curie('text_synonyms'),
                   model_uri=ALLIANCE.text_synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.member_terms = Slot(uri=ALLIANCE.member_terms, name="member_terms", curie=ALLIANCE.curie('member_terms'),
                   model_uri=ALLIANCE.member_terms, domain=None, range=Optional[Union[Union[str, VocabularyTermName], List[Union[str, VocabularyTermName]]]])

slots.vocabulary_description = Slot(uri=ALLIANCE.vocabulary_description, name="vocabulary_description", curie=ALLIANCE.curie('vocabulary_description'),
                   model_uri=ALLIANCE.vocabulary_description, domain=None, range=Optional[str])

slots.synonym = Slot(uri=ALLIANCE.synonym, name="synonym", curie=ALLIANCE.curie('synonym'),
                   model_uri=ALLIANCE.synonym, domain=None, range=Optional[str])

slots.start = Slot(uri=ALLIANCE.start, name="start", curie=ALLIANCE.curie('start'),
                   model_uri=ALLIANCE.start, domain=None, range=Optional[str])

slots.end = Slot(uri=ALLIANCE.end, name="end", curie=ALLIANCE.curie('end'),
                   model_uri=ALLIANCE.end, domain=None, range=Optional[str])

slots.has_assembly = Slot(uri=ALLIANCE.has_assembly, name="has_assembly", curie=ALLIANCE.curie('has_assembly'),
                   model_uri=ALLIANCE.has_assembly, domain=GenomicLocation, range=Union[str, AssemblyCurie])

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
                   model_uri=ALLIANCE.internal, domain=None, range=Union[bool, Bool])

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

slots.genomic_locations = Slot(uri=ALLIANCE.genomic_locations, name="genomic_locations", curie=ALLIANCE.curie('genomic_locations'),
                   model_uri=ALLIANCE.genomic_locations, domain=GenomicEntity, range=Optional[Union[Union[dict, "GenomicLocation"], List[Union[dict, "GenomicLocation"]]]])

slots.table_key = Slot(uri=ALLIANCE.table_key, name="table_key", curie=ALLIANCE.curie('table_key'),
                   model_uri=ALLIANCE.table_key, domain=None, range=Optional[int])

slots.date_created = Slot(uri=ALLIANCE.date_created, name="date_created", curie=ALLIANCE.curie('date_created'),
                   model_uri=ALLIANCE.date_created, domain=None, range=Optional[Union[str, XSDDate]])

slots.date_updated = Slot(uri=ALLIANCE.date_updated, name="date_updated", curie=ALLIANCE.curie('date_updated'),
                   model_uri=ALLIANCE.date_updated, domain=None, range=Optional[Union[str, XSDDate]])

slots.created_by = Slot(uri=ALLIANCE.created_by, name="created_by", curie=ALLIANCE.curie('created_by'),
                   model_uri=ALLIANCE.created_by, domain=AuditedObject, range=Optional[Union[str, PersonUniqueId]])

slots.updated_by = Slot(uri=ALLIANCE.updated_by, name="updated_by", curie=ALLIANCE.curie('updated_by'),
                   model_uri=ALLIANCE.updated_by, domain=AuditedObject, range=Optional[Union[str, PersonUniqueId]])

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

slots.subject = Slot(uri=ALLIANCE.subject, name="subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.subject, domain=None, range=str)

slots.object = Slot(uri=ALLIANCE.object, name="object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.object, domain=None, range=str)

slots.predicate = Slot(uri=ALLIANCE.predicate, name="predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.predicate, domain=None, range=str)

slots.related_to = Slot(uri=ALLIANCE.related_to, name="related_to", curie=ALLIANCE.curie('related_to'),
                   model_uri=ALLIANCE.related_to, domain=None, range=Optional[Union[str, List[str]]])

slots.belongs_to_expression_experiment = Slot(uri=ALLIANCE.belongs_to_expression_experiment, name="belongs_to_expression_experiment", curie=ALLIANCE.curie('belongs_to_expression_experiment'),
                   model_uri=ALLIANCE.belongs_to_expression_experiment, domain=ExpressionAnnotation, range=Union[str, ExpressionExperimentCurie])

slots.age = Slot(uri=ALLIANCE.age, name="age", curie=ALLIANCE.curie('age'),
                   model_uri=ALLIANCE.age, domain=TemporalContext, range=Optional[str])

slots.anatomical_structure = Slot(uri=ALLIANCE.anatomical_structure, name="anatomical_structure", curie=ALLIANCE.curie('anatomical_structure'),
                   model_uri=ALLIANCE.anatomical_structure, domain=AnatomicalTerm, range=Optional[Union[str, AnatomicalTermCurie]])

slots.anatomical_substructure = Slot(uri=ALLIANCE.anatomical_substructure, name="anatomical_substructure", curie=ALLIANCE.curie('anatomical_substructure'),
                   model_uri=ALLIANCE.anatomical_substructure, domain=AnatomicalTerm, range=Optional[Union[str, AnatomicalTermCurie]])

slots.assay_used = Slot(uri=ALLIANCE.assay_used, name="assay_used", curie=ALLIANCE.curie('assay_used'),
                   model_uri=ALLIANCE.assay_used, domain=ExpressionExperiment, range=Optional[Union[str, MMOTermCurie]])

slots.cellular_component = Slot(uri=ALLIANCE.cellular_component, name="cellular_component", curie=ALLIANCE.curie('cellular_component'),
                   model_uri=ALLIANCE.cellular_component, domain=AnatomicalSite, range=Optional[Union[str, GOTermCurie]])

slots.developmental_stage_start = Slot(uri=ALLIANCE.developmental_stage_start, name="developmental_stage_start", curie=ALLIANCE.curie('developmental_stage_start'),
                   model_uri=ALLIANCE.developmental_stage_start, domain=TemporalContext, range=Optional[Union[str, StageTermCurie]])

slots.developmental_stage_stop = Slot(uri=ALLIANCE.developmental_stage_stop, name="developmental_stage_stop", curie=ALLIANCE.curie('developmental_stage_stop'),
                   model_uri=ALLIANCE.developmental_stage_stop, domain=TemporalContext, range=Optional[Union[str, StageTermCurie]])

slots.expression_qualifiers = Slot(uri=ALLIANCE.expression_qualifiers, name="expression_qualifiers", curie=ALLIANCE.curie('expression_qualifiers'),
                   model_uri=ALLIANCE.expression_qualifiers, domain=ExpressionAnnotation, range=Optional[Union[str, "ExpressionQualifierSet"]])

slots.biological_entity_assayed = Slot(uri=ALLIANCE.biological_entity_assayed, name="biological_entity_assayed", curie=ALLIANCE.curie('biological_entity_assayed'),
                   model_uri=ALLIANCE.biological_entity_assayed, domain=ExpressionExperiment, range=Optional[Union[str, BiologicalEntityCurie]])

slots.image = Slot(uri=ALLIANCE.image, name="image", curie=ALLIANCE.curie('image'),
                   model_uri=ALLIANCE.image, domain=None, range=Optional[Union[str, ImageCurie]])

slots.spatial_qualifiers = Slot(uri=ALLIANCE.spatial_qualifiers, name="spatial_qualifiers", curie=ALLIANCE.curie('spatial_qualifiers'),
                   model_uri=ALLIANCE.spatial_qualifiers, domain=AnatomicalSite, range=Optional[Union[str, "SpatialQualifierSet"]])

slots.reagents_used = Slot(uri=ALLIANCE.reagents_used, name="reagents_used", curie=ALLIANCE.curie('reagents_used'),
                   model_uri=ALLIANCE.reagents_used, domain=ExpressionExperiment, range=Optional[Union[Union[str, ReagentCurie], List[Union[str, ReagentCurie]]]])

slots.specimen_alleles = Slot(uri=ALLIANCE.specimen_alleles, name="specimen_alleles", curie=ALLIANCE.curie('specimen_alleles'),
                   model_uri=ALLIANCE.specimen_alleles, domain=ExpressionExperiment, range=Optional[Union[Union[str, AlleleCurie], List[Union[str, AlleleCurie]]]])

slots.specimen_genomic_model = Slot(uri=ALLIANCE.specimen_genomic_model, name="specimen_genomic_model", curie=ALLIANCE.curie('specimen_genomic_model'),
                   model_uri=ALLIANCE.specimen_genomic_model, domain=ExpressionExperiment, range=Optional[Union[str, AffectedGenomicModelCurie]])

slots.temporal_qualifiers = Slot(uri=ALLIANCE.temporal_qualifiers, name="temporal_qualifiers", curie=ALLIANCE.curie('temporal_qualifiers'),
                   model_uri=ALLIANCE.temporal_qualifiers, domain=TemporalContext, range=Optional[Union[str, "TemporalQualifierSet"]])

slots.when_expressed = Slot(uri=ALLIANCE.when_expressed, name="when_expressed", curie=ALLIANCE.curie('when_expressed'),
                   model_uri=ALLIANCE.when_expressed, domain=ExpressionAnnotation, range=Optional[Union[dict, "TemporalContext"]])

slots.where_expressed = Slot(uri=ALLIANCE.where_expressed, name="where_expressed", curie=ALLIANCE.curie('where_expressed'),
                   model_uri=ALLIANCE.where_expressed, domain=ExpressionAnnotation, range=Optional[Union[dict, "AnatomicalSite"]])

slots.assay_notes = Slot(uri=ALLIANCE.assay_notes, name="assay_notes", curie=ALLIANCE.curie('assay_notes'),
                   model_uri=ALLIANCE.assay_notes, domain=None, range=Optional[str])

slots.gene_type = Slot(uri=ALLIANCE.gene_type, name="gene_type", curie=ALLIANCE.curie('gene_type'),
                   model_uri=ALLIANCE.gene_type, domain=Gene, range=Optional[Union[str, SOTermCurie]])

slots.gene_types_secondary = Slot(uri=ALLIANCE.gene_types_secondary, name="gene_types_secondary", curie=ALLIANCE.curie('gene_types_secondary'),
                   model_uri=ALLIANCE.gene_types_secondary, domain=Gene, range=Optional[Union[Union[str, SOTermCurie], List[Union[str, SOTermCurie]]]])

slots.designating_laboratories = Slot(uri=ALLIANCE.designating_laboratories, name="designating_laboratories", curie=ALLIANCE.curie('designating_laboratories'),
                   model_uri=ALLIANCE.designating_laboratories, domain=Gene, range=Optional[Union[Union[dict, Laboratory], List[Union[dict, Laboratory]]]])

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

slots.allele_ingest_set = Slot(uri=ALLIANCE.allele_ingest_set, name="allele_ingest_set", curie=ALLIANCE.curie('allele_ingest_set'),
                   model_uri=ALLIANCE.allele_ingest_set, domain=Ingest, range=Optional[Union[Dict[Union[str, AlleleCurie], Union[dict, Allele]], List[Union[dict, Allele]]]])

slots.agm_ingest_set = Slot(uri=ALLIANCE.agm_ingest_set, name="agm_ingest_set", curie=ALLIANCE.curie('agm_ingest_set'),
                   model_uri=ALLIANCE.agm_ingest_set, domain=Ingest, range=Optional[Union[Dict[Union[str, AffectedGenomicModelCurie], Union[dict, AffectedGenomicModel]], List[Union[dict, AffectedGenomicModel]]]])

slots.sqtr_ingest_set = Slot(uri=ALLIANCE.sqtr_ingest_set, name="sqtr_ingest_set", curie=ALLIANCE.curie('sqtr_ingest_set'),
                   model_uri=ALLIANCE.sqtr_ingest_set, domain=Ingest, range=Optional[Union[Dict[Union[str, SequenceTargetingReagentCurie], Union[dict, SequenceTargetingReagent]], List[Union[dict, SequenceTargetingReagent]]]])

slots.variant_ingest_set = Slot(uri=ALLIANCE.variant_ingest_set, name="variant_ingest_set", curie=ALLIANCE.curie('variant_ingest_set'),
                   model_uri=ALLIANCE.variant_ingest_set, domain=Ingest, range=Optional[Union[Dict[Union[str, VariantCurie], Union[dict, "Variant"]], List[Union[dict, "Variant"]]]])

slots.allele_variant_association_ingest_set = Slot(uri=ALLIANCE.allele_variant_association_ingest_set, name="allele_variant_association_ingest_set", curie=ALLIANCE.curie('allele_variant_association_ingest_set'),
                   model_uri=ALLIANCE.allele_variant_association_ingest_set, domain=Ingest, range=Optional[Union[Union[dict, AlleleVariantAssociation], List[Union[dict, AlleleVariantAssociation]]]])

slots.disease_allele_ingest_set = Slot(uri=ALLIANCE.disease_allele_ingest_set, name="disease_allele_ingest_set", curie=ALLIANCE.curie('disease_allele_ingest_set'),
                   model_uri=ALLIANCE.disease_allele_ingest_set, domain=Ingest, range=Optional[Union[Union[dict, "AlleleDiseaseAnnotation"], List[Union[dict, "AlleleDiseaseAnnotation"]]]])

slots.disease_agm_ingest_set = Slot(uri=ALLIANCE.disease_agm_ingest_set, name="disease_agm_ingest_set", curie=ALLIANCE.curie('disease_agm_ingest_set'),
                   model_uri=ALLIANCE.disease_agm_ingest_set, domain=Ingest, range=Optional[Union[Union[dict, "AGMDiseaseAnnotation"], List[Union[dict, "AGMDiseaseAnnotation"]]]])

slots.disease_gene_ingest_set = Slot(uri=ALLIANCE.disease_gene_ingest_set, name="disease_gene_ingest_set", curie=ALLIANCE.curie('disease_gene_ingest_set'),
                   model_uri=ALLIANCE.disease_gene_ingest_set, domain=Ingest, range=Optional[Union[Union[dict, "GeneDiseaseAnnotation"], List[Union[dict, "GeneDiseaseAnnotation"]]]])

slots.gene_ingest_set = Slot(uri=ALLIANCE.gene_ingest_set, name="gene_ingest_set", curie=ALLIANCE.curie('gene_ingest_set'),
                   model_uri=ALLIANCE.gene_ingest_set, domain=Ingest, range=Optional[Union[Dict[Union[str, GeneCurie], Union[dict, Gene]], List[Union[dict, Gene]]]])

slots.object_set = Slot(uri=ALLIANCE.object_set, name="object_set", curie=ALLIANCE.curie('object_set'),
                   model_uri=ALLIANCE.object_set, domain=Ingest, range=Optional[Union[str, List[str]]])

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

slots.condition_anatomy = Slot(uri=ALLIANCE.condition_anatomy, name="condition_anatomy", curie=ALLIANCE.curie('condition_anatomy'),
                   model_uri=ALLIANCE.condition_anatomy, domain=ExperimentalCondition, range=Optional[Union[str, AnatomicalTermCurie]])

slots.condition_chemical = Slot(uri=ALLIANCE.condition_chemical, name="condition_chemical", curie=ALLIANCE.curie('condition_chemical'),
                   model_uri=ALLIANCE.condition_chemical, domain=ExperimentalCondition, range=Optional[Union[str, OntologyTermCurie]])

slots.condition_class = Slot(uri=ALLIANCE.condition_class, name="condition_class", curie=ALLIANCE.curie('condition_class'),
                   model_uri=ALLIANCE.condition_class, domain=ExperimentalCondition, range=Union[str, ZECOTermCurie])

slots.condition_gene_ontology = Slot(uri=ALLIANCE.condition_gene_ontology, name="condition_gene_ontology", curie=ALLIANCE.curie('condition_gene_ontology'),
                   model_uri=ALLIANCE.condition_gene_ontology, domain=ExperimentalCondition, range=Optional[Union[str, GOTermCurie]])

slots.condition_id = Slot(uri=ALLIANCE.condition_id, name="condition_id", curie=ALLIANCE.curie('condition_id'),
                   model_uri=ALLIANCE.condition_id, domain=ExperimentalCondition, range=Optional[Union[str, ExperimentalConditionOntologyTermCurie]])

slots.condition_quantity = Slot(uri=ALLIANCE.condition_quantity, name="condition_quantity", curie=ALLIANCE.curie('condition_quantity'),
                   model_uri=ALLIANCE.condition_quantity, domain=ExperimentalCondition, range=Optional[str])

slots.condition_statement = Slot(uri=ALLIANCE.condition_statement, name="condition_statement", curie=ALLIANCE.curie('condition_statement'),
                   model_uri=ALLIANCE.condition_statement, domain=ExperimentalCondition, range=str)

slots.condition_summary = Slot(uri=ALLIANCE.condition_summary, name="condition_summary", curie=ALLIANCE.curie('condition_summary'),
                   model_uri=ALLIANCE.condition_summary, domain=ExperimentalCondition, range=Optional[str])

slots.condition_free_text = Slot(uri=ALLIANCE.condition_free_text, name="condition_free_text", curie=ALLIANCE.curie('condition_free_text'),
                   model_uri=ALLIANCE.condition_free_text, domain=ExperimentalCondition, range=Optional[str])

slots.condition_taxon = Slot(uri=ALLIANCE.condition_taxon, name="condition_taxon", curie=ALLIANCE.curie('condition_taxon'),
                   model_uri=ALLIANCE.condition_taxon, domain=ExperimentalCondition, range=Optional[Union[str, NCBITaxonTermCurie]])

slots.condition_relations = Slot(uri=ALLIANCE.condition_relations, name="condition_relations", curie=ALLIANCE.curie('condition_relations'),
                   model_uri=ALLIANCE.condition_relations, domain=None, range=Optional[Union[Union[dict, ConditionRelation], List[Union[dict, ConditionRelation]]]])

slots.condition_relation_type = Slot(uri=ALLIANCE.condition_relation_type, name="condition_relation_type", curie=ALLIANCE.curie('condition_relation_type'),
                   model_uri=ALLIANCE.condition_relation_type, domain=ConditionRelation, range=Optional[Union[str, VocabularyTermName]])

slots.conditions = Slot(uri=ALLIANCE.conditions, name="conditions", curie=ALLIANCE.curie('conditions'),
                   model_uri=ALLIANCE.conditions, domain=None, range=Optional[Union[Union[dict, ExperimentalCondition], List[Union[dict, ExperimentalCondition]]]])

slots.inferred_gene = Slot(uri=ALLIANCE.inferred_gene, name="inferred_gene", curie=ALLIANCE.curie('inferred_gene'),
                   model_uri=ALLIANCE.inferred_gene, domain=None, range=Optional[Union[str, GeneCurie]])

slots.inferred_allele = Slot(uri=ALLIANCE.inferred_allele, name="inferred_allele", curie=ALLIANCE.curie('inferred_allele'),
                   model_uri=ALLIANCE.inferred_allele, domain=None, range=Optional[Union[str, AlleleCurie]])

slots.asserted_gene = Slot(uri=ALLIANCE.asserted_gene, name="asserted_gene", curie=ALLIANCE.curie('asserted_gene'),
                   model_uri=ALLIANCE.asserted_gene, domain=None, range=Optional[Union[str, GeneCurie]])

slots.asserted_allele = Slot(uri=ALLIANCE.asserted_allele, name="asserted_allele", curie=ALLIANCE.curie('asserted_allele'),
                   model_uri=ALLIANCE.asserted_allele, domain=None, range=Optional[Union[str, AlleleCurie]])

slots.disease_qualifiers = Slot(uri=ALLIANCE.disease_qualifiers, name="disease_qualifiers", curie=ALLIANCE.curie('disease_qualifiers'),
                   model_uri=ALLIANCE.disease_qualifiers, domain=DiseaseAnnotation, range=Optional[Union[Union[str, VocabularyTermName], List[Union[str, VocabularyTermName]]]])

slots.genetic_sex = Slot(uri=ALLIANCE.genetic_sex, name="genetic_sex", curie=ALLIANCE.curie('genetic_sex'),
                   model_uri=ALLIANCE.genetic_sex, domain=None, range=Optional[Union[str, VocabularyTermName]])

slots.sgd_strain_background = Slot(uri=ALLIANCE.sgd_strain_background, name="sgd_strain_background", curie=ALLIANCE.curie('sgd_strain_background'),
                   model_uri=ALLIANCE.sgd_strain_background, domain=None, range=Optional[Union[str, AffectedGenomicModelCurie]])

slots.annotation_type = Slot(uri=ALLIANCE.annotation_type, name="annotation_type", curie=ALLIANCE.curie('annotation_type'),
                   model_uri=ALLIANCE.annotation_type, domain=None, range=Optional[Union[str, VocabularyTermName]])

slots.disease_genetic_modifier = Slot(uri=ALLIANCE.disease_genetic_modifier, name="disease_genetic_modifier", curie=ALLIANCE.curie('disease_genetic_modifier'),
                   model_uri=ALLIANCE.disease_genetic_modifier, domain=None, range=Optional[Union[str, BiologicalEntityCurie]])

slots.disease_genetic_modifier_relation = Slot(uri=ALLIANCE.disease_genetic_modifier_relation, name="disease_genetic_modifier_relation", curie=ALLIANCE.curie('disease_genetic_modifier_relation'),
                   model_uri=ALLIANCE.disease_genetic_modifier_relation, domain=None, range=Optional[Union[str, VocabularyTermName]])

slots.phenotype_term = Slot(uri=ALLIANCE.phenotype_term, name="phenotype_term", curie=ALLIANCE.curie('phenotype_term'),
                   model_uri=ALLIANCE.phenotype_term, domain=None, range=Optional[Union[str, PhenotypeTermCurie]])

slots.with = Slot(uri=ALLIANCE.with, name="with", curie=ALLIANCE.curie('with'),
                   model_uri=ALLIANCE.with, domain=None, range=Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]])

slots.handle = Slot(uri=ALLIANCE.handle, name="handle", curie=ALLIANCE.curie('handle'),
                   model_uri=ALLIANCE.handle, domain=None, range=Optional[str])

slots.antibody_target_genes = Slot(uri=ALLIANCE.antibody_target_genes, name="antibody_target_genes", curie=ALLIANCE.curie('antibody_target_genes'),
                   model_uri=ALLIANCE.antibody_target_genes, domain=Antibody, range=Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]])

slots.antigen_taxon = Slot(uri=ALLIANCE.antigen_taxon, name="antigen_taxon", curie=ALLIANCE.curie('antigen_taxon'),
                   model_uri=ALLIANCE.antigen_taxon, domain=Antibody, range=Optional[Union[str, NCBITaxonTermCurie]])

slots.clonality = Slot(uri=ALLIANCE.clonality, name="clonality", curie=ALLIANCE.curie('clonality'),
                   model_uri=ALLIANCE.clonality, domain=Antibody, range=Union[str, "AntibodyClonalitySet"])

slots.heavy_chain_isotype = Slot(uri=ALLIANCE.heavy_chain_isotype, name="heavy_chain_isotype", curie=ALLIANCE.curie('heavy_chain_isotype'),
                   model_uri=ALLIANCE.heavy_chain_isotype, domain=Antibody, range=Optional[Union[str, "HeavyChainIsotypeSet"]])

slots.light_chain_isotype = Slot(uri=ALLIANCE.light_chain_isotype, name="light_chain_isotype", curie=ALLIANCE.curie('light_chain_isotype'),
                   model_uri=ALLIANCE.light_chain_isotype, domain=Antibody, range=Optional[Union[str, "LightChainIsotypeSet"]])

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

slots.vep_impact = Slot(uri=ALLIANCE.vep_impact, name="vep_impact", curie=ALLIANCE.curie('vep_impact'),
                   model_uri=ALLIANCE.vep_impact, domain=None, range=Optional[str])

slots.vep_consequence = Slot(uri=ALLIANCE.vep_consequence, name="vep_consequence", curie=ALLIANCE.curie('vep_consequence'),
                   model_uri=ALLIANCE.vep_consequence, domain=None, range=Optional[Union[str, "VepConsequenceLevels"]])

slots.polyphen_score = Slot(uri=ALLIANCE.polyphen_score, name="polyphen_score", curie=ALLIANCE.curie('polyphen_score'),
                   model_uri=ALLIANCE.polyphen_score, domain=VariantGeneConsequence, range=Optional[float])

slots.polyphen_prediction = Slot(uri=ALLIANCE.polyphen_prediction, name="polyphen_prediction", curie=ALLIANCE.curie('polyphen_prediction'),
                   model_uri=ALLIANCE.polyphen_prediction, domain=None, range=Optional[Union[str, "PolyphenPredictionLevels"]])

slots.sift_score = Slot(uri=ALLIANCE.sift_score, name="sift_score", curie=ALLIANCE.curie('sift_score'),
                   model_uri=ALLIANCE.sift_score, domain=VariantGeneConsequence, range=Optional[float])

slots.sift_prediction = Slot(uri=ALLIANCE.sift_prediction, name="sift_prediction", curie=ALLIANCE.curie('sift_prediction'),
                   model_uri=ALLIANCE.sift_prediction, domain=None, range=Optional[Union[str, "SiftPredictionLevels"]])

slots.amino_acid_reference = Slot(uri=ALLIANCE.amino_acid_reference, name="amino_acid_reference", curie=ALLIANCE.curie('amino_acid_reference'),
                   model_uri=ALLIANCE.amino_acid_reference, domain=VariantTranscriptConsequence, range=Optional[str])

slots.amino_acid_variant = Slot(uri=ALLIANCE.amino_acid_variant, name="amino_acid_variant", curie=ALLIANCE.curie('amino_acid_variant'),
                   model_uri=ALLIANCE.amino_acid_variant, domain=VariantTranscriptConsequence, range=Optional[str])

slots.codon_reference = Slot(uri=ALLIANCE.codon_reference, name="codon_reference", curie=ALLIANCE.curie('codon_reference'),
                   model_uri=ALLIANCE.codon_reference, domain=VariantTranscriptConsequence, range=Optional[str])

slots.codon_variant = Slot(uri=ALLIANCE.codon_variant, name="codon_variant", curie=ALLIANCE.curie('codon_variant'),
                   model_uri=ALLIANCE.codon_variant, domain=VariantTranscriptConsequence, range=Optional[str])

slots.cdna_start = Slot(uri=ALLIANCE.cdna_start, name="cdna_start", curie=ALLIANCE.curie('cdna_start'),
                   model_uri=ALLIANCE.cdna_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.cdna_end = Slot(uri=ALLIANCE.cdna_end, name="cdna_end", curie=ALLIANCE.curie('cdna_end'),
                   model_uri=ALLIANCE.cdna_end, domain=VariantTranscriptConsequence, range=Optional[int])

slots.cds_start = Slot(uri=ALLIANCE.cds_start, name="cds_start", curie=ALLIANCE.curie('cds_start'),
                   model_uri=ALLIANCE.cds_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.cds_end = Slot(uri=ALLIANCE.cds_end, name="cds_end", curie=ALLIANCE.curie('cds_end'),
                   model_uri=ALLIANCE.cds_end, domain=VariantTranscriptConsequence, range=Optional[int])

slots.protein_start = Slot(uri=ALLIANCE.protein_start, name="protein_start", curie=ALLIANCE.curie('protein_start'),
                   model_uri=ALLIANCE.protein_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.protein_end = Slot(uri=ALLIANCE.protein_end, name="protein_end", curie=ALLIANCE.curie('protein_end'),
                   model_uri=ALLIANCE.protein_end, domain=VariantTranscriptConsequence, range=Optional[int])

slots.hgvs_protein_nomenclature = Slot(uri=ALLIANCE.hgvs_protein_nomenclature, name="hgvs_protein_nomenclature", curie=ALLIANCE.curie('hgvs_protein_nomenclature'),
                   model_uri=ALLIANCE.hgvs_protein_nomenclature, domain=VariantTranscriptConsequence, range=Optional[str])

slots.hgvs_coding_nomenclature = Slot(uri=ALLIANCE.hgvs_coding_nomenclature, name="hgvs_coding_nomenclature", curie=ALLIANCE.curie('hgvs_coding_nomenclature'),
                   model_uri=ALLIANCE.hgvs_coding_nomenclature, domain=VariantTranscriptConsequence, range=Optional[str])

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
                   model_uri=ALLIANCE.variant_locations, domain=Variant, range=Union[Union[dict, "VariantLocation"], List[Union[dict, "VariantLocation"]]])

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

slots.Person_unique_id = Slot(uri=ALLIANCE.unique_id, name="Person_unique_id", curie=ALLIANCE.curie('unique_id'),
                   model_uri=ALLIANCE.Person_unique_id, domain=Person, range=Union[str, PersonUniqueId])

slots.LoggedInPerson_okta_id = Slot(uri=ALLIANCE.okta_id, name="LoggedInPerson_okta_id", curie=ALLIANCE.curie('okta_id'),
                   model_uri=ALLIANCE.LoggedInPerson_okta_id, domain=LoggedInPerson, range=str)

slots.LoggedInPerson_okta_email = Slot(uri=ALLIANCE.okta_email, name="LoggedInPerson_okta_email", curie=ALLIANCE.curie('okta_email'),
                   model_uri=ALLIANCE.LoggedInPerson_okta_email, domain=LoggedInPerson, range=str)

slots.Allele_synonyms = Slot(uri=ALLIANCE.synonyms, name="Allele_synonyms", curie=ALLIANCE.curie('synonyms'),
                   model_uri=ALLIANCE.Allele_synonyms, domain=Allele, range=Optional[Union[Union[dict, "Synonym"], List[Union[dict, "Synonym"]]]])

slots.Allele_germline_transmission_status = Slot(uri=ALLIANCE.germline_transmission_status, name="Allele_germline_transmission_status", curie=ALLIANCE.curie('germline_transmission_status'),
                   model_uri=ALLIANCE.Allele_germline_transmission_status, domain=Allele, range=Optional[Union[str, VocabularyTermName]])

slots.Allele_parent_cell_line = Slot(uri=ALLIANCE.parent_cell_line, name="Allele_parent_cell_line", curie=ALLIANCE.curie('parent_cell_line'),
                   model_uri=ALLIANCE.Allele_parent_cell_line, domain=Allele, range=Optional[Union[dict, "CellLine"]])

slots.Allele_mutant_cell_lines = Slot(uri=ALLIANCE.mutant_cell_lines, name="Allele_mutant_cell_lines", curie=ALLIANCE.curie('mutant_cell_lines'),
                   model_uri=ALLIANCE.Allele_mutant_cell_lines, domain=Allele, range=Optional[Union[Union[dict, "CellLine"], List[Union[dict, "CellLine"]]]])

slots.Allele_embryonic_stem_cell_lines = Slot(uri=ALLIANCE.embryonic_stem_cell_lines, name="Allele_embryonic_stem_cell_lines", curie=ALLIANCE.curie('embryonic_stem_cell_lines'),
                   model_uri=ALLIANCE.Allele_embryonic_stem_cell_lines, domain=Allele, range=Optional[Union[Union[dict, "CellLine"], List[Union[dict, "CellLine"]]]])

slots.Allele_transposon_insertion = Slot(uri=ALLIANCE.transposon_insertion, name="Allele_transposon_insertion", curie=ALLIANCE.curie('transposon_insertion'),
                   model_uri=ALLIANCE.Allele_transposon_insertion, domain=Allele, range=Optional[str])

slots.Allele_aberration = Slot(uri=ALLIANCE.aberration, name="Allele_aberration", curie=ALLIANCE.curie('aberration'),
                   model_uri=ALLIANCE.Allele_aberration, domain=Allele, range=Optional[str])

slots.Allele_name = Slot(uri=ALLIANCE.name, name="Allele_name", curie=ALLIANCE.curie('name'),
                   model_uri=ALLIANCE.Allele_name, domain=Allele, range=str)

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

slots.Construct_curie = Slot(uri=ALLIANCE.curie, name="Construct_curie", curie=ALLIANCE.curie('curie'),
                   model_uri=ALLIANCE.Construct_curie, domain=Construct, range=Union[str, ConstructCurie])

slots.Construct_name = Slot(uri=ALLIANCE.name, name="Construct_name", curie=ALLIANCE.curie('name'),
                   model_uri=ALLIANCE.Construct_name, domain=Construct, range=str)

slots.SequenceTargetingReagent_curie = Slot(uri=ALLIANCE.curie, name="SequenceTargetingReagent_curie", curie=ALLIANCE.curie('curie'),
                   model_uri=ALLIANCE.SequenceTargetingReagent_curie, domain=SequenceTargetingReagent, range=Union[str, SequenceTargetingReagentCurie])

slots.SequenceTargetingReagent_name = Slot(uri=ALLIANCE.name, name="SequenceTargetingReagent_name", curie=ALLIANCE.curie('name'),
                   model_uri=ALLIANCE.SequenceTargetingReagent_name, domain=SequenceTargetingReagent, range=str)

slots.SequenceTargetingReagentToGeneAssociation_predicate = Slot(uri=ALLIANCE.predicate, name="SequenceTargetingReagentToGeneAssociation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.SequenceTargetingReagentToGeneAssociation_predicate, domain=SequenceTargetingReagentToGeneAssociation, range=Union[str, "SqtrRelationEnum"])

slots.SequenceTargetingReagentToGeneAssociation_subject = Slot(uri=ALLIANCE.subject, name="SequenceTargetingReagentToGeneAssociation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.SequenceTargetingReagentToGeneAssociation_subject, domain=SequenceTargetingReagentToGeneAssociation, range=Union[str, SequenceTargetingReagentCurie])

slots.SequenceTargetingReagentToGeneAssociation_object = Slot(uri=ALLIANCE.object, name="SequenceTargetingReagentToGeneAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.SequenceTargetingReagentToGeneAssociation_object, domain=SequenceTargetingReagentToGeneAssociation, range=Union[str, GeneCurie])

slots.ConstructComponentAssociation_predicate = Slot(uri=ALLIANCE.predicate, name="ConstructComponentAssociation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.ConstructComponentAssociation_predicate, domain=ConstructComponentAssociation, range=Union[str, "ConstructComponentRelationEnum"])

slots.ConstructComponentAssociation_subject = Slot(uri=ALLIANCE.subject, name="ConstructComponentAssociation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.ConstructComponentAssociation_subject, domain=ConstructComponentAssociation, range=Union[str, ConstructCurie])

slots.ConstructComponentAssociation_object = Slot(uri=ALLIANCE.object, name="ConstructComponentAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.ConstructComponentAssociation_object, domain=ConstructComponentAssociation, range=Union[str, ConstructComponentCurie])

slots.GeneToPathwayAssociation_predicate = Slot(uri=ALLIANCE.predicate, name="GeneToPathwayAssociation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.GeneToPathwayAssociation_predicate, domain=GeneToPathwayAssociation, range=str)

slots.GeneToPathwayAssociation_subject = Slot(uri=ALLIANCE.subject, name="GeneToPathwayAssociation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.GeneToPathwayAssociation_subject, domain=GeneToPathwayAssociation, range=Union[str, GeneCurie])

slots.GeneToPathwayAssociation_object = Slot(uri=ALLIANCE.object, name="GeneToPathwayAssociation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.GeneToPathwayAssociation_object, domain=GeneToPathwayAssociation, range=Union[str, PathwayCurie])

slots.VocabularyTerm_name = Slot(uri=ALLIANCE.name, name="VocabularyTerm_name", curie=ALLIANCE.curie('name'),
                   model_uri=ALLIANCE.VocabularyTerm_name, domain=VocabularyTerm, range=Union[str, VocabularyTermName])

slots.Vocabulary_name = Slot(uri=ALLIANCE.name, name="Vocabulary_name", curie=ALLIANCE.curie('name'),
                   model_uri=ALLIANCE.Vocabulary_name, domain=Vocabulary, range=Union[str, VocabularyName])

slots.BiologicalEntity_taxon = Slot(uri=ALLIANCE.taxon, name="BiologicalEntity_taxon", curie=ALLIANCE.curie('taxon'),
                   model_uri=ALLIANCE.BiologicalEntity_taxon, domain=BiologicalEntity, range=Union[str, NCBITaxonTermCurie])

slots.Note_free_text = Slot(uri=ALLIANCE.free_text, name="Note_free_text", curie=ALLIANCE.curie('free_text'),
                   model_uri=ALLIANCE.Note_free_text, domain=Note, range=str)

slots.Note_note_type = Slot(uri=ALLIANCE.note_type, name="Note_note_type", curie=ALLIANCE.curie('note_type'),
                   model_uri=ALLIANCE.Note_note_type, domain=Note, range=Union[str, VocabularyTermName])

slots.EntitySynonym_object = Slot(uri=ALLIANCE.object, name="EntitySynonym_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.EntitySynonym_object, domain=EntitySynonym, range=Union[dict, Synonym])

slots.EntitySynonym_predicate = Slot(uri=ALLIANCE.predicate, name="EntitySynonym_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.EntitySynonym_predicate, domain=EntitySynonym, range=Union[str, "EntitySynonymTypeSet"])

slots.EntitySynonym_references = Slot(uri=ALLIANCE.references, name="EntitySynonym_references", curie=ALLIANCE.curie('references'),
                   model_uri=ALLIANCE.EntitySynonym_references, domain=EntitySynonym, range=Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]])

slots.GenomicLocation_subject = Slot(uri=ALLIANCE.subject, name="GenomicLocation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.GenomicLocation_subject, domain=GenomicLocation, range=Union[str, GenomicEntityCurie])

slots.GenomicLocation_object = Slot(uri=ALLIANCE.object, name="GenomicLocation_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.GenomicLocation_object, domain=GenomicLocation, range=Union[str, ChromosomeCurie])

slots.ExpressionAnnotation_associated_with_figure = Slot(uri=ALLIANCE.associated_with_figure, name="ExpressionAnnotation_associated_with_figure", curie=ALLIANCE.curie('associated_with_figure'),
                   model_uri=ALLIANCE.ExpressionAnnotation_associated_with_figure, domain=ExpressionAnnotation, range=Optional[Union[Union[str, FigureCurie], List[Union[str, FigureCurie]]]])

slots.ExpressionAnnotationImagePane_subject = Slot(uri=ALLIANCE.subject, name="ExpressionAnnotationImagePane_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.ExpressionAnnotationImagePane_subject, domain=ExpressionAnnotationImagePane, range=Union[dict, ExpressionAnnotation])

slots.ExpressionAnnotationImagePane_object = Slot(uri=ALLIANCE.object, name="ExpressionAnnotationImagePane_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.ExpressionAnnotationImagePane_object, domain=ExpressionAnnotationImagePane, range=Union[dict, "ImagePane"])

slots.GeneExpressionStatement_statement_subject = Slot(uri=ALLIANCE.statement_subject, name="GeneExpressionStatement_statement_subject", curie=ALLIANCE.curie('statement_subject'),
                   model_uri=ALLIANCE.GeneExpressionStatement_statement_subject, domain=GeneExpressionStatement, range=Optional[Union[str, GeneCurie]])

slots.GeneExpressionStatement_statement_type = Slot(uri=ALLIANCE.statement_type, name="GeneExpressionStatement_statement_type", curie=ALLIANCE.curie('statement_type'),
                   model_uri=ALLIANCE.GeneExpressionStatement_statement_type, domain=GeneExpressionStatement, range=Optional[Union[str, "ExpressionStatementTypeEnum"]])

slots.ExpressionExperimentStatement_statement_subject = Slot(uri=ALLIANCE.statement_subject, name="ExpressionExperimentStatement_statement_subject", curie=ALLIANCE.curie('statement_subject'),
                   model_uri=ALLIANCE.ExpressionExperimentStatement_statement_subject, domain=ExpressionExperimentStatement, range=Optional[Union[str, ExpressionExperimentCurie]])

slots.ExpressionAnnotationStatement_statement_subject = Slot(uri=ALLIANCE.statement_subject, name="ExpressionAnnotationStatement_statement_subject", curie=ALLIANCE.curie('statement_subject'),
                   model_uri=ALLIANCE.ExpressionAnnotationStatement_statement_subject, domain=ExpressionAnnotationStatement, range=Optional[Union[dict, ExpressionAnnotation]])

slots.ExpressionAnnotationStatement_statement_type = Slot(uri=ALLIANCE.statement_type, name="ExpressionAnnotationStatement_statement_type", curie=ALLIANCE.curie('statement_type'),
                   model_uri=ALLIANCE.ExpressionAnnotationStatement_statement_type, domain=ExpressionAnnotationStatement, range=Optional[Union[str, "ExpressionStatementTypeEnum"]])

slots.Gene_symbol = Slot(uri=ALLIANCE.symbol, name="Gene_symbol", curie=ALLIANCE.curie('symbol'),
                   model_uri=ALLIANCE.Gene_symbol, domain=Gene, range=str)

slots.Gene_related_notes = Slot(uri=ALLIANCE.related_notes, name="Gene_related_notes", curie=ALLIANCE.curie('related_notes'),
                   model_uri=ALLIANCE.Gene_related_notes, domain=Gene, range=Optional[Union[Union[dict, Note], List[Union[dict, Note]]]])

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

slots.OntologyTerm_definition = Slot(uri=ALLIANCE.definition, name="OntologyTerm_definition", curie=ALLIANCE.curie('definition'),
                   model_uri=ALLIANCE.OntologyTerm_definition, domain=OntologyTerm, range=Optional[str])

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
                   model_uri=ALLIANCE.PhenotypeAnnotation_date_created, domain=PhenotypeAnnotation, range=Union[str, XSDDate])

slots.GenePhenotypeAnnotation_subject = Slot(uri=ALLIANCE.subject, name="GenePhenotypeAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.GenePhenotypeAnnotation_subject, domain=GenePhenotypeAnnotation, range=Union[str, GeneCurie])

slots.AllelePhenotypeAnnotation_subject = Slot(uri=ALLIANCE.subject, name="AllelePhenotypeAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.AllelePhenotypeAnnotation_subject, domain=AllelePhenotypeAnnotation, range=Union[str, AlleleCurie])

slots.AllelePhenotypeAnnotation_inferred_gene = Slot(uri=ALLIANCE.inferred_gene, name="AllelePhenotypeAnnotation_inferred_gene", curie=ALLIANCE.curie('inferred_gene'),
                   model_uri=ALLIANCE.AllelePhenotypeAnnotation_inferred_gene, domain=AllelePhenotypeAnnotation, range=Optional[Union[str, GeneCurie]])

slots.AllelePhenotypeAnnotation_asserted_gene = Slot(uri=ALLIANCE.asserted_gene, name="AllelePhenotypeAnnotation_asserted_gene", curie=ALLIANCE.curie('asserted_gene'),
                   model_uri=ALLIANCE.AllelePhenotypeAnnotation_asserted_gene, domain=AllelePhenotypeAnnotation, range=Optional[Union[str, GeneCurie]])

slots.AllelePhenotypeAnnotation_asserted_allele = Slot(uri=ALLIANCE.asserted_allele, name="AllelePhenotypeAnnotation_asserted_allele", curie=ALLIANCE.curie('asserted_allele'),
                   model_uri=ALLIANCE.AllelePhenotypeAnnotation_asserted_allele, domain=AllelePhenotypeAnnotation, range=Optional[Union[str, AlleleCurie]])

slots.AGMPhenotypeAnnotation_subject = Slot(uri=ALLIANCE.subject, name="AGMPhenotypeAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.AGMPhenotypeAnnotation_subject, domain=AGMPhenotypeAnnotation, range=Union[str, AffectedGenomicModelCurie])

slots.AGMPhenotypeAnnotation_inferred_gene = Slot(uri=ALLIANCE.inferred_gene, name="AGMPhenotypeAnnotation_inferred_gene", curie=ALLIANCE.curie('inferred_gene'),
                   model_uri=ALLIANCE.AGMPhenotypeAnnotation_inferred_gene, domain=AGMPhenotypeAnnotation, range=Optional[Union[str, GeneCurie]])

slots.AGMPhenotypeAnnotation_inferred_allele = Slot(uri=ALLIANCE.inferred_allele, name="AGMPhenotypeAnnotation_inferred_allele", curie=ALLIANCE.curie('inferred_allele'),
                   model_uri=ALLIANCE.AGMPhenotypeAnnotation_inferred_allele, domain=AGMPhenotypeAnnotation, range=Optional[Union[str, AlleleCurie]])

slots.AGMPhenotypeAnnotation_asserted_gene = Slot(uri=ALLIANCE.asserted_gene, name="AGMPhenotypeAnnotation_asserted_gene", curie=ALLIANCE.curie('asserted_gene'),
                   model_uri=ALLIANCE.AGMPhenotypeAnnotation_asserted_gene, domain=AGMPhenotypeAnnotation, range=Optional[Union[str, GeneCurie]])

slots.AGMPhenotypeAnnotation_asserted_allele = Slot(uri=ALLIANCE.asserted_allele, name="AGMPhenotypeAnnotation_asserted_allele", curie=ALLIANCE.curie('asserted_allele'),
                   model_uri=ALLIANCE.AGMPhenotypeAnnotation_asserted_allele, domain=AGMPhenotypeAnnotation, range=Optional[Union[str, AlleleCurie]])

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
                   model_uri=ALLIANCE.DiseaseAnnotation_data_provider, domain=DiseaseAnnotation, range=str)

slots.DiseaseAnnotation_annotation_type = Slot(uri=ALLIANCE.annotation_type, name="DiseaseAnnotation_annotation_type", curie=ALLIANCE.curie('annotation_type'),
                   model_uri=ALLIANCE.DiseaseAnnotation_annotation_type, domain=DiseaseAnnotation, range=Optional[Union[str, VocabularyTermName]])

slots.DiseaseAnnotation_with = Slot(uri=ALLIANCE.with, name="DiseaseAnnotation_with", curie=ALLIANCE.curie('with'),
                   model_uri=ALLIANCE.DiseaseAnnotation_with, domain=DiseaseAnnotation, range=Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]])

slots.DiseaseAnnotation_single_reference = Slot(uri=ALLIANCE.single_reference, name="DiseaseAnnotation_single_reference", curie=ALLIANCE.curie('single_reference'),
                   model_uri=ALLIANCE.DiseaseAnnotation_single_reference, domain=DiseaseAnnotation, range=Union[str, ReferenceCurie])

slots.DiseaseAnnotation_evidence_codes = Slot(uri=ALLIANCE.evidence_codes, name="DiseaseAnnotation_evidence_codes", curie=ALLIANCE.curie('evidence_codes'),
                   model_uri=ALLIANCE.DiseaseAnnotation_evidence_codes, domain=DiseaseAnnotation, range=Union[Union[str, ECOTermCurie], List[Union[str, ECOTermCurie]]])

slots.DiseaseAnnotation_genetic_sex = Slot(uri=ALLIANCE.genetic_sex, name="DiseaseAnnotation_genetic_sex", curie=ALLIANCE.curie('genetic_sex'),
                   model_uri=ALLIANCE.DiseaseAnnotation_genetic_sex, domain=DiseaseAnnotation, range=Optional[Union[str, VocabularyTermName]])

slots.DiseaseAnnotation_related_notes = Slot(uri=ALLIANCE.related_notes, name="DiseaseAnnotation_related_notes", curie=ALLIANCE.curie('related_notes'),
                   model_uri=ALLIANCE.DiseaseAnnotation_related_notes, domain=DiseaseAnnotation, range=Optional[Union[Union[dict, Note], List[Union[dict, Note]]]])

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

slots.AlleleDiseaseAnnotation_asserted_gene = Slot(uri=ALLIANCE.asserted_gene, name="AlleleDiseaseAnnotation_asserted_gene", curie=ALLIANCE.curie('asserted_gene'),
                   model_uri=ALLIANCE.AlleleDiseaseAnnotation_asserted_gene, domain=AlleleDiseaseAnnotation, range=Optional[Union[str, GeneCurie]])

slots.AGMDiseaseAnnotation_subject = Slot(uri=ALLIANCE.subject, name="AGMDiseaseAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.AGMDiseaseAnnotation_subject, domain=AGMDiseaseAnnotation, range=Union[str, AffectedGenomicModelCurie])

slots.AGMDiseaseAnnotation_predicate = Slot(uri=ALLIANCE.predicate, name="AGMDiseaseAnnotation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.AGMDiseaseAnnotation_predicate, domain=AGMDiseaseAnnotation, range=Union[str, VocabularyTermName])

slots.AGMDiseaseAnnotation_inferred_gene = Slot(uri=ALLIANCE.inferred_gene, name="AGMDiseaseAnnotation_inferred_gene", curie=ALLIANCE.curie('inferred_gene'),
                   model_uri=ALLIANCE.AGMDiseaseAnnotation_inferred_gene, domain=AGMDiseaseAnnotation, range=Optional[Union[str, GeneCurie]])

slots.AGMDiseaseAnnotation_inferred_allele = Slot(uri=ALLIANCE.inferred_allele, name="AGMDiseaseAnnotation_inferred_allele", curie=ALLIANCE.curie('inferred_allele'),
                   model_uri=ALLIANCE.AGMDiseaseAnnotation_inferred_allele, domain=AGMDiseaseAnnotation, range=Optional[Union[str, AlleleCurie]])

slots.AGMDiseaseAnnotation_asserted_gene = Slot(uri=ALLIANCE.asserted_gene, name="AGMDiseaseAnnotation_asserted_gene", curie=ALLIANCE.curie('asserted_gene'),
                   model_uri=ALLIANCE.AGMDiseaseAnnotation_asserted_gene, domain=AGMDiseaseAnnotation, range=Optional[Union[str, GeneCurie]])

slots.AGMDiseaseAnnotation_asserted_allele = Slot(uri=ALLIANCE.asserted_allele, name="AGMDiseaseAnnotation_asserted_allele", curie=ALLIANCE.curie('asserted_allele'),
                   model_uri=ALLIANCE.AGMDiseaseAnnotation_asserted_allele, domain=AGMDiseaseAnnotation, range=Optional[Union[str, AlleleCurie]])

slots.ExperimentalCondition_unique_id = Slot(uri=ALLIANCE.unique_id, name="ExperimentalCondition_unique_id", curie=ALLIANCE.curie('unique_id'),
                   model_uri=ALLIANCE.ExperimentalCondition_unique_id, domain=ExperimentalCondition, range=Optional[str])

slots.ExperimentalCondition_condition_class = Slot(uri=ALLIANCE.condition_class, name="ExperimentalCondition_condition_class", curie=ALLIANCE.curie('condition_class'),
                   model_uri=ALLIANCE.ExperimentalCondition_condition_class, domain=ExperimentalCondition, range=Union[str, ZECOTermCurie])

slots.ExperimentalCondition_condition_statement = Slot(uri=ALLIANCE.condition_statement, name="ExperimentalCondition_condition_statement", curie=ALLIANCE.curie('condition_statement'),
                   model_uri=ALLIANCE.ExperimentalCondition_condition_statement, domain=ExperimentalCondition, range=str)

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

slots.Antibody_curie = Slot(uri=ALLIANCE.curie, name="Antibody_curie", curie=ALLIANCE.curie('curie'),
                   model_uri=ALLIANCE.Antibody_curie, domain=Antibody, range=Union[str, AntibodyCurie])

slots.Antibody_name = Slot(uri=ALLIANCE.name, name="Antibody_name", curie=ALLIANCE.curie('name'),
                   model_uri=ALLIANCE.Antibody_name, domain=Antibody, range=str)

slots.Antibody_taxon = Slot(uri=ALLIANCE.taxon, name="Antibody_taxon", curie=ALLIANCE.curie('taxon'),
                   model_uri=ALLIANCE.Antibody_taxon, domain=Antibody, range=Optional[Union[str, NCBITaxonTermCurie]])

slots.Antibody_original_reference = Slot(uri=ALLIANCE.original_reference, name="Antibody_original_reference", curie=ALLIANCE.curie('original_reference'),
                   model_uri=ALLIANCE.Antibody_original_reference, domain=Antibody, range=Optional[Union[str, ReferenceCurie]])

slots.Reference_reference_id = Slot(uri=ALLIANCE.reference_id, name="Reference_reference_id", curie=ALLIANCE.curie('reference_id'),
                   model_uri=ALLIANCE.Reference_reference_id, domain=Reference, range=int)

slots.MeshDetail_reference_id = Slot(uri=ALLIANCE.reference_id, name="MeshDetail_reference_id", curie=ALLIANCE.curie('reference_id'),
                   model_uri=ALLIANCE.MeshDetail_reference_id, domain=MeshDetail, range=int)

slots.Resource_id = Slot(uri=ALLIANCE.id, name="Resource_id", curie=ALLIANCE.curie('id'),
                   model_uri=ALLIANCE.Resource_id, domain=Resource, range=Optional[str])

slots.Resource_title = Slot(uri=ALLIANCE.title, name="Resource_title", curie=ALLIANCE.curie('title'),
                   model_uri=ALLIANCE.Resource_title, domain=Resource, range=Optional[str])

slots.VariantGeneConsequence_object = Slot(uri=ALLIANCE.object, name="VariantGeneConsequence_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.VariantGeneConsequence_object, domain=VariantGeneConsequence, range=Union[str, GeneCurie])

slots.VariantGeneConsequence_subject = Slot(uri=ALLIANCE.subject, name="VariantGeneConsequence_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.VariantGeneConsequence_subject, domain=VariantGeneConsequence, range=Union[dict, "VariantGenomeLocation"])

slots.VariantTranscriptConsequence_object = Slot(uri=ALLIANCE.object, name="VariantTranscriptConsequence_object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.VariantTranscriptConsequence_object, domain=VariantTranscriptConsequence, range=Union[str, TranscriptCurie])

slots.VariantTranscriptConsequence_subject = Slot(uri=ALLIANCE.subject, name="VariantTranscriptConsequence_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.VariantTranscriptConsequence_subject, domain=VariantTranscriptConsequence, range=Union[dict, "VariantTranscriptLocation"])

slots.VariantTranscriptConsequence_amino_acid_reference = Slot(uri=ALLIANCE.amino_acid_reference, name="VariantTranscriptConsequence_amino_acid_reference", curie=ALLIANCE.curie('amino_acid_reference'),
                   model_uri=ALLIANCE.VariantTranscriptConsequence_amino_acid_reference, domain=VariantTranscriptConsequence, range=Optional[str])

slots.VariantTranscriptConsequence_amino_acid_variant = Slot(uri=ALLIANCE.amino_acid_variant, name="VariantTranscriptConsequence_amino_acid_variant", curie=ALLIANCE.curie('amino_acid_variant'),
                   model_uri=ALLIANCE.VariantTranscriptConsequence_amino_acid_variant, domain=VariantTranscriptConsequence, range=Optional[str])

slots.VariantTranscriptConsequence_codon_reference = Slot(uri=ALLIANCE.codon_reference, name="VariantTranscriptConsequence_codon_reference", curie=ALLIANCE.curie('codon_reference'),
                   model_uri=ALLIANCE.VariantTranscriptConsequence_codon_reference, domain=VariantTranscriptConsequence, range=Optional[str])

slots.VariantTranscriptConsequence_codon_variant = Slot(uri=ALLIANCE.codon_variant, name="VariantTranscriptConsequence_codon_variant", curie=ALLIANCE.curie('codon_variant'),
                   model_uri=ALLIANCE.VariantTranscriptConsequence_codon_variant, domain=VariantTranscriptConsequence, range=Optional[str])

slots.VariantTranscriptConsequence_cdna_start = Slot(uri=ALLIANCE.cdna_start, name="VariantTranscriptConsequence_cdna_start", curie=ALLIANCE.curie('cdna_start'),
                   model_uri=ALLIANCE.VariantTranscriptConsequence_cdna_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.VariantTranscriptConsequence_cdna_end = Slot(uri=ALLIANCE.cdna_end, name="VariantTranscriptConsequence_cdna_end", curie=ALLIANCE.curie('cdna_end'),
                   model_uri=ALLIANCE.VariantTranscriptConsequence_cdna_end, domain=VariantTranscriptConsequence, range=Optional[int])

slots.VariantTranscriptConsequence_cds_start = Slot(uri=ALLIANCE.cds_start, name="VariantTranscriptConsequence_cds_start", curie=ALLIANCE.curie('cds_start'),
                   model_uri=ALLIANCE.VariantTranscriptConsequence_cds_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.VariantTranscriptConsequence_cds_end = Slot(uri=ALLIANCE.cds_end, name="VariantTranscriptConsequence_cds_end", curie=ALLIANCE.curie('cds_end'),
                   model_uri=ALLIANCE.VariantTranscriptConsequence_cds_end, domain=VariantTranscriptConsequence, range=Optional[int])

slots.VariantTranscriptConsequence_protein_start = Slot(uri=ALLIANCE.protein_start, name="VariantTranscriptConsequence_protein_start", curie=ALLIANCE.curie('protein_start'),
                   model_uri=ALLIANCE.VariantTranscriptConsequence_protein_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.VariantTranscriptConsequence_protein_end = Slot(uri=ALLIANCE.protein_end, name="VariantTranscriptConsequence_protein_end", curie=ALLIANCE.curie('protein_end'),
                   model_uri=ALLIANCE.VariantTranscriptConsequence_protein_end, domain=VariantTranscriptConsequence, range=Optional[int])

slots.VariantTranscriptConsequence_hgvs_protein_nomenclature = Slot(uri=ALLIANCE.hgvs_protein_nomenclature, name="VariantTranscriptConsequence_hgvs_protein_nomenclature", curie=ALLIANCE.curie('hgvs_protein_nomenclature'),
                   model_uri=ALLIANCE.VariantTranscriptConsequence_hgvs_protein_nomenclature, domain=VariantTranscriptConsequence, range=Optional[str])

slots.VariantTranscriptConsequence_hgvs_coding_nomenclature = Slot(uri=ALLIANCE.hgvs_coding_nomenclature, name="VariantTranscriptConsequence_hgvs_coding_nomenclature", curie=ALLIANCE.curie('hgvs_coding_nomenclature'),
                   model_uri=ALLIANCE.VariantTranscriptConsequence_hgvs_coding_nomenclature, domain=VariantTranscriptConsequence, range=Optional[str])

slots.SourceVariantLocation_single_reference = Slot(uri=ALLIANCE.single_reference, name="SourceVariantLocation_single_reference", curie=ALLIANCE.curie('single_reference'),
                   model_uri=ALLIANCE.SourceVariantLocation_single_reference, domain=SourceVariantLocation, range=Union[str, ReferenceCurie])

slots.VariantLocation_evidence_code = Slot(uri=ALLIANCE.evidence_code, name="VariantLocation_evidence_code", curie=ALLIANCE.curie('evidence_code'),
                   model_uri=ALLIANCE.VariantLocation_evidence_code, domain=VariantLocation, range=Optional[Union[str, ECOTermCurie]])

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
