# Auto generated from geneInteraction.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-11-16 23:00
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
from . allele import AlleleCurie
from . core import Association, BiologicalEntity, BiologicalEntityCurie, CrossReferenceCurie, Curie, Gene, GeneCurie
from . reference import ReferenceCurie
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOGRID = CurieNamespace('BIOGRID', 'http://identifiers.org/biogrid/')
DIP = CurieNamespace('DIP', 'http://identifiers.org/dip/')
EMDB = CurieNamespace('EMDB', 'http://identifiers.org/emdb/')
FB = CurieNamespace('FB', 'http://identifiers.org/fb/')
IMEX = CurieNamespace('IMEX', 'http://identifiers.org/imex/')
INTACT = CurieNamespace('INTACT', 'http://identifiers.org/intact/')
MINT = CurieNamespace('MINT', 'http://identifiers.org/mint/')
PDBE = CurieNamespace('PDBE', 'https://www.ebi.ac.uk/pdbe/entry/pdb/')
RCSB_PDB = CurieNamespace('RCSB_PDB', 'https://www.rcsb.org/structure/')
WB = CurieNamespace('WB', 'http://identifiers.org/wb/')
WWPDB = CurieNamespace('WWPDB', 'https://www.rcsb.org/structure/')
ALLIANCE = CurieNamespace('alliance', 'http://alliancegenome.org')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ALLIANCE


# Types

# Class references
class GeneInteractionCurie(URIorCURIE):
    pass


class GeneMolecularInteractionCurie(GeneInteractionCurie):
    pass


class GeneGeneticInteractionCurie(GeneInteractionCurie):
    pass


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
    cross_references: Optional[Union[Union[str, CrossReferenceCurie], List[Union[str, CrossReferenceCurie]]]] = empty_list()
    interactor_A_role: Optional[Union[Union[str, "InteractorARoleEnum"], List[Union[str, "InteractorARoleEnum"]]]] = empty_list()
    interactor_B_role: Optional[Union[Union[str, "InteractorBRoleEnum"], List[Union[str, "InteractorBRoleEnum"]]]] = empty_list()
    references: Optional[Union[str, ReferenceCurie]] = None

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

        if not isinstance(self.cross_references, list):
            self.cross_references = [self.cross_references] if self.cross_references is not None else []
        self.cross_references = [v if isinstance(v, CrossReferenceCurie) else CrossReferenceCurie(v) for v in self.cross_references]

        if not isinstance(self.interactor_A_role, list):
            self.interactor_A_role = [self.interactor_A_role] if self.interactor_A_role is not None else []
        self.interactor_A_role = [v if isinstance(v, InteractorARoleEnum) else InteractorARoleEnum(v) for v in self.interactor_A_role]

        if not isinstance(self.interactor_B_role, list):
            self.interactor_B_role = [self.interactor_B_role] if self.interactor_B_role is not None else []
        self.interactor_B_role = [v if isinstance(v, InteractorBRoleEnum) else InteractorBRoleEnum(v) for v in self.interactor_B_role]

        if self.references is not None and not isinstance(self.references, ReferenceCurie):
            self.references = ReferenceCurie(self.references)

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

# Slots

