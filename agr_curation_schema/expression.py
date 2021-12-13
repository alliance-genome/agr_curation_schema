# Auto generated from expression.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-11-16 23:00
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
from . core import Association, BiologicalEntityCurie, GeneCurie, Reagent
from . image import FigureCurie, ImageCurie, ImagePane
from . ontologyTerm import AnatomicalTerm, AnatomicalTermCurie, GOTermCurie, MMOTermCurie, StageTermCurie
from . person import PersonPersonId
from . phenotypeAndDiseaseAnnotation import ExperimentalConditionCurie
from . reference import ReferenceCurie
from linkml_runtime.linkml_model.types import Boolean, Date, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/')


# Types

# Class references
class ExpressionAnnotationCurie(URIorCURIE):
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
    reagents: Optional[Union[Union[dict, Reagent], List[Union[dict, Reagent]]]] = empty_list()
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
class ExpressionAnnotationImagePane(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ExpressionAnnotationImagePane")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ExpressionAnnotationImagePane"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/expression.yaml/ExpressionAnnotationImagePane")

    predicate: str = None
    subject: Union[str, ExpressionAnnotationCurie] = None
    object: Union[dict, ImagePane] = None

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
    experimental_condition: Optional[Union[str, ExperimentalConditionCurie]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, ExpressionConditionRelationEnum):
            self.predicate = ExpressionConditionRelationEnum(self.predicate)

        if self.phenotype_annotation is not None and not isinstance(self.phenotype_annotation, ExpressionAnnotationCurie):
            self.phenotype_annotation = ExpressionAnnotationCurie(self.phenotype_annotation)

        if self.experimental_condition is not None and not isinstance(self.experimental_condition, ExperimentalConditionCurie):
            self.experimental_condition = ExperimentalConditionCurie(self.experimental_condition)

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

# Slots

