# Auto generated from phenotypeAndDiseaseAnnotation.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-12-13 16:39
# Schema: Alliance-Schema-Prototype-Phenotype-and-Disease-Annotation
#
# id: https://github.com/alliance-genome/agr_persistent_schema/phenotypeAndDiseaseAnnotation.yaml
# description: Alliance Phenotype and Disease Annotation Schema Prototype with LinkML
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
from . affectedGenomicModel import AffectedGenomicModelCurie
from . allele import AlleleCurie
from . core import Association, BiologicalEntityCurie, CrossReference, CrossReferenceCurie, Entity, GeneCurie, Synonym
from . ontologyTerm import AnatomicalTermCurie, DOTermCurie, ECOTermCurie, ExperimentalConditionOntologyTermCurie, GOTermCurie, OntologyTermCurie, PhenotypeTermCurie, ZECOTermCurie
from . person import PersonPersonId
from . reference import ReferenceCurie
from linkml_runtime.linkml_model.types import Boolean, Date, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ALLIANCE = CurieNamespace('alliance', 'http://alliancegenome.org')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ALLIANCE


# Types

# Class references
class ExperimentalConditionCurie(URIorCURIE):
    pass


class ConditionRelationCurie(URIorCURIE):
    pass


class MoleculeCurie(URIorCURIE):
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

    curie: Union[str, ExperimentalConditionCurie] = None
    condition_class: Union[str, ZECOTermCurie] = None
    condition_statement: str = None
    condition_id: Optional[Union[str, ExperimentalConditionOntologyTermCurie]] = None
    condition_quantity: Optional[str] = None
    condition_anatomy: Optional[Union[str, AnatomicalTermCurie]] = None
    condition_gene_ontology: Optional[Union[str, GOTermCurie]] = None
    condition_taxon: Optional[Union[str, OntologyTermCurie]] = None
    condition_chemical: Optional[Union[str, OntologyTermCurie]] = None
    paper_handles: Optional[Union[Union[dict, "PaperHandle"], List[Union[dict, "PaperHandle"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ExperimentalConditionCurie):
            self.curie = ExperimentalConditionCurie(self.curie)

        if self._is_empty(self.condition_class):
            self.MissingRequiredField("condition_class")
        if not isinstance(self.condition_class, ZECOTermCurie):
            self.condition_class = ZECOTermCurie(self.condition_class)

        if self._is_empty(self.condition_statement):
            self.MissingRequiredField("condition_statement")
        if not isinstance(self.condition_statement, str):
            self.condition_statement = str(self.condition_statement)

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

    curie: Union[str, ConditionRelationCurie] = None
    condition_relation_type: Union[str, "ConditionRelationEnum"] = None
    conditions: Optional[Union[Dict[Union[str, ExperimentalConditionCurie], Union[dict, ExperimentalCondition]], List[Union[dict, ExperimentalCondition]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, ConditionRelationCurie):
            self.curie = ConditionRelationCurie(self.curie)

        if self._is_empty(self.condition_relation_type):
            self.MissingRequiredField("condition_relation_type")
        if not isinstance(self.condition_relation_type, ConditionRelationEnum):
            self.condition_relation_type = ConditionRelationEnum(self.condition_relation_type)

        self._normalize_inlined_as_list(slot_name="conditions", slot_type=ExperimentalCondition, key_name="curie", keyed=True)

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
    condition_relations: Optional[Union[Dict[Union[str, ConditionRelationCurie], Union[dict, "ConditionRelation"]], List[Union[dict, "ConditionRelation"]]]] = empty_dict()
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

        self._normalize_inlined_as_list(slot_name="condition_relations", slot_type=ConditionRelation, key_name="curie", keyed=True)

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

    curie: Union[str, DiseaseAnnotationCurie] = None
    evidence_codes: Union[Union[str, ECOTermCurie], List[Union[str, ECOTermCurie]]] = None
    reference: Union[str, ReferenceCurie] = None
    data_provider: Union[str, List[str]] = None
    subject: Union[str, BiologicalEntityCurie] = None
    predicate: str = None
    object: Union[str, DOTermCurie] = None
    created_by: Union[str, PersonPersonId] = None
    modified_by: Union[str, PersonPersonId] = None
    mod_id: Optional[str] = None
    negated: Optional[Union[bool, Bool]] = None
    annotation_type: Optional[Union[str, "AnnotationTypeEnum"]] = None
    with: Optional[Union[str, GeneCurie]] = None
    disease_qualifiers: Optional[Union[str, "DiseaseAnnotationQualifierEnum"]] = None
    condition_relations: Optional[Union[Dict[Union[str, ConditionRelationCurie], Union[dict, "ConditionRelation"]], List[Union[dict, "ConditionRelation"]]]] = empty_dict()
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
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, DiseaseAnnotationCurie):
            self.curie = DiseaseAnnotationCurie(self.curie)

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

        self._normalize_inlined_as_list(slot_name="condition_relations", slot_type=ConditionRelation, key_name="curie", keyed=True)

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

    curie: Union[str, GeneDiseaseAnnotationCurie] = None
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

    curie: Union[str, AlleleDiseaseAnnotationCurie] = None
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

    curie: Union[str, AGMDiseaseAnnotationCurie] = None
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
        if not isinstance(self.predicate, AgmDiseaseRelationEnum):
            self.predicate = AgmDiseaseRelationEnum(self.predicate)

        if self.inferred_allele is not None and not isinstance(self.inferred_allele, AlleleCurie):
            self.inferred_allele = AlleleCurie(self.inferred_allele)

        if self.inferred_gene is not None and not isinstance(self.inferred_gene, GeneCurie):
            self.inferred_gene = GeneCurie(self.inferred_gene)

        super().__post_init__(**kwargs)


# Enumerations
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

