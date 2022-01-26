
# Alliance-Schema-Prototype schema


Alliance Schema Prototype


### Classes

 * [AffectedGenomicModelComponent](AffectedGenomicModelComponent.md) - Allele that affects the model and its zygosity
 * [Agent](Agent.md) - An individual, group, organization or project that provides information and/or materials.
     * [Organization](Organization.md)
         * [Company](Company.md)
         * [Laboratory](Laboratory.md)
     * [Person](Person.md)
 * [Assembly](Assembly.md)
 * [Association](Association.md) - A typed association between two entities, supported by evidence.
     * [DiseaseAnnotation](DiseaseAnnotation.md) - An annotation asserting an association between a biological entity and a disease supported by evidence.
         * [AGMDiseaseAnnotation](AGMDiseaseAnnotation.md) - An annotation asserting an association between an AGM and a disease supported by evidence.
         * [AlleleDiseaseAnnotation](AlleleDiseaseAnnotation.md) - An annotation asserting an association between an allele and a disease supported by evidence.
         * [GeneDiseaseAnnotation](GeneDiseaseAnnotation.md) - An annotation asserting an association between a gene and a disease supported by evidence.
     * [EntitySynonym](EntitySynonym.md) - A relationship between an entity and a synonym.
     * [GeneToGeneAssociation](GeneToGeneAssociation.md) - abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction.
         * [GeneInteraction](GeneInteraction.md) - An interaction between two genes or gene products; this may be a physical molecular interaction between gene products (e.g. protein-protein interactions), or may be a genetic interaction between genes (e.g. phenotypic suppression)
             * [GeneGeneticInteraction](GeneGeneticInteraction.md) - A genetic interaction between genes (e.g. phenotypic suppression)
             * [GeneMolecularInteraction](GeneMolecularInteraction.md) - A physical molecular interaction between gene products (e.g. protein-protein interactions or protein-RNA interactions) or between genes and DNA-binding factors (e.g. protein-DNA interactions)
     * [PhenotypeAnnotation](PhenotypeAnnotation.md) - An annotation asserting an association between a biological entity and a phenotype supported by evidence.
         * [AGMPhenotypeAnnotation](AGMPhenotypeAnnotation.md) - An annotation asserting an association between an AGM and a phenotype supported by evidence.
         * [AllelePhenotypeAnnotation](AllelePhenotypeAnnotation.md) - An annotation asserting an association between an allele and a phenotype supported by evidence.
         * [GenePhenotypeAnnotation](GenePhenotypeAnnotation.md) - An annotation asserting an association between a gene and a phenotype supported by evidence.
 * [AuthorReference](AuthorReference.md)
 * [BiologicalEntity](BiologicalEntity.md) - A high-level entity comprising .
     * [Antibody](Antibody.md) - Immunoglobulin proteins that bind specific molecule(s). Can be used experimentally for the purposes of detection or purification.
     * [GenomicEntity](GenomicEntity.md)
         * [AffectedGenomicModel](AffectedGenomicModel.md) - Includes inbred strains, stocks, disease models and mutant genotypes
         * [Allele](Allele.md) - One of multiple possible forms of a functional genomic element (most often described as a locus or gene), differing from the reference DNA sequence.  The genomic element can be endogenous or constructed.
         * [Construct](Construct.md)
         * [ConstructComponent](ConstructComponent.md)
         * [Gene](Gene.md) - Placeholder.
         * [Transcript](Transcript.md) - Placeholder.
         * [Variant](Variant.md) - A DNA sequence that differs relative to a designated reference sequence.  The sequence occurs at a single position or in contiguous nucleotides.
 * [CellLine](CellLine.md) - Dummy cell line class
 * [Chromosome](Chromosome.md) - The ID of the landmark used to establish the coordinate system for the current feature.
 * [ConditionRelation](ConditionRelation.md) - A pairing of an experimental condition relation (i.e. has_condition) with a list of 1 or more ExperimentalCondition objects. Annotation objects can connect directly to a set of 0 or more of these ConditionRelation objects via a 'condition_relations' slot to express the experimental conditions relevant to the annotation.
 * [Entity](Entity.md)
 * [EntityStatement](EntityStatement.md) - Free-text describing some aspect of an entity.
     * [AntibodyNote](AntibodyNote.md)
 * [ExperimentalCondition](ExperimentalCondition.md) - The environmental context in which an experiment is carried out. This may (e.g. drug treatment) or may not (e.g. standard conditions) directly influence the outcome of the experiment.
 * [ExternalDatabaseLink](ExternalDatabaseLink.md) - Base relation that holds the identifier prefix, base url and url suffix to help in generating URLs in crossReferences.
 * [Figure](Figure.md) - An entity representing a figure or table in a publication.
 * [File](File.md) - A dummy object.
 * [GeneGenomicLocation](GeneGenomicLocation.md)
 * [Image](Image.md) - The set of files and metadata that constitute an image.
 * [ImagePane](ImagePane.md) - Part of an Image that is relevant to some annotation. An annotation may reference many panes of an Image.
 * [InformationContentEntity](InformationContentEntity.md) - a piece of information that typically describes some topic of discourse or is used as support. Precedence of identifiers for references is as follows: PMID if available; DOI if not; actual alternate CURIE otherwise.
     * [CrossReference](CrossReference.md)
     * [Reference](Reference.md)
     * [Resource](Resource.md)
 * [MolecularMutation](MolecularMutation.md) - Description of the DNA changes with unknown precise genomic location
 * [Molecule](Molecule.md) - Molecules as described by WormBase
 * [NoteType](NoteType.md) - Describes the relation between a note and an object
 * [OntologyTerm](OntologyTerm.md) - A concept or class in an ontology, vocabulary or thesaurus. Note, ontology terms can be found in multiple ontologies (ie: mireoting). defining_slots helps define an alternative key for ontology terms.
     * [AnatomicalTerm](AnatomicalTerm.md)
         * [CLTerm](CLTerm.md)
         * [EMAPATerm](EMAPATerm.md)
         * [FBBTTerm](FBBTTerm.md)
         * [MATerm](MATerm.md)
         * [UBERONTerm](UBERONTerm.md)
         * [WBBTTerm](WBBTTerm.md)
         * [ZFATerm](ZFATerm.md)
     * [CHEBITerm](CHEBITerm.md)
     * [DOTerm](DOTerm.md)
     * [ECOTerm](ECOTerm.md)
     * [ExperimentalConditionOntologyTerm](ExperimentalConditionOntologyTerm.md)
         * [XCOTerm](XCOTerm.md)
         * [ZECOTerm](ZECOTerm.md)
     * [FBCVTerm](FBCVTerm.md)
     * [GOTerm](GOTerm.md)
     * [MITerm](MITerm.md)
     * [MMOTerm](MMOTerm.md)
     * [MMUSDVTerm](MMUSDVTerm.md)
     * [PhenotypeTerm](PhenotypeTerm.md) - An ontology term representing a characteristic of an organism. This may or may not be expressed as a difference in comparison to a reference organism.
     * [SOTerm](SOTerm.md)
     * [StageTerm](StageTerm.md)
         * [FBDVTerm](FBDVTerm.md)
         * [WBLSTerm](WBLSTerm.md)
         * [ZFSTerm](ZFSTerm.md)
 * [PaperHandle](PaperHandle.md) - A pairing of a reference and a free text string that allows an object to have a reference-specific alias (or handle). For example, used for experimental conditions from ZFIN to label (in a reference-specific manner) individual experimental conditions when curating a particular reference.
 * [ReferenceType](ReferenceType.md) - Describes the relation between a reference and an object
 * [SequenceTargetingReagent](SequenceTargetingReagent.md) - Dummy sequence targeting reagent class
 * [Species](Species.md)
 * [Synonym](Synonym.md)
 * [VariantConsequence](VariantConsequence.md) - Parent class for gene- and transcript-level consequences
     * [VariantGeneConsequence](VariantGeneConsequence.md) - Class for gene-level VEP results
     * [VariantTranscriptConsequence](VariantTranscriptConsequence.md) - Class for transcript-level VEP results
 * [VariantGenomicLocation](VariantGenomicLocation.md)
 * [Vocabulary](Vocabulary.md) - A set of VocabularyTerm objects.
 * [VocabularyTerm](VocabularyTerm.md) - A concept or class in a simple vocabulary.

### Mixins

 * [AuditedObject](AuditedObject.md) - Some entity for which changes are tracked, including date/time of change and the agent responsible for the change.
 * [Reagent](Reagent.md) - A material entity used in experiments.

### Slots

 * [PubMed_type](PubMed_type.md) - Type of InformationContentEntity as described by pub med.
 * [abbreviation](abbreviation.md)
     * [ECOTerm➞abbreviation](ECOTerm_abbreviation.md) - Letter code used by curators to refer to the ECO term.
 * [aberration](aberration.md) - Associated deficiency (etc.) whose breakpoint causes the mutation
     * [Allele➞aberration](Allele_aberration.md)
 * [abstract](abstract.md)
 * [address](address.md) - the particulars of the place where someone or an organization is situated.  For now, this slot is a simple text blob containing all relevant details of the given location for fitness of purpose. For the moment, this address can include other contact details such as email and phone number(?).
 * [affected_entities](affected_entities.md) - Biological entities affected by allele
 * [aggregation_database](aggregation_database.md)
     * [GeneMolecularInteraction➞aggregation_database](GeneMolecularInteraction_aggregation_database.md) - The database that collected the interaction annotation from another resource and aggregated it into a consolidated resource. e.g. IMEx
 * [alliance_category](alliance_category.md)
 * [amino_acid_reference](amino_acid_reference.md) - reference genome amino acid sequence at variant position
     * [VariantTranscriptConsequence➞amino_acid_reference](VariantTranscriptConsequence_amino_acid_reference.md) - Amino acid sequence encoded by codon(s) in reference genome sequence altered by the variant
 * [amino_acid_variant](amino_acid_variant.md) - variant amino acid sequence at variant position
     * [VariantTranscriptConsequence➞amino_acid_variant](VariantTranscriptConsequence_amino_acid_variant.md) - Amino acid sequence encoded by codon(s) in variant sequence
 * [annotation_type](annotation_type.md) - The type of annotation classified according to curation method: manually curated, high-throughput, computational
     * [DiseaseAnnotation➞annotation_type](DiseaseAnnotation_annotation_type.md)
 * [antibody_target_genes](antibody_target_genes.md) - The genes whose gene products are recognized by the antibody.
 * [associated_notes](associated_notes.md) - Notes associated with the entity in some way
 * [associated_references](associated_references.md) - References associated with the entity in some way
 * [association_slot](association_slot.md) - any slot that relates an association to another entity
     * [interaction_type](interaction_type.md) - The type of interaction between the two genes or gene products. e.g. physical association
     * [interactor_A_genetic_perturbation](interactor_A_genetic_perturbation.md)
     * [interactor_A_role](interactor_A_role.md)
     * [interactor_A_type](interactor_A_type.md)
     * [interactor_B_genetic_perturbation](interactor_B_genetic_perturbation.md)
     * [interactor_B_role](interactor_B_role.md)
     * [interactor_B_type](interactor_B_type.md)
     * [object](object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
         * [DiseaseAnnotation➞object](DiseaseAnnotation_object.md) - The disease ontology term.
         * [EntitySynonym➞object](EntitySynonym_object.md)
         * [GeneGenomicLocation➞object](GeneGenomicLocation_object.md) - object should be the chromosome identifier
         * [GeneToGeneAssociation➞object](GeneToGeneAssociation_object.md) - the object gene in the association. If the relation is symmetric, subject vs object is arbitrary. We allow a gene product to stand as a proxy for the gene or vice versa.
             * [GeneInteraction➞object](GeneInteraction_object.md) - connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
         * [PhenotypeAnnotation➞object](PhenotypeAnnotation_object.md) - phenotype statement: The label of an individual phenotype term from a phenotype ontology or the post-composed statement of the phenotype from a post-composed terminology
         * [VariantGeneConsequence➞object](VariantGeneConsequence_object.md)
         * [VariantGenomicLocation➞object](VariantGenomicLocation_object.md) - object should be the chromosome identifier
         * [VariantTranscriptConsequence➞object](VariantTranscriptConsequence_object.md)
     * [predicate](predicate.md) - A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
         * [DiseaseAnnotation➞predicate](DiseaseAnnotation_predicate.md) - Constrains the disease subject, associationType and inferredGeneAssociation.
             * [AGMDiseaseAnnotation➞predicate](AGMDiseaseAnnotation_predicate.md) - The relationship between AGM and disease.
             * [AlleleDiseaseAnnotation➞predicate](AlleleDiseaseAnnotation_predicate.md) - The relationship between allele and disease.
             * [GeneDiseaseAnnotation➞predicate](GeneDiseaseAnnotation_predicate.md) - The relationship between gene and disease.
         * [EntitySynonym➞predicate](EntitySynonym_predicate.md)
         * [GeneInteraction➞predicate](GeneInteraction_predicate.md)
             * [GeneGeneticInteraction➞predicate](GeneGeneticInteraction_predicate.md)
             * [GeneMolecularInteraction➞predicate](GeneMolecularInteraction_predicate.md)
     * [subject](subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
         * [DiseaseAnnotation➞subject](DiseaseAnnotation_subject.md) - The biological entity to which the disease ontology term is associated.
             * [AGMDiseaseAnnotation➞subject](AGMDiseaseAnnotation_subject.md) - The AGM to which the disease ontology term is associated.
             * [AlleleDiseaseAnnotation➞subject](AlleleDiseaseAnnotation_subject.md) - The allele to which the disease ontology term is associated.
             * [GeneDiseaseAnnotation➞subject](GeneDiseaseAnnotation_subject.md) - The gene to which the disease ontology term is associated.
         * [GeneGenomicLocation➞subject](GeneGenomicLocation_subject.md) - subject should be the gene identifier
         * [GeneToGeneAssociation➞subject](GeneToGeneAssociation_subject.md) - the subject gene in the association. If the relation is symmetric, subject vs object is arbitrary. We allow a gene product to stand as a proxy for the gene or vice versa.
             * [GeneInteraction➞subject](GeneInteraction_subject.md) - connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
         * [PhenotypeAnnotation➞subject](PhenotypeAnnotation_subject.md) - The biological entity (e.g. gene, allele, genotype) to which the phenotype is associated, by direct curation.
             * [AGMPhenotypeAnnotation➞subject](AGMPhenotypeAnnotation_subject.md) - The AGM to which the phenotype ontology term is associated.
             * [AllelePhenotypeAnnotation➞subject](AllelePhenotypeAnnotation_subject.md) - The allele to which the phenotype ontology term is associated.
             * [GenePhenotypeAnnotation➞subject](GenePhenotypeAnnotation_subject.md) - The gene to which the phenotype ontology term is associated.
         * [VariantConsequence➞subject](VariantConsequence_subject.md)
         * [VariantGenomicLocation➞subject](VariantGenomicLocation_subject.md) - subject should be the variant identifier
 * [authors](authors.md)
 * [automated_gene_description](automated_gene_description.md) - Gene description generated via algorithm developed at the alliance.
 * [caption](caption.md) - Text describing the contents of a figure or table in a publication.
 * [cdna_end](cdna_end.md) - end position of variation in cDNA coordinates
 * [cdna_start](cdna_start.md) - start position of variation in cDNA coordinates
     * [VariantTranscriptConsequence➞cdna_start](VariantTranscriptConsequence_cdna_start.md) - Start position of variant in cDNA coordinates
 * [cds_end](cds_end.md) - end position of variation in CDS coordinates
     * [VariantTranscriptConsequence➞cds_end](VariantTranscriptConsequence_cds_end.md) - End position of variant in CDS coordinates
 * [cds_start](cds_start.md) - start position of variation in CDS coordinates
     * [VariantTranscriptConsequence➞cds_start](VariantTranscriptConsequence_cds_start.md) - Start position of variant in CDS coordinates
 * [citation](citation.md)
 * [clonality](clonality.md) - The clonality of the antibody: e.g., monoclonal.
 * [cnda_end](cnda_end.md) - End position of variant in cDNA coordinates
     * [VariantTranscriptConsequence➞cnda_end](VariantTranscriptConsequence_cnda_end.md)
 * [codon_reference](codon_reference.md) - reference sequence of codon(s) affected by variation - bases outside of the variant region are in lower case, those within are in upper case (e.g. cTa)
     * [VariantTranscriptConsequence➞codon_reference](VariantTranscriptConsequence_codon_reference.md) - Reference genome sequence of codon(s) altered by the variant.  Bases affected by the variant are given in upper case, bases flanking the variation are given in lower case
 * [codon_variant](codon_variant.md) - variant sequence of codon(s) affected by variation - bases outside of the variant region are in lower case, those within are in upper case (e.g. cAa)
     * [VariantTranscriptConsequence➞codon_variant](VariantTranscriptConsequence_codon_variant.md) - Sequence of codon(s) in variant sequence altered by the variant. Bases affected by the variant are given in upper case, bases flanking the variation are given in lower case
 * [component_relation](component_relation.md)
 * [components](components.md) - Collection of genomic components that make up a model, i.e. 'allele', each with a zygosity
 * [computed_gene](computed_gene.md)
 * [condition_anatomy](condition_anatomy.md)
     * [ExperimentalCondition➞condition_anatomy](ExperimentalCondition_condition_anatomy.md) - Anatomical ontology identifier used in cases like regeneration/wounding.
 * [condition_chemical](condition_chemical.md)
     * [ExperimentalCondition➞condition_chemical](ExperimentalCondition_condition_chemical.md) - ChEBI or molecular ontology id used in subset of condition terms.  ie: the specific chemcial used in conjunction with 'chemical condition'.
 * [condition_class](condition_class.md)
     * [ExperimentalCondition➞condition_class](ExperimentalCondition_condition_class.md) - The ZECO ID that represents the high level condition grouping term.  This will come from a slim in the ZECO, called 'AllianceSlim'.
 * [condition_gene_ontology](condition_gene_ontology.md)
     * [ExperimentalCondition➞condition_gene_ontology](ExperimentalCondition_condition_gene_ontology.md) - Gene Ontology id used in subset of condition types.
 * [condition_id](condition_id.md)
     * [ExperimentalCondition➞condition_id](ExperimentalCondition_condition_id.md) - The specific ontology ID for the condition when that is not covered by any of the other condition ontology ID attributes (chemical, NCBITaxon, anatomical). This could also be another ZECO term if the ZECO term that describes this condition is more specific, or outside the conditionClassId slim.
 * [condition_quantity](condition_quantity.md)
     * [ExperimentalCondition➞condition_quantity](ExperimentalCondition_condition_quantity.md) - Optional free text field that records the units/amount/degrees of a condition.
 * [condition_relation_type](condition_relation_type.md)
     * [ConditionRelation➞condition_relation_type](ConditionRelation_condition_relation_type.md)
 * [condition_relations](condition_relations.md)
 * [condition_statement](condition_statement.md)
     * [ExperimentalCondition➞condition_statement](ExperimentalCondition_condition_statement.md) - Free text describing the environmental/experimental condition. For some groups this is a single term, others is it is a concatenation of the term names from the ontologies included in this data structure.
 * [condition_taxon](condition_taxon.md)
     * [ExperimentalCondition➞condition_taxon](ExperimentalCondition_condition_taxon.md) - NCBITaxon ontology id used in subset of condition types like 'bacterial infection'.
 * [conditions](conditions.md)
 * [construct_components](construct_components.md)
 * [contains_construct](contains_construct.md)
 * [copyright_date](copyright_date.md)
 * [corresponding_author](corresponding_author.md)
 * [created_by](created_by.md) - The individual that created the entity.
 * [creation_date](creation_date.md) - The date on which an entity was created. This can be applied to nodes or edges.
     * [PhenotypeAnnotation➞creation_date](PhenotypeAnnotation_creation_date.md) - The date of curation at the source (MOD) database.
 * [cropped_from](cropped_from.md) - Another larger image from which this image was cropped.
 * [cross_references](cross_references.md) - Holds between an object and its CrossReferences.
     * [GeneInteraction➞cross_references](GeneInteraction_cross_references.md) - Additional identifier(s) of the interaction annotation other than the primary id.
 * [curator_comment](curator_comment.md) - A publicly visible explanatory note from curators about some entity.
 * [curie](curie.md) - A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
     * [Antibody➞curie](Antibody_curie.md) - A unique identifier for the antibody: e.g., WBAntibody0000001.
     * [GeneInteraction➞curie](GeneInteraction_curie.md) - The unique primary identifier for the interaction. This should be the source (curation) database identifier, or if that is not available then the aggregation database identifier (e.g. IMEx)
 * [current](current.md)
 * [data_provider](data_provider.md) - MOD that provided data
     * [DiseaseAnnotation➞data_provider](DiseaseAnnotation_data_provider.md)
 * [database_status](database_status.md) - Database status of the allele
 * [date_arrived_in_PubMed](date_arrived_in_PubMed.md) - Day in which a reference or resource was created in PUBMED. Only relevant for PUBMED references.
 * [date_last_modified](date_last_modified.md) - Date on which an entity was last modified.
 * [date_last_modified_in_PubMed](date_last_modified_in_PubMed.md) - Date on which an entity was created.
 * [date_published](date_published.md) - Date on which an entity was created.
 * [day_published](day_published.md) - Day in which an entity was created.
 * [dbkey](dbkey.md) - Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
 * [definition](definition.md) - The explanation of the meaning of a term.
     * [OntologyTerm➞definition](OntologyTerm_definition.md) - The definition of the ontology term. This is a reference to an object that holds the text description of the term and a collection of URLs that further define the term.
 * [definition_urls](definition_urls.md)
 * [description](description.md) - a human-readable description of an entity
 * [detection_method](detection_method.md)
     * [GeneMolecularInteraction➞detection_method](GeneMolecularInteraction_detection_method.md) - The experimental method used to identify the physical interaction between two molecules
 * [disease_annotation_note](disease_annotation_note.md)
 * [disease_annotation_summary](disease_annotation_summary.md)
 * [disease_genetic_modifier](disease_genetic_modifier.md) - Specifies a genetic object that modifies the disease model. May be a gene, allele, AGM.
 * [disease_genetic_modifier_relation](disease_genetic_modifier_relation.md) - A relation describing how the genetic modifier modifies the disease model.
 * [disease_qualifiers](disease_qualifiers.md)
 * [display_name](display_name.md)
 * [display_synonym](display_synonym.md) - Placeholder.
 * [editors](editors.md) - holds between a resource and a editor_resource
 * [embryonic_cell_lines](embryonic_cell_lines.md)
     * [Allele➞embryonic_cell_lines](Allele_embryonic_cell_lines.md)
 * [embryonic_stem_cell_lines](embryonic_stem_cell_lines.md) - Embryonic stem cell lines known to carry the allele
 * [end](end.md) - The end of the feature in positive 1-based integer coordinates
 * [evidence_codes](evidence_codes.md) - ECO term IDs
     * [DiseaseAnnotation➞evidence_codes](DiseaseAnnotation_evidence_codes.md)
 * [first_name](first_name.md)
 * [formula](formula.md) - Formula of the molecule
 * [from_resource](from_resource.md)
 * [from_species](from_species.md) - Holds between an entity and a Species.
 * [functional_impact](functional_impact.md) - Experimentally assessed functional impact of the allele, e.g. knockout / amorphic
 * [gene_synopsis](gene_synopsis.md) - Gene description provided by source resource (ie: MOD gene description that is curated or automated via MOD internal processes).
 * [gene_synopsis_URL](gene_synopsis_URL.md) - Gene description reference URL provided by source resource (aka: MOD) in the case where the curated gene_synopsis has a reference URL outside of the MOD.
 * [gene_type](gene_type.md) - SOTerm describing gene type
 * [generated_by](generated_by.md) - Holds between a material entity and an Agent that generated it: e.g., Thomas Blumenthal, Kornberg Laboratory.
 * [generation_method](generation_method.md) - Technique used to create the allele, e.g. spontaneous / naturally occuring / radiation
 * [genetic_sex](genetic_sex.md)
     * [DiseaseAnnotation➞genetic_sex](DiseaseAnnotation_genetic_sex.md)
 * [genomic_locations](genomic_locations.md)
 * [genomic_reference_sequence](genomic_reference_sequence.md) - reference genome sequence at variation position
 * [genomic_variant_sequence](genomic_variant_sequence.md) - variant genome sequence at variation position
 * [germline_transmission_status](germline_transmission_status.md) - For alleles made in cell lines, have they been transmitted to the germline of an animal
     * [Allele➞germline_transmission_status](Allele_germline_transmission_status.md)
 * [handle](handle.md) - A slot pointing to a free-text alias or 'handle' for a data object, such as a reference-specific alias for a data object used while curating.
     * [PaperHandle➞handle](PaperHandle_handle.md)
 * [has_allele](has_allele.md)
 * [has_assembly](has_assembly.md)
 * [has_figure](has_figure.md) - Holds between an entity and a Figure.
     * [Image➞has_figure](Image_has_figure.md) - The figure to which the image belongs.
 * [has_reference](has_reference.md) - Associated reference
     * [Figure➞has_reference](Figure_has_reference.md)
 * [heavy_chain_isotype](heavy_chain_isotype.md) - The isotype of the antibody heavy chain: e.g., IgA.
 * [height](height.md) - The height of the image (pixels).
 * [hgvs_coding_nomenclature](hgvs_coding_nomenclature.md) - HGVSc nomenclature for variation in coding sequence
     * [VariantTranscriptConsequence➞hgvs_coding_nomenclature](VariantTranscriptConsequence_hgvs_coding_nomenclature.md) - HGVS coding sequence (HGVSc) name
 * [hgvs_nomenclature](hgvs_nomenclature.md) - HGVSg nomenclature for variant
 * [hgvs_protein_nomenclature](hgvs_protein_nomenclature.md) - HGVSp nomenclature for variation in protein
     * [VariantTranscriptConsequence➞hgvs_protein_nomenclature](VariantTranscriptConsequence_hgvs_protein_nomenclature.md) - HGVS protein sequence (HGVSp) name
 * [id](id.md)
     * [Reference➞id](Reference_id.md)
     * [Resource➞id](Resource_id.md) - Precedence of identifiers for references is as follows: PMID if available; DOI if not; actual alternate CURIE otherwise.
 * [image_file](image_file.md) - The file representing the full-sized version of this image.
 * [image_medium_file](image_medium_file.md) - The file representing a medium-sized version of this image.
 * [image_thumbnail_file](image_thumbnail_file.md) - The file representing the thumbnail of this image.
 * [image_x_origin](image_x_origin.md) - The x coordinate start point when specifying a spatial section within a larger image.
     * [ImagePane➞image_x_origin](ImagePane_image_x_origin.md) - The x coordinate within a larger source image from which the pane begins.
     * [Image➞image_x_origin](Image_image_x_origin.md) - The x coordinate within a larger source image from which the crop begins.
 * [image_y_origin](image_y_origin.md) - The y coordinate start point when specifying a spatial section within a larger image.
     * [ImagePane➞image_y_origin](ImagePane_image_y_origin.md) - The y coordinate within a larger source image from which the pane begins.
     * [Image➞image_y_origin](Image_image_y_origin.md) - The y coordinate within a larger source image from which the crop begins.
 * [images](images.md) - Any associated image
     * [ImagePane➞images](ImagePane_images.md)
 * [in_collection](in_collection.md) - Set of high-throughput alleles made by large projects
 * [inchi](inchi.md) - InChi style description of the molecule
 * [inchi_key](inchi_key.md) - InChi key description of the molecule
 * [inferred_allele](inferred_allele.md) - The allele to which something is inferred to be associated.
     * [AGMDiseaseAnnotation➞inferred_allele](AGMDiseaseAnnotation_inferred_allele.md) - The allele to which the disease is inferred to be associated.
     * [AGMPhenotypeAnnotation➞inferred_allele](AGMPhenotypeAnnotation_inferred_allele.md) - The allele to which the phenotype is inferred to be associated.
 * [inferred_gene](inferred_gene.md) - The gene to which something is inferred to be associated.
     * [AGMDiseaseAnnotation➞inferred_gene](AGMDiseaseAnnotation_inferred_gene.md) - The gene to which the disease is inferred to be associated.
     * [AGMPhenotypeAnnotation➞inferred_gene](AGMPhenotypeAnnotation_inferred_gene.md) - The gene to which the phenotype is inferred to be associated.
     * [AlleleDiseaseAnnotation➞inferred_gene](AlleleDiseaseAnnotation_inferred_gene.md) - The gene to which the disease is inferred to be associated.
     * [AllelePhenotypeAnnotation➞inferred_gene](AllelePhenotypeAnnotation_inferred_gene.md) - The gene to which the phenotype is inferred to be associated.
 * [inheritence_mode](inheritence_mode.md) - Mode of inheritence, e.g. dominant / semi-dominant / recessive / unknown
 * [initials](initials.md)
 * [interaction_data_provider](interaction_data_provider.md) - The interaction database that curated the interaction. e.g. BioGRID
     * [GeneInteraction➞interaction_data_provider](GeneInteraction_interaction_data_provider.md)
 * [is_extinct](is_extinct.md) - Does the allele still exist in a population somewhere?
 * [is_obsolete](is_obsolete.md) - Entity is no longer current.
 * [iso_abbreviation](iso_abbreviation.md)
 * [issue_date](issue_date.md) - Date on which an entity was issued.
 * [issue_name](issue_name.md)
 * [iupac](iupac.md) - IUPAC name of the molecule
 * [keywords](keywords.md) - keywords tagging a publication
 * [label](label.md) - A short display name for the figure. For example: Figure 2, Figure 3B
 * [last_name](last_name.md)
 * [light_chain_isotype](light_chain_isotype.md) - The isotype of the antibody light chain: e.g., i4.
 * [located on](located_on.md)
 * [manufactured_by](manufactured_by.md) - Holds between a material entity and an Agent that has manufactured it: e.g., olecular Probes.
 * [medline_abbreviation](medline_abbreviation.md)
 * [member_terms](member_terms.md) - Set of VocabularyTerm objects in a Vocabulary object set
 * [middle_names](middle_names.md)
 * [mod_id](mod_id.md) - The model organism database (MOD) identifier/curie for the object
     * [DiseaseAnnotation➞mod_id](DiseaseAnnotation_mod_id.md) - The model organism database (MOD) identifier/curie for the disease annotation. Currently only used by WormBase for disease annotations, e.g. "WBDOannot00000907"
 * [mod_reference_types](mod_reference_types.md) - List of types as assigned at a MOD.
 * [modified_by](modified_by.md) - The individual that last modified the entity.
 * [molecular_mutation](molecular_mutation.md) - Description of the DNA changes if precise genomic location unknown
 * [month_published](month_published.md) - Month in which an entity was created.
 * [mutant_cell_lines](mutant_cell_lines.md) - Mutant cell lines known to carry the allele
     * [Allele➞mutant_cell_lines](Allele_mutant_cell_lines.md)
 * [mutation_description](mutation_description.md) - Additional information about the nature of the mutation not captured by the SOTerm
 * [mutation_type](mutation_type.md) - SO term for type of mutation
     * [MolecularMutation➞mutation_type](MolecularMutation_mutation_type.md)
 * [name](name.md) - a human-readable name for an entity
     * [Antibody➞name](Antibody_name.md) - Publicly displayed name of the antibody. It often includes the name of the antibody target: e.g., anti-WNT-4. It may also include the host species and antibody clonality.
     * [Molecule➞name](Molecule_name.md)
     * [VocabularyTerm➞name](VocabularyTerm_name.md)
     * [Vocabulary➞name](Vocabulary_name.md)
 * [namespace](namespace.md) - the namespace of the ontology.
 * [negated](negated.md) - if set to true, then the association is negated i.e. is not true
     * [DiseaseAnnotation➞negated](DiseaseAnnotation_negated.md) - The negative qualifier for the annotation.
 * [note_association](note_association.md) - Description of how a note is associated with an entity, e.g. curators comments / private / origin
 * [note_type](note_type.md)
     * [AntibodyNote➞note_type](AntibodyNote_note_type.md)
 * [notes](notes.md)
 * [online_issn](online_issn.md)
 * [orcid](orcid.md)
 * [origins](origins.md) - Affected genomic models that the allele was introduced in
 * [padding_left](padding_left.md) - flanking sequence upstream of the variation position on the sense strand of the reference genome
 * [padding_right](padding_right.md) - flanking sequence downstream of the variation position on the sense strand of the reference genome
 * [page_areas](page_areas.md)
 * [pages](pages.md) - page number of source referenced for statement or publication
 * [paper_handles](paper_handles.md) - A slot that points to a list of PaperHandle objects, pairings of a reference and a free text string that allows an object to have a reference-specific alias (or handle). Used for experimental conditions from ZFIN to label (in a reference-specific manner) individual experimental conditions when curating a particular reference.
     * [ExperimentalCondition➞paper_handles](ExperimentalCondition_paper_handles.md) - Used by ZFIN to provide reference-specific labels/aliases to experimental conditions; useful for referencing experimental conditions while curating.
 * [parent_cell_line](parent_cell_line.md) - Parental cell line of alleles made in embryonic stem cells
     * [Allele➞parent_cell_line](Allele_parent_cell_line.md)
 * [parental_populations](parental_populations.md)
 * [person id](person_id.md)
     * [Person➞person id](Person_person_id.md)
 * [phenotype_or_trait](phenotype_or_trait.md)
 * [phenotype_term](phenotype_term.md)
     * [PhenotypeAnnotation➞phenotype_term](PhenotypeAnnotation_phenotype_term.md)
 * [polyphen_prediction](polyphen_prediction.md) - PolyPhen-2 prediction
 * [polyphen_score](polyphen_score.md) - PolyPhen-2 score between 0 and 1
 * [prefix](prefix.md) - Denormalization to help with classifying types of crossReferences, distinguishing DOIs from PMC ids, etc.
 * [prefix_order](prefix_order.md) - The relative order of the resource when listed with other crossReferences.
 * [prefix_page](prefix_page.md) - The cateogry of pages the resource in the context of the URL associated with the crossReference provides.  Equivalent to the 'page' attribute in the Alliance resourceDescriptor file.
 * [print_issn](print_issn.md)
 * [private_comment](private_comment.md) - A private explanatory note from curators about some entity, for internal use only.
 * [private_note](private_note.md)
 * [protein_end](protein_end.md) - end position of variation in protein amino acid coordinates
     * [VariantTranscriptConsequence➞protein_end](VariantTranscriptConsequence_protein_end.md) - End position of variant in amino acid sequence
 * [protein_sequence](protein_sequence.md)
 * [protein_start](protein_start.md) - start position of variation in protein amino acid coordinates
     * [VariantTranscriptConsequence➞protein_start](VariantTranscriptConsequence_protein_start.md) - Start position of variant in amino acid sequence
 * [publisher](publisher.md)
 * [qualifiers](qualifiers.md) - This is the MeSH qualifier term that is optionally added to the descriptor term.
 * [reference](reference.md) - holds between an object and a single reference
     * [DiseaseAnnotation➞reference](DiseaseAnnotation_reference.md) - The reference in which the disease association was asserted/reported.
     * [PaperHandle➞reference](PaperHandle_reference.md)
     * [PhenotypeAnnotation➞reference](PhenotypeAnnotation_reference.md) - The reference in which the phenotype association was asserted/reported.
 * [reference_association](reference_association.md) - Description of how a reference is associated with an entity, e.g. molecular / origin / other
 * [references](references.md) - holds between an object and a list of references
     * [EntitySynonym➞references](EntitySynonym_references.md) - The references in which the synonym is used to refer to the entity.
     * [GeneInteraction➞references](GeneInteraction_references.md) - The reference from which the interaction was annotated.
     * [original_reference](original_reference.md) - Holds between an entity and the first reference to describe that entity.
         * [Antibody➞original_reference](Antibody_original_reference.md) - The reference providing the original description of the antibody's generation.
 * [related_to](related_to.md) - A relationship that is asserted between two named things.
     * [ameliorated_by](ameliorated_by.md)
     * [ameliorates](ameliorates.md)
     * [exacerbated_by](exacerbated_by.md)
     * [exacerbates](exacerbates.md)
     * [has_condition](has_condition.md)
     * [induced_by](induced_by.md)
     * [induces](induces.md)
     * [interacts_with](interacts_with.md) - holds between any two entities that directly or indirectly interact with each other
         * [genetically_interacts_with](genetically_interacts_with.md) - holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality.
         * [physically_interacts_with](physically_interacts_with.md) - holds between two entities that make physical contact as part of some interaction
     * [is_condition_in](is_condition_in.md)
 * [release](release.md) - MOD release ID
 * [secondary_identifiers](secondary_identifiers.md)
 * [sequence_targeting_reagents](sequence_targeting_reagents.md)
 * [sgd_strain_background](sgd_strain_background.md)
 * [sift_prediction](sift_prediction.md) - SIFT prediction
 * [sift_score](sift_score.md) - SIFT score between 0 and 1
 * [smiles](smiles.md) - Molecular structure in SMILES format
 * [start](start.md) - The start of the feature in positive 1-based integer coordinates
 * [statement_subject](statement_subject.md) - The entity being described by the note.
 * [statement_text](statement_text.md) - Free-text describing some aspect of an entity.
 * [statement_type](statement_type.md) - The type of free-text statement. For example: cytology, private, curator_comments.
 * [subsets](subsets.md)
 * [subtype](subtype.md) - Subtype of affected genomic model
 * [summary](summary.md)
 * [symbol](symbol.md) - Symbol for a particular thing
     * [Gene➞symbol](Gene_symbol.md)
 * [synonyms](synonyms.md) - holds between a named thing and a synonym
     * [Allele➞synonyms](Allele_synonyms.md) - synonyms for allele names and synonyms
 * [table_key](table_key.md) - The primary key for a specific table entry, unique for that table.
 * [tags](tags.md) - Optional ist of controlled vocabulary tags that give categories to each pub (ie: can show images).
 * [taxon](taxon.md) - The taxon from which the biological entity derives.
     * [BiologicalEntity➞taxon](BiologicalEntity_taxon.md)
         * [Antibody➞taxon](Antibody_taxon.md) - The species in which the antibody was raised: e.g., mouse, rabbit, guinea pig, goat, camel, etc.
     * [antigen_taxon](antigen_taxon.md) - Holds between an Antibody and the species from which the antigen originates (as represented by taxon).
 * [taxon_id](taxon_id.md) - NCBI taxid
 * [text_synonyms](text_synonyms.md) - Free text synonym(s) of a term, used for controlled vocabulary terms; this is distinct from the 'synonyms' slot which has a range of a Synonym class object.
 * [title](title.md) - A human readable title for a reference.
     * [Resource➞title](Resource_title.md) - the title of the publication
 * [topics](topics.md) - Connects an object to a vocabulary term or ontology that describes some aspect of the entity.
 * [transposon_insertion](transposon_insertion.md) - Associated transposon insertion that causes the mutation
     * [Allele➞transposon_insertion](Allele_transposon_insertion.md)
 * [type](type.md)
 * [uncertain](uncertain.md) - If set to true, then the related entity is uncertain.
 * [unique_id](unique_id.md) - A non-curie unique identifier for a thing.
     * [ConditionRelation➞unique_id](ConditionRelation_unique_id.md) - Unique identifer for the condition relation.  Will be generated at AGR.
     * [DiseaseAnnotation➞unique_id](DiseaseAnnotation_unique_id.md) - Unique identifer for the disease annotation.  Will be generated at AGR if not submitted by the MOD.
     * [ExperimentalCondition➞unique_id](ExperimentalCondition_unique_id.md) - Unique identifer for the experimental condition.  Will be generated at AGR.
 * [url_prefix](url_prefix.md) - The prefix of the url before the accession number.
 * [url_suffix](url_suffix.md) - The suffix of the url after the accession number.
 * [variant_of_allele](variant_of_allele.md)
 * [variant_of_transcript](variant_of_transcript.md)
 * [vep_consequence](vep_consequence.md) - VEP consequence
 * [vep_impact](vep_impact.md) - VEP predicted impact of variation on molecule
 * [video_still](video_still.md) - An image represents a video still.
 * [vocabulary_description](vocabulary_description.md) - The free text description of a Vocabulary including its intended use.
 * [volume](volume.md)
 * [volumes](volumes.md)
 * [width](width.md) - The width of the image (pixels).
 * [with](with.md) - http://geneontology.org/docs/go-annotation-file-gaf-format-2.2/#with-or-from-column-8
     * [DiseaseAnnotation➞with](DiseaseAnnotation_with.md) - A field for disease annotations that captures the human gene the implicated MOD gene is homologous or orthologous to when using the ISS (inferred from sequence similarity) evidence code or the ISO (inferred from sequence orthology) evidence code. The assertion would state that the MOD gene is implicated in the indicated disease based on sequence-similarity/sequence-orthology "with" some human gene. Currently used by SGD.
 * [year_published](year_published.md) - Year in which an entity was created.
 * [zygosity](zygosity.md) - GENO onotology ID for allele zygosity

### Enums

 * [aggregation_database_enum](aggregation_database_enum.md)
 * [agm_disease_relation_enum](agm_disease_relation_enum.md) - Permissible values describing the relationship between gene and disease.
 * [allele_disease_relation_enum](allele_disease_relation_enum.md) - Permissible values describing the relationship between allele and disease.
 * [annotation_type_enum](annotation_type_enum.md)
 * [antibody_clonality_set](antibody_clonality_set.md)
 * [antibody_note_type_set](antibody_note_type_set.md)
 * [component_relations_enum](component_relations_enum.md)
 * [condition_relation_enum](condition_relation_enum.md)
 * [database_statuses](database_statuses.md)
 * [detection_methods_enum](detection_methods_enum.md)
 * [disease_annotation_qualifier_enum](disease_annotation_qualifier_enum.md)
 * [entity_synonym_type_set](entity_synonym_type_set.md)
 * [gene_disease_relation_enum](gene_disease_relation_enum.md) - Permissible values describing the relationship between gene and disease.
 * [genetic_modifier_relation_enum](genetic_modifier_relation_enum.md) - Permissible values for describing how a genetic object modifies the disease model.
 * [genetic_sex_enum](genetic_sex_enum.md) - Permissible values for the genetic sex.
 * [heavy_chain_isotype_set](heavy_chain_isotype_set.md)
 * [interaction_source_enum](interaction_source_enum.md)
 * [interaction_type_enum](interaction_type_enum.md)
 * [interactor_A_role_enum](interactor_A_role_enum.md)
 * [interactor_B_role_enum](interactor_B_role_enum.md)
 * [interactor_type_enum](interactor_type_enum.md)
 * [light_chain_isotype_set](light_chain_isotype_set.md)
 * [modes_of_inheritence](modes_of_inheritence.md)
 * [note_association_types](note_association_types.md)
 * [polyphen_prediction_levels](polyphen_prediction_levels.md)
 * [reference_association_types](reference_association_types.md)
 * [sift_prediction_levels](sift_prediction_levels.md)
 * [subtype_values](subtype_values.md)
 * [tag_set](tag_set.md)
 * [vep_consequence_levels](vep_consequence_levels.md)
 * [zygosity_values](zygosity_values.md)

### Subsets

 * [AllianceSubset](AllianceSubset.md) - Subset consisting of just the alliance activities

### Types


#### Built in

 * **Bool**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [BiologicalSequence](types/BiologicalSequence.md)  ([String](types/String.md)) 
 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
