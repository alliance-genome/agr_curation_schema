# Auto generated from expression.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-01-26T16:37:28
# Schema: expression.yaml
#
# id: https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml
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
from linkml_runtime.linkml_model.types import Boolean, Date, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DOI = CurieNamespace('DOI', 'http://identifiers.org/doi/')
ENSEMBL = CurieNamespace('ENSEMBL', 'http://identifiers.org/ensembl/')
FB = CurieNamespace('FB', 'http://identifiers.org/fb/')
HGNC = CurieNamespace('HGNC', 'http://identifiers.org/hgnc/')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
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
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
OBOGRAPH = CurieNamespace('obograph', 'https://github.com/biodatamodels/obograph')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/')


# Types
class BiologicalSequence(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "biological_sequence"
    type_model_uri = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/BiologicalSequence")


# Class references
class ExpressionAnnotationCurie(URIorCURIE):
    pass


class BiologicalEntityCurie(URIorCURIE):
    pass


class GenomicEntityCurie(BiologicalEntityCurie):
    pass


class AffectedGenomicModelCurie(GenomicEntityCurie):
    pass


class AlleleCurie(GenomicEntityCurie):
    pass


class ConstructCurie(GenomicEntityCurie):
    pass


class ConstructComponentCurie(GenomicEntityCurie):
    pass


class TranscriptCurie(GenomicEntityCurie):
    pass


class GeneCurie(GenomicEntityCurie):
    pass


class ChromosomeCurie(URIorCURIE):
    pass


class AssemblyCurie(URIorCURIE):
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


class VariantCurie(GenomicEntityCurie):
    pass


class InformationContentEntityCurie(URIorCURIE):
    pass


class CrossReferenceCurie(InformationContentEntityCurie):
    pass


class ReferenceCurie(InformationContentEntityCurie):
    pass


class ResourceCurie(InformationContentEntityCurie):
    pass


class PersonPersonId(extended_str):
    pass


@dataclass
class AnatomicalSite(YAMLRoot):
    """
    The developmental stage and/or age of the specimen in an annotation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/AnatomicalSite")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AnatomicalSite"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/AnatomicalSite")

    anatomical_structure: Optional[Union[str, AnatomicalTermCurie]] = None
    anatomical_substructure: Optional[Union[str, AnatomicalTermCurie]] = None
    cellular_component: Optional[Union[str, GOTermCurie]] = None
    anatomical_qualifiers: Optional[Union[str, "AnatomicalQualifierSet"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.anatomical_structure is not None and not isinstance(self.anatomical_structure, AnatomicalTermCurie):
            self.anatomical_structure = AnatomicalTermCurie(self.anatomical_structure)

        if self.anatomical_substructure is not None and not isinstance(self.anatomical_substructure, AnatomicalTermCurie):
            self.anatomical_substructure = AnatomicalTermCurie(self.anatomical_substructure)

        if self.cellular_component is not None and not isinstance(self.cellular_component, GOTermCurie):
            self.cellular_component = GOTermCurie(self.cellular_component)

        if self.anatomical_qualifiers is not None and not isinstance(self.anatomical_qualifiers, AnatomicalQualifierSet):
            self.anatomical_qualifiers = AnatomicalQualifierSet(self.anatomical_qualifiers)

        super().__post_init__(**kwargs)


@dataclass
class ExpressionAnnotation(YAMLRoot):
    """
    A description of when and where gene products are observed to be present, including experimental details,
    supporting evidence, and curator notes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ExpressionAnnotation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ExpressionAnnotation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ExpressionAnnotation")

    curie: Union[str, ExpressionAnnotationCurie] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    gene: Optional[Union[str, GeneCurie]] = None
    when_expressed: Optional[Union[dict, "TemporalContext"]] = None
    where_expressed: Optional[Union[dict, AnatomicalSite]] = None
    assay: Optional[Union[str, MMOTermCurie]] = None
    reagents: Optional[Union[Union[dict, "Reagent"], List[Union[dict, "Reagent"]]]] = empty_list()
    expression_qualifiers: Optional[Union[str, "ExpressionQualifierSet"]] = None
    perturbed_expression_qualifiers: Optional[Union[str, "PerturbedExpressionQualifierSet"]] = None
    perturbed: Optional[Union[bool, Bool]] = None
    negated: Optional[Union[bool, Bool]] = None
    uncertain: Optional[Union[bool, Bool]] = None
    primary_genetic_entities: Optional[Union[Union[str, BiologicalEntityCurie], List[Union[str, BiologicalEntityCurie]]]] = empty_list()
    when_expressed_note: Optional[str] = None
    where_expressed_note: Optional[str] = None
    expression_annotation_note: Optional[str] = None
    has_reference: Optional[Union[str, ReferenceCurie]] = None
    has_figure: Optional[Union[str, FigureCurie]] = None
    table_key: Optional[int] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ExpressionAnnotationCurie):
            self.curie = ExpressionAnnotationCurie(self.curie)

        if self._is_empty(self.created_by):
            self.MissingRequiredField("created_by")
        if not isinstance(self.created_by, PersonPersonId):
            self.created_by = PersonPersonId(self.created_by)

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, PersonPersonId):
            self.modified_by = PersonPersonId(self.modified_by)

        if self.gene is not None and not isinstance(self.gene, GeneCurie):
            self.gene = GeneCurie(self.gene)

        if self.when_expressed is not None and not isinstance(self.when_expressed, TemporalContext):
            self.when_expressed = TemporalContext(**as_dict(self.when_expressed))

        if self.where_expressed is not None and not isinstance(self.where_expressed, AnatomicalSite):
            self.where_expressed = AnatomicalSite(**as_dict(self.where_expressed))

        if self.assay is not None and not isinstance(self.assay, MMOTermCurie):
            self.assay = MMOTermCurie(self.assay)

        if not isinstance(self.reagents, list):
            self.reagents = [self.reagents] if self.reagents is not None else []
        self.reagents = [v if isinstance(v, Reagent) else Reagent(**as_dict(v)) for v in self.reagents]

        if self.expression_qualifiers is not None and not isinstance(self.expression_qualifiers, ExpressionQualifierSet):
            self.expression_qualifiers = ExpressionQualifierSet(self.expression_qualifiers)

        if self.perturbed_expression_qualifiers is not None and not isinstance(self.perturbed_expression_qualifiers, PerturbedExpressionQualifierSet):
            self.perturbed_expression_qualifiers = PerturbedExpressionQualifierSet(self.perturbed_expression_qualifiers)

        if self.perturbed is not None and not isinstance(self.perturbed, Bool):
            self.perturbed = Bool(self.perturbed)

        if self.negated is not None and not isinstance(self.negated, Bool):
            self.negated = Bool(self.negated)

        if self.uncertain is not None and not isinstance(self.uncertain, Bool):
            self.uncertain = Bool(self.uncertain)

        if not isinstance(self.primary_genetic_entities, list):
            self.primary_genetic_entities = [self.primary_genetic_entities] if self.primary_genetic_entities is not None else []
        self.primary_genetic_entities = [v if isinstance(v, BiologicalEntityCurie) else BiologicalEntityCurie(v) for v in self.primary_genetic_entities]

        if self.when_expressed_note is not None and not isinstance(self.when_expressed_note, str):
            self.when_expressed_note = str(self.when_expressed_note)

        if self.where_expressed_note is not None and not isinstance(self.where_expressed_note, str):
            self.where_expressed_note = str(self.where_expressed_note)

        if self.expression_annotation_note is not None and not isinstance(self.expression_annotation_note, str):
            self.expression_annotation_note = str(self.expression_annotation_note)

        if self.has_reference is not None and not isinstance(self.has_reference, ReferenceCurie):
            self.has_reference = ReferenceCurie(self.has_reference)

        if self.has_figure is not None and not isinstance(self.has_figure, FigureCurie):
            self.has_figure = FigureCurie(self.has_figure)

        if self.table_key is not None and not isinstance(self.table_key, int):
            self.table_key = int(self.table_key)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

        super().__post_init__(**kwargs)


@dataclass
class TemporalContext(YAMLRoot):
    """
    The developmental stage and/or age of the specimen in an annotation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/TemporalContext")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "TemporalContext"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/TemporalContext")

    developmental_stage: Optional[Union[str, StageTermCurie]] = None
    age: Optional[str] = None
    temporal_qualifiers: Optional[Union[str, "TemporalQualifierSet"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.developmental_stage is not None and not isinstance(self.developmental_stage, StageTermCurie):
            self.developmental_stage = StageTermCurie(self.developmental_stage)

        if self.age is not None and not isinstance(self.age, str):
            self.age = str(self.age)

        if self.temporal_qualifiers is not None and not isinstance(self.temporal_qualifiers, TemporalQualifierSet):
            self.temporal_qualifiers = TemporalQualifierSet(self.temporal_qualifiers)

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/AffectedGenomicModelComponent")

    has_allele: Optional[Union[str, AlleleCurie]] = None
    zygosity: Optional[Union[str, "ZygosityValues"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_allele is not None and not isinstance(self.has_allele, AlleleCurie):
            self.has_allele = AlleleCurie(self.has_allele)

        if self.zygosity is not None and not isinstance(self.zygosity, ZygosityValues):
            self.zygosity = ZygosityValues(self.zygosity)

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ReferenceType")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/NoteType")

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
class MolecularMutation(YAMLRoot):
    """
    Description of the DNA changes with unknown precise genomic location
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/MolecularMutation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "MolecularMutation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/MolecularMutation")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/CellLine")


class SequenceTargetingReagent(YAMLRoot):
    """
    Dummy sequence targeting reagent class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/SequenceTargetingReagent")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SequenceTargetingReagent"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/SequenceTargetingReagent")


class Entity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Entity
    class_class_curie: ClassVar[str] = "alliance:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Entity")


@dataclass
class BiologicalEntity(YAMLRoot):
    """
    A high-level entity comprising .
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.BiologicalEntity
    class_class_curie: ClassVar[str] = "alliance:BiologicalEntity"
    class_name: ClassVar[str] = "BiologicalEntity"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/BiologicalEntity")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/GenomicEntity")

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
class AffectedGenomicModel(GenomicEntity):
    """
    Includes inbred strains, stocks, disease models and mutant genotypes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/affectedGenomicModel/AffectedGenomicModel")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AffectedGenomicModel"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/AffectedGenomicModel")

    curie: Union[str, AffectedGenomicModelCurie] = None
    taxon: Union[str, URIorCURIE] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    subtype: Optional[Union[str, "SubtypeValues"]] = None
    components: Optional[Union[Union[dict, "AffectedGenomicModelComponent"], List[Union[dict, "AffectedGenomicModelComponent"]]]] = empty_list()
    sequence_targeting_reagents: Optional[Union[Union[dict, "SequenceTargetingReagent"], List[Union[dict, "SequenceTargetingReagent"]]]] = empty_list()
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
class Allele(GenomicEntity):
    """
    One of multiple possible forms of a functional genomic element (most often described as a locus or gene),
    differing from the reference DNA sequence. The genomic element can be endogenous or constructed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/Allele")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Allele"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Allele")

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
    synonyms: Optional[Union[Union[dict, "Synonym"], List[Union[dict, "Synonym"]]]] = empty_list()
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
class Construct(GenomicEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/allele/Construct")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Construct"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Construct")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ConstructComponent")

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
class Transcript(GenomicEntity):
    """
    Placeholder.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Transcript
    class_class_curie: ClassVar[str] = "alliance:Transcript"
    class_name: ClassVar[str] = "Transcript"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Transcript")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Gene")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Species")


class Synonym(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Synonym
    class_class_curie: ClassVar[str] = "alliance:Synonym"
    class_name: ClassVar[str] = "Synonym"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Synonym")


@dataclass
class AuditedObject(YAMLRoot):
    """
    Some entity for which changes are tracked, including date/time of change and the agent responsible for the change.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AuditedObject
    class_class_curie: ClassVar[str] = "alliance:AuditedObject"
    class_name: ClassVar[str] = "AuditedObject"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/AuditedObject")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Reagent")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/EntityStatement")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Association")

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
class ExpressionAnnotationImagePane(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ExpressionAnnotationImagePane")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ExpressionAnnotationImagePane"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ExpressionAnnotationImagePane")

    predicate: str = None
    subject: Union[str, ExpressionAnnotationCurie] = None
    object: Union[dict, "ImagePane"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ExpressionAnnotationCurie):
            self.subject = ExpressionAnnotationCurie(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ImagePane):
            self.object = ImagePane(**as_dict(self.object))

        super().__post_init__(**kwargs)


@dataclass
class ExpressionAnnotationExperimentalConditionAssociation(Association):
    """
    A typed (predicate-specified) association between an expression annotation object and an experimental condition
    object
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ExpressionAnnotationExperimentalConditionAssociation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ExpressionAnnotationExperimentalConditionAssociation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ExpressionAnnotationExperimentalConditionAssociation")

    subject: str = None
    object: str = None
    predicate: Union[str, "ExpressionConditionRelationEnum"] = None
    phenotype_annotation: Optional[Union[str, ExpressionAnnotationCurie]] = None
    experimental_condition: Optional[Union[dict, "ExperimentalCondition"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, ExpressionConditionRelationEnum):
            self.predicate = ExpressionConditionRelationEnum(self.predicate)

        if self.phenotype_annotation is not None and not isinstance(self.phenotype_annotation, ExpressionAnnotationCurie):
            self.phenotype_annotation = ExpressionAnnotationCurie(self.phenotype_annotation)

        if self.experimental_condition is not None and not isinstance(self.experimental_condition, ExperimentalCondition):
            self.experimental_condition = ExperimentalCondition(**as_dict(self.experimental_condition))

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/EntitySynonym")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ExternalDatabaseLink")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Chromosome")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Assembly")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/GeneGenomicLocation")

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
class Figure(YAMLRoot):
    """
    An entity representing a figure or table in a publication.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/image.yaml/Figure")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Figure"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Figure")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/File")


@dataclass
class Image(YAMLRoot):
    """
    The set of files and metadata that constitute an image.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/image.yaml/Image")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Image"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Image")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ImagePane")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/OntologyTerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/DOTerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ECOTerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/FBCVTerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/GOTerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/MITerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/MMOTerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/MMUSDVTerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/SOTerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/CHEBITerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/StageTerm")

    curie: Union[str, StageTermCurie] = None

@dataclass
class FBDVTerm(StageTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/FBDVTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "FBDVTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/FBDVTerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/WBLSTerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ZFSTerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ExperimentalConditionOntologyTerm")

    curie: Union[str, ExperimentalConditionOntologyTermCurie] = None

@dataclass
class ZECOTerm(ExperimentalConditionOntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/ZECOTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ZECOTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ZECOTerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/XCOTerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/AnatomicalTerm")

    curie: Union[str, AnatomicalTermCurie] = None

@dataclass
class CLTerm(AnatomicalTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/CLTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CLTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/CLTerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/EMAPATerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/FBBTTerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/MATerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/UBERONTerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/WBBTTerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ZFATerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/PhenotypeTerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/PhenotypeAnnotation")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/GenePhenotypeAnnotation")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/AllelePhenotypeAnnotation")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/AGMPhenotypeAnnotation")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/DiseaseAnnotation")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/GeneDiseaseAnnotation")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/AlleleDiseaseAnnotation")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/AGMDiseaseAnnotation")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ExperimentalCondition")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ConditionRelation")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Molecule")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/PaperHandle")

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
class Variant(GenomicEntity):
    """
    A DNA sequence that differs relative to a designated reference sequence. The sequence occurs at a single position
    or in contiguous nucleotides.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/variation/Variant")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Variant"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Variant")

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
    cross_references: Optional[Union[Dict[Union[str, CrossReferenceCurie], Union[dict, CrossReference]], List[Union[dict, CrossReference]]]] = empty_dict()

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
class InformationContentEntity(YAMLRoot):
    """
    a piece of information that typically describes some topic of discourse or is used as support. Precedence of
    identifiers for references is as follows: PMID if available; DOI if not; actual alternate CURIE otherwise.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.InformationContentEntity
    class_class_curie: ClassVar[str] = "alliance:InformationContentEntity"
    class_name: ClassVar[str] = "InformationContentEntity"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/InformationContentEntity")

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
class CrossReference(InformationContentEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.CrossReference
    class_class_curie: ClassVar[str] = "alliance:CrossReference"
    class_name: ClassVar[str] = "CrossReference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/CrossReference")

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
class Reference(InformationContentEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/reference/Reference")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Reference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Reference")

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
    cross_references: Optional[Union[Dict[Union[str, CrossReferenceCurie], Union[dict, CrossReference]], List[Union[dict, CrossReference]]]] = empty_dict()
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
class AuthorReference(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AuthorReference
    class_class_curie: ClassVar[str] = "alliance:AuthorReference"
    class_name: ClassVar[str] = "AuthorReference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/AuthorReference")

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


@dataclass
class Resource(InformationContentEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/resource/Resource")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Resource")

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


class Agent(YAMLRoot):
    """
    An individual, group, organization or project that provides information and/or materials.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Agent
    class_class_curie: ClassVar[str] = "alliance:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Agent")


class Organization(Agent):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Organization
    class_class_curie: ClassVar[str] = "alliance:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Organization")


class Laboratory(Organization):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Laboratory
    class_class_curie: ClassVar[str] = "alliance:Laboratory"
    class_name: ClassVar[str] = "Laboratory"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Laboratory")


class Company(Organization):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Company
    class_class_curie: ClassVar[str] = "alliance:Company"
    class_name: ClassVar[str] = "Company"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Company")


@dataclass
class Person(Agent):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Person
    class_class_curie: ClassVar[str] = "alliance:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Person")

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


# Enumerations
class AnatomicalQualifierSet(EnumDefinitionImpl):

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
        name="AnatomicalQualifierSet",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "dorso-lateral",
                PermissibleValue(text="dorso-lateral") )

class ExpressionConditionRelationEnum(EnumDefinitionImpl):

    has_condition = PermissibleValue(text="has_condition")
    induced_by = PermissibleValue(text="induced_by")

    _defn = EnumDefinition(
        name="ExpressionConditionRelationEnum",
    )

class ExpressionQualifierSet(EnumDefinitionImpl):

    faint = PermissibleValue(text="faint")
    granular = PermissibleValue(text="granular")
    intense = PermissibleValue(text="intense")
    punctate = PermissibleValue(text="punctate")
    uniform = PermissibleValue(text="uniform")
    variable = PermissibleValue(text="variable")

    _defn = EnumDefinition(
        name="ExpressionQualifierSet",
    )

class PerturbedExpressionQualifierSet(EnumDefinitionImpl):

    increased = PermissibleValue(text="increased")
    decreased = PermissibleValue(text="decreased")
    mislocalized = PermissibleValue(text="mislocalized")

    _defn = EnumDefinition(
        name="PerturbedExpressionQualifierSet",
    )

class TemporalQualifierSet(EnumDefinitionImpl):

    progressive = PermissibleValue(text="progressive",
                                             description="An event that gets more pronounced with time.")

    _defn = EnumDefinition(
        name="TemporalQualifierSet",
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

class EntitySynonymTypeSet(EnumDefinitionImpl):

    current = PermissibleValue(text="current",
                                     description="The synonym is an officially accepted synonym for an entity. An entity should have only one current synonym of a give type. For example, only one current symbol and one current full name.")
    alias = PermissibleValue(text="alias",
                                 description="The synonym is an alternate symbol or name for the entity. It is not the currently preferred symbol/name for the entity.")

    _defn = EnumDefinition(
        name="EntitySynonymTypeSet",
    )

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

class TagSet(EnumDefinitionImpl):

    image = PermissibleValue(text="image")
    test = PermissibleValue(text="test")

    _defn = EnumDefinition(
        name="TagSet",
    )

# Slots
class slots:
    pass

slots.age = Slot(uri=DEFAULT_.age, name="age", curie=DEFAULT_.curie('age'),
                   model_uri=DEFAULT_.age, domain=TemporalContext, range=Optional[str])

slots.anatomical_qualifiers = Slot(uri=DEFAULT_.anatomical_qualifiers, name="anatomical_qualifiers", curie=DEFAULT_.curie('anatomical_qualifiers'),
                   model_uri=DEFAULT_.anatomical_qualifiers, domain=AnatomicalSite, range=Optional[Union[str, "AnatomicalQualifierSet"]])

slots.anatomical_structure = Slot(uri=DEFAULT_.anatomical_structure, name="anatomical_structure", curie=DEFAULT_.curie('anatomical_structure'),
                   model_uri=DEFAULT_.anatomical_structure, domain=AnatomicalTerm, range=Optional[Union[str, AnatomicalTermCurie]])

slots.anatomical_structure_note = Slot(uri=DEFAULT_.anatomical_structure_note, name="anatomical_structure_note", curie=DEFAULT_.curie('anatomical_structure_note'),
                   model_uri=DEFAULT_.anatomical_structure_note, domain=ExpressionAnnotation, range=Optional[str])

slots.anatomical_substructure = Slot(uri=DEFAULT_.anatomical_substructure, name="anatomical_substructure", curie=DEFAULT_.curie('anatomical_substructure'),
                   model_uri=DEFAULT_.anatomical_substructure, domain=AnatomicalTerm, range=Optional[Union[str, AnatomicalTermCurie]])

slots.anatomical_substructure_note = Slot(uri=DEFAULT_.anatomical_substructure_note, name="anatomical_substructure_note", curie=DEFAULT_.curie('anatomical_substructure_note'),
                   model_uri=DEFAULT_.anatomical_substructure_note, domain=ExpressionAnnotation, range=Optional[str])

slots.assay = Slot(uri=DEFAULT_.assay, name="assay", curie=DEFAULT_.curie('assay'),
                   model_uri=DEFAULT_.assay, domain=ExpressionAnnotation, range=Optional[Union[str, MMOTermCurie]])

slots.cellular_component = Slot(uri=DEFAULT_.cellular_component, name="cellular_component", curie=DEFAULT_.curie('cellular_component'),
                   model_uri=DEFAULT_.cellular_component, domain=AnatomicalSite, range=Optional[Union[str, GOTermCurie]])

slots.cellular_component_note = Slot(uri=DEFAULT_.cellular_component_note, name="cellular_component_note", curie=DEFAULT_.curie('cellular_component_note'),
                   model_uri=DEFAULT_.cellular_component_note, domain=ExpressionAnnotation, range=Optional[str])

slots.developmental_stage = Slot(uri=DEFAULT_.developmental_stage, name="developmental_stage", curie=DEFAULT_.curie('developmental_stage'),
                   model_uri=DEFAULT_.developmental_stage, domain=TemporalContext, range=Optional[Union[str, StageTermCurie]])

slots.expression_annotation_note = Slot(uri=DEFAULT_.expression_annotation_note, name="expression_annotation_note", curie=DEFAULT_.curie('expression_annotation_note'),
                   model_uri=DEFAULT_.expression_annotation_note, domain=ExpressionAnnotation, range=Optional[str])

slots.expression_qualifiers = Slot(uri=DEFAULT_.expression_qualifiers, name="expression_qualifiers", curie=DEFAULT_.curie('expression_qualifiers'),
                   model_uri=DEFAULT_.expression_qualifiers, domain=ExpressionAnnotation, range=Optional[Union[str, "ExpressionQualifierSet"]])

slots.gene = Slot(uri=DEFAULT_.gene, name="gene", curie=DEFAULT_.curie('gene'),
                   model_uri=DEFAULT_.gene, domain=ExpressionAnnotation, range=Optional[Union[str, GeneCurie]])

slots.image = Slot(uri=DEFAULT_.image, name="image", curie=DEFAULT_.curie('image'),
                   model_uri=DEFAULT_.image, domain=None, range=Optional[Union[str, ImageCurie]])

slots.perturbed = Slot(uri=DEFAULT_.perturbed, name="perturbed", curie=DEFAULT_.curie('perturbed'),
                   model_uri=DEFAULT_.perturbed, domain=None, range=Optional[Union[bool, Bool]])

slots.perturbed_expression_qualifiers = Slot(uri=DEFAULT_.perturbed_expression_qualifiers, name="perturbed_expression_qualifiers", curie=DEFAULT_.curie('perturbed_expression_qualifiers'),
                   model_uri=DEFAULT_.perturbed_expression_qualifiers, domain=ExpressionAnnotation, range=Optional[Union[str, "PerturbedExpressionQualifierSet"]])

slots.primary_genetic_entities = Slot(uri=DEFAULT_.primary_genetic_entities, name="primary_genetic_entities", curie=DEFAULT_.curie('primary_genetic_entities'),
                   model_uri=DEFAULT_.primary_genetic_entities, domain=ExpressionAnnotation, range=Optional[Union[Union[str, BiologicalEntityCurie], List[Union[str, BiologicalEntityCurie]]]])

slots.reagents = Slot(uri=DEFAULT_.reagents, name="reagents", curie=DEFAULT_.curie('reagents'),
                   model_uri=DEFAULT_.reagents, domain=ExpressionAnnotation, range=Optional[Union[Union[dict, "Reagent"], List[Union[dict, "Reagent"]]]])

slots.temporal_qualifiers = Slot(uri=DEFAULT_.temporal_qualifiers, name="temporal_qualifiers", curie=DEFAULT_.curie('temporal_qualifiers'),
                   model_uri=DEFAULT_.temporal_qualifiers, domain=TemporalContext, range=Optional[Union[str, "TemporalQualifierSet"]])

slots.when_expressed = Slot(uri=DEFAULT_.when_expressed, name="when_expressed", curie=DEFAULT_.curie('when_expressed'),
                   model_uri=DEFAULT_.when_expressed, domain=ExpressionAnnotation, range=Optional[Union[dict, "TemporalContext"]])

slots.when_expressed_note = Slot(uri=DEFAULT_.when_expressed_note, name="when_expressed_note", curie=DEFAULT_.curie('when_expressed_note'),
                   model_uri=DEFAULT_.when_expressed_note, domain=ExpressionAnnotation, range=Optional[str])

slots.where_expressed = Slot(uri=DEFAULT_.where_expressed, name="where_expressed", curie=DEFAULT_.curie('where_expressed'),
                   model_uri=DEFAULT_.where_expressed, domain=ExpressionAnnotation, range=Optional[Union[dict, AnatomicalSite]])

slots.where_expressed_note = Slot(uri=DEFAULT_.where_expressed_note, name="where_expressed_note", curie=DEFAULT_.curie('where_expressed_note'),
                   model_uri=DEFAULT_.where_expressed_note, domain=ExpressionAnnotation, range=Optional[str])

slots.subtype = Slot(uri="str(uriorcurie)", name="subtype", curie=None,
                   model_uri=DEFAULT_.subtype, domain=AffectedGenomicModel, range=Optional[Union[str, "SubtypeValues"]])

slots.components = Slot(uri="str(uriorcurie)", name="components", curie=None,
                   model_uri=DEFAULT_.components, domain=AffectedGenomicModel, range=Optional[Union[Union[dict, "AffectedGenomicModelComponent"], List[Union[dict, "AffectedGenomicModelComponent"]]]])

slots.has_allele = Slot(uri="str(uriorcurie)", name="has_allele", curie=None,
                   model_uri=DEFAULT_.has_allele, domain=AffectedGenomicModelComponent, range=Optional[Union[str, AlleleCurie]])

slots.zygosity = Slot(uri="str(uriorcurie)", name="zygosity", curie=None,
                   model_uri=DEFAULT_.zygosity, domain=AffectedGenomicModelComponent, range=Optional[Union[str, "ZygosityValues"]])

slots.sequence_targeting_reagents = Slot(uri="str(uriorcurie)", name="sequence_targeting_reagents", curie=None,
                   model_uri=DEFAULT_.sequence_targeting_reagents, domain=AffectedGenomicModel, range=Optional[Union[Union[dict, "SequenceTargetingReagent"], List[Union[dict, "SequenceTargetingReagent"]]]])

slots.parental_populations = Slot(uri="str(uriorcurie)", name="parental_populations", curie=None,
                   model_uri=DEFAULT_.parental_populations, domain=AffectedGenomicModel, range=Optional[Union[str, URIorCURIE]])

slots.component_relation = Slot(uri="str(uriorcurie)", name="component_relation", curie=None,
                   model_uri=DEFAULT_.component_relation, domain=None, range=Optional[Union[str, "ComponentRelationsEnum"]])

slots.construct_components = Slot(uri="str(uriorcurie)", name="construct_components", curie=None,
                   model_uri=DEFAULT_.construct_components, domain=None, range=Optional[Union[Union[str, ConstructComponentCurie], List[Union[str, ConstructComponentCurie]]]])

slots.affected_entities = Slot(uri="str(uriorcurie)", name="affected_entities", curie=None,
                   model_uri=DEFAULT_.affected_entities, domain=Allele, range=Optional[Union[Union[str, BiologicalEntityCurie], List[Union[str, BiologicalEntityCurie]]]])

slots.contains_construct = Slot(uri="str(uriorcurie)", name="contains_construct", curie=None,
                   model_uri=DEFAULT_.contains_construct, domain=Allele, range=Optional[Union[str, ConstructCurie]])

slots.molecular_mutation = Slot(uri="str(uriorcurie)", name="molecular_mutation", curie=None,
                   model_uri=DEFAULT_.molecular_mutation, domain=Allele, range=Optional[Union[dict, "MolecularMutation"]])

slots.mutation_type = Slot(uri="str(uriorcurie)", name="mutation_type", curie=None,
                   model_uri=DEFAULT_.mutation_type, domain=MolecularMutation, range=Optional[Union[str, SOTermCurie]])

slots.mutation_description = Slot(uri="str(uriorcurie)", name="mutation_description", curie=None,
                   model_uri=DEFAULT_.mutation_description, domain=None, range=Optional[str])

slots.functional_impact = Slot(uri="str(uriorcurie)", name="functional_impact", curie=None,
                   model_uri=DEFAULT_.functional_impact, domain=Allele, range=Optional[str])

slots.generation_method = Slot(uri="str(uriorcurie)", name="generation_method", curie=None,
                   model_uri=DEFAULT_.generation_method, domain=Allele, range=Optional[str])

slots.associated_references = Slot(uri="str(uriorcurie)", name="associated_references", curie=None,
                   model_uri=DEFAULT_.associated_references, domain=None, range=Optional[Union[Union[dict, ReferenceType], List[Union[dict, ReferenceType]]]])

slots.reference_association = Slot(uri="str(uriorcurie)", name="reference_association", curie=None,
                   model_uri=DEFAULT_.reference_association, domain=ReferenceType, range=Optional[Union[str, "ReferenceAssociationTypes"]])

slots.has_reference = Slot(uri="str(uriorcurie)", name="has_reference", curie=None,
                   model_uri=DEFAULT_.has_reference, domain=ReferenceType, range=Optional[Union[str, ReferenceCurie]])

slots.associated_notes = Slot(uri="str(uriorcurie)", name="associated_notes", curie=None,
                   model_uri=DEFAULT_.associated_notes, domain=None, range=Optional[Union[dict, NoteType]])

slots.note_association = Slot(uri="str(uriorcurie)", name="note_association", curie=None,
                   model_uri=DEFAULT_.note_association, domain=NoteType, range=Optional[Union[str, "NoteAssociationTypes"]])

slots.origins = Slot(uri="str(uriorcurie)", name="origins", curie=None,
                   model_uri=DEFAULT_.origins, domain=Allele, range=Optional[Union[Union[str, AffectedGenomicModelCurie], List[Union[str, AffectedGenomicModelCurie]]]])

slots.germline_transmission_status = Slot(uri="str(uriorcurie)", name="germline_transmission_status", curie=None,
                   model_uri=DEFAULT_.germline_transmission_status, domain=Allele, range=Optional[str])

slots.parent_cell_line = Slot(uri="str(uriorcurie)", name="parent_cell_line", curie=None,
                   model_uri=DEFAULT_.parent_cell_line, domain=Allele, range=Optional[Union[dict, "CellLine"]])

slots.mutant_cell_lines = Slot(uri="str(uriorcurie)", name="mutant_cell_lines", curie=None,
                   model_uri=DEFAULT_.mutant_cell_lines, domain=Allele, range=Optional[Union[Union[dict, "CellLine"], List[Union[dict, "CellLine"]]]])

slots.embryonic_stem_cell_lines = Slot(uri="str(uriorcurie)", name="embryonic_stem_cell_lines", curie=None,
                   model_uri=DEFAULT_.embryonic_stem_cell_lines, domain=Allele, range=Optional[Union[Union[dict, "CellLine"], List[Union[dict, "CellLine"]]]])

slots.database_status = Slot(uri="str(uriorcurie)", name="database_status", curie=None,
                   model_uri=DEFAULT_.database_status, domain=None, range=Optional[Union[str, "DatabaseStatuses"]])

slots.inheritence_mode = Slot(uri="str(uriorcurie)", name="inheritence_mode", curie=None,
                   model_uri=DEFAULT_.inheritence_mode, domain=Allele, range=Optional[Union[str, "ModesOfInheritence"]])

slots.in_collection = Slot(uri="str(uriorcurie)", name="in_collection", curie=None,
                   model_uri=DEFAULT_.in_collection, domain=Allele, range=Optional[str])

slots.transposon_insertion = Slot(uri="str(uriorcurie)", name="transposon_insertion", curie=None,
                   model_uri=DEFAULT_.transposon_insertion, domain=Allele, range=Optional[str])

slots.aberration = Slot(uri="str(uriorcurie)", name="aberration", curie=None,
                   model_uri=DEFAULT_.aberration, domain=Allele, range=Optional[str])

slots.is_extinct = Slot(uri="str(uriorcurie)", name="is_extinct", curie=None,
                   model_uri=DEFAULT_.is_extinct, domain=Allele, range=Optional[Union[bool, Bool]])

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
                   model_uri=DEFAULT_.taxon, domain=None, range=Optional[Union[str, URIorCURIE]])

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
                   model_uri=DEFAULT_.created_by, domain=None, range=Union[str, PersonPersonId])

slots.modified_by = Slot(uri=ALLIANCE.modified_by, name="modified_by", curie=ALLIANCE.curie('modified_by'),
                   model_uri=DEFAULT_.modified_by, domain=None, range=Union[str, PersonPersonId])

slots.release = Slot(uri=ALLIANCE.release, name="release", curie=ALLIANCE.curie('release'),
                   model_uri=DEFAULT_.release, domain=None, range=Optional[str])

slots.data_provider = Slot(uri=ALLIANCE.data_provider, name="data_provider", curie=ALLIANCE.curie('data_provider'),
                   model_uri=DEFAULT_.data_provider, domain=None, range=Optional[Union[str, List[str]]])

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

slots.from_species = Slot(uri=ALLIANCE.from_species, name="from_species", curie=ALLIANCE.curie('from_species'),
                   model_uri=DEFAULT_.from_species, domain=None, range=Optional[Union[dict, Species]])

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

slots.taxon_id = Slot(uri=ALLIANCE.taxon_id, name="taxon_id", curie=ALLIANCE.curie('taxon_id'),
                   model_uri=DEFAULT_.taxon_id, domain=None, range=Optional[int])

slots.references = Slot(uri=ALLIANCE.references, name="references", curie=ALLIANCE.curie('references'),
                   model_uri=DEFAULT_.references, domain=None, range=Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]])

slots.reference = Slot(uri=ALLIANCE.reference, name="reference", curie=ALLIANCE.curie('reference'),
                   model_uri=DEFAULT_.reference, domain=None, range=Optional[Union[str, ReferenceCurie]])

slots.original_reference = Slot(uri=ALLIANCE.original_reference, name="original_reference", curie=ALLIANCE.curie('original_reference'),
                   model_uri=DEFAULT_.original_reference, domain=None, range=Optional[Union[str, ReferenceCurie]])

slots.is_obsolete = Slot(uri=ALLIANCE.is_obsolete, name="is_obsolete", curie=ALLIANCE.curie('is_obsolete'),
                   model_uri=DEFAULT_.is_obsolete, domain=None, range=Optional[Union[bool, Bool]])

slots.abbreviation = Slot(uri=ALLIANCE.abbreviation, name="abbreviation", curie=ALLIANCE.curie('abbreviation'),
                   model_uri=DEFAULT_.abbreviation, domain=None, range=Optional[str])

slots.subject = Slot(uri=ALLIANCE.subject, name="subject", curie=ALLIANCE.curie('subject'),
                   model_uri=DEFAULT_.subject, domain=None, range=str)

slots.object = Slot(uri=ALLIANCE.object, name="object", curie=ALLIANCE.curie('object'),
                   model_uri=DEFAULT_.object, domain=None, range=str)

slots.predicate = Slot(uri=ALLIANCE.predicate, name="predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=DEFAULT_.predicate, domain=None, range=str)

slots.related_to = Slot(uri=ALLIANCE.related_to, name="related_to", curie=ALLIANCE.curie('related_to'),
                   model_uri=DEFAULT_.related_to, domain=None, range=Optional[Union[str, List[str]]])

slots.caption = Slot(uri="str(uriorcurie)", name="caption", curie=None,
                   model_uri=DEFAULT_.caption, domain=Figure, range=Optional[str])

slots.cropped_from = Slot(uri="str(uriorcurie)", name="cropped_from", curie=None,
                   model_uri=DEFAULT_.cropped_from, domain=Image, range=Optional[Union[str, ImageCurie]])

slots.has_figure = Slot(uri="str(uriorcurie)", name="has_figure", curie=None,
                   model_uri=DEFAULT_.has_figure, domain=None, range=Optional[Union[str, FigureCurie]])

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

slots.condition_anatomy = Slot(uri=ALLIANCE.condition_anatomy, name="condition_anatomy", curie=ALLIANCE.curie('condition_anatomy'),
                   model_uri=DEFAULT_.condition_anatomy, domain=ExperimentalCondition, range=Optional[Union[str, AnatomicalTermCurie]])

slots.condition_chemical = Slot(uri=ALLIANCE.condition_chemical, name="condition_chemical", curie=ALLIANCE.curie('condition_chemical'),
                   model_uri=DEFAULT_.condition_chemical, domain=ExperimentalCondition, range=Optional[Union[str, URIorCURIE]])

slots.condition_class = Slot(uri=ALLIANCE.condition_class, name="condition_class", curie=ALLIANCE.curie('condition_class'),
                   model_uri=DEFAULT_.condition_class, domain=ExperimentalCondition, range=Optional[Union[str, ZECOTermCurie]])

slots.condition_gene_ontology = Slot(uri=ALLIANCE.condition_gene_ontology, name="condition_gene_ontology", curie=ALLIANCE.curie('condition_gene_ontology'),
                   model_uri=DEFAULT_.condition_gene_ontology, domain=ExperimentalCondition, range=Optional[Union[str, GOTermCurie]])

slots.condition_id = Slot(uri=ALLIANCE.condition_id, name="condition_id", curie=ALLIANCE.curie('condition_id'),
                   model_uri=DEFAULT_.condition_id, domain=ExperimentalCondition, range=Optional[Union[str, ExperimentalConditionOntologyTermCurie]])

slots.condition_quantity = Slot(uri=ALLIANCE.condition_quantity, name="condition_quantity", curie=ALLIANCE.curie('condition_quantity'),
                   model_uri=DEFAULT_.condition_quantity, domain=ExperimentalCondition, range=Optional[str])

slots.condition_statement = Slot(uri=ALLIANCE.condition_statement, name="condition_statement", curie=ALLIANCE.curie('condition_statement'),
                   model_uri=DEFAULT_.condition_statement, domain=ExperimentalCondition, range=Optional[str])

slots.condition_taxon = Slot(uri=ALLIANCE.condition_taxon, name="condition_taxon", curie=ALLIANCE.curie('condition_taxon'),
                   model_uri=DEFAULT_.condition_taxon, domain=ExperimentalCondition, range=Optional[Union[str, URIorCURIE]])

slots.condition_relations = Slot(uri=ALLIANCE.condition_relations, name="condition_relations", curie=ALLIANCE.curie('condition_relations'),
                   model_uri=DEFAULT_.condition_relations, domain=None, range=Optional[Union[Union[dict, ConditionRelation], List[Union[dict, ConditionRelation]]]])

slots.condition_relation_type = Slot(uri=ALLIANCE.condition_relation_type, name="condition_relation_type", curie=ALLIANCE.curie('condition_relation_type'),
                   model_uri=DEFAULT_.condition_relation_type, domain=None, range=Optional[Union[str, "ConditionRelationEnum"]])

slots.conditions = Slot(uri=ALLIANCE.conditions, name="conditions", curie=ALLIANCE.curie('conditions'),
                   model_uri=DEFAULT_.conditions, domain=None, range=Optional[Union[Union[dict, ExperimentalCondition], List[Union[dict, ExperimentalCondition]]]])

slots.evidence_codes = Slot(uri=ALLIANCE.evidence_codes, name="evidence_codes", curie=ALLIANCE.curie('evidence_codes'),
                   model_uri=DEFAULT_.evidence_codes, domain=None, range=Optional[Union[Union[str, ECOTermCurie], List[Union[str, ECOTermCurie]]]])

slots.inferred_gene = Slot(uri=ALLIANCE.inferred_gene, name="inferred_gene", curie=ALLIANCE.curie('inferred_gene'),
                   model_uri=DEFAULT_.inferred_gene, domain=None, range=Optional[Union[str, GeneCurie]])

slots.inferred_allele = Slot(uri=ALLIANCE.inferred_allele, name="inferred_allele", curie=ALLIANCE.curie('inferred_allele'),
                   model_uri=DEFAULT_.inferred_allele, domain=None, range=Optional[Union[str, AlleleCurie]])

slots.disease_qualifiers = Slot(uri=ALLIANCE.disease_qualifiers, name="disease_qualifiers", curie=ALLIANCE.curie('disease_qualifiers'),
                   model_uri=DEFAULT_.disease_qualifiers, domain=None, range=Optional[Union[str, "DiseaseAnnotationQualifierEnum"]])

slots.genetic_sex = Slot(uri=ALLIANCE.genetic_sex, name="genetic_sex", curie=ALLIANCE.curie('genetic_sex'),
                   model_uri=DEFAULT_.genetic_sex, domain=None, range=Optional[Union[str, "GeneticSexEnum"]])

slots.private_note = Slot(uri=ALLIANCE.private_note, name="private_note", curie=ALLIANCE.curie('private_note'),
                   model_uri=DEFAULT_.private_note, domain=None, range=Optional[str])

slots.disease_annotation_note = Slot(uri=ALLIANCE.disease_annotation_note, name="disease_annotation_note", curie=ALLIANCE.curie('disease_annotation_note'),
                   model_uri=DEFAULT_.disease_annotation_note, domain=None, range=Optional[str])

slots.disease_annotation_summary = Slot(uri=ALLIANCE.disease_annotation_summary, name="disease_annotation_summary", curie=ALLIANCE.curie('disease_annotation_summary'),
                   model_uri=DEFAULT_.disease_annotation_summary, domain=None, range=Optional[str])

slots.sgd_strain_background = Slot(uri=ALLIANCE.sgd_strain_background, name="sgd_strain_background", curie=ALLIANCE.curie('sgd_strain_background'),
                   model_uri=DEFAULT_.sgd_strain_background, domain=None, range=Optional[Union[str, AffectedGenomicModelCurie]])

slots.annotation_type = Slot(uri=ALLIANCE.annotation_type, name="annotation_type", curie=ALLIANCE.curie('annotation_type'),
                   model_uri=DEFAULT_.annotation_type, domain=None, range=Optional[Union[str, "AnnotationTypeEnum"]])

slots.disease_genetic_modifier = Slot(uri=ALLIANCE.disease_genetic_modifier, name="disease_genetic_modifier", curie=ALLIANCE.curie('disease_genetic_modifier'),
                   model_uri=DEFAULT_.disease_genetic_modifier, domain=None, range=Optional[Union[str, BiologicalEntityCurie]])

slots.disease_genetic_modifier_relation = Slot(uri=ALLIANCE.disease_genetic_modifier_relation, name="disease_genetic_modifier_relation", curie=ALLIANCE.curie('disease_genetic_modifier_relation'),
                   model_uri=DEFAULT_.disease_genetic_modifier_relation, domain=None, range=Optional[Union[str, "GeneticModifierRelationEnum"]])

slots.phenotype_term = Slot(uri=ALLIANCE.phenotype_term, name="phenotype_term", curie=ALLIANCE.curie('phenotype_term'),
                   model_uri=DEFAULT_.phenotype_term, domain=None, range=Optional[Union[str, PhenotypeTermCurie]])

slots.with = Slot(uri=ALLIANCE.with, name="with", curie=ALLIANCE.curie('with'),
                   model_uri=DEFAULT_.with, domain=None, range=Optional[Union[str, GeneCurie]])

slots.mod_id = Slot(uri=ALLIANCE.mod_id, name="mod_id", curie=ALLIANCE.curie('mod_id'),
                   model_uri=DEFAULT_.mod_id, domain=None, range=Optional[str])

slots.paper_handles = Slot(uri=ALLIANCE.paper_handles, name="paper_handles", curie=ALLIANCE.curie('paper_handles'),
                   model_uri=DEFAULT_.paper_handles, domain=None, range=Optional[Union[Union[dict, PaperHandle], List[Union[dict, PaperHandle]]]])

slots.handle = Slot(uri=ALLIANCE.handle, name="handle", curie=ALLIANCE.curie('handle'),
                   model_uri=DEFAULT_.handle, domain=None, range=Optional[str])

slots.has_condition = Slot(uri=ALLIANCE.has_condition, name="has_condition", curie=ALLIANCE.curie('has_condition'),
                   model_uri=DEFAULT_.has_condition, domain=Entity, range=Optional[Union[Union[dict, "ExperimentalCondition"], List[Union[dict, "ExperimentalCondition"]]]])

slots.is_condition_in = Slot(uri=ALLIANCE.is_condition_in, name="is_condition_in", curie=ALLIANCE.curie('is_condition_in'),
                   model_uri=DEFAULT_.is_condition_in, domain=ExperimentalCondition, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.induced_by = Slot(uri=ALLIANCE.induced_by, name="induced_by", curie=ALLIANCE.curie('induced_by'),
                   model_uri=DEFAULT_.induced_by, domain=Entity, range=Optional[Union[Union[dict, "ExperimentalCondition"], List[Union[dict, "ExperimentalCondition"]]]])

slots.induces = Slot(uri=ALLIANCE.induces, name="induces", curie=ALLIANCE.curie('induces'),
                   model_uri=DEFAULT_.induces, domain=ExperimentalCondition, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.ameliorated_by = Slot(uri=ALLIANCE.ameliorated_by, name="ameliorated_by", curie=ALLIANCE.curie('ameliorated_by'),
                   model_uri=DEFAULT_.ameliorated_by, domain=Entity, range=Optional[Union[Union[dict, "ExperimentalCondition"], List[Union[dict, "ExperimentalCondition"]]]])

slots.ameliorates = Slot(uri=ALLIANCE.ameliorates, name="ameliorates", curie=ALLIANCE.curie('ameliorates'),
                   model_uri=DEFAULT_.ameliorates, domain=ExperimentalCondition, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.exacerbated_by = Slot(uri=ALLIANCE.exacerbated_by, name="exacerbated_by", curie=ALLIANCE.curie('exacerbated_by'),
                   model_uri=DEFAULT_.exacerbated_by, domain=Entity, range=Optional[Union[Union[dict, "ExperimentalCondition"], List[Union[dict, "ExperimentalCondition"]]]])

slots.exacerbates = Slot(uri=ALLIANCE.exacerbates, name="exacerbates", curie=ALLIANCE.curie('exacerbates'),
                   model_uri=DEFAULT_.exacerbates, domain=ExperimentalCondition, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.inchi = Slot(uri=ALLIANCE.inchi, name="inchi", curie=ALLIANCE.curie('inchi'),
                   model_uri=DEFAULT_.inchi, domain=Molecule, range=Optional[str])

slots.inchi_key = Slot(uri=ALLIANCE.inchi_key, name="inchi_key", curie=ALLIANCE.curie('inchi_key'),
                   model_uri=DEFAULT_.inchi_key, domain=Molecule, range=Optional[str])

slots.iupac = Slot(uri=ALLIANCE.iupac, name="iupac", curie=ALLIANCE.curie('iupac'),
                   model_uri=DEFAULT_.iupac, domain=Molecule, range=Optional[str])

slots.formula = Slot(uri=ALLIANCE.formula, name="formula", curie=ALLIANCE.curie('formula'),
                   model_uri=DEFAULT_.formula, domain=Molecule, range=Optional[str])

slots.smiles = Slot(uri=ALLIANCE.smiles, name="smiles", curie=ALLIANCE.curie('smiles'),
                   model_uri=DEFAULT_.smiles, domain=Molecule, range=Optional[str])

slots.topics = Slot(uri="str(uriorcurie)", name="topics", curie=None,
                   model_uri=DEFAULT_.topics, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.PubMed_type = Slot(uri="str(uriorcurie)", name="PubMed_type", curie=None,
                   model_uri=DEFAULT_.PubMed_type, domain=InformationContentEntity, range=Optional[str])

slots.date_published = Slot(uri="str(uriorcurie)", name="date_published", curie=None,
                   model_uri=DEFAULT_.date_published, domain=InformationContentEntity, range=Optional[Union[str, XSDDate]])

slots.date_last_modified_in_PubMed = Slot(uri="str(uriorcurie)", name="date_last_modified_in_PubMed", curie=None,
                   model_uri=DEFAULT_.date_last_modified_in_PubMed, domain=InformationContentEntity, range=Optional[Union[str, XSDDate]])

slots.year_published = Slot(uri="str(uriorcurie)", name="year_published", curie=None,
                   model_uri=DEFAULT_.year_published, domain=InformationContentEntity, range=Optional[str])

slots.month_published = Slot(uri="str(uriorcurie)", name="month_published", curie=None,
                   model_uri=DEFAULT_.month_published, domain=InformationContentEntity, range=Optional[str])

slots.day_published = Slot(uri="str(uriorcurie)", name="day_published", curie=None,
                   model_uri=DEFAULT_.day_published, domain=InformationContentEntity, range=Optional[str])

slots.date_arrived_in_PubMed = Slot(uri="str(uriorcurie)", name="date_arrived_in_PubMed", curie=None,
                   model_uri=DEFAULT_.date_arrived_in_PubMed, domain=InformationContentEntity, range=Optional[Union[str, XSDDate]])

slots.mod_reference_types = Slot(uri="str(uriorcurie)", name="mod_reference_types", curie=None,
                   model_uri=DEFAULT_.mod_reference_types, domain=None, range=Optional[Union[str, List[str]]])

slots.tags = Slot(uri="str(uriorcurie)", name="tags", curie=None,
                   model_uri=DEFAULT_.tags, domain=None, range=Optional[Union[Union[str, "TagSet"], List[Union[str, "TagSet"]]]])

slots.issue_date = Slot(uri="str(uriorcurie)", name="issue_date", curie=None,
                   model_uri=DEFAULT_.issue_date, domain=InformationContentEntity, range=Optional[Union[str, XSDDate]])

slots.volume = Slot(uri="str(uriorcurie)", name="volume", curie=None,
                   model_uri=DEFAULT_.volume, domain=InformationContentEntity, range=Optional[str])

slots.pages = Slot(uri="str(uriorcurie)", name="pages", curie=None,
                   model_uri=DEFAULT_.pages, domain=InformationContentEntity, range=Optional[Union[str, List[str]]])

slots.abstract = Slot(uri="str(uriorcurie)", name="abstract", curie=None,
                   model_uri=DEFAULT_.abstract, domain=Reference, range=Optional[str])

slots.citation = Slot(uri="str(uriorcurie)", name="citation", curie=None,
                   model_uri=DEFAULT_.citation, domain=Reference, range=Optional[str])

slots.issue_name = Slot(uri="str(uriorcurie)", name="issue_name", curie=None,
                   model_uri=DEFAULT_.issue_name, domain=Reference, range=Optional[str])

slots.alliance_category = Slot(uri="str(uriorcurie)", name="alliance_category", curie=None,
                   model_uri=DEFAULT_.alliance_category, domain=Reference, range=Optional[str])

slots.keywords = Slot(uri="str(uriorcurie)", name="keywords", curie=None,
                   model_uri=DEFAULT_.keywords, domain=InformationContentEntity, range=Optional[Union[str, List[str]]])

slots.from_resource = Slot(uri="str(uriorcurie)", name="from_resource", curie=None,
                   model_uri=DEFAULT_.from_resource, domain=Reference, range=Optional[Union[str, ResourceCurie]])

slots.notes = Slot(uri="str(uriorcurie)", name="notes", curie=None,
                   model_uri=DEFAULT_.notes, domain=None, range=Optional[Union[str, List[str]]])

slots.hgvs_nomenclature = Slot(uri="str(uriorcurie)", name="hgvs_nomenclature", curie=None,
                   model_uri=DEFAULT_.hgvs_nomenclature, domain=Variant, range=Optional[str])

slots.genomic_reference_sequence = Slot(uri="str(uriorcurie)", name="genomic_reference_sequence", curie=None,
                   model_uri=DEFAULT_.genomic_reference_sequence, domain=Variant, range=Optional[str])

slots.genomic_variant_sequence = Slot(uri="str(uriorcurie)", name="genomic_variant_sequence", curie=None,
                   model_uri=DEFAULT_.genomic_variant_sequence, domain=Variant, range=Optional[str])

slots.padding_left = Slot(uri="str(uriorcurie)", name="padding_left", curie=None,
                   model_uri=DEFAULT_.padding_left, domain=Variant, range=Optional[str])

slots.padding_right = Slot(uri="str(uriorcurie)", name="padding_right", curie=None,
                   model_uri=DEFAULT_.padding_right, domain=Variant, range=Optional[Union[str, BiologicalSequence]])

slots.protein_sequence = Slot(uri="str(uriorcurie)", name="protein_sequence", curie=None,
                   model_uri=DEFAULT_.protein_sequence, domain=Variant, range=Optional[str])

slots.computed_gene = Slot(uri="str(uriorcurie)", name="computed_gene", curie=None,
                   model_uri=DEFAULT_.computed_gene, domain=Variant, range=Optional[Union[str, GeneCurie]])

slots.variant_of_transcript = Slot(uri="str(uriorcurie)", name="variant_of_transcript", curie=None,
                   model_uri=DEFAULT_.variant_of_transcript, domain=Variant, range=Optional[Union[str, TranscriptCurie]])

slots.variant_of_allele = Slot(uri="str(uriorcurie)", name="variant_of_allele", curie=None,
                   model_uri=DEFAULT_.variant_of_allele, domain=Variant, range=Optional[Union[str, AlleleCurie]])

slots.summary = Slot(uri=ALLIANCE.summary, name="summary", curie=ALLIANCE.curie('summary'),
                   model_uri=DEFAULT_.summary, domain=InformationContentEntity, range=Optional[str])

slots.copyright_date = Slot(uri=ALLIANCE.copyright_date, name="copyright_date", curie=ALLIANCE.curie('copyright_date'),
                   model_uri=DEFAULT_.copyright_date, domain=InformationContentEntity, range=Optional[Union[str, XSDDate]])

slots.authors = Slot(uri=ALLIANCE.authors, name="authors", curie=ALLIANCE.curie('authors'),
                   model_uri=DEFAULT_.authors, domain=InformationContentEntity, range=Optional[Union[Union[dict, "AuthorReference"], List[Union[dict, "AuthorReference"]]]])

slots.corresponding_author = Slot(uri=ALLIANCE.corresponding_author, name="corresponding_author", curie=ALLIANCE.curie('corresponding_author'),
                   model_uri=DEFAULT_.corresponding_author, domain=InformationContentEntity, range=Optional[Union[str, InformationContentEntityCurie]])

slots.first_name = Slot(uri=ALLIANCE.first_name, name="first_name", curie=ALLIANCE.curie('first_name'),
                   model_uri=DEFAULT_.first_name, domain=InformationContentEntity, range=Optional[Union[str, InformationContentEntityCurie]])

slots.middle_names = Slot(uri=ALLIANCE.middle_names, name="middle_names", curie=ALLIANCE.curie('middle_names'),
                   model_uri=DEFAULT_.middle_names, domain=InformationContentEntity, range=Optional[Union[str, InformationContentEntityCurie]])

slots.last_name = Slot(uri=ALLIANCE.last_name, name="last_name", curie=ALLIANCE.curie('last_name'),
                   model_uri=DEFAULT_.last_name, domain=InformationContentEntity, range=Optional[Union[str, InformationContentEntityCurie]])

slots.initials = Slot(uri=ALLIANCE.initials, name="initials", curie=ALLIANCE.curie('initials'),
                   model_uri=DEFAULT_.initials, domain=InformationContentEntity, range=Optional[Union[str, InformationContentEntityCurie]])

slots.title = Slot(uri=ALLIANCE.title, name="title", curie=ALLIANCE.curie('title'),
                   model_uri=DEFAULT_.title, domain=InformationContentEntity, range=Optional[str])

slots.volumes = Slot(uri=ALLIANCE.volumes, name="volumes", curie=ALLIANCE.curie('volumes'),
                   model_uri=DEFAULT_.volumes, domain=InformationContentEntity, range=Optional[str])

slots.publisher = Slot(uri=ALLIANCE.publisher, name="publisher", curie=ALLIANCE.curie('publisher'),
                   model_uri=DEFAULT_.publisher, domain=InformationContentEntity, range=Optional[Union[str, InformationContentEntityCurie]])

slots.address = Slot(uri=ALLIANCE.address, name="address", curie=ALLIANCE.curie('address'),
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
                   model_uri=DEFAULT_.orcid, domain=InformationContentEntity, range=Optional[str])

slots.phenotype_annotation = Slot(uri=DEFAULT_.phenotype_annotation, name="phenotype_annotation", curie=DEFAULT_.curie('phenotype_annotation'),
                   model_uri=DEFAULT_.phenotype_annotation, domain=None, range=Optional[Union[str, ExpressionAnnotationCurie]])

slots.experimental_condition = Slot(uri=DEFAULT_.experimental_condition, name="experimental_condition", curie=DEFAULT_.curie('experimental_condition'),
                   model_uri=DEFAULT_.experimental_condition, domain=None, range=Optional[Union[dict, ExperimentalCondition]])

slots.embryonic_cell_lines = Slot(uri=DEFAULT_.embryonic_cell_lines, name="embryonic_cell_lines", curie=DEFAULT_.curie('embryonic_cell_lines'),
                   model_uri=DEFAULT_.embryonic_cell_lines, domain=None, range=Optional[str])

slots.id = Slot(uri=DEFAULT_.id, name="id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.id, domain=None, range=Optional[str])

slots.person_id = Slot(uri=DEFAULT_.person_id, name="person id", curie=DEFAULT_.curie('person_id'),
                   model_uri=DEFAULT_.person_id, domain=None, range=URIRef)

slots.ExpressionAnnotation_has_figure = Slot(uri="str(uriorcurie)", name="ExpressionAnnotation_has_figure", curie=None,
                   model_uri=DEFAULT_.ExpressionAnnotation_has_figure, domain=ExpressionAnnotation, range=Optional[Union[str, FigureCurie]])

slots.ExpressionAnnotation_has_reference = Slot(uri="str(uriorcurie)", name="ExpressionAnnotation_has_reference", curie=None,
                   model_uri=DEFAULT_.ExpressionAnnotation_has_reference, domain=ExpressionAnnotation, range=Optional[Union[str, ReferenceCurie]])

slots.ExpressionAnnotationImagePane_subject = Slot(uri=ALLIANCE.subject, name="ExpressionAnnotationImagePane_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=DEFAULT_.ExpressionAnnotationImagePane_subject, domain=ExpressionAnnotationImagePane, range=Union[str, ExpressionAnnotationCurie])

slots.ExpressionAnnotationImagePane_object = Slot(uri=ALLIANCE.object, name="ExpressionAnnotationImagePane_object", curie=ALLIANCE.curie('object'),
                   model_uri=DEFAULT_.ExpressionAnnotationImagePane_object, domain=ExpressionAnnotationImagePane, range=Union[dict, "ImagePane"])

slots.ExpressionAnnotationExperimentalConditionAssociation_phenotype_annotation = Slot(uri=DEFAULT_.phenotype_annotation, name="ExpressionAnnotationExperimentalConditionAssociation_phenotype_annotation", curie=DEFAULT_.curie('phenotype_annotation'),
                   model_uri=DEFAULT_.ExpressionAnnotationExperimentalConditionAssociation_phenotype_annotation, domain=ExpressionAnnotationExperimentalConditionAssociation, range=Optional[Union[str, ExpressionAnnotationCurie]])

slots.ExpressionAnnotationExperimentalConditionAssociation_experimental_condition = Slot(uri=DEFAULT_.experimental_condition, name="ExpressionAnnotationExperimentalConditionAssociation_experimental_condition", curie=DEFAULT_.curie('experimental_condition'),
                   model_uri=DEFAULT_.ExpressionAnnotationExperimentalConditionAssociation_experimental_condition, domain=ExpressionAnnotationExperimentalConditionAssociation, range=Optional[Union[dict, "ExperimentalCondition"]])

slots.ExpressionAnnotationExperimentalConditionAssociation_predicate = Slot(uri=ALLIANCE.predicate, name="ExpressionAnnotationExperimentalConditionAssociation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=DEFAULT_.ExpressionAnnotationExperimentalConditionAssociation_predicate, domain=ExpressionAnnotationExperimentalConditionAssociation, range=Union[str, "ExpressionConditionRelationEnum"])

slots.Allele_synonyms = Slot(uri=ALLIANCE.synonyms, name="Allele_synonyms", curie=ALLIANCE.curie('synonyms'),
                   model_uri=DEFAULT_.Allele_synonyms, domain=Allele, range=Optional[Union[Union[dict, "Synonym"], List[Union[dict, "Synonym"]]]])

slots.Allele_germline_transmission_status = Slot(uri="str(uriorcurie)", name="Allele_germline_transmission_status", curie=None,
                   model_uri=DEFAULT_.Allele_germline_transmission_status, domain=Allele, range=Optional[str])

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

slots.MolecularMutation_mutation_type = Slot(uri="str(uriorcurie)", name="MolecularMutation_mutation_type", curie=None,
                   model_uri=DEFAULT_.MolecularMutation_mutation_type, domain=MolecularMutation, range=Union[str, SOTermCurie])

slots.BiologicalEntity_taxon = Slot(uri=ALLIANCE.taxon, name="BiologicalEntity_taxon", curie=ALLIANCE.curie('taxon'),
                   model_uri=DEFAULT_.BiologicalEntity_taxon, domain=BiologicalEntity, range=Union[str, URIorCURIE])

slots.Gene_symbol = Slot(uri=ALLIANCE.symbol, name="Gene_symbol", curie=ALLIANCE.curie('symbol'),
                   model_uri=DEFAULT_.Gene_symbol, domain=Gene, range=str)

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

slots.Figure_has_reference = Slot(uri="str(uriorcurie)", name="Figure_has_reference", curie=None,
                   model_uri=DEFAULT_.Figure_has_reference, domain=Figure, range=Union[str, ReferenceCurie])

slots.Image_has_figure = Slot(uri="str(uriorcurie)", name="Image_has_figure", curie=None,
                   model_uri=DEFAULT_.Image_has_figure, domain=Image, range=Union[str, FigureCurie])

slots.Image_image_x_origin = Slot(uri="str(uriorcurie)", name="Image_image_x_origin", curie=None,
                   model_uri=DEFAULT_.Image_image_x_origin, domain=Image, range=Optional[int])

slots.Image_image_y_origin = Slot(uri="str(uriorcurie)", name="Image_image_y_origin", curie=None,
                   model_uri=DEFAULT_.Image_image_y_origin, domain=Image, range=Optional[int])

slots.ImagePane_images = Slot(uri="str(uriorcurie)", name="ImagePane_images", curie=None,
                   model_uri=DEFAULT_.ImagePane_images, domain=ImagePane, range=Union[str, ImageCurie])

slots.ImagePane_image_x_origin = Slot(uri="str(uriorcurie)", name="ImagePane_image_x_origin", curie=None,
                   model_uri=DEFAULT_.ImagePane_image_x_origin, domain=ImagePane, range=Optional[int])

slots.ImagePane_image_y_origin = Slot(uri="str(uriorcurie)", name="ImagePane_image_y_origin", curie=None,
                   model_uri=DEFAULT_.ImagePane_image_y_origin, domain=ImagePane, range=Optional[int])

slots.OntologyTerm_definition = Slot(uri="str(uriorcurie)", name="OntologyTerm_definition", curie=None,
                   model_uri=DEFAULT_.OntologyTerm_definition, domain=OntologyTerm, range=Optional[str])

slots.ECOTerm_abbreviation = Slot(uri=ALLIANCE.abbreviation, name="ECOTerm_abbreviation", curie=ALLIANCE.curie('abbreviation'),
                   model_uri=DEFAULT_.ECOTerm_abbreviation, domain=ECOTerm, range=Optional[str])

slots.PhenotypeAnnotation_subject = Slot(uri=ALLIANCE.subject, name="PhenotypeAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=DEFAULT_.PhenotypeAnnotation_subject, domain=PhenotypeAnnotation, range=Union[str, BiologicalEntityCurie])

slots.PhenotypeAnnotation_phenotype_term = Slot(uri=ALLIANCE.phenotype_term, name="PhenotypeAnnotation_phenotype_term", curie=ALLIANCE.curie('phenotype_term'),
                   model_uri=DEFAULT_.PhenotypeAnnotation_phenotype_term, domain=PhenotypeAnnotation, range=Optional[Union[str, PhenotypeTermCurie]])

slots.PhenotypeAnnotation_object = Slot(uri=ALLIANCE.object, name="PhenotypeAnnotation_object", curie=ALLIANCE.curie('object'),
                   model_uri=DEFAULT_.PhenotypeAnnotation_object, domain=PhenotypeAnnotation, range=str)

slots.PhenotypeAnnotation_reference = Slot(uri=ALLIANCE.reference, name="PhenotypeAnnotation_reference", curie=ALLIANCE.curie('reference'),
                   model_uri=DEFAULT_.PhenotypeAnnotation_reference, domain=PhenotypeAnnotation, range=Optional[Union[str, ReferenceCurie]])

slots.PhenotypeAnnotation_creation_date = Slot(uri=ALLIANCE.creation_date, name="PhenotypeAnnotation_creation_date", curie=ALLIANCE.curie('creation_date'),
                   model_uri=DEFAULT_.PhenotypeAnnotation_creation_date, domain=PhenotypeAnnotation, range=Union[str, XSDDate])

slots.GenePhenotypeAnnotation_subject = Slot(uri=ALLIANCE.subject, name="GenePhenotypeAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=DEFAULT_.GenePhenotypeAnnotation_subject, domain=GenePhenotypeAnnotation, range=Union[str, GeneCurie])

slots.AllelePhenotypeAnnotation_subject = Slot(uri=ALLIANCE.subject, name="AllelePhenotypeAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=DEFAULT_.AllelePhenotypeAnnotation_subject, domain=AllelePhenotypeAnnotation, range=Union[str, AlleleCurie])

slots.AllelePhenotypeAnnotation_inferred_gene = Slot(uri=ALLIANCE.inferred_gene, name="AllelePhenotypeAnnotation_inferred_gene", curie=ALLIANCE.curie('inferred_gene'),
                   model_uri=DEFAULT_.AllelePhenotypeAnnotation_inferred_gene, domain=AllelePhenotypeAnnotation, range=Optional[Union[str, GeneCurie]])

slots.AGMPhenotypeAnnotation_subject = Slot(uri=ALLIANCE.subject, name="AGMPhenotypeAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=DEFAULT_.AGMPhenotypeAnnotation_subject, domain=AGMPhenotypeAnnotation, range=Union[str, AffectedGenomicModelCurie])

slots.AGMPhenotypeAnnotation_inferred_gene = Slot(uri=ALLIANCE.inferred_gene, name="AGMPhenotypeAnnotation_inferred_gene", curie=ALLIANCE.curie('inferred_gene'),
                   model_uri=DEFAULT_.AGMPhenotypeAnnotation_inferred_gene, domain=AGMPhenotypeAnnotation, range=Optional[Union[str, GeneCurie]])

slots.AGMPhenotypeAnnotation_inferred_allele = Slot(uri=ALLIANCE.inferred_allele, name="AGMPhenotypeAnnotation_inferred_allele", curie=ALLIANCE.curie('inferred_allele'),
                   model_uri=DEFAULT_.AGMPhenotypeAnnotation_inferred_allele, domain=AGMPhenotypeAnnotation, range=Optional[Union[str, AlleleCurie]])

slots.DiseaseAnnotation_unique_id = Slot(uri=ALLIANCE.unique_id, name="DiseaseAnnotation_unique_id", curie=ALLIANCE.curie('unique_id'),
                   model_uri=DEFAULT_.DiseaseAnnotation_unique_id, domain=DiseaseAnnotation, range=Optional[str])

slots.DiseaseAnnotation_mod_id = Slot(uri=ALLIANCE.mod_id, name="DiseaseAnnotation_mod_id", curie=ALLIANCE.curie('mod_id'),
                   model_uri=DEFAULT_.DiseaseAnnotation_mod_id, domain=DiseaseAnnotation, range=Optional[str])

slots.DiseaseAnnotation_subject = Slot(uri=ALLIANCE.subject, name="DiseaseAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=DEFAULT_.DiseaseAnnotation_subject, domain=DiseaseAnnotation, range=Union[str, BiologicalEntityCurie])

slots.DiseaseAnnotation_predicate = Slot(uri=ALLIANCE.predicate, name="DiseaseAnnotation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=DEFAULT_.DiseaseAnnotation_predicate, domain=DiseaseAnnotation, range=str)

slots.DiseaseAnnotation_negated = Slot(uri=ALLIANCE.negated, name="DiseaseAnnotation_negated", curie=ALLIANCE.curie('negated'),
                   model_uri=DEFAULT_.DiseaseAnnotation_negated, domain=DiseaseAnnotation, range=Optional[Union[bool, Bool]])

slots.DiseaseAnnotation_object = Slot(uri=ALLIANCE.object, name="DiseaseAnnotation_object", curie=ALLIANCE.curie('object'),
                   model_uri=DEFAULT_.DiseaseAnnotation_object, domain=DiseaseAnnotation, range=Union[str, DOTermCurie])

slots.DiseaseAnnotation_data_provider = Slot(uri=ALLIANCE.data_provider, name="DiseaseAnnotation_data_provider", curie=ALLIANCE.curie('data_provider'),
                   model_uri=DEFAULT_.DiseaseAnnotation_data_provider, domain=DiseaseAnnotation, range=Union[str, List[str]])

slots.DiseaseAnnotation_annotation_type = Slot(uri=ALLIANCE.annotation_type, name="DiseaseAnnotation_annotation_type", curie=ALLIANCE.curie('annotation_type'),
                   model_uri=DEFAULT_.DiseaseAnnotation_annotation_type, domain=DiseaseAnnotation, range=Optional[Union[str, "AnnotationTypeEnum"]])

slots.DiseaseAnnotation_with = Slot(uri=ALLIANCE.with, name="DiseaseAnnotation_with", curie=ALLIANCE.curie('with'),
                   model_uri=DEFAULT_.DiseaseAnnotation_with, domain=DiseaseAnnotation, range=Optional[Union[str, GeneCurie]])

slots.DiseaseAnnotation_reference = Slot(uri=ALLIANCE.reference, name="DiseaseAnnotation_reference", curie=ALLIANCE.curie('reference'),
                   model_uri=DEFAULT_.DiseaseAnnotation_reference, domain=DiseaseAnnotation, range=Union[str, ReferenceCurie])

slots.DiseaseAnnotation_evidence_codes = Slot(uri=ALLIANCE.evidence_codes, name="DiseaseAnnotation_evidence_codes", curie=ALLIANCE.curie('evidence_codes'),
                   model_uri=DEFAULT_.DiseaseAnnotation_evidence_codes, domain=DiseaseAnnotation, range=Union[Union[str, ECOTermCurie], List[Union[str, ECOTermCurie]]])

slots.DiseaseAnnotation_genetic_sex = Slot(uri=ALLIANCE.genetic_sex, name="DiseaseAnnotation_genetic_sex", curie=ALLIANCE.curie('genetic_sex'),
                   model_uri=DEFAULT_.DiseaseAnnotation_genetic_sex, domain=DiseaseAnnotation, range=Optional[Union[str, "GeneticSexEnum"]])

slots.GeneDiseaseAnnotation_subject = Slot(uri=ALLIANCE.subject, name="GeneDiseaseAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=DEFAULT_.GeneDiseaseAnnotation_subject, domain=GeneDiseaseAnnotation, range=Union[str, GeneCurie])

slots.GeneDiseaseAnnotation_predicate = Slot(uri=ALLIANCE.predicate, name="GeneDiseaseAnnotation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=DEFAULT_.GeneDiseaseAnnotation_predicate, domain=GeneDiseaseAnnotation, range=Union[str, "GeneDiseaseRelationEnum"])

slots.AlleleDiseaseAnnotation_subject = Slot(uri=ALLIANCE.subject, name="AlleleDiseaseAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=DEFAULT_.AlleleDiseaseAnnotation_subject, domain=AlleleDiseaseAnnotation, range=Union[str, AlleleCurie])

slots.AlleleDiseaseAnnotation_predicate = Slot(uri=ALLIANCE.predicate, name="AlleleDiseaseAnnotation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=DEFAULT_.AlleleDiseaseAnnotation_predicate, domain=AlleleDiseaseAnnotation, range=Union[str, "AlleleDiseaseRelationEnum"])

slots.AlleleDiseaseAnnotation_inferred_gene = Slot(uri=ALLIANCE.inferred_gene, name="AlleleDiseaseAnnotation_inferred_gene", curie=ALLIANCE.curie('inferred_gene'),
                   model_uri=DEFAULT_.AlleleDiseaseAnnotation_inferred_gene, domain=AlleleDiseaseAnnotation, range=Optional[Union[str, GeneCurie]])

slots.AGMDiseaseAnnotation_subject = Slot(uri=ALLIANCE.subject, name="AGMDiseaseAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=DEFAULT_.AGMDiseaseAnnotation_subject, domain=AGMDiseaseAnnotation, range=Union[str, AffectedGenomicModelCurie])

slots.AGMDiseaseAnnotation_predicate = Slot(uri=ALLIANCE.predicate, name="AGMDiseaseAnnotation_predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=DEFAULT_.AGMDiseaseAnnotation_predicate, domain=AGMDiseaseAnnotation, range=Union[str, "AgmDiseaseRelationEnum"])

slots.AGMDiseaseAnnotation_inferred_gene = Slot(uri=ALLIANCE.inferred_gene, name="AGMDiseaseAnnotation_inferred_gene", curie=ALLIANCE.curie('inferred_gene'),
                   model_uri=DEFAULT_.AGMDiseaseAnnotation_inferred_gene, domain=AGMDiseaseAnnotation, range=Optional[Union[str, GeneCurie]])

slots.AGMDiseaseAnnotation_inferred_allele = Slot(uri=ALLIANCE.inferred_allele, name="AGMDiseaseAnnotation_inferred_allele", curie=ALLIANCE.curie('inferred_allele'),
                   model_uri=DEFAULT_.AGMDiseaseAnnotation_inferred_allele, domain=AGMDiseaseAnnotation, range=Optional[Union[str, AlleleCurie]])

slots.ExperimentalCondition_unique_id = Slot(uri=ALLIANCE.unique_id, name="ExperimentalCondition_unique_id", curie=ALLIANCE.curie('unique_id'),
                   model_uri=DEFAULT_.ExperimentalCondition_unique_id, domain=ExperimentalCondition, range=Optional[str])

slots.ExperimentalCondition_condition_class = Slot(uri=ALLIANCE.condition_class, name="ExperimentalCondition_condition_class", curie=ALLIANCE.curie('condition_class'),
                   model_uri=DEFAULT_.ExperimentalCondition_condition_class, domain=ExperimentalCondition, range=Union[str, ZECOTermCurie])

slots.ExperimentalCondition_condition_statement = Slot(uri=ALLIANCE.condition_statement, name="ExperimentalCondition_condition_statement", curie=ALLIANCE.curie('condition_statement'),
                   model_uri=DEFAULT_.ExperimentalCondition_condition_statement, domain=ExperimentalCondition, range=str)

slots.ExperimentalCondition_condition_id = Slot(uri=ALLIANCE.condition_id, name="ExperimentalCondition_condition_id", curie=ALLIANCE.curie('condition_id'),
                   model_uri=DEFAULT_.ExperimentalCondition_condition_id, domain=ExperimentalCondition, range=Optional[Union[str, ExperimentalConditionOntologyTermCurie]])

slots.ExperimentalCondition_condition_quantity = Slot(uri=ALLIANCE.condition_quantity, name="ExperimentalCondition_condition_quantity", curie=ALLIANCE.curie('condition_quantity'),
                   model_uri=DEFAULT_.ExperimentalCondition_condition_quantity, domain=ExperimentalCondition, range=Optional[str])

slots.ExperimentalCondition_condition_anatomy = Slot(uri=ALLIANCE.condition_anatomy, name="ExperimentalCondition_condition_anatomy", curie=ALLIANCE.curie('condition_anatomy'),
                   model_uri=DEFAULT_.ExperimentalCondition_condition_anatomy, domain=ExperimentalCondition, range=Optional[Union[str, AnatomicalTermCurie]])

slots.ExperimentalCondition_condition_gene_ontology = Slot(uri=ALLIANCE.condition_gene_ontology, name="ExperimentalCondition_condition_gene_ontology", curie=ALLIANCE.curie('condition_gene_ontology'),
                   model_uri=DEFAULT_.ExperimentalCondition_condition_gene_ontology, domain=ExperimentalCondition, range=Optional[Union[str, GOTermCurie]])

slots.ExperimentalCondition_condition_taxon = Slot(uri=ALLIANCE.condition_taxon, name="ExperimentalCondition_condition_taxon", curie=ALLIANCE.curie('condition_taxon'),
                   model_uri=DEFAULT_.ExperimentalCondition_condition_taxon, domain=ExperimentalCondition, range=Optional[Union[str, OntologyTermCurie]])

slots.ExperimentalCondition_condition_chemical = Slot(uri=ALLIANCE.condition_chemical, name="ExperimentalCondition_condition_chemical", curie=ALLIANCE.curie('condition_chemical'),
                   model_uri=DEFAULT_.ExperimentalCondition_condition_chemical, domain=ExperimentalCondition, range=Optional[Union[str, OntologyTermCurie]])

slots.ExperimentalCondition_paper_handles = Slot(uri=ALLIANCE.paper_handles, name="ExperimentalCondition_paper_handles", curie=ALLIANCE.curie('paper_handles'),
                   model_uri=DEFAULT_.ExperimentalCondition_paper_handles, domain=ExperimentalCondition, range=Optional[Union[Union[dict, "PaperHandle"], List[Union[dict, "PaperHandle"]]]])

slots.ConditionRelation_unique_id = Slot(uri=ALLIANCE.unique_id, name="ConditionRelation_unique_id", curie=ALLIANCE.curie('unique_id'),
                   model_uri=DEFAULT_.ConditionRelation_unique_id, domain=ConditionRelation, range=Optional[str])

slots.ConditionRelation_condition_relation_type = Slot(uri=ALLIANCE.condition_relation_type, name="ConditionRelation_condition_relation_type", curie=ALLIANCE.curie('condition_relation_type'),
                   model_uri=DEFAULT_.ConditionRelation_condition_relation_type, domain=ConditionRelation, range=Union[str, "ConditionRelationEnum"])

slots.Molecule_name = Slot(uri=ALLIANCE.name, name="Molecule_name", curie=ALLIANCE.curie('name'),
                   model_uri=DEFAULT_.Molecule_name, domain=Molecule, range=str)

slots.PaperHandle_reference = Slot(uri=ALLIANCE.reference, name="PaperHandle_reference", curie=ALLIANCE.curie('reference'),
                   model_uri=DEFAULT_.PaperHandle_reference, domain=PaperHandle, range=Union[str, ReferenceCurie])

slots.PaperHandle_handle = Slot(uri=ALLIANCE.handle, name="PaperHandle_handle", curie=ALLIANCE.curie('handle'),
                   model_uri=DEFAULT_.PaperHandle_handle, domain=PaperHandle, range=str)

slots.Reference_id = Slot(uri=DEFAULT_.id, name="Reference_id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.Reference_id, domain=Reference, range=Optional[str])

slots.Resource_id = Slot(uri=DEFAULT_.id, name="Resource_id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.Resource_id, domain=Resource, range=Optional[str])

slots.Resource_title = Slot(uri=ALLIANCE.title, name="Resource_title", curie=ALLIANCE.curie('title'),
                   model_uri=DEFAULT_.Resource_title, domain=Resource, range=Optional[str])

slots.Person_person_id = Slot(uri=DEFAULT_.person_id, name="Person_person id", curie=DEFAULT_.curie('person_id'),
                   model_uri=DEFAULT_.Person_person_id, domain=Person, range=Union[str, PersonPersonId])
