-- # Class: "ExpressionExperiment" Description: "Defined by the gene of interest, the specimen, the assay, the reagents (Antibody, Probe), and the reference. It groups ExpressionAnnotations."
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: biological_entity_assayed Description: Holds between a BiologicalEntity and an ExpressionExperiment that reports on its expression.
--     * Slot: assay_used Description: The assay used to experimentally determine gene expression.
--     * Slot: specimen_genomic_model Description: The AffectedGenomicModel of the specimen assayed.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "ExpressionAnnotation" Description: "A description of when and where gene products are observed to be present, including experimental details, supporting evidence, and curator notes."
--     * Slot: id Description: 
--     * Slot: belongs_to_expression_experiment Description: Holds between an ExpressionAnnotation and an ExpressionExperiment.
--     * Slot: expression_qualifiers Description: Qualifiers that describe additional characteristics of gene expression. For example: aint, intense, restricted.
--     * Slot: negated Description: if set to true, then the association is negated i.e. is not true
--     * Slot: uncertain Description: If set to true, then the related entity is uncertain.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: when_expressed_id Description: When a gene product is observed to be present.
--     * Slot: where_expressed_id Description: Where a gene product is observed to be present.
-- # Class: "TemporalContext" Description: "The developmental stage and/or age of the specimen in an annotation. Developmental_stage_stop is optional. Add an uncertainty flag here?"
--     * Slot: id Description: 
--     * Slot: developmental_stage_start Description: The beginning developmental stage at which an annotated event was observed.
--     * Slot: developmental_stage_stop Description: The end developmental stage at which an annotated event was observed.
--     * Slot: age Description: The age at which an annotated event was observed.
--     * Slot: temporal_qualifiers Description: Qualifiers of the stage or age in an annotation.
--     * Slot: stage_uncertainty Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AnatomicalSite" Description: "The developmental stage and/or age of the specimen in an annotation."
--     * Slot: id Description: 
--     * Slot: anatomical_structure Description: 
--     * Slot: anatomical_substructure Description: 
--     * Slot: cellular_component Description: 
--     * Slot: spatial_qualifiers Description: Qualifiers that describe the spatial characteristics of an event.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "ExpressionAnnotationImagePane" Description: ""
--     * Slot: id Description: 
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: subject_id Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: object_id Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
-- # Class: "GeneExpressionStatement" Description: "Free-text describing some aspect(s) of a gene's expression, particularly nuanced information that is not readily captured in annotations. May summarize data from many annotations and/or many publications."
--     * Slot: id Description: 
--     * Slot: statement_subject Description: The entity being described by the note.
--     * Slot: statement_type Description: The type of free-text statement. For example: cytology, private, curator_comments.
--     * Slot: statement_text Description: Free-text describing some aspect of an entity.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "ExpressionExperimentStatement" Description: "Free-text describing some aspect(s) of a gene's expression, particularly nuanced information that is not readily captured in annotations. This statement's scope is limited to the associated ExpressionExperiment."
--     * Slot: id Description: 
--     * Slot: statement_subject Description: The entity being described by the note.
--     * Slot: statement_type Description: The type of free-text statement. For example: cytology, private, curator_comments.
--     * Slot: statement_text Description: Free-text describing some aspect of an entity.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "ExpressionAnnotationStatement" Description: ""
--     * Slot: id Description: 
--     * Slot: statement_type Description: The type of free-text statement. For example: cytology, private, curator_comments.
--     * Slot: statement_text Description: Free-text describing some aspect of an entity.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: statement_subject_id Description: The entity being described by the note.
-- # Class: "AuthorReference" Description: ""
--     * Slot: id Description: 
--     * Slot: corresponding_author Description: 
--     * Slot: first_name Description: first name of a person
--     * Slot: middle_name Description: middle names of a person
--     * Slot: last_name Description: last (family) name of a person
--     * Slot: initials Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Reference" Description: ""
--     * Slot: abstract Description: The author summary of the publication.
--     * Slot: category Description: 
--     * Slot: citation Description: A short form way of referring to a publication, typically consisting of the first author's name, publication date, and journal (title, vol, pages).
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: date_published Description: Date on which an entity was created.
--     * Slot: issue_date Description: Date on which an entity was issued.
--     * Slot: issue_name Description: 
--     * Slot: language Description: Language of the reference
--     * Slot: merged_into_id Description: ID that used to refer to this reference
--     * Slot: open_access Description: Indicates if the reference is freely available for use by anyone, usually with fewer copyright and licensing barriers.
--     * Slot: pages Description: page number of source referenced for statement or publication
--     * Slot: plain_language_abstract Description: Plain language abstract
--     * Slot: publisher Description: 
--     * Slot: pubmed_publication_status Description: status of the publication
--     * Slot: reference_id Description: The primary key for the Reference object in the references table.
--     * Slot: resource_id Description: 
--     * Slot: title Description: A human readable title for a reference.
--     * Slot: volume Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "MeshDetail" Description: "Medical Subject Headings information coming from PubMed."
--     * Slot: id Description: 
--     * Slot: mesh_detail_id Description: The primary key for a MeshDetail object.
--     * Slot: reference_id Description: Here, a foreign key referring to the references table.
--     * Slot: heading_term Description: The MeSH term description or definition from PubMed. e.g. Measles in a Measles/epidemiology term.
--     * Slot: qualifier_term Description: The MeSH term subheading from PubMed, to narrow down the topic. e.g. epidemiology in a Measles/epidemiology term.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AuditedObject" Description: "Base class for all other LinkML classes. Some entity for which changes are tracked, including date/time of change, the agent responsible for the change, and whether the entity is internal (private)."
--     * Slot: id Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "BiologicalEntity" Description: "An entity of biological origin that can be unambiguously attributed to a single species."
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "GenomicEntity" Description: "An entity that is part of a genome (i.e. segment of the DNA molecule), is derived directly from the genome (i.e. RNA transcript molecule), or is derived indirectly from the genome (i.e. polypeptide or protein via RNA transcript translation)."
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Transcript" Description: "Placeholder."
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Gene" Description: "A DNA genomic entity from which one or more functional* RNA transcript molecules are transcribed, along with cis-regulatory elements responsible for regulating expression (transcription) of the gene. * A functional RNA molecule here can mean one that is directly responsible for the gene's function (e.g. catalysis, structure, etc.) or one that is translated to produce a functional polypeptide/protein. A pseudogene may be considered a gene under this definition, albeit no longer functional."
--     * Slot: symbol Description: Symbol for a particular thing
--     * Slot: gene_synopsis Description: Gene description provided by source resource (ie: MOD gene description that is curated or automated via MOD internal processes).
--     * Slot: gene_synopsis_URL Description: Gene description reference URL provided by source resource (aka: MOD) in the case where the curated gene_synopsis has a reference URL outside of the MOD.
--     * Slot: gene_type Description: SOTerm describing gene type
--     * Slot: automated_gene_description Description: Gene description generated via algorithm developed at the alliance.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
-- # Class: "CrossReference" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: display_name Description: 
--     * Slot: prefix Description: Denormalization to help with classifying types of crossReferences, distinguishing DOIs from PMC ids, etc.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: AuthorReference_id Description: Autocreated FK slot
--     * Slot: GenomicEntity_curie Description: Autocreated FK slot
--     * Slot: Transcript_curie Description: Autocreated FK slot
--     * Slot: Gene_curie Description: Autocreated FK slot
--     * Slot: Protein_curie Description: Autocreated FK slot
--     * Slot: OntologyTerm_curie Description: Autocreated FK slot
--     * Slot: DOTerm_curie Description: Autocreated FK slot
--     * Slot: ECOTerm_curie Description: Autocreated FK slot
--     * Slot: NCBITaxonTerm_curie Description: Autocreated FK slot
--     * Slot: FBCVTerm_curie Description: Autocreated FK slot
--     * Slot: GOTerm_curie Description: Autocreated FK slot
--     * Slot: ROTerm_curie Description: Autocreated FK slot
--     * Slot: MITerm_curie Description: Autocreated FK slot
--     * Slot: MMOTerm_curie Description: Autocreated FK slot
--     * Slot: MMUSDVTerm_curie Description: Autocreated FK slot
--     * Slot: SOTerm_curie Description: Autocreated FK slot
--     * Slot: XBEDTerm_curie Description: Autocreated FK slot
--     * Slot: CHEBITerm_curie Description: Autocreated FK slot
--     * Slot: StageTerm_curie Description: Autocreated FK slot
--     * Slot: FBDVTerm_curie Description: Autocreated FK slot
--     * Slot: WBLSTerm_curie Description: Autocreated FK slot
--     * Slot: XBSTerm_curie Description: Autocreated FK slot
--     * Slot: ZFSTerm_curie Description: Autocreated FK slot
--     * Slot: ExperimentalConditionOntologyTerm_curie Description: Autocreated FK slot
--     * Slot: ZECOTerm_curie Description: Autocreated FK slot
--     * Slot: XCOTerm_curie Description: Autocreated FK slot
--     * Slot: AnatomicalTerm_curie Description: Autocreated FK slot
--     * Slot: CLTerm_curie Description: Autocreated FK slot
--     * Slot: EMAPATerm_curie Description: Autocreated FK slot
--     * Slot: DAOTerm_curie Description: Autocreated FK slot
--     * Slot: MATerm_curie Description: Autocreated FK slot
--     * Slot: UBERONTerm_curie Description: Autocreated FK slot
--     * Slot: WBBTTerm_curie Description: Autocreated FK slot
--     * Slot: XBATerm_curie Description: Autocreated FK slot
--     * Slot: ZFATerm_curie Description: Autocreated FK slot
--     * Slot: PhenotypeTerm_curie Description: Autocreated FK slot
--     * Slot: XPOTerm_curie Description: Autocreated FK slot
--     * Slot: ChemicalTerm_curie Description: Autocreated FK slot
--     * Slot: XSMOTerm_curie Description: Autocreated FK slot
--     * Slot: Molecule_curie Description: Autocreated FK slot
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: Construct_curie Description: Autocreated FK slot
--     * Slot: SequenceTargetingReagent_curie Description: Autocreated FK slot
--     * Slot: ConstructComponent_curie Description: Autocreated FK slot
--     * Slot: AffectedGenomicModel_curie Description: Autocreated FK slot
--     * Slot: Variant_curie Description: Autocreated FK slot
--     * Slot: Antibody_curie Description: Autocreated FK slot
--     * Slot: GeneInteraction_curie Description: Autocreated FK slot
--     * Slot: GeneMolecularInteraction_curie Description: Autocreated FK slot
--     * Slot: GeneGeneticInteraction_curie Description: Autocreated FK slot
-- # Class: "Synonym" Description: ""
--     * Slot: id Description: 
--     * Slot: synonym Description: the text string of the synonym
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Note" Description: "Note object for capturing free-text describing some attribute of an entity, coupled with a 'note type', internal boolean, and an optional list of references. Permissible values for 'note_type' currently = disease_summary, disease_note"
--     * Slot: id Description: 
--     * Slot: free_text Description: A free text string that describes some aspect of an entity.
--     * Slot: note_type Description: The type of note: e.g., cytology, comment, summary. Permissible values for 'note_type' currently = disease_summary, disease_note
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "EntityStatement" Description: "Free-text describing some aspect of an entity."
--     * Slot: id Description: 
--     * Slot: statement_subject Description: The entity being described by the note.
--     * Slot: statement_type Description: The type of free-text statement. For example: cytology, private, curator_comments.
--     * Slot: statement_text Description: Free-text describing some aspect of an entity.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Association" Description: "A typed association between two entities, supported by evidence."
--     * Slot: id Description: 
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "EntitySynonym" Description: "A relationship between an entity and a synonym."
--     * Slot: id Description: 
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: object_id Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
-- # Class: "ExternalDatabaseLink" Description: "Base relation that holds the identifier prefix, base url and url suffix to help in generating URLs in crossReferences."
--     * Slot: id Description: 
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: prefix Description: Denormalization to help with classifying types of crossReferences, distinguishing DOIs from PMC ids, etc.
--     * Slot: url_prefix Description: The prefix of the url before the accession number.
--     * Slot: url_suffix Description: The suffix of the url after the accession number.
--     * Slot: prefix_page Description: The cateogry of pages the resource in the context of the URL associated with the crossReference provides.  Equivalent to the 'page' attribute in the Alliance resourceDescriptor file.
--     * Slot: prefix_order Description: The relative order of the resource when listed with other crossReferences.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Chromosome" Description: "The ID of the landmark used to establish the coordinate system for the current feature."
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Assembly" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "GenomicLocation" Description: ""
--     * Slot: id Description: 
--     * Slot: subject Description: subject should be a genomic entity
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: object should be the chromosome identifier
--     * Slot: has_assembly Description: 
--     * Slot: start Description: The start of the feature in positive 1-based integer coordinates
--     * Slot: end Description: The end of the feature in positive 1-based integer coordinates
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Protein" Description: ""
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "VocabularyTerm" Description: "A concept or class in a simple vocabulary."
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: abbreviation Description: 
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Vocabulary" Description: "A set of VocabularyTerm objects."
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: vocabulary_description Description: The free text description of a Vocabulary including its intended use.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "OntologyTerm" Description: "A concept or class in an ontology, vocabulary or thesaurus. Note, ontology terms can be found in multiple ontologies (ie: mireoting). defining_slots helps define an alternative key for ontology terms."
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The definition of the ontology term. This is a reference to an object that holds the text description of the term and a collection of URLs that further define the term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "DOTerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "ECOTerm" Description: ""
--     * Slot: abbreviation Description: Letter code used by curators to refer to the ECO term.
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "NCBITaxonTerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "FBCVTerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "GOTerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "ROTerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "MITerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "MMOTerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "MMUSDVTerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "SOTerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "XBEDTerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "CHEBITerm" Description: ""
--     * Slot: inchi Description: InChi style description of the molecule
--     * Slot: inchi_key Description: InChi key description of the molecule
--     * Slot: iupac Description: IUPAC name of the molecule
--     * Slot: formula Description: Formula of the molecule
--     * Slot: smiles Description: Molecular structure in SMILES format
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "StageTerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "FBDVTerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "WBLSTerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "XBSTerm" Description: "The Xenbase anatomy ontology XAO is home to Xenopus anatomy terms as well as Xenopus developmental life stage terms, differentiated by namespace. The anatomy term class in LinkML will be named 'XBATerm' for Xenbase Anatomy Term and life stage terms will be named 'XBSTerm' for Xenbase Stage Term."
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "ZFSTerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "ExperimentalConditionOntologyTerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "ZECOTerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "XCOTerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AnatomicalTerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "CLTerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "EMAPATerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "DAOTerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "MATerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "UBERONTerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "WBBTTerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "XBATerm" Description: "The Xenbase anatomy ontology XAO is home to Xenopus anatomy terms as well as Xenopus developmental life stage terms, differentiated by namespace. The anatomy term class in LinkML will be named 'XBATerm' for Xenbase Anatomy Term and life stage terms will be named 'XBSTerm' for Xenbase Stage Term."
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "ZFATerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "PhenotypeTerm" Description: "An ontology term representing a characteristic of an organism. This may or may not be expressed as a difference in comparison to a reference organism."
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "XPOTerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "ChemicalTerm" Description: "An ontology term representing a chemical or molecule"
--     * Slot: inchi Description: InChi style description of the molecule
--     * Slot: inchi_key Description: InChi key description of the molecule
--     * Slot: iupac Description: IUPAC name of the molecule
--     * Slot: formula Description: Formula of the molecule
--     * Slot: smiles Description: Molecular structure in SMILES format
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "XSMOTerm" Description: ""
--     * Slot: inchi Description: InChi style description of the molecule
--     * Slot: inchi_key Description: InChi key description of the molecule
--     * Slot: iupac Description: IUPAC name of the molecule
--     * Slot: formula Description: Formula of the molecule
--     * Slot: smiles Description: Molecular structure in SMILES format
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Molecule" Description: "Molecules as described by WormBase"
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: inchi Description: InChi style description of the molecule
--     * Slot: inchi_key Description: InChi key description of the molecule
--     * Slot: iupac Description: IUPAC name of the molecule
--     * Slot: formula Description: Formula of the molecule
--     * Slot: smiles Description: Molecular structure in SMILES format
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
-- # Class: "Allele" Description: "One of multiple possible forms of a functional genomic element (most often described as a locus or gene), differing from the reference DNA sequence.  The genomic element can be endogenous or constructed."
--     * Slot: symbol Description: Symbol for a particular thing
--     * Slot: functional_impact Description: Experimentally assessed functional impact of the allele, e.g. knockout / amorphic
--     * Slot: generation_method Description: Technique used to create the allele, e.g. spontaneous / naturally occuring / radiation
--     * Slot: germline_transmission_status Description: For alleles made in cell lines, have they been transmitted to the germline of an animal
--     * Slot: images Description: Any associated image
--     * Slot: database_status Description: Database status of the allele
--     * Slot: inheritence_mode Description: Mode of inheritence, e.g. dominant / semi-dominant / recessive / unknown
--     * Slot: in_collection Description: Set of high-throughput alleles made by large projects
--     * Slot: transposon_insertion Description: Associated transposon insertion that causes the mutation
--     * Slot: aberration Description: Associated deficiency (etc.) whose breakpoint causes the mutation
--     * Slot: is_extinct Description: Does the allele still exist in a population somewhere?
--     * Slot: sequencing_status Description: Status of whether or not the variant genomic location has been verified by sequencing
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
--     * Slot: parent_cell_line_id Description: Parental cell line of alleles made in embryonic stem cells
-- # Class: "AlleleGenomicEntityAssociation" Description: "Association between an allele and a genomic entity"
--     * Slot: id Description: 
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: evidence_code Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: related_note_id Description: Holds between an object and a Note object.
-- # Class: "AlleleGeneAssociation" Description: "Association between an allele and a gene"
--     * Slot: id Description: 
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: evidence_code Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: related_note_id Description: Holds between an object and a Note object.
-- # Class: "AlleleTranscriptAssociation" Description: "Association between an allele and a transcript"
--     * Slot: id Description: 
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: evidence_code Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: related_note_id Description: Holds between an object and a Note object.
-- # Class: "AlleleProteinAssociation" Description: "Association between an allele and a protein"
--     * Slot: id Description: 
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: evidence_code Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: related_note_id Description: Holds between an object and a Note object.
-- # Class: "AlleleVariantAssociation" Description: "The relationship between an allele and a variant is many to many. An Allele may have many variants and a variant can be present in many alleles."
--     * Slot: id Description: 
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: evidence_code Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: Ingest_id Description: Autocreated FK slot
--     * Slot: related_note_id Description: Holds between an object and a Note object.
-- # Class: "AssociatedReference" Description: "Describes the relation between a reference and an object"
--     * Slot: id Description: 
--     * Slot: reference_type Description: Description of how a reference is associated with an entity, e.g. molecular / origin / other
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Construct" Description: ""
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "CellLine" Description: "Dummy cell line class"
--     * Slot: id Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "SequenceTargetingReagent" Description: ""
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
-- # Class: "SequenceTargetingReagentToGeneAssociation" Description: "the relationship between a Sequence Targeting Reagent and its targeted genes."
--     * Slot: id Description: 
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "ConstructComponentAssociation" Description: ""
--     * Slot: id Description: 
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "ConstructComponent" Description: ""
--     * Slot: symbol Description: Symbol for a particular thing
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AffectedGenomicModel" Description: "Includes inbred strains, stocks, disease models and mutant genotypes"
--     * Slot: subtype Description: Subtype of affected genomic model
--     * Slot: parental_populations Description: 
--     * Slot: data_provider Description: Organization (e.g. MOD) from which the data was sourced
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
-- # Class: "AffectedGenomicModelComponent" Description: "Allele that affects the model and its zygosity"
--     * Slot: id Description: 
--     * Slot: has_allele Description: 
--     * Slot: zygosity Description: GENO onotology ID for allele zygosity
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Variant" Description: "A DNA, RNA or protein/polypeptide sequence that differs relative to a designated reference sequence.  The sequence occurs at a single position or in a range of contiguous nucleotides or amino acids."
--     * Slot: variant_type Description: SOTerm describing the type of variant. In practice, variant type will be limited to a subset of the SO specified in an Alliance controlled vocabulary in order to maintain consistency.
--     * Slot: source_general_consequence Description: SOTerm (child of SO:0001576 - transcript_variant) that describes the consequence of the variant, as stated in the source reference when no transcript ID is provided. Since a curator would determine variant location and consequences relative to at least one specific genome assembly, transcript and/or polypeptide, no slot for curated general consequence is provided.
--     * Slot: variant_status Description: 
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
-- # Class: "SourceVariantLocation" Description: "Links a paper to the variant locations described in that paper"
--     * Slot: id Description: 
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "VariantLocation" Description: "Base class linking a variant to a position on a genomic entity and the resulting consequence to the sequence and/or function of that genomic entity. Slots are provided for data taken from a source publication or data load and for data resulting from manual curation. Where the values are the same, the curator has confirmed the information from the source.  In other cases, the curator's analysis has resulted in different values, for instance, if the assembly is different, the source did not specify the transcript or protein isoform, the definition of the transcript or protein isoform used by the source has changed, or if there was an error in the source data."
--     * Slot: id Description: 
--     * Slot: evidence_code Description: 
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: start_position Description: Start position of variant on genomic entity.
--     * Slot: end_position Description: End position of variant on genomic entity.
--     * Slot: reference_sequence Description: Reference sequence of genome or genomic entity at position of aligned variant.
--     * Slot: variant_sequence Description: Sequence that differs from the reference sequence of genome or genomic entity at position of variant, as specified by curator.
--     * Slot: consequence Description: SOTerm (child of SO:0001576 - transcript_variant) that describes the consequence of the variant, as stated in the source reference. In practice source consequence will be associated with locations at any or all of VariantGenomeLocation, VariantTranscriptLocation, and VariantPolypeptideLocation.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "VariantGenomeLocation" Description: "Links a variant to a genomic position and the resulting consequence to the sequence and/or function. In practice, functional consequences for variants which overlap genes are not generally provided at the genome level but rather are calculated and annotated relative to a specific transcript or protein isoform."
--     * Slot: id Description: 
--     * Slot: assembly Description: Assembly to which variant is aligned.
--     * Slot: chromosome Description: Chromosome to which variant is aligned.
--     * Slot: evidence_code Description: 
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: start_position Description: Start position of variant on genomic entity.
--     * Slot: end_position Description: End position of variant on genomic entity.
--     * Slot: reference_sequence Description: Reference sequence of genome or genomic entity at position of aligned variant.
--     * Slot: variant_sequence Description: Sequence that differs from the reference sequence of genome or genomic entity at position of variant, as specified by curator.
--     * Slot: consequence Description: SOTerm (child of SO:0001576 - transcript_variant) that describes the consequence of the variant, as stated in the source reference. In practice source consequence will be associated with locations at any or all of VariantGenomeLocation, VariantTranscriptLocation, and VariantPolypeptideLocation.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "VariantTranscriptLocation" Description: "Links a variant to a position on a specified transcript and the resulting consequence to the sequence and/or function of that transcript."
--     * Slot: id Description: 
--     * Slot: transcript Description: Transcript associated with variant and for which a specific location and consequence of that variant is provided, as specified at source.  Multivalued=false for this slot because although a variant can have multiple VariantTranscriptLocation stanzas, each stanza will have one and only one source transcript ID.
--     * Slot: evidence_code Description: 
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: start_position Description: Start position of variant on genomic entity.
--     * Slot: end_position Description: End position of variant on genomic entity.
--     * Slot: reference_sequence Description: Reference sequence of genome or genomic entity at position of aligned variant.
--     * Slot: variant_sequence Description: Sequence that differs from the reference sequence of genome or genomic entity at position of variant, as specified by curator.
--     * Slot: consequence Description: SOTerm (child of SO:0001576 - transcript_variant) that describes the consequence of the variant, as stated in the source reference. In practice source consequence will be associated with locations at any or all of VariantGenomeLocation, VariantTranscriptLocation, and VariantPolypeptideLocation.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "VariantPolypeptideLocation" Description: "Links a variant to a position on a specified polypeptide and the resulting consequence to the sequence and/or function of that polypeptide."
--     * Slot: id Description: 
--     * Slot: polypeptide Description: Transcript associated with variant and for which a specific location and consequence of that variant is provided, as specified by curator. Multivalued=false for this slot because although a variant can have multiple VariantTranscriptLocation stanzas, each stanza will have one and only one curated transcript ID.
--     * Slot: evidence_code Description: 
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: start_position Description: Start position of variant on genomic entity.
--     * Slot: end_position Description: End position of variant on genomic entity.
--     * Slot: reference_sequence Description: Reference sequence of genome or genomic entity at position of aligned variant.
--     * Slot: variant_sequence Description: Sequence that differs from the reference sequence of genome or genomic entity at position of variant, as specified by curator.
--     * Slot: consequence Description: SOTerm (child of SO:0001576 - transcript_variant) that describes the consequence of the variant, as stated in the source reference. In practice source consequence will be associated with locations at any or all of VariantGenomeLocation, VariantTranscriptLocation, and VariantPolypeptideLocation.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Figure" Description: "An entity representing a figure or table in a publication."
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: label Description: A short display name for the figure. For example: Figure 2, Figure 3B
--     * Slot: caption Description: Text describing the contents of a figure or table in a publication.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "File" Description: "A dummy object."
--     * Slot: id Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Image" Description: "The set of files and metadata that constitute an image."
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: associated_with_figure Description: The figure to which the image belongs.
--     * Slot: width Description: The width of the image (pixels).
--     * Slot: height Description: The height of the image (pixels).
--     * Slot: cropped_from Description: Another larger image from which this image was cropped.
--     * Slot: image_x_origin Description: The x coordinate within a larger source image from which the crop begins.
--     * Slot: image_y_origin Description: The y coordinate within a larger source image from which the crop begins.
--     * Slot: video_still Description: An image represents a video still.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: image_file_id Description: The file representing the full-sized version of this image.
--     * Slot: image_medium_file_id Description: The file representing a medium-sized version of this image.
--     * Slot: image_thumbnail_file_id Description: The file representing the thumbnail of this image.
-- # Class: "ImagePane" Description: "Part of an Image that is relevant to some annotation. An annotation may reference many panes of an Image."
--     * Slot: id Description: 
--     * Slot: from_image Description: Holds between an ImagePane and an Image.
--     * Slot: label Description: A short display name for the figure. For example: Figure 2, Figure 3B
--     * Slot: width Description: The width of the image (pixels).
--     * Slot: height Description: The height of the image (pixels).
--     * Slot: image_x_origin Description: The x coordinate within a larger source image from which the pane begins.
--     * Slot: image_y_origin Description: The y coordinate within a larger source image from which the pane begins.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Agent" Description: "An individual, group, organization or project that provides information and/or materials."
--     * Slot: id Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Organization" Description: ""
--     * Slot: id Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Laboratory" Description: ""
--     * Slot: id Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Company" Description: ""
--     * Slot: id Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Person" Description: ""
--     * Slot: last_name Description: last (family) name of a person
--     * Slot: middle_name Description: middle names of a person
--     * Slot: first_name Description: first name of a person
--     * Slot: orcid Description: Open Researcher and Contributor ID
--     * Slot: mod_entity_id Description: The model organism database (MOD) identifier/curie for the object
--     * Slot: unique_id Description: A non-curie unique identifier for a thing.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "LoggedInPerson" Description: ""
--     * Slot: okta_id Description: The Okta identifier for the person registered in Okta for user authentication
--     * Slot: okta_email Description: The email address of the LoggedInPerson registered with Okta for user authentication
--     * Slot: last_name Description: last (family) name of a person
--     * Slot: middle_name Description: middle names of a person
--     * Slot: first_name Description: first name of a person
--     * Slot: orcid Description: Open Researcher and Contributor ID
--     * Slot: mod_entity_id Description: The model organism database (MOD) identifier/curie for the object
--     * Slot: unique_id Description: A non-curie unique identifier for a thing.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Resource" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: title Description: the title of the publication
--     * Slot: iso_abbreviation Description: 
--     * Slot: medline_abbreviation Description: 
--     * Slot: copyright_date Description: 
--     * Slot: print_issn Description: 
--     * Slot: online_issn Description: 
--     * Slot: publisher Description: 
--     * Slot: volume Description: 
--     * Slot: summary Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "PhenotypeAnnotation" Description: "An annotation asserting an association between a biological entity and a phenotype supported by evidence."
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: single_reference Description: The reference in which the phenotype association was asserted/reported.
--     * Slot: phenotype_term Description: 
--     * Slot: subject Description: The biological entity (e.g. gene, allele, genotype) to which the phenotype is associated, by direct curation.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: phenotype statement: The label of an individual phenotype term from a phenotype ontology or the post-composed statement of the phenotype from a post-composed terminology
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date of curation at the source (MOD) database.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "GenePhenotypeAnnotation" Description: "An annotation asserting an association between a gene and a phenotype supported by evidence."
--     * Slot: sgd_strain_background Description: 
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: phenotype_term Description: 
--     * Slot: subject Description: The gene to which the phenotype ontology term is associated.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AllelePhenotypeAnnotation" Description: "An annotation asserting an association between an allele and a phenotype supported by evidence."
--     * Slot: inferred_gene Description: The gene to which the phenotype is inferred to be associated.
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: phenotype_term Description: 
--     * Slot: subject Description: The allele to which the phenotype ontology term is associated.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AGMPhenotypeAnnotation" Description: "An annotation asserting an association between an AGM and a phenotype supported by evidence."
--     * Slot: inferred_allele Description: The allele to which the phenotype is inferred to be associated.
--     * Slot: inferred_gene Description: The gene to which the phenotype is inferred to be associated.
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: phenotype_term Description: 
--     * Slot: subject Description: The AGM to which the phenotype ontology term is associated.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "DiseaseAnnotation" Description: "An annotation asserting an association between a biological entity and a disease supported by evidence."
--     * Slot: id Description: 
--     * Slot: unique_id Description: Unique identifer for the disease annotation.  Will be generated at AGR if not submitted by the MOD.
--     * Slot: mod_entity_id Description: The model organism database (MOD) identifier/curie for the disease annotation. Currently only used by WormBase for disease annotations, e.g. "WBDOannot00000907"
--     * Slot: negated Description: The negative qualifier for the annotation.
--     * Slot: single_reference Description: The reference in which the disease association was asserted/reported.
--     * Slot: annotation_type Description: The type of annotation classified according to curation method. Submitted value should be a vocabulary term from the 'Annotation types' vocabulary
--     * Slot: genetic_sex Description: Submitted value should be a vocabulary term from the 'Genetic sexes' vocabulary
--     * Slot: data_provider Description: Organization (e.g. MOD) from which the data was sourced
--     * Slot: secondary_data_provider Description: Organization (e.g. MOD) that provided the data directly to the Alliance, but not the original source
--     * Slot: disease_genetic_modifier Description: Specifies a genetic object that modifies the disease model. May be a gene, allele, AGM.
--     * Slot: disease_genetic_modifier_relation Description: A relation describing how the genetic modifier modifies the disease model. Submitted value should be a vocabulary term from the 'Disease genetic modifiers' vocabulary
--     * Slot: subject Description: The biological entity to which the disease ontology term is associated.
--     * Slot: predicate Description: Constrains the disease subject, associationType and inferredGeneAssociation.
--     * Slot: object Description: The disease ontology term.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "GeneDiseaseAnnotation" Description: "An annotation asserting an association between a gene and a disease supported by evidence."
--     * Slot: id Description: 
--     * Slot: sgd_strain_background Description: 
--     * Slot: unique_id Description: A non-curie unique identifier for a thing.
--     * Slot: mod_entity_id Description: The model organism database (MOD) identifier/curie for the object
--     * Slot: negated Description: if set to true, then the association is negated i.e. is not true
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: annotation_type Description: The type of annotation classified according to curation method. Submitted value should be a vocabulary term from the 'Annotation types' vocabulary
--     * Slot: genetic_sex Description: Submitted value should be a vocabulary term from the 'Genetic sexes' vocabulary
--     * Slot: data_provider Description: Organization (e.g. MOD) from which the data was sourced
--     * Slot: secondary_data_provider Description: Organization (e.g. MOD) that provided the data directly to the Alliance, but not the original source
--     * Slot: disease_genetic_modifier Description: Specifies a genetic object that modifies the disease model. May be a gene, allele, AGM.
--     * Slot: disease_genetic_modifier_relation Description: A relation describing how the genetic modifier modifies the disease model. Submitted value should be a vocabulary term from the 'Disease genetic modifiers' vocabulary
--     * Slot: subject Description: The gene to which the disease ontology term is associated.
--     * Slot: predicate Description: The relationship between gene and disease. Submitted value should be a vocabulary term from the 'Gene disease relations' vocabulary
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
-- # Class: "AlleleDiseaseAnnotation" Description: "An annotation asserting an association between an allele and a disease supported by evidence."
--     * Slot: id Description: 
--     * Slot: inferred_gene Description: The gene to which the disease is inferred to be associated.
--     * Slot: unique_id Description: A non-curie unique identifier for a thing.
--     * Slot: mod_entity_id Description: The model organism database (MOD) identifier/curie for the object
--     * Slot: negated Description: if set to true, then the association is negated i.e. is not true
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: annotation_type Description: The type of annotation classified according to curation method. Submitted value should be a vocabulary term from the 'Annotation types' vocabulary
--     * Slot: genetic_sex Description: Submitted value should be a vocabulary term from the 'Genetic sexes' vocabulary
--     * Slot: data_provider Description: Organization (e.g. MOD) from which the data was sourced
--     * Slot: secondary_data_provider Description: Organization (e.g. MOD) that provided the data directly to the Alliance, but not the original source
--     * Slot: disease_genetic_modifier Description: Specifies a genetic object that modifies the disease model. May be a gene, allele, AGM.
--     * Slot: disease_genetic_modifier_relation Description: A relation describing how the genetic modifier modifies the disease model. Submitted value should be a vocabulary term from the 'Disease genetic modifiers' vocabulary
--     * Slot: subject Description: The allele to which the disease ontology term is associated.
--     * Slot: predicate Description: The relationship between allele and disease. Submitted value should be a vocabulary term from the 'Allele disease relations' vocabulary
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
-- # Class: "AGMDiseaseAnnotation" Description: "An annotation asserting an association between an AGM and a disease supported by evidence."
--     * Slot: id Description: 
--     * Slot: inferred_allele Description: The allele to which the disease is inferred to be associated.
--     * Slot: inferred_gene Description: The gene to which the disease is inferred to be associated.
--     * Slot: unique_id Description: A non-curie unique identifier for a thing.
--     * Slot: mod_entity_id Description: The model organism database (MOD) identifier/curie for the object
--     * Slot: negated Description: if set to true, then the association is negated i.e. is not true
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: annotation_type Description: The type of annotation classified according to curation method. Submitted value should be a vocabulary term from the 'Annotation types' vocabulary
--     * Slot: genetic_sex Description: Submitted value should be a vocabulary term from the 'Genetic sexes' vocabulary
--     * Slot: data_provider Description: Organization (e.g. MOD) from which the data was sourced
--     * Slot: secondary_data_provider Description: Organization (e.g. MOD) that provided the data directly to the Alliance, but not the original source
--     * Slot: disease_genetic_modifier Description: Specifies a genetic object that modifies the disease model. May be a gene, allele, AGM.
--     * Slot: disease_genetic_modifier_relation Description: A relation describing how the genetic modifier modifies the disease model. Submitted value should be a vocabulary term from the 'Disease genetic modifiers' vocabulary
--     * Slot: subject Description: The AGM to which the disease ontology term is associated.
--     * Slot: predicate Description: The relationship between AGM and disease. Submitted value should be a vocabulary term from the 'AGM disease relations' vocabulary
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
-- # Class: "ExperimentalCondition" Description: "The environmental context in which an experiment is carried out. This may (e.g. drug treatment) or may not (e.g. standard conditions) directly influence the outcome of the experiment."
--     * Slot: id Description: 
--     * Slot: unique_id Description: Unique identifer for the experimental condition.  Will be generated at AGR.
--     * Slot: condition_class Description: The ZECO ID that represents the high level condition grouping term.  This will come from a slim in the ZECO, called 'AllianceSlim'.
--     * Slot: condition_summary Description: Free text describing the environmental/experimental condition. For some groups this is a single term, others is it is a concatenation of the term names from the ontologies included in this data structure. Similar to condition_statement except the condition_summary will not be submitted by DQMs but rather generated at the Alliance after ingest (or generated/updated in the curation interface and persistent store).
--     * Slot: condition_statement Description: Free text describing the environmental/experimental condition. For some groups this is a single term, others is it is a concatenation of the term names from the ontologies included in this data structure. To be submitted by DQMs; eventually will be deprecated once DQMs no longer submit these ExperimentalCondition objects.
--     * Slot: condition_id Description: The specific ontology ID for the condition when that is not covered by any of the other condition ontology ID attributes (chemical, NCBITaxon, anatomical). This could also be another ZECO term if the ZECO term that describes this condition is more specific, or outside the conditionClassId slim.
--     * Slot: condition_free_text Description: Free-text description of the experimental condition
--     * Slot: condition_quantity Description: Optional free text field that records the units/amount/degrees of a condition.
--     * Slot: condition_anatomy Description: Anatomical ontology identifier used in cases like regeneration/wounding.
--     * Slot: condition_gene_ontology Description: Gene Ontology id used in subset of condition types.
--     * Slot: condition_taxon Description: NCBITaxon ontology id used in subset of condition types like 'bacterial infection'.
--     * Slot: condition_chemical Description: ChEBI or molecular ontology id used in subset of condition terms.  ie: the specific chemcial used in conjunction with 'chemical condition'.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: ConditionRelation_id Description: Autocreated FK slot
-- # Class: "ConditionRelation" Description: "A pairing of an experimental condition relation (i.e. has_condition) with a list of 1 or more ExperimentalCondition objects. Annotation objects can connect directly to a set of 0 or more of these ConditionRelation objects via a 'condition_relations' slot to express the experimental conditions relevant to the annotation."
--     * Slot: id Description: 
--     * Slot: unique_id Description: Unique identifer for the condition relation.  Will be generated at AGR.
--     * Slot: handle Description: A slot pointing to a free-text alias or 'handle' for a data object, such as a reference-specific alias for a data object used while curating.
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: condition_relation_type Description: Submitted value should be a vocabulary term from the 'Condition relation types' vocabulary
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: ExpressionExperiment_curie Description: Autocreated FK slot
--     * Slot: PhenotypeAnnotation_curie Description: Autocreated FK slot
--     * Slot: GenePhenotypeAnnotation_curie Description: Autocreated FK slot
--     * Slot: AllelePhenotypeAnnotation_curie Description: Autocreated FK slot
--     * Slot: AGMPhenotypeAnnotation_curie Description: Autocreated FK slot
--     * Slot: DiseaseAnnotation_id Description: Autocreated FK slot
--     * Slot: GeneDiseaseAnnotation_id Description: Autocreated FK slot
--     * Slot: AlleleDiseaseAnnotation_id Description: Autocreated FK slot
--     * Slot: AGMDiseaseAnnotation_id Description: Autocreated FK slot
-- # Class: "Reagent" Description: "A material entity used in experiments."
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Antibody" Description: "Immunoglobulin proteins that bind specific molecule(s). Can be used experimentally for the purposes of detection or purification."
--     * Slot: name Description: Publicly displayed name of the antibody. It often includes the name of the antibody target: e.g., anti-WNT-4. It may also include the host species and antibody clonality.
--     * Slot: antigen_taxon Description: Holds between an Antibody and the species from which the antigen originates (as represented by taxon).
--     * Slot: clonality Description: The clonality of the antibody: e.g., monoclonal.
--     * Slot: heavy_chain_isotype Description: The isotype of the antibody heavy chain: e.g., IgA.
--     * Slot: light_chain_isotype Description: The isotype of the antibody light chain: e.g., i4.
--     * Slot: curie Description: A unique identifier for the antibody: e.g., WBAntibody0000001.
--     * Slot: taxon Description: The species in which the antibody was raised: e.g., mouse, rabbit, guinea pig, goat, camel, etc.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "DNAClone" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "RNAClone" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Ingest" Description: ""
--     * Slot: id Description: 
-- # Class: "GeneToGeneAssociation" Description: "abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction."
--     * Slot: id Description: 
--     * Slot: subject Description: the subject gene in the association. If the relation is symmetric, subject vs object is arbitrary. We allow a gene product to stand as a proxy for the gene or vice versa.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: the object gene in the association. If the relation is symmetric, subject vs object is arbitrary. We allow a gene product to stand as a proxy for the gene or vice versa.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "GeneInteraction" Description: "An interaction between two genes or gene products; this may be a physical molecular interaction between gene products (e.g. protein-protein interactions), or may be a genetic interaction between genes (e.g. phenotypic suppression)"
--     * Slot: curie Description: The unique primary identifier for the interaction. This should be the source (curation) database identifier, or if that is not available then the aggregation database identifier (e.g. IMEx)
--     * Slot: interaction_data_provider Description: The interaction database that curated the interaction. e.g. BioGRID
--     * Slot: interaction_type Description: The type of interaction between the two genes or gene products. e.g. physical association
--     * Slot: interactor_A_type Description: 
--     * Slot: interactor_B_type Description: 
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "GeneMolecularInteraction" Description: "A physical molecular interaction between gene products (e.g. protein-protein interactions or protein-RNA interactions) or between genes and DNA-binding factors (e.g. protein-DNA interactions)"
--     * Slot: aggregation_database Description: The database that collected the interaction annotation from another resource and aggregated it into a consolidated resource. e.g. IMEx
--     * Slot: detection_method Description: The experimental method used to identify the physical interaction between two molecules
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: interaction_data_provider Description: The interaction database that curated the interaction. e.g. BioGRID
--     * Slot: interaction_type Description: The type of interaction between the two genes or gene products. e.g. physical association
--     * Slot: interactor_A_type Description: 
--     * Slot: interactor_B_type Description: 
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "GeneGeneticInteraction" Description: "A genetic interaction between genes (e.g. phenotypic suppression)"
--     * Slot: interactor_A_genetic_perturbation Description: 
--     * Slot: interactor_B_genetic_perturbation Description: 
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: interaction_data_provider Description: The interaction database that curated the interaction. e.g. BioGRID
--     * Slot: interaction_type Description: The type of interaction between the two genes or gene products. e.g. physical association
--     * Slot: interactor_A_type Description: 
--     * Slot: interactor_B_type Description: 
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "VariantConsequence" Description: "Parent class for gene- and transcript-level consequences"
--     * Slot: id Description: 
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: vep_consequence Description: VEP consequence
--     * Slot: vep_impact Description: VEP predicted impact of variation on molecule
--     * Slot: polyphen_score Description: PolyPhen-2 score between 0 and 1
--     * Slot: polyphen_prediction Description: PolyPhen-2 prediction
--     * Slot: sift_score Description: SIFT score between 0 and 1
--     * Slot: sift_prediction Description: SIFT prediction
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "VariantGeneConsequence" Description: "Class for gene-level VEP results"
--     * Slot: id Description: 
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: vep_consequence Description: VEP consequence
--     * Slot: vep_impact Description: VEP predicted impact of variation on molecule
--     * Slot: polyphen_score Description: PolyPhen-2 score between 0 and 1
--     * Slot: polyphen_prediction Description: PolyPhen-2 prediction
--     * Slot: sift_score Description: SIFT score between 0 and 1
--     * Slot: sift_prediction Description: SIFT prediction
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: subject_id Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
-- # Class: "VariantTranscriptConsequence" Description: "Class for transcript-level VEP results"
--     * Slot: id Description: 
--     * Slot: amino_acid_reference Description: Amino acid sequence encoded by codon(s) in reference genome sequence altered by the variant
--     * Slot: amino_acid_variant Description: Amino acid sequence encoded by codon(s) in variant sequence
--     * Slot: codon_reference Description: Reference genome sequence of codon(s) altered by the variant.  Bases affected by the variant are given in upper case, bases flanking the variation are given in lower case
--     * Slot: codon_variant Description: Sequence of codon(s) in variant sequence altered by the variant. Bases affected by the variant are given in upper case, bases flanking the variation are given in lower case
--     * Slot: cdna_start Description: Start position of variant in cDNA coordinates
--     * Slot: cdna_end Description: end position of variation in cDNA coordinates
--     * Slot: cds_start Description: Start position of variant in CDS coordinates
--     * Slot: cds_end Description: End position of variant in CDS coordinates
--     * Slot: protein_start Description: Start position of variant in amino acid sequence
--     * Slot: protein_end Description: End position of variant in amino acid sequence
--     * Slot: hgvs_protein_nomenclature Description: HGVS protein sequence (HGVSp) name
--     * Slot: hgvs_coding_nomenclature Description: HGVS coding sequence (HGVSc) name
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: vep_consequence Description: VEP consequence
--     * Slot: vep_impact Description: VEP predicted impact of variation on molecule
--     * Slot: polyphen_score Description: PolyPhen-2 score between 0 and 1
--     * Slot: polyphen_prediction Description: PolyPhen-2 prediction
--     * Slot: sift_score Description: SIFT score between 0 and 1
--     * Slot: sift_prediction Description: SIFT prediction
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: modified_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: subject_id Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
-- # Class: "ExpressionExperiment_reagents_used" Description: ""
--     * Slot: ExpressionExperiment_curie Description: Autocreated FK slot
--     * Slot: reagents_used Description: Reagents used in the expression assay: e.g., antibodies, probes.
-- # Class: "ExpressionExperiment_specimen_alleles" Description: ""
--     * Slot: ExpressionExperiment_curie Description: Autocreated FK slot
--     * Slot: specimen_alleles Description: The Allele(s) of the specimen assayed.
-- # Class: "ExpressionAnnotation_associated_with_figure" Description: ""
--     * Slot: ExpressionAnnotation_id Description: Autocreated FK slot
--     * Slot: associated_with_figure Description: The figure(s) that support(s) the expression annotation.
-- # Class: "GeneExpressionStatement_reference" Description: ""
--     * Slot: GeneExpressionStatement_id Description: Autocreated FK slot
--     * Slot: reference Description: holds between an object and a list of references
-- # Class: "ExpressionExperimentStatement_reference" Description: ""
--     * Slot: ExpressionExperimentStatement_id Description: Autocreated FK slot
--     * Slot: reference Description: holds between an object and a list of references
-- # Class: "ExpressionAnnotationStatement_reference" Description: ""
--     * Slot: ExpressionAnnotationStatement_id Description: Autocreated FK slot
--     * Slot: reference Description: holds between an object and a list of references
-- # Class: "Reference_date_arrived_in_pubmed" Description: ""
--     * Slot: Reference_curie Description: Autocreated FK slot
--     * Slot: date_arrived_in_pubmed Description: Day in which a reference or resource was created in PUBMED. Only relevant for PUBMED references.
-- # Class: "Reference_keywords" Description: ""
--     * Slot: Reference_curie Description: Autocreated FK slot
--     * Slot: keywords Description: keywords tagging a publication
-- # Class: "Reference_pubmed_abstract_languages" Description: ""
--     * Slot: Reference_curie Description: Autocreated FK slot
--     * Slot: pubmed_abstract_languages Description: Languages for the abstract
-- # Class: "Reference_pubmed_type" Description: ""
--     * Slot: Reference_curie Description: Autocreated FK slot
--     * Slot: pubmed_type Description: Type of Reference as described by PubMed.
-- # Class: "GenomicEntity_synonym" Description: ""
--     * Slot: GenomicEntity_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "GenomicEntity_secondary_identifiers" Description: ""
--     * Slot: GenomicEntity_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "GenomicEntity_genomic_locations" Description: ""
--     * Slot: GenomicEntity_curie Description: Autocreated FK slot
--     * Slot: genomic_locations_id Description: 
-- # Class: "Transcript_synonym" Description: ""
--     * Slot: Transcript_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "Transcript_secondary_identifiers" Description: ""
--     * Slot: Transcript_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "Transcript_genomic_locations" Description: ""
--     * Slot: Transcript_curie Description: Autocreated FK slot
--     * Slot: genomic_locations_id Description: 
-- # Class: "Gene_synonym" Description: ""
--     * Slot: Gene_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "Gene_secondary_identifiers" Description: ""
--     * Slot: Gene_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "Gene_genomic_locations" Description: ""
--     * Slot: Gene_curie Description: Autocreated FK slot
--     * Slot: genomic_locations_id Description: 
-- # Class: "CrossReference_page_areas" Description: ""
--     * Slot: CrossReference_curie Description: Autocreated FK slot
--     * Slot: page_areas Description: 
-- # Class: "Note_reference" Description: ""
--     * Slot: Note_id Description: Autocreated FK slot
--     * Slot: reference Description: holds between an object and a list of references
-- # Class: "EntityStatement_reference" Description: ""
--     * Slot: EntityStatement_id Description: Autocreated FK slot
--     * Slot: reference Description: holds between an object and a list of references
-- # Class: "Protein_synonym" Description: ""
--     * Slot: Protein_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "Protein_secondary_identifiers" Description: ""
--     * Slot: Protein_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "Protein_genomic_locations" Description: ""
--     * Slot: Protein_curie Description: Autocreated FK slot
--     * Slot: genomic_locations_id Description: 
-- # Class: "VocabularyTerm_text_synonyms" Description: ""
--     * Slot: VocabularyTerm_name Description: Autocreated FK slot
--     * Slot: text_synonyms Description: Free text synonym(s) of a term, used for controlled vocabulary terms; this is distinct from the 'synonyms' slot which has a range of a Synonym class object.
-- # Class: "Vocabulary_member_terms" Description: ""
--     * Slot: Vocabulary_name Description: Autocreated FK slot
--     * Slot: member_terms Description: Set of VocabularyTerm objects in a Vocabulary object set
-- # Class: "OntologyTerm_definition_urls" Description: ""
--     * Slot: OntologyTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "OntologyTerm_synonym" Description: ""
--     * Slot: OntologyTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "OntologyTerm_subsets" Description: ""
--     * Slot: OntologyTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "OntologyTerm_secondary_identifiers" Description: ""
--     * Slot: OntologyTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "DOTerm_definition_urls" Description: ""
--     * Slot: DOTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "DOTerm_synonym" Description: ""
--     * Slot: DOTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "DOTerm_subsets" Description: ""
--     * Slot: DOTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "DOTerm_secondary_identifiers" Description: ""
--     * Slot: DOTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "ECOTerm_definition_urls" Description: ""
--     * Slot: ECOTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "ECOTerm_synonym" Description: ""
--     * Slot: ECOTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "ECOTerm_subsets" Description: ""
--     * Slot: ECOTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "ECOTerm_secondary_identifiers" Description: ""
--     * Slot: ECOTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "NCBITaxonTerm_definition_urls" Description: ""
--     * Slot: NCBITaxonTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "NCBITaxonTerm_synonym" Description: ""
--     * Slot: NCBITaxonTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "NCBITaxonTerm_subsets" Description: ""
--     * Slot: NCBITaxonTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "NCBITaxonTerm_secondary_identifiers" Description: ""
--     * Slot: NCBITaxonTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "FBCVTerm_definition_urls" Description: ""
--     * Slot: FBCVTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "FBCVTerm_synonym" Description: ""
--     * Slot: FBCVTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "FBCVTerm_subsets" Description: ""
--     * Slot: FBCVTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "FBCVTerm_secondary_identifiers" Description: ""
--     * Slot: FBCVTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "GOTerm_definition_urls" Description: ""
--     * Slot: GOTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "GOTerm_synonym" Description: ""
--     * Slot: GOTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "GOTerm_subsets" Description: ""
--     * Slot: GOTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "GOTerm_secondary_identifiers" Description: ""
--     * Slot: GOTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "ROTerm_definition_urls" Description: ""
--     * Slot: ROTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "ROTerm_synonym" Description: ""
--     * Slot: ROTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "ROTerm_subsets" Description: ""
--     * Slot: ROTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "ROTerm_secondary_identifiers" Description: ""
--     * Slot: ROTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "MITerm_definition_urls" Description: ""
--     * Slot: MITerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "MITerm_synonym" Description: ""
--     * Slot: MITerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "MITerm_subsets" Description: ""
--     * Slot: MITerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "MITerm_secondary_identifiers" Description: ""
--     * Slot: MITerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "MMOTerm_definition_urls" Description: ""
--     * Slot: MMOTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "MMOTerm_synonym" Description: ""
--     * Slot: MMOTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "MMOTerm_subsets" Description: ""
--     * Slot: MMOTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "MMOTerm_secondary_identifiers" Description: ""
--     * Slot: MMOTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "MMUSDVTerm_definition_urls" Description: ""
--     * Slot: MMUSDVTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "MMUSDVTerm_synonym" Description: ""
--     * Slot: MMUSDVTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "MMUSDVTerm_subsets" Description: ""
--     * Slot: MMUSDVTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "MMUSDVTerm_secondary_identifiers" Description: ""
--     * Slot: MMUSDVTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "SOTerm_definition_urls" Description: ""
--     * Slot: SOTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "SOTerm_synonym" Description: ""
--     * Slot: SOTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "SOTerm_subsets" Description: ""
--     * Slot: SOTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "SOTerm_secondary_identifiers" Description: ""
--     * Slot: SOTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "XBEDTerm_definition_urls" Description: ""
--     * Slot: XBEDTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "XBEDTerm_synonym" Description: ""
--     * Slot: XBEDTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "XBEDTerm_subsets" Description: ""
--     * Slot: XBEDTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "XBEDTerm_secondary_identifiers" Description: ""
--     * Slot: XBEDTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "CHEBITerm_definition_urls" Description: ""
--     * Slot: CHEBITerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "CHEBITerm_synonym" Description: ""
--     * Slot: CHEBITerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "CHEBITerm_subsets" Description: ""
--     * Slot: CHEBITerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "CHEBITerm_secondary_identifiers" Description: ""
--     * Slot: CHEBITerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "StageTerm_definition_urls" Description: ""
--     * Slot: StageTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "StageTerm_synonym" Description: ""
--     * Slot: StageTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "StageTerm_subsets" Description: ""
--     * Slot: StageTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "StageTerm_secondary_identifiers" Description: ""
--     * Slot: StageTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "FBDVTerm_definition_urls" Description: ""
--     * Slot: FBDVTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "FBDVTerm_synonym" Description: ""
--     * Slot: FBDVTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "FBDVTerm_subsets" Description: ""
--     * Slot: FBDVTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "FBDVTerm_secondary_identifiers" Description: ""
--     * Slot: FBDVTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "WBLSTerm_definition_urls" Description: ""
--     * Slot: WBLSTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "WBLSTerm_synonym" Description: ""
--     * Slot: WBLSTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "WBLSTerm_subsets" Description: ""
--     * Slot: WBLSTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "WBLSTerm_secondary_identifiers" Description: ""
--     * Slot: WBLSTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "XBSTerm_definition_urls" Description: ""
--     * Slot: XBSTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "XBSTerm_synonym" Description: ""
--     * Slot: XBSTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "XBSTerm_subsets" Description: ""
--     * Slot: XBSTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "XBSTerm_secondary_identifiers" Description: ""
--     * Slot: XBSTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "ZFSTerm_definition_urls" Description: ""
--     * Slot: ZFSTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "ZFSTerm_synonym" Description: ""
--     * Slot: ZFSTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "ZFSTerm_subsets" Description: ""
--     * Slot: ZFSTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "ZFSTerm_secondary_identifiers" Description: ""
--     * Slot: ZFSTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "ExperimentalConditionOntologyTerm_definition_urls" Description: ""
--     * Slot: ExperimentalConditionOntologyTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "ExperimentalConditionOntologyTerm_synonym" Description: ""
--     * Slot: ExperimentalConditionOntologyTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "ExperimentalConditionOntologyTerm_subsets" Description: ""
--     * Slot: ExperimentalConditionOntologyTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "ExperimentalConditionOntologyTerm_secondary_identifiers" Description: ""
--     * Slot: ExperimentalConditionOntologyTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "ZECOTerm_definition_urls" Description: ""
--     * Slot: ZECOTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "ZECOTerm_synonym" Description: ""
--     * Slot: ZECOTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "ZECOTerm_subsets" Description: ""
--     * Slot: ZECOTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "ZECOTerm_secondary_identifiers" Description: ""
--     * Slot: ZECOTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "XCOTerm_definition_urls" Description: ""
--     * Slot: XCOTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "XCOTerm_synonym" Description: ""
--     * Slot: XCOTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "XCOTerm_subsets" Description: ""
--     * Slot: XCOTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "XCOTerm_secondary_identifiers" Description: ""
--     * Slot: XCOTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "AnatomicalTerm_definition_urls" Description: ""
--     * Slot: AnatomicalTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "AnatomicalTerm_synonym" Description: ""
--     * Slot: AnatomicalTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "AnatomicalTerm_subsets" Description: ""
--     * Slot: AnatomicalTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "AnatomicalTerm_secondary_identifiers" Description: ""
--     * Slot: AnatomicalTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "CLTerm_definition_urls" Description: ""
--     * Slot: CLTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "CLTerm_synonym" Description: ""
--     * Slot: CLTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "CLTerm_subsets" Description: ""
--     * Slot: CLTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "CLTerm_secondary_identifiers" Description: ""
--     * Slot: CLTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "EMAPATerm_definition_urls" Description: ""
--     * Slot: EMAPATerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "EMAPATerm_synonym" Description: ""
--     * Slot: EMAPATerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "EMAPATerm_subsets" Description: ""
--     * Slot: EMAPATerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "EMAPATerm_secondary_identifiers" Description: ""
--     * Slot: EMAPATerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "DAOTerm_definition_urls" Description: ""
--     * Slot: DAOTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "DAOTerm_synonym" Description: ""
--     * Slot: DAOTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "DAOTerm_subsets" Description: ""
--     * Slot: DAOTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "DAOTerm_secondary_identifiers" Description: ""
--     * Slot: DAOTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "MATerm_definition_urls" Description: ""
--     * Slot: MATerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "MATerm_synonym" Description: ""
--     * Slot: MATerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "MATerm_subsets" Description: ""
--     * Slot: MATerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "MATerm_secondary_identifiers" Description: ""
--     * Slot: MATerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "UBERONTerm_definition_urls" Description: ""
--     * Slot: UBERONTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "UBERONTerm_synonym" Description: ""
--     * Slot: UBERONTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "UBERONTerm_subsets" Description: ""
--     * Slot: UBERONTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "UBERONTerm_secondary_identifiers" Description: ""
--     * Slot: UBERONTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "WBBTTerm_definition_urls" Description: ""
--     * Slot: WBBTTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "WBBTTerm_synonym" Description: ""
--     * Slot: WBBTTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "WBBTTerm_subsets" Description: ""
--     * Slot: WBBTTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "WBBTTerm_secondary_identifiers" Description: ""
--     * Slot: WBBTTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "XBATerm_definition_urls" Description: ""
--     * Slot: XBATerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "XBATerm_synonym" Description: ""
--     * Slot: XBATerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "XBATerm_subsets" Description: ""
--     * Slot: XBATerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "XBATerm_secondary_identifiers" Description: ""
--     * Slot: XBATerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "ZFATerm_definition_urls" Description: ""
--     * Slot: ZFATerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "ZFATerm_synonym" Description: ""
--     * Slot: ZFATerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "ZFATerm_subsets" Description: ""
--     * Slot: ZFATerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "ZFATerm_secondary_identifiers" Description: ""
--     * Slot: ZFATerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "PhenotypeTerm_definition_urls" Description: ""
--     * Slot: PhenotypeTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "PhenotypeTerm_synonym" Description: ""
--     * Slot: PhenotypeTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "PhenotypeTerm_subsets" Description: ""
--     * Slot: PhenotypeTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "PhenotypeTerm_secondary_identifiers" Description: ""
--     * Slot: PhenotypeTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "XPOTerm_definition_urls" Description: ""
--     * Slot: XPOTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "XPOTerm_synonym" Description: ""
--     * Slot: XPOTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "XPOTerm_subsets" Description: ""
--     * Slot: XPOTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "XPOTerm_secondary_identifiers" Description: ""
--     * Slot: XPOTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "ChemicalTerm_definition_urls" Description: ""
--     * Slot: ChemicalTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "ChemicalTerm_synonym" Description: ""
--     * Slot: ChemicalTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "ChemicalTerm_subsets" Description: ""
--     * Slot: ChemicalTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "ChemicalTerm_secondary_identifiers" Description: ""
--     * Slot: ChemicalTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "XSMOTerm_definition_urls" Description: ""
--     * Slot: XSMOTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "XSMOTerm_synonym" Description: ""
--     * Slot: XSMOTerm_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "XSMOTerm_subsets" Description: ""
--     * Slot: XSMOTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "XSMOTerm_secondary_identifiers" Description: ""
--     * Slot: XSMOTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "Molecule_definition_urls" Description: ""
--     * Slot: Molecule_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "Molecule_synonym" Description: ""
--     * Slot: Molecule_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "Molecule_subsets" Description: ""
--     * Slot: Molecule_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "Molecule_secondary_identifiers" Description: ""
--     * Slot: Molecule_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "Allele_contains_constructs" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: contains_constructs Description: 
-- # Class: "Allele_molecular_mutations" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: molecular_mutations Description: Description of the DNA changes if precise genomic location unknown
-- # Class: "Allele_associated_references" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: associated_references_id Description: List of references associated with the entity in some way with a description of the association.
-- # Class: "Allele_related_notes" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: related_notes_id Description: Holds between an object and a list of related Note objects.
-- # Class: "Allele_mutant_cell_line" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: mutant_cell_line_id Description: Mutant cell lines known to carry the allele
-- # Class: "Allele_embryonic_stem_cell_line" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: embryonic_stem_cell_line_id Description: Embryonic stem cell lines known to carry the allele
-- # Class: "Allele_origin" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: origin Description: Affected genomic models that the allele was introduced in
-- # Class: "Allele_synonym" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: synonyms for allele names and synonyms
-- # Class: "Allele_secondary_identifiers" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "Allele_genomic_locations" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: genomic_locations_id Description: 
-- # Class: "Construct_construct_components" Description: ""
--     * Slot: Construct_curie Description: Autocreated FK slot
--     * Slot: construct_components Description: 
-- # Class: "Construct_reference" Description: ""
--     * Slot: Construct_curie Description: Autocreated FK slot
--     * Slot: reference Description: holds between an object and a list of references
-- # Class: "Construct_synonym" Description: ""
--     * Slot: Construct_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "Construct_secondary_identifiers" Description: ""
--     * Slot: Construct_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "Construct_genomic_locations" Description: ""
--     * Slot: Construct_curie Description: Autocreated FK slot
--     * Slot: genomic_locations_id Description: 
-- # Class: "SequenceTargetingReagent_reference" Description: ""
--     * Slot: SequenceTargetingReagent_curie Description: Autocreated FK slot
--     * Slot: reference Description: holds between an object and a list of references
-- # Class: "SequenceTargetingReagent_synonym" Description: ""
--     * Slot: SequenceTargetingReagent_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "SequenceTargetingReagent_secondary_identifiers" Description: ""
--     * Slot: SequenceTargetingReagent_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "SequenceTargetingReagent_genomic_locations" Description: ""
--     * Slot: SequenceTargetingReagent_curie Description: Autocreated FK slot
--     * Slot: genomic_locations_id Description: 
-- # Class: "SequenceTargetingReagentToGeneAssociation_reference" Description: ""
--     * Slot: SequenceTargetingReagentToGeneAssociation_id Description: Autocreated FK slot
--     * Slot: reference Description: holds between an object and a list of references
-- # Class: "ConstructComponent_synonym" Description: ""
--     * Slot: ConstructComponent_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "ConstructComponent_secondary_identifiers" Description: ""
--     * Slot: ConstructComponent_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "ConstructComponent_genomic_locations" Description: ""
--     * Slot: ConstructComponent_curie Description: Autocreated FK slot
--     * Slot: genomic_locations_id Description: 
-- # Class: "AffectedGenomicModel_component" Description: ""
--     * Slot: AffectedGenomicModel_curie Description: Autocreated FK slot
--     * Slot: component_id Description: Collection of genomic components that make up a model, i.e. 'allele', each with a zygosity
-- # Class: "AffectedGenomicModel_sequence_targeting_reagent" Description: ""
--     * Slot: AffectedGenomicModel_curie Description: Autocreated FK slot
--     * Slot: sequence_targeting_reagent Description: 
-- # Class: "AffectedGenomicModel_reference" Description: ""
--     * Slot: AffectedGenomicModel_curie Description: Autocreated FK slot
--     * Slot: reference Description: holds between an object and a list of references
-- # Class: "AffectedGenomicModel_synonym" Description: ""
--     * Slot: AffectedGenomicModel_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "AffectedGenomicModel_secondary_identifiers" Description: ""
--     * Slot: AffectedGenomicModel_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "AffectedGenomicModel_genomic_locations" Description: ""
--     * Slot: AffectedGenomicModel_curie Description: Autocreated FK slot
--     * Slot: genomic_locations_id Description: 
-- # Class: "Variant_related_notes" Description: ""
--     * Slot: Variant_curie Description: Autocreated FK slot
--     * Slot: related_notes_id Description: Holds between an object and a list of related Note objects.
-- # Class: "Variant_variant_genome_locations" Description: ""
--     * Slot: Variant_curie Description: Autocreated FK slot
--     * Slot: variant_genome_locations_id Description: Location of the variant in a genomic context.  multiple variant_genome_locations represent multiple assemblies.
-- # Class: "Variant_variant_polypeptide_locations" Description: ""
--     * Slot: Variant_curie Description: Autocreated FK slot
--     * Slot: variant_polypeptide_locations_id Description: Location of the variant within polypeptide entities.
-- # Class: "Variant_variant_transcript_locations" Description: ""
--     * Slot: Variant_curie Description: Autocreated FK slot
--     * Slot: variant_transcript_locations_id Description: Location of the variant within transcript entities.
-- # Class: "Variant_source_variant_locations" Description: ""
--     * Slot: Variant_curie Description: Autocreated FK slot
--     * Slot: source_variant_locations_id Description: Location of the variant within genomic entities,as described in the source references.
-- # Class: "Variant_synonym" Description: ""
--     * Slot: Variant_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "Variant_secondary_identifiers" Description: ""
--     * Slot: Variant_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "Variant_genomic_locations" Description: ""
--     * Slot: Variant_curie Description: Autocreated FK slot
--     * Slot: genomic_locations_id Description: 
-- # Class: "SourceVariantLocation_variant_locations" Description: ""
--     * Slot: SourceVariantLocation_id Description: Autocreated FK slot
--     * Slot: variant_locations_id Description: Location of the variant within genomic entities. Variant_locations can include any or all of: one VariantGenomeLocation stanza, one or more VariantTranscriptLocation stanzas and/or one or more VariantPolypeptideLocation stanzas.
-- # Class: "VariantPolypeptideLocation_associated_transcripts" Description: ""
--     * Slot: VariantPolypeptideLocation_id Description: Autocreated FK slot
--     * Slot: associated_transcripts Description: Transcript(s) associated with polypeptide to which variant is aligned.
-- # Class: "Figure_secondary_identifiers" Description: ""
--     * Slot: Figure_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "Image_secondary_identifiers" Description: ""
--     * Slot: Image_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "Person_emails" Description: ""
--     * Slot: Person_unique_id Description: Autocreated FK slot
--     * Slot: emails Description: list of emails for a person
-- # Class: "Person_old_emails" Description: ""
--     * Slot: Person_unique_id Description: Autocreated FK slot
--     * Slot: old_emails Description: list of old (outdated) emails for a person
-- # Class: "LoggedInPerson_emails" Description: ""
--     * Slot: LoggedInPerson_unique_id Description: Autocreated FK slot
--     * Slot: emails Description: list of emails for a person
-- # Class: "LoggedInPerson_old_emails" Description: ""
--     * Slot: LoggedInPerson_unique_id Description: Autocreated FK slot
--     * Slot: old_emails Description: list of old (outdated) emails for a person
-- # Class: "Resource_synonym" Description: ""
--     * Slot: Resource_curie Description: Autocreated FK slot
--     * Slot: synonym_id Description: holds between a named thing and a synonym
-- # Class: "Resource_authors" Description: ""
--     * Slot: Resource_curie Description: Autocreated FK slot
--     * Slot: authors_id Description: 
-- # Class: "Resource_editor" Description: ""
--     * Slot: Resource_curie Description: Autocreated FK slot
--     * Slot: editor_id Description: holds between a resource and a editor_resource
-- # Class: "DiseaseAnnotation_evidence_codes" Description: ""
--     * Slot: DiseaseAnnotation_id Description: Autocreated FK slot
--     * Slot: evidence_codes Description: ECO term IDs
-- # Class: "DiseaseAnnotation_with" Description: ""
--     * Slot: DiseaseAnnotation_id Description: Autocreated FK slot
--     * Slot: with Description: A field for disease annotations that captures the human gene the implicated MOD gene is homologous or orthologous to when using the ISS (inferred from sequence similarity) evidence code or the ISO (inferred from sequence orthology) evidence code. The assertion would state that the MOD gene is implicated in the indicated disease based on sequence-similarity/sequence-orthology "with" some human gene. Currently used by SGD.
-- # Class: "DiseaseAnnotation_disease_qualifiers" Description: ""
--     * Slot: DiseaseAnnotation_id Description: Autocreated FK slot
--     * Slot: disease_qualifiers Description: Submitted values should be vocabulary terms from the 'Disease Qualifiers' vocabulary
-- # Class: "DiseaseAnnotation_related_notes" Description: ""
--     * Slot: DiseaseAnnotation_id Description: Autocreated FK slot
--     * Slot: related_notes_id Description: Holds between an object and a list of related Note objects.
-- # Class: "GeneDiseaseAnnotation_evidence_codes" Description: ""
--     * Slot: GeneDiseaseAnnotation_id Description: Autocreated FK slot
--     * Slot: evidence_codes Description: ECO term IDs
-- # Class: "GeneDiseaseAnnotation_with" Description: ""
--     * Slot: GeneDiseaseAnnotation_id Description: Autocreated FK slot
--     * Slot: with Description: http://geneontology.org/docs/go-annotation-file-gaf-format-2.2/#with-or-from-column-8
-- # Class: "GeneDiseaseAnnotation_disease_qualifiers" Description: ""
--     * Slot: GeneDiseaseAnnotation_id Description: Autocreated FK slot
--     * Slot: disease_qualifiers Description: Submitted values should be vocabulary terms from the 'Disease Qualifiers' vocabulary
-- # Class: "GeneDiseaseAnnotation_related_notes" Description: ""
--     * Slot: GeneDiseaseAnnotation_id Description: Autocreated FK slot
--     * Slot: related_notes_id Description: Holds between an object and a list of related Note objects.
-- # Class: "AlleleDiseaseAnnotation_evidence_codes" Description: ""
--     * Slot: AlleleDiseaseAnnotation_id Description: Autocreated FK slot
--     * Slot: evidence_codes Description: ECO term IDs
-- # Class: "AlleleDiseaseAnnotation_with" Description: ""
--     * Slot: AlleleDiseaseAnnotation_id Description: Autocreated FK slot
--     * Slot: with Description: http://geneontology.org/docs/go-annotation-file-gaf-format-2.2/#with-or-from-column-8
-- # Class: "AlleleDiseaseAnnotation_disease_qualifiers" Description: ""
--     * Slot: AlleleDiseaseAnnotation_id Description: Autocreated FK slot
--     * Slot: disease_qualifiers Description: Submitted values should be vocabulary terms from the 'Disease Qualifiers' vocabulary
-- # Class: "AlleleDiseaseAnnotation_related_notes" Description: ""
--     * Slot: AlleleDiseaseAnnotation_id Description: Autocreated FK slot
--     * Slot: related_notes_id Description: Holds between an object and a list of related Note objects.
-- # Class: "AGMDiseaseAnnotation_evidence_codes" Description: ""
--     * Slot: AGMDiseaseAnnotation_id Description: Autocreated FK slot
--     * Slot: evidence_codes Description: ECO term IDs
-- # Class: "AGMDiseaseAnnotation_with" Description: ""
--     * Slot: AGMDiseaseAnnotation_id Description: Autocreated FK slot
--     * Slot: with Description: http://geneontology.org/docs/go-annotation-file-gaf-format-2.2/#with-or-from-column-8
-- # Class: "AGMDiseaseAnnotation_disease_qualifiers" Description: ""
--     * Slot: AGMDiseaseAnnotation_id Description: Autocreated FK slot
--     * Slot: disease_qualifiers Description: Submitted values should be vocabulary terms from the 'Disease Qualifiers' vocabulary
-- # Class: "AGMDiseaseAnnotation_related_notes" Description: ""
--     * Slot: AGMDiseaseAnnotation_id Description: Autocreated FK slot
--     * Slot: related_notes_id Description: Holds between an object and a list of related Note objects.
-- # Class: "Reagent_generated_by" Description: ""
--     * Slot: Reagent_curie Description: Autocreated FK slot
--     * Slot: generated_by_id Description: Holds between a material entity and an Agent that generated it: e.g., Thomas Blumenthal, Kornberg Laboratory.
-- # Class: "Reagent_manufactured_by" Description: ""
--     * Slot: Reagent_curie Description: Autocreated FK slot
--     * Slot: manufactured_by_id Description: Holds between a material entity and an Agent that has manufactured it: e.g., Molecular Probes.
-- # Class: "Antibody_antibody_target_genes" Description: ""
--     * Slot: Antibody_curie Description: Autocreated FK slot
--     * Slot: antibody_target_genes Description: The genes whose gene products are recognized by the antibody.
-- # Class: "Antibody_secondary_identifiers" Description: ""
--     * Slot: Antibody_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "Antibody_reference" Description: ""
--     * Slot: Antibody_curie Description: Autocreated FK slot
--     * Slot: reference Description: holds between an object and a list of references
-- # Class: "Antibody_original_reference" Description: ""
--     * Slot: Antibody_curie Description: Autocreated FK slot
--     * Slot: original_reference Description: The reference providing the original description of the antibody's generation.
-- # Class: "Antibody_related_notes" Description: ""
--     * Slot: Antibody_curie Description: Autocreated FK slot
--     * Slot: related_notes_id Description: Holds between an object and a list of related Note objects.
-- # Class: "Antibody_generated_by" Description: ""
--     * Slot: Antibody_curie Description: Autocreated FK slot
--     * Slot: generated_by_id Description: Holds between a material entity and an Agent that generated it: e.g., Thomas Blumenthal, Kornberg Laboratory.
-- # Class: "Antibody_manufactured_by" Description: ""
--     * Slot: Antibody_curie Description: Autocreated FK slot
--     * Slot: manufactured_by_id Description: Holds between a material entity and an Agent that has manufactured it: e.g., Molecular Probes.
-- # Class: "DNAClone_generated_by" Description: ""
--     * Slot: DNAClone_curie Description: Autocreated FK slot
--     * Slot: generated_by_id Description: Holds between a material entity and an Agent that generated it: e.g., Thomas Blumenthal, Kornberg Laboratory.
-- # Class: "DNAClone_manufactured_by" Description: ""
--     * Slot: DNAClone_curie Description: Autocreated FK slot
--     * Slot: manufactured_by_id Description: Holds between a material entity and an Agent that has manufactured it: e.g., Molecular Probes.
-- # Class: "RNAClone_generated_by" Description: ""
--     * Slot: RNAClone_curie Description: Autocreated FK slot
--     * Slot: generated_by_id Description: Holds between a material entity and an Agent that generated it: e.g., Thomas Blumenthal, Kornberg Laboratory.
-- # Class: "RNAClone_manufactured_by" Description: ""
--     * Slot: RNAClone_curie Description: Autocreated FK slot
--     * Slot: manufactured_by_id Description: Holds between a material entity and an Agent that has manufactured it: e.g., Molecular Probes.
-- # Class: "GeneInteraction_interactor_A_role" Description: ""
--     * Slot: GeneInteraction_curie Description: Autocreated FK slot
--     * Slot: interactor_A_role Description: 
-- # Class: "GeneInteraction_interactor_B_role" Description: ""
--     * Slot: GeneInteraction_curie Description: Autocreated FK slot
--     * Slot: interactor_B_role Description: 
-- # Class: "GeneMolecularInteraction_interactor_A_role" Description: ""
--     * Slot: GeneMolecularInteraction_curie Description: Autocreated FK slot
--     * Slot: interactor_A_role Description: 
-- # Class: "GeneMolecularInteraction_interactor_B_role" Description: ""
--     * Slot: GeneMolecularInteraction_curie Description: Autocreated FK slot
--     * Slot: interactor_B_role Description: 
-- # Class: "GeneGeneticInteraction_phenotype_or_trait" Description: ""
--     * Slot: GeneGeneticInteraction_curie Description: Autocreated FK slot
--     * Slot: phenotype_or_trait Description: 
-- # Class: "GeneGeneticInteraction_interactor_A_role" Description: ""
--     * Slot: GeneGeneticInteraction_curie Description: Autocreated FK slot
--     * Slot: interactor_A_role Description: 
-- # Class: "GeneGeneticInteraction_interactor_B_role" Description: ""
--     * Slot: GeneGeneticInteraction_curie Description: Autocreated FK slot
--     * Slot: interactor_B_role Description: 

CREATE TABLE "Person" (
	last_name TEXT, 
	middle_name TEXT, 
	first_name TEXT, 
	orcid TEXT, 
	mod_entity_id TEXT, 
	unique_id TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (unique_id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Ingest" (
	id INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "Reference" (
	abstract TEXT, 
	category VARCHAR(26), 
	citation TEXT, 
	curie TEXT NOT NULL, 
	date_published TEXT, 
	issue_date TEXT, 
	issue_name TEXT, 
	language TEXT, 
	merged_into_id TEXT, 
	open_access BOOLEAN, 
	pages TEXT, 
	plain_language_abstract TEXT, 
	publisher TEXT, 
	pubmed_publication_status VARCHAR(12), 
	reference_id INTEGER NOT NULL, 
	resource_id INTEGER, 
	title TEXT, 
	volume TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "MeshDetail" (
	id INTEGER, 
	mesh_detail_id INTEGER NOT NULL, 
	reference_id INTEGER NOT NULL, 
	heading_term TEXT NOT NULL, 
	qualifier_term TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AuditedObject" (
	id INTEGER, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Synonym" (
	id INTEGER, 
	synonym TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "EntityStatement" (
	id INTEGER, 
	statement_subject TEXT, 
	statement_type TEXT, 
	statement_text TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Association" (
	id INTEGER, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "ExternalDatabaseLink" (
	id INTEGER, 
	dbkey TEXT, 
	prefix TEXT NOT NULL, 
	url_prefix TEXT, 
	url_suffix TEXT, 
	prefix_page TEXT, 
	prefix_order TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Chromosome" (
	curie TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Assembly" (
	curie TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "VocabularyTerm" (
	name TEXT NOT NULL, 
	abbreviation TEXT, 
	definition TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (name), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Vocabulary" (
	name TEXT NOT NULL, 
	vocabulary_description TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (name), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "OntologyTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "DOTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "ECOTerm" (
	abbreviation TEXT, 
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "NCBITaxonTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "FBCVTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "GOTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "ROTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "MITerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "MMOTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "MMUSDVTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "SOTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "XBEDTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "CHEBITerm" (
	inchi TEXT, 
	inchi_key TEXT, 
	iupac TEXT, 
	formula TEXT, 
	smiles TEXT, 
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "StageTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "FBDVTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "WBLSTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "XBSTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "ZFSTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "ExperimentalConditionOntologyTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "ZECOTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "XCOTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AnatomicalTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "CLTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "EMAPATerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "DAOTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "MATerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "UBERONTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "WBBTTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "XBATerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "ZFATerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "PhenotypeTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "XPOTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "ChemicalTerm" (
	inchi TEXT, 
	inchi_key TEXT, 
	iupac TEXT, 
	formula TEXT, 
	smiles TEXT, 
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "XSMOTerm" (
	inchi TEXT, 
	inchi_key TEXT, 
	iupac TEXT, 
	formula TEXT, 
	smiles TEXT, 
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Molecule" (
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	inchi TEXT, 
	inchi_key TEXT, 
	iupac TEXT, 
	formula TEXT, 
	smiles TEXT, 
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "CellLine" (
	id INTEGER, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "File" (
	id INTEGER, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Agent" (
	id INTEGER, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Organization" (
	id INTEGER, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Laboratory" (
	id INTEGER, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Company" (
	id INTEGER, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "LoggedInPerson" (
	okta_id TEXT NOT NULL, 
	okta_email TEXT NOT NULL, 
	last_name TEXT, 
	middle_name TEXT, 
	first_name TEXT, 
	orcid TEXT, 
	mod_entity_id TEXT, 
	unique_id TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (unique_id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Resource" (
	curie TEXT NOT NULL, 
	title TEXT, 
	iso_abbreviation TEXT, 
	medline_abbreviation TEXT, 
	copyright_date DATE, 
	print_issn TEXT, 
	online_issn TEXT, 
	publisher TEXT, 
	volume TEXT, 
	summary TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "VariantConsequence" (
	id INTEGER, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	vep_consequence VARCHAR(8), 
	vep_impact TEXT, 
	polyphen_score FLOAT, 
	polyphen_prediction VARCHAR(17), 
	sift_score FLOAT, 
	sift_prediction VARCHAR(11), 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Person_emails" (
	"Person_unique_id" TEXT, 
	emails TEXT, 
	PRIMARY KEY ("Person_unique_id", emails), 
	FOREIGN KEY("Person_unique_id") REFERENCES "Person" (unique_id)
);
CREATE TABLE "Person_old_emails" (
	"Person_unique_id" TEXT, 
	old_emails TEXT, 
	PRIMARY KEY ("Person_unique_id", old_emails), 
	FOREIGN KEY("Person_unique_id") REFERENCES "Person" (unique_id)
);
CREATE TABLE "TemporalContext" (
	id INTEGER, 
	developmental_stage_start TEXT, 
	developmental_stage_stop TEXT, 
	age TEXT, 
	temporal_qualifiers VARCHAR(15), 
	stage_uncertainty TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(developmental_stage_start) REFERENCES "StageTerm" (curie), 
	FOREIGN KEY(developmental_stage_stop) REFERENCES "StageTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AnatomicalSite" (
	id INTEGER, 
	anatomical_structure TEXT, 
	anatomical_substructure TEXT, 
	cellular_component TEXT, 
	spatial_qualifiers VARCHAR(35), 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(anatomical_structure) REFERENCES "AnatomicalTerm" (curie), 
	FOREIGN KEY(anatomical_substructure) REFERENCES "AnatomicalTerm" (curie), 
	FOREIGN KEY(cellular_component) REFERENCES "GOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AuthorReference" (
	id INTEGER, 
	corresponding_author TEXT, 
	first_name TEXT, 
	middle_name TEXT, 
	last_name TEXT, 
	initials TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(corresponding_author) REFERENCES "Reference" (curie), 
	FOREIGN KEY(initials) REFERENCES "Reference" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "BiologicalEntity" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "GenomicEntity" (
	name TEXT, 
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Transcript" (
	name TEXT, 
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Gene" (
	symbol TEXT NOT NULL, 
	gene_synopsis TEXT, 
	"gene_synopsis_URL" TEXT, 
	gene_type TEXT, 
	automated_gene_description TEXT, 
	name TEXT, 
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(gene_type) REFERENCES "SOTerm" (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id)
);
CREATE TABLE "Note" (
	id INTEGER, 
	free_text TEXT NOT NULL, 
	note_type TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(note_type) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "EntitySynonym" (
	id INTEGER, 
	subject TEXT NOT NULL, 
	predicate VARCHAR(7) NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	object_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(object_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "Protein" (
	name TEXT, 
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AssociatedReference" (
	id INTEGER, 
	reference_type TEXT NOT NULL, 
	single_reference TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(reference_type) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Construct" (
	name TEXT NOT NULL, 
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "SequenceTargetingReagent" (
	name TEXT NOT NULL, 
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id)
);
CREATE TABLE "ConstructComponent" (
	symbol TEXT, 
	name TEXT, 
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AffectedGenomicModel" (
	subtype VARCHAR(8) NOT NULL, 
	parental_populations TEXT, 
	data_provider TEXT, 
	name TEXT, 
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id)
);
CREATE TABLE "Variant" (
	variant_type TEXT NOT NULL, 
	source_general_consequence TEXT, 
	variant_status VARCHAR(7), 
	name TEXT, 
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(variant_type) REFERENCES "SOTerm" (curie), 
	FOREIGN KEY(source_general_consequence) REFERENCES "SOTerm" (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id)
);
CREATE TABLE "SourceVariantLocation" (
	id INTEGER, 
	single_reference TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "VariantLocation" (
	id INTEGER, 
	evidence_code TEXT, 
	single_reference TEXT, 
	start_position INTEGER, 
	end_position INTEGER, 
	reference_sequence TEXT, 
	variant_sequence TEXT, 
	consequence TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(evidence_code) REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(consequence) REFERENCES "SOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "VariantGenomeLocation" (
	id INTEGER, 
	assembly TEXT, 
	chromosome TEXT, 
	evidence_code TEXT, 
	single_reference TEXT, 
	start_position INTEGER, 
	end_position INTEGER, 
	reference_sequence TEXT, 
	variant_sequence TEXT, 
	consequence TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(assembly) REFERENCES "Assembly" (curie), 
	FOREIGN KEY(chromosome) REFERENCES "Chromosome" (curie), 
	FOREIGN KEY(evidence_code) REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(consequence) REFERENCES "SOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Figure" (
	curie TEXT NOT NULL, 
	single_reference TEXT NOT NULL, 
	label TEXT, 
	caption TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Reagent" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Antibody" (
	name TEXT NOT NULL, 
	antigen_taxon TEXT, 
	clonality VARCHAR(11) NOT NULL, 
	heavy_chain_isotype VARCHAR(5), 
	light_chain_isotype VARCHAR(2), 
	curie TEXT NOT NULL, 
	taxon TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(antigen_taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "DNAClone" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "RNAClone" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Reference_date_arrived_in_pubmed" (
	"Reference_curie" TEXT, 
	date_arrived_in_pubmed TEXT, 
	PRIMARY KEY ("Reference_curie", date_arrived_in_pubmed), 
	FOREIGN KEY("Reference_curie") REFERENCES "Reference" (curie)
);
CREATE TABLE "Reference_keywords" (
	"Reference_curie" TEXT, 
	keywords TEXT, 
	PRIMARY KEY ("Reference_curie", keywords), 
	FOREIGN KEY("Reference_curie") REFERENCES "Reference" (curie)
);
CREATE TABLE "Reference_pubmed_abstract_languages" (
	"Reference_curie" TEXT, 
	pubmed_abstract_languages TEXT, 
	PRIMARY KEY ("Reference_curie", pubmed_abstract_languages), 
	FOREIGN KEY("Reference_curie") REFERENCES "Reference" (curie)
);
CREATE TABLE "Reference_pubmed_type" (
	"Reference_curie" TEXT, 
	pubmed_type VARCHAR(56), 
	PRIMARY KEY ("Reference_curie", pubmed_type), 
	FOREIGN KEY("Reference_curie") REFERENCES "Reference" (curie)
);
CREATE TABLE "EntityStatement_reference" (
	"EntityStatement_id" TEXT, 
	reference TEXT, 
	PRIMARY KEY ("EntityStatement_id", reference), 
	FOREIGN KEY("EntityStatement_id") REFERENCES "EntityStatement" (id), 
	FOREIGN KEY(reference) REFERENCES "Reference" (curie)
);
CREATE TABLE "VocabularyTerm_text_synonyms" (
	"VocabularyTerm_name" TEXT, 
	text_synonyms TEXT, 
	PRIMARY KEY ("VocabularyTerm_name", text_synonyms), 
	FOREIGN KEY("VocabularyTerm_name") REFERENCES "VocabularyTerm" (name)
);
CREATE TABLE "Vocabulary_member_terms" (
	"Vocabulary_name" TEXT, 
	member_terms TEXT, 
	PRIMARY KEY ("Vocabulary_name", member_terms), 
	FOREIGN KEY("Vocabulary_name") REFERENCES "Vocabulary" (name), 
	FOREIGN KEY(member_terms) REFERENCES "VocabularyTerm" (name)
);
CREATE TABLE "OntologyTerm_definition_urls" (
	"OntologyTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("OntologyTerm_curie", definition_urls), 
	FOREIGN KEY("OntologyTerm_curie") REFERENCES "OntologyTerm" (curie)
);
CREATE TABLE "OntologyTerm_synonym" (
	"OntologyTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("OntologyTerm_curie", synonym_id), 
	FOREIGN KEY("OntologyTerm_curie") REFERENCES "OntologyTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "OntologyTerm_subsets" (
	"OntologyTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("OntologyTerm_curie", subsets), 
	FOREIGN KEY("OntologyTerm_curie") REFERENCES "OntologyTerm" (curie)
);
CREATE TABLE "OntologyTerm_secondary_identifiers" (
	"OntologyTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("OntologyTerm_curie", secondary_identifiers), 
	FOREIGN KEY("OntologyTerm_curie") REFERENCES "OntologyTerm" (curie)
);
CREATE TABLE "DOTerm_definition_urls" (
	"DOTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("DOTerm_curie", definition_urls), 
	FOREIGN KEY("DOTerm_curie") REFERENCES "DOTerm" (curie)
);
CREATE TABLE "DOTerm_synonym" (
	"DOTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("DOTerm_curie", synonym_id), 
	FOREIGN KEY("DOTerm_curie") REFERENCES "DOTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "DOTerm_subsets" (
	"DOTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("DOTerm_curie", subsets), 
	FOREIGN KEY("DOTerm_curie") REFERENCES "DOTerm" (curie)
);
CREATE TABLE "DOTerm_secondary_identifiers" (
	"DOTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("DOTerm_curie", secondary_identifiers), 
	FOREIGN KEY("DOTerm_curie") REFERENCES "DOTerm" (curie)
);
CREATE TABLE "ECOTerm_definition_urls" (
	"ECOTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("ECOTerm_curie", definition_urls), 
	FOREIGN KEY("ECOTerm_curie") REFERENCES "ECOTerm" (curie)
);
CREATE TABLE "ECOTerm_synonym" (
	"ECOTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("ECOTerm_curie", synonym_id), 
	FOREIGN KEY("ECOTerm_curie") REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "ECOTerm_subsets" (
	"ECOTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("ECOTerm_curie", subsets), 
	FOREIGN KEY("ECOTerm_curie") REFERENCES "ECOTerm" (curie)
);
CREATE TABLE "ECOTerm_secondary_identifiers" (
	"ECOTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("ECOTerm_curie", secondary_identifiers), 
	FOREIGN KEY("ECOTerm_curie") REFERENCES "ECOTerm" (curie)
);
CREATE TABLE "NCBITaxonTerm_definition_urls" (
	"NCBITaxonTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("NCBITaxonTerm_curie", definition_urls), 
	FOREIGN KEY("NCBITaxonTerm_curie") REFERENCES "NCBITaxonTerm" (curie)
);
CREATE TABLE "NCBITaxonTerm_synonym" (
	"NCBITaxonTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("NCBITaxonTerm_curie", synonym_id), 
	FOREIGN KEY("NCBITaxonTerm_curie") REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "NCBITaxonTerm_subsets" (
	"NCBITaxonTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("NCBITaxonTerm_curie", subsets), 
	FOREIGN KEY("NCBITaxonTerm_curie") REFERENCES "NCBITaxonTerm" (curie)
);
CREATE TABLE "NCBITaxonTerm_secondary_identifiers" (
	"NCBITaxonTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("NCBITaxonTerm_curie", secondary_identifiers), 
	FOREIGN KEY("NCBITaxonTerm_curie") REFERENCES "NCBITaxonTerm" (curie)
);
CREATE TABLE "FBCVTerm_definition_urls" (
	"FBCVTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("FBCVTerm_curie", definition_urls), 
	FOREIGN KEY("FBCVTerm_curie") REFERENCES "FBCVTerm" (curie)
);
CREATE TABLE "FBCVTerm_synonym" (
	"FBCVTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("FBCVTerm_curie", synonym_id), 
	FOREIGN KEY("FBCVTerm_curie") REFERENCES "FBCVTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "FBCVTerm_subsets" (
	"FBCVTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("FBCVTerm_curie", subsets), 
	FOREIGN KEY("FBCVTerm_curie") REFERENCES "FBCVTerm" (curie)
);
CREATE TABLE "FBCVTerm_secondary_identifiers" (
	"FBCVTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("FBCVTerm_curie", secondary_identifiers), 
	FOREIGN KEY("FBCVTerm_curie") REFERENCES "FBCVTerm" (curie)
);
CREATE TABLE "GOTerm_definition_urls" (
	"GOTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("GOTerm_curie", definition_urls), 
	FOREIGN KEY("GOTerm_curie") REFERENCES "GOTerm" (curie)
);
CREATE TABLE "GOTerm_synonym" (
	"GOTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("GOTerm_curie", synonym_id), 
	FOREIGN KEY("GOTerm_curie") REFERENCES "GOTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "GOTerm_subsets" (
	"GOTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("GOTerm_curie", subsets), 
	FOREIGN KEY("GOTerm_curie") REFERENCES "GOTerm" (curie)
);
CREATE TABLE "GOTerm_secondary_identifiers" (
	"GOTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("GOTerm_curie", secondary_identifiers), 
	FOREIGN KEY("GOTerm_curie") REFERENCES "GOTerm" (curie)
);
CREATE TABLE "ROTerm_definition_urls" (
	"ROTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("ROTerm_curie", definition_urls), 
	FOREIGN KEY("ROTerm_curie") REFERENCES "ROTerm" (curie)
);
CREATE TABLE "ROTerm_synonym" (
	"ROTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("ROTerm_curie", synonym_id), 
	FOREIGN KEY("ROTerm_curie") REFERENCES "ROTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "ROTerm_subsets" (
	"ROTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("ROTerm_curie", subsets), 
	FOREIGN KEY("ROTerm_curie") REFERENCES "ROTerm" (curie)
);
CREATE TABLE "ROTerm_secondary_identifiers" (
	"ROTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("ROTerm_curie", secondary_identifiers), 
	FOREIGN KEY("ROTerm_curie") REFERENCES "ROTerm" (curie)
);
CREATE TABLE "MITerm_definition_urls" (
	"MITerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("MITerm_curie", definition_urls), 
	FOREIGN KEY("MITerm_curie") REFERENCES "MITerm" (curie)
);
CREATE TABLE "MITerm_synonym" (
	"MITerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("MITerm_curie", synonym_id), 
	FOREIGN KEY("MITerm_curie") REFERENCES "MITerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "MITerm_subsets" (
	"MITerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("MITerm_curie", subsets), 
	FOREIGN KEY("MITerm_curie") REFERENCES "MITerm" (curie)
);
CREATE TABLE "MITerm_secondary_identifiers" (
	"MITerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("MITerm_curie", secondary_identifiers), 
	FOREIGN KEY("MITerm_curie") REFERENCES "MITerm" (curie)
);
CREATE TABLE "MMOTerm_definition_urls" (
	"MMOTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("MMOTerm_curie", definition_urls), 
	FOREIGN KEY("MMOTerm_curie") REFERENCES "MMOTerm" (curie)
);
CREATE TABLE "MMOTerm_synonym" (
	"MMOTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("MMOTerm_curie", synonym_id), 
	FOREIGN KEY("MMOTerm_curie") REFERENCES "MMOTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "MMOTerm_subsets" (
	"MMOTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("MMOTerm_curie", subsets), 
	FOREIGN KEY("MMOTerm_curie") REFERENCES "MMOTerm" (curie)
);
CREATE TABLE "MMOTerm_secondary_identifiers" (
	"MMOTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("MMOTerm_curie", secondary_identifiers), 
	FOREIGN KEY("MMOTerm_curie") REFERENCES "MMOTerm" (curie)
);
CREATE TABLE "MMUSDVTerm_definition_urls" (
	"MMUSDVTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("MMUSDVTerm_curie", definition_urls), 
	FOREIGN KEY("MMUSDVTerm_curie") REFERENCES "MMUSDVTerm" (curie)
);
CREATE TABLE "MMUSDVTerm_synonym" (
	"MMUSDVTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("MMUSDVTerm_curie", synonym_id), 
	FOREIGN KEY("MMUSDVTerm_curie") REFERENCES "MMUSDVTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "MMUSDVTerm_subsets" (
	"MMUSDVTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("MMUSDVTerm_curie", subsets), 
	FOREIGN KEY("MMUSDVTerm_curie") REFERENCES "MMUSDVTerm" (curie)
);
CREATE TABLE "MMUSDVTerm_secondary_identifiers" (
	"MMUSDVTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("MMUSDVTerm_curie", secondary_identifiers), 
	FOREIGN KEY("MMUSDVTerm_curie") REFERENCES "MMUSDVTerm" (curie)
);
CREATE TABLE "SOTerm_definition_urls" (
	"SOTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("SOTerm_curie", definition_urls), 
	FOREIGN KEY("SOTerm_curie") REFERENCES "SOTerm" (curie)
);
CREATE TABLE "SOTerm_synonym" (
	"SOTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("SOTerm_curie", synonym_id), 
	FOREIGN KEY("SOTerm_curie") REFERENCES "SOTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "SOTerm_subsets" (
	"SOTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("SOTerm_curie", subsets), 
	FOREIGN KEY("SOTerm_curie") REFERENCES "SOTerm" (curie)
);
CREATE TABLE "SOTerm_secondary_identifiers" (
	"SOTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("SOTerm_curie", secondary_identifiers), 
	FOREIGN KEY("SOTerm_curie") REFERENCES "SOTerm" (curie)
);
CREATE TABLE "XBEDTerm_definition_urls" (
	"XBEDTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("XBEDTerm_curie", definition_urls), 
	FOREIGN KEY("XBEDTerm_curie") REFERENCES "XBEDTerm" (curie)
);
CREATE TABLE "XBEDTerm_synonym" (
	"XBEDTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("XBEDTerm_curie", synonym_id), 
	FOREIGN KEY("XBEDTerm_curie") REFERENCES "XBEDTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "XBEDTerm_subsets" (
	"XBEDTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("XBEDTerm_curie", subsets), 
	FOREIGN KEY("XBEDTerm_curie") REFERENCES "XBEDTerm" (curie)
);
CREATE TABLE "XBEDTerm_secondary_identifiers" (
	"XBEDTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("XBEDTerm_curie", secondary_identifiers), 
	FOREIGN KEY("XBEDTerm_curie") REFERENCES "XBEDTerm" (curie)
);
CREATE TABLE "CHEBITerm_definition_urls" (
	"CHEBITerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("CHEBITerm_curie", definition_urls), 
	FOREIGN KEY("CHEBITerm_curie") REFERENCES "CHEBITerm" (curie)
);
CREATE TABLE "CHEBITerm_synonym" (
	"CHEBITerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("CHEBITerm_curie", synonym_id), 
	FOREIGN KEY("CHEBITerm_curie") REFERENCES "CHEBITerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "CHEBITerm_subsets" (
	"CHEBITerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("CHEBITerm_curie", subsets), 
	FOREIGN KEY("CHEBITerm_curie") REFERENCES "CHEBITerm" (curie)
);
CREATE TABLE "CHEBITerm_secondary_identifiers" (
	"CHEBITerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("CHEBITerm_curie", secondary_identifiers), 
	FOREIGN KEY("CHEBITerm_curie") REFERENCES "CHEBITerm" (curie)
);
CREATE TABLE "StageTerm_definition_urls" (
	"StageTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("StageTerm_curie", definition_urls), 
	FOREIGN KEY("StageTerm_curie") REFERENCES "StageTerm" (curie)
);
CREATE TABLE "StageTerm_synonym" (
	"StageTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("StageTerm_curie", synonym_id), 
	FOREIGN KEY("StageTerm_curie") REFERENCES "StageTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "StageTerm_subsets" (
	"StageTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("StageTerm_curie", subsets), 
	FOREIGN KEY("StageTerm_curie") REFERENCES "StageTerm" (curie)
);
CREATE TABLE "StageTerm_secondary_identifiers" (
	"StageTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("StageTerm_curie", secondary_identifiers), 
	FOREIGN KEY("StageTerm_curie") REFERENCES "StageTerm" (curie)
);
CREATE TABLE "FBDVTerm_definition_urls" (
	"FBDVTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("FBDVTerm_curie", definition_urls), 
	FOREIGN KEY("FBDVTerm_curie") REFERENCES "FBDVTerm" (curie)
);
CREATE TABLE "FBDVTerm_synonym" (
	"FBDVTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("FBDVTerm_curie", synonym_id), 
	FOREIGN KEY("FBDVTerm_curie") REFERENCES "FBDVTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "FBDVTerm_subsets" (
	"FBDVTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("FBDVTerm_curie", subsets), 
	FOREIGN KEY("FBDVTerm_curie") REFERENCES "FBDVTerm" (curie)
);
CREATE TABLE "FBDVTerm_secondary_identifiers" (
	"FBDVTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("FBDVTerm_curie", secondary_identifiers), 
	FOREIGN KEY("FBDVTerm_curie") REFERENCES "FBDVTerm" (curie)
);
CREATE TABLE "WBLSTerm_definition_urls" (
	"WBLSTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("WBLSTerm_curie", definition_urls), 
	FOREIGN KEY("WBLSTerm_curie") REFERENCES "WBLSTerm" (curie)
);
CREATE TABLE "WBLSTerm_synonym" (
	"WBLSTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("WBLSTerm_curie", synonym_id), 
	FOREIGN KEY("WBLSTerm_curie") REFERENCES "WBLSTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "WBLSTerm_subsets" (
	"WBLSTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("WBLSTerm_curie", subsets), 
	FOREIGN KEY("WBLSTerm_curie") REFERENCES "WBLSTerm" (curie)
);
CREATE TABLE "WBLSTerm_secondary_identifiers" (
	"WBLSTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("WBLSTerm_curie", secondary_identifiers), 
	FOREIGN KEY("WBLSTerm_curie") REFERENCES "WBLSTerm" (curie)
);
CREATE TABLE "XBSTerm_definition_urls" (
	"XBSTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("XBSTerm_curie", definition_urls), 
	FOREIGN KEY("XBSTerm_curie") REFERENCES "XBSTerm" (curie)
);
CREATE TABLE "XBSTerm_synonym" (
	"XBSTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("XBSTerm_curie", synonym_id), 
	FOREIGN KEY("XBSTerm_curie") REFERENCES "XBSTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "XBSTerm_subsets" (
	"XBSTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("XBSTerm_curie", subsets), 
	FOREIGN KEY("XBSTerm_curie") REFERENCES "XBSTerm" (curie)
);
CREATE TABLE "XBSTerm_secondary_identifiers" (
	"XBSTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("XBSTerm_curie", secondary_identifiers), 
	FOREIGN KEY("XBSTerm_curie") REFERENCES "XBSTerm" (curie)
);
CREATE TABLE "ZFSTerm_definition_urls" (
	"ZFSTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("ZFSTerm_curie", definition_urls), 
	FOREIGN KEY("ZFSTerm_curie") REFERENCES "ZFSTerm" (curie)
);
CREATE TABLE "ZFSTerm_synonym" (
	"ZFSTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("ZFSTerm_curie", synonym_id), 
	FOREIGN KEY("ZFSTerm_curie") REFERENCES "ZFSTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "ZFSTerm_subsets" (
	"ZFSTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("ZFSTerm_curie", subsets), 
	FOREIGN KEY("ZFSTerm_curie") REFERENCES "ZFSTerm" (curie)
);
CREATE TABLE "ZFSTerm_secondary_identifiers" (
	"ZFSTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("ZFSTerm_curie", secondary_identifiers), 
	FOREIGN KEY("ZFSTerm_curie") REFERENCES "ZFSTerm" (curie)
);
CREATE TABLE "ExperimentalConditionOntologyTerm_definition_urls" (
	"ExperimentalConditionOntologyTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("ExperimentalConditionOntologyTerm_curie", definition_urls), 
	FOREIGN KEY("ExperimentalConditionOntologyTerm_curie") REFERENCES "ExperimentalConditionOntologyTerm" (curie)
);
CREATE TABLE "ExperimentalConditionOntologyTerm_synonym" (
	"ExperimentalConditionOntologyTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("ExperimentalConditionOntologyTerm_curie", synonym_id), 
	FOREIGN KEY("ExperimentalConditionOntologyTerm_curie") REFERENCES "ExperimentalConditionOntologyTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "ExperimentalConditionOntologyTerm_subsets" (
	"ExperimentalConditionOntologyTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("ExperimentalConditionOntologyTerm_curie", subsets), 
	FOREIGN KEY("ExperimentalConditionOntologyTerm_curie") REFERENCES "ExperimentalConditionOntologyTerm" (curie)
);
CREATE TABLE "ExperimentalConditionOntologyTerm_secondary_identifiers" (
	"ExperimentalConditionOntologyTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("ExperimentalConditionOntologyTerm_curie", secondary_identifiers), 
	FOREIGN KEY("ExperimentalConditionOntologyTerm_curie") REFERENCES "ExperimentalConditionOntologyTerm" (curie)
);
CREATE TABLE "ZECOTerm_definition_urls" (
	"ZECOTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("ZECOTerm_curie", definition_urls), 
	FOREIGN KEY("ZECOTerm_curie") REFERENCES "ZECOTerm" (curie)
);
CREATE TABLE "ZECOTerm_synonym" (
	"ZECOTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("ZECOTerm_curie", synonym_id), 
	FOREIGN KEY("ZECOTerm_curie") REFERENCES "ZECOTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "ZECOTerm_subsets" (
	"ZECOTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("ZECOTerm_curie", subsets), 
	FOREIGN KEY("ZECOTerm_curie") REFERENCES "ZECOTerm" (curie)
);
CREATE TABLE "ZECOTerm_secondary_identifiers" (
	"ZECOTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("ZECOTerm_curie", secondary_identifiers), 
	FOREIGN KEY("ZECOTerm_curie") REFERENCES "ZECOTerm" (curie)
);
CREATE TABLE "XCOTerm_definition_urls" (
	"XCOTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("XCOTerm_curie", definition_urls), 
	FOREIGN KEY("XCOTerm_curie") REFERENCES "XCOTerm" (curie)
);
CREATE TABLE "XCOTerm_synonym" (
	"XCOTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("XCOTerm_curie", synonym_id), 
	FOREIGN KEY("XCOTerm_curie") REFERENCES "XCOTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "XCOTerm_subsets" (
	"XCOTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("XCOTerm_curie", subsets), 
	FOREIGN KEY("XCOTerm_curie") REFERENCES "XCOTerm" (curie)
);
CREATE TABLE "XCOTerm_secondary_identifiers" (
	"XCOTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("XCOTerm_curie", secondary_identifiers), 
	FOREIGN KEY("XCOTerm_curie") REFERENCES "XCOTerm" (curie)
);
CREATE TABLE "AnatomicalTerm_definition_urls" (
	"AnatomicalTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("AnatomicalTerm_curie", definition_urls), 
	FOREIGN KEY("AnatomicalTerm_curie") REFERENCES "AnatomicalTerm" (curie)
);
CREATE TABLE "AnatomicalTerm_synonym" (
	"AnatomicalTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("AnatomicalTerm_curie", synonym_id), 
	FOREIGN KEY("AnatomicalTerm_curie") REFERENCES "AnatomicalTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "AnatomicalTerm_subsets" (
	"AnatomicalTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("AnatomicalTerm_curie", subsets), 
	FOREIGN KEY("AnatomicalTerm_curie") REFERENCES "AnatomicalTerm" (curie)
);
CREATE TABLE "AnatomicalTerm_secondary_identifiers" (
	"AnatomicalTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("AnatomicalTerm_curie", secondary_identifiers), 
	FOREIGN KEY("AnatomicalTerm_curie") REFERENCES "AnatomicalTerm" (curie)
);
CREATE TABLE "CLTerm_definition_urls" (
	"CLTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("CLTerm_curie", definition_urls), 
	FOREIGN KEY("CLTerm_curie") REFERENCES "CLTerm" (curie)
);
CREATE TABLE "CLTerm_synonym" (
	"CLTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("CLTerm_curie", synonym_id), 
	FOREIGN KEY("CLTerm_curie") REFERENCES "CLTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "CLTerm_subsets" (
	"CLTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("CLTerm_curie", subsets), 
	FOREIGN KEY("CLTerm_curie") REFERENCES "CLTerm" (curie)
);
CREATE TABLE "CLTerm_secondary_identifiers" (
	"CLTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("CLTerm_curie", secondary_identifiers), 
	FOREIGN KEY("CLTerm_curie") REFERENCES "CLTerm" (curie)
);
CREATE TABLE "EMAPATerm_definition_urls" (
	"EMAPATerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("EMAPATerm_curie", definition_urls), 
	FOREIGN KEY("EMAPATerm_curie") REFERENCES "EMAPATerm" (curie)
);
CREATE TABLE "EMAPATerm_synonym" (
	"EMAPATerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("EMAPATerm_curie", synonym_id), 
	FOREIGN KEY("EMAPATerm_curie") REFERENCES "EMAPATerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "EMAPATerm_subsets" (
	"EMAPATerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("EMAPATerm_curie", subsets), 
	FOREIGN KEY("EMAPATerm_curie") REFERENCES "EMAPATerm" (curie)
);
CREATE TABLE "EMAPATerm_secondary_identifiers" (
	"EMAPATerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("EMAPATerm_curie", secondary_identifiers), 
	FOREIGN KEY("EMAPATerm_curie") REFERENCES "EMAPATerm" (curie)
);
CREATE TABLE "DAOTerm_definition_urls" (
	"DAOTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("DAOTerm_curie", definition_urls), 
	FOREIGN KEY("DAOTerm_curie") REFERENCES "DAOTerm" (curie)
);
CREATE TABLE "DAOTerm_synonym" (
	"DAOTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("DAOTerm_curie", synonym_id), 
	FOREIGN KEY("DAOTerm_curie") REFERENCES "DAOTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "DAOTerm_subsets" (
	"DAOTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("DAOTerm_curie", subsets), 
	FOREIGN KEY("DAOTerm_curie") REFERENCES "DAOTerm" (curie)
);
CREATE TABLE "DAOTerm_secondary_identifiers" (
	"DAOTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("DAOTerm_curie", secondary_identifiers), 
	FOREIGN KEY("DAOTerm_curie") REFERENCES "DAOTerm" (curie)
);
CREATE TABLE "MATerm_definition_urls" (
	"MATerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("MATerm_curie", definition_urls), 
	FOREIGN KEY("MATerm_curie") REFERENCES "MATerm" (curie)
);
CREATE TABLE "MATerm_synonym" (
	"MATerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("MATerm_curie", synonym_id), 
	FOREIGN KEY("MATerm_curie") REFERENCES "MATerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "MATerm_subsets" (
	"MATerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("MATerm_curie", subsets), 
	FOREIGN KEY("MATerm_curie") REFERENCES "MATerm" (curie)
);
CREATE TABLE "MATerm_secondary_identifiers" (
	"MATerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("MATerm_curie", secondary_identifiers), 
	FOREIGN KEY("MATerm_curie") REFERENCES "MATerm" (curie)
);
CREATE TABLE "UBERONTerm_definition_urls" (
	"UBERONTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("UBERONTerm_curie", definition_urls), 
	FOREIGN KEY("UBERONTerm_curie") REFERENCES "UBERONTerm" (curie)
);
CREATE TABLE "UBERONTerm_synonym" (
	"UBERONTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("UBERONTerm_curie", synonym_id), 
	FOREIGN KEY("UBERONTerm_curie") REFERENCES "UBERONTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "UBERONTerm_subsets" (
	"UBERONTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("UBERONTerm_curie", subsets), 
	FOREIGN KEY("UBERONTerm_curie") REFERENCES "UBERONTerm" (curie)
);
CREATE TABLE "UBERONTerm_secondary_identifiers" (
	"UBERONTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("UBERONTerm_curie", secondary_identifiers), 
	FOREIGN KEY("UBERONTerm_curie") REFERENCES "UBERONTerm" (curie)
);
CREATE TABLE "WBBTTerm_definition_urls" (
	"WBBTTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("WBBTTerm_curie", definition_urls), 
	FOREIGN KEY("WBBTTerm_curie") REFERENCES "WBBTTerm" (curie)
);
CREATE TABLE "WBBTTerm_synonym" (
	"WBBTTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("WBBTTerm_curie", synonym_id), 
	FOREIGN KEY("WBBTTerm_curie") REFERENCES "WBBTTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "WBBTTerm_subsets" (
	"WBBTTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("WBBTTerm_curie", subsets), 
	FOREIGN KEY("WBBTTerm_curie") REFERENCES "WBBTTerm" (curie)
);
CREATE TABLE "WBBTTerm_secondary_identifiers" (
	"WBBTTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("WBBTTerm_curie", secondary_identifiers), 
	FOREIGN KEY("WBBTTerm_curie") REFERENCES "WBBTTerm" (curie)
);
CREATE TABLE "XBATerm_definition_urls" (
	"XBATerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("XBATerm_curie", definition_urls), 
	FOREIGN KEY("XBATerm_curie") REFERENCES "XBATerm" (curie)
);
CREATE TABLE "XBATerm_synonym" (
	"XBATerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("XBATerm_curie", synonym_id), 
	FOREIGN KEY("XBATerm_curie") REFERENCES "XBATerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "XBATerm_subsets" (
	"XBATerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("XBATerm_curie", subsets), 
	FOREIGN KEY("XBATerm_curie") REFERENCES "XBATerm" (curie)
);
CREATE TABLE "XBATerm_secondary_identifiers" (
	"XBATerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("XBATerm_curie", secondary_identifiers), 
	FOREIGN KEY("XBATerm_curie") REFERENCES "XBATerm" (curie)
);
CREATE TABLE "ZFATerm_definition_urls" (
	"ZFATerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("ZFATerm_curie", definition_urls), 
	FOREIGN KEY("ZFATerm_curie") REFERENCES "ZFATerm" (curie)
);
CREATE TABLE "ZFATerm_synonym" (
	"ZFATerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("ZFATerm_curie", synonym_id), 
	FOREIGN KEY("ZFATerm_curie") REFERENCES "ZFATerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "ZFATerm_subsets" (
	"ZFATerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("ZFATerm_curie", subsets), 
	FOREIGN KEY("ZFATerm_curie") REFERENCES "ZFATerm" (curie)
);
CREATE TABLE "ZFATerm_secondary_identifiers" (
	"ZFATerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("ZFATerm_curie", secondary_identifiers), 
	FOREIGN KEY("ZFATerm_curie") REFERENCES "ZFATerm" (curie)
);
CREATE TABLE "PhenotypeTerm_definition_urls" (
	"PhenotypeTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("PhenotypeTerm_curie", definition_urls), 
	FOREIGN KEY("PhenotypeTerm_curie") REFERENCES "PhenotypeTerm" (curie)
);
CREATE TABLE "PhenotypeTerm_synonym" (
	"PhenotypeTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("PhenotypeTerm_curie", synonym_id), 
	FOREIGN KEY("PhenotypeTerm_curie") REFERENCES "PhenotypeTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "PhenotypeTerm_subsets" (
	"PhenotypeTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("PhenotypeTerm_curie", subsets), 
	FOREIGN KEY("PhenotypeTerm_curie") REFERENCES "PhenotypeTerm" (curie)
);
CREATE TABLE "PhenotypeTerm_secondary_identifiers" (
	"PhenotypeTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("PhenotypeTerm_curie", secondary_identifiers), 
	FOREIGN KEY("PhenotypeTerm_curie") REFERENCES "PhenotypeTerm" (curie)
);
CREATE TABLE "XPOTerm_definition_urls" (
	"XPOTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("XPOTerm_curie", definition_urls), 
	FOREIGN KEY("XPOTerm_curie") REFERENCES "XPOTerm" (curie)
);
CREATE TABLE "XPOTerm_synonym" (
	"XPOTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("XPOTerm_curie", synonym_id), 
	FOREIGN KEY("XPOTerm_curie") REFERENCES "XPOTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "XPOTerm_subsets" (
	"XPOTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("XPOTerm_curie", subsets), 
	FOREIGN KEY("XPOTerm_curie") REFERENCES "XPOTerm" (curie)
);
CREATE TABLE "XPOTerm_secondary_identifiers" (
	"XPOTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("XPOTerm_curie", secondary_identifiers), 
	FOREIGN KEY("XPOTerm_curie") REFERENCES "XPOTerm" (curie)
);
CREATE TABLE "ChemicalTerm_definition_urls" (
	"ChemicalTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("ChemicalTerm_curie", definition_urls), 
	FOREIGN KEY("ChemicalTerm_curie") REFERENCES "ChemicalTerm" (curie)
);
CREATE TABLE "ChemicalTerm_synonym" (
	"ChemicalTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("ChemicalTerm_curie", synonym_id), 
	FOREIGN KEY("ChemicalTerm_curie") REFERENCES "ChemicalTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "ChemicalTerm_subsets" (
	"ChemicalTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("ChemicalTerm_curie", subsets), 
	FOREIGN KEY("ChemicalTerm_curie") REFERENCES "ChemicalTerm" (curie)
);
CREATE TABLE "ChemicalTerm_secondary_identifiers" (
	"ChemicalTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("ChemicalTerm_curie", secondary_identifiers), 
	FOREIGN KEY("ChemicalTerm_curie") REFERENCES "ChemicalTerm" (curie)
);
CREATE TABLE "XSMOTerm_definition_urls" (
	"XSMOTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("XSMOTerm_curie", definition_urls), 
	FOREIGN KEY("XSMOTerm_curie") REFERENCES "XSMOTerm" (curie)
);
CREATE TABLE "XSMOTerm_synonym" (
	"XSMOTerm_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("XSMOTerm_curie", synonym_id), 
	FOREIGN KEY("XSMOTerm_curie") REFERENCES "XSMOTerm" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "XSMOTerm_subsets" (
	"XSMOTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("XSMOTerm_curie", subsets), 
	FOREIGN KEY("XSMOTerm_curie") REFERENCES "XSMOTerm" (curie)
);
CREATE TABLE "XSMOTerm_secondary_identifiers" (
	"XSMOTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("XSMOTerm_curie", secondary_identifiers), 
	FOREIGN KEY("XSMOTerm_curie") REFERENCES "XSMOTerm" (curie)
);
CREATE TABLE "Molecule_definition_urls" (
	"Molecule_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("Molecule_curie", definition_urls), 
	FOREIGN KEY("Molecule_curie") REFERENCES "Molecule" (curie)
);
CREATE TABLE "Molecule_synonym" (
	"Molecule_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("Molecule_curie", synonym_id), 
	FOREIGN KEY("Molecule_curie") REFERENCES "Molecule" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "Molecule_subsets" (
	"Molecule_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("Molecule_curie", subsets), 
	FOREIGN KEY("Molecule_curie") REFERENCES "Molecule" (curie)
);
CREATE TABLE "Molecule_secondary_identifiers" (
	"Molecule_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("Molecule_curie", secondary_identifiers), 
	FOREIGN KEY("Molecule_curie") REFERENCES "Molecule" (curie)
);
CREATE TABLE "LoggedInPerson_emails" (
	"LoggedInPerson_unique_id" TEXT, 
	emails TEXT, 
	PRIMARY KEY ("LoggedInPerson_unique_id", emails), 
	FOREIGN KEY("LoggedInPerson_unique_id") REFERENCES "LoggedInPerson" (unique_id)
);
CREATE TABLE "LoggedInPerson_old_emails" (
	"LoggedInPerson_unique_id" TEXT, 
	old_emails TEXT, 
	PRIMARY KEY ("LoggedInPerson_unique_id", old_emails), 
	FOREIGN KEY("LoggedInPerson_unique_id") REFERENCES "LoggedInPerson" (unique_id)
);
CREATE TABLE "Resource_synonym" (
	"Resource_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("Resource_curie", synonym_id), 
	FOREIGN KEY("Resource_curie") REFERENCES "Resource" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "ExpressionExperiment" (
	curie TEXT NOT NULL, 
	single_reference TEXT, 
	biological_entity_assayed TEXT, 
	assay_used TEXT, 
	specimen_genomic_model TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(biological_entity_assayed) REFERENCES "BiologicalEntity" (curie), 
	FOREIGN KEY(assay_used) REFERENCES "MMOTerm" (curie), 
	FOREIGN KEY(specimen_genomic_model) REFERENCES "AffectedGenomicModel" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "GeneExpressionStatement" (
	id INTEGER, 
	statement_subject TEXT, 
	statement_type VARCHAR(26), 
	statement_text TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(statement_subject) REFERENCES "Gene" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "GenomicLocation" (
	id INTEGER, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	has_assembly TEXT NOT NULL, 
	start TEXT, 
	"end" TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES "GenomicEntity" (curie), 
	FOREIGN KEY(object) REFERENCES "Chromosome" (curie), 
	FOREIGN KEY(has_assembly) REFERENCES "Assembly" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "SequenceTargetingReagentToGeneAssociation" (
	id INTEGER, 
	subject TEXT NOT NULL, 
	predicate VARCHAR(7) NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES "SequenceTargetingReagent" (curie), 
	FOREIGN KEY(object) REFERENCES "Gene" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "ConstructComponentAssociation" (
	id INTEGER, 
	subject TEXT NOT NULL, 
	predicate VARCHAR(15) NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES "Construct" (curie), 
	FOREIGN KEY(object) REFERENCES "ConstructComponent" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "VariantTranscriptLocation" (
	id INTEGER, 
	transcript TEXT, 
	evidence_code TEXT, 
	single_reference TEXT, 
	start_position INTEGER, 
	end_position INTEGER, 
	reference_sequence TEXT, 
	variant_sequence TEXT, 
	consequence TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(transcript) REFERENCES "Transcript" (curie), 
	FOREIGN KEY(evidence_code) REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(consequence) REFERENCES "SOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "VariantPolypeptideLocation" (
	id INTEGER, 
	polypeptide TEXT NOT NULL, 
	evidence_code TEXT, 
	single_reference TEXT, 
	start_position INTEGER, 
	end_position INTEGER, 
	reference_sequence TEXT, 
	variant_sequence TEXT, 
	consequence TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(polypeptide) REFERENCES "Transcript" (curie), 
	FOREIGN KEY(evidence_code) REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(consequence) REFERENCES "SOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Image" (
	curie TEXT NOT NULL, 
	associated_with_figure TEXT NOT NULL, 
	width INTEGER NOT NULL, 
	height INTEGER NOT NULL, 
	cropped_from TEXT, 
	image_x_origin INTEGER, 
	image_y_origin INTEGER, 
	video_still BOOLEAN, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	image_file_id TEXT NOT NULL, 
	image_medium_file_id TEXT NOT NULL, 
	image_thumbnail_file_id TEXT NOT NULL, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(associated_with_figure) REFERENCES "Figure" (curie), 
	FOREIGN KEY(cropped_from) REFERENCES "Image" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(image_file_id) REFERENCES "File" (id), 
	FOREIGN KEY(image_medium_file_id) REFERENCES "File" (id), 
	FOREIGN KEY(image_thumbnail_file_id) REFERENCES "File" (id)
);
CREATE TABLE "PhenotypeAnnotation" (
	curie TEXT NOT NULL, 
	single_reference TEXT, 
	phenotype_term TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE NOT NULL, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(phenotype_term) REFERENCES "PhenotypeTerm" (curie), 
	FOREIGN KEY(subject) REFERENCES "BiologicalEntity" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "GenePhenotypeAnnotation" (
	sgd_strain_background TEXT, 
	curie TEXT NOT NULL, 
	single_reference TEXT, 
	phenotype_term TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE NOT NULL, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(sgd_strain_background) REFERENCES "AffectedGenomicModel" (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(phenotype_term) REFERENCES "PhenotypeTerm" (curie), 
	FOREIGN KEY(subject) REFERENCES "Gene" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "DiseaseAnnotation" (
	id INTEGER, 
	unique_id TEXT, 
	mod_entity_id TEXT, 
	negated BOOLEAN, 
	single_reference TEXT NOT NULL, 
	annotation_type TEXT, 
	genetic_sex TEXT, 
	data_provider TEXT NOT NULL, 
	secondary_data_provider TEXT, 
	disease_genetic_modifier TEXT, 
	disease_genetic_modifier_relation TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(annotation_type) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(genetic_sex) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(disease_genetic_modifier) REFERENCES "BiologicalEntity" (curie), 
	FOREIGN KEY(disease_genetic_modifier_relation) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(subject) REFERENCES "BiologicalEntity" (curie), 
	FOREIGN KEY(object) REFERENCES "DOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "GeneDiseaseAnnotation" (
	id INTEGER, 
	sgd_strain_background TEXT, 
	unique_id TEXT, 
	mod_entity_id TEXT, 
	negated BOOLEAN, 
	single_reference TEXT NOT NULL, 
	annotation_type TEXT, 
	genetic_sex TEXT, 
	data_provider TEXT NOT NULL, 
	secondary_data_provider TEXT, 
	disease_genetic_modifier TEXT, 
	disease_genetic_modifier_relation TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(sgd_strain_background) REFERENCES "AffectedGenomicModel" (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(annotation_type) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(genetic_sex) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(disease_genetic_modifier) REFERENCES "BiologicalEntity" (curie), 
	FOREIGN KEY(disease_genetic_modifier_relation) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(subject) REFERENCES "Gene" (curie), 
	FOREIGN KEY(predicate) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(object) REFERENCES "DOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id)
);
CREATE TABLE "GeneToGeneAssociation" (
	id INTEGER, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES "Gene" (curie), 
	FOREIGN KEY(object) REFERENCES "Gene" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "GeneInteraction" (
	curie TEXT NOT NULL, 
	interaction_data_provider VARCHAR(7) NOT NULL, 
	interaction_type VARCHAR(7) NOT NULL, 
	"interactor_A_type" VARCHAR(7) NOT NULL, 
	"interactor_B_type" VARCHAR(7) NOT NULL, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(subject) REFERENCES "Gene" (curie), 
	FOREIGN KEY(object) REFERENCES "Gene" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "GeneMolecularInteraction" (
	aggregation_database VARCHAR(7), 
	detection_method VARCHAR(7), 
	curie TEXT NOT NULL, 
	interaction_data_provider VARCHAR(7) NOT NULL, 
	interaction_type VARCHAR(7) NOT NULL, 
	"interactor_A_type" VARCHAR(7) NOT NULL, 
	"interactor_B_type" VARCHAR(7) NOT NULL, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(subject) REFERENCES "Gene" (curie), 
	FOREIGN KEY(object) REFERENCES "Gene" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "VariantGeneConsequence" (
	id INTEGER, 
	object TEXT NOT NULL, 
	vep_consequence VARCHAR(8), 
	vep_impact TEXT, 
	polyphen_score FLOAT, 
	polyphen_prediction VARCHAR(17), 
	sift_score FLOAT, 
	sift_prediction VARCHAR(11), 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	subject_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(object) REFERENCES "Gene" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(subject_id) REFERENCES "VariantGenomeLocation" (id)
);
CREATE TABLE "GenomicEntity_synonym" (
	"GenomicEntity_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("GenomicEntity_curie", synonym_id), 
	FOREIGN KEY("GenomicEntity_curie") REFERENCES "GenomicEntity" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "GenomicEntity_secondary_identifiers" (
	"GenomicEntity_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("GenomicEntity_curie", secondary_identifiers), 
	FOREIGN KEY("GenomicEntity_curie") REFERENCES "GenomicEntity" (curie)
);
CREATE TABLE "Transcript_synonym" (
	"Transcript_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("Transcript_curie", synonym_id), 
	FOREIGN KEY("Transcript_curie") REFERENCES "Transcript" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "Transcript_secondary_identifiers" (
	"Transcript_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("Transcript_curie", secondary_identifiers), 
	FOREIGN KEY("Transcript_curie") REFERENCES "Transcript" (curie)
);
CREATE TABLE "Gene_synonym" (
	"Gene_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("Gene_curie", synonym_id), 
	FOREIGN KEY("Gene_curie") REFERENCES "Gene" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "Gene_secondary_identifiers" (
	"Gene_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("Gene_curie", secondary_identifiers), 
	FOREIGN KEY("Gene_curie") REFERENCES "Gene" (curie)
);
CREATE TABLE "Note_reference" (
	"Note_id" TEXT, 
	reference TEXT, 
	PRIMARY KEY ("Note_id", reference), 
	FOREIGN KEY("Note_id") REFERENCES "Note" (id), 
	FOREIGN KEY(reference) REFERENCES "Reference" (curie)
);
CREATE TABLE "Protein_synonym" (
	"Protein_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("Protein_curie", synonym_id), 
	FOREIGN KEY("Protein_curie") REFERENCES "Protein" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "Protein_secondary_identifiers" (
	"Protein_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("Protein_curie", secondary_identifiers), 
	FOREIGN KEY("Protein_curie") REFERENCES "Protein" (curie)
);
CREATE TABLE "Construct_construct_components" (
	"Construct_curie" TEXT, 
	construct_components TEXT, 
	PRIMARY KEY ("Construct_curie", construct_components), 
	FOREIGN KEY("Construct_curie") REFERENCES "Construct" (curie), 
	FOREIGN KEY(construct_components) REFERENCES "GenomicEntity" (curie)
);
CREATE TABLE "Construct_reference" (
	"Construct_curie" TEXT, 
	reference TEXT, 
	PRIMARY KEY ("Construct_curie", reference), 
	FOREIGN KEY("Construct_curie") REFERENCES "Construct" (curie), 
	FOREIGN KEY(reference) REFERENCES "Reference" (curie)
);
CREATE TABLE "Construct_synonym" (
	"Construct_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("Construct_curie", synonym_id), 
	FOREIGN KEY("Construct_curie") REFERENCES "Construct" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "Construct_secondary_identifiers" (
	"Construct_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("Construct_curie", secondary_identifiers), 
	FOREIGN KEY("Construct_curie") REFERENCES "Construct" (curie)
);
CREATE TABLE "SequenceTargetingReagent_reference" (
	"SequenceTargetingReagent_curie" TEXT, 
	reference TEXT, 
	PRIMARY KEY ("SequenceTargetingReagent_curie", reference), 
	FOREIGN KEY("SequenceTargetingReagent_curie") REFERENCES "SequenceTargetingReagent" (curie), 
	FOREIGN KEY(reference) REFERENCES "Reference" (curie)
);
CREATE TABLE "SequenceTargetingReagent_synonym" (
	"SequenceTargetingReagent_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("SequenceTargetingReagent_curie", synonym_id), 
	FOREIGN KEY("SequenceTargetingReagent_curie") REFERENCES "SequenceTargetingReagent" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "SequenceTargetingReagent_secondary_identifiers" (
	"SequenceTargetingReagent_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("SequenceTargetingReagent_curie", secondary_identifiers), 
	FOREIGN KEY("SequenceTargetingReagent_curie") REFERENCES "SequenceTargetingReagent" (curie)
);
CREATE TABLE "ConstructComponent_synonym" (
	"ConstructComponent_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("ConstructComponent_curie", synonym_id), 
	FOREIGN KEY("ConstructComponent_curie") REFERENCES "ConstructComponent" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "ConstructComponent_secondary_identifiers" (
	"ConstructComponent_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("ConstructComponent_curie", secondary_identifiers), 
	FOREIGN KEY("ConstructComponent_curie") REFERENCES "ConstructComponent" (curie)
);
CREATE TABLE "AffectedGenomicModel_sequence_targeting_reagent" (
	"AffectedGenomicModel_curie" TEXT, 
	sequence_targeting_reagent TEXT, 
	PRIMARY KEY ("AffectedGenomicModel_curie", sequence_targeting_reagent), 
	FOREIGN KEY("AffectedGenomicModel_curie") REFERENCES "AffectedGenomicModel" (curie), 
	FOREIGN KEY(sequence_targeting_reagent) REFERENCES "SequenceTargetingReagent" (curie)
);
CREATE TABLE "AffectedGenomicModel_reference" (
	"AffectedGenomicModel_curie" TEXT, 
	reference TEXT, 
	PRIMARY KEY ("AffectedGenomicModel_curie", reference), 
	FOREIGN KEY("AffectedGenomicModel_curie") REFERENCES "AffectedGenomicModel" (curie), 
	FOREIGN KEY(reference) REFERENCES "Reference" (curie)
);
CREATE TABLE "AffectedGenomicModel_synonym" (
	"AffectedGenomicModel_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("AffectedGenomicModel_curie", synonym_id), 
	FOREIGN KEY("AffectedGenomicModel_curie") REFERENCES "AffectedGenomicModel" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "AffectedGenomicModel_secondary_identifiers" (
	"AffectedGenomicModel_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("AffectedGenomicModel_curie", secondary_identifiers), 
	FOREIGN KEY("AffectedGenomicModel_curie") REFERENCES "AffectedGenomicModel" (curie)
);
CREATE TABLE "Variant_related_notes" (
	"Variant_curie" TEXT, 
	related_notes_id TEXT, 
	PRIMARY KEY ("Variant_curie", related_notes_id), 
	FOREIGN KEY("Variant_curie") REFERENCES "Variant" (curie), 
	FOREIGN KEY(related_notes_id) REFERENCES "Note" (id)
);
CREATE TABLE "Variant_variant_genome_locations" (
	"Variant_curie" TEXT, 
	variant_genome_locations_id TEXT NOT NULL, 
	PRIMARY KEY ("Variant_curie", variant_genome_locations_id), 
	FOREIGN KEY("Variant_curie") REFERENCES "Variant" (curie), 
	FOREIGN KEY(variant_genome_locations_id) REFERENCES "VariantGenomeLocation" (id)
);
CREATE TABLE "Variant_source_variant_locations" (
	"Variant_curie" TEXT, 
	source_variant_locations_id TEXT, 
	PRIMARY KEY ("Variant_curie", source_variant_locations_id), 
	FOREIGN KEY("Variant_curie") REFERENCES "Variant" (curie), 
	FOREIGN KEY(source_variant_locations_id) REFERENCES "SourceVariantLocation" (id)
);
CREATE TABLE "Variant_synonym" (
	"Variant_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("Variant_curie", synonym_id), 
	FOREIGN KEY("Variant_curie") REFERENCES "Variant" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "Variant_secondary_identifiers" (
	"Variant_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("Variant_curie", secondary_identifiers), 
	FOREIGN KEY("Variant_curie") REFERENCES "Variant" (curie)
);
CREATE TABLE "SourceVariantLocation_variant_locations" (
	"SourceVariantLocation_id" TEXT, 
	variant_locations_id TEXT NOT NULL, 
	PRIMARY KEY ("SourceVariantLocation_id", variant_locations_id), 
	FOREIGN KEY("SourceVariantLocation_id") REFERENCES "SourceVariantLocation" (id), 
	FOREIGN KEY(variant_locations_id) REFERENCES "VariantLocation" (id)
);
CREATE TABLE "Figure_secondary_identifiers" (
	"Figure_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("Figure_curie", secondary_identifiers), 
	FOREIGN KEY("Figure_curie") REFERENCES "Figure" (curie)
);
CREATE TABLE "Resource_authors" (
	"Resource_curie" TEXT, 
	authors_id TEXT, 
	PRIMARY KEY ("Resource_curie", authors_id), 
	FOREIGN KEY("Resource_curie") REFERENCES "Resource" (curie), 
	FOREIGN KEY(authors_id) REFERENCES "AuthorReference" (id)
);
CREATE TABLE "Resource_editor" (
	"Resource_curie" TEXT, 
	editor_id TEXT, 
	PRIMARY KEY ("Resource_curie", editor_id), 
	FOREIGN KEY("Resource_curie") REFERENCES "Resource" (curie), 
	FOREIGN KEY(editor_id) REFERENCES "AuthorReference" (id)
);
CREATE TABLE "Reagent_generated_by" (
	"Reagent_curie" TEXT, 
	generated_by_id TEXT, 
	PRIMARY KEY ("Reagent_curie", generated_by_id), 
	FOREIGN KEY("Reagent_curie") REFERENCES "Reagent" (curie), 
	FOREIGN KEY(generated_by_id) REFERENCES "Agent" (id)
);
CREATE TABLE "Reagent_manufactured_by" (
	"Reagent_curie" TEXT, 
	manufactured_by_id TEXT, 
	PRIMARY KEY ("Reagent_curie", manufactured_by_id), 
	FOREIGN KEY("Reagent_curie") REFERENCES "Reagent" (curie), 
	FOREIGN KEY(manufactured_by_id) REFERENCES "Agent" (id)
);
CREATE TABLE "Antibody_antibody_target_genes" (
	"Antibody_curie" TEXT, 
	antibody_target_genes TEXT, 
	PRIMARY KEY ("Antibody_curie", antibody_target_genes), 
	FOREIGN KEY("Antibody_curie") REFERENCES "Antibody" (curie), 
	FOREIGN KEY(antibody_target_genes) REFERENCES "Gene" (curie)
);
CREATE TABLE "Antibody_secondary_identifiers" (
	"Antibody_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("Antibody_curie", secondary_identifiers), 
	FOREIGN KEY("Antibody_curie") REFERENCES "Antibody" (curie)
);
CREATE TABLE "Antibody_reference" (
	"Antibody_curie" TEXT, 
	reference TEXT, 
	PRIMARY KEY ("Antibody_curie", reference), 
	FOREIGN KEY("Antibody_curie") REFERENCES "Antibody" (curie), 
	FOREIGN KEY(reference) REFERENCES "Reference" (curie)
);
CREATE TABLE "Antibody_original_reference" (
	"Antibody_curie" TEXT, 
	original_reference TEXT, 
	PRIMARY KEY ("Antibody_curie", original_reference), 
	FOREIGN KEY("Antibody_curie") REFERENCES "Antibody" (curie), 
	FOREIGN KEY(original_reference) REFERENCES "Reference" (curie)
);
CREATE TABLE "Antibody_related_notes" (
	"Antibody_curie" TEXT, 
	related_notes_id TEXT, 
	PRIMARY KEY ("Antibody_curie", related_notes_id), 
	FOREIGN KEY("Antibody_curie") REFERENCES "Antibody" (curie), 
	FOREIGN KEY(related_notes_id) REFERENCES "Note" (id)
);
CREATE TABLE "Antibody_generated_by" (
	"Antibody_curie" TEXT, 
	generated_by_id TEXT, 
	PRIMARY KEY ("Antibody_curie", generated_by_id), 
	FOREIGN KEY("Antibody_curie") REFERENCES "Antibody" (curie), 
	FOREIGN KEY(generated_by_id) REFERENCES "Agent" (id)
);
CREATE TABLE "Antibody_manufactured_by" (
	"Antibody_curie" TEXT, 
	manufactured_by_id TEXT, 
	PRIMARY KEY ("Antibody_curie", manufactured_by_id), 
	FOREIGN KEY("Antibody_curie") REFERENCES "Antibody" (curie), 
	FOREIGN KEY(manufactured_by_id) REFERENCES "Agent" (id)
);
CREATE TABLE "DNAClone_generated_by" (
	"DNAClone_curie" TEXT, 
	generated_by_id TEXT, 
	PRIMARY KEY ("DNAClone_curie", generated_by_id), 
	FOREIGN KEY("DNAClone_curie") REFERENCES "DNAClone" (curie), 
	FOREIGN KEY(generated_by_id) REFERENCES "Agent" (id)
);
CREATE TABLE "DNAClone_manufactured_by" (
	"DNAClone_curie" TEXT, 
	manufactured_by_id TEXT, 
	PRIMARY KEY ("DNAClone_curie", manufactured_by_id), 
	FOREIGN KEY("DNAClone_curie") REFERENCES "DNAClone" (curie), 
	FOREIGN KEY(manufactured_by_id) REFERENCES "Agent" (id)
);
CREATE TABLE "RNAClone_generated_by" (
	"RNAClone_curie" TEXT, 
	generated_by_id TEXT, 
	PRIMARY KEY ("RNAClone_curie", generated_by_id), 
	FOREIGN KEY("RNAClone_curie") REFERENCES "RNAClone" (curie), 
	FOREIGN KEY(generated_by_id) REFERENCES "Agent" (id)
);
CREATE TABLE "RNAClone_manufactured_by" (
	"RNAClone_curie" TEXT, 
	manufactured_by_id TEXT, 
	PRIMARY KEY ("RNAClone_curie", manufactured_by_id), 
	FOREIGN KEY("RNAClone_curie") REFERENCES "RNAClone" (curie), 
	FOREIGN KEY(manufactured_by_id) REFERENCES "Agent" (id)
);
CREATE TABLE "ExpressionAnnotation" (
	id INTEGER, 
	belongs_to_expression_experiment TEXT NOT NULL, 
	expression_qualifiers VARCHAR(21), 
	negated BOOLEAN, 
	uncertain BOOLEAN, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	when_expressed_id TEXT, 
	where_expressed_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(belongs_to_expression_experiment) REFERENCES "ExpressionExperiment" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(when_expressed_id) REFERENCES "TemporalContext" (id), 
	FOREIGN KEY(where_expressed_id) REFERENCES "AnatomicalSite" (id)
);
CREATE TABLE "ExpressionExperimentStatement" (
	id INTEGER, 
	statement_subject TEXT, 
	statement_type TEXT, 
	statement_text TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(statement_subject) REFERENCES "ExpressionExperiment" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Allele" (
	symbol TEXT, 
	functional_impact TEXT, 
	generation_method TEXT, 
	germline_transmission_status TEXT, 
	images TEXT, 
	database_status TEXT, 
	inheritence_mode TEXT, 
	in_collection TEXT, 
	transposon_insertion TEXT, 
	aberration TEXT, 
	is_extinct BOOLEAN, 
	sequencing_status TEXT, 
	name TEXT NOT NULL, 
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	parent_cell_line_id TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(germline_transmission_status) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(images) REFERENCES "Image" (curie), 
	FOREIGN KEY(database_status) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(inheritence_mode) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(in_collection) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(sequencing_status) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id), 
	FOREIGN KEY(parent_cell_line_id) REFERENCES "CellLine" (id)
);
CREATE TABLE "ImagePane" (
	id INTEGER, 
	from_image TEXT NOT NULL, 
	label TEXT, 
	width INTEGER NOT NULL, 
	height INTEGER NOT NULL, 
	image_x_origin INTEGER, 
	image_y_origin INTEGER, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(from_image) REFERENCES "Image" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "VariantTranscriptConsequence" (
	id INTEGER, 
	amino_acid_reference TEXT, 
	amino_acid_variant TEXT, 
	codon_reference TEXT, 
	codon_variant TEXT, 
	cdna_start INTEGER, 
	cdna_end INTEGER, 
	cds_start INTEGER, 
	cds_end INTEGER, 
	protein_start INTEGER, 
	protein_end INTEGER, 
	hgvs_protein_nomenclature TEXT, 
	hgvs_coding_nomenclature TEXT, 
	object TEXT NOT NULL, 
	vep_consequence VARCHAR(8), 
	vep_impact TEXT, 
	polyphen_score FLOAT, 
	polyphen_prediction VARCHAR(17), 
	sift_score FLOAT, 
	sift_prediction VARCHAR(11), 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	subject_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(object) REFERENCES "Transcript" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(subject_id) REFERENCES "VariantTranscriptLocation" (id)
);
CREATE TABLE "ExpressionExperiment_reagents_used" (
	"ExpressionExperiment_curie" TEXT, 
	reagents_used TEXT, 
	PRIMARY KEY ("ExpressionExperiment_curie", reagents_used), 
	FOREIGN KEY("ExpressionExperiment_curie") REFERENCES "ExpressionExperiment" (curie), 
	FOREIGN KEY(reagents_used) REFERENCES "Reagent" (curie)
);
CREATE TABLE "GeneExpressionStatement_reference" (
	"GeneExpressionStatement_id" TEXT, 
	reference TEXT, 
	PRIMARY KEY ("GeneExpressionStatement_id", reference), 
	FOREIGN KEY("GeneExpressionStatement_id") REFERENCES "GeneExpressionStatement" (id), 
	FOREIGN KEY(reference) REFERENCES "Reference" (curie)
);
CREATE TABLE "GenomicEntity_genomic_locations" (
	"GenomicEntity_curie" TEXT, 
	genomic_locations_id TEXT, 
	PRIMARY KEY ("GenomicEntity_curie", genomic_locations_id), 
	FOREIGN KEY("GenomicEntity_curie") REFERENCES "GenomicEntity" (curie), 
	FOREIGN KEY(genomic_locations_id) REFERENCES "GenomicLocation" (id)
);
CREATE TABLE "Transcript_genomic_locations" (
	"Transcript_curie" TEXT, 
	genomic_locations_id TEXT, 
	PRIMARY KEY ("Transcript_curie", genomic_locations_id), 
	FOREIGN KEY("Transcript_curie") REFERENCES "Transcript" (curie), 
	FOREIGN KEY(genomic_locations_id) REFERENCES "GenomicLocation" (id)
);
CREATE TABLE "Gene_genomic_locations" (
	"Gene_curie" TEXT, 
	genomic_locations_id TEXT, 
	PRIMARY KEY ("Gene_curie", genomic_locations_id), 
	FOREIGN KEY("Gene_curie") REFERENCES "Gene" (curie), 
	FOREIGN KEY(genomic_locations_id) REFERENCES "GenomicLocation" (id)
);
CREATE TABLE "Protein_genomic_locations" (
	"Protein_curie" TEXT, 
	genomic_locations_id TEXT, 
	PRIMARY KEY ("Protein_curie", genomic_locations_id), 
	FOREIGN KEY("Protein_curie") REFERENCES "Protein" (curie), 
	FOREIGN KEY(genomic_locations_id) REFERENCES "GenomicLocation" (id)
);
CREATE TABLE "Construct_genomic_locations" (
	"Construct_curie" TEXT, 
	genomic_locations_id TEXT, 
	PRIMARY KEY ("Construct_curie", genomic_locations_id), 
	FOREIGN KEY("Construct_curie") REFERENCES "Construct" (curie), 
	FOREIGN KEY(genomic_locations_id) REFERENCES "GenomicLocation" (id)
);
CREATE TABLE "SequenceTargetingReagent_genomic_locations" (
	"SequenceTargetingReagent_curie" TEXT, 
	genomic_locations_id TEXT, 
	PRIMARY KEY ("SequenceTargetingReagent_curie", genomic_locations_id), 
	FOREIGN KEY("SequenceTargetingReagent_curie") REFERENCES "SequenceTargetingReagent" (curie), 
	FOREIGN KEY(genomic_locations_id) REFERENCES "GenomicLocation" (id)
);
CREATE TABLE "SequenceTargetingReagentToGeneAssociation_reference" (
	"SequenceTargetingReagentToGeneAssociation_id" TEXT, 
	reference TEXT, 
	PRIMARY KEY ("SequenceTargetingReagentToGeneAssociation_id", reference), 
	FOREIGN KEY("SequenceTargetingReagentToGeneAssociation_id") REFERENCES "SequenceTargetingReagentToGeneAssociation" (id), 
	FOREIGN KEY(reference) REFERENCES "Reference" (curie)
);
CREATE TABLE "ConstructComponent_genomic_locations" (
	"ConstructComponent_curie" TEXT, 
	genomic_locations_id TEXT, 
	PRIMARY KEY ("ConstructComponent_curie", genomic_locations_id), 
	FOREIGN KEY("ConstructComponent_curie") REFERENCES "ConstructComponent" (curie), 
	FOREIGN KEY(genomic_locations_id) REFERENCES "GenomicLocation" (id)
);
CREATE TABLE "AffectedGenomicModel_genomic_locations" (
	"AffectedGenomicModel_curie" TEXT, 
	genomic_locations_id TEXT, 
	PRIMARY KEY ("AffectedGenomicModel_curie", genomic_locations_id), 
	FOREIGN KEY("AffectedGenomicModel_curie") REFERENCES "AffectedGenomicModel" (curie), 
	FOREIGN KEY(genomic_locations_id) REFERENCES "GenomicLocation" (id)
);
CREATE TABLE "Variant_variant_polypeptide_locations" (
	"Variant_curie" TEXT, 
	variant_polypeptide_locations_id TEXT NOT NULL, 
	PRIMARY KEY ("Variant_curie", variant_polypeptide_locations_id), 
	FOREIGN KEY("Variant_curie") REFERENCES "Variant" (curie), 
	FOREIGN KEY(variant_polypeptide_locations_id) REFERENCES "VariantPolypeptideLocation" (id)
);
CREATE TABLE "Variant_variant_transcript_locations" (
	"Variant_curie" TEXT, 
	variant_transcript_locations_id TEXT NOT NULL, 
	PRIMARY KEY ("Variant_curie", variant_transcript_locations_id), 
	FOREIGN KEY("Variant_curie") REFERENCES "Variant" (curie), 
	FOREIGN KEY(variant_transcript_locations_id) REFERENCES "VariantTranscriptLocation" (id)
);
CREATE TABLE "Variant_genomic_locations" (
	"Variant_curie" TEXT, 
	genomic_locations_id TEXT, 
	PRIMARY KEY ("Variant_curie", genomic_locations_id), 
	FOREIGN KEY("Variant_curie") REFERENCES "Variant" (curie), 
	FOREIGN KEY(genomic_locations_id) REFERENCES "GenomicLocation" (id)
);
CREATE TABLE "VariantPolypeptideLocation_associated_transcripts" (
	"VariantPolypeptideLocation_id" TEXT, 
	associated_transcripts TEXT, 
	PRIMARY KEY ("VariantPolypeptideLocation_id", associated_transcripts), 
	FOREIGN KEY("VariantPolypeptideLocation_id") REFERENCES "VariantPolypeptideLocation" (id), 
	FOREIGN KEY(associated_transcripts) REFERENCES "Transcript" (curie)
);
CREATE TABLE "Image_secondary_identifiers" (
	"Image_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("Image_curie", secondary_identifiers), 
	FOREIGN KEY("Image_curie") REFERENCES "Image" (curie)
);
CREATE TABLE "DiseaseAnnotation_evidence_codes" (
	"DiseaseAnnotation_id" TEXT, 
	evidence_codes TEXT NOT NULL, 
	PRIMARY KEY ("DiseaseAnnotation_id", evidence_codes), 
	FOREIGN KEY("DiseaseAnnotation_id") REFERENCES "DiseaseAnnotation" (id), 
	FOREIGN KEY(evidence_codes) REFERENCES "ECOTerm" (curie)
);
CREATE TABLE "DiseaseAnnotation_with" (
	"DiseaseAnnotation_id" TEXT, 
	with TEXT, 
	PRIMARY KEY ("DiseaseAnnotation_id", with), 
	FOREIGN KEY("DiseaseAnnotation_id") REFERENCES "DiseaseAnnotation" (id), 
	FOREIGN KEY(with) REFERENCES "Gene" (curie)
);
CREATE TABLE "DiseaseAnnotation_disease_qualifiers" (
	"DiseaseAnnotation_id" TEXT, 
	disease_qualifiers TEXT, 
	PRIMARY KEY ("DiseaseAnnotation_id", disease_qualifiers), 
	FOREIGN KEY("DiseaseAnnotation_id") REFERENCES "DiseaseAnnotation" (id), 
	FOREIGN KEY(disease_qualifiers) REFERENCES "VocabularyTerm" (name)
);
CREATE TABLE "DiseaseAnnotation_related_notes" (
	"DiseaseAnnotation_id" TEXT, 
	related_notes_id TEXT, 
	PRIMARY KEY ("DiseaseAnnotation_id", related_notes_id), 
	FOREIGN KEY("DiseaseAnnotation_id") REFERENCES "DiseaseAnnotation" (id), 
	FOREIGN KEY(related_notes_id) REFERENCES "Note" (id)
);
CREATE TABLE "GeneDiseaseAnnotation_evidence_codes" (
	"GeneDiseaseAnnotation_id" TEXT, 
	evidence_codes TEXT NOT NULL, 
	PRIMARY KEY ("GeneDiseaseAnnotation_id", evidence_codes), 
	FOREIGN KEY("GeneDiseaseAnnotation_id") REFERENCES "GeneDiseaseAnnotation" (id), 
	FOREIGN KEY(evidence_codes) REFERENCES "ECOTerm" (curie)
);
CREATE TABLE "GeneDiseaseAnnotation_with" (
	"GeneDiseaseAnnotation_id" TEXT, 
	with TEXT, 
	PRIMARY KEY ("GeneDiseaseAnnotation_id", with), 
	FOREIGN KEY("GeneDiseaseAnnotation_id") REFERENCES "GeneDiseaseAnnotation" (id), 
	FOREIGN KEY(with) REFERENCES "Gene" (curie)
);
CREATE TABLE "GeneDiseaseAnnotation_disease_qualifiers" (
	"GeneDiseaseAnnotation_id" TEXT, 
	disease_qualifiers TEXT, 
	PRIMARY KEY ("GeneDiseaseAnnotation_id", disease_qualifiers), 
	FOREIGN KEY("GeneDiseaseAnnotation_id") REFERENCES "GeneDiseaseAnnotation" (id), 
	FOREIGN KEY(disease_qualifiers) REFERENCES "VocabularyTerm" (name)
);
CREATE TABLE "GeneDiseaseAnnotation_related_notes" (
	"GeneDiseaseAnnotation_id" TEXT, 
	related_notes_id TEXT, 
	PRIMARY KEY ("GeneDiseaseAnnotation_id", related_notes_id), 
	FOREIGN KEY("GeneDiseaseAnnotation_id") REFERENCES "GeneDiseaseAnnotation" (id), 
	FOREIGN KEY(related_notes_id) REFERENCES "Note" (id)
);
CREATE TABLE "GeneInteraction_interactor_A_role" (
	"GeneInteraction_curie" TEXT, 
	"interactor_A_role" VARCHAR(7), 
	PRIMARY KEY ("GeneInteraction_curie", "interactor_A_role"), 
	FOREIGN KEY("GeneInteraction_curie") REFERENCES "GeneInteraction" (curie)
);
CREATE TABLE "GeneInteraction_interactor_B_role" (
	"GeneInteraction_curie" TEXT, 
	"interactor_B_role" VARCHAR(7), 
	PRIMARY KEY ("GeneInteraction_curie", "interactor_B_role"), 
	FOREIGN KEY("GeneInteraction_curie") REFERENCES "GeneInteraction" (curie)
);
CREATE TABLE "GeneMolecularInteraction_interactor_A_role" (
	"GeneMolecularInteraction_curie" TEXT, 
	"interactor_A_role" VARCHAR(7), 
	PRIMARY KEY ("GeneMolecularInteraction_curie", "interactor_A_role"), 
	FOREIGN KEY("GeneMolecularInteraction_curie") REFERENCES "GeneMolecularInteraction" (curie)
);
CREATE TABLE "GeneMolecularInteraction_interactor_B_role" (
	"GeneMolecularInteraction_curie" TEXT, 
	"interactor_B_role" VARCHAR(7), 
	PRIMARY KEY ("GeneMolecularInteraction_curie", "interactor_B_role"), 
	FOREIGN KEY("GeneMolecularInteraction_curie") REFERENCES "GeneMolecularInteraction" (curie)
);
CREATE TABLE "ExpressionAnnotationImagePane" (
	id INTEGER, 
	predicate TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	subject_id TEXT NOT NULL, 
	object_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(subject_id) REFERENCES "ExpressionAnnotation" (id), 
	FOREIGN KEY(object_id) REFERENCES "ImagePane" (id)
);
CREATE TABLE "ExpressionAnnotationStatement" (
	id INTEGER, 
	statement_type VARCHAR(26), 
	statement_text TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	statement_subject_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(statement_subject_id) REFERENCES "ExpressionAnnotation" (id)
);
CREATE TABLE "AlleleGenomicEntityAssociation" (
	id INTEGER, 
	single_reference TEXT, 
	evidence_code TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	related_note_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(evidence_code) REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(subject) REFERENCES "Allele" (curie), 
	FOREIGN KEY(predicate) REFERENCES "ROTerm" (curie), 
	FOREIGN KEY(object) REFERENCES "GenomicEntity" (curie), 
	FOREIGN KEY(related_note_id) REFERENCES "Note" (id)
);
CREATE TABLE "AlleleGeneAssociation" (
	id INTEGER, 
	single_reference TEXT, 
	evidence_code TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	related_note_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(evidence_code) REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(subject) REFERENCES "Allele" (curie), 
	FOREIGN KEY(predicate) REFERENCES "ROTerm" (curie), 
	FOREIGN KEY(object) REFERENCES "Gene" (curie), 
	FOREIGN KEY(related_note_id) REFERENCES "Note" (id)
);
CREATE TABLE "AlleleTranscriptAssociation" (
	id INTEGER, 
	single_reference TEXT, 
	evidence_code TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	related_note_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(evidence_code) REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(subject) REFERENCES "Allele" (curie), 
	FOREIGN KEY(predicate) REFERENCES "ROTerm" (curie), 
	FOREIGN KEY(object) REFERENCES "Transcript" (curie), 
	FOREIGN KEY(related_note_id) REFERENCES "Note" (id)
);
CREATE TABLE "AlleleProteinAssociation" (
	id INTEGER, 
	single_reference TEXT, 
	evidence_code TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	related_note_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(evidence_code) REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(subject) REFERENCES "Allele" (curie), 
	FOREIGN KEY(predicate) REFERENCES "ROTerm" (curie), 
	FOREIGN KEY(object) REFERENCES "Protein" (curie), 
	FOREIGN KEY(related_note_id) REFERENCES "Note" (id)
);
CREATE TABLE "AlleleVariantAssociation" (
	id INTEGER, 
	single_reference TEXT, 
	evidence_code TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	"Ingest_id" TEXT, 
	related_note_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(evidence_code) REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(subject) REFERENCES "Allele" (curie), 
	FOREIGN KEY(predicate) REFERENCES "ROTerm" (curie), 
	FOREIGN KEY(object) REFERENCES "Variant" (curie), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id), 
	FOREIGN KEY(related_note_id) REFERENCES "Note" (id)
);
CREATE TABLE "AffectedGenomicModelComponent" (
	id INTEGER, 
	has_allele TEXT, 
	zygosity VARCHAR(12), 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_allele) REFERENCES "Allele" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AllelePhenotypeAnnotation" (
	inferred_gene TEXT, 
	curie TEXT NOT NULL, 
	single_reference TEXT, 
	phenotype_term TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE NOT NULL, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(inferred_gene) REFERENCES "Gene" (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(phenotype_term) REFERENCES "PhenotypeTerm" (curie), 
	FOREIGN KEY(subject) REFERENCES "Allele" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AGMPhenotypeAnnotation" (
	inferred_allele TEXT, 
	inferred_gene TEXT, 
	curie TEXT NOT NULL, 
	single_reference TEXT, 
	phenotype_term TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE NOT NULL, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(inferred_allele) REFERENCES "Allele" (curie), 
	FOREIGN KEY(inferred_gene) REFERENCES "Gene" (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(phenotype_term) REFERENCES "PhenotypeTerm" (curie), 
	FOREIGN KEY(subject) REFERENCES "AffectedGenomicModel" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AlleleDiseaseAnnotation" (
	id INTEGER, 
	inferred_gene TEXT, 
	unique_id TEXT, 
	mod_entity_id TEXT, 
	negated BOOLEAN, 
	single_reference TEXT NOT NULL, 
	annotation_type TEXT, 
	genetic_sex TEXT, 
	data_provider TEXT NOT NULL, 
	secondary_data_provider TEXT, 
	disease_genetic_modifier TEXT, 
	disease_genetic_modifier_relation TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(inferred_gene) REFERENCES "Gene" (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(annotation_type) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(genetic_sex) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(disease_genetic_modifier) REFERENCES "BiologicalEntity" (curie), 
	FOREIGN KEY(disease_genetic_modifier_relation) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(subject) REFERENCES "Allele" (curie), 
	FOREIGN KEY(predicate) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(object) REFERENCES "DOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id)
);
CREATE TABLE "AGMDiseaseAnnotation" (
	id INTEGER, 
	inferred_allele TEXT, 
	inferred_gene TEXT, 
	unique_id TEXT, 
	mod_entity_id TEXT, 
	negated BOOLEAN, 
	single_reference TEXT NOT NULL, 
	annotation_type TEXT, 
	genetic_sex TEXT, 
	data_provider TEXT NOT NULL, 
	secondary_data_provider TEXT, 
	disease_genetic_modifier TEXT, 
	disease_genetic_modifier_relation TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(inferred_allele) REFERENCES "Allele" (curie), 
	FOREIGN KEY(inferred_gene) REFERENCES "Gene" (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(annotation_type) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(genetic_sex) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(disease_genetic_modifier) REFERENCES "BiologicalEntity" (curie), 
	FOREIGN KEY(disease_genetic_modifier_relation) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(subject) REFERENCES "AffectedGenomicModel" (curie), 
	FOREIGN KEY(predicate) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(object) REFERENCES "DOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id)
);
CREATE TABLE "GeneGeneticInteraction" (
	"interactor_A_genetic_perturbation" TEXT, 
	"interactor_B_genetic_perturbation" TEXT, 
	curie TEXT NOT NULL, 
	interaction_data_provider VARCHAR(7) NOT NULL, 
	interaction_type VARCHAR(7) NOT NULL, 
	"interactor_A_type" VARCHAR(7) NOT NULL, 
	"interactor_B_type" VARCHAR(7) NOT NULL, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY("interactor_A_genetic_perturbation") REFERENCES "Allele" (curie), 
	FOREIGN KEY("interactor_B_genetic_perturbation") REFERENCES "Allele" (curie), 
	FOREIGN KEY(subject) REFERENCES "Gene" (curie), 
	FOREIGN KEY(object) REFERENCES "Gene" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "ExpressionExperiment_specimen_alleles" (
	"ExpressionExperiment_curie" TEXT, 
	specimen_alleles TEXT, 
	PRIMARY KEY ("ExpressionExperiment_curie", specimen_alleles), 
	FOREIGN KEY("ExpressionExperiment_curie") REFERENCES "ExpressionExperiment" (curie), 
	FOREIGN KEY(specimen_alleles) REFERENCES "Allele" (curie)
);
CREATE TABLE "ExpressionAnnotation_associated_with_figure" (
	"ExpressionAnnotation_id" TEXT, 
	associated_with_figure TEXT, 
	PRIMARY KEY ("ExpressionAnnotation_id", associated_with_figure), 
	FOREIGN KEY("ExpressionAnnotation_id") REFERENCES "ExpressionAnnotation" (id), 
	FOREIGN KEY(associated_with_figure) REFERENCES "Figure" (curie)
);
CREATE TABLE "ExpressionExperimentStatement_reference" (
	"ExpressionExperimentStatement_id" TEXT, 
	reference TEXT, 
	PRIMARY KEY ("ExpressionExperimentStatement_id", reference), 
	FOREIGN KEY("ExpressionExperimentStatement_id") REFERENCES "ExpressionExperimentStatement" (id), 
	FOREIGN KEY(reference) REFERENCES "Reference" (curie)
);
CREATE TABLE "Allele_contains_constructs" (
	"Allele_curie" TEXT, 
	contains_constructs TEXT, 
	PRIMARY KEY ("Allele_curie", contains_constructs), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(contains_constructs) REFERENCES "Construct" (curie)
);
CREATE TABLE "Allele_molecular_mutations" (
	"Allele_curie" TEXT, 
	molecular_mutations TEXT, 
	PRIMARY KEY ("Allele_curie", molecular_mutations), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie)
);
CREATE TABLE "Allele_associated_references" (
	"Allele_curie" TEXT, 
	associated_references_id TEXT, 
	PRIMARY KEY ("Allele_curie", associated_references_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(associated_references_id) REFERENCES "AssociatedReference" (id)
);
CREATE TABLE "Allele_related_notes" (
	"Allele_curie" TEXT, 
	related_notes_id TEXT, 
	PRIMARY KEY ("Allele_curie", related_notes_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(related_notes_id) REFERENCES "Note" (id)
);
CREATE TABLE "Allele_mutant_cell_line" (
	"Allele_curie" TEXT, 
	mutant_cell_line_id TEXT, 
	PRIMARY KEY ("Allele_curie", mutant_cell_line_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(mutant_cell_line_id) REFERENCES "CellLine" (id)
);
CREATE TABLE "Allele_embryonic_stem_cell_line" (
	"Allele_curie" TEXT, 
	embryonic_stem_cell_line_id TEXT, 
	PRIMARY KEY ("Allele_curie", embryonic_stem_cell_line_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(embryonic_stem_cell_line_id) REFERENCES "CellLine" (id)
);
CREATE TABLE "Allele_origin" (
	"Allele_curie" TEXT, 
	origin TEXT, 
	PRIMARY KEY ("Allele_curie", origin), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(origin) REFERENCES "AffectedGenomicModel" (curie)
);
CREATE TABLE "Allele_synonym" (
	"Allele_curie" TEXT, 
	synonym_id TEXT, 
	PRIMARY KEY ("Allele_curie", synonym_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(synonym_id) REFERENCES "Synonym" (id)
);
CREATE TABLE "Allele_secondary_identifiers" (
	"Allele_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("Allele_curie", secondary_identifiers), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie)
);
CREATE TABLE "Allele_genomic_locations" (
	"Allele_curie" TEXT, 
	genomic_locations_id TEXT, 
	PRIMARY KEY ("Allele_curie", genomic_locations_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(genomic_locations_id) REFERENCES "GenomicLocation" (id)
);
CREATE TABLE "CrossReference" (
	curie TEXT NOT NULL, 
	display_name TEXT NOT NULL, 
	prefix TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"AuthorReference_id" TEXT, 
	"GenomicEntity_curie" TEXT, 
	"Transcript_curie" TEXT, 
	"Gene_curie" TEXT, 
	"Protein_curie" TEXT, 
	"OntologyTerm_curie" TEXT, 
	"DOTerm_curie" TEXT, 
	"ECOTerm_curie" TEXT, 
	"NCBITaxonTerm_curie" TEXT, 
	"FBCVTerm_curie" TEXT, 
	"GOTerm_curie" TEXT, 
	"ROTerm_curie" TEXT, 
	"MITerm_curie" TEXT, 
	"MMOTerm_curie" TEXT, 
	"MMUSDVTerm_curie" TEXT, 
	"SOTerm_curie" TEXT, 
	"XBEDTerm_curie" TEXT, 
	"CHEBITerm_curie" TEXT, 
	"StageTerm_curie" TEXT, 
	"FBDVTerm_curie" TEXT, 
	"WBLSTerm_curie" TEXT, 
	"XBSTerm_curie" TEXT, 
	"ZFSTerm_curie" TEXT, 
	"ExperimentalConditionOntologyTerm_curie" TEXT, 
	"ZECOTerm_curie" TEXT, 
	"XCOTerm_curie" TEXT, 
	"AnatomicalTerm_curie" TEXT, 
	"CLTerm_curie" TEXT, 
	"EMAPATerm_curie" TEXT, 
	"DAOTerm_curie" TEXT, 
	"MATerm_curie" TEXT, 
	"UBERONTerm_curie" TEXT, 
	"WBBTTerm_curie" TEXT, 
	"XBATerm_curie" TEXT, 
	"ZFATerm_curie" TEXT, 
	"PhenotypeTerm_curie" TEXT, 
	"XPOTerm_curie" TEXT, 
	"ChemicalTerm_curie" TEXT, 
	"XSMOTerm_curie" TEXT, 
	"Molecule_curie" TEXT, 
	"Allele_curie" TEXT, 
	"Construct_curie" TEXT, 
	"SequenceTargetingReagent_curie" TEXT, 
	"ConstructComponent_curie" TEXT, 
	"AffectedGenomicModel_curie" TEXT, 
	"Variant_curie" TEXT, 
	"Antibody_curie" TEXT, 
	"GeneInteraction_curie" TEXT, 
	"GeneMolecularInteraction_curie" TEXT, 
	"GeneGeneticInteraction_curie" TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY("AuthorReference_id") REFERENCES "AuthorReference" (id), 
	FOREIGN KEY("GenomicEntity_curie") REFERENCES "GenomicEntity" (curie), 
	FOREIGN KEY("Transcript_curie") REFERENCES "Transcript" (curie), 
	FOREIGN KEY("Gene_curie") REFERENCES "Gene" (curie), 
	FOREIGN KEY("Protein_curie") REFERENCES "Protein" (curie), 
	FOREIGN KEY("OntologyTerm_curie") REFERENCES "OntologyTerm" (curie), 
	FOREIGN KEY("DOTerm_curie") REFERENCES "DOTerm" (curie), 
	FOREIGN KEY("ECOTerm_curie") REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY("NCBITaxonTerm_curie") REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY("FBCVTerm_curie") REFERENCES "FBCVTerm" (curie), 
	FOREIGN KEY("GOTerm_curie") REFERENCES "GOTerm" (curie), 
	FOREIGN KEY("ROTerm_curie") REFERENCES "ROTerm" (curie), 
	FOREIGN KEY("MITerm_curie") REFERENCES "MITerm" (curie), 
	FOREIGN KEY("MMOTerm_curie") REFERENCES "MMOTerm" (curie), 
	FOREIGN KEY("MMUSDVTerm_curie") REFERENCES "MMUSDVTerm" (curie), 
	FOREIGN KEY("SOTerm_curie") REFERENCES "SOTerm" (curie), 
	FOREIGN KEY("XBEDTerm_curie") REFERENCES "XBEDTerm" (curie), 
	FOREIGN KEY("CHEBITerm_curie") REFERENCES "CHEBITerm" (curie), 
	FOREIGN KEY("StageTerm_curie") REFERENCES "StageTerm" (curie), 
	FOREIGN KEY("FBDVTerm_curie") REFERENCES "FBDVTerm" (curie), 
	FOREIGN KEY("WBLSTerm_curie") REFERENCES "WBLSTerm" (curie), 
	FOREIGN KEY("XBSTerm_curie") REFERENCES "XBSTerm" (curie), 
	FOREIGN KEY("ZFSTerm_curie") REFERENCES "ZFSTerm" (curie), 
	FOREIGN KEY("ExperimentalConditionOntologyTerm_curie") REFERENCES "ExperimentalConditionOntologyTerm" (curie), 
	FOREIGN KEY("ZECOTerm_curie") REFERENCES "ZECOTerm" (curie), 
	FOREIGN KEY("XCOTerm_curie") REFERENCES "XCOTerm" (curie), 
	FOREIGN KEY("AnatomicalTerm_curie") REFERENCES "AnatomicalTerm" (curie), 
	FOREIGN KEY("CLTerm_curie") REFERENCES "CLTerm" (curie), 
	FOREIGN KEY("EMAPATerm_curie") REFERENCES "EMAPATerm" (curie), 
	FOREIGN KEY("DAOTerm_curie") REFERENCES "DAOTerm" (curie), 
	FOREIGN KEY("MATerm_curie") REFERENCES "MATerm" (curie), 
	FOREIGN KEY("UBERONTerm_curie") REFERENCES "UBERONTerm" (curie), 
	FOREIGN KEY("WBBTTerm_curie") REFERENCES "WBBTTerm" (curie), 
	FOREIGN KEY("XBATerm_curie") REFERENCES "XBATerm" (curie), 
	FOREIGN KEY("ZFATerm_curie") REFERENCES "ZFATerm" (curie), 
	FOREIGN KEY("PhenotypeTerm_curie") REFERENCES "PhenotypeTerm" (curie), 
	FOREIGN KEY("XPOTerm_curie") REFERENCES "XPOTerm" (curie), 
	FOREIGN KEY("ChemicalTerm_curie") REFERENCES "ChemicalTerm" (curie), 
	FOREIGN KEY("XSMOTerm_curie") REFERENCES "XSMOTerm" (curie), 
	FOREIGN KEY("Molecule_curie") REFERENCES "Molecule" (curie), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY("Construct_curie") REFERENCES "Construct" (curie), 
	FOREIGN KEY("SequenceTargetingReagent_curie") REFERENCES "SequenceTargetingReagent" (curie), 
	FOREIGN KEY("ConstructComponent_curie") REFERENCES "ConstructComponent" (curie), 
	FOREIGN KEY("AffectedGenomicModel_curie") REFERENCES "AffectedGenomicModel" (curie), 
	FOREIGN KEY("Variant_curie") REFERENCES "Variant" (curie), 
	FOREIGN KEY("Antibody_curie") REFERENCES "Antibody" (curie), 
	FOREIGN KEY("GeneInteraction_curie") REFERENCES "GeneInteraction" (curie), 
	FOREIGN KEY("GeneMolecularInteraction_curie") REFERENCES "GeneMolecularInteraction" (curie), 
	FOREIGN KEY("GeneGeneticInteraction_curie") REFERENCES "GeneGeneticInteraction" (curie)
);
CREATE TABLE "ConditionRelation" (
	id INTEGER, 
	unique_id TEXT, 
	handle TEXT, 
	single_reference TEXT, 
	condition_relation_type TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"ExpressionExperiment_curie" TEXT, 
	"PhenotypeAnnotation_curie" TEXT, 
	"GenePhenotypeAnnotation_curie" TEXT, 
	"AllelePhenotypeAnnotation_curie" TEXT, 
	"AGMPhenotypeAnnotation_curie" TEXT, 
	"DiseaseAnnotation_id" TEXT, 
	"GeneDiseaseAnnotation_id" TEXT, 
	"AlleleDiseaseAnnotation_id" TEXT, 
	"AGMDiseaseAnnotation_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(condition_relation_type) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY("ExpressionExperiment_curie") REFERENCES "ExpressionExperiment" (curie), 
	FOREIGN KEY("PhenotypeAnnotation_curie") REFERENCES "PhenotypeAnnotation" (curie), 
	FOREIGN KEY("GenePhenotypeAnnotation_curie") REFERENCES "GenePhenotypeAnnotation" (curie), 
	FOREIGN KEY("AllelePhenotypeAnnotation_curie") REFERENCES "AllelePhenotypeAnnotation" (curie), 
	FOREIGN KEY("AGMPhenotypeAnnotation_curie") REFERENCES "AGMPhenotypeAnnotation" (curie), 
	FOREIGN KEY("DiseaseAnnotation_id") REFERENCES "DiseaseAnnotation" (id), 
	FOREIGN KEY("GeneDiseaseAnnotation_id") REFERENCES "GeneDiseaseAnnotation" (id), 
	FOREIGN KEY("AlleleDiseaseAnnotation_id") REFERENCES "AlleleDiseaseAnnotation" (id), 
	FOREIGN KEY("AGMDiseaseAnnotation_id") REFERENCES "AGMDiseaseAnnotation" (id)
);
CREATE TABLE "ExpressionAnnotationStatement_reference" (
	"ExpressionAnnotationStatement_id" TEXT, 
	reference TEXT, 
	PRIMARY KEY ("ExpressionAnnotationStatement_id", reference), 
	FOREIGN KEY("ExpressionAnnotationStatement_id") REFERENCES "ExpressionAnnotationStatement" (id), 
	FOREIGN KEY(reference) REFERENCES "Reference" (curie)
);
CREATE TABLE "AffectedGenomicModel_component" (
	"AffectedGenomicModel_curie" TEXT, 
	component_id TEXT, 
	PRIMARY KEY ("AffectedGenomicModel_curie", component_id), 
	FOREIGN KEY("AffectedGenomicModel_curie") REFERENCES "AffectedGenomicModel" (curie), 
	FOREIGN KEY(component_id) REFERENCES "AffectedGenomicModelComponent" (id)
);
CREATE TABLE "AlleleDiseaseAnnotation_evidence_codes" (
	"AlleleDiseaseAnnotation_id" TEXT, 
	evidence_codes TEXT NOT NULL, 
	PRIMARY KEY ("AlleleDiseaseAnnotation_id", evidence_codes), 
	FOREIGN KEY("AlleleDiseaseAnnotation_id") REFERENCES "AlleleDiseaseAnnotation" (id), 
	FOREIGN KEY(evidence_codes) REFERENCES "ECOTerm" (curie)
);
CREATE TABLE "AlleleDiseaseAnnotation_with" (
	"AlleleDiseaseAnnotation_id" TEXT, 
	with TEXT, 
	PRIMARY KEY ("AlleleDiseaseAnnotation_id", with), 
	FOREIGN KEY("AlleleDiseaseAnnotation_id") REFERENCES "AlleleDiseaseAnnotation" (id), 
	FOREIGN KEY(with) REFERENCES "Gene" (curie)
);
CREATE TABLE "AlleleDiseaseAnnotation_disease_qualifiers" (
	"AlleleDiseaseAnnotation_id" TEXT, 
	disease_qualifiers TEXT, 
	PRIMARY KEY ("AlleleDiseaseAnnotation_id", disease_qualifiers), 
	FOREIGN KEY("AlleleDiseaseAnnotation_id") REFERENCES "AlleleDiseaseAnnotation" (id), 
	FOREIGN KEY(disease_qualifiers) REFERENCES "VocabularyTerm" (name)
);
CREATE TABLE "AlleleDiseaseAnnotation_related_notes" (
	"AlleleDiseaseAnnotation_id" TEXT, 
	related_notes_id TEXT, 
	PRIMARY KEY ("AlleleDiseaseAnnotation_id", related_notes_id), 
	FOREIGN KEY("AlleleDiseaseAnnotation_id") REFERENCES "AlleleDiseaseAnnotation" (id), 
	FOREIGN KEY(related_notes_id) REFERENCES "Note" (id)
);
CREATE TABLE "AGMDiseaseAnnotation_evidence_codes" (
	"AGMDiseaseAnnotation_id" TEXT, 
	evidence_codes TEXT NOT NULL, 
	PRIMARY KEY ("AGMDiseaseAnnotation_id", evidence_codes), 
	FOREIGN KEY("AGMDiseaseAnnotation_id") REFERENCES "AGMDiseaseAnnotation" (id), 
	FOREIGN KEY(evidence_codes) REFERENCES "ECOTerm" (curie)
);
CREATE TABLE "AGMDiseaseAnnotation_with" (
	"AGMDiseaseAnnotation_id" TEXT, 
	with TEXT, 
	PRIMARY KEY ("AGMDiseaseAnnotation_id", with), 
	FOREIGN KEY("AGMDiseaseAnnotation_id") REFERENCES "AGMDiseaseAnnotation" (id), 
	FOREIGN KEY(with) REFERENCES "Gene" (curie)
);
CREATE TABLE "AGMDiseaseAnnotation_disease_qualifiers" (
	"AGMDiseaseAnnotation_id" TEXT, 
	disease_qualifiers TEXT, 
	PRIMARY KEY ("AGMDiseaseAnnotation_id", disease_qualifiers), 
	FOREIGN KEY("AGMDiseaseAnnotation_id") REFERENCES "AGMDiseaseAnnotation" (id), 
	FOREIGN KEY(disease_qualifiers) REFERENCES "VocabularyTerm" (name)
);
CREATE TABLE "AGMDiseaseAnnotation_related_notes" (
	"AGMDiseaseAnnotation_id" TEXT, 
	related_notes_id TEXT, 
	PRIMARY KEY ("AGMDiseaseAnnotation_id", related_notes_id), 
	FOREIGN KEY("AGMDiseaseAnnotation_id") REFERENCES "AGMDiseaseAnnotation" (id), 
	FOREIGN KEY(related_notes_id) REFERENCES "Note" (id)
);
CREATE TABLE "GeneGeneticInteraction_phenotype_or_trait" (
	"GeneGeneticInteraction_curie" TEXT, 
	phenotype_or_trait TEXT, 
	PRIMARY KEY ("GeneGeneticInteraction_curie", phenotype_or_trait), 
	FOREIGN KEY("GeneGeneticInteraction_curie") REFERENCES "GeneGeneticInteraction" (curie)
);
CREATE TABLE "GeneGeneticInteraction_interactor_A_role" (
	"GeneGeneticInteraction_curie" TEXT, 
	"interactor_A_role" VARCHAR(7), 
	PRIMARY KEY ("GeneGeneticInteraction_curie", "interactor_A_role"), 
	FOREIGN KEY("GeneGeneticInteraction_curie") REFERENCES "GeneGeneticInteraction" (curie)
);
CREATE TABLE "GeneGeneticInteraction_interactor_B_role" (
	"GeneGeneticInteraction_curie" TEXT, 
	"interactor_B_role" VARCHAR(7), 
	PRIMARY KEY ("GeneGeneticInteraction_curie", "interactor_B_role"), 
	FOREIGN KEY("GeneGeneticInteraction_curie") REFERENCES "GeneGeneticInteraction" (curie)
);
CREATE TABLE "ExperimentalCondition" (
	id INTEGER, 
	unique_id TEXT, 
	condition_class TEXT NOT NULL, 
	condition_summary TEXT, 
	condition_statement TEXT NOT NULL, 
	condition_id TEXT, 
	condition_free_text TEXT, 
	condition_quantity TEXT, 
	condition_anatomy TEXT, 
	condition_gene_ontology TEXT, 
	condition_taxon TEXT, 
	condition_chemical TEXT, 
	created_by TEXT, 
	date_created DATE, 
	modified_by TEXT, 
	date_updated DATE, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"ConditionRelation_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(condition_class) REFERENCES "ZECOTerm" (curie), 
	FOREIGN KEY(condition_id) REFERENCES "ExperimentalConditionOntologyTerm" (curie), 
	FOREIGN KEY(condition_anatomy) REFERENCES "AnatomicalTerm" (curie), 
	FOREIGN KEY(condition_gene_ontology) REFERENCES "GOTerm" (curie), 
	FOREIGN KEY(condition_taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(condition_chemical) REFERENCES "ChemicalTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY("ConditionRelation_id") REFERENCES "ConditionRelation" (id)
);
CREATE TABLE "CrossReference_page_areas" (
	"CrossReference_curie" TEXT, 
	page_areas TEXT NOT NULL, 
	PRIMARY KEY ("CrossReference_curie", page_areas), 
	FOREIGN KEY("CrossReference_curie") REFERENCES "CrossReference" (curie)
);
