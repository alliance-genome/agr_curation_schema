# Auto generated from expression.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-02-09T16:11:29
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
class ExpressionExperimentCurie(URIorCURIE):
    pass


class BiologicalEntityCurie(URIorCURIE):
    pass


class AntibodyCurie(BiologicalEntityCurie):
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


class NCBITaxonTermCurie(OntologyTermCurie):
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


class PhenotypeAnnotationCurie(URIorCURIE):
    pass


class GenePhenotypeAnnotationCurie(PhenotypeAnnotationCurie):
    pass


class AllelePhenotypeAnnotationCurie(PhenotypeAnnotationCurie):
    pass


class AGMPhenotypeAnnotationCurie(PhenotypeAnnotationCurie):
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


class VocabularyName(extended_str):
    pass


@dataclass
class ExpressionExperiment(YAMLRoot):
    """
    Defined by the gene of interest, the specimen, the assay, the reagents (Antibody, Probe), and the reference. It
    groups ExpressionAnnotations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ExpressionExperiment")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ExpressionExperiment"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ExpressionExperiment")

    curie: Union[str, ExpressionExperimentCurie] = None
    biological_entity_assayed: Union[str, BiologicalEntityCurie] = None
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
    references: Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]] = empty_list()
    assay_used: Optional[Union[str, MMOTermCurie]] = None
    reagents_used: Optional[Union[Union[dict, "Reagent"], List[Union[dict, "Reagent"]]]] = empty_list()
    specimen_genomic_model: Optional[Union[str, AffectedGenomicModelCurie]] = None
    specimen_alleles: Optional[Union[Union[str, AlleleCurie], List[Union[str, AlleleCurie]]]] = empty_list()
    condition_relations: Optional[Union[Union[dict, "ConditionRelation"], List[Union[dict, "ConditionRelation"]]]] = empty_list()
    table_key: Optional[int] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ExpressionExperimentCurie):
            self.curie = ExpressionExperimentCurie(self.curie)

        if self._is_empty(self.biological_entity_assayed):
            self.MissingRequiredField("biological_entity_assayed")
        if not isinstance(self.biological_entity_assayed, BiologicalEntityCurie):
            self.biological_entity_assayed = BiologicalEntityCurie(self.biological_entity_assayed)

        if self._is_empty(self.created_by):
            self.MissingRequiredField("created_by")
        if not isinstance(self.created_by, Person):
            self.created_by = Person(**as_dict(self.created_by))

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, Person):
            self.modified_by = Person(**as_dict(self.modified_by))

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, ReferenceCurie) else ReferenceCurie(v) for v in self.references]

        if self.assay_used is not None and not isinstance(self.assay_used, MMOTermCurie):
            self.assay_used = MMOTermCurie(self.assay_used)

        if not isinstance(self.reagents_used, list):
            self.reagents_used = [self.reagents_used] if self.reagents_used is not None else []
        self.reagents_used = [v if isinstance(v, Reagent) else Reagent(**as_dict(v)) for v in self.reagents_used]

        if self.specimen_genomic_model is not None and not isinstance(self.specimen_genomic_model, AffectedGenomicModelCurie):
            self.specimen_genomic_model = AffectedGenomicModelCurie(self.specimen_genomic_model)

        if not isinstance(self.specimen_alleles, list):
            self.specimen_alleles = [self.specimen_alleles] if self.specimen_alleles is not None else []
        self.specimen_alleles = [v if isinstance(v, AlleleCurie) else AlleleCurie(v) for v in self.specimen_alleles]

        if not isinstance(self.condition_relations, list):
            self.condition_relations = [self.condition_relations] if self.condition_relations is not None else []
        self.condition_relations = [v if isinstance(v, ConditionRelation) else ConditionRelation(**as_dict(v)) for v in self.condition_relations]

        if self.table_key is not None and not isinstance(self.table_key, int):
            self.table_key = int(self.table_key)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

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

    belongs_to_expression_experiment: Union[str, ExpressionExperimentCurie] = None
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
    when_expressed: Optional[Union[dict, "TemporalContext"]] = None
    where_expressed: Optional[Union[dict, "AnatomicalSite"]] = None
    expression_qualifiers: Optional[Union[str, "ExpressionQualifierSet"]] = None
    negated: Optional[Union[bool, Bool]] = None
    uncertain: Optional[Union[bool, Bool]] = None
    associated_with_figure: Optional[Union[Union[str, FigureCurie], List[Union[str, FigureCurie]]]] = empty_list()
    has_reference: Optional[Union[str, ReferenceCurie]] = None
    table_key: Optional[int] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.belongs_to_expression_experiment):
            self.MissingRequiredField("belongs_to_expression_experiment")
        if not isinstance(self.belongs_to_expression_experiment, ExpressionExperimentCurie):
            self.belongs_to_expression_experiment = ExpressionExperimentCurie(self.belongs_to_expression_experiment)

        if self._is_empty(self.created_by):
            self.MissingRequiredField("created_by")
        if not isinstance(self.created_by, Person):
            self.created_by = Person(**as_dict(self.created_by))

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, Person):
            self.modified_by = Person(**as_dict(self.modified_by))

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

        if self.has_reference is not None and not isinstance(self.has_reference, ReferenceCurie):
            self.has_reference = ReferenceCurie(self.has_reference)

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
    The developmental stage and/or age of the specimen in an annotation. Developmental_stage_stop is optional. Add an
    uncertainty flag here?
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/TemporalContext")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "TemporalContext"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/TemporalContext")

    developmental_stage_start: Optional[Union[str, StageTermCurie]] = None
    developmental_stage_stop: Optional[Union[str, StageTermCurie]] = None
    age: Optional[str] = None
    temporal_qualifiers: Optional[Union[str, "TemporalQualifierSet"]] = None
    stage_uncertainty: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.developmental_stage_start is not None and not isinstance(self.developmental_stage_start, StageTermCurie):
            self.developmental_stage_start = StageTermCurie(self.developmental_stage_start)

        if self.developmental_stage_stop is not None and not isinstance(self.developmental_stage_stop, StageTermCurie):
            self.developmental_stage_stop = StageTermCurie(self.developmental_stage_stop)

        if self.age is not None and not isinstance(self.age, str):
            self.age = str(self.age)

        if self.temporal_qualifiers is not None and not isinstance(self.temporal_qualifiers, TemporalQualifierSet):
            self.temporal_qualifiers = TemporalQualifierSet(self.temporal_qualifiers)

        if self.stage_uncertainty is not None and not isinstance(self.stage_uncertainty, str):
            self.stage_uncertainty = str(self.stage_uncertainty)

        super().__post_init__(**kwargs)


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
    taxon: Union[str, NCBITaxonTermCurie] = None
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
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
        if not isinstance(self.created_by, Person):
            self.created_by = Person(**as_dict(self.created_by))

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, Person):
            self.modified_by = Person(**as_dict(self.modified_by))

        if self.table_key is not None and not isinstance(self.table_key, int):
            self.table_key = int(self.table_key)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Antibody")

    curie: Union[str, AntibodyCurie] = None
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
    name: str = None
    clonality: Union[str, "AntibodyClonalitySet"] = None
    table_key: Optional[int] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None
    antigen_taxon: Optional[Union[str, NCBITaxonTermCurie]] = None
    heavy_chain_isotype: Optional[Union[str, "HeavyChainIsotypeSet"]] = None
    light_chain_isotype: Optional[Union[str, "LightChainIsotypeSet"]] = None
    antibody_target_genes: Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]] = empty_list()
    cross_references: Optional[Union[Dict[Union[str, CrossReferenceCurie], Union[dict, "CrossReference"]], List[Union[dict, "CrossReference"]]]] = empty_dict()
    secondary_identifiers: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    references: Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]] = empty_list()
    original_reference: Optional[Union[str, ReferenceCurie]] = None
    taxon: Optional[Union[str, NCBITaxonTermCurie]] = None
    generated_by: Optional[Union[Union[dict, "Agent"], List[Union[dict, "Agent"]]]] = empty_list()
    manufactured_by: Optional[Union[Union[dict, "Agent"], List[Union[dict, "Agent"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, AntibodyCurie):
            self.curie = AntibodyCurie(self.curie)

        if self._is_empty(self.created_by):
            self.MissingRequiredField("created_by")
        if not isinstance(self.created_by, Person):
            self.created_by = Person(**as_dict(self.created_by))

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, Person):
            self.modified_by = Person(**as_dict(self.modified_by))

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

        if self.taxon is not None and not isinstance(self.taxon, NCBITaxonTermCurie):
            self.taxon = NCBITaxonTermCurie(self.taxon)

        if not isinstance(self.generated_by, list):
            self.generated_by = [self.generated_by] if self.generated_by is not None else []
        self.generated_by = [v if isinstance(v, Agent) else Agent(**as_dict(v)) for v in self.generated_by]

        if not isinstance(self.manufactured_by, list):
            self.manufactured_by = [self.manufactured_by] if self.manufactured_by is not None else []
        self.manufactured_by = [v if isinstance(v, Agent) else Agent(**as_dict(v)) for v in self.manufactured_by]

        super().__post_init__(**kwargs)


@dataclass
class GenomicEntity(BiologicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GenomicEntity
    class_class_curie: ClassVar[str] = "alliance:GenomicEntity"
    class_name: ClassVar[str] = "GenomicEntity"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/GenomicEntity")

    curie: Union[str, GenomicEntityCurie] = None
    taxon: Union[str, NCBITaxonTermCurie] = None
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
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
    taxon: Union[str, NCBITaxonTermCurie] = None
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
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
    taxon: Union[str, NCBITaxonTermCurie] = None
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
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
    taxon: Union[str, NCBITaxonTermCurie] = None
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
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
    taxon: Union[str, NCBITaxonTermCurie] = None
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
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
    taxon: Union[str, NCBITaxonTermCurie] = None
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None

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
    taxon: Union[str, NCBITaxonTermCurie] = None
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
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

    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
    table_key: Optional[int] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.created_by):
            self.MissingRequiredField("created_by")
        if not isinstance(self.created_by, Person):
            self.created_by = Person(**as_dict(self.created_by))

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, Person):
            self.modified_by = Person(**as_dict(self.modified_by))

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
class Note(YAMLRoot):
    """
    Note object for capturing free-text describing some attribute of an entity, coupled with a 'note type', private
    boolean, and an optional list of references.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Note
    class_class_curie: ClassVar[str] = "alliance:Note"
    class_name: ClassVar[str] = "Note"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Note")

    free_text: str = None
    note_type: Union[dict, "VocabularyTerm"] = None
    private: Union[bool, Bool] = None
    references: Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.free_text):
            self.MissingRequiredField("free_text")
        if not isinstance(self.free_text, str):
            self.free_text = str(self.free_text)

        if self._is_empty(self.note_type):
            self.MissingRequiredField("note_type")
        if not isinstance(self.note_type, VocabularyTerm):
            self.note_type = VocabularyTerm(**as_dict(self.note_type))

        if self._is_empty(self.private):
            self.MissingRequiredField("private")
        if not isinstance(self.private, Bool):
            self.private = Bool(self.private)

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
class GeneExpressionStatement(EntityStatement):
    """
    Free-text describing some aspect(s) of a gene's expression, particularly nuanced information that is not readily
    captured in annotations. May summarize data from many annotations and/or many publications.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/GeneExpressionStatement")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "GeneExpressionStatement"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/GeneExpressionStatement")

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

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ExpressionExperimentStatement")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ExpressionExperimentStatement"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ExpressionExperimentStatement")

    statement_subject: Optional[Union[str, ExpressionExperimentCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.statement_subject is not None and not isinstance(self.statement_subject, ExpressionExperimentCurie):
            self.statement_subject = ExpressionExperimentCurie(self.statement_subject)

        super().__post_init__(**kwargs)


@dataclass
class ExpressionAnnotationStatement(EntityStatement):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ExpressionAnnotationStatement")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ExpressionAnnotationStatement"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ExpressionAnnotationStatement")

    statement_subject: Optional[Union[dict, ExpressionAnnotation]] = None
    statement_type: Optional[Union[str, "ExpressionStatementTypeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.statement_subject is not None and not isinstance(self.statement_subject, ExpressionAnnotation):
            self.statement_subject = ExpressionAnnotation(**as_dict(self.statement_subject))

        if self.statement_type is not None and not isinstance(self.statement_type, ExpressionStatementTypeEnum):
            self.statement_type = ExpressionStatementTypeEnum(self.statement_type)

        super().__post_init__(**kwargs)


@dataclass
class AntibodyNote(EntityStatement):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/antibody.yaml/AntibodyNote")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AntibodyNote"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/AntibodyNote")

    note_type: Optional[Union[str, "AntibodyNoteTypeSet"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.note_type is not None and not isinstance(self.note_type, AntibodyNoteTypeSet):
            self.note_type = AntibodyNoteTypeSet(self.note_type)

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
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
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
        if not isinstance(self.created_by, Person):
            self.created_by = Person(**as_dict(self.created_by))

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, Person):
            self.modified_by = Person(**as_dict(self.modified_by))

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
    associated_with_figure: Union[str, FigureCurie] = None
    width: int = None
    height: int = None
    image_file: Union[dict, File] = None
    image_medium_file: Union[dict, File] = None
    image_thumbnail_file: Union[dict, File] = None
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
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
        if not isinstance(self.created_by, Person):
            self.created_by = Person(**as_dict(self.created_by))

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, Person):
            self.modified_by = Person(**as_dict(self.modified_by))

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

    from_image: Union[str, ImageCurie] = None
    width: int = None
    height: int = None
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
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
        if not isinstance(self.created_by, Person):
            self.created_by = Person(**as_dict(self.created_by))

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, Person):
            self.modified_by = Person(**as_dict(self.modified_by))

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
class NCBITaxonTerm(OntologyTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/NCBITaxonTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "NCBITaxonTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/NCBITaxonTerm")

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
class DAOTerm(AnatomicalTerm):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/DAOTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DAOTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/DAOTerm")

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
class ChemicalTerm(OntologyTerm):
    """
    An ontology term representing a chemical or molecule
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/ontologyTerm.yaml/ChemicalTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ChemicalTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ChemicalTerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/CHEBITerm")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Molecule")

    curie: Union[str, MoleculeCurie] = None
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
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
        if not isinstance(self.created_by, Person):
            self.created_by = Person(**as_dict(self.created_by))

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, Person):
            self.modified_by = Person(**as_dict(self.modified_by))

        if self.table_key is not None and not isinstance(self.table_key, int):
            self.table_key = int(self.table_key)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

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
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
    single_reference: Optional[Union[str, ReferenceCurie]] = None
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
        if not isinstance(self.created_by, Person):
            self.created_by = Person(**as_dict(self.created_by))

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, Person):
            self.modified_by = Person(**as_dict(self.modified_by))

        if self.single_reference is not None and not isinstance(self.single_reference, ReferenceCurie):
            self.single_reference = ReferenceCurie(self.single_reference)

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
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
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
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
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
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
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
    single_reference: Union[str, ReferenceCurie] = None
    data_provider: Union[str, List[str]] = None
    subject: Union[str, BiologicalEntityCurie] = None
    predicate: str = None
    object: Union[str, DOTermCurie] = None
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
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

        if self._is_empty(self.single_reference):
            self.MissingRequiredField("single_reference")
        if not isinstance(self.single_reference, ReferenceCurie):
            self.single_reference = ReferenceCurie(self.single_reference)

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
        if not isinstance(self.created_by, Person):
            self.created_by = Person(**as_dict(self.created_by))

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, Person):
            self.modified_by = Person(**as_dict(self.modified_by))

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
    single_reference: Union[str, ReferenceCurie] = None
    data_provider: Union[str, List[str]] = None
    object: Union[str, DOTermCurie] = None
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
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
    single_reference: Union[str, ReferenceCurie] = None
    data_provider: Union[str, List[str]] = None
    object: Union[str, DOTermCurie] = None
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
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
    single_reference: Union[str, ReferenceCurie] = None
    data_provider: Union[str, List[str]] = None
    object: Union[str, DOTermCurie] = None
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
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
    condition_taxon: Optional[Union[str, NCBITaxonTermCurie]] = None
    condition_chemical: Optional[Union[str, OntologyTermCurie]] = None

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

        if self.condition_taxon is not None and not isinstance(self.condition_taxon, NCBITaxonTermCurie):
            self.condition_taxon = NCBITaxonTermCurie(self.condition_taxon)

        if self.condition_chemical is not None and not isinstance(self.condition_chemical, OntologyTermCurie):
            self.condition_chemical = OntologyTermCurie(self.condition_chemical)

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

    single_reference: Union[str, ReferenceCurie] = None
    handle: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.single_reference):
            self.MissingRequiredField("single_reference")
        if not isinstance(self.single_reference, ReferenceCurie):
            self.single_reference = ReferenceCurie(self.single_reference)

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
    taxon: Union[str, NCBITaxonTermCurie] = None
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
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
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
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
        if not isinstance(self.created_by, Person):
            self.created_by = Person(**as_dict(self.created_by))

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, Person):
            self.modified_by = Person(**as_dict(self.modified_by))

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
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
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
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
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
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    initials: Optional[Union[str, InformationContentEntityCurie]] = None
    cross_references: Optional[Union[Dict[Union[str, CrossReferenceCurie], Union[dict, CrossReference]], List[Union[dict, CrossReference]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.corresponding_author is not None and not isinstance(self.corresponding_author, InformationContentEntityCurie):
            self.corresponding_author = InformationContentEntityCurie(self.corresponding_author)

        if self.first_name is not None and not isinstance(self.first_name, str):
            self.first_name = str(self.first_name)

        if self.middle_name is not None and not isinstance(self.middle_name, str):
            self.middle_name = str(self.middle_name)

        if self.last_name is not None and not isinstance(self.last_name, str):
            self.last_name = str(self.last_name)

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
    created_by: Union[dict, "Person"] = None
    modified_by: Union[dict, "Person"] = None
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

    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    first_name: Optional[str] = None
    orcid: Optional[Union[str, URIorCURIE]] = None
    emails: Optional[Union[str, List[str]]] = empty_list()
    old_emails: Optional[Union[str, List[str]]] = empty_list()
    mod_id: Optional[str] = None
    unique_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        if self.mod_id is not None and not isinstance(self.mod_id, str):
            self.mod_id = str(self.mod_id)

        if self.unique_id is not None and not isinstance(self.unique_id, str):
            self.unique_id = str(self.unique_id)

        super().__post_init__(**kwargs)


@dataclass
class LoggedInPerson(Person):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.LoggedInPerson
    class_class_curie: ClassVar[str] = "alliance:LoggedInPerson"
    class_name: ClassVar[str] = "LoggedInPerson"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/LoggedInPerson")

    okta_id: str = None
    okta_email: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
class VocabularyTerm(YAMLRoot):
    """
    A concept or class in a simple vocabulary.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/controlledVocabulary.yaml/VocabularyTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "VocabularyTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/VocabularyTerm")

    name: str = None
    created_by: Union[dict, Person] = None
    modified_by: Union[dict, Person] = None
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
        if not isinstance(self.created_by, Person):
            self.created_by = Person(**as_dict(self.created_by))

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, Person):
            self.modified_by = Person(**as_dict(self.modified_by))

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/Vocabulary")

    name: Union[str, VocabularyName] = None
    created_by: Union[dict, Person] = None
    modified_by: Union[dict, Person] = None
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
        if not isinstance(self.created_by, Person):
            self.created_by = Person(**as_dict(self.created_by))

        if self._is_empty(self.modified_by):
            self.MissingRequiredField("modified_by")
        if not isinstance(self.modified_by, Person):
            self.modified_by = Person(**as_dict(self.modified_by))

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

    progressive = PermissibleValue(text="progressive",
                                             description="An event that gets more pronounced with time.")
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
    when_expressed_note = PermissibleValue(text="when_expressed_note",
                                                             description="Additional free-text describing the stage/age of expression in an expression annotation.")
    where_expressed_note = PermissibleValue(text="where_expressed_note",
                                                               description="Additional free-text describing the anatomical site of expression in an expression annotation.")
    expression_annotation_note = PermissibleValue(text="expression_annotation_note",
                                                                           description="Additional free-text describing other aspects of an expression annotation. For example, only in the head neurons, only when JNK is activated, etc. Corresponds to note type #1 of AGR-1407.")

    _defn = EnumDefinition(
        name="ExpressionStatementTypeEnum",
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

slots.belongs_to_expression_experiment = Slot(uri=DEFAULT_.belongs_to_expression_experiment, name="belongs_to_expression_experiment", curie=DEFAULT_.curie('belongs_to_expression_experiment'),
                   model_uri=DEFAULT_.belongs_to_expression_experiment, domain=ExpressionAnnotation, range=Union[str, ExpressionExperimentCurie])

slots.age = Slot(uri=DEFAULT_.age, name="age", curie=DEFAULT_.curie('age'),
                   model_uri=DEFAULT_.age, domain=TemporalContext, range=Optional[str])

slots.anatomical_structure = Slot(uri=DEFAULT_.anatomical_structure, name="anatomical_structure", curie=DEFAULT_.curie('anatomical_structure'),
                   model_uri=DEFAULT_.anatomical_structure, domain=AnatomicalTerm, range=Optional[Union[str, AnatomicalTermCurie]])

slots.anatomical_substructure = Slot(uri=DEFAULT_.anatomical_substructure, name="anatomical_substructure", curie=DEFAULT_.curie('anatomical_substructure'),
                   model_uri=DEFAULT_.anatomical_substructure, domain=AnatomicalTerm, range=Optional[Union[str, AnatomicalTermCurie]])

slots.assay_used = Slot(uri=DEFAULT_.assay_used, name="assay_used", curie=DEFAULT_.curie('assay_used'),
                   model_uri=DEFAULT_.assay_used, domain=ExpressionExperiment, range=Optional[Union[str, MMOTermCurie]])

slots.cellular_component = Slot(uri=DEFAULT_.cellular_component, name="cellular_component", curie=DEFAULT_.curie('cellular_component'),
                   model_uri=DEFAULT_.cellular_component, domain=AnatomicalSite, range=Optional[Union[str, GOTermCurie]])

slots.developmental_stage_start = Slot(uri=DEFAULT_.developmental_stage_start, name="developmental_stage_start", curie=DEFAULT_.curie('developmental_stage_start'),
                   model_uri=DEFAULT_.developmental_stage_start, domain=TemporalContext, range=Optional[Union[str, StageTermCurie]])

slots.developmental_stage_stop = Slot(uri=DEFAULT_.developmental_stage_stop, name="developmental_stage_stop", curie=DEFAULT_.curie('developmental_stage_stop'),
                   model_uri=DEFAULT_.developmental_stage_stop, domain=TemporalContext, range=Optional[Union[str, StageTermCurie]])

slots.expression_qualifiers = Slot(uri=DEFAULT_.expression_qualifiers, name="expression_qualifiers", curie=DEFAULT_.curie('expression_qualifiers'),
                   model_uri=DEFAULT_.expression_qualifiers, domain=ExpressionAnnotation, range=Optional[Union[str, "ExpressionQualifierSet"]])

slots.biological_entity_assayed = Slot(uri=DEFAULT_.biological_entity_assayed, name="biological_entity_assayed", curie=DEFAULT_.curie('biological_entity_assayed'),
                   model_uri=DEFAULT_.biological_entity_assayed, domain=ExpressionExperiment, range=Union[str, BiologicalEntityCurie])

slots.image = Slot(uri=DEFAULT_.image, name="image", curie=DEFAULT_.curie('image'),
                   model_uri=DEFAULT_.image, domain=None, range=Optional[Union[str, ImageCurie]])

slots.spatial_qualifiers = Slot(uri=DEFAULT_.spatial_qualifiers, name="spatial_qualifiers", curie=DEFAULT_.curie('spatial_qualifiers'),
                   model_uri=DEFAULT_.spatial_qualifiers, domain=AnatomicalSite, range=Optional[Union[str, "SpatialQualifierSet"]])

slots.reagents_used = Slot(uri=DEFAULT_.reagents_used, name="reagents_used", curie=DEFAULT_.curie('reagents_used'),
                   model_uri=DEFAULT_.reagents_used, domain=ExpressionExperiment, range=Optional[Union[Union[dict, "Reagent"], List[Union[dict, "Reagent"]]]])

slots.specimen_alleles = Slot(uri=DEFAULT_.specimen_alleles, name="specimen_alleles", curie=DEFAULT_.curie('specimen_alleles'),
                   model_uri=DEFAULT_.specimen_alleles, domain=ExpressionExperiment, range=Optional[Union[Union[str, AlleleCurie], List[Union[str, AlleleCurie]]]])

slots.specimen_genomic_model = Slot(uri=DEFAULT_.specimen_genomic_model, name="specimen_genomic_model", curie=DEFAULT_.curie('specimen_genomic_model'),
                   model_uri=DEFAULT_.specimen_genomic_model, domain=ExpressionExperiment, range=Optional[Union[str, AffectedGenomicModelCurie]])

slots.stage_uncertainty = Slot(uri=DEFAULT_.stage_uncertainty, name="stage_uncertainty", curie=DEFAULT_.curie('stage_uncertainty'),
                   model_uri=DEFAULT_.stage_uncertainty, domain=TemporalContext, range=Optional[str])

slots.temporal_qualifiers = Slot(uri=DEFAULT_.temporal_qualifiers, name="temporal_qualifiers", curie=DEFAULT_.curie('temporal_qualifiers'),
                   model_uri=DEFAULT_.temporal_qualifiers, domain=TemporalContext, range=Optional[Union[str, "TemporalQualifierSet"]])

slots.when_expressed = Slot(uri=DEFAULT_.when_expressed, name="when_expressed", curie=DEFAULT_.curie('when_expressed'),
                   model_uri=DEFAULT_.when_expressed, domain=ExpressionAnnotation, range=Optional[Union[dict, "TemporalContext"]])

slots.where_expressed = Slot(uri=DEFAULT_.where_expressed, name="where_expressed", curie=DEFAULT_.curie('where_expressed'),
                   model_uri=DEFAULT_.where_expressed, domain=ExpressionAnnotation, range=Optional[Union[dict, "AnatomicalSite"]])

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

slots.antibody_target_genes = Slot(uri="str(uriorcurie)", name="antibody_target_genes", curie=None,
                   model_uri=DEFAULT_.antibody_target_genes, domain=Antibody, range=Optional[Union[Union[str, GeneCurie], List[Union[str, GeneCurie]]]])

slots.antigen_taxon = Slot(uri="str(uriorcurie)", name="antigen_taxon", curie=None,
                   model_uri=DEFAULT_.antigen_taxon, domain=Antibody, range=Optional[Union[str, NCBITaxonTermCurie]])

slots.clonality = Slot(uri="str(uriorcurie)", name="clonality", curie=None,
                   model_uri=DEFAULT_.clonality, domain=Antibody, range=Union[str, "AntibodyClonalitySet"])

slots.heavy_chain_isotype = Slot(uri="str(uriorcurie)", name="heavy_chain_isotype", curie=None,
                   model_uri=DEFAULT_.heavy_chain_isotype, domain=Antibody, range=Optional[Union[str, "HeavyChainIsotypeSet"]])

slots.light_chain_isotype = Slot(uri="str(uriorcurie)", name="light_chain_isotype", curie=None,
                   model_uri=DEFAULT_.light_chain_isotype, domain=Antibody, range=Optional[Union[str, "LightChainIsotypeSet"]])

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
                   model_uri=DEFAULT_.note_type, domain=None, range=Optional[Union[dict, VocabularyTerm]])

slots.private = Slot(uri=ALLIANCE.private, name="private", curie=ALLIANCE.curie('private'),
                   model_uri=DEFAULT_.private, domain=None, range=Optional[Union[bool, Bool]])

slots.related_notes = Slot(uri=ALLIANCE.related_notes, name="related_notes", curie=ALLIANCE.curie('related_notes'),
                   model_uri=DEFAULT_.related_notes, domain=None, range=Optional[Union[Union[dict, Note], List[Union[dict, Note]]]])

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
                   model_uri=DEFAULT_.created_by, domain=None, range=Union[dict, "Person"])

slots.modified_by = Slot(uri=ALLIANCE.modified_by, name="modified_by", curie=ALLIANCE.curie('modified_by'),
                   model_uri=DEFAULT_.modified_by, domain=None, range=Union[dict, "Person"])

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

slots.mod_id = Slot(uri=ALLIANCE.mod_id, name="mod_id", curie=ALLIANCE.curie('mod_id'),
                   model_uri=DEFAULT_.mod_id, domain=None, range=Optional[str])

slots.first_name = Slot(uri=ALLIANCE.first_name, name="first_name", curie=ALLIANCE.curie('first_name'),
                   model_uri=DEFAULT_.first_name, domain=None, range=Optional[str])

slots.middle_name = Slot(uri=ALLIANCE.middle_name, name="middle_name", curie=ALLIANCE.curie('middle_name'),
                   model_uri=DEFAULT_.middle_name, domain=None, range=Optional[str])

slots.last_name = Slot(uri=ALLIANCE.last_name, name="last_name", curie=ALLIANCE.curie('last_name'),
                   model_uri=DEFAULT_.last_name, domain=None, range=Optional[str])

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

slots.condition_anatomy = Slot(uri=ALLIANCE.condition_anatomy, name="condition_anatomy", curie=ALLIANCE.curie('condition_anatomy'),
                   model_uri=DEFAULT_.condition_anatomy, domain=ExperimentalCondition, range=Optional[Union[str, AnatomicalTermCurie]])

slots.condition_chemical = Slot(uri=ALLIANCE.condition_chemical, name="condition_chemical", curie=ALLIANCE.curie('condition_chemical'),
                   model_uri=DEFAULT_.condition_chemical, domain=ExperimentalCondition, range=Optional[Union[str, OntologyTermCurie]])

slots.condition_class = Slot(uri=ALLIANCE.condition_class, name="condition_class", curie=ALLIANCE.curie('condition_class'),
                   model_uri=DEFAULT_.condition_class, domain=ExperimentalCondition, range=Union[str, ZECOTermCurie])

slots.condition_gene_ontology = Slot(uri=ALLIANCE.condition_gene_ontology, name="condition_gene_ontology", curie=ALLIANCE.curie('condition_gene_ontology'),
                   model_uri=DEFAULT_.condition_gene_ontology, domain=ExperimentalCondition, range=Optional[Union[str, GOTermCurie]])

slots.condition_id = Slot(uri=ALLIANCE.condition_id, name="condition_id", curie=ALLIANCE.curie('condition_id'),
                   model_uri=DEFAULT_.condition_id, domain=ExperimentalCondition, range=Optional[Union[str, ExperimentalConditionOntologyTermCurie]])

slots.condition_quantity = Slot(uri=ALLIANCE.condition_quantity, name="condition_quantity", curie=ALLIANCE.curie('condition_quantity'),
                   model_uri=DEFAULT_.condition_quantity, domain=ExperimentalCondition, range=Optional[str])

slots.condition_statement = Slot(uri=ALLIANCE.condition_statement, name="condition_statement", curie=ALLIANCE.curie('condition_statement'),
                   model_uri=DEFAULT_.condition_statement, domain=ExperimentalCondition, range=str)

slots.condition_taxon = Slot(uri=ALLIANCE.condition_taxon, name="condition_taxon", curie=ALLIANCE.curie('condition_taxon'),
                   model_uri=DEFAULT_.condition_taxon, domain=ExperimentalCondition, range=Optional[Union[str, NCBITaxonTermCurie]])

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
                   model_uri=DEFAULT_.orcid, domain=Person, range=Optional[Union[str, URIorCURIE]])

slots.emails = Slot(uri=ALLIANCE.emails, name="emails", curie=ALLIANCE.curie('emails'),
                   model_uri=DEFAULT_.emails, domain=None, range=Optional[Union[str, List[str]]])

slots.old_emails = Slot(uri=ALLIANCE.old_emails, name="old_emails", curie=ALLIANCE.curie('old_emails'),
                   model_uri=DEFAULT_.old_emails, domain=None, range=Optional[Union[str, List[str]]])

slots.okta_id = Slot(uri=ALLIANCE.okta_id, name="okta_id", curie=ALLIANCE.curie('okta_id'),
                   model_uri=DEFAULT_.okta_id, domain=LoggedInPerson, range=Optional[str])

slots.okta_email = Slot(uri=ALLIANCE.okta_email, name="okta_email", curie=ALLIANCE.curie('okta_email'),
                   model_uri=DEFAULT_.okta_email, domain=LoggedInPerson, range=Optional[str])

slots.text_synonyms = Slot(uri="str(uriorcurie)", name="text_synonyms", curie=None,
                   model_uri=DEFAULT_.text_synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.member_terms = Slot(uri="str(uriorcurie)", name="member_terms", curie=None,
                   model_uri=DEFAULT_.member_terms, domain=None, range=Optional[Union[Union[dict, VocabularyTerm], List[Union[dict, VocabularyTerm]]]])

slots.vocabulary_description = Slot(uri="str(uriorcurie)", name="vocabulary_description", curie=None,
                   model_uri=DEFAULT_.vocabulary_description, domain=None, range=Optional[str])

slots.embryonic_cell_lines = Slot(uri=DEFAULT_.embryonic_cell_lines, name="embryonic_cell_lines", curie=DEFAULT_.curie('embryonic_cell_lines'),
                   model_uri=DEFAULT_.embryonic_cell_lines, domain=None, range=Optional[str])

slots.id = Slot(uri=DEFAULT_.id, name="id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.id, domain=None, range=Optional[str])

slots.ExpressionExperiment_references = Slot(uri=ALLIANCE.references, name="ExpressionExperiment_references", curie=ALLIANCE.curie('references'),
                   model_uri=DEFAULT_.ExpressionExperiment_references, domain=ExpressionExperiment, range=Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]])

slots.ExpressionAnnotation_associated_with_figure = Slot(uri="str(uriorcurie)", name="ExpressionAnnotation_associated_with_figure", curie=None,
                   model_uri=DEFAULT_.ExpressionAnnotation_associated_with_figure, domain=ExpressionAnnotation, range=Optional[Union[Union[str, FigureCurie], List[Union[str, FigureCurie]]]])

slots.ExpressionAnnotation_has_reference = Slot(uri="str(uriorcurie)", name="ExpressionAnnotation_has_reference", curie=None,
                   model_uri=DEFAULT_.ExpressionAnnotation_has_reference, domain=ExpressionAnnotation, range=Optional[Union[str, ReferenceCurie]])

slots.ExpressionAnnotationImagePane_subject = Slot(uri=ALLIANCE.subject, name="ExpressionAnnotationImagePane_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=DEFAULT_.ExpressionAnnotationImagePane_subject, domain=ExpressionAnnotationImagePane, range=Union[dict, ExpressionAnnotation])

slots.ExpressionAnnotationImagePane_object = Slot(uri=ALLIANCE.object, name="ExpressionAnnotationImagePane_object", curie=ALLIANCE.curie('object'),
                   model_uri=DEFAULT_.ExpressionAnnotationImagePane_object, domain=ExpressionAnnotationImagePane, range=Union[dict, "ImagePane"])

slots.GeneExpressionStatement_statement_subject = Slot(uri=ALLIANCE.statement_subject, name="GeneExpressionStatement_statement_subject", curie=ALLIANCE.curie('statement_subject'),
                   model_uri=DEFAULT_.GeneExpressionStatement_statement_subject, domain=GeneExpressionStatement, range=Optional[Union[str, GeneCurie]])

slots.GeneExpressionStatement_statement_type = Slot(uri=ALLIANCE.statement_type, name="GeneExpressionStatement_statement_type", curie=ALLIANCE.curie('statement_type'),
                   model_uri=DEFAULT_.GeneExpressionStatement_statement_type, domain=GeneExpressionStatement, range=Optional[Union[str, "ExpressionStatementTypeEnum"]])

slots.ExpressionExperimentStatement_statement_subject = Slot(uri=ALLIANCE.statement_subject, name="ExpressionExperimentStatement_statement_subject", curie=ALLIANCE.curie('statement_subject'),
                   model_uri=DEFAULT_.ExpressionExperimentStatement_statement_subject, domain=ExpressionExperimentStatement, range=Optional[Union[str, ExpressionExperimentCurie]])

slots.ExpressionAnnotationStatement_statement_subject = Slot(uri=ALLIANCE.statement_subject, name="ExpressionAnnotationStatement_statement_subject", curie=ALLIANCE.curie('statement_subject'),
                   model_uri=DEFAULT_.ExpressionAnnotationStatement_statement_subject, domain=ExpressionAnnotationStatement, range=Optional[Union[dict, ExpressionAnnotation]])

slots.ExpressionAnnotationStatement_statement_type = Slot(uri=ALLIANCE.statement_type, name="ExpressionAnnotationStatement_statement_type", curie=ALLIANCE.curie('statement_type'),
                   model_uri=DEFAULT_.ExpressionAnnotationStatement_statement_type, domain=ExpressionAnnotationStatement, range=Optional[Union[str, "ExpressionStatementTypeEnum"]])

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

slots.Antibody_curie = Slot(uri=ALLIANCE.curie, name="Antibody_curie", curie=ALLIANCE.curie('curie'),
                   model_uri=DEFAULT_.Antibody_curie, domain=Antibody, range=Union[str, AntibodyCurie])

slots.Antibody_name = Slot(uri=ALLIANCE.name, name="Antibody_name", curie=ALLIANCE.curie('name'),
                   model_uri=DEFAULT_.Antibody_name, domain=Antibody, range=str)

slots.Antibody_taxon = Slot(uri=ALLIANCE.taxon, name="Antibody_taxon", curie=ALLIANCE.curie('taxon'),
                   model_uri=DEFAULT_.Antibody_taxon, domain=Antibody, range=Optional[Union[str, NCBITaxonTermCurie]])

slots.Antibody_original_reference = Slot(uri=ALLIANCE.original_reference, name="Antibody_original_reference", curie=ALLIANCE.curie('original_reference'),
                   model_uri=DEFAULT_.Antibody_original_reference, domain=Antibody, range=Optional[Union[str, ReferenceCurie]])

slots.AntibodyNote_note_type = Slot(uri=ALLIANCE.note_type, name="AntibodyNote_note_type", curie=ALLIANCE.curie('note_type'),
                   model_uri=DEFAULT_.AntibodyNote_note_type, domain=AntibodyNote, range=Optional[Union[str, "AntibodyNoteTypeSet"]])

slots.BiologicalEntity_taxon = Slot(uri=ALLIANCE.taxon, name="BiologicalEntity_taxon", curie=ALLIANCE.curie('taxon'),
                   model_uri=DEFAULT_.BiologicalEntity_taxon, domain=BiologicalEntity, range=Union[str, NCBITaxonTermCurie])

slots.Gene_symbol = Slot(uri=ALLIANCE.symbol, name="Gene_symbol", curie=ALLIANCE.curie('symbol'),
                   model_uri=DEFAULT_.Gene_symbol, domain=Gene, range=str)

slots.Note_free_text = Slot(uri=ALLIANCE.free_text, name="Note_free_text", curie=ALLIANCE.curie('free_text'),
                   model_uri=DEFAULT_.Note_free_text, domain=Note, range=str)

slots.Note_note_type = Slot(uri=ALLIANCE.note_type, name="Note_note_type", curie=ALLIANCE.curie('note_type'),
                   model_uri=DEFAULT_.Note_note_type, domain=Note, range=Union[dict, "VocabularyTerm"])

slots.Note_private = Slot(uri=ALLIANCE.private, name="Note_private", curie=ALLIANCE.curie('private'),
                   model_uri=DEFAULT_.Note_private, domain=Note, range=Union[bool, Bool])

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

slots.PhenotypeAnnotation_subject = Slot(uri=ALLIANCE.subject, name="PhenotypeAnnotation_subject", curie=ALLIANCE.curie('subject'),
                   model_uri=DEFAULT_.PhenotypeAnnotation_subject, domain=PhenotypeAnnotation, range=Union[str, BiologicalEntityCurie])

slots.PhenotypeAnnotation_phenotype_term = Slot(uri=ALLIANCE.phenotype_term, name="PhenotypeAnnotation_phenotype_term", curie=ALLIANCE.curie('phenotype_term'),
                   model_uri=DEFAULT_.PhenotypeAnnotation_phenotype_term, domain=PhenotypeAnnotation, range=Optional[Union[str, PhenotypeTermCurie]])

slots.PhenotypeAnnotation_object = Slot(uri=ALLIANCE.object, name="PhenotypeAnnotation_object", curie=ALLIANCE.curie('object'),
                   model_uri=DEFAULT_.PhenotypeAnnotation_object, domain=PhenotypeAnnotation, range=str)

slots.PhenotypeAnnotation_single_reference = Slot(uri=ALLIANCE.single_reference, name="PhenotypeAnnotation_single_reference", curie=ALLIANCE.curie('single_reference'),
                   model_uri=DEFAULT_.PhenotypeAnnotation_single_reference, domain=PhenotypeAnnotation, range=Optional[Union[str, ReferenceCurie]])

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

slots.DiseaseAnnotation_single_reference = Slot(uri=ALLIANCE.single_reference, name="DiseaseAnnotation_single_reference", curie=ALLIANCE.curie('single_reference'),
                   model_uri=DEFAULT_.DiseaseAnnotation_single_reference, domain=DiseaseAnnotation, range=Union[str, ReferenceCurie])

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
                   model_uri=DEFAULT_.ExperimentalCondition_condition_taxon, domain=ExperimentalCondition, range=Optional[Union[str, NCBITaxonTermCurie]])

slots.ExperimentalCondition_condition_chemical = Slot(uri=ALLIANCE.condition_chemical, name="ExperimentalCondition_condition_chemical", curie=ALLIANCE.curie('condition_chemical'),
                   model_uri=DEFAULT_.ExperimentalCondition_condition_chemical, domain=ExperimentalCondition, range=Optional[Union[str, OntologyTermCurie]])

slots.ConditionRelation_unique_id = Slot(uri=ALLIANCE.unique_id, name="ConditionRelation_unique_id", curie=ALLIANCE.curie('unique_id'),
                   model_uri=DEFAULT_.ConditionRelation_unique_id, domain=ConditionRelation, range=Optional[str])

slots.ConditionRelation_condition_relation_type = Slot(uri=ALLIANCE.condition_relation_type, name="ConditionRelation_condition_relation_type", curie=ALLIANCE.curie('condition_relation_type'),
                   model_uri=DEFAULT_.ConditionRelation_condition_relation_type, domain=ConditionRelation, range=Union[str, "ConditionRelationEnum"])

slots.PaperHandle_single_reference = Slot(uri=ALLIANCE.single_reference, name="PaperHandle_single_reference", curie=ALLIANCE.curie('single_reference'),
                   model_uri=DEFAULT_.PaperHandle_single_reference, domain=PaperHandle, range=Union[str, ReferenceCurie])

slots.PaperHandle_handle = Slot(uri=ALLIANCE.handle, name="PaperHandle_handle", curie=ALLIANCE.curie('handle'),
                   model_uri=DEFAULT_.PaperHandle_handle, domain=PaperHandle, range=str)

slots.Reference_id = Slot(uri=DEFAULT_.id, name="Reference_id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.Reference_id, domain=Reference, range=Optional[str])

slots.Resource_id = Slot(uri=DEFAULT_.id, name="Resource_id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.Resource_id, domain=Resource, range=Optional[str])

slots.Resource_title = Slot(uri=ALLIANCE.title, name="Resource_title", curie=ALLIANCE.curie('title'),
                   model_uri=DEFAULT_.Resource_title, domain=Resource, range=Optional[str])

slots.LoggedInPerson_okta_id = Slot(uri=ALLIANCE.okta_id, name="LoggedInPerson_okta_id", curie=ALLIANCE.curie('okta_id'),
                   model_uri=DEFAULT_.LoggedInPerson_okta_id, domain=LoggedInPerson, range=str)

slots.LoggedInPerson_okta_email = Slot(uri=ALLIANCE.okta_email, name="LoggedInPerson_okta_email", curie=ALLIANCE.curie('okta_email'),
                   model_uri=DEFAULT_.LoggedInPerson_okta_email, domain=LoggedInPerson, range=str)

slots.VocabularyTerm_name = Slot(uri=ALLIANCE.name, name="VocabularyTerm_name", curie=ALLIANCE.curie('name'),
                   model_uri=DEFAULT_.VocabularyTerm_name, domain=VocabularyTerm, range=str)

slots.Vocabulary_name = Slot(uri=ALLIANCE.name, name="Vocabulary_name", curie=ALLIANCE.curie('name'),
                   model_uri=DEFAULT_.Vocabulary_name, domain=Vocabulary, range=Union[str, VocabularyName])
