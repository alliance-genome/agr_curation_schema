# Auto generated from antibody.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-11-16 23:00
# Schema: antibody.yaml
#
# id: https://github.com/alliance-genome/agr_curation_schema/src/schema/antibody.yaml
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
from . core import BiologicalEntity, BiologicalEntityCurie, CrossReferenceCurie, Curie, EntityStatement, GeneCurie
from . person import Agent, PersonPersonId
from . reference import ReferenceCurie
from linkml_runtime.linkml_model.types import Date, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
FB = CurieNamespace('FB', 'http://identifiers.org/fb/')
MGI = CurieNamespace('MGI', 'http://identifiers.org/mgi/')
NLMID = CurieNamespace('NLMID', 'https://www.ncbi.nlm.nih.gov/nlmcatalog/?term=')
RGD = CurieNamespace('RGD', 'http://identifiers.org/rgd/')
SGD = CurieNamespace('SGD', 'http://identifiers.org/sgd/')
WB = CurieNamespace('WB', 'http://identifiers.org/wb/')
ZFIN = CurieNamespace('ZFIN', 'http://identifiers.org/zfin/')
ALLIANCE = CurieNamespace('alliance', 'http://alliancegenome.org')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
FALDO = CurieNamespace('faldo', 'http://biohackathon.org/resource/faldo#')
GFF = CurieNamespace('gff', 'https://w3id.org/gff')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_curation_schema/src/schema/antibody.yaml/')


# Types

# Class references
class AntibodyCurie(BiologicalEntityCurie):
    pass


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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/antibody.yaml/Antibody")

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
    cross_references: Optional[Union[Union[str, CrossReferenceCurie], List[Union[str, CrossReferenceCurie]]]] = empty_list()
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

        if not isinstance(self.cross_references, list):
            self.cross_references = [self.cross_references] if self.cross_references is not None else []
        self.cross_references = [v if isinstance(v, CrossReferenceCurie) else CrossReferenceCurie(v) for v in self.cross_references]

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_curation_schema/src/schema/antibody.yaml/AntibodyNote")

    note_type: Optional[Union[str, "AntibodyNoteTypeSet"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.note_type is not None and not isinstance(self.note_type, AntibodyNoteTypeSet):
            self.note_type = AntibodyNoteTypeSet(self.note_type)

        super().__post_init__(**kwargs)


# Enumerations
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

# Slots

