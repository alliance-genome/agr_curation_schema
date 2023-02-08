-- # Class: "Variant" Description: "A DNA, RNA or protein/polypeptide sequence that differs relative to a designated reference sequence.  The sequence occurs at a single position or in a range of contiguous nucleotides or amino acids."
--     * Slot: variant_type Description: SOTerm describing the type of variant. In practice, variant type will be limited to a subset of the SO specified in an Alliance controlled vocabulary in order to maintain consistency.
--     * Slot: source_general_consequence Description: SOTerm (child of SO:0001576 - transcript_variant) that describes the consequence of the variant, as stated in the source reference when no transcript ID is provided. Since a curator would determine variant location and consequences relative to at least one specific genome assembly, transcript and/or polypeptide, no slot for curated general consequence is provided.
--     * Slot: variant_status Description: 
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
-- # Class: "SourceVariantLocation" Description: "Links a paper to the variant locations described in that paper"
--     * Slot: id Description: 
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Variant_curie Description: Autocreated FK slot
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "OntologyTermClosure" Description: ""
--     * Slot: id Description: 
--     * Slot: distance_between Description: distance_between is zero for reflexive–transitive closure each node has an ancestor or descendant of itself
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
-- # Class: "DOTerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "MPTerm" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "ATPTerm" Description: "An ontology term from the Alliance Tags for Papers ontology (ATP)"
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: dbkey Description: Typically the primary key on the table.  Should be a global sequence in the database to insure uniqueness over the entire suite of tables.  Alternatively, could be a serial8 identifier. Tables with a dbkey should have an alternate key to establish uniqueness based on the data in the table.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: type Description: 
--     * Slot: namespace Description: the namespace of the ontology.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Molecule" Description: "Molecules as described by WormBase"
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Allele" Description: "One of multiple possible forms of a functional genomic element (most often described as a locus or gene), differing from the reference DNA sequence.  The genomic element can be endogenous or constructed."
--     * Slot: in_collection Description: Set of high-throughput alleles made by large projects
--     * Slot: laboratory_of_origin Description: The laboratory of origin for the entity.
--     * Slot: is_extinct Description: Does the allele still exist in a population somewhere?
--     * Slot: is_extrachromosomal Description: Used by WormBase to indicate whether a transgenic allele is known to be extrachromosomal.
--     * Slot: is_integrated Description: Used by WormBase to indicate whether a transgenic allele is known to be integrated into the genome.
--     * Slot: transgene_chromosome_location Description: The chromosome to which a transgene has been mapped. Used for WormBase transgenes that have been integrated into the genome and mapped to a chromosome.
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: allele_symbol_id Description: The one current accepted symbol for the allele: e.g., wg<sup>1</sup>.
--     * Slot: allele_full_name_id Description: The one current full name for an allele: e.g., wg<sup>1</sup>.
--     * Slot: allele_germline_transmission_status_id Description: Germline transmission status for a given allele
--     * Slot: allele_database_status_id Description: Database status of a given allele
-- # Class: "CellLine" Description: "Dummy cell line class"
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Construct" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "ConstructComponent" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "ConstructComponentAssociation" Description: "The predicate should be a VocabularyTerm with one of the following values - expresses (RO:0002292) / is_regulated_by (RO:0002334) / targets (RO:0002436)"
--     * Slot: id Description: 
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "GenerationMethod" Description: ""
--     * Slot: id Description: 
--     * Slot: mutagenesis_target Description: The target of the mutation, e.g. strain / adult females / adult males / embryos / sperm / not specified
--     * Slot: integration_method Description: WormBase captures the method by which an extrachromosomal transgene was integrated into the genome.
--     * Slot: chemical_mutagen Description: The chemical used to generate the mutation through mutagenesis
--     * Slot: irradiation_mutagen Description: The irradiation used to generate the mutation through mutagenesis
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "SequenceTargetingReagent" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "SequenceTargetingReagentToGeneAssociation" Description: "the relationship between a Sequence Targeting Reagent and its targeted genes. The predicate should be a VocabularyTerm with one of the following values - targets"
--     * Slot: id Description: 
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AlleleDatabaseStatusSlotAnnotation" Description: ""
--     * Slot: id Description: 
--     * Slot: single_allele Description: 
--     * Slot: database_status Description: Database status of the allele
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AlleleFullNameSlotAnnotation" Description: "The one current full name for the allele."
--     * Slot: id Description: 
--     * Slot: single_allele Description: 
--     * Slot: name_type Description: The type of name: e.g., symbol, full_name, systematic_name, etc.
--     * Slot: format_text Description: A version of a synonym string using only ASCII characters, which is easier to type (for searches), print and parse. For example, Greek characters are transliterated.
--     * Slot: display_text Description: A version of a synonym string for display. Any UTF8 character is permitted.
--     * Slot: synonym_url Description: URL for a synonym: e.g., NCBI URL for the NCBI synonym of an object.
--     * Slot: synonym_scope Description: the scope of the synonym - permissible values are narrow / broad / related / exact
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AlleleFunctionalImpactSlotAnnotation" Description: ""
--     * Slot: id Description: 
--     * Slot: single_allele Description: 
--     * Slot: phenotype_term Description: For some MODs, the functional impact of an allele is reported specifically in the context of a particular phenotype. This slot is intended to capture the PhenotypeTerm.
--     * Slot: phenotype_statement Description: For some MODs, the functional impact of an allele is reported specifically in the context of a particular phenotype. This slot is intended to capture the free-text phenotype statement.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AlleleGermlineTransmissionStatusSlotAnnotation" Description: ""
--     * Slot: id Description: 
--     * Slot: single_allele Description: 
--     * Slot: germline_transmission_status Description: For alleles made in cell lines, have they been transmitted to the germline of an animal
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AlleleInheritanceModeSlotAnnotation" Description: ""
--     * Slot: id Description: 
--     * Slot: single_allele Description: 
--     * Slot: inheritance_mode Description: Mode of inheritance, e.g. dominant / semi-dominant / recessive / unknown / codominant
--     * Slot: phenotype_term Description: For some MODs, the inheritance mode of an allele is reported specifically in the context of a particular phenotype. This slot is intended to capture the phenotype ontology term.
--     * Slot: phenotype_statement Description: For some MODs, the inheritance mode of an allele is reported specifically in the context of a particular phenotype. This slot is intended to capture the free-text phenotype statement.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AlleleMolecularMutationSlotAnnotation" Description: ""
--     * Slot: id Description: 
--     * Slot: single_allele Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AlleleMutationTypeSlotAnnotation" Description: ""
--     * Slot: id Description: 
--     * Slot: single_allele Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AlleleNomenclatureEventSlotAnnotation" Description: ""
--     * Slot: id Description: 
--     * Slot: single_allele Description: 
--     * Slot: nomenclature_event Description: any of the kinds of changes made to an object's name or symbol
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AlleleNoteSlotAnnotation" Description: ""
--     * Slot: id Description: 
--     * Slot: single_allele Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: related_note_id Description: Holds between an object and a Note object.
-- # Class: "AlleleSecondaryIdSlotAnnotation" Description: ""
--     * Slot: id Description: 
--     * Slot: single_allele Description: 
--     * Slot: secondary_id Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AlleleSymbolSlotAnnotation" Description: "The one current symbol for the allele."
--     * Slot: id Description: 
--     * Slot: single_allele Description: 
--     * Slot: name_type Description: The type of name: e.g., symbol, full_name, systematic_name, etc.
--     * Slot: format_text Description: A version of a synonym string using only ASCII characters, which is easier to type (for searches), print and parse. For example, Greek characters are transliterated.
--     * Slot: display_text Description: A version of a synonym string for display. Any UTF8 character is permitted.
--     * Slot: synonym_url Description: URL for a synonym: e.g., NCBI URL for the NCBI synonym of an object.
--     * Slot: synonym_scope Description: the scope of the synonym - permissible values are narrow / broad / related / exact
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AlleleSynonymSlotAnnotation" Description: "All aliases (non-preferred names) for the allele. Any type of synonym is acceptable."
--     * Slot: id Description: 
--     * Slot: single_allele Description: 
--     * Slot: name_type Description: The type of name: e.g., symbol, full_name, systematic_name, etc.
--     * Slot: format_text Description: A version of a synonym string using only ASCII characters, which is easier to type (for searches), print and parse. For example, Greek characters are transliterated.
--     * Slot: display_text Description: A version of a synonym string for display. Any UTF8 character is permitted.
--     * Slot: synonym_url Description: URL for a synonym: e.g., NCBI URL for the NCBI synonym of an object.
--     * Slot: synonym_scope Description: the scope of the synonym - permissible values are narrow / broad / related / exact
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AlleleAlleleAssociation" Description: "Association between an allele and another allele"
--     * Slot: id Description: 
--     * Slot: evidence_code Description: 
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: related_note_id Description: Holds between an object and a Note object.
-- # Class: "AlleleCellLineAssociation" Description: "The relationship between an allele and a cell line.  Includes mutant/ embryonic stem cell lines known to carry the allele, and parental cell line of alleles made in embryonic stem cells."
--     * Slot: id Description: 
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AlleleConstructAssociation" Description: "The relationship between an allele and constructs contained in that allele."
--     * Slot: id Description: 
--     * Slot: evidence_code Description: 
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: related_note_id Description: Holds between an object and a Note object.
-- # Class: "AlleleGeneAssociation" Description: "Association between an allele and a gene"
--     * Slot: id Description: 
--     * Slot: evidence_code Description: 
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: related_note_id Description: Holds between an object and a Note object.
-- # Class: "AlleleGenerationMethodAssociation" Description: ""
--     * Slot: id Description: 
--     * Slot: mutation_target_strain Description: The particular strain (solely for and from MGI) that is targeted by the generation method for a particular allele.
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: object_id Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
-- # Class: "AlleleGenomicEntityAssociation" Description: "Association between an allele and a genomic entity"
--     * Slot: id Description: 
--     * Slot: evidence_code Description: 
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: related_note_id Description: Holds between an object and a Note object.
-- # Class: "AlleleImageAssociation" Description: "The relationship between an allele and an image."
--     * Slot: id Description: 
--     * Slot: primary_image Description: Can be null; if false, maybe you would show all the images. We need to revisit this issue.
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AlleleOriginAssociation" Description: "The relationship between an allele and the origin of the allele."
--     * Slot: id Description: 
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AlleleProteinAssociation" Description: "Association between an allele and a protein"
--     * Slot: id Description: 
--     * Slot: evidence_code Description: 
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: related_note_id Description: Holds between an object and a Note object.
-- # Class: "AlleleTranscriptAssociation" Description: "Association between an allele and a transcript"
--     * Slot: id Description: 
--     * Slot: evidence_code Description: 
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: related_note_id Description: Holds between an object and a Note object.
-- # Class: "AlleleVariantAssociation" Description: "The relationship between an allele and a variant is many to many. An Allele may have many variants and a variant can be present in many alleles."
--     * Slot: id Description: 
--     * Slot: evidence_code Description: 
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: related_note_id Description: Holds between an object and a Note object.
-- # Class: "PhenotypeAnnotation" Description: "An annotation asserting an association between a biological entity and a phenotype supported by evidence."
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: single_reference Description: The reference in which the phenotype association was asserted/reported.
--     * Slot: phenotype_term Description: The phenotype ontology term used to describe the phenotype of an organism or a set of organisms.
--     * Slot: subject Description: The biological entity (e.g. gene, allele, genotype) to which the phenotype is associated, by direct curation.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: phenotype statement: The label of an individual phenotype term from a phenotype ontology or the post-composed statement of the phenotype from a post-composed terminology
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date of curation at the source (MOD) database.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "GenePhenotypeAnnotation" Description: "An annotation asserting an association between a gene and a phenotype supported by evidence."
--     * Slot: sgd_strain_background Description: 
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: phenotype_term Description: The phenotype ontology term used to describe the phenotype of an organism or a set of organisms.
--     * Slot: subject Description: The gene to which the phenotype ontology term is associated.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AllelePhenotypeAnnotation" Description: "An annotation asserting an association between an allele and a phenotype supported by evidence."
--     * Slot: inferred_gene Description: The gene to which the phenotype is inferred to be associated.
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: phenotype_term Description: The phenotype ontology term used to describe the phenotype of an organism or a set of organisms.
--     * Slot: subject Description: The allele to which the phenotype ontology term is associated.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AGMPhenotypeAnnotation" Description: "An annotation asserting an association between an AGM and a phenotype supported by evidence."
--     * Slot: inferred_allele Description: The allele to which the phenotype is inferred to be associated.
--     * Slot: inferred_gene Description: The gene to which the phenotype is inferred to be associated.
--     * Slot: asserted_allele Description: The allele to which something is manually asserted to be associated.
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: phenotype_term Description: The phenotype ontology term used to describe the phenotype of an organism or a set of organisms.
--     * Slot: subject Description: The AGM to which the phenotype ontology term is associated.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "DiseaseAnnotation" Description: "An annotation asserting an association between a biological entity and a disease supported by evidence."
--     * Slot: curie Description: The Alliance-minted ID for the disease annotation. The ID is of the format AGRKB:100000000000001, where the first three digits represent the DiseaseAnnotation class code of "100", followed by a 12-digit identifier
--     * Slot: unique_id Description: Unique identifer for the disease annotation.  Will be generated at AGR if not submitted by the MOD.
--     * Slot: mod_entity_id Description: The model organism database (MOD) identifier/curie for the disease annotation. Currently only used by WormBase for disease annotations, e.g. "WBDOannot00000907"
--     * Slot: negated Description: The negative qualifier for the annotation.
--     * Slot: single_reference Description: The reference in which the disease association was asserted/reported.
--     * Slot: annotation_type Description: The type of annotation classified according to curation method. Submitted value should be a vocabulary term from the 'Annotation types' vocabulary
--     * Slot: genetic_sex Description: Submitted value should be a vocabulary term from the 'Genetic sexes' vocabulary
--     * Slot: disease_genetic_modifier Description: Specifies a genetic object that modifies the disease model. May be a gene, allele, AGM.
--     * Slot: disease_genetic_modifier_relation Description: A relation describing how the genetic modifier modifies the disease model. Submitted value should be a vocabulary term from the 'Disease genetic modifiers' vocabulary
--     * Slot: subject Description: The biological entity to which the disease ontology term is associated.
--     * Slot: predicate Description: Constrains the disease subject, associationType and inferredGeneAssociation.
--     * Slot: object Description: The disease ontology term.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: data_provider_id Description: Object representing the organization (e.g. MOD) from which the data was sourced and a CrossReference to that organisation's site
--     * Slot: secondary_data_provider_id Description: Object representing organization (e.g. MOD) that provided the data directly to the Alliance, but not the original source, and a CrossReference to that organisation's site
-- # Class: "DiseaseAnnotationDTO" Description: "Ingest class for association between a biological entity and a disease"
--     * Slot: id Description: 
--     * Slot: disease_relation_name Description: Name of term from 'Disease Relation Vocabulary' vocabulary
--     * Slot: do_term_curie Description: Curie of DOTerm describing the disease
--     * Slot: mod_entity_id Description: The model organism database (MOD) identifier/curie for the object
--     * Slot: negated Description: if set to true, then the association is negated i.e. is not true
--     * Slot: reference_curie Description: External reference curie used for ingest
--     * Slot: annotation_type_name Description: Name of the VocabularyTerm describing the annotation type selected from the 'Annotation types' Vocabulary
--     * Slot: genetic_sex_name Description: Name of term from the 'Genetic sexes' vocabulary
--     * Slot: disease_genetic_modifier_curie Description: Curie of BiologcalEntity that modifies the disease model
--     * Slot: disease_genetic_modifier_relation_name Description: Name of the VocabularyTerm that describes how the genetic modifier modifies the disease model, selected from the 'Disease genetic modifier relations' Vocabulary.
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: data_provider_dto_id Description: Ingest object representing the organization (e.g. MOD) from which the data was sourced and a CrossReference to that organisation's site
--     * Slot: secondary_data_provider_dto_id Description: Ingest object representing organization (e.g. MOD) that provided the data directly to the Alliance, but not the original source, and a CrossReference to that organisation's site
-- # Class: "GeneDiseaseAnnotation" Description: "An annotation asserting an association between a gene and a disease supported by evidence."
--     * Slot: sgd_strain_background Description: 
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: unique_id Description: A non-curie unique identifier for a thing.
--     * Slot: mod_entity_id Description: The model organism database (MOD) identifier/curie for the object
--     * Slot: negated Description: if set to true, then the association is negated i.e. is not true
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: annotation_type Description: The type of annotation classified according to curation method. Submitted value should be a vocabulary term from the 'Annotation types' vocabulary
--     * Slot: genetic_sex Description: Submitted value should be a vocabulary term from the 'Genetic sexes' vocabulary
--     * Slot: disease_genetic_modifier Description: Specifies a genetic object that modifies the disease model. May be a gene, allele, AGM.
--     * Slot: disease_genetic_modifier_relation Description: A relation describing how the genetic modifier modifies the disease model. Submitted value should be a vocabulary term from the 'Disease genetic modifiers' vocabulary
--     * Slot: subject Description: The gene to which the disease ontology term is associated.
--     * Slot: predicate Description: The relationship between gene and disease. Submitted value should be a vocabulary term from the 'Gene disease relations' vocabulary
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: data_provider_id Description: Object representing the organization (e.g. MOD) from which the data was sourced and a CrossReference to that organisation's site
--     * Slot: secondary_data_provider_id Description: Object representing organization (e.g. MOD) that provided the data directly to the Alliance, but not the original source, and a CrossReference to that organisation's site
-- # Class: "GeneDiseaseAnnotationDTO" Description: "Ingest class for an association between a gene and a disease"
--     * Slot: id Description: 
--     * Slot: gene_curie Description: 
--     * Slot: sgd_strain_background_curie Description: Curie of SGD strain background AGM
--     * Slot: disease_relation_name Description: Name of term from 'Disease Relation Vocabulary' vocabulary
--     * Slot: do_term_curie Description: Curie of DOTerm describing the disease
--     * Slot: mod_entity_id Description: The model organism database (MOD) identifier/curie for the object
--     * Slot: negated Description: if set to true, then the association is negated i.e. is not true
--     * Slot: reference_curie Description: External reference curie used for ingest
--     * Slot: annotation_type_name Description: Name of the VocabularyTerm describing the annotation type selected from the 'Annotation types' Vocabulary
--     * Slot: genetic_sex_name Description: Name of term from the 'Genetic sexes' vocabulary
--     * Slot: disease_genetic_modifier_curie Description: Curie of BiologcalEntity that modifies the disease model
--     * Slot: disease_genetic_modifier_relation_name Description: Name of the VocabularyTerm that describes how the genetic modifier modifies the disease model, selected from the 'Disease genetic modifier relations' Vocabulary.
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
--     * Slot: data_provider_dto_id Description: Ingest object representing the organization (e.g. MOD) from which the data was sourced and a CrossReference to that organisation's site
--     * Slot: secondary_data_provider_dto_id Description: Ingest object representing organization (e.g. MOD) that provided the data directly to the Alliance, but not the original source, and a CrossReference to that organisation's site
-- # Class: "AlleleDiseaseAnnotation" Description: "An annotation asserting an association between an allele and a disease supported by evidence."
--     * Slot: inferred_gene Description: The gene to which the disease is inferred to be associated.
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: unique_id Description: A non-curie unique identifier for a thing.
--     * Slot: mod_entity_id Description: The model organism database (MOD) identifier/curie for the object
--     * Slot: negated Description: if set to true, then the association is negated i.e. is not true
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: annotation_type Description: The type of annotation classified according to curation method. Submitted value should be a vocabulary term from the 'Annotation types' vocabulary
--     * Slot: genetic_sex Description: Submitted value should be a vocabulary term from the 'Genetic sexes' vocabulary
--     * Slot: disease_genetic_modifier Description: Specifies a genetic object that modifies the disease model. May be a gene, allele, AGM.
--     * Slot: disease_genetic_modifier_relation Description: A relation describing how the genetic modifier modifies the disease model. Submitted value should be a vocabulary term from the 'Disease genetic modifiers' vocabulary
--     * Slot: subject Description: The allele to which the disease ontology term is associated.
--     * Slot: predicate Description: The relationship between allele and disease. Submitted value should be a vocabulary term from the 'Allele disease relations' vocabulary
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: data_provider_id Description: Object representing the organization (e.g. MOD) from which the data was sourced and a CrossReference to that organisation's site
--     * Slot: secondary_data_provider_id Description: Object representing organization (e.g. MOD) that provided the data directly to the Alliance, but not the original source, and a CrossReference to that organisation's site
-- # Class: "AlleleDiseaseAnnotationDTO" Description: "Ingest class for an association between an allele and a disease"
--     * Slot: id Description: 
--     * Slot: allele_curie Description: 
--     * Slot: inferred_gene_curie Description: Curie of gene to which something is inferred to be associated via an automated pipeline
--     * Slot: disease_relation_name Description: Name of term from 'Disease Relation Vocabulary' vocabulary
--     * Slot: do_term_curie Description: Curie of DOTerm describing the disease
--     * Slot: mod_entity_id Description: The model organism database (MOD) identifier/curie for the object
--     * Slot: negated Description: if set to true, then the association is negated i.e. is not true
--     * Slot: reference_curie Description: External reference curie used for ingest
--     * Slot: annotation_type_name Description: Name of the VocabularyTerm describing the annotation type selected from the 'Annotation types' Vocabulary
--     * Slot: genetic_sex_name Description: Name of term from the 'Genetic sexes' vocabulary
--     * Slot: disease_genetic_modifier_curie Description: Curie of BiologcalEntity that modifies the disease model
--     * Slot: disease_genetic_modifier_relation_name Description: Name of the VocabularyTerm that describes how the genetic modifier modifies the disease model, selected from the 'Disease genetic modifier relations' Vocabulary.
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
--     * Slot: data_provider_dto_id Description: Ingest object representing the organization (e.g. MOD) from which the data was sourced and a CrossReference to that organisation's site
--     * Slot: secondary_data_provider_dto_id Description: Ingest object representing organization (e.g. MOD) that provided the data directly to the Alliance, but not the original source, and a CrossReference to that organisation's site
-- # Class: "AGMDiseaseAnnotation" Description: "An annotation asserting an association between an AGM and a disease supported by evidence."
--     * Slot: inferred_allele Description: The allele to which the disease is inferred to be associated.
--     * Slot: inferred_gene Description: The gene to which the disease is inferred to be associated.
--     * Slot: asserted_allele Description: The allele to which something is manually asserted to be associated.
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: unique_id Description: A non-curie unique identifier for a thing.
--     * Slot: mod_entity_id Description: The model organism database (MOD) identifier/curie for the object
--     * Slot: negated Description: if set to true, then the association is negated i.e. is not true
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: annotation_type Description: The type of annotation classified according to curation method. Submitted value should be a vocabulary term from the 'Annotation types' vocabulary
--     * Slot: genetic_sex Description: Submitted value should be a vocabulary term from the 'Genetic sexes' vocabulary
--     * Slot: disease_genetic_modifier Description: Specifies a genetic object that modifies the disease model. May be a gene, allele, AGM.
--     * Slot: disease_genetic_modifier_relation Description: A relation describing how the genetic modifier modifies the disease model. Submitted value should be a vocabulary term from the 'Disease genetic modifiers' vocabulary
--     * Slot: subject Description: The AGM to which the disease ontology term is associated.
--     * Slot: predicate Description: The relationship between AGM and disease. Submitted value should be a vocabulary term from the 'AGM disease relations' vocabulary
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: data_provider_id Description: Object representing the organization (e.g. MOD) from which the data was sourced and a CrossReference to that organisation's site
--     * Slot: secondary_data_provider_id Description: Object representing organization (e.g. MOD) that provided the data directly to the Alliance, but not the original source, and a CrossReference to that organisation's site
-- # Class: "AGMDiseaseAnnotationDTO" Description: "Ingest class for an association between an AGM and a disease"
--     * Slot: id Description: 
--     * Slot: agm_curie Description: 
--     * Slot: inferred_gene_curie Description: Curie of gene to which something is inferred to be associated via an automated pipeline
--     * Slot: inferred_allele_curie Description: Curie of allele to which something is inferred to be associated via an automated pipeline
--     * Slot: asserted_allele_curie Description: Curie of the allele to which something is manually asserted to be associated
--     * Slot: disease_relation_name Description: Name of term from 'Disease Relation Vocabulary' vocabulary
--     * Slot: do_term_curie Description: Curie of DOTerm describing the disease
--     * Slot: mod_entity_id Description: The model organism database (MOD) identifier/curie for the object
--     * Slot: negated Description: if set to true, then the association is negated i.e. is not true
--     * Slot: reference_curie Description: External reference curie used for ingest
--     * Slot: annotation_type_name Description: Name of the VocabularyTerm describing the annotation type selected from the 'Annotation types' Vocabulary
--     * Slot: genetic_sex_name Description: Name of term from the 'Genetic sexes' vocabulary
--     * Slot: disease_genetic_modifier_curie Description: Curie of BiologcalEntity that modifies the disease model
--     * Slot: disease_genetic_modifier_relation_name Description: Name of the VocabularyTerm that describes how the genetic modifier modifies the disease model, selected from the 'Disease genetic modifier relations' Vocabulary.
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
--     * Slot: data_provider_dto_id Description: Ingest object representing the organization (e.g. MOD) from which the data was sourced and a CrossReference to that organisation's site
--     * Slot: secondary_data_provider_dto_id Description: Ingest object representing organization (e.g. MOD) that provided the data directly to the Alliance, but not the original source, and a CrossReference to that organisation's site
-- # Class: "ExperimentalCondition" Description: "The environmental context in which an experiment is carried out. This may (e.g. drug treatment) or may not (e.g. standard conditions) directly influence the outcome of the experiment."
--     * Slot: id Description: 
--     * Slot: unique_id Description: Unique identifer for the experimental condition.  Will be generated at AGR.
--     * Slot: condition_class Description: The ZECO ID that represents the high level condition grouping term.  This will come from a slim in the ZECO, called 'AllianceSlim'.
--     * Slot: condition_summary Description: Free text describing the environmental/experimental condition. For some groups this is a single term, others is it is a concatenation of the term names from the ontologies included in this data structure. The condition_summary will not be submitted by DQMs but rather generated at the Alliance after ingest (or generated/updated in the curation interface and persistent store).
--     * Slot: condition_id Description: The specific ontology ID for the condition when that is not covered by any of the other condition ontology ID attributes (chemical, NCBITaxon, anatomical). This could also be another ZECO term if the ZECO term that describes this condition is more specific, or outside the conditionClassId slim.
--     * Slot: condition_free_text Description: Free-text description of the experimental condition
--     * Slot: condition_quantity Description: Optional free text field that records the units/amount/degrees of a condition.
--     * Slot: condition_anatomy Description: Anatomical ontology identifier used in cases like regeneration/wounding.
--     * Slot: condition_gene_ontology Description: Gene Ontology id used in subset of condition types.
--     * Slot: condition_taxon Description: NCBITaxon ontology id used in subset of condition types like 'bacterial infection'.
--     * Slot: condition_chemical Description: ChEBI or molecular ontology id used in subset of condition terms.  ie: the specific chemcial used in conjunction with 'chemical condition'.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "ExperimentalConditionDTO" Description: "Ingest class for describing the environmental context in which an experiment is carried out"
--     * Slot: id Description: 
--     * Slot: condition_class_curie Description: Curie of ZECOTerm describing condition class
--     * Slot: condition_id_curie Description: Curie of ExperimentalConditionOntologyTerm describing condition
--     * Slot: condition_free_text Description: Free-text description of the experimental condition
--     * Slot: condition_quantity Description: 
--     * Slot: condition_anatomy_curie Description: Curie of AnatomicalTerm associated with condition
--     * Slot: condition_gene_ontology_curie Description: Curie of GOTerm associated with condition
--     * Slot: condition_taxon_curie Description: Curie of NCBITaxonTerm associated with condition
--     * Slot: condition_chemical_curie Description: Curie of ChemicalTerm associated with condition
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: ConditionRelationDTO_id Description: Autocreated FK slot
-- # Class: "ConditionRelation" Description: "A pairing of an experimental condition relation (i.e. has_condition) with a list of 1 or more ExperimentalCondition objects. Annotation objects can connect directly to a set of 0 or more of these ConditionRelation objects via a 'condition_relations' slot to express the experimental conditions relevant to the annotation."
--     * Slot: id Description: 
--     * Slot: unique_id Description: Unique identifer for the condition relation.  Will be generated at AGR.
--     * Slot: handle Description: A slot pointing to a free-text alias or 'handle' for a data object, such as a reference-specific alias for a data object used while curating.
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: condition_relation_type Description: Submitted value should be a vocabulary term from the 'Condition relation types' vocabulary
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "ConditionRelationDTO" Description: "Ingest class for the pairing of an experimental condition relation with a list of one or more conditions"
--     * Slot: id Description: 
--     * Slot: handle Description: A slot pointing to a free-text alias or 'handle' for a data object, such as a reference-specific alias for a data object used while curating.
--     * Slot: reference_curie Description: External reference curie used for ingest
--     * Slot: condition_relation_type_name Description: Name of VocabularyTerm from 'Condition relation types' vocabulary
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: DiseaseAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: GeneDiseaseAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: AlleleDiseaseAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: AGMDiseaseAnnotationDTO_id Description: Autocreated FK slot
-- # Class: "AlleleDTO" Description: "Ingest class for an Allele object"
--     * Slot: in_collection_name Description: Name of VocabularyTerm describing the collection from the 'Allele collection vocabulary' Vocabulary
--     * Slot: laboratory_of_origin_curie Description: The curie of the laboratory of origin for the entity.
--     * Slot: is_extinct Description: Does the allele still exist in a population somewhere?
--     * Slot: is_extrachromosomal Description: Used by WormBase to indicate whether a transgenic allele is known to be extrachromosomal.
--     * Slot: is_integrated Description: Used by WormBase to indicate whether a transgenic allele is known to be integrated into the genome.
--     * Slot: transgene_chromosome_location_curie Description: The curie string of the chromosome to which a transgene has been mapped. Used for WormBase transgenes that have been integrated into the genome and mapped to a chromosome.
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon_curie Description: Curie of the NCBITaxonTerm representing the taxon from which the biological entity derives
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
--     * Slot: allele_symbol_dto_id Description: The one current accepted symbol for the allele: e.g., wg<sup>1</sup>.
--     * Slot: allele_full_name_dto_id Description: The one current full name for an allele: e.g., wg<sup>1</sup>.
--     * Slot: allele_germline_transmission_status_dto_id Description: 
--     * Slot: allele_database_status_dto_id Description: 
-- # Class: "CellLineDTO" Description: "Dummy cell line DTO class"
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon_curie Description: Curie of the NCBITaxonTerm representing the taxon from which the biological entity derives
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "ConstructDTO" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon_curie Description: Curie of the NCBITaxonTerm representing the taxon from which the biological entity derives
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "GenerationMethodDTO" Description: ""
--     * Slot: id Description: 
--     * Slot: mutagenesis_target Description: The target of the mutation, e.g. strain / adult females / adult males / embryos / sperm / not specified
--     * Slot: integration_method_name Description: WormBase captures the method by which an extrachromosomal transgene was integrated into the genome.
--     * Slot: chemical_mutagen_name Description: The name of the chemical used to generate the mutation through mutagenesis
--     * Slot: irradiation_mutagen_name Description: The name of the irradiation used to generate the mutation through mutagenesis
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "SequenceTargetingReagentDTO" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon_curie Description: Curie of the NCBITaxonTerm representing the taxon from which the biological entity derives
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
-- # Class: "AlleleDatabaseStatusSlotAnnotationDTO" Description: ""
--     * Slot: id Description: 
--     * Slot: database_status_name Description: Name of the VocabularyTerm describing the database status
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AlleleFunctionalImpactSlotAnnotationDTO" Description: ""
--     * Slot: id Description: 
--     * Slot: phenotype_term_curie Description: The string representation of the phenotype ontology term (PhenotypeTerm) curie
--     * Slot: phenotype_statement Description: For some MODs, the functional impact of an allele is reported specifically in the context of a particular phenotype. This slot is intended to capture the free-text phenotype statement.
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: AlleleDTO_curie Description: Autocreated FK slot
-- # Class: "AlleleGermlineTransmissionStatusSlotAnnotationDTO" Description: ""
--     * Slot: id Description: 
--     * Slot: germline_transmission_status_name Description: Name of the VocabularyTerm representing the germline transmission status
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AlleleInheritanceModeSlotAnnotationDTO" Description: ""
--     * Slot: id Description: 
--     * Slot: inheritance_mode_name Description: Name of VocabularyTerm describing the inheritance mode from the 'Allele inheritance mode vocabulary', e.g. dominant / semi-dominant / recessive / unknown / codominant
--     * Slot: phenotype_term_curie Description: For some MODs, the inheritance mode of an allele is reported specifically in the context of a particular phenotype. This slot is intended to capture the phenotype ontology term.
--     * Slot: phenotype_statement Description: For some MODs, the inheritance mode of an allele is reported specifically in the context of a particular phenotype. This slot is intended to capture the free-text phenotype statement.
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: AlleleDTO_curie Description: Autocreated FK slot
-- # Class: "AlleleMolecularMutationSlotAnnotationDTO" Description: ""
--     * Slot: id Description: 
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: AlleleDTO_curie Description: Autocreated FK slot
-- # Class: "AlleleMutationTypeSlotAnnotationDTO" Description: ""
--     * Slot: id Description: 
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: AlleleDTO_curie Description: Autocreated FK slot
-- # Class: "AlleleNomenclatureEventSlotAnnotationDTO" Description: ""
--     * Slot: id Description: 
--     * Slot: nomenclature_event_name Description: Name of the VocabularyTerm describing the nomenclature event
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: AlleleDTO_curie Description: Autocreated FK slot
-- # Class: "AlleleNoteSlotAnnotationDTO" Description: ""
--     * Slot: id Description: 
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: AlleleDTO_curie Description: Autocreated FK slot
--     * Slot: note_dto_id Description: 
-- # Class: "AlleleSecondaryIdSlotAnnotationDTO" Description: ""
--     * Slot: id Description: 
--     * Slot: secondary_id Description: 
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: AlleleDTO_curie Description: Autocreated FK slot
-- # Class: "AlleleAlleleAssociationDTO" Description: "Association between an allele and another allele"
--     * Slot: id Description: 
--     * Slot: object_allele_curie Description: The curie of the allele that is acting as the object of an AlleleAlleleAssociation
--     * Slot: allele_curie Description: 
--     * Slot: predicate_name Description: Name of VocabularyTerm representing predicate of an Association
--     * Slot: evidence_code_curie Description: Curie of ECOTerm
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: note_dto_id Description: 
-- # Class: "AlleleCellLineAssociationDTO" Description: "The relationship between an allele and a cell line.  Includes mutant/ embryonic stem cell lines known to carry the allele, and parental cell line of alleles made in embryonic stem cells."
--     * Slot: id Description: 
--     * Slot: allele_curie Description: 
--     * Slot: predicate_name Description: Name of VocabularyTerm representing predicate of an Association
--     * Slot: cell_line_curie Description: 
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
-- # Class: "AlleleConstructAssociationDTO" Description: "The relationship between an allele and constructs contained in that allele."
--     * Slot: id Description: 
--     * Slot: construct_curie Description: 
--     * Slot: allele_curie Description: 
--     * Slot: predicate_name Description: Name of VocabularyTerm representing predicate of an Association
--     * Slot: evidence_code_curie Description: Curie of ECOTerm
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
--     * Slot: note_dto_id Description: 
-- # Class: "AlleleGeneAssociationDTO" Description: "Association between an allele and a gene"
--     * Slot: id Description: 
--     * Slot: gene_curie Description: 
--     * Slot: allele_curie Description: 
--     * Slot: predicate_name Description: Name of VocabularyTerm representing predicate of an Association
--     * Slot: evidence_code_curie Description: Curie of ECOTerm
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
--     * Slot: note_dto_id Description: 
-- # Class: "AlleleGenerationMethodAssociationDTO" Description: ""
--     * Slot: id Description: 
--     * Slot: allele_curie Description: 
--     * Slot: predicate_name Description: Name of VocabularyTerm representing predicate of an Association
--     * Slot: mutation_target_strain_curie Description: Curie of the particular strain that is targeted by the generation method for a particular allele (MGI only)
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
--     * Slot: generation_method_dto_id Description: 
-- # Class: "AlleleGenomicEntityAssociationDTO" Description: ""
--     * Slot: id Description: 
--     * Slot: allele_curie Description: 
--     * Slot: predicate_name Description: Name of VocabularyTerm representing predicate of an Association
--     * Slot: evidence_code_curie Description: Curie of ECOTerm
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: note_dto_id Description: 
-- # Class: "AlleleImageAssociationDTO" Description: "The relationship between an allele and an image."
--     * Slot: id Description: 
--     * Slot: allele_curie Description: 
--     * Slot: predicate_name Description: Name of VocabularyTerm representing predicate of an Association
--     * Slot: image_curie Description: 
--     * Slot: primary_image Description: Can be null; if false, maybe you would show all the images. We need to revisit this issue.
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
-- # Class: "AlleleOriginAssociationDTO" Description: "The relationship between an allele and the AGM origin of the allele."
--     * Slot: id Description: 
--     * Slot: allele_curie Description: 
--     * Slot: predicate_name Description: Name of VocabularyTerm representing predicate of an Association
--     * Slot: agm_curie Description: 
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
-- # Class: "AlleleProteinAssociationDTO" Description: "Association between an allele and a protein"
--     * Slot: id Description: 
--     * Slot: protein_curie Description: 
--     * Slot: allele_curie Description: 
--     * Slot: predicate_name Description: Name of VocabularyTerm representing predicate of an Association
--     * Slot: evidence_code_curie Description: Curie of ECOTerm
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
--     * Slot: note_dto_id Description: 
-- # Class: "AlleleTranscriptAssociationDTO" Description: "Association between an allele and a transcript"
--     * Slot: id Description: 
--     * Slot: transcript_curie Description: 
--     * Slot: allele_curie Description: 
--     * Slot: predicate_name Description: Name of VocabularyTerm representing predicate of an Association
--     * Slot: evidence_code_curie Description: Curie of ECOTerm
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
--     * Slot: note_dto_id Description: 
-- # Class: "AlleleVariantAssociationDTO" Description: "The relationship between an allele and a variant is many to many. An Allele may have many variants and a variant can be present in many alleles."
--     * Slot: id Description: 
--     * Slot: variant_curie Description: 
--     * Slot: allele_curie Description: 
--     * Slot: predicate_name Description: Name of VocabularyTerm representing predicate of an Association
--     * Slot: evidence_code_curie Description: Curie of ECOTerm
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
--     * Slot: note_dto_id Description: 
-- # Class: "AuditedObject" Description: "Base class for all other LinkML classes. Some entity for which changes are tracked, including date/time of change, the agent responsible for the change, and whether the entity is internal (private)."
--     * Slot: id Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AuditedObjectDTO" Description: "Base class for all other LinkML DTO classes."
--     * Slot: id Description: 
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "BiologicalEntity" Description: "An entity of biological origin that can be unambiguously attributed to a single species."
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "BiologicalEntityDTO" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon_curie Description: Curie of the NCBITaxonTerm representing the taxon from which the biological entity derives
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "GenomicEntity" Description: "An entity that is part of a genome (i.e. segment of the DNA molecule), is derived directly from the genome (i.e. RNA transcript molecule), or is derived indirectly from the genome (i.e. polypeptide or protein via RNA transcript translation)."
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "GenomicEntityDTO" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon_curie Description: Curie of the NCBITaxonTerm representing the taxon from which the biological entity derives
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Transcript" Description: "Placeholder."
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "CrossReference" Description: ""
--     * Slot: id Description: 
--     * Slot: referenced_curie Description: Curie of the thing being referenced in a CrossReference
--     * Slot: display_name Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: resource_descriptor_page_id Description: 
-- # Class: "CrossReferenceDTO" Description: ""
--     * Slot: id Description: 
--     * Slot: referenced_curie Description: Curie of the thing being referenced in a CrossReference
--     * Slot: page_area Description: 
--     * Slot: display_name Description: 
--     * Slot: prefix Description: Denormalization to help with classifying types of crossReferences, distinguishing DOIs from PMC ids, etc.
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: AlleleDTO_curie Description: Autocreated FK slot
--     * Slot: CellLineDTO_curie Description: Autocreated FK slot
--     * Slot: ConstructDTO_curie Description: Autocreated FK slot
--     * Slot: SequenceTargetingReagentDTO_curie Description: Autocreated FK slot
--     * Slot: GenomicEntityDTO_curie Description: Autocreated FK slot
--     * Slot: AffectedGenomicModelDTO_curie Description: Autocreated FK slot
--     * Slot: GeneDTO_curie Description: Autocreated FK slot
-- # Class: "DataProvider" Description: ""
--     * Slot: id Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: source_organization_id Description: 
--     * Slot: cross_reference_id Description: 
-- # Class: "DataProviderDTO" Description: ""
--     * Slot: id Description: 
--     * Slot: source_organization_abbreviation Description: 
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: cross_reference_dto_id Description: 
-- # Class: "Note" Description: "Note object for capturing free-text describing some attribute of an entity, coupled with a 'note type', internal boolean, and an optional list of references. Permissible values for note_type can be viewed and managed in the A-Team curation UI Controlled Vocabulary Terms Table."
--     * Slot: id Description: 
--     * Slot: free_text Description: A free text string that describes some aspect of an entity.
--     * Slot: note_type Description: The type of note: e.g., cytology, comment, summary. Permissible values for 'note_type' currently = disease_summary, disease_note
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "NoteDTO" Description: ""
--     * Slot: id Description: 
--     * Slot: free_text Description: A free text string that describes some aspect of an entity.
--     * Slot: note_type_name Description: Name of VocabularyTerm representing note type selected from the appropriate Vocabulary
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: DiseaseAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: GeneDiseaseAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: AlleleDiseaseAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: AGMDiseaseAnnotationDTO_id Description: Autocreated FK slot
-- # Class: "SlotAnnotation" Description: "SlotAnnotation classes should be used when we need to attach metadata (in particular evidence and provenance) to a slot in the context of its referencing class, that can not be fully captured using an Association between the full class itself, and an InformationContentEntity. Evidence and provenance can exist here in the form of an evidence code, a publication, a personal communication or any other kind of InformationContentEntity. SlotAnnotation classes are used where the slot is not referencing a class in and of itself, and often has a scalar range."
--     * Slot: id Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "SlotAnnotationDTO" Description: ""
--     * Slot: id Description: 
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "NameSlotAnnotation" Description: "Some symbol or name for an object, including current names as well as aliases, with accompanying metadata. The entity to which the symbol/name applies is specified in objects that inherit from this object."
--     * Slot: id Description: 
--     * Slot: name_type Description: The type of name: e.g., symbol, full_name, systematic_name, etc.
--     * Slot: format_text Description: A version of a synonym string using only ASCII characters, which is easier to type (for searches), print and parse. For example, Greek characters are transliterated.
--     * Slot: display_text Description: A version of a synonym string for display. Any UTF8 character is permitted.
--     * Slot: synonym_url Description: URL for a synonym: e.g., NCBI URL for the NCBI synonym of an object.
--     * Slot: synonym_scope Description: the scope of the synonym - permissible values are narrow / broad / related / exact
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "NameSlotAnnotationDTO" Description: ""
--     * Slot: id Description: 
--     * Slot: name_type_name Description: Name of the VocabularyTerm representing the name type of the synonym - proposed values are nomenclature_symbol / full_name / systematic_name / ncbi_protein_name / uniform / non_uniform / retired_name / unspecified
--     * Slot: format_text Description: A version of a synonym string using only ASCII characters, which is easier to type (for searches), print and parse. For example, Greek characters are transliterated.
--     * Slot: display_text Description: A version of a synonym string for display. Any UTF8 character is permitted.
--     * Slot: synonym_url Description: URL for a synonym: e.g., NCBI URL for the NCBI synonym of an object.
--     * Slot: synonym_scope_name Description: Name of the VocabularyTerm representing the scope of the synonym - permissible values are narrow / broad / related / exact
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: AlleleDTO_curie Description: Autocreated FK slot
--     * Slot: GeneDTO_curie Description: Autocreated FK slot
-- # Class: "SymbolSlotAnnotationDTO" Description: ""
--     * Slot: id Description: 
--     * Slot: name_type_name Description: Name of the VocabularyTerm representing the name type of the synonym - proposed values are nomenclature_symbol / full_name / systematic_name / ncbi_protein_name / uniform / non_uniform / retired_name / unspecified
--     * Slot: format_text Description: A version of a synonym string using only ASCII characters, which is easier to type (for searches), print and parse. For example, Greek characters are transliterated.
--     * Slot: display_text Description: A version of a synonym string for display. Any UTF8 character is permitted.
--     * Slot: synonym_url Description: URL for a synonym: e.g., NCBI URL for the NCBI synonym of an object.
--     * Slot: synonym_scope_name Description: Name of the VocabularyTerm representing the scope of the synonym - permissible values are narrow / broad / related / exact
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "FullNameSlotAnnotationDTO" Description: ""
--     * Slot: id Description: 
--     * Slot: name_type_name Description: Name of the VocabularyTerm representing the name type of the synonym - proposed values are nomenclature_symbol / full_name / systematic_name / ncbi_protein_name / uniform / non_uniform / retired_name / unspecified
--     * Slot: format_text Description: A version of a synonym string using only ASCII characters, which is easier to type (for searches), print and parse. For example, Greek characters are transliterated.
--     * Slot: display_text Description: A version of a synonym string for display. Any UTF8 character is permitted.
--     * Slot: synonym_url Description: URL for a synonym: e.g., NCBI URL for the NCBI synonym of an object.
--     * Slot: synonym_scope_name Description: Name of the VocabularyTerm representing the scope of the synonym - permissible values are narrow / broad / related / exact
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "SystematicNameSlotAnnotationDTO" Description: ""
--     * Slot: id Description: 
--     * Slot: name_type_name Description: Name of the VocabularyTerm representing the name type of the synonym - proposed values are nomenclature_symbol / full_name / systematic_name / ncbi_protein_name / uniform / non_uniform / retired_name / unspecified
--     * Slot: format_text Description: A version of a synonym string using only ASCII characters, which is easier to type (for searches), print and parse. For example, Greek characters are transliterated.
--     * Slot: display_text Description: A version of a synonym string for display. Any UTF8 character is permitted.
--     * Slot: synonym_url Description: URL for a synonym: e.g., NCBI URL for the NCBI synonym of an object.
--     * Slot: synonym_scope_name Description: Name of the VocabularyTerm representing the scope of the synonym - permissible values are narrow / broad / related / exact
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Association" Description: "A typed association between two entities, supported by evidence.  Associations have three base slots: subject, object, and predicate, but they can have any number of additional attributes that help qualify the relationship between the subject and the object.  The subject is the curie (or identifier) of the class that is the subject of the association, and likewise the object is the curie (or identifier of the class that is the object. The relationship between subject and object is defined by the predicate slot (which can also be constrained using the range of the predicate)."
--     * Slot: id Description: 
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Chromosome" Description: "The ID of the landmark used to establish the coordinate system for the current feature."
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Assembly" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "GenomicLocationAssociation" Description: ""
--     * Slot: id Description: 
--     * Slot: has_assembly Description: 
--     * Slot: start Description: The start of the feature in positive 1-based integer coordinates
--     * Slot: end Description: The end of the feature in positive 1-based integer coordinates
--     * Slot: subject Description: subject should be a genomic entity
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: object should be the chromosome identifier
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "GenomicLocationAssociationDTO" Description: ""
--     * Slot: id Description: 
--     * Slot: genomic_entity_curie Description: 
--     * Slot: predicate_name Description: Name of VocabularyTerm representing predicate of an Association
--     * Slot: chromosome_curie Description: 
--     * Slot: assembly_curie Description: 
--     * Slot: start Description: The start of the feature in positive 1-based integer coordinates
--     * Slot: end Description: The end of the feature in positive 1-based integer coordinates
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: AlleleDTO_curie Description: Autocreated FK slot
--     * Slot: CellLineDTO_curie Description: Autocreated FK slot
--     * Slot: ConstructDTO_curie Description: Autocreated FK slot
--     * Slot: SequenceTargetingReagentDTO_curie Description: Autocreated FK slot
--     * Slot: GenomicEntityDTO_curie Description: Autocreated FK slot
--     * Slot: AffectedGenomicModelDTO_curie Description: Autocreated FK slot
--     * Slot: GeneDTO_curie Description: Autocreated FK slot
--     * Slot: Ingest_id Description: Autocreated FK slot
-- # Class: "Protein" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Identifier" Description: ""
--     * Slot: counter Description: a number to identify an alliance resource in a subdomain
--     * Slot: subdomain_code Description: a three letter string, representing a subdomain (e.g 101 represents disease_annotation)
--     * Slot: subdomain_name Description: subdomain name (e.g disease_annotation)
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
-- # Class: "IdentifiersRange" Description: ""
--     * Slot: id Description: 
--     * Slot: first Description: first identifier in a range
--     * Slot: last Description: last identifier in a range
-- # Class: "ResourceDescriptor" Description: ""
--     * Slot: id Description: 
--     * Slot: prefix Description: Denormalization to help with classifying types of crossReferences, distinguishing DOIs from PMC ids, etc.
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: id_pattern Description: Regex for the expected format of the ID
--     * Slot: id_example Description: Example ID for the resource that fits the pattern described by the id_pattern slot
--     * Slot: default_url_template Description: Default URL template for the resource
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "ResourceDescriptorPage" Description: ""
--     * Slot: id Description: 
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: url_template Description: URL template for constructing link to resource using prodived ID, eg. "https://www.omim.org/phenotypicSeries/[%s]"
--     * Slot: page_description Description: Description of page
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AffectedGenomicModel" Description: "Includes inbred strains, stocks, disease models and mutant genotypes"
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: subtype Description: Subtype of affected genomic model - permissible values: strain / genotype / fish
--     * Slot: parental_populations Description: 
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: data_provider_id Description: Object representing the organization (e.g. MOD) from which the data was sourced and a CrossReference to that organisation's site
-- # Class: "AffectedGenomicModelDTO" Description: "Ingest class for AGMs"
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: subtype_name Description: Name of VocabularyTerm describing subtype - permissible values: strain / genotype / fish
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon_curie Description: Curie of the NCBITaxonTerm representing the taxon from which the biological entity derives
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
--     * Slot: data_provider_dto_id Description: Ingest object representing the organization (e.g. MOD) from which the data was sourced and a CrossReference to that organisation's site
-- # Class: "AffectedGenomicModelComponent" Description: "Allele that affects the model and its zygosity"
--     * Slot: id Description: 
--     * Slot: single_allele Description: 
--     * Slot: zygosity Description: GENO onotology ID for allele zygosity
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AffectedGenomicModelComponentDTO" Description: ""
--     * Slot: id Description: 
--     * Slot: allele_curie Description: 
--     * Slot: zygosity_curie Description: Curie of GENO ontology ID for allele zygosity - permissible_values: GENO:0000602 / GENO:0000603 / GENO:0000604 / GENO:0000605 / GENO:0000606 / GENO:0000135 / GENO:0000136 / GENO:0000137 / GENO:0000134
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: AffectedGenomicModelDTO_curie Description: Autocreated FK slot
-- # Class: "VocabularyTerm" Description: "A concept or class in a simple vocabulary."
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: abbreviation Description: 
--     * Slot: definition Description: The explanation of the meaning of a term.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Vocabulary" Description: "A set of VocabularyTerm objects."
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: vocabulary_description Description: The free text description of a Vocabulary including its intended use.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "VocabularyTermSet" Description: "A subset of terms from a Vocabulary that are valid for particular applications"
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: vocabulary_term_set_vocabulary Description: The Vocabulary from which the terms contained in theVocabularyTermSet belong
--     * Slot: vocabulary_term_set_description Description: The free text description of a VocabularyTermSet including its intended use.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Figure" Description: "An entity representing a figure or table in a publication."
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: label Description: A short display name for the figure. For example: Figure 2, Figure 3B
--     * Slot: caption Description: Text describing the contents of a figure or table in a publication.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "File" Description: "A dummy object."
--     * Slot: id Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Agent" Description: "An individual, group, organization or project that provides information and/or materials."
--     * Slot: id Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Organization" Description: "An organization that provides information and/or materials to the Alliance. This includes Alliance member organizations (see AllianceMember subclass)."
--     * Slot: id Description: 
--     * Slot: abbreviation Description: 
--     * Slot: full_name Description: The full name of the Organization. e.g. Mouse Genome Database, FlyBase, Online Mendelian Inheritance of Man
--     * Slot: short_name Description: The short name of the organization. For Alliance Members, this is the short name used in the Members list on the website. e.g. MGD, FB, OMIM
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: homepage_resource_descriptor_page_id Description: ResourceDescriptorPage containing URL template for organization's homepage
-- # Class: "Laboratory" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: abbreviation Description: 
--     * Slot: full_name Description: The full name of the Organization. e.g. Mouse Genome Database, FlyBase, Online Mendelian Inheritance of Man
--     * Slot: short_name Description: The short name of the organization. For Alliance Members, this is the short name used in the Members list on the website. e.g. MGD, FB, OMIM
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: homepage_resource_descriptor_page_id Description: ResourceDescriptorPage containing URL template for organization's homepage
-- # Class: "Company" Description: ""
--     * Slot: id Description: 
--     * Slot: abbreviation Description: 
--     * Slot: full_name Description: The full name of the Organization. e.g. Mouse Genome Database, FlyBase, Online Mendelian Inheritance of Man
--     * Slot: short_name Description: The short name of the organization. For Alliance Members, this is the short name used in the Members list on the website. e.g. MGD, FB, OMIM
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: homepage_resource_descriptor_page_id Description: ResourceDescriptorPage containing URL template for organization's homepage
-- # Class: "Person" Description: ""
--     * Slot: last_name Description: last (family) name of a person
--     * Slot: middle_name Description: middle names of a person
--     * Slot: first_name Description: first name of a person
--     * Slot: orcid Description: Open Researcher and Contributor ID
--     * Slot: mod_entity_id Description: The model organism database (MOD) identifier/curie for the object
--     * Slot: unique_id Description: A non-curie unique identifier for a thing.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: affiliated_alliance_member_id Description: The Alliance Member the person is affiliated with
-- # Class: "LoggedInPerson" Description: ""
--     * Slot: okta_id Description: The Okta identifier for the person registered in Okta for user authentication
--     * Slot: okta_email Description: The email address of the LoggedInPerson registered with Okta for user authentication
--     * Slot: user_settings Description: JSON Blob containing details of UI settings for LoggedInPerson
--     * Slot: api_token Description: The API token of the LoggedInPerson for the curation system
--     * Slot: last_name Description: last (family) name of a person
--     * Slot: middle_name Description: middle names of a person
--     * Slot: first_name Description: first name of a person
--     * Slot: orcid Description: Open Researcher and Contributor ID
--     * Slot: mod_entity_id Description: The model organism database (MOD) identifier/curie for the object
--     * Slot: unique_id Description: A non-curie unique identifier for a thing.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: affiliated_alliance_member_id Description: The Alliance Member the person is affiliated with
-- # Class: "AllianceMember" Description: "An organization that is a member of the Alliance of Genome Resources."
--     * Slot: id Description: 
--     * Slot: alliance_member_id Description: An integer referring to an AllianceMember object in the AllianceMember/MOD database table. It's a primary key in the AllianceMember/MOD table, a foreign key if used in other tables.
--     * Slot: abbreviation Description: The curie prefix, or letter code used by FMS (Alliance file management system).  e.g. MGI, FB
--     * Slot: full_name Description: The full name of the Organization. e.g. Mouse Genome Database, FlyBase, Online Mendelian Inheritance of Man
--     * Slot: short_name Description: The short name of the organization. For Alliance Members, this is the short name used in the Members list on the website. e.g. MGD, FB, OMIM
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: homepage_resource_descriptor_page_id Description: ResourceDescriptorPage containing URL template for organization's homepage
-- # Class: "InformationContentEntity" Description: "a piece of information that typically is used as support for an assertion or annotation."
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "AuthorReference" Description: ""
--     * Slot: id Description: 
--     * Slot: corresponding_author Description: Indicates if the author is a corresponding author.
--     * Slot: first_author Description: Indicates if the author is a first author.
--     * Slot: first_name Description: first name of a person
--     * Slot: last_name Description: last (family) name of a person
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Reference" Description: ""
--     * Slot: abstract Description: The author summary of the publication. From PubMed otherwise from Mod or manual reference creation.
--     * Slot: category Description: The alliance category type.  Only relevant at Alliance.
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: date_last_modified_in_pubmed Description: Date on which entity was last updated at PubMed. Only relevant for PubMed references.
--     * Slot: date_published Description: Date on which an entity was published.  From PubMed otherwise from Mod or manual reference creation.
--     * Slot: issue_name Description: The number of the journal issue in which the article was published. From PubMed otherwise from Mod or manual reference creation.
--     * Slot: language Description: Language of the reference.  Aggregation of PubMed and FlyBase, editable at Alliance.
--     * Slot: merged_into_id Description: ID that used to refer to this reference
--     * Slot: open_access Description: Indicates if the reference is freely available for use by anyone, usually with fewer copyright and licensing barriers.
--     * Slot: page_range Description: Page numbers of source referenced for statement or publication. From PubMed otherwise from Mod or manual reference creation.
--     * Slot: plain_language_abstract Description: Lay person, readable version of the abstract. Only relevant for PubMed references.
--     * Slot: publisher Description: Publisher associated with a reference or resource. From PubMed otherwise from Mod or manual reference creation.
--     * Slot: pubmed_publication_status Description: Status of the publication at PubMed. Only relevant for PubMed references.
--     * Slot: reference_id Description: The primary key for the Reference object in the references table.
--     * Slot: resource_id Description: 
--     * Slot: title Description: A human readable title for a reference. From PubMed otherwise from Mod or manual reference creation.
--     * Slot: volume Description: Volume associated with a reference. From PubMed otherwise from Mod or manual reference creation.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "PersonalCommunication" Description: "a piece of information that is used to support an assertion or annotation, where the information comes from a person other than the author of the assertion or annotation, or the author of the reference."
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: publisher Description: Publisher associated with a reference or resource. From PubMed otherwise from Mod or manual reference creation.
--     * Slot: volume Description: Volume associated with a reference. From PubMed otherwise from Mod or manual reference creation.
--     * Slot: summary Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Gene" Description: "A DNA genomic entity from which one or more functional* RNA transcript molecules are transcribed, along with cis-regulatory elements responsible for regulating expression (transcription) of the gene. * A functional RNA molecule here can mean one that is directly responsible for the gene's function (e.g. catalysis, structure, etc.) or one that is translated to produce a functional polypeptide/protein. A pseudogene may be considered a gene under this definition, albeit no longer functional."
--     * Slot: gene_type Description: SOTerm describing gene type
--     * Slot: transposon_origin Description: If this gene contains or is originating from a transposon
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: gene_symbol_id Description: The one current accepted symbol for a gene: e.g., wg, pax2a.
--     * Slot: gene_full_name_id Description: The one current full name for a gene: e.g., wingless, paired box 2a.
--     * Slot: gene_systematic_name_id Description: The one current systematic name for a gene: e.g., YHR084W, R09F10.2.
-- # Class: "GeneDTO" Description: "Ingest class for genes"
--     * Slot: gene_type_curie Description: Curie of SOTerm describing gene type
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon_curie Description: Curie of the NCBITaxonTerm representing the taxon from which the biological entity derives
--     * Slot: created_by_curie Description: Curie of the Person object representing the individual that created the entity
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by_curie Description: Curie of the Person object representing the individual that updated the entity
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: Ingest_id Description: Autocreated FK slot
--     * Slot: gene_symbol_dto_id Description: The one current accepted symbol for a gene: e.g., wg, pax2a.
--     * Slot: gene_full_name_dto_id Description: The one current full name for a gene: e.g., wingless, paired box 2a.
--     * Slot: gene_systematic_name_dto_id Description: The one current systematic name for a gene: e.g., YHR084W, R09F10.2.
-- # Class: "GeneSymbolSlotAnnotation" Description: "The one current symbol for the gene."
--     * Slot: id Description: 
--     * Slot: single_gene Description: 
--     * Slot: name_type Description: The type of name: e.g., symbol, full_name, systematic_name, etc.
--     * Slot: format_text Description: A version of a synonym string using only ASCII characters, which is easier to type (for searches), print and parse. For example, Greek characters are transliterated.
--     * Slot: display_text Description: A version of a synonym string for display. Any UTF8 character is permitted.
--     * Slot: synonym_url Description: URL for a synonym: e.g., NCBI URL for the NCBI synonym of an object.
--     * Slot: synonym_scope Description: the scope of the synonym - permissible values are narrow / broad / related / exact
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "GeneFullNameSlotAnnotation" Description: "The one current full name for the gene."
--     * Slot: id Description: 
--     * Slot: single_gene Description: 
--     * Slot: name_type Description: The type of name: e.g., symbol, full_name, systematic_name, etc.
--     * Slot: format_text Description: A version of a synonym string using only ASCII characters, which is easier to type (for searches), print and parse. For example, Greek characters are transliterated.
--     * Slot: display_text Description: A version of a synonym string for display. Any UTF8 character is permitted.
--     * Slot: synonym_url Description: URL for a synonym: e.g., NCBI URL for the NCBI synonym of an object.
--     * Slot: synonym_scope Description: the scope of the synonym - permissible values are narrow / broad / related / exact
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "GeneSystematicNameSlotAnnotation" Description: "The one current systematic name for the gene."
--     * Slot: id Description: 
--     * Slot: single_gene Description: 
--     * Slot: name_type Description: The type of name: e.g., symbol, full_name, systematic_name, etc.
--     * Slot: format_text Description: A version of a synonym string using only ASCII characters, which is easier to type (for searches), print and parse. For example, Greek characters are transliterated.
--     * Slot: display_text Description: A version of a synonym string for display. Any UTF8 character is permitted.
--     * Slot: synonym_url Description: URL for a synonym: e.g., NCBI URL for the NCBI synonym of an object.
--     * Slot: synonym_scope Description: the scope of the synonym - permissible values are narrow / broad / related / exact
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "GeneSynonymSlotAnnotation" Description: "All aliases (non-preferred names) for the gene. Any type of synonym is acceptable."
--     * Slot: id Description: 
--     * Slot: single_gene Description: 
--     * Slot: name_type Description: The type of name: e.g., symbol, full_name, systematic_name, etc.
--     * Slot: format_text Description: A version of a synonym string using only ASCII characters, which is easier to type (for searches), print and parse. For example, Greek characters are transliterated.
--     * Slot: display_text Description: A version of a synonym string for display. Any UTF8 character is permitted.
--     * Slot: synonym_url Description: URL for a synonym: e.g., NCBI URL for the NCBI synonym of an object.
--     * Slot: synonym_scope Description: the scope of the synonym - permissible values are narrow / broad / related / exact
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "GeneticMapPosition" Description: "A genetic map position."
--     * Slot: genetic_map_chromosome Description: Chromosome or contig to which the gene has been genetically mapped
--     * Slot: genetic_map_band Description: Genetic map predicted chromosome location eg 10q12
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "GeneHistory" Description: "The history of a gene"
--     * Slot: id Description: 
--     * Slot: current_version Description: Current version of this object with each version eg 1,2,3 describing major updates
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: cdna_end Description: End position of variant in cDNA coordinates
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: subject_id Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
-- # Class: "Reagent" Description: "A material entity used in experiments."
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "DNAClone" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "RNAClone" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "GeneToGeneOrthology" Description: ""
--     * Slot: id Description: 
--     * Slot: gene_subject Description: 
--     * Slot: predicate Description: orthologous relationship type
--     * Slot: gene_object Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "GeneToGeneOrthologyCurated" Description: "Class that holds the properties necessary to store a curated orthology record."
--     * Slot: id Description: 
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: evidence_code Description: 
--     * Slot: gene_subject Description: 
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: gene_object Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "GeneToGeneOrthologyGenerated" Description: "Class that holds the properties necessary to record an orthology record from DIOPT"
--     * Slot: id Description: 
--     * Slot: is_best_score Description: 
--     * Slot: is_best_reverse_score Description: 
--     * Slot: confidence Description: 
--     * Slot: strict_filter Description: 
--     * Slot: moderate_filter Description: 
--     * Slot: gene_subject Description: 
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: gene_object Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "ModCorpusAssociation" Description: "For a given reference and Mod, whether it is inside corpus, outside corpus, or needs review, as well as where this sorting came from."
--     * Slot: corpus Description: in-out-review corpus status of the publication at the mod. null means needs_review, false means outside_corpus,  true means inside_corpus.
--     * Slot: mod_corpus_association_id Description: An integer referring to a ModCorpusAssociation object. A primary key in the mod_corpus_association table, a foreign key if used in other tables.
--     * Slot: mod_corpus_sort_source Description: origin of corpus determination for that publication and mod
--     * Slot: alliance_member_id Description: An integer referring to an AllianceMember object in the AllianceMember/MOD database table. It's a primary key in the AllianceMember/MOD table, a foreign key if used in other tables.
--     * Slot: reference_id Description: An integer referring to a Reference object in the references table. It's a primary key in the references table, a foreign key when in other tables.
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Ingest" Description: ""
--     * Slot: id Description: 
--     * Slot: linkml_version Description: Version of LinkML schema used for submitted file in the format n.n.n (e.g. 1.2.4 or 2.0.0)
-- # Class: "GeneToGeneAssociation" Description: "abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction."
--     * Slot: id Description: 
--     * Slot: subject Description: the subject gene in the association. If the relation is symmetric, subject vs object is arbitrary. We allow a gene product to stand as a proxy for the gene or vice versa.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: the object gene in the association. If the relation is symmetric, subject vs object is arbitrary. We allow a gene product to stand as a proxy for the gene or vice versa.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "ExpressionExperiment" Description: "Defined by the gene of interest, the specimen, the assay, the reagents (Antibody, Probe), and the reference. It groups ExpressionAnnotations."
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: biological_entity_assayed Description: Holds between a BiologicalEntity and an ExpressionExperiment that reports on its expression.
--     * Slot: assay_used Description: The assay used to experimentally determine gene expression.
--     * Slot: specimen_genomic_model Description: The AffectedGenomicModel of the specimen assayed.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
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
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "ExpressionAnnotationImagePane" Description: ""
--     * Slot: id Description: 
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: subject_id Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: object_id Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
-- # Class: "CurationReportGroup" Description: "This class is use to group together curation reports"
--     * Slot: id Description: 
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "CurationReport" Description: "Base class for all curation reports"
--     * Slot: id Description: 
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: birt_report_file_path Description: File path to where the BIRT file has been saved
--     * Slot: schedule_active Description: This determines if the the schedule is active or not
--     * Slot: cron_schedule Description: A string describing the cron syntax for the schedule
--     * Slot: curation_report_status Description: Describes the status of the curation report
--     * Slot: error_message Description: Error message for curation reports
--     * Slot: scheduling_error_message Description: Error message for scheduling of curation reports
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: curation_report_group_id Description: Links a curation report to its report group
-- # Class: "CurationReportHistory" Description: "Object used to describe the indiviual run of this curation report"
--     * Slot: id Description: 
--     * Slot: curation_report_timestamp Description: Timestamp for creation of BIRT report file
--     * Slot: pdf_file_path Description: File path of the PDF file generated from the BIRT report
--     * Slot: xls_file_path Description: File path of the Excel file generated from the BIRT report
--     * Slot: html_file_path Description: File path of the HTML file generated from the BIRT report
--     * Slot: curation_report_status Description: Describes the status of the curation report
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: curation_report_id Description: Links a report history to its associated report
-- # Class: "BulkLoadGroup" Description: "This class is use to group together bulk load_files"
--     * Slot: id Description: 
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "BulkLoad" Description: "Base class for all loads"
--     * Slot: id Description: 
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: bulkload_status Description: Status used to capture the progress of the load
--     * Slot: error_message Description: Error message for curation reports
--     * Slot: backend_bulk_load_type Description: 
--     * Slot: ontology_type Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: bulkload_group_id Description: Bulk load group designed to group together bulk loads
-- # Class: "BulkLoadFile" Description: "This class is used to hold version of the files being loaded"
--     * Slot: id Description: 
--     * Slot: bulkload_status Description: Status used to capture the progress of the load
--     * Slot: md5_sum Description: Generated md5Sum of the file that has been uploaded
--     * Slot: local_file_path Description: Local file path to where the file has been saved for processing
--     * Slot: file_size Description: The size of the file
--     * Slot: s3_path Description: The relative path to the file in the S3 bucket
--     * Slot: s3_url Description: The full URL to the file from S3
--     * Slot: record_count Description: The number of records found in the file
--     * Slot: error_message Description: Error message for curation reports
--     * Slot: date_last_loaded Description: Indicates when the file was last loaded
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: bulk_load_id Description: A link back to the parent bulk load
-- # Class: "BulkScheduledLoad" Description: "This a bulk load that includes a cron scheuld"
--     * Slot: id Description: 
--     * Slot: schedule_active Description: This determines if the the schedule is active or not
--     * Slot: cron_schedule Description: A string describing the cron syntax for the schedule
--     * Slot: scheduling_error_message Description: Error message for scheduling of curation reports
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: bulkload_status Description: Status used to capture the progress of the load
--     * Slot: error_message Description: Error message for curation reports
--     * Slot: backend_bulk_load_type Description: 
--     * Slot: ontology_type Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: bulkload_group_id Description: Bulk load group designed to group together bulk loads
-- # Class: "BulkFMSLoad" Description: "This bulk load automatically pulls files from the BulkFMSLoad"
--     * Slot: id Description: 
--     * Slot: fms_data_type Description: The dataType paramater in the FMS
--     * Slot: fms_data_sub_type Description: The dataSubType paramater in the FMS
--     * Slot: schedule_active Description: This determines if the the schedule is active or not
--     * Slot: cron_schedule Description: A string describing the cron syntax for the schedule
--     * Slot: scheduling_error_message Description: Error message for scheduling of curation reports
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: bulkload_status Description: Status used to capture the progress of the load
--     * Slot: error_message Description: Error message for curation reports
--     * Slot: backend_bulk_load_type Description: 
--     * Slot: ontology_type Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: bulkload_group_id Description: Bulk load group designed to group together bulk loads
-- # Class: "BulkURLLoad" Description: "This bulk load automatically pulls files from a defined BulkURLLoad"
--     * Slot: id Description: 
--     * Slot: bulkload_url Description: The URL that this bulk load will download for ingest
--     * Slot: schedule_active Description: This determines if the the schedule is active or not
--     * Slot: cron_schedule Description: A string describing the cron syntax for the schedule
--     * Slot: scheduling_error_message Description: Error message for scheduling of curation reports
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: bulkload_status Description: Status used to capture the progress of the load
--     * Slot: error_message Description: Error message for curation reports
--     * Slot: backend_bulk_load_type Description: 
--     * Slot: ontology_type Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: bulkload_group_id Description: Bulk load group designed to group together bulk loads
-- # Class: "BulkManualLoad" Description: "This bulk load is used by DQM's to submit their files to the curation system"
--     * Slot: id Description: 
--     * Slot: backend_load_type Description: 
--     * Slot: name Description: a human-readable name for an entity
--     * Slot: bulkload_status Description: Status used to capture the progress of the load
--     * Slot: error_message Description: Error message for curation reports
--     * Slot: backend_bulk_load_type Description: 
--     * Slot: ontology_type Description: 
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: bulkload_group_id Description: Bulk load group designed to group together bulk loads
-- # Class: "BulkLoadFileHistory" Description: "Object used to describe the indiviual run of this BulkLoadFile"
--     * Slot: id Description: 
--     * Slot: load_started Description: The date and time that the load started.
--     * Slot: load_finished Description: The date and time that the load finished.
--     * Slot: total_records Description: The total number of records
--     * Slot: failed_records Description: The number of failed records
--     * Slot: completed_records Description: The number of completed records
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "GeneCluster" Description: "A gene cluster is a set of genes which have a biological significance, and which are probably clustered together on the genome, like histones and miRNAs"
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: related_note_id Description: Holds between an object and a Note object.
-- # Class: "GeneCollection" Description: "A gene collection is a set of genes which have been grouped based on experimental evidence, for example a set of interacting genes, genes in expression cluster, or a set of ChIP binding peaks"
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: related_note_id Description: Holds between an object and a Note object.
-- # Class: "GeneNomenclatureSet" Description: "WB specific. A gene class is a set of genes which share nomenclature, belonging to the same gene class."
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: designating_laboratory Description: A laboratory which designated this gene class
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: related_note_id Description: Holds between an object and a Note object.
-- # Class: "Operon" Description: "The DNA region of a group of adjacent genes whose transcription is coordinated on one or several mutually overlapping transcription units transcribed in the same direction and sharing at least one gene."
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
--     * Slot: related_note_id Description: Holds between an object and a Note object.
-- # Class: "UniGeneSet" Description: "XenBase-specific. A set of three genes from X. tropicalis and X. laevis (S and L forms) representing a single unigene."
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "FunctionalGeneSet" Description: ""
--     * Slot: single_reference Description: holds between an object and a single reference
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Pathway" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "ProteinComplex" Description: ""
--     * Slot: curie Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: taxon Description: The taxon from which the biological entity derives.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "GeneToPathwayAssociation" Description: ""
--     * Slot: id Description: 
--     * Slot: subject Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: predicate Description: A high-level grouping for the relationship type. This is analogous to category for nodes. In RDF, this corresponds to rdf:predicate and in Neo4j this corresponds to the relationship type.
--     * Slot: object Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
--     * Slot: created_by Description: The individual that created the entity.
--     * Slot: date_created Description: The date on which an entity was created. This can be applied to nodes or edges.
--     * Slot: updated_by Description: The individual that last modified the entity.
--     * Slot: date_updated Description: Date on which an entity was last modified.
--     * Slot: db_date_created Description: The date on which an entity was created in the Alliance database.  This is disinct from date_created, which represents the date when the entity was originally created (i.e. at the MOD for imported data).
--     * Slot: db_date_updated Description: Date on which an entity was last modified in the Alliance database.  This is disinct from date_updated, which represents the date when the entity was last modified and may predate import into the Alliance database.
--     * Slot: internal Description: Classifies the entity as private (for internal use) or not (for public use).
--     * Slot: obsolete Description: Entity is no longer current.
-- # Class: "Variant_related_notes" Description: ""
--     * Slot: Variant_curie Description: Autocreated FK slot
--     * Slot: related_notes_id Description: Holds between an object and a list of related Note objects.
-- # Class: "Variant_variant_polypeptide_locations" Description: ""
--     * Slot: Variant_curie Description: Autocreated FK slot
--     * Slot: variant_polypeptide_locations_id Description: Location of the variant within polypeptide entities.
-- # Class: "Variant_variant_transcript_locations" Description: ""
--     * Slot: Variant_curie Description: Autocreated FK slot
--     * Slot: variant_transcript_locations_id Description: Location of the variant within transcript entities.
-- # Class: "Variant_source_variant_locations" Description: ""
--     * Slot: Variant_curie Description: Autocreated FK slot
--     * Slot: source_variant_locations_id Description: Location of the variant within genomic entities,as described in the source references.
-- # Class: "Variant_cross_reference" Description: ""
--     * Slot: Variant_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "Variant_secondary_identifiers" Description: ""
--     * Slot: Variant_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "Variant_genomic_location_associations" Description: ""
--     * Slot: Variant_curie Description: Autocreated FK slot
--     * Slot: genomic_location_associations_id Description: 
-- # Class: "SourceVariantLocation_variant_locations" Description: ""
--     * Slot: SourceVariantLocation_id Description: Autocreated FK slot
--     * Slot: variant_locations_id Description: Location of the variant within genomic entities. Variant_locations can include any or all of: one VariantGenomeLocation stanza, one or more VariantTranscriptLocation stanzas and/or one or more VariantPolypeptideLocation stanzas.
-- # Class: "VariantPolypeptideLocation_associated_transcripts" Description: ""
--     * Slot: VariantPolypeptideLocation_id Description: Autocreated FK slot
--     * Slot: associated_transcripts Description: Transcript(s) associated with polypeptide to which variant is aligned.
-- # Class: "OntologyTerm_definition_urls" Description: ""
--     * Slot: OntologyTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "OntologyTerm_cross_reference" Description: ""
--     * Slot: OntologyTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "OntologyTerm_synonyms" Description: ""
--     * Slot: OntologyTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "OntologyTerm_subsets" Description: ""
--     * Slot: OntologyTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "OntologyTerm_secondary_identifiers" Description: ""
--     * Slot: OntologyTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "OntologyTerm_ancestors" Description: ""
--     * Slot: OntologyTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "OntologyTerm_descendants" Description: ""
--     * Slot: OntologyTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "OntologyTermClosure_relationship_type" Description: ""
--     * Slot: OntologyTermClosure_id Description: Autocreated FK slot
--     * Slot: relationship_type Description: 
-- # Class: "OntologyTermClosure_evidence" Description: ""
--     * Slot: OntologyTermClosure_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "DOTerm_definition_urls" Description: ""
--     * Slot: DOTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "DOTerm_cross_reference" Description: ""
--     * Slot: DOTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "DOTerm_synonyms" Description: ""
--     * Slot: DOTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "DOTerm_subsets" Description: ""
--     * Slot: DOTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "DOTerm_secondary_identifiers" Description: ""
--     * Slot: DOTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "DOTerm_ancestors" Description: ""
--     * Slot: DOTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "DOTerm_descendants" Description: ""
--     * Slot: DOTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "ECOTerm_definition_urls" Description: ""
--     * Slot: ECOTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "ECOTerm_cross_reference" Description: ""
--     * Slot: ECOTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "ECOTerm_synonyms" Description: ""
--     * Slot: ECOTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "ECOTerm_subsets" Description: ""
--     * Slot: ECOTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "ECOTerm_secondary_identifiers" Description: ""
--     * Slot: ECOTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "ECOTerm_ancestors" Description: ""
--     * Slot: ECOTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "ECOTerm_descendants" Description: ""
--     * Slot: ECOTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "NCBITaxonTerm_definition_urls" Description: ""
--     * Slot: NCBITaxonTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "NCBITaxonTerm_cross_reference" Description: ""
--     * Slot: NCBITaxonTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "NCBITaxonTerm_synonyms" Description: ""
--     * Slot: NCBITaxonTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "NCBITaxonTerm_subsets" Description: ""
--     * Slot: NCBITaxonTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "NCBITaxonTerm_secondary_identifiers" Description: ""
--     * Slot: NCBITaxonTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "NCBITaxonTerm_ancestors" Description: ""
--     * Slot: NCBITaxonTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "NCBITaxonTerm_descendants" Description: ""
--     * Slot: NCBITaxonTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "FBCVTerm_definition_urls" Description: ""
--     * Slot: FBCVTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "FBCVTerm_cross_reference" Description: ""
--     * Slot: FBCVTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "FBCVTerm_synonyms" Description: ""
--     * Slot: FBCVTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "FBCVTerm_subsets" Description: ""
--     * Slot: FBCVTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "FBCVTerm_secondary_identifiers" Description: ""
--     * Slot: FBCVTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "FBCVTerm_ancestors" Description: ""
--     * Slot: FBCVTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "FBCVTerm_descendants" Description: ""
--     * Slot: FBCVTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "GOTerm_definition_urls" Description: ""
--     * Slot: GOTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "GOTerm_cross_reference" Description: ""
--     * Slot: GOTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "GOTerm_synonyms" Description: ""
--     * Slot: GOTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "GOTerm_subsets" Description: ""
--     * Slot: GOTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "GOTerm_secondary_identifiers" Description: ""
--     * Slot: GOTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "GOTerm_ancestors" Description: ""
--     * Slot: GOTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "GOTerm_descendants" Description: ""
--     * Slot: GOTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "ROTerm_definition_urls" Description: ""
--     * Slot: ROTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "ROTerm_cross_reference" Description: ""
--     * Slot: ROTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "ROTerm_synonyms" Description: ""
--     * Slot: ROTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "ROTerm_subsets" Description: ""
--     * Slot: ROTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "ROTerm_secondary_identifiers" Description: ""
--     * Slot: ROTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "ROTerm_ancestors" Description: ""
--     * Slot: ROTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "ROTerm_descendants" Description: ""
--     * Slot: ROTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "MITerm_definition_urls" Description: ""
--     * Slot: MITerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "MITerm_cross_reference" Description: ""
--     * Slot: MITerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "MITerm_synonyms" Description: ""
--     * Slot: MITerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "MITerm_subsets" Description: ""
--     * Slot: MITerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "MITerm_secondary_identifiers" Description: ""
--     * Slot: MITerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "MITerm_ancestors" Description: ""
--     * Slot: MITerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "MITerm_descendants" Description: ""
--     * Slot: MITerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "MMOTerm_definition_urls" Description: ""
--     * Slot: MMOTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "MMOTerm_cross_reference" Description: ""
--     * Slot: MMOTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "MMOTerm_synonyms" Description: ""
--     * Slot: MMOTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "MMOTerm_subsets" Description: ""
--     * Slot: MMOTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "MMOTerm_secondary_identifiers" Description: ""
--     * Slot: MMOTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "MMOTerm_ancestors" Description: ""
--     * Slot: MMOTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "MMOTerm_descendants" Description: ""
--     * Slot: MMOTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "MMUSDVTerm_definition_urls" Description: ""
--     * Slot: MMUSDVTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "MMUSDVTerm_cross_reference" Description: ""
--     * Slot: MMUSDVTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "MMUSDVTerm_synonyms" Description: ""
--     * Slot: MMUSDVTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "MMUSDVTerm_subsets" Description: ""
--     * Slot: MMUSDVTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "MMUSDVTerm_secondary_identifiers" Description: ""
--     * Slot: MMUSDVTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "MMUSDVTerm_ancestors" Description: ""
--     * Slot: MMUSDVTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "MMUSDVTerm_descendants" Description: ""
--     * Slot: MMUSDVTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "SOTerm_definition_urls" Description: ""
--     * Slot: SOTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "SOTerm_cross_reference" Description: ""
--     * Slot: SOTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "SOTerm_synonyms" Description: ""
--     * Slot: SOTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "SOTerm_subsets" Description: ""
--     * Slot: SOTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "SOTerm_secondary_identifiers" Description: ""
--     * Slot: SOTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "SOTerm_ancestors" Description: ""
--     * Slot: SOTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "SOTerm_descendants" Description: ""
--     * Slot: SOTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "XBEDTerm_definition_urls" Description: ""
--     * Slot: XBEDTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "XBEDTerm_cross_reference" Description: ""
--     * Slot: XBEDTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "XBEDTerm_synonyms" Description: ""
--     * Slot: XBEDTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "XBEDTerm_subsets" Description: ""
--     * Slot: XBEDTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "XBEDTerm_secondary_identifiers" Description: ""
--     * Slot: XBEDTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "XBEDTerm_ancestors" Description: ""
--     * Slot: XBEDTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "XBEDTerm_descendants" Description: ""
--     * Slot: XBEDTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "CHEBITerm_definition_urls" Description: ""
--     * Slot: CHEBITerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "CHEBITerm_cross_reference" Description: ""
--     * Slot: CHEBITerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "CHEBITerm_synonyms" Description: ""
--     * Slot: CHEBITerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "CHEBITerm_subsets" Description: ""
--     * Slot: CHEBITerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "CHEBITerm_secondary_identifiers" Description: ""
--     * Slot: CHEBITerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "CHEBITerm_ancestors" Description: ""
--     * Slot: CHEBITerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "CHEBITerm_descendants" Description: ""
--     * Slot: CHEBITerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "StageTerm_definition_urls" Description: ""
--     * Slot: StageTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "StageTerm_cross_reference" Description: ""
--     * Slot: StageTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "StageTerm_synonyms" Description: ""
--     * Slot: StageTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "StageTerm_subsets" Description: ""
--     * Slot: StageTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "StageTerm_secondary_identifiers" Description: ""
--     * Slot: StageTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "StageTerm_ancestors" Description: ""
--     * Slot: StageTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "StageTerm_descendants" Description: ""
--     * Slot: StageTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "FBDVTerm_definition_urls" Description: ""
--     * Slot: FBDVTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "FBDVTerm_cross_reference" Description: ""
--     * Slot: FBDVTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "FBDVTerm_synonyms" Description: ""
--     * Slot: FBDVTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "FBDVTerm_subsets" Description: ""
--     * Slot: FBDVTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "FBDVTerm_secondary_identifiers" Description: ""
--     * Slot: FBDVTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "FBDVTerm_ancestors" Description: ""
--     * Slot: FBDVTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "FBDVTerm_descendants" Description: ""
--     * Slot: FBDVTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "WBLSTerm_definition_urls" Description: ""
--     * Slot: WBLSTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "WBLSTerm_cross_reference" Description: ""
--     * Slot: WBLSTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "WBLSTerm_synonyms" Description: ""
--     * Slot: WBLSTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "WBLSTerm_subsets" Description: ""
--     * Slot: WBLSTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "WBLSTerm_secondary_identifiers" Description: ""
--     * Slot: WBLSTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "WBLSTerm_ancestors" Description: ""
--     * Slot: WBLSTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "WBLSTerm_descendants" Description: ""
--     * Slot: WBLSTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "XBSTerm_definition_urls" Description: ""
--     * Slot: XBSTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "XBSTerm_cross_reference" Description: ""
--     * Slot: XBSTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "XBSTerm_synonyms" Description: ""
--     * Slot: XBSTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "XBSTerm_subsets" Description: ""
--     * Slot: XBSTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "XBSTerm_secondary_identifiers" Description: ""
--     * Slot: XBSTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "XBSTerm_ancestors" Description: ""
--     * Slot: XBSTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "XBSTerm_descendants" Description: ""
--     * Slot: XBSTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "ZFSTerm_definition_urls" Description: ""
--     * Slot: ZFSTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "ZFSTerm_cross_reference" Description: ""
--     * Slot: ZFSTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "ZFSTerm_synonyms" Description: ""
--     * Slot: ZFSTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "ZFSTerm_subsets" Description: ""
--     * Slot: ZFSTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "ZFSTerm_secondary_identifiers" Description: ""
--     * Slot: ZFSTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "ZFSTerm_ancestors" Description: ""
--     * Slot: ZFSTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "ZFSTerm_descendants" Description: ""
--     * Slot: ZFSTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "ExperimentalConditionOntologyTerm_definition_urls" Description: ""
--     * Slot: ExperimentalConditionOntologyTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "ExperimentalConditionOntologyTerm_cross_reference" Description: ""
--     * Slot: ExperimentalConditionOntologyTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "ExperimentalConditionOntologyTerm_synonyms" Description: ""
--     * Slot: ExperimentalConditionOntologyTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "ExperimentalConditionOntologyTerm_subsets" Description: ""
--     * Slot: ExperimentalConditionOntologyTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "ExperimentalConditionOntologyTerm_secondary_identifiers" Description: ""
--     * Slot: ExperimentalConditionOntologyTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "ExperimentalConditionOntologyTerm_ancestors" Description: ""
--     * Slot: ExperimentalConditionOntologyTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "ExperimentalConditionOntologyTerm_descendants" Description: ""
--     * Slot: ExperimentalConditionOntologyTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "ZECOTerm_definition_urls" Description: ""
--     * Slot: ZECOTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "ZECOTerm_cross_reference" Description: ""
--     * Slot: ZECOTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "ZECOTerm_synonyms" Description: ""
--     * Slot: ZECOTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "ZECOTerm_subsets" Description: ""
--     * Slot: ZECOTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "ZECOTerm_secondary_identifiers" Description: ""
--     * Slot: ZECOTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "ZECOTerm_ancestors" Description: ""
--     * Slot: ZECOTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "ZECOTerm_descendants" Description: ""
--     * Slot: ZECOTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "XCOTerm_definition_urls" Description: ""
--     * Slot: XCOTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "XCOTerm_cross_reference" Description: ""
--     * Slot: XCOTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "XCOTerm_synonyms" Description: ""
--     * Slot: XCOTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "XCOTerm_subsets" Description: ""
--     * Slot: XCOTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "XCOTerm_secondary_identifiers" Description: ""
--     * Slot: XCOTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "XCOTerm_ancestors" Description: ""
--     * Slot: XCOTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "XCOTerm_descendants" Description: ""
--     * Slot: XCOTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "AnatomicalTerm_definition_urls" Description: ""
--     * Slot: AnatomicalTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "AnatomicalTerm_cross_reference" Description: ""
--     * Slot: AnatomicalTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "AnatomicalTerm_synonyms" Description: ""
--     * Slot: AnatomicalTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "AnatomicalTerm_subsets" Description: ""
--     * Slot: AnatomicalTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "AnatomicalTerm_secondary_identifiers" Description: ""
--     * Slot: AnatomicalTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "AnatomicalTerm_ancestors" Description: ""
--     * Slot: AnatomicalTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "AnatomicalTerm_descendants" Description: ""
--     * Slot: AnatomicalTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "CLTerm_definition_urls" Description: ""
--     * Slot: CLTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "CLTerm_cross_reference" Description: ""
--     * Slot: CLTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "CLTerm_synonyms" Description: ""
--     * Slot: CLTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "CLTerm_subsets" Description: ""
--     * Slot: CLTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "CLTerm_secondary_identifiers" Description: ""
--     * Slot: CLTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "CLTerm_ancestors" Description: ""
--     * Slot: CLTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "CLTerm_descendants" Description: ""
--     * Slot: CLTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "EMAPATerm_definition_urls" Description: ""
--     * Slot: EMAPATerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "EMAPATerm_cross_reference" Description: ""
--     * Slot: EMAPATerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "EMAPATerm_synonyms" Description: ""
--     * Slot: EMAPATerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "EMAPATerm_subsets" Description: ""
--     * Slot: EMAPATerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "EMAPATerm_secondary_identifiers" Description: ""
--     * Slot: EMAPATerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "EMAPATerm_ancestors" Description: ""
--     * Slot: EMAPATerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "EMAPATerm_descendants" Description: ""
--     * Slot: EMAPATerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "DAOTerm_definition_urls" Description: ""
--     * Slot: DAOTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "DAOTerm_cross_reference" Description: ""
--     * Slot: DAOTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "DAOTerm_synonyms" Description: ""
--     * Slot: DAOTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "DAOTerm_subsets" Description: ""
--     * Slot: DAOTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "DAOTerm_secondary_identifiers" Description: ""
--     * Slot: DAOTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "DAOTerm_ancestors" Description: ""
--     * Slot: DAOTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "DAOTerm_descendants" Description: ""
--     * Slot: DAOTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "MATerm_definition_urls" Description: ""
--     * Slot: MATerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "MATerm_cross_reference" Description: ""
--     * Slot: MATerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "MATerm_synonyms" Description: ""
--     * Slot: MATerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "MATerm_subsets" Description: ""
--     * Slot: MATerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "MATerm_secondary_identifiers" Description: ""
--     * Slot: MATerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "MATerm_ancestors" Description: ""
--     * Slot: MATerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "MATerm_descendants" Description: ""
--     * Slot: MATerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "UBERONTerm_definition_urls" Description: ""
--     * Slot: UBERONTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "UBERONTerm_cross_reference" Description: ""
--     * Slot: UBERONTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "UBERONTerm_synonyms" Description: ""
--     * Slot: UBERONTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "UBERONTerm_subsets" Description: ""
--     * Slot: UBERONTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "UBERONTerm_secondary_identifiers" Description: ""
--     * Slot: UBERONTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "UBERONTerm_ancestors" Description: ""
--     * Slot: UBERONTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "UBERONTerm_descendants" Description: ""
--     * Slot: UBERONTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "WBBTTerm_definition_urls" Description: ""
--     * Slot: WBBTTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "WBBTTerm_cross_reference" Description: ""
--     * Slot: WBBTTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "WBBTTerm_synonyms" Description: ""
--     * Slot: WBBTTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "WBBTTerm_subsets" Description: ""
--     * Slot: WBBTTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "WBBTTerm_secondary_identifiers" Description: ""
--     * Slot: WBBTTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "WBBTTerm_ancestors" Description: ""
--     * Slot: WBBTTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "WBBTTerm_descendants" Description: ""
--     * Slot: WBBTTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "XBATerm_definition_urls" Description: ""
--     * Slot: XBATerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "XBATerm_cross_reference" Description: ""
--     * Slot: XBATerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "XBATerm_synonyms" Description: ""
--     * Slot: XBATerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "XBATerm_subsets" Description: ""
--     * Slot: XBATerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "XBATerm_secondary_identifiers" Description: ""
--     * Slot: XBATerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "XBATerm_ancestors" Description: ""
--     * Slot: XBATerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "XBATerm_descendants" Description: ""
--     * Slot: XBATerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "ZFATerm_definition_urls" Description: ""
--     * Slot: ZFATerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "ZFATerm_cross_reference" Description: ""
--     * Slot: ZFATerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "ZFATerm_synonyms" Description: ""
--     * Slot: ZFATerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "ZFATerm_subsets" Description: ""
--     * Slot: ZFATerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "ZFATerm_secondary_identifiers" Description: ""
--     * Slot: ZFATerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "ZFATerm_ancestors" Description: ""
--     * Slot: ZFATerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "ZFATerm_descendants" Description: ""
--     * Slot: ZFATerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "PhenotypeTerm_definition_urls" Description: ""
--     * Slot: PhenotypeTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "PhenotypeTerm_cross_reference" Description: ""
--     * Slot: PhenotypeTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "PhenotypeTerm_synonyms" Description: ""
--     * Slot: PhenotypeTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "PhenotypeTerm_subsets" Description: ""
--     * Slot: PhenotypeTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "PhenotypeTerm_secondary_identifiers" Description: ""
--     * Slot: PhenotypeTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "PhenotypeTerm_ancestors" Description: ""
--     * Slot: PhenotypeTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "PhenotypeTerm_descendants" Description: ""
--     * Slot: PhenotypeTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "XPOTerm_definition_urls" Description: ""
--     * Slot: XPOTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "XPOTerm_cross_reference" Description: ""
--     * Slot: XPOTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "XPOTerm_synonyms" Description: ""
--     * Slot: XPOTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "XPOTerm_subsets" Description: ""
--     * Slot: XPOTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "XPOTerm_secondary_identifiers" Description: ""
--     * Slot: XPOTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "XPOTerm_ancestors" Description: ""
--     * Slot: XPOTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "XPOTerm_descendants" Description: ""
--     * Slot: XPOTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "MPTerm_definition_urls" Description: ""
--     * Slot: MPTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "MPTerm_cross_reference" Description: ""
--     * Slot: MPTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "MPTerm_synonyms" Description: ""
--     * Slot: MPTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "MPTerm_subsets" Description: ""
--     * Slot: MPTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "MPTerm_secondary_identifiers" Description: ""
--     * Slot: MPTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "MPTerm_ancestors" Description: ""
--     * Slot: MPTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "MPTerm_descendants" Description: ""
--     * Slot: MPTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "ATPTerm_definition_urls" Description: ""
--     * Slot: ATPTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "ATPTerm_cross_reference" Description: ""
--     * Slot: ATPTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "ATPTerm_synonyms" Description: ""
--     * Slot: ATPTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "ATPTerm_subsets" Description: ""
--     * Slot: ATPTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "ATPTerm_secondary_identifiers" Description: ""
--     * Slot: ATPTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "ATPTerm_ancestors" Description: ""
--     * Slot: ATPTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "ATPTerm_descendants" Description: ""
--     * Slot: ATPTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "ChemicalTerm_definition_urls" Description: ""
--     * Slot: ChemicalTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "ChemicalTerm_cross_reference" Description: ""
--     * Slot: ChemicalTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "ChemicalTerm_synonyms" Description: ""
--     * Slot: ChemicalTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "ChemicalTerm_subsets" Description: ""
--     * Slot: ChemicalTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "ChemicalTerm_secondary_identifiers" Description: ""
--     * Slot: ChemicalTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "ChemicalTerm_ancestors" Description: ""
--     * Slot: ChemicalTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "ChemicalTerm_descendants" Description: ""
--     * Slot: ChemicalTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "XSMOTerm_definition_urls" Description: ""
--     * Slot: XSMOTerm_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "XSMOTerm_cross_reference" Description: ""
--     * Slot: XSMOTerm_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "XSMOTerm_synonyms" Description: ""
--     * Slot: XSMOTerm_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "XSMOTerm_subsets" Description: ""
--     * Slot: XSMOTerm_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "XSMOTerm_secondary_identifiers" Description: ""
--     * Slot: XSMOTerm_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "XSMOTerm_ancestors" Description: ""
--     * Slot: XSMOTerm_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "XSMOTerm_descendants" Description: ""
--     * Slot: XSMOTerm_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "Molecule_definition_urls" Description: ""
--     * Slot: Molecule_curie Description: Autocreated FK slot
--     * Slot: definition_urls Description: 
-- # Class: "Molecule_cross_reference" Description: ""
--     * Slot: Molecule_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "Molecule_synonyms" Description: ""
--     * Slot: Molecule_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "Molecule_subsets" Description: ""
--     * Slot: Molecule_curie Description: Autocreated FK slot
--     * Slot: subsets Description: 
-- # Class: "Molecule_secondary_identifiers" Description: ""
--     * Slot: Molecule_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "Molecule_ancestors" Description: ""
--     * Slot: Molecule_curie Description: Autocreated FK slot
--     * Slot: ancestors_id Description: The ancestors of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms from which this term develops (not a true parent/child or ancestor/descendant relationship).
-- # Class: "Molecule_descendants" Description: ""
--     * Slot: Molecule_curie Description: Autocreated FK slot
--     * Slot: descendants_id Description: The descendants of this term in the ontology, including the term itself. This language works well for the majority of use cases, however for a relationship like "develops_from", ancestors are the terms to which this term develops into (not a true parent/child or ancestor/descendant relationship).
-- # Class: "Allele_reference" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: reference Description: holds between an object and a list of references
-- # Class: "Allele_allele_mutation_types" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: allele_mutation_types_id Description: Mutation types for a given allele
-- # Class: "Allele_allele_inheritance_modes" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: allele_inheritance_modes_id Description: Inheritance modes for an allele
-- # Class: "Allele_allele_functional_impacts" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: allele_functional_impacts_id Description: Functional impacts of a given allele
-- # Class: "Allele_allele_molecular_mutations" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: allele_molecular_mutations_id Description: Molecular mutations of a given allele
-- # Class: "Allele_allele_secondary_ids" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: allele_secondary_ids_id Description: Secondary IDs of a given allele
-- # Class: "Allele_allele_nomenclature_events" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: allele_nomenclature_events_id Description: Nomenclature events of a given allele
-- # Class: "Allele_allele_notes" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: allele_notes_id Description: Notes for a given allele
-- # Class: "Allele_allele_synonyms" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: allele_synonyms_id Description: Holds between an Allele and a synonym.
-- # Class: "Allele_allele_gene_associations" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: allele_gene_associations_id Description: 
-- # Class: "Allele_allele_transcript_associations" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: allele_transcript_associations_id Description: 
-- # Class: "Allele_allele_protein_associations" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: allele_protein_associations_id Description: 
-- # Class: "Allele_allele_allele_associations" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: allele_allele_associations_id Description: 
-- # Class: "Allele_allele_variant_associations" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: allele_variant_associations_id Description: 
-- # Class: "Allele_allele_construct_associations" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: allele_construct_associations_id Description: 
-- # Class: "Allele_allele_cell_line_associations" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: allele_cell_line_associations_id Description: 
-- # Class: "Allele_allele_image_associations" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: allele_image_associations_id Description: 
-- # Class: "Allele_allele_origin_associations" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: allele_origin_associations_id Description: 
-- # Class: "Allele_allele_generation_method_associations" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: allele_generation_method_associations_id Description: 
-- # Class: "Allele_cross_reference" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "Allele_secondary_identifiers" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "Allele_genomic_location_associations" Description: ""
--     * Slot: Allele_curie Description: Autocreated FK slot
--     * Slot: genomic_location_associations_id Description: 
-- # Class: "CellLine_cross_reference" Description: ""
--     * Slot: CellLine_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "CellLine_secondary_identifiers" Description: ""
--     * Slot: CellLine_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "CellLine_genomic_location_associations" Description: ""
--     * Slot: CellLine_curie Description: Autocreated FK slot
--     * Slot: genomic_location_associations_id Description: 
-- # Class: "Construct_construct_components" Description: ""
--     * Slot: Construct_curie Description: Autocreated FK slot
--     * Slot: construct_components Description: 
-- # Class: "Construct_reference" Description: ""
--     * Slot: Construct_curie Description: Autocreated FK slot
--     * Slot: reference Description: holds between an object and a list of references
-- # Class: "Construct_cross_reference" Description: ""
--     * Slot: Construct_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "Construct_secondary_identifiers" Description: ""
--     * Slot: Construct_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "Construct_genomic_location_associations" Description: ""
--     * Slot: Construct_curie Description: Autocreated FK slot
--     * Slot: genomic_location_associations_id Description: 
-- # Class: "ConstructComponent_cross_reference" Description: ""
--     * Slot: ConstructComponent_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "ConstructComponent_secondary_identifiers" Description: ""
--     * Slot: ConstructComponent_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "ConstructComponent_genomic_location_associations" Description: ""
--     * Slot: ConstructComponent_curie Description: Autocreated FK slot
--     * Slot: genomic_location_associations_id Description: 
-- # Class: "ConstructComponentAssociation_evidence" Description: ""
--     * Slot: ConstructComponentAssociation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "GenerationMethod_mutagenesis_methods" Description: ""
--     * Slot: GenerationMethod_id Description: Autocreated FK slot
--     * Slot: mutagenesis_methods Description: Technique used to create the allele, e.g. spontaneous / naturally occurring / radiation-induced / recombinant / ENU / CRISPR / TALEN / gamma rays / not specified / spontaneous / DNA / DNA AND CRISPR / DNA and TALEN / zinc finger nuclease / EMS
-- # Class: "SequenceTargetingReagent_reference" Description: ""
--     * Slot: SequenceTargetingReagent_curie Description: Autocreated FK slot
--     * Slot: reference Description: holds between an object and a list of references
-- # Class: "SequenceTargetingReagent_cross_reference" Description: ""
--     * Slot: SequenceTargetingReagent_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "SequenceTargetingReagent_secondary_identifiers" Description: ""
--     * Slot: SequenceTargetingReagent_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "SequenceTargetingReagent_genomic_location_associations" Description: ""
--     * Slot: SequenceTargetingReagent_curie Description: Autocreated FK slot
--     * Slot: genomic_location_associations_id Description: 
-- # Class: "SequenceTargetingReagentToGeneAssociation_reference" Description: ""
--     * Slot: SequenceTargetingReagentToGeneAssociation_id Description: Autocreated FK slot
--     * Slot: reference Description: holds between an object and a list of references
-- # Class: "SequenceTargetingReagentToGeneAssociation_evidence" Description: ""
--     * Slot: SequenceTargetingReagentToGeneAssociation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AlleleDatabaseStatusSlotAnnotation_evidence" Description: ""
--     * Slot: AlleleDatabaseStatusSlotAnnotation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AlleleFullNameSlotAnnotation_evidence" Description: ""
--     * Slot: AlleleFullNameSlotAnnotation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AlleleFunctionalImpactSlotAnnotation_functional_impacts" Description: ""
--     * Slot: AlleleFunctionalImpactSlotAnnotation_id Description: Autocreated FK slot
--     * Slot: functional_impacts Description: Experimentally assessed functional impact of the allele, e.g. knockout / amorphic
-- # Class: "AlleleFunctionalImpactSlotAnnotation_evidence" Description: ""
--     * Slot: AlleleFunctionalImpactSlotAnnotation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AlleleGermlineTransmissionStatusSlotAnnotation_evidence" Description: ""
--     * Slot: AlleleGermlineTransmissionStatusSlotAnnotation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AlleleInheritanceModeSlotAnnotation_evidence" Description: ""
--     * Slot: AlleleInheritanceModeSlotAnnotation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AlleleMolecularMutationSlotAnnotation_molecular_mutations" Description: ""
--     * Slot: AlleleMolecularMutationSlotAnnotation_id Description: Autocreated FK slot
--     * Slot: molecular_mutations Description: Description of the DNA changes if precise genomic location unknown
-- # Class: "AlleleMolecularMutationSlotAnnotation_evidence" Description: ""
--     * Slot: AlleleMolecularMutationSlotAnnotation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AlleleMutationTypeSlotAnnotation_mutation_types" Description: ""
--     * Slot: AlleleMutationTypeSlotAnnotation_id Description: Autocreated FK slot
--     * Slot: mutation_types Description: SO term for type of mutation
-- # Class: "AlleleMutationTypeSlotAnnotation_evidence" Description: ""
--     * Slot: AlleleMutationTypeSlotAnnotation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AlleleNomenclatureEventSlotAnnotation_evidence" Description: ""
--     * Slot: AlleleNomenclatureEventSlotAnnotation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AlleleNoteSlotAnnotation_evidence" Description: ""
--     * Slot: AlleleNoteSlotAnnotation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AlleleSecondaryIdSlotAnnotation_evidence" Description: ""
--     * Slot: AlleleSecondaryIdSlotAnnotation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AlleleSymbolSlotAnnotation_evidence" Description: ""
--     * Slot: AlleleSymbolSlotAnnotation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AlleleSynonymSlotAnnotation_evidence" Description: ""
--     * Slot: AlleleSynonymSlotAnnotation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AlleleAlleleAssociation_evidence" Description: ""
--     * Slot: AlleleAlleleAssociation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AlleleCellLineAssociation_evidence" Description: ""
--     * Slot: AlleleCellLineAssociation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AlleleConstructAssociation_evidence" Description: ""
--     * Slot: AlleleConstructAssociation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AlleleGeneAssociation_evidence" Description: ""
--     * Slot: AlleleGeneAssociation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AlleleGenerationMethodAssociation_evidence" Description: ""
--     * Slot: AlleleGenerationMethodAssociation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AlleleGenomicEntityAssociation_evidence" Description: ""
--     * Slot: AlleleGenomicEntityAssociation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AlleleImageAssociation_evidence" Description: ""
--     * Slot: AlleleImageAssociation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AlleleOriginAssociation_evidence" Description: ""
--     * Slot: AlleleOriginAssociation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AlleleProteinAssociation_evidence" Description: ""
--     * Slot: AlleleProteinAssociation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AlleleTranscriptAssociation_evidence" Description: ""
--     * Slot: AlleleTranscriptAssociation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AlleleVariantAssociation_evidence" Description: ""
--     * Slot: AlleleVariantAssociation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "PhenotypeAnnotation_condition_relations" Description: ""
--     * Slot: PhenotypeAnnotation_curie Description: Autocreated FK slot
--     * Slot: condition_relations_id Description: 
-- # Class: "PhenotypeAnnotation_evidence" Description: ""
--     * Slot: PhenotypeAnnotation_curie Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "GenePhenotypeAnnotation_condition_relations" Description: ""
--     * Slot: GenePhenotypeAnnotation_curie Description: Autocreated FK slot
--     * Slot: condition_relations_id Description: 
-- # Class: "GenePhenotypeAnnotation_evidence" Description: ""
--     * Slot: GenePhenotypeAnnotation_curie Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AllelePhenotypeAnnotation_asserted_gene" Description: ""
--     * Slot: AllelePhenotypeAnnotation_curie Description: Autocreated FK slot
--     * Slot: asserted_gene Description: The gene(s) to which something is manually asserted to be associated.
-- # Class: "AllelePhenotypeAnnotation_condition_relations" Description: ""
--     * Slot: AllelePhenotypeAnnotation_curie Description: Autocreated FK slot
--     * Slot: condition_relations_id Description: 
-- # Class: "AllelePhenotypeAnnotation_evidence" Description: ""
--     * Slot: AllelePhenotypeAnnotation_curie Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AGMPhenotypeAnnotation_asserted_gene" Description: ""
--     * Slot: AGMPhenotypeAnnotation_curie Description: Autocreated FK slot
--     * Slot: asserted_gene Description: The gene(s) to which something is manually asserted to be associated.
-- # Class: "AGMPhenotypeAnnotation_condition_relations" Description: ""
--     * Slot: AGMPhenotypeAnnotation_curie Description: Autocreated FK slot
--     * Slot: condition_relations_id Description: 
-- # Class: "AGMPhenotypeAnnotation_evidence" Description: ""
--     * Slot: AGMPhenotypeAnnotation_curie Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "DiseaseAnnotation_evidence_codes" Description: ""
--     * Slot: DiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: evidence_codes Description: ECO term IDs
-- # Class: "DiseaseAnnotation_with_or_from" Description: ""
--     * Slot: DiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: with_or_from Description: A field for disease annotations that captures the human gene the implicated MOD gene is homologous or orthologous to when using the ISS (inferred from sequence similarity) evidence code or the ISO (inferred from sequence orthology) evidence code. The assertion would state that the MOD gene is implicated in the indicated disease based on sequence-similarity/sequence-orthology "with" some human gene. Currently used by SGD.
-- # Class: "DiseaseAnnotation_disease_qualifiers" Description: ""
--     * Slot: DiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: disease_qualifiers Description: Submitted values should be vocabulary terms from the 'Disease qualifiers' Vocabulary
-- # Class: "DiseaseAnnotation_condition_relations" Description: ""
--     * Slot: DiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: condition_relations_id Description: 
-- # Class: "DiseaseAnnotation_related_notes" Description: ""
--     * Slot: DiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: related_notes_id Description: Valid note types are available for viewing in the A-Team curation tool Controlled Vocabulary Terms Table (in the "Disease annotation note types" vocabulary) on the production environment (curation.alliancegenome.org). New terms can be added as needed.
-- # Class: "DiseaseAnnotation_evidence" Description: ""
--     * Slot: DiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "DiseaseAnnotationDTO_evidence_curies" Description: ""
--     * Slot: DiseaseAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "DiseaseAnnotationDTO_evidence_code_curies" Description: ""
--     * Slot: DiseaseAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_code_curies Description: List of ECOTerm curies
-- # Class: "DiseaseAnnotationDTO_with_gene_curies" Description: ""
--     * Slot: DiseaseAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: with_gene_curies Description: http://geneontology.org/docs/go-annotation-file-gaf-format-2.2/#with-or-from-column-8
-- # Class: "DiseaseAnnotationDTO_disease_qualifier_names" Description: ""
--     * Slot: DiseaseAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: disease_qualifier_names Description: Names of terms from the 'Disease qualifiers' vocabulary
-- # Class: "GeneDiseaseAnnotation_evidence_codes" Description: ""
--     * Slot: GeneDiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: evidence_codes Description: ECO term IDs
-- # Class: "GeneDiseaseAnnotation_with_or_from" Description: ""
--     * Slot: GeneDiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: with_or_from Description: http://geneontology.org/docs/go-annotation-file-gaf-format-2.2/#with-or-from-column-8
-- # Class: "GeneDiseaseAnnotation_disease_qualifiers" Description: ""
--     * Slot: GeneDiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: disease_qualifiers Description: Submitted values should be vocabulary terms from the 'Disease qualifiers' Vocabulary
-- # Class: "GeneDiseaseAnnotation_condition_relations" Description: ""
--     * Slot: GeneDiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: condition_relations_id Description: 
-- # Class: "GeneDiseaseAnnotation_related_notes" Description: ""
--     * Slot: GeneDiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: related_notes_id Description: Holds between an object and a list of related Note objects.
-- # Class: "GeneDiseaseAnnotation_evidence" Description: ""
--     * Slot: GeneDiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "GeneDiseaseAnnotationDTO_evidence_curies" Description: ""
--     * Slot: GeneDiseaseAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "GeneDiseaseAnnotationDTO_evidence_code_curies" Description: ""
--     * Slot: GeneDiseaseAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_code_curies Description: List of ECOTerm curies
-- # Class: "GeneDiseaseAnnotationDTO_with_gene_curies" Description: ""
--     * Slot: GeneDiseaseAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: with_gene_curies Description: http://geneontology.org/docs/go-annotation-file-gaf-format-2.2/#with-or-from-column-8
-- # Class: "GeneDiseaseAnnotationDTO_disease_qualifier_names" Description: ""
--     * Slot: GeneDiseaseAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: disease_qualifier_names Description: Names of terms from the 'Disease qualifiers' vocabulary
-- # Class: "AlleleDiseaseAnnotation_asserted_gene" Description: ""
--     * Slot: AlleleDiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: asserted_gene Description: The gene(s) to which something is manually asserted to be associated.
-- # Class: "AlleleDiseaseAnnotation_evidence_codes" Description: ""
--     * Slot: AlleleDiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: evidence_codes Description: ECO term IDs
-- # Class: "AlleleDiseaseAnnotation_with_or_from" Description: ""
--     * Slot: AlleleDiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: with_or_from Description: http://geneontology.org/docs/go-annotation-file-gaf-format-2.2/#with-or-from-column-8
-- # Class: "AlleleDiseaseAnnotation_disease_qualifiers" Description: ""
--     * Slot: AlleleDiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: disease_qualifiers Description: Submitted values should be vocabulary terms from the 'Disease qualifiers' Vocabulary
-- # Class: "AlleleDiseaseAnnotation_condition_relations" Description: ""
--     * Slot: AlleleDiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: condition_relations_id Description: 
-- # Class: "AlleleDiseaseAnnotation_related_notes" Description: ""
--     * Slot: AlleleDiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: related_notes_id Description: Holds between an object and a list of related Note objects.
-- # Class: "AlleleDiseaseAnnotation_evidence" Description: ""
--     * Slot: AlleleDiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AlleleDiseaseAnnotationDTO_asserted_gene_curies" Description: ""
--     * Slot: AlleleDiseaseAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: asserted_gene_curies Description: Curies of the gene(s) to which something is manually asserted to be associated
-- # Class: "AlleleDiseaseAnnotationDTO_evidence_curies" Description: ""
--     * Slot: AlleleDiseaseAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "AlleleDiseaseAnnotationDTO_evidence_code_curies" Description: ""
--     * Slot: AlleleDiseaseAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_code_curies Description: List of ECOTerm curies
-- # Class: "AlleleDiseaseAnnotationDTO_with_gene_curies" Description: ""
--     * Slot: AlleleDiseaseAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: with_gene_curies Description: http://geneontology.org/docs/go-annotation-file-gaf-format-2.2/#with-or-from-column-8
-- # Class: "AlleleDiseaseAnnotationDTO_disease_qualifier_names" Description: ""
--     * Slot: AlleleDiseaseAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: disease_qualifier_names Description: Names of terms from the 'Disease qualifiers' vocabulary
-- # Class: "AGMDiseaseAnnotation_asserted_gene" Description: ""
--     * Slot: AGMDiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: asserted_gene Description: The gene(s) to which something is manually asserted to be associated.
-- # Class: "AGMDiseaseAnnotation_evidence_codes" Description: ""
--     * Slot: AGMDiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: evidence_codes Description: ECO term IDs
-- # Class: "AGMDiseaseAnnotation_with_or_from" Description: ""
--     * Slot: AGMDiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: with_or_from Description: http://geneontology.org/docs/go-annotation-file-gaf-format-2.2/#with-or-from-column-8
-- # Class: "AGMDiseaseAnnotation_disease_qualifiers" Description: ""
--     * Slot: AGMDiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: disease_qualifiers Description: Submitted values should be vocabulary terms from the 'Disease qualifiers' Vocabulary
-- # Class: "AGMDiseaseAnnotation_condition_relations" Description: ""
--     * Slot: AGMDiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: condition_relations_id Description: 
-- # Class: "AGMDiseaseAnnotation_related_notes" Description: ""
--     * Slot: AGMDiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: related_notes_id Description: Holds between an object and a list of related Note objects.
-- # Class: "AGMDiseaseAnnotation_evidence" Description: ""
--     * Slot: AGMDiseaseAnnotation_curie Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "AGMDiseaseAnnotationDTO_asserted_gene_curies" Description: ""
--     * Slot: AGMDiseaseAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: asserted_gene_curies Description: Curies of the gene(s) to which something is manually asserted to be associated
-- # Class: "AGMDiseaseAnnotationDTO_evidence_curies" Description: ""
--     * Slot: AGMDiseaseAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "AGMDiseaseAnnotationDTO_evidence_code_curies" Description: ""
--     * Slot: AGMDiseaseAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_code_curies Description: List of ECOTerm curies
-- # Class: "AGMDiseaseAnnotationDTO_with_gene_curies" Description: ""
--     * Slot: AGMDiseaseAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: with_gene_curies Description: http://geneontology.org/docs/go-annotation-file-gaf-format-2.2/#with-or-from-column-8
-- # Class: "AGMDiseaseAnnotationDTO_disease_qualifier_names" Description: ""
--     * Slot: AGMDiseaseAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: disease_qualifier_names Description: Names of terms from the 'Disease qualifiers' vocabulary
-- # Class: "ConditionRelation_conditions" Description: ""
--     * Slot: ConditionRelation_id Description: Autocreated FK slot
--     * Slot: conditions_id Description: 
-- # Class: "AlleleDTO_reference_curies" Description: ""
--     * Slot: AlleleDTO_curie Description: Autocreated FK slot
--     * Slot: reference_curies Description: External reference curies used for ingest
-- # Class: "AlleleDTO_secondary_identifiers" Description: ""
--     * Slot: AlleleDTO_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "CellLineDTO_secondary_identifiers" Description: ""
--     * Slot: CellLineDTO_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "ConstructDTO_construct_component_dtos" Description: ""
--     * Slot: ConstructDTO_curie Description: Autocreated FK slot
--     * Slot: construct_component_dtos Description: 
-- # Class: "ConstructDTO_reference_curies" Description: ""
--     * Slot: ConstructDTO_curie Description: Autocreated FK slot
--     * Slot: reference_curies Description: External reference curies used for ingest
-- # Class: "ConstructDTO_secondary_identifiers" Description: ""
--     * Slot: ConstructDTO_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "GenerationMethodDTO_mutagenesis_method_names" Description: ""
--     * Slot: GenerationMethodDTO_id Description: Autocreated FK slot
--     * Slot: mutagenesis_method_names Description: Name of the VocabularyTerm describing the mutagenesis method, e.g. spontaneous / naturally occurring / radiation-induced / recombinant / ENU / CRISPR / TALEN / gamma rays / not specified / spontaneous / DNA / DNA AND CRISPR / DNA and TALEN / zinc finger nuclease / EMS
-- # Class: "SequenceTargetingReagentDTO_reference_curies" Description: ""
--     * Slot: SequenceTargetingReagentDTO_curie Description: Autocreated FK slot
--     * Slot: reference_curies Description: External reference curies used for ingest
-- # Class: "SequenceTargetingReagentDTO_secondary_identifiers" Description: ""
--     * Slot: SequenceTargetingReagentDTO_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "AlleleDatabaseStatusSlotAnnotationDTO_evidence_curies" Description: ""
--     * Slot: AlleleDatabaseStatusSlotAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "AlleleFunctionalImpactSlotAnnotationDTO_functional_impact_names" Description: ""
--     * Slot: AlleleFunctionalImpactSlotAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: functional_impact_names Description: Name of the VocabularyTerm describing the experimentally assessed functional impact of the allele, e.g. knockout / amorphic
-- # Class: "AlleleFunctionalImpactSlotAnnotationDTO_evidence_curies" Description: ""
--     * Slot: AlleleFunctionalImpactSlotAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "AlleleGermlineTransmissionStatusSlotAnnotationDTO_evidence_curies" Description: ""
--     * Slot: AlleleGermlineTransmissionStatusSlotAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "AlleleInheritanceModeSlotAnnotationDTO_evidence_curies" Description: ""
--     * Slot: AlleleInheritanceModeSlotAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "AlleleMolecularMutationSlotAnnotationDTO_molecular_mutation_names" Description: ""
--     * Slot: AlleleMolecularMutationSlotAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: molecular_mutation_names Description: Name of the VocabularyTerm describing the molecular mutation
-- # Class: "AlleleMolecularMutationSlotAnnotationDTO_evidence_curies" Description: ""
--     * Slot: AlleleMolecularMutationSlotAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "AlleleMutationTypeSlotAnnotationDTO_mutation_type_curies" Description: ""
--     * Slot: AlleleMutationTypeSlotAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: mutation_type_curies Description: Curies of SOTerms representing mutation type
-- # Class: "AlleleMutationTypeSlotAnnotationDTO_evidence_curies" Description: ""
--     * Slot: AlleleMutationTypeSlotAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "AlleleNomenclatureEventSlotAnnotationDTO_evidence_curies" Description: ""
--     * Slot: AlleleNomenclatureEventSlotAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "AlleleNoteSlotAnnotationDTO_evidence_curies" Description: ""
--     * Slot: AlleleNoteSlotAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "AlleleSecondaryIdSlotAnnotationDTO_evidence_curies" Description: ""
--     * Slot: AlleleSecondaryIdSlotAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "AlleleAlleleAssociationDTO_evidence_curies" Description: ""
--     * Slot: AlleleAlleleAssociationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "AlleleCellLineAssociationDTO_evidence_curies" Description: ""
--     * Slot: AlleleCellLineAssociationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "AlleleConstructAssociationDTO_evidence_curies" Description: ""
--     * Slot: AlleleConstructAssociationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "AlleleGeneAssociationDTO_evidence_curies" Description: ""
--     * Slot: AlleleGeneAssociationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "AlleleGenerationMethodAssociationDTO_evidence_curies" Description: ""
--     * Slot: AlleleGenerationMethodAssociationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "AlleleGenomicEntityAssociationDTO_evidence_curies" Description: ""
--     * Slot: AlleleGenomicEntityAssociationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "AlleleImageAssociationDTO_evidence_curies" Description: ""
--     * Slot: AlleleImageAssociationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "AlleleOriginAssociationDTO_evidence_curies" Description: ""
--     * Slot: AlleleOriginAssociationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "AlleleProteinAssociationDTO_evidence_curies" Description: ""
--     * Slot: AlleleProteinAssociationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "AlleleTranscriptAssociationDTO_evidence_curies" Description: ""
--     * Slot: AlleleTranscriptAssociationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "AlleleVariantAssociationDTO_evidence_curies" Description: ""
--     * Slot: AlleleVariantAssociationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "GenomicEntity_cross_reference" Description: ""
--     * Slot: GenomicEntity_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "GenomicEntity_secondary_identifiers" Description: ""
--     * Slot: GenomicEntity_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "GenomicEntity_genomic_location_associations" Description: ""
--     * Slot: GenomicEntity_curie Description: Autocreated FK slot
--     * Slot: genomic_location_associations_id Description: 
-- # Class: "GenomicEntityDTO_secondary_identifiers" Description: ""
--     * Slot: GenomicEntityDTO_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "Transcript_cross_reference" Description: ""
--     * Slot: Transcript_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "Transcript_secondary_identifiers" Description: ""
--     * Slot: Transcript_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "Transcript_genomic_location_associations" Description: ""
--     * Slot: Transcript_curie Description: Autocreated FK slot
--     * Slot: genomic_location_associations_id Description: 
-- # Class: "Note_evidence" Description: ""
--     * Slot: Note_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "NoteDTO_evidence_curies" Description: ""
--     * Slot: NoteDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "SlotAnnotation_evidence" Description: ""
--     * Slot: SlotAnnotation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "SlotAnnotationDTO_evidence_curies" Description: ""
--     * Slot: SlotAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "NameSlotAnnotation_evidence" Description: ""
--     * Slot: NameSlotAnnotation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "NameSlotAnnotationDTO_evidence_curies" Description: ""
--     * Slot: NameSlotAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "SymbolSlotAnnotationDTO_evidence_curies" Description: ""
--     * Slot: SymbolSlotAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "FullNameSlotAnnotationDTO_evidence_curies" Description: ""
--     * Slot: FullNameSlotAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "SystematicNameSlotAnnotationDTO_evidence_curies" Description: ""
--     * Slot: SystematicNameSlotAnnotationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "Association_evidence" Description: ""
--     * Slot: Association_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "GenomicLocationAssociation_evidence" Description: ""
--     * Slot: GenomicLocationAssociation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "GenomicLocationAssociationDTO_evidence_curies" Description: ""
--     * Slot: GenomicLocationAssociationDTO_id Description: Autocreated FK slot
--     * Slot: evidence_curies Description: Curies of InformationContentEntity objects given as evidence
-- # Class: "Protein_cross_reference" Description: ""
--     * Slot: Protein_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "Protein_secondary_identifiers" Description: ""
--     * Slot: Protein_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "Protein_genomic_location_associations" Description: ""
--     * Slot: Protein_curie Description: Autocreated FK slot
--     * Slot: genomic_location_associations_id Description: 
-- # Class: "ResourceDescriptor_synonyms" Description: ""
--     * Slot: ResourceDescriptor_id Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "ResourceDescriptor_resource_pages" Description: ""
--     * Slot: ResourceDescriptor_id Description: Autocreated FK slot
--     * Slot: resource_pages_id Description: Pages for a particular resource
-- # Class: "AffectedGenomicModel_component" Description: ""
--     * Slot: AffectedGenomicModel_curie Description: Autocreated FK slot
--     * Slot: component_id Description: Collection of genomic components that make up a model, i.e. 'allele', each with a zygosity
-- # Class: "AffectedGenomicModel_sequence_targeting_reagent" Description: ""
--     * Slot: AffectedGenomicModel_curie Description: Autocreated FK slot
--     * Slot: sequence_targeting_reagent Description: 
-- # Class: "AffectedGenomicModel_reference" Description: ""
--     * Slot: AffectedGenomicModel_curie Description: Autocreated FK slot
--     * Slot: reference Description: holds between an object and a list of references
-- # Class: "AffectedGenomicModel_cross_reference" Description: ""
--     * Slot: AffectedGenomicModel_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "AffectedGenomicModel_secondary_identifiers" Description: ""
--     * Slot: AffectedGenomicModel_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "AffectedGenomicModel_genomic_location_associations" Description: ""
--     * Slot: AffectedGenomicModel_curie Description: Autocreated FK slot
--     * Slot: genomic_location_associations_id Description: 
-- # Class: "AffectedGenomicModelDTO_reference_curies" Description: ""
--     * Slot: AffectedGenomicModelDTO_curie Description: Autocreated FK slot
--     * Slot: reference_curies Description: External reference curies used for ingest
-- # Class: "AffectedGenomicModelDTO_sequence_targeting_reagent_curies" Description: ""
--     * Slot: AffectedGenomicModelDTO_curie Description: Autocreated FK slot
--     * Slot: sequence_targeting_reagent_curies Description: 
-- # Class: "AffectedGenomicModelDTO_secondary_identifiers" Description: ""
--     * Slot: AffectedGenomicModelDTO_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "VocabularyTerm_text_synonyms" Description: ""
--     * Slot: VocabularyTerm_name Description: Autocreated FK slot
--     * Slot: text_synonyms Description: Free text synonym(s) of a term, used for controlled vocabulary terms; this is distinct from the 'synonyms' slot which has a range of a Synonym class object.
-- # Class: "Vocabulary_member_terms" Description: ""
--     * Slot: Vocabulary_name Description: Autocreated FK slot
--     * Slot: member_terms Description: Set of VocabularyTerm objects in a Vocabulary object set
-- # Class: "VocabularyTermSet_member_terms" Description: ""
--     * Slot: VocabularyTermSet_name Description: Autocreated FK slot
--     * Slot: member_terms Description: Set of VocabularyTerm objects in a Vocabulary object set
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
-- # Class: "AuthorReference_cross_reference" Description: ""
--     * Slot: AuthorReference_id Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "Reference_authors" Description: ""
--     * Slot: Reference_curie Description: Autocreated FK slot
--     * Slot: authors_id Description: Ordered author entities for this publication.  An Author is associated with only one publication.  A Person can be associated with multiple publications.
-- # Class: "Reference_date_arrived_in_pubmed" Description: ""
--     * Slot: Reference_curie Description: Autocreated FK slot
--     * Slot: date_arrived_in_pubmed Description: Day in which a reference or resource was created in PubMed. Only relevant for PubMed references.
-- # Class: "Reference_keywords" Description: ""
--     * Slot: Reference_curie Description: Autocreated FK slot
--     * Slot: keywords Description: Keywords tagging a publication.  Aggregation of PubMed and ZFIN, editable at Alliance.
-- # Class: "Reference_pubmed_abstract_languages" Description: ""
--     * Slot: Reference_curie Description: Autocreated FK slot
--     * Slot: pubmed_abstract_languages Description: Languages for the abstract. Only relevant for PubMed references.
-- # Class: "Reference_pubmed_type" Description: ""
--     * Slot: Reference_curie Description: Autocreated FK slot
--     * Slot: pubmed_type Description: Type of Reference as described by PubMed. Only relevant for PubMed references.
-- # Class: "Resource_synonyms" Description: ""
--     * Slot: Resource_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "Resource_authors" Description: ""
--     * Slot: Resource_curie Description: Autocreated FK slot
--     * Slot: authors_id Description: Ordered author entities for this publication.  An Author is associated with only one publication.  A Person can be associated with multiple publications.
-- # Class: "Resource_editor" Description: ""
--     * Slot: Resource_curie Description: Autocreated FK slot
--     * Slot: editor_id Description: holds between a resource and a editor_resource
-- # Class: "Gene_gene_synonyms" Description: ""
--     * Slot: Gene_curie Description: Autocreated FK slot
--     * Slot: gene_synonyms_id Description: Holds between a Gene and a synonym.
-- # Class: "Gene_related_notes" Description: ""
--     * Slot: Gene_curie Description: Autocreated FK slot
--     * Slot: related_notes_id Description: Valid note types are available for viewing in the A-Team curation tool Controlled Vocabulary Terms Table (in the "Gene note types" vocabulary) on the production environment (curation.alliancegenome.org). New terms can be added as needed.
-- # Class: "Gene_gene_types_secondary" Description: ""
--     * Slot: Gene_curie Description: Autocreated FK slot
--     * Slot: gene_types_secondary Description: SOTerm describing alternate gene types
-- # Class: "Gene_designating_laboratories" Description: ""
--     * Slot: Gene_curie Description: Autocreated FK slot
--     * Slot: designating_laboratories Description: A laboratory, rarely laboratories, which designated this gene
-- # Class: "Gene_designating_persons" Description: ""
--     * Slot: Gene_curie Description: Autocreated FK slot
--     * Slot: designating_persons Description: A person/persons who designated this gene
-- # Class: "Gene_trans_splice_leaders" Description: ""
--     * Slot: Gene_curie Description: Autocreated FK slot
--     * Slot: trans_splice_leaders Description: Trans-splicing splice leaders observed to operate on this gene, in species which have spliced leader trans-splicing
-- # Class: "Gene_contig" Description: ""
--     * Slot: Gene_curie Description: Autocreated FK slot
--     * Slot: contig Description: Contig or clone this gene is located to
-- # Class: "Gene_anatomy_function" Description: ""
--     * Slot: Gene_curie Description: Autocreated FK slot
--     * Slot: anatomy_function Description: WB specific. Allow the connection between Anatomy_term, Phenotype and gene Eg WBbtf0001
-- # Class: "Gene_product_binds_matrix" Description: ""
--     * Slot: Gene_curie Description: Autocreated FK slot
--     * Slot: product_binds_matrix Description: WB specific. ID of position matrix object
-- # Class: "Gene_wbprocess" Description: ""
--     * Slot: Gene_curie Description: Autocreated FK slot
--     * Slot: wbprocess Description: WB specific. Eg WBbiop00000015 Corpse engulfment
-- # Class: "Gene_cross_reference" Description: ""
--     * Slot: Gene_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "Gene_secondary_identifiers" Description: ""
--     * Slot: Gene_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "Gene_genomic_location_associations" Description: ""
--     * Slot: Gene_curie Description: Autocreated FK slot
--     * Slot: genomic_location_associations_id Description: 
-- # Class: "GeneDTO_secondary_identifiers" Description: ""
--     * Slot: GeneDTO_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "GeneSymbolSlotAnnotation_evidence" Description: ""
--     * Slot: GeneSymbolSlotAnnotation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "GeneFullNameSlotAnnotation_evidence" Description: ""
--     * Slot: GeneFullNameSlotAnnotation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "GeneSystematicNameSlotAnnotation_evidence" Description: ""
--     * Slot: GeneSystematicNameSlotAnnotation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "GeneSynonymSlotAnnotation_evidence" Description: ""
--     * Slot: GeneSynonymSlotAnnotation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "GeneticMapPosition_genetic_map_position_centimorgan" Description: ""
--     * Slot: GeneticMapPosition_curie Description: Autocreated FK slot
--     * Slot: genetic_map_position_centimorgan Description: Genetic map predicted chromosome location in centimorgans eg 22.3366 cM
-- # Class: "GeneticMapPosition_genetic_map_position_centimorgan_error" Description: ""
--     * Slot: GeneticMapPosition_curie Description: Autocreated FK slot
--     * Slot: genetic_map_position_centimorgan_error Description: Genetic map calculated error in the predicted chromosome location in centimorgans eg 0.045 cM
-- # Class: "GeneticMapPosition_genetic_map_position_radiation" Description: ""
--     * Slot: GeneticMapPosition_curie Description: Autocreated FK slot
--     * Slot: genetic_map_position_radiation Description: Radiation hybrid map predicted chromosome location eg 66.5 cR
-- # Class: "GeneticMapPosition_cross_reference" Description: ""
--     * Slot: GeneticMapPosition_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "GeneticMapPosition_secondary_identifiers" Description: ""
--     * Slot: GeneticMapPosition_curie Description: Autocreated FK slot
--     * Slot: secondary_identifiers Description: 
-- # Class: "GeneticMapPosition_genomic_location_associations" Description: ""
--     * Slot: GeneticMapPosition_curie Description: Autocreated FK slot
--     * Slot: genomic_location_associations_id Description: 
-- # Class: "GeneHistory_current_status" Description: ""
--     * Slot: GeneHistory_id Description: Autocreated FK slot
--     * Slot: current_status Description: Current status of this object
-- # Class: "GeneHistory_merged_into" Description: ""
--     * Slot: GeneHistory_id Description: Autocreated FK slot
--     * Slot: merged_into Description: This gene has been merged into
-- # Class: "GeneHistory_acquires_merge" Description: ""
--     * Slot: GeneHistory_id Description: Autocreated FK slot
--     * Slot: acquires_merge Description: Genes which have been merged into this gene
-- # Class: "GeneHistory_split_from" Description: ""
--     * Slot: GeneHistory_id Description: Autocreated FK slot
--     * Slot: split_from Description: This gene exists because it has been split from this gene
-- # Class: "GeneHistory_split_into" Description: ""
--     * Slot: GeneHistory_id Description: Autocreated FK slot
--     * Slot: split_into Description: This gene has been split into these genes
-- # Class: "Reagent_generated_by" Description: ""
--     * Slot: Reagent_curie Description: Autocreated FK slot
--     * Slot: generated_by_id Description: Holds between a material entity and an Agent that generated it: e.g., Thomas Blumenthal, Kornberg Laboratory.
-- # Class: "Reagent_manufactured_by" Description: ""
--     * Slot: Reagent_curie Description: Autocreated FK slot
--     * Slot: manufactured_by_id Description: Holds between a material entity and an Agent that has manufactured it: e.g., Molecular Probes.
-- # Class: "Antibody_antibody_target_genes" Description: ""
--     * Slot: Antibody_curie Description: Autocreated FK slot
--     * Slot: antibody_target_genes Description: The genes whose gene products are recognized by the antibody.
-- # Class: "Antibody_cross_reference" Description: ""
--     * Slot: Antibody_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
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
-- # Class: "GeneToGeneAssociation_evidence" Description: ""
--     * Slot: GeneToGeneAssociation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "GeneInteraction_cross_reference" Description: ""
--     * Slot: GeneInteraction_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Additional identifier(s) of the interaction annotation other than the primary id.
-- # Class: "GeneInteraction_interactor_A_role" Description: ""
--     * Slot: GeneInteraction_curie Description: Autocreated FK slot
--     * Slot: interactor_A_role Description: 
-- # Class: "GeneInteraction_interactor_B_role" Description: ""
--     * Slot: GeneInteraction_curie Description: Autocreated FK slot
--     * Slot: interactor_B_role Description: 
-- # Class: "GeneInteraction_evidence" Description: ""
--     * Slot: GeneInteraction_curie Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "GeneMolecularInteraction_cross_reference" Description: ""
--     * Slot: GeneMolecularInteraction_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "GeneMolecularInteraction_interactor_A_role" Description: ""
--     * Slot: GeneMolecularInteraction_curie Description: Autocreated FK slot
--     * Slot: interactor_A_role Description: 
-- # Class: "GeneMolecularInteraction_interactor_B_role" Description: ""
--     * Slot: GeneMolecularInteraction_curie Description: Autocreated FK slot
--     * Slot: interactor_B_role Description: 
-- # Class: "GeneMolecularInteraction_evidence" Description: ""
--     * Slot: GeneMolecularInteraction_curie Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "GeneGeneticInteraction_phenotype_or_trait" Description: ""
--     * Slot: GeneGeneticInteraction_curie Description: Autocreated FK slot
--     * Slot: phenotype_or_trait Description: 
-- # Class: "GeneGeneticInteraction_cross_reference" Description: ""
--     * Slot: GeneGeneticInteraction_curie Description: Autocreated FK slot
--     * Slot: cross_reference_id Description: Holds between an object and its CrossReferences.
-- # Class: "GeneGeneticInteraction_interactor_A_role" Description: ""
--     * Slot: GeneGeneticInteraction_curie Description: Autocreated FK slot
--     * Slot: interactor_A_role Description: 
-- # Class: "GeneGeneticInteraction_interactor_B_role" Description: ""
--     * Slot: GeneGeneticInteraction_curie Description: Autocreated FK slot
--     * Slot: interactor_B_role Description: 
-- # Class: "GeneGeneticInteraction_evidence" Description: ""
--     * Slot: GeneGeneticInteraction_curie Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "ExpressionExperiment_reagents_used" Description: ""
--     * Slot: ExpressionExperiment_curie Description: Autocreated FK slot
--     * Slot: reagents_used Description: Reagents used in the expression assay: e.g., antibodies, probes.
-- # Class: "ExpressionExperiment_specimen_alleles" Description: ""
--     * Slot: ExpressionExperiment_curie Description: Autocreated FK slot
--     * Slot: specimen_alleles Description: The Allele(s) of the specimen assayed.
-- # Class: "ExpressionExperiment_condition_relations" Description: ""
--     * Slot: ExpressionExperiment_curie Description: Autocreated FK slot
--     * Slot: condition_relations_id Description: 
-- # Class: "ExpressionExperiment_related_notes" Description: ""
--     * Slot: ExpressionExperiment_curie Description: Autocreated FK slot
--     * Slot: related_notes_id Description: Holds between an object and a list of related Note objects.
-- # Class: "ExpressionAnnotation_associated_with_figure" Description: ""
--     * Slot: ExpressionAnnotation_id Description: Autocreated FK slot
--     * Slot: associated_with_figure Description: The figure(s) that support(s) the expression annotation.
-- # Class: "ExpressionAnnotation_related_notes" Description: ""
--     * Slot: ExpressionAnnotation_id Description: Autocreated FK slot
--     * Slot: related_notes_id Description: Holds between an object and a list of related Note objects.
-- # Class: "ExpressionAnnotationImagePane_evidence" Description: ""
--     * Slot: ExpressionAnnotationImagePane_id Description: Autocreated FK slot
--     * Slot: evidence Description: 
-- # Class: "BulkLoadGroup_loads" Description: ""
--     * Slot: BulkLoadGroup_id Description: Autocreated FK slot
--     * Slot: loads_id Description: 
-- # Class: "BulkLoad_load_files" Description: ""
--     * Slot: BulkLoad_id Description: Autocreated FK slot
--     * Slot: load_files_id Description: 
-- # Class: "BulkScheduledLoad_load_files" Description: ""
--     * Slot: BulkScheduledLoad_id Description: Autocreated FK slot
--     * Slot: load_files_id Description: 
-- # Class: "BulkFMSLoad_load_files" Description: ""
--     * Slot: BulkFMSLoad_id Description: Autocreated FK slot
--     * Slot: load_files_id Description: 
-- # Class: "BulkURLLoad_load_files" Description: ""
--     * Slot: BulkURLLoad_id Description: Autocreated FK slot
--     * Slot: load_files_id Description: 
-- # Class: "BulkManualLoad_load_files" Description: ""
--     * Slot: BulkManualLoad_id Description: Autocreated FK slot
--     * Slot: load_files_id Description: 
-- # Class: "BulkLoadFileHistory_load_exceptions" Description: ""
--     * Slot: BulkLoadFileHistory_id Description: Autocreated FK slot
--     * Slot: load_exceptions Description: A list of execeptions the load encountered
-- # Class: "GeneCluster_genes" Description: ""
--     * Slot: GeneCluster_curie Description: Autocreated FK slot
--     * Slot: genes Description: 
-- # Class: "GeneCollection_genes" Description: ""
--     * Slot: GeneCollection_curie Description: Autocreated FK slot
--     * Slot: genes Description: 
-- # Class: "GeneCollection_experiment_type" Description: ""
--     * Slot: GeneCollection_curie Description: Autocreated FK slot
--     * Slot: experiment_type Description: Type of experiment by which these genes were collated eg chip-seq, interaction, expression
-- # Class: "GeneNomenclatureSet_genes" Description: ""
--     * Slot: GeneNomenclatureSet_curie Description: Autocreated FK slot
--     * Slot: genes Description: 
-- # Class: "GeneNomenclatureSet_old_members" Description: ""
--     * Slot: GeneNomenclatureSet_curie Description: Autocreated FK slot
--     * Slot: old_members Description: Gene which were formerly members of this GeneClass
-- # Class: "GeneNomenclatureSet_synonyms" Description: ""
--     * Slot: GeneNomenclatureSet_curie Description: Autocreated FK slot
--     * Slot: synonyms Description: Placeholder? Some objects still use this slot. Not clear how it fits in with NameSlotAnnotation (which captures evidence).
-- # Class: "Operon_genes" Description: ""
--     * Slot: Operon_curie Description: Autocreated FK slot
--     * Slot: genes Description: 
-- # Class: "UniGeneSet_genes" Description: ""
--     * Slot: UniGeneSet_curie Description: Autocreated FK slot
--     * Slot: genes Description: 
-- # Class: "FunctionalGeneSet_genes" Description: ""
--     * Slot: FunctionalGeneSet_curie Description: Autocreated FK slot
--     * Slot: genes Description: 
-- # Class: "ProteinComplex_proteins" Description: ""
--     * Slot: ProteinComplex_curie Description: Autocreated FK slot
--     * Slot: proteins Description: 
-- # Class: "GeneToPathwayAssociation_evidence" Description: ""
--     * Slot: GeneToPathwayAssociation_id Description: Autocreated FK slot
--     * Slot: evidence Description: 

CREATE TABLE "Allele" (
	in_collection TEXT, 
	laboratory_of_origin TEXT, 
	is_extinct BOOLEAN, 
	is_extrachromosomal BOOLEAN, 
	is_integrated BOOLEAN, 
	transgene_chromosome_location TEXT, 
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	allele_symbol_id TEXT NOT NULL, 
	allele_full_name_id TEXT, 
	allele_germline_transmission_status_id TEXT, 
	allele_database_status_id TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(in_collection) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(laboratory_of_origin) REFERENCES "Laboratory" (curie), 
	FOREIGN KEY(transgene_chromosome_location) REFERENCES "Chromosome" (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(allele_symbol_id) REFERENCES "AlleleSymbolSlotAnnotation" (id), 
	FOREIGN KEY(allele_full_name_id) REFERENCES "AlleleFullNameSlotAnnotation" (id), 
	FOREIGN KEY(allele_germline_transmission_status_id) REFERENCES "AlleleGermlineTransmissionStatusSlotAnnotation" (id), 
	FOREIGN KEY(allele_database_status_id) REFERENCES "AlleleDatabaseStatusSlotAnnotation" (id)
);
CREATE TABLE "AlleleDatabaseStatusSlotAnnotation" (
	id INTEGER, 
	single_allele TEXT NOT NULL, 
	database_status TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_allele) REFERENCES "Allele" (curie), 
	FOREIGN KEY(database_status) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AlleleFullNameSlotAnnotation" (
	id INTEGER, 
	single_allele TEXT NOT NULL, 
	name_type TEXT NOT NULL, 
	format_text TEXT NOT NULL, 
	display_text TEXT NOT NULL, 
	synonym_url TEXT, 
	synonym_scope TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_allele) REFERENCES "Allele" (curie), 
	FOREIGN KEY(name_type) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(synonym_scope) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AlleleGermlineTransmissionStatusSlotAnnotation" (
	id INTEGER, 
	single_allele TEXT NOT NULL, 
	germline_transmission_status TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_allele) REFERENCES "Allele" (curie), 
	FOREIGN KEY(germline_transmission_status) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AlleleSymbolSlotAnnotation" (
	id INTEGER, 
	single_allele TEXT NOT NULL, 
	name_type TEXT NOT NULL, 
	format_text TEXT NOT NULL, 
	display_text TEXT NOT NULL, 
	synonym_url TEXT, 
	synonym_scope TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_allele) REFERENCES "Allele" (curie), 
	FOREIGN KEY(name_type) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(synonym_scope) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "CellLineDTO" (
	curie TEXT NOT NULL, 
	taxon_curie TEXT NOT NULL, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie)
);
CREATE TABLE "ConstructDTO" (
	curie TEXT NOT NULL, 
	taxon_curie TEXT NOT NULL, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie)
);
CREATE TABLE "GenerationMethodDTO" (
	id INTEGER, 
	mutagenesis_target TEXT, 
	integration_method_name TEXT, 
	chemical_mutagen_name TEXT, 
	irradiation_mutagen_name TEXT, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id)
);
CREATE TABLE "AlleleDatabaseStatusSlotAnnotationDTO" (
	id INTEGER, 
	database_status_name TEXT NOT NULL, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id)
);
CREATE TABLE "AlleleGermlineTransmissionStatusSlotAnnotationDTO" (
	id INTEGER, 
	germline_transmission_status_name TEXT NOT NULL, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id)
);
CREATE TABLE "AuditedObjectDTO" (
	id INTEGER, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id)
);
CREATE TABLE "BiologicalEntityDTO" (
	curie TEXT NOT NULL, 
	taxon_curie TEXT NOT NULL, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie)
);
CREATE TABLE "GenomicEntityDTO" (
	curie TEXT NOT NULL, 
	taxon_curie TEXT NOT NULL, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie)
);
CREATE TABLE "CrossReferenceDTO" (
	id INTEGER, 
	referenced_curie TEXT NOT NULL, 
	page_area TEXT NOT NULL, 
	display_name TEXT NOT NULL, 
	prefix TEXT NOT NULL, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"AlleleDTO_curie" TEXT, 
	"CellLineDTO_curie" TEXT, 
	"ConstructDTO_curie" TEXT, 
	"SequenceTargetingReagentDTO_curie" TEXT, 
	"GenomicEntityDTO_curie" TEXT, 
	"AffectedGenomicModelDTO_curie" TEXT, 
	"GeneDTO_curie" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("AlleleDTO_curie") REFERENCES "AlleleDTO" (curie), 
	FOREIGN KEY("CellLineDTO_curie") REFERENCES "CellLineDTO" (curie), 
	FOREIGN KEY("ConstructDTO_curie") REFERENCES "ConstructDTO" (curie), 
	FOREIGN KEY("SequenceTargetingReagentDTO_curie") REFERENCES "SequenceTargetingReagentDTO" (curie), 
	FOREIGN KEY("GenomicEntityDTO_curie") REFERENCES "GenomicEntityDTO" (curie), 
	FOREIGN KEY("AffectedGenomicModelDTO_curie") REFERENCES "AffectedGenomicModelDTO" (curie), 
	FOREIGN KEY("GeneDTO_curie") REFERENCES "GeneDTO" (curie)
);
CREATE TABLE "DataProviderDTO" (
	id INTEGER, 
	source_organization_abbreviation TEXT NOT NULL, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	cross_reference_dto_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(cross_reference_dto_id) REFERENCES "CrossReferenceDTO" (id)
);
CREATE TABLE "SlotAnnotationDTO" (
	id INTEGER, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id)
);
CREATE TABLE "SymbolSlotAnnotationDTO" (
	id INTEGER, 
	name_type_name TEXT NOT NULL, 
	format_text TEXT NOT NULL, 
	display_text TEXT NOT NULL, 
	synonym_url TEXT, 
	synonym_scope_name TEXT, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id)
);
CREATE TABLE "FullNameSlotAnnotationDTO" (
	id INTEGER, 
	name_type_name TEXT NOT NULL, 
	format_text TEXT NOT NULL, 
	display_text TEXT NOT NULL, 
	synonym_url TEXT, 
	synonym_scope_name TEXT, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id)
);
CREATE TABLE "SystematicNameSlotAnnotationDTO" (
	id INTEGER, 
	name_type_name TEXT NOT NULL, 
	format_text TEXT NOT NULL, 
	display_text TEXT NOT NULL, 
	synonym_url TEXT, 
	synonym_scope_name TEXT, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id)
);
CREATE TABLE "Identifier" (
	counter INTEGER, 
	subdomain_code TEXT, 
	subdomain_name TEXT, 
	curie TEXT, 
	PRIMARY KEY (curie)
);
CREATE TABLE "ResourceDescriptorPage" (
	id INTEGER, 
	name TEXT NOT NULL, 
	url_template TEXT, 
	page_description TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AffectedGenomicModelDTO" (
	name TEXT, 
	subtype_name TEXT NOT NULL, 
	curie TEXT NOT NULL, 
	taxon_curie TEXT NOT NULL, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	data_provider_dto_id TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id), 
	FOREIGN KEY(data_provider_dto_id) REFERENCES "DataProviderDTO" (id)
);
CREATE TABLE "Person" (
	last_name TEXT, 
	middle_name TEXT, 
	first_name TEXT, 
	orcid TEXT, 
	mod_entity_id TEXT, 
	unique_id TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	affiliated_alliance_member_id TEXT, 
	PRIMARY KEY (unique_id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(affiliated_alliance_member_id) REFERENCES "AllianceMember" (id)
);
CREATE TABLE "AllianceMember" (
	id INTEGER, 
	alliance_member_id INTEGER NOT NULL, 
	abbreviation TEXT NOT NULL, 
	full_name TEXT NOT NULL, 
	short_name TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME NOT NULL, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	homepage_resource_descriptor_page_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(homepage_resource_descriptor_page_id) REFERENCES "ResourceDescriptorPage" (id)
);
CREATE TABLE "Gene" (
	gene_type TEXT, 
	transposon_origin BOOLEAN, 
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	gene_symbol_id TEXT NOT NULL, 
	gene_full_name_id TEXT, 
	gene_systematic_name_id TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(gene_type) REFERENCES "SOTerm" (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(gene_symbol_id) REFERENCES "GeneSymbolSlotAnnotation" (id), 
	FOREIGN KEY(gene_full_name_id) REFERENCES "GeneFullNameSlotAnnotation" (id), 
	FOREIGN KEY(gene_systematic_name_id) REFERENCES "GeneSystematicNameSlotAnnotation" (id)
);
CREATE TABLE "GeneSymbolSlotAnnotation" (
	id INTEGER, 
	single_gene TEXT NOT NULL, 
	name_type TEXT NOT NULL, 
	format_text TEXT NOT NULL, 
	display_text TEXT NOT NULL, 
	synonym_url TEXT, 
	synonym_scope TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_gene) REFERENCES "Gene" (curie), 
	FOREIGN KEY(name_type) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(synonym_scope) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "GeneFullNameSlotAnnotation" (
	id INTEGER, 
	single_gene TEXT NOT NULL, 
	name_type TEXT NOT NULL, 
	format_text TEXT NOT NULL, 
	display_text TEXT NOT NULL, 
	synonym_url TEXT, 
	synonym_scope TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_gene) REFERENCES "Gene" (curie), 
	FOREIGN KEY(name_type) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(synonym_scope) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "GeneSystematicNameSlotAnnotation" (
	id INTEGER, 
	single_gene TEXT NOT NULL, 
	name_type TEXT NOT NULL, 
	format_text TEXT NOT NULL, 
	display_text TEXT NOT NULL, 
	synonym_url TEXT, 
	synonym_scope TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_gene) REFERENCES "Gene" (curie), 
	FOREIGN KEY(name_type) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(synonym_scope) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Ingest" (
	id INTEGER, 
	linkml_version TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "OntologyTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "DOTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
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
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "NCBITaxonTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "FBCVTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "GOTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "ROTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "MITerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "MMOTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "MMUSDVTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "SOTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "XBEDTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
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
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "StageTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "FBDVTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "WBLSTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "XBSTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "ZFSTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "ExperimentalConditionOntologyTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "ZECOTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "XCOTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AnatomicalTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "CLTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "EMAPATerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "DAOTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "MATerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "UBERONTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "WBBTTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "XBATerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "ZFATerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "PhenotypeTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "XPOTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "MPTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "ATPTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	namespace TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
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
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
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
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Molecule" (
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
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AlleleMolecularMutationSlotAnnotation" (
	id INTEGER, 
	single_allele TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_allele) REFERENCES "Allele" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AlleleMutationTypeSlotAnnotation" (
	id INTEGER, 
	single_allele TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_allele) REFERENCES "Allele" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AlleleSecondaryIdSlotAnnotation" (
	id INTEGER, 
	single_allele TEXT NOT NULL, 
	secondary_id TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_allele) REFERENCES "Allele" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "DiseaseAnnotationDTO" (
	id INTEGER, 
	disease_relation_name TEXT NOT NULL, 
	do_term_curie TEXT NOT NULL, 
	mod_entity_id TEXT, 
	negated BOOLEAN, 
	reference_curie TEXT, 
	annotation_type_name TEXT, 
	genetic_sex_name TEXT, 
	disease_genetic_modifier_curie TEXT, 
	disease_genetic_modifier_relation_name TEXT, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	data_provider_dto_id TEXT NOT NULL, 
	secondary_data_provider_dto_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(data_provider_dto_id) REFERENCES "DataProviderDTO" (id), 
	FOREIGN KEY(secondary_data_provider_dto_id) REFERENCES "DataProviderDTO" (id)
);
CREATE TABLE "GeneDiseaseAnnotationDTO" (
	id INTEGER, 
	gene_curie TEXT NOT NULL, 
	sgd_strain_background_curie TEXT, 
	disease_relation_name TEXT NOT NULL, 
	do_term_curie TEXT NOT NULL, 
	mod_entity_id TEXT, 
	negated BOOLEAN, 
	reference_curie TEXT, 
	annotation_type_name TEXT, 
	genetic_sex_name TEXT, 
	disease_genetic_modifier_curie TEXT, 
	disease_genetic_modifier_relation_name TEXT, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	data_provider_dto_id TEXT NOT NULL, 
	secondary_data_provider_dto_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id), 
	FOREIGN KEY(data_provider_dto_id) REFERENCES "DataProviderDTO" (id), 
	FOREIGN KEY(secondary_data_provider_dto_id) REFERENCES "DataProviderDTO" (id)
);
CREATE TABLE "AlleleDiseaseAnnotationDTO" (
	id INTEGER, 
	allele_curie TEXT NOT NULL, 
	inferred_gene_curie TEXT, 
	disease_relation_name TEXT NOT NULL, 
	do_term_curie TEXT NOT NULL, 
	mod_entity_id TEXT, 
	negated BOOLEAN, 
	reference_curie TEXT, 
	annotation_type_name TEXT, 
	genetic_sex_name TEXT, 
	disease_genetic_modifier_curie TEXT, 
	disease_genetic_modifier_relation_name TEXT, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	data_provider_dto_id TEXT NOT NULL, 
	secondary_data_provider_dto_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id), 
	FOREIGN KEY(data_provider_dto_id) REFERENCES "DataProviderDTO" (id), 
	FOREIGN KEY(secondary_data_provider_dto_id) REFERENCES "DataProviderDTO" (id)
);
CREATE TABLE "AGMDiseaseAnnotationDTO" (
	id INTEGER, 
	agm_curie TEXT NOT NULL, 
	inferred_gene_curie TEXT, 
	inferred_allele_curie TEXT, 
	asserted_allele_curie TEXT, 
	disease_relation_name TEXT NOT NULL, 
	do_term_curie TEXT NOT NULL, 
	mod_entity_id TEXT, 
	negated BOOLEAN, 
	reference_curie TEXT, 
	annotation_type_name TEXT, 
	genetic_sex_name TEXT, 
	disease_genetic_modifier_curie TEXT, 
	disease_genetic_modifier_relation_name TEXT, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	data_provider_dto_id TEXT NOT NULL, 
	secondary_data_provider_dto_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id), 
	FOREIGN KEY(data_provider_dto_id) REFERENCES "DataProviderDTO" (id), 
	FOREIGN KEY(secondary_data_provider_dto_id) REFERENCES "DataProviderDTO" (id)
);
CREATE TABLE "AlleleDTO" (
	in_collection_name TEXT, 
	laboratory_of_origin_curie TEXT, 
	is_extinct BOOLEAN, 
	is_extrachromosomal BOOLEAN, 
	is_integrated BOOLEAN, 
	transgene_chromosome_location_curie TEXT, 
	curie TEXT NOT NULL, 
	taxon_curie TEXT NOT NULL, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	allele_symbol_dto_id TEXT NOT NULL, 
	allele_full_name_dto_id TEXT, 
	allele_germline_transmission_status_dto_id TEXT, 
	allele_database_status_dto_id TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id), 
	FOREIGN KEY(allele_symbol_dto_id) REFERENCES "SymbolSlotAnnotationDTO" (id), 
	FOREIGN KEY(allele_full_name_dto_id) REFERENCES "FullNameSlotAnnotationDTO" (id), 
	FOREIGN KEY(allele_germline_transmission_status_dto_id) REFERENCES "AlleleGermlineTransmissionStatusSlotAnnotationDTO" (id), 
	FOREIGN KEY(allele_database_status_dto_id) REFERENCES "AlleleDatabaseStatusSlotAnnotationDTO" (id)
);
CREATE TABLE "SequenceTargetingReagentDTO" (
	curie TEXT NOT NULL, 
	taxon_curie TEXT NOT NULL, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id)
);
CREATE TABLE "AlleleCellLineAssociationDTO" (
	id INTEGER, 
	allele_curie TEXT NOT NULL, 
	predicate_name TEXT NOT NULL, 
	cell_line_curie TEXT NOT NULL, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id)
);
CREATE TABLE "AlleleGenerationMethodAssociationDTO" (
	id INTEGER, 
	allele_curie TEXT NOT NULL, 
	predicate_name TEXT NOT NULL, 
	mutation_target_strain_curie TEXT, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	generation_method_dto_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id), 
	FOREIGN KEY(generation_method_dto_id) REFERENCES "GenerationMethodDTO" (id)
);
CREATE TABLE "AlleleImageAssociationDTO" (
	id INTEGER, 
	allele_curie TEXT NOT NULL, 
	predicate_name TEXT NOT NULL, 
	image_curie TEXT NOT NULL, 
	primary_image BOOLEAN, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id)
);
CREATE TABLE "AlleleOriginAssociationDTO" (
	id INTEGER, 
	allele_curie TEXT NOT NULL, 
	predicate_name TEXT NOT NULL, 
	agm_curie TEXT NOT NULL, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id)
);
CREATE TABLE "AuditedObject" (
	id INTEGER, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "CrossReference" (
	id INTEGER, 
	referenced_curie TEXT NOT NULL, 
	display_name TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	resource_descriptor_page_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(resource_descriptor_page_id) REFERENCES "ResourceDescriptorPage" (id)
);
CREATE TABLE "SlotAnnotation" (
	id INTEGER, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Association" (
	id INTEGER, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
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
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Chromosome" (
	curie TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Assembly" (
	curie TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "IdentifiersRange" (
	id INTEGER, 
	first TEXT, 
	last TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(first) REFERENCES "Identifier" (curie), 
	FOREIGN KEY(last) REFERENCES "Identifier" (curie)
);
CREATE TABLE "ResourceDescriptor" (
	id INTEGER, 
	prefix TEXT NOT NULL, 
	name TEXT, 
	id_pattern TEXT, 
	id_example TEXT, 
	default_url_template TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AffectedGenomicModelComponent" (
	id INTEGER, 
	single_allele TEXT, 
	zygosity VARCHAR(12), 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_allele) REFERENCES "Allele" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AffectedGenomicModelComponentDTO" (
	id INTEGER, 
	allele_curie TEXT NOT NULL, 
	zygosity_curie TEXT, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"AffectedGenomicModelDTO_curie" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("AffectedGenomicModelDTO_curie") REFERENCES "AffectedGenomicModelDTO" (curie)
);
CREATE TABLE "VocabularyTerm" (
	name TEXT NOT NULL, 
	abbreviation TEXT, 
	definition TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (name), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Vocabulary" (
	name TEXT NOT NULL, 
	vocabulary_description TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (name), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "File" (
	id INTEGER, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Agent" (
	id INTEGER, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Organization" (
	id INTEGER, 
	abbreviation TEXT, 
	full_name TEXT NOT NULL, 
	short_name TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	homepage_resource_descriptor_page_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(homepage_resource_descriptor_page_id) REFERENCES "ResourceDescriptorPage" (id)
);
CREATE TABLE "Laboratory" (
	curie TEXT, 
	abbreviation TEXT, 
	full_name TEXT NOT NULL, 
	short_name TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	homepage_resource_descriptor_page_id TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(homepage_resource_descriptor_page_id) REFERENCES "ResourceDescriptorPage" (id)
);
CREATE TABLE "Company" (
	id INTEGER, 
	abbreviation TEXT, 
	full_name TEXT NOT NULL, 
	short_name TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	homepage_resource_descriptor_page_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(homepage_resource_descriptor_page_id) REFERENCES "ResourceDescriptorPage" (id)
);
CREATE TABLE "LoggedInPerson" (
	okta_id TEXT NOT NULL, 
	okta_email TEXT NOT NULL, 
	user_settings TEXT, 
	api_token TEXT, 
	last_name TEXT, 
	middle_name TEXT, 
	first_name TEXT, 
	orcid TEXT, 
	mod_entity_id TEXT, 
	unique_id TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	affiliated_alliance_member_id TEXT, 
	PRIMARY KEY (unique_id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(affiliated_alliance_member_id) REFERENCES "AllianceMember" (id)
);
CREATE TABLE "InformationContentEntity" (
	curie TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AuthorReference" (
	id INTEGER, 
	corresponding_author BOOLEAN, 
	first_author BOOLEAN, 
	first_name TEXT, 
	last_name TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Reference" (
	abstract TEXT, 
	category VARCHAR(26), 
	curie TEXT, 
	date_last_modified_in_pubmed TEXT, 
	date_published TEXT, 
	issue_name TEXT, 
	language TEXT, 
	merged_into_id TEXT, 
	open_access BOOLEAN, 
	page_range TEXT, 
	plain_language_abstract TEXT, 
	publisher TEXT, 
	pubmed_publication_status VARCHAR(12), 
	reference_id INTEGER NOT NULL, 
	resource_id INTEGER, 
	title TEXT, 
	volume TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "PersonalCommunication" (
	curie TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "MeshDetail" (
	id INTEGER, 
	mesh_detail_id INTEGER NOT NULL, 
	reference_id INTEGER NOT NULL, 
	heading_term TEXT NOT NULL, 
	qualifier_term TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Resource" (
	curie TEXT, 
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
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "GeneDTO" (
	gene_type_curie TEXT, 
	curie TEXT NOT NULL, 
	taxon_curie TEXT NOT NULL, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	gene_symbol_dto_id TEXT NOT NULL, 
	gene_full_name_dto_id TEXT, 
	gene_systematic_name_dto_id TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id), 
	FOREIGN KEY(gene_symbol_dto_id) REFERENCES "SymbolSlotAnnotationDTO" (id), 
	FOREIGN KEY(gene_full_name_dto_id) REFERENCES "FullNameSlotAnnotationDTO" (id), 
	FOREIGN KEY(gene_systematic_name_dto_id) REFERENCES "SystematicNameSlotAnnotationDTO" (id)
);
CREATE TABLE "GeneHistory" (
	id INTEGER, 
	current_version INTEGER, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
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
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "GeneToGeneOrthology" (
	id INTEGER, 
	gene_subject TEXT, 
	predicate TEXT NOT NULL, 
	gene_object TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(gene_subject) REFERENCES "Gene" (curie), 
	FOREIGN KEY(gene_object) REFERENCES "Gene" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "GeneToGeneOrthologyGenerated" (
	id INTEGER, 
	is_best_score TEXT, 
	is_best_reverse_score TEXT, 
	confidence TEXT, 
	strict_filter TEXT, 
	moderate_filter TEXT, 
	gene_subject TEXT, 
	predicate TEXT NOT NULL, 
	gene_object TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(gene_subject) REFERENCES "Gene" (curie), 
	FOREIGN KEY(gene_object) REFERENCES "Gene" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "ModCorpusAssociation" (
	corpus BOOLEAN, 
	mod_corpus_association_id INTEGER NOT NULL, 
	mod_corpus_sort_source VARCHAR(19) NOT NULL, 
	alliance_member_id INTEGER NOT NULL, 
	reference_id INTEGER NOT NULL, 
	curie TEXT, 
	created_by TEXT, 
	date_created DATETIME NOT NULL, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "GeneToGeneAssociation" (
	id INTEGER, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES "Gene" (curie), 
	FOREIGN KEY(object) REFERENCES "Gene" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "GeneInteraction" (
	curie TEXT, 
	interaction_data_provider VARCHAR(7) NOT NULL, 
	interaction_type VARCHAR(7) NOT NULL, 
	"interactor_A_type" VARCHAR(7) NOT NULL, 
	"interactor_B_type" VARCHAR(7) NOT NULL, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(subject) REFERENCES "Gene" (curie), 
	FOREIGN KEY(object) REFERENCES "Gene" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "GeneMolecularInteraction" (
	aggregation_database VARCHAR(7), 
	detection_method VARCHAR(7), 
	curie TEXT, 
	interaction_data_provider VARCHAR(7) NOT NULL, 
	interaction_type VARCHAR(7) NOT NULL, 
	"interactor_A_type" VARCHAR(7) NOT NULL, 
	"interactor_B_type" VARCHAR(7) NOT NULL, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(subject) REFERENCES "Gene" (curie), 
	FOREIGN KEY(object) REFERENCES "Gene" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "GeneGeneticInteraction" (
	"interactor_A_genetic_perturbation" TEXT, 
	"interactor_B_genetic_perturbation" TEXT, 
	curie TEXT, 
	interaction_data_provider VARCHAR(7) NOT NULL, 
	interaction_type VARCHAR(7) NOT NULL, 
	"interactor_A_type" VARCHAR(7) NOT NULL, 
	"interactor_B_type" VARCHAR(7) NOT NULL, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY("interactor_A_genetic_perturbation") REFERENCES "Allele" (curie), 
	FOREIGN KEY("interactor_B_genetic_perturbation") REFERENCES "Allele" (curie), 
	FOREIGN KEY(subject) REFERENCES "Gene" (curie), 
	FOREIGN KEY(object) REFERENCES "Gene" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "CurationReportGroup" (
	id INTEGER, 
	name TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "BulkLoadGroup" (
	id INTEGER, 
	name TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "BulkLoadFileHistory" (
	id INTEGER, 
	load_started DATETIME, 
	load_finished DATETIME, 
	total_records INTEGER, 
	failed_records INTEGER, 
	completed_records TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Allele_secondary_identifiers" (
	"Allele_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("Allele_curie", secondary_identifiers), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie)
);
CREATE TABLE "CellLineDTO_secondary_identifiers" (
	"CellLineDTO_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("CellLineDTO_curie", secondary_identifiers), 
	FOREIGN KEY("CellLineDTO_curie") REFERENCES "CellLineDTO" (curie)
);
CREATE TABLE "ConstructDTO_construct_component_dtos" (
	"ConstructDTO_curie" TEXT, 
	construct_component_dtos TEXT, 
	PRIMARY KEY ("ConstructDTO_curie", construct_component_dtos), 
	FOREIGN KEY("ConstructDTO_curie") REFERENCES "ConstructDTO" (curie), 
	FOREIGN KEY(construct_component_dtos) REFERENCES "GenomicEntityDTO" (curie)
);
CREATE TABLE "ConstructDTO_reference_curies" (
	"ConstructDTO_curie" TEXT, 
	reference_curies TEXT, 
	PRIMARY KEY ("ConstructDTO_curie", reference_curies), 
	FOREIGN KEY("ConstructDTO_curie") REFERENCES "ConstructDTO" (curie)
);
CREATE TABLE "ConstructDTO_secondary_identifiers" (
	"ConstructDTO_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("ConstructDTO_curie", secondary_identifiers), 
	FOREIGN KEY("ConstructDTO_curie") REFERENCES "ConstructDTO" (curie)
);
CREATE TABLE "GenerationMethodDTO_mutagenesis_method_names" (
	"GenerationMethodDTO_id" TEXT, 
	mutagenesis_method_names TEXT, 
	PRIMARY KEY ("GenerationMethodDTO_id", mutagenesis_method_names), 
	FOREIGN KEY("GenerationMethodDTO_id") REFERENCES "GenerationMethodDTO" (id)
);
CREATE TABLE "AlleleDatabaseStatusSlotAnnotationDTO_evidence_curies" (
	"AlleleDatabaseStatusSlotAnnotationDTO_id" TEXT, 
	evidence_curies TEXT, 
	PRIMARY KEY ("AlleleDatabaseStatusSlotAnnotationDTO_id", evidence_curies), 
	FOREIGN KEY("AlleleDatabaseStatusSlotAnnotationDTO_id") REFERENCES "AlleleDatabaseStatusSlotAnnotationDTO" (id)
);
CREATE TABLE "AlleleGermlineTransmissionStatusSlotAnnotationDTO_evidence_curies" (
	"AlleleGermlineTransmissionStatusSlotAnnotationDTO_id" TEXT, 
	evidence_curies TEXT, 
	PRIMARY KEY ("AlleleGermlineTransmissionStatusSlotAnnotationDTO_id", evidence_curies), 
	FOREIGN KEY("AlleleGermlineTransmissionStatusSlotAnnotationDTO_id") REFERENCES "AlleleGermlineTransmissionStatusSlotAnnotationDTO" (id)
);
CREATE TABLE "GenomicEntityDTO_secondary_identifiers" (
	"GenomicEntityDTO_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("GenomicEntityDTO_curie", secondary_identifiers), 
	FOREIGN KEY("GenomicEntityDTO_curie") REFERENCES "GenomicEntityDTO" (curie)
);
CREATE TABLE "SlotAnnotationDTO_evidence_curies" (
	"SlotAnnotationDTO_id" TEXT, 
	evidence_curies TEXT, 
	PRIMARY KEY ("SlotAnnotationDTO_id", evidence_curies), 
	FOREIGN KEY("SlotAnnotationDTO_id") REFERENCES "SlotAnnotationDTO" (id)
);
CREATE TABLE "SymbolSlotAnnotationDTO_evidence_curies" (
	"SymbolSlotAnnotationDTO_id" TEXT, 
	evidence_curies TEXT, 
	PRIMARY KEY ("SymbolSlotAnnotationDTO_id", evidence_curies), 
	FOREIGN KEY("SymbolSlotAnnotationDTO_id") REFERENCES "SymbolSlotAnnotationDTO" (id)
);
CREATE TABLE "FullNameSlotAnnotationDTO_evidence_curies" (
	"FullNameSlotAnnotationDTO_id" TEXT, 
	evidence_curies TEXT, 
	PRIMARY KEY ("FullNameSlotAnnotationDTO_id", evidence_curies), 
	FOREIGN KEY("FullNameSlotAnnotationDTO_id") REFERENCES "FullNameSlotAnnotationDTO" (id)
);
CREATE TABLE "SystematicNameSlotAnnotationDTO_evidence_curies" (
	"SystematicNameSlotAnnotationDTO_id" TEXT, 
	evidence_curies TEXT, 
	PRIMARY KEY ("SystematicNameSlotAnnotationDTO_id", evidence_curies), 
	FOREIGN KEY("SystematicNameSlotAnnotationDTO_id") REFERENCES "SystematicNameSlotAnnotationDTO" (id)
);
CREATE TABLE "AffectedGenomicModelDTO_reference_curies" (
	"AffectedGenomicModelDTO_curie" TEXT, 
	reference_curies TEXT, 
	PRIMARY KEY ("AffectedGenomicModelDTO_curie", reference_curies), 
	FOREIGN KEY("AffectedGenomicModelDTO_curie") REFERENCES "AffectedGenomicModelDTO" (curie)
);
CREATE TABLE "AffectedGenomicModelDTO_sequence_targeting_reagent_curies" (
	"AffectedGenomicModelDTO_curie" TEXT, 
	sequence_targeting_reagent_curies TEXT, 
	PRIMARY KEY ("AffectedGenomicModelDTO_curie", sequence_targeting_reagent_curies), 
	FOREIGN KEY("AffectedGenomicModelDTO_curie") REFERENCES "AffectedGenomicModelDTO" (curie)
);
CREATE TABLE "AffectedGenomicModelDTO_secondary_identifiers" (
	"AffectedGenomicModelDTO_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("AffectedGenomicModelDTO_curie", secondary_identifiers), 
	FOREIGN KEY("AffectedGenomicModelDTO_curie") REFERENCES "AffectedGenomicModelDTO" (curie)
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
CREATE TABLE "Gene_designating_persons" (
	"Gene_curie" TEXT, 
	designating_persons TEXT, 
	PRIMARY KEY ("Gene_curie", designating_persons), 
	FOREIGN KEY("Gene_curie") REFERENCES "Gene" (curie)
);
CREATE TABLE "Gene_trans_splice_leaders" (
	"Gene_curie" TEXT, 
	trans_splice_leaders TEXT, 
	PRIMARY KEY ("Gene_curie", trans_splice_leaders), 
	FOREIGN KEY("Gene_curie") REFERENCES "Gene" (curie)
);
CREATE TABLE "Gene_contig" (
	"Gene_curie" TEXT, 
	contig TEXT, 
	PRIMARY KEY ("Gene_curie", contig), 
	FOREIGN KEY("Gene_curie") REFERENCES "Gene" (curie)
);
CREATE TABLE "Gene_anatomy_function" (
	"Gene_curie" TEXT, 
	anatomy_function TEXT, 
	PRIMARY KEY ("Gene_curie", anatomy_function), 
	FOREIGN KEY("Gene_curie") REFERENCES "Gene" (curie)
);
CREATE TABLE "Gene_product_binds_matrix" (
	"Gene_curie" TEXT, 
	product_binds_matrix TEXT, 
	PRIMARY KEY ("Gene_curie", product_binds_matrix), 
	FOREIGN KEY("Gene_curie") REFERENCES "Gene" (curie)
);
CREATE TABLE "Gene_wbprocess" (
	"Gene_curie" TEXT, 
	wbprocess TEXT, 
	PRIMARY KEY ("Gene_curie", wbprocess), 
	FOREIGN KEY("Gene_curie") REFERENCES "Gene" (curie)
);
CREATE TABLE "Gene_secondary_identifiers" (
	"Gene_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("Gene_curie", secondary_identifiers), 
	FOREIGN KEY("Gene_curie") REFERENCES "Gene" (curie)
);
CREATE TABLE "Variant" (
	variant_type TEXT NOT NULL, 
	source_general_consequence TEXT, 
	variant_status VARCHAR(7), 
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(variant_type) REFERENCES "SOTerm" (curie), 
	FOREIGN KEY(source_general_consequence) REFERENCES "SOTerm" (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id)
);
CREATE TABLE "SourceVariantLocation" (
	id INTEGER, 
	single_reference TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
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
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(evidence_code) REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(consequence) REFERENCES "SOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "OntologyTermClosure" (
	id INTEGER, 
	distance_between INTEGER, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES "OntologyTerm" (curie), 
	FOREIGN KEY(object) REFERENCES "OntologyTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id)
);
CREATE TABLE "CellLine" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Construct" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "ConstructComponent" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "GenerationMethod" (
	id INTEGER, 
	mutagenesis_target TEXT, 
	integration_method TEXT, 
	chemical_mutagen TEXT, 
	irradiation_mutagen TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(integration_method) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(chemical_mutagen) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(irradiation_mutagen) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "SequenceTargetingReagent" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AlleleFunctionalImpactSlotAnnotation" (
	id INTEGER, 
	single_allele TEXT NOT NULL, 
	phenotype_term TEXT, 
	phenotype_statement TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_allele) REFERENCES "Allele" (curie), 
	FOREIGN KEY(phenotype_term) REFERENCES "PhenotypeTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AlleleInheritanceModeSlotAnnotation" (
	id INTEGER, 
	single_allele TEXT NOT NULL, 
	inheritance_mode TEXT NOT NULL, 
	phenotype_term TEXT, 
	phenotype_statement TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_allele) REFERENCES "Allele" (curie), 
	FOREIGN KEY(inheritance_mode) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(phenotype_term) REFERENCES "PhenotypeTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AlleleNomenclatureEventSlotAnnotation" (
	id INTEGER, 
	single_allele TEXT NOT NULL, 
	nomenclature_event TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_allele) REFERENCES "Allele" (curie), 
	FOREIGN KEY(nomenclature_event) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AlleleSynonymSlotAnnotation" (
	id INTEGER, 
	single_allele TEXT NOT NULL, 
	name_type TEXT NOT NULL, 
	format_text TEXT NOT NULL, 
	display_text TEXT NOT NULL, 
	synonym_url TEXT, 
	synonym_scope TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_allele) REFERENCES "Allele" (curie), 
	FOREIGN KEY(name_type) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(synonym_scope) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AllelePhenotypeAnnotation" (
	inferred_gene TEXT, 
	curie TEXT, 
	single_reference TEXT, 
	phenotype_term TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME NOT NULL, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(inferred_gene) REFERENCES "Gene" (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(phenotype_term) REFERENCES "PhenotypeTerm" (curie), 
	FOREIGN KEY(subject) REFERENCES "Allele" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "ExperimentalCondition" (
	id INTEGER, 
	unique_id TEXT, 
	condition_class TEXT NOT NULL, 
	condition_summary TEXT, 
	condition_id TEXT, 
	condition_free_text TEXT, 
	condition_quantity TEXT, 
	condition_anatomy TEXT, 
	condition_gene_ontology TEXT, 
	condition_taxon TEXT, 
	condition_chemical TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(condition_class) REFERENCES "ZECOTerm" (curie), 
	FOREIGN KEY(condition_id) REFERENCES "ExperimentalConditionOntologyTerm" (curie), 
	FOREIGN KEY(condition_anatomy) REFERENCES "AnatomicalTerm" (curie), 
	FOREIGN KEY(condition_gene_ontology) REFERENCES "GOTerm" (curie), 
	FOREIGN KEY(condition_taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(condition_chemical) REFERENCES "ChemicalTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "ConditionRelation" (
	id INTEGER, 
	unique_id TEXT, 
	handle TEXT, 
	single_reference TEXT, 
	condition_relation_type TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(condition_relation_type) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "ConditionRelationDTO" (
	id INTEGER, 
	handle TEXT, 
	reference_curie TEXT, 
	condition_relation_type_name TEXT NOT NULL, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"DiseaseAnnotationDTO_id" TEXT, 
	"GeneDiseaseAnnotationDTO_id" TEXT, 
	"AlleleDiseaseAnnotationDTO_id" TEXT, 
	"AGMDiseaseAnnotationDTO_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("DiseaseAnnotationDTO_id") REFERENCES "DiseaseAnnotationDTO" (id), 
	FOREIGN KEY("GeneDiseaseAnnotationDTO_id") REFERENCES "GeneDiseaseAnnotationDTO" (id), 
	FOREIGN KEY("AlleleDiseaseAnnotationDTO_id") REFERENCES "AlleleDiseaseAnnotationDTO" (id), 
	FOREIGN KEY("AGMDiseaseAnnotationDTO_id") REFERENCES "AGMDiseaseAnnotationDTO" (id)
);
CREATE TABLE "AlleleFunctionalImpactSlotAnnotationDTO" (
	id INTEGER, 
	phenotype_term_curie TEXT, 
	phenotype_statement TEXT, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"AlleleDTO_curie" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("AlleleDTO_curie") REFERENCES "AlleleDTO" (curie)
);
CREATE TABLE "AlleleInheritanceModeSlotAnnotationDTO" (
	id INTEGER, 
	inheritance_mode_name TEXT NOT NULL, 
	phenotype_term_curie TEXT, 
	phenotype_statement TEXT, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"AlleleDTO_curie" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("AlleleDTO_curie") REFERENCES "AlleleDTO" (curie)
);
CREATE TABLE "AlleleMolecularMutationSlotAnnotationDTO" (
	id INTEGER, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"AlleleDTO_curie" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("AlleleDTO_curie") REFERENCES "AlleleDTO" (curie)
);
CREATE TABLE "AlleleMutationTypeSlotAnnotationDTO" (
	id INTEGER, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"AlleleDTO_curie" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("AlleleDTO_curie") REFERENCES "AlleleDTO" (curie)
);
CREATE TABLE "AlleleNomenclatureEventSlotAnnotationDTO" (
	id INTEGER, 
	nomenclature_event_name TEXT NOT NULL, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"AlleleDTO_curie" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("AlleleDTO_curie") REFERENCES "AlleleDTO" (curie)
);
CREATE TABLE "AlleleSecondaryIdSlotAnnotationDTO" (
	id INTEGER, 
	secondary_id TEXT NOT NULL, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"AlleleDTO_curie" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("AlleleDTO_curie") REFERENCES "AlleleDTO" (curie)
);
CREATE TABLE "BiologicalEntity" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "GenomicEntity" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Transcript" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "DataProvider" (
	id INTEGER, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	source_organization_id TEXT NOT NULL, 
	cross_reference_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(source_organization_id) REFERENCES "Organization" (id), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "Note" (
	id INTEGER, 
	free_text TEXT NOT NULL, 
	note_type TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(note_type) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "NoteDTO" (
	id INTEGER, 
	free_text TEXT NOT NULL, 
	note_type_name TEXT NOT NULL, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"DiseaseAnnotationDTO_id" TEXT, 
	"GeneDiseaseAnnotationDTO_id" TEXT, 
	"AlleleDiseaseAnnotationDTO_id" TEXT, 
	"AGMDiseaseAnnotationDTO_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("DiseaseAnnotationDTO_id") REFERENCES "DiseaseAnnotationDTO" (id), 
	FOREIGN KEY("GeneDiseaseAnnotationDTO_id") REFERENCES "GeneDiseaseAnnotationDTO" (id), 
	FOREIGN KEY("AlleleDiseaseAnnotationDTO_id") REFERENCES "AlleleDiseaseAnnotationDTO" (id), 
	FOREIGN KEY("AGMDiseaseAnnotationDTO_id") REFERENCES "AGMDiseaseAnnotationDTO" (id)
);
CREATE TABLE "NameSlotAnnotation" (
	id INTEGER, 
	name_type TEXT NOT NULL, 
	format_text TEXT NOT NULL, 
	display_text TEXT NOT NULL, 
	synonym_url TEXT, 
	synonym_scope TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(name_type) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(synonym_scope) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "NameSlotAnnotationDTO" (
	id INTEGER, 
	name_type_name TEXT NOT NULL, 
	format_text TEXT NOT NULL, 
	display_text TEXT NOT NULL, 
	synonym_url TEXT, 
	synonym_scope_name TEXT, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"AlleleDTO_curie" TEXT, 
	"GeneDTO_curie" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("AlleleDTO_curie") REFERENCES "AlleleDTO" (curie), 
	FOREIGN KEY("GeneDTO_curie") REFERENCES "GeneDTO" (curie)
);
CREATE TABLE "GenomicLocationAssociationDTO" (
	id INTEGER, 
	genomic_entity_curie TEXT NOT NULL, 
	predicate_name TEXT NOT NULL, 
	chromosome_curie TEXT NOT NULL, 
	assembly_curie TEXT NOT NULL, 
	start INTEGER NOT NULL, 
	"end" INTEGER NOT NULL, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"AlleleDTO_curie" TEXT, 
	"CellLineDTO_curie" TEXT, 
	"ConstructDTO_curie" TEXT, 
	"SequenceTargetingReagentDTO_curie" TEXT, 
	"GenomicEntityDTO_curie" TEXT, 
	"AffectedGenomicModelDTO_curie" TEXT, 
	"GeneDTO_curie" TEXT, 
	"Ingest_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("AlleleDTO_curie") REFERENCES "AlleleDTO" (curie), 
	FOREIGN KEY("CellLineDTO_curie") REFERENCES "CellLineDTO" (curie), 
	FOREIGN KEY("ConstructDTO_curie") REFERENCES "ConstructDTO" (curie), 
	FOREIGN KEY("SequenceTargetingReagentDTO_curie") REFERENCES "SequenceTargetingReagentDTO" (curie), 
	FOREIGN KEY("GenomicEntityDTO_curie") REFERENCES "GenomicEntityDTO" (curie), 
	FOREIGN KEY("AffectedGenomicModelDTO_curie") REFERENCES "AffectedGenomicModelDTO" (curie), 
	FOREIGN KEY("GeneDTO_curie") REFERENCES "GeneDTO" (curie), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id)
);
CREATE TABLE "Protein" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "VocabularyTermSet" (
	name TEXT NOT NULL, 
	vocabulary_term_set_vocabulary TEXT NOT NULL, 
	vocabulary_term_set_description TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (name), 
	FOREIGN KEY(vocabulary_term_set_vocabulary) REFERENCES "Vocabulary" (name), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Figure" (
	curie TEXT, 
	single_reference TEXT NOT NULL, 
	label TEXT, 
	caption TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "GeneSynonymSlotAnnotation" (
	id INTEGER, 
	single_gene TEXT NOT NULL, 
	name_type TEXT NOT NULL, 
	format_text TEXT NOT NULL, 
	display_text TEXT NOT NULL, 
	synonym_url TEXT, 
	synonym_scope TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_gene) REFERENCES "Gene" (curie), 
	FOREIGN KEY(name_type) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(synonym_scope) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "GeneticMapPosition" (
	genetic_map_chromosome TEXT, 
	genetic_map_band TEXT, 
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(genetic_map_chromosome) REFERENCES "Chromosome" (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Reagent" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
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
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(antigen_taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "DNAClone" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "RNAClone" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "GeneToGeneOrthologyCurated" (
	id INTEGER, 
	single_reference TEXT, 
	evidence_code TEXT, 
	gene_subject TEXT, 
	predicate TEXT NOT NULL, 
	gene_object TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(evidence_code) REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY(gene_subject) REFERENCES "Gene" (curie), 
	FOREIGN KEY(gene_object) REFERENCES "Gene" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "TemporalContext" (
	id INTEGER, 
	developmental_stage_start TEXT, 
	developmental_stage_stop TEXT, 
	age TEXT, 
	temporal_qualifiers VARCHAR(15), 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(developmental_stage_start) REFERENCES "StageTerm" (curie), 
	FOREIGN KEY(developmental_stage_stop) REFERENCES "StageTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AnatomicalSite" (
	id INTEGER, 
	anatomical_structure TEXT, 
	anatomical_substructure TEXT, 
	cellular_component TEXT, 
	spatial_qualifiers VARCHAR(35), 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(anatomical_structure) REFERENCES "AnatomicalTerm" (curie), 
	FOREIGN KEY(anatomical_substructure) REFERENCES "AnatomicalTerm" (curie), 
	FOREIGN KEY(cellular_component) REFERENCES "GOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "CurationReport" (
	id INTEGER, 
	name TEXT, 
	birt_report_file_path TEXT, 
	schedule_active BOOLEAN, 
	cron_schedule TEXT, 
	curation_report_status TEXT, 
	error_message TEXT, 
	scheduling_error_message TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	curation_report_group_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(curation_report_group_id) REFERENCES "CurationReportGroup" (id)
);
CREATE TABLE "BulkLoad" (
	id INTEGER, 
	name TEXT, 
	bulkload_status VARCHAR(24), 
	error_message TEXT, 
	backend_bulk_load_type VARCHAR(22), 
	ontology_type VARCHAR(5), 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	bulkload_group_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(bulkload_group_id) REFERENCES "BulkLoadGroup" (id)
);
CREATE TABLE "BulkScheduledLoad" (
	id INTEGER, 
	schedule_active BOOLEAN, 
	cron_schedule TEXT, 
	scheduling_error_message TEXT, 
	name TEXT, 
	bulkload_status VARCHAR(24), 
	error_message TEXT, 
	backend_bulk_load_type VARCHAR(22), 
	ontology_type VARCHAR(5), 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	bulkload_group_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(bulkload_group_id) REFERENCES "BulkLoadGroup" (id)
);
CREATE TABLE "BulkFMSLoad" (
	id INTEGER, 
	fms_data_type TEXT, 
	fms_data_sub_type TEXT, 
	schedule_active BOOLEAN, 
	cron_schedule TEXT, 
	scheduling_error_message TEXT, 
	name TEXT, 
	bulkload_status VARCHAR(24), 
	error_message TEXT, 
	backend_bulk_load_type VARCHAR(22), 
	ontology_type VARCHAR(5), 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	bulkload_group_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(bulkload_group_id) REFERENCES "BulkLoadGroup" (id)
);
CREATE TABLE "BulkURLLoad" (
	id INTEGER, 
	bulkload_url TEXT, 
	schedule_active BOOLEAN, 
	cron_schedule TEXT, 
	scheduling_error_message TEXT, 
	name TEXT, 
	bulkload_status VARCHAR(24), 
	error_message TEXT, 
	backend_bulk_load_type VARCHAR(22), 
	ontology_type VARCHAR(5), 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	bulkload_group_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(bulkload_group_id) REFERENCES "BulkLoadGroup" (id)
);
CREATE TABLE "BulkManualLoad" (
	id INTEGER, 
	backend_load_type VARCHAR(5), 
	name TEXT, 
	bulkload_status VARCHAR(24), 
	error_message TEXT, 
	backend_bulk_load_type VARCHAR(22), 
	ontology_type VARCHAR(5), 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	bulkload_group_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(bulkload_group_id) REFERENCES "BulkLoadGroup" (id)
);
CREATE TABLE "UniGeneSet" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "FunctionalGeneSet" (
	single_reference TEXT, 
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Pathway" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "ProteinComplex" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "OntologyTerm_definition_urls" (
	"OntologyTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("OntologyTerm_curie", definition_urls), 
	FOREIGN KEY("OntologyTerm_curie") REFERENCES "OntologyTerm" (curie)
);
CREATE TABLE "OntologyTerm_cross_reference" (
	"OntologyTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("OntologyTerm_curie", cross_reference_id), 
	FOREIGN KEY("OntologyTerm_curie") REFERENCES "OntologyTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "OntologyTerm_synonyms" (
	"OntologyTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("OntologyTerm_curie", synonyms), 
	FOREIGN KEY("OntologyTerm_curie") REFERENCES "OntologyTerm" (curie)
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
CREATE TABLE "DOTerm_cross_reference" (
	"DOTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("DOTerm_curie", cross_reference_id), 
	FOREIGN KEY("DOTerm_curie") REFERENCES "DOTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "DOTerm_synonyms" (
	"DOTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("DOTerm_curie", synonyms), 
	FOREIGN KEY("DOTerm_curie") REFERENCES "DOTerm" (curie)
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
CREATE TABLE "ECOTerm_cross_reference" (
	"ECOTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("ECOTerm_curie", cross_reference_id), 
	FOREIGN KEY("ECOTerm_curie") REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "ECOTerm_synonyms" (
	"ECOTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("ECOTerm_curie", synonyms), 
	FOREIGN KEY("ECOTerm_curie") REFERENCES "ECOTerm" (curie)
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
CREATE TABLE "NCBITaxonTerm_cross_reference" (
	"NCBITaxonTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("NCBITaxonTerm_curie", cross_reference_id), 
	FOREIGN KEY("NCBITaxonTerm_curie") REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "NCBITaxonTerm_synonyms" (
	"NCBITaxonTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("NCBITaxonTerm_curie", synonyms), 
	FOREIGN KEY("NCBITaxonTerm_curie") REFERENCES "NCBITaxonTerm" (curie)
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
CREATE TABLE "FBCVTerm_cross_reference" (
	"FBCVTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("FBCVTerm_curie", cross_reference_id), 
	FOREIGN KEY("FBCVTerm_curie") REFERENCES "FBCVTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "FBCVTerm_synonyms" (
	"FBCVTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("FBCVTerm_curie", synonyms), 
	FOREIGN KEY("FBCVTerm_curie") REFERENCES "FBCVTerm" (curie)
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
CREATE TABLE "GOTerm_cross_reference" (
	"GOTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("GOTerm_curie", cross_reference_id), 
	FOREIGN KEY("GOTerm_curie") REFERENCES "GOTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "GOTerm_synonyms" (
	"GOTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("GOTerm_curie", synonyms), 
	FOREIGN KEY("GOTerm_curie") REFERENCES "GOTerm" (curie)
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
CREATE TABLE "ROTerm_cross_reference" (
	"ROTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("ROTerm_curie", cross_reference_id), 
	FOREIGN KEY("ROTerm_curie") REFERENCES "ROTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "ROTerm_synonyms" (
	"ROTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("ROTerm_curie", synonyms), 
	FOREIGN KEY("ROTerm_curie") REFERENCES "ROTerm" (curie)
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
CREATE TABLE "MITerm_cross_reference" (
	"MITerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("MITerm_curie", cross_reference_id), 
	FOREIGN KEY("MITerm_curie") REFERENCES "MITerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "MITerm_synonyms" (
	"MITerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("MITerm_curie", synonyms), 
	FOREIGN KEY("MITerm_curie") REFERENCES "MITerm" (curie)
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
CREATE TABLE "MMOTerm_cross_reference" (
	"MMOTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("MMOTerm_curie", cross_reference_id), 
	FOREIGN KEY("MMOTerm_curie") REFERENCES "MMOTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "MMOTerm_synonyms" (
	"MMOTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("MMOTerm_curie", synonyms), 
	FOREIGN KEY("MMOTerm_curie") REFERENCES "MMOTerm" (curie)
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
CREATE TABLE "MMUSDVTerm_cross_reference" (
	"MMUSDVTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("MMUSDVTerm_curie", cross_reference_id), 
	FOREIGN KEY("MMUSDVTerm_curie") REFERENCES "MMUSDVTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "MMUSDVTerm_synonyms" (
	"MMUSDVTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("MMUSDVTerm_curie", synonyms), 
	FOREIGN KEY("MMUSDVTerm_curie") REFERENCES "MMUSDVTerm" (curie)
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
CREATE TABLE "SOTerm_cross_reference" (
	"SOTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("SOTerm_curie", cross_reference_id), 
	FOREIGN KEY("SOTerm_curie") REFERENCES "SOTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "SOTerm_synonyms" (
	"SOTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("SOTerm_curie", synonyms), 
	FOREIGN KEY("SOTerm_curie") REFERENCES "SOTerm" (curie)
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
CREATE TABLE "XBEDTerm_cross_reference" (
	"XBEDTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("XBEDTerm_curie", cross_reference_id), 
	FOREIGN KEY("XBEDTerm_curie") REFERENCES "XBEDTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "XBEDTerm_synonyms" (
	"XBEDTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("XBEDTerm_curie", synonyms), 
	FOREIGN KEY("XBEDTerm_curie") REFERENCES "XBEDTerm" (curie)
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
CREATE TABLE "CHEBITerm_cross_reference" (
	"CHEBITerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("CHEBITerm_curie", cross_reference_id), 
	FOREIGN KEY("CHEBITerm_curie") REFERENCES "CHEBITerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "CHEBITerm_synonyms" (
	"CHEBITerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("CHEBITerm_curie", synonyms), 
	FOREIGN KEY("CHEBITerm_curie") REFERENCES "CHEBITerm" (curie)
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
CREATE TABLE "StageTerm_cross_reference" (
	"StageTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("StageTerm_curie", cross_reference_id), 
	FOREIGN KEY("StageTerm_curie") REFERENCES "StageTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "StageTerm_synonyms" (
	"StageTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("StageTerm_curie", synonyms), 
	FOREIGN KEY("StageTerm_curie") REFERENCES "StageTerm" (curie)
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
CREATE TABLE "FBDVTerm_cross_reference" (
	"FBDVTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("FBDVTerm_curie", cross_reference_id), 
	FOREIGN KEY("FBDVTerm_curie") REFERENCES "FBDVTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "FBDVTerm_synonyms" (
	"FBDVTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("FBDVTerm_curie", synonyms), 
	FOREIGN KEY("FBDVTerm_curie") REFERENCES "FBDVTerm" (curie)
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
CREATE TABLE "WBLSTerm_cross_reference" (
	"WBLSTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("WBLSTerm_curie", cross_reference_id), 
	FOREIGN KEY("WBLSTerm_curie") REFERENCES "WBLSTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "WBLSTerm_synonyms" (
	"WBLSTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("WBLSTerm_curie", synonyms), 
	FOREIGN KEY("WBLSTerm_curie") REFERENCES "WBLSTerm" (curie)
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
CREATE TABLE "XBSTerm_cross_reference" (
	"XBSTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("XBSTerm_curie", cross_reference_id), 
	FOREIGN KEY("XBSTerm_curie") REFERENCES "XBSTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "XBSTerm_synonyms" (
	"XBSTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("XBSTerm_curie", synonyms), 
	FOREIGN KEY("XBSTerm_curie") REFERENCES "XBSTerm" (curie)
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
CREATE TABLE "ZFSTerm_cross_reference" (
	"ZFSTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("ZFSTerm_curie", cross_reference_id), 
	FOREIGN KEY("ZFSTerm_curie") REFERENCES "ZFSTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "ZFSTerm_synonyms" (
	"ZFSTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("ZFSTerm_curie", synonyms), 
	FOREIGN KEY("ZFSTerm_curie") REFERENCES "ZFSTerm" (curie)
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
CREATE TABLE "ExperimentalConditionOntologyTerm_cross_reference" (
	"ExperimentalConditionOntologyTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("ExperimentalConditionOntologyTerm_curie", cross_reference_id), 
	FOREIGN KEY("ExperimentalConditionOntologyTerm_curie") REFERENCES "ExperimentalConditionOntologyTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "ExperimentalConditionOntologyTerm_synonyms" (
	"ExperimentalConditionOntologyTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("ExperimentalConditionOntologyTerm_curie", synonyms), 
	FOREIGN KEY("ExperimentalConditionOntologyTerm_curie") REFERENCES "ExperimentalConditionOntologyTerm" (curie)
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
CREATE TABLE "ZECOTerm_cross_reference" (
	"ZECOTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("ZECOTerm_curie", cross_reference_id), 
	FOREIGN KEY("ZECOTerm_curie") REFERENCES "ZECOTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "ZECOTerm_synonyms" (
	"ZECOTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("ZECOTerm_curie", synonyms), 
	FOREIGN KEY("ZECOTerm_curie") REFERENCES "ZECOTerm" (curie)
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
CREATE TABLE "XCOTerm_cross_reference" (
	"XCOTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("XCOTerm_curie", cross_reference_id), 
	FOREIGN KEY("XCOTerm_curie") REFERENCES "XCOTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "XCOTerm_synonyms" (
	"XCOTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("XCOTerm_curie", synonyms), 
	FOREIGN KEY("XCOTerm_curie") REFERENCES "XCOTerm" (curie)
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
CREATE TABLE "AnatomicalTerm_cross_reference" (
	"AnatomicalTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("AnatomicalTerm_curie", cross_reference_id), 
	FOREIGN KEY("AnatomicalTerm_curie") REFERENCES "AnatomicalTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "AnatomicalTerm_synonyms" (
	"AnatomicalTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("AnatomicalTerm_curie", synonyms), 
	FOREIGN KEY("AnatomicalTerm_curie") REFERENCES "AnatomicalTerm" (curie)
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
CREATE TABLE "CLTerm_cross_reference" (
	"CLTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("CLTerm_curie", cross_reference_id), 
	FOREIGN KEY("CLTerm_curie") REFERENCES "CLTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "CLTerm_synonyms" (
	"CLTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("CLTerm_curie", synonyms), 
	FOREIGN KEY("CLTerm_curie") REFERENCES "CLTerm" (curie)
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
CREATE TABLE "EMAPATerm_cross_reference" (
	"EMAPATerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("EMAPATerm_curie", cross_reference_id), 
	FOREIGN KEY("EMAPATerm_curie") REFERENCES "EMAPATerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "EMAPATerm_synonyms" (
	"EMAPATerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("EMAPATerm_curie", synonyms), 
	FOREIGN KEY("EMAPATerm_curie") REFERENCES "EMAPATerm" (curie)
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
CREATE TABLE "DAOTerm_cross_reference" (
	"DAOTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("DAOTerm_curie", cross_reference_id), 
	FOREIGN KEY("DAOTerm_curie") REFERENCES "DAOTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "DAOTerm_synonyms" (
	"DAOTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("DAOTerm_curie", synonyms), 
	FOREIGN KEY("DAOTerm_curie") REFERENCES "DAOTerm" (curie)
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
CREATE TABLE "MATerm_cross_reference" (
	"MATerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("MATerm_curie", cross_reference_id), 
	FOREIGN KEY("MATerm_curie") REFERENCES "MATerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "MATerm_synonyms" (
	"MATerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("MATerm_curie", synonyms), 
	FOREIGN KEY("MATerm_curie") REFERENCES "MATerm" (curie)
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
CREATE TABLE "UBERONTerm_cross_reference" (
	"UBERONTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("UBERONTerm_curie", cross_reference_id), 
	FOREIGN KEY("UBERONTerm_curie") REFERENCES "UBERONTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "UBERONTerm_synonyms" (
	"UBERONTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("UBERONTerm_curie", synonyms), 
	FOREIGN KEY("UBERONTerm_curie") REFERENCES "UBERONTerm" (curie)
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
CREATE TABLE "WBBTTerm_cross_reference" (
	"WBBTTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("WBBTTerm_curie", cross_reference_id), 
	FOREIGN KEY("WBBTTerm_curie") REFERENCES "WBBTTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "WBBTTerm_synonyms" (
	"WBBTTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("WBBTTerm_curie", synonyms), 
	FOREIGN KEY("WBBTTerm_curie") REFERENCES "WBBTTerm" (curie)
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
CREATE TABLE "XBATerm_cross_reference" (
	"XBATerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("XBATerm_curie", cross_reference_id), 
	FOREIGN KEY("XBATerm_curie") REFERENCES "XBATerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "XBATerm_synonyms" (
	"XBATerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("XBATerm_curie", synonyms), 
	FOREIGN KEY("XBATerm_curie") REFERENCES "XBATerm" (curie)
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
CREATE TABLE "ZFATerm_cross_reference" (
	"ZFATerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("ZFATerm_curie", cross_reference_id), 
	FOREIGN KEY("ZFATerm_curie") REFERENCES "ZFATerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "ZFATerm_synonyms" (
	"ZFATerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("ZFATerm_curie", synonyms), 
	FOREIGN KEY("ZFATerm_curie") REFERENCES "ZFATerm" (curie)
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
CREATE TABLE "PhenotypeTerm_cross_reference" (
	"PhenotypeTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("PhenotypeTerm_curie", cross_reference_id), 
	FOREIGN KEY("PhenotypeTerm_curie") REFERENCES "PhenotypeTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "PhenotypeTerm_synonyms" (
	"PhenotypeTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("PhenotypeTerm_curie", synonyms), 
	FOREIGN KEY("PhenotypeTerm_curie") REFERENCES "PhenotypeTerm" (curie)
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
CREATE TABLE "XPOTerm_cross_reference" (
	"XPOTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("XPOTerm_curie", cross_reference_id), 
	FOREIGN KEY("XPOTerm_curie") REFERENCES "XPOTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "XPOTerm_synonyms" (
	"XPOTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("XPOTerm_curie", synonyms), 
	FOREIGN KEY("XPOTerm_curie") REFERENCES "XPOTerm" (curie)
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
CREATE TABLE "MPTerm_definition_urls" (
	"MPTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("MPTerm_curie", definition_urls), 
	FOREIGN KEY("MPTerm_curie") REFERENCES "MPTerm" (curie)
);
CREATE TABLE "MPTerm_cross_reference" (
	"MPTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("MPTerm_curie", cross_reference_id), 
	FOREIGN KEY("MPTerm_curie") REFERENCES "MPTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "MPTerm_synonyms" (
	"MPTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("MPTerm_curie", synonyms), 
	FOREIGN KEY("MPTerm_curie") REFERENCES "MPTerm" (curie)
);
CREATE TABLE "MPTerm_subsets" (
	"MPTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("MPTerm_curie", subsets), 
	FOREIGN KEY("MPTerm_curie") REFERENCES "MPTerm" (curie)
);
CREATE TABLE "MPTerm_secondary_identifiers" (
	"MPTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("MPTerm_curie", secondary_identifiers), 
	FOREIGN KEY("MPTerm_curie") REFERENCES "MPTerm" (curie)
);
CREATE TABLE "ATPTerm_definition_urls" (
	"ATPTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("ATPTerm_curie", definition_urls), 
	FOREIGN KEY("ATPTerm_curie") REFERENCES "ATPTerm" (curie)
);
CREATE TABLE "ATPTerm_cross_reference" (
	"ATPTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("ATPTerm_curie", cross_reference_id), 
	FOREIGN KEY("ATPTerm_curie") REFERENCES "ATPTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "ATPTerm_synonyms" (
	"ATPTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("ATPTerm_curie", synonyms), 
	FOREIGN KEY("ATPTerm_curie") REFERENCES "ATPTerm" (curie)
);
CREATE TABLE "ATPTerm_subsets" (
	"ATPTerm_curie" TEXT, 
	subsets TEXT, 
	PRIMARY KEY ("ATPTerm_curie", subsets), 
	FOREIGN KEY("ATPTerm_curie") REFERENCES "ATPTerm" (curie)
);
CREATE TABLE "ATPTerm_secondary_identifiers" (
	"ATPTerm_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("ATPTerm_curie", secondary_identifiers), 
	FOREIGN KEY("ATPTerm_curie") REFERENCES "ATPTerm" (curie)
);
CREATE TABLE "ChemicalTerm_definition_urls" (
	"ChemicalTerm_curie" TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY ("ChemicalTerm_curie", definition_urls), 
	FOREIGN KEY("ChemicalTerm_curie") REFERENCES "ChemicalTerm" (curie)
);
CREATE TABLE "ChemicalTerm_cross_reference" (
	"ChemicalTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("ChemicalTerm_curie", cross_reference_id), 
	FOREIGN KEY("ChemicalTerm_curie") REFERENCES "ChemicalTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "ChemicalTerm_synonyms" (
	"ChemicalTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("ChemicalTerm_curie", synonyms), 
	FOREIGN KEY("ChemicalTerm_curie") REFERENCES "ChemicalTerm" (curie)
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
CREATE TABLE "XSMOTerm_cross_reference" (
	"XSMOTerm_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("XSMOTerm_curie", cross_reference_id), 
	FOREIGN KEY("XSMOTerm_curie") REFERENCES "XSMOTerm" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "XSMOTerm_synonyms" (
	"XSMOTerm_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("XSMOTerm_curie", synonyms), 
	FOREIGN KEY("XSMOTerm_curie") REFERENCES "XSMOTerm" (curie)
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
CREATE TABLE "Molecule_cross_reference" (
	"Molecule_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("Molecule_curie", cross_reference_id), 
	FOREIGN KEY("Molecule_curie") REFERENCES "Molecule" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "Molecule_synonyms" (
	"Molecule_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("Molecule_curie", synonyms), 
	FOREIGN KEY("Molecule_curie") REFERENCES "Molecule" (curie)
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
CREATE TABLE "Allele_reference" (
	"Allele_curie" TEXT, 
	reference TEXT, 
	PRIMARY KEY ("Allele_curie", reference), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(reference) REFERENCES "Reference" (curie)
);
CREATE TABLE "Allele_allele_mutation_types" (
	"Allele_curie" TEXT, 
	allele_mutation_types_id TEXT, 
	PRIMARY KEY ("Allele_curie", allele_mutation_types_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(allele_mutation_types_id) REFERENCES "AlleleMutationTypeSlotAnnotation" (id)
);
CREATE TABLE "Allele_allele_molecular_mutations" (
	"Allele_curie" TEXT, 
	allele_molecular_mutations_id TEXT, 
	PRIMARY KEY ("Allele_curie", allele_molecular_mutations_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(allele_molecular_mutations_id) REFERENCES "AlleleMolecularMutationSlotAnnotation" (id)
);
CREATE TABLE "Allele_allele_secondary_ids" (
	"Allele_curie" TEXT, 
	allele_secondary_ids_id TEXT, 
	PRIMARY KEY ("Allele_curie", allele_secondary_ids_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(allele_secondary_ids_id) REFERENCES "AlleleSecondaryIdSlotAnnotation" (id)
);
CREATE TABLE "Allele_cross_reference" (
	"Allele_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("Allele_curie", cross_reference_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "AlleleDatabaseStatusSlotAnnotation_evidence" (
	"AlleleDatabaseStatusSlotAnnotation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AlleleDatabaseStatusSlotAnnotation_id", evidence), 
	FOREIGN KEY("AlleleDatabaseStatusSlotAnnotation_id") REFERENCES "AlleleDatabaseStatusSlotAnnotation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "AlleleFullNameSlotAnnotation_evidence" (
	"AlleleFullNameSlotAnnotation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AlleleFullNameSlotAnnotation_id", evidence), 
	FOREIGN KEY("AlleleFullNameSlotAnnotation_id") REFERENCES "AlleleFullNameSlotAnnotation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "AlleleGermlineTransmissionStatusSlotAnnotation_evidence" (
	"AlleleGermlineTransmissionStatusSlotAnnotation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AlleleGermlineTransmissionStatusSlotAnnotation_id", evidence), 
	FOREIGN KEY("AlleleGermlineTransmissionStatusSlotAnnotation_id") REFERENCES "AlleleGermlineTransmissionStatusSlotAnnotation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "AlleleMolecularMutationSlotAnnotation_molecular_mutations" (
	"AlleleMolecularMutationSlotAnnotation_id" TEXT, 
	molecular_mutations TEXT NOT NULL, 
	PRIMARY KEY ("AlleleMolecularMutationSlotAnnotation_id", molecular_mutations), 
	FOREIGN KEY("AlleleMolecularMutationSlotAnnotation_id") REFERENCES "AlleleMolecularMutationSlotAnnotation" (id)
);
CREATE TABLE "AlleleMolecularMutationSlotAnnotation_evidence" (
	"AlleleMolecularMutationSlotAnnotation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AlleleMolecularMutationSlotAnnotation_id", evidence), 
	FOREIGN KEY("AlleleMolecularMutationSlotAnnotation_id") REFERENCES "AlleleMolecularMutationSlotAnnotation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "AlleleMutationTypeSlotAnnotation_mutation_types" (
	"AlleleMutationTypeSlotAnnotation_id" TEXT, 
	mutation_types TEXT NOT NULL, 
	PRIMARY KEY ("AlleleMutationTypeSlotAnnotation_id", mutation_types), 
	FOREIGN KEY("AlleleMutationTypeSlotAnnotation_id") REFERENCES "AlleleMutationTypeSlotAnnotation" (id), 
	FOREIGN KEY(mutation_types) REFERENCES "SOTerm" (curie)
);
CREATE TABLE "AlleleMutationTypeSlotAnnotation_evidence" (
	"AlleleMutationTypeSlotAnnotation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AlleleMutationTypeSlotAnnotation_id", evidence), 
	FOREIGN KEY("AlleleMutationTypeSlotAnnotation_id") REFERENCES "AlleleMutationTypeSlotAnnotation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "AlleleSecondaryIdSlotAnnotation_evidence" (
	"AlleleSecondaryIdSlotAnnotation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AlleleSecondaryIdSlotAnnotation_id", evidence), 
	FOREIGN KEY("AlleleSecondaryIdSlotAnnotation_id") REFERENCES "AlleleSecondaryIdSlotAnnotation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "AlleleSymbolSlotAnnotation_evidence" (
	"AlleleSymbolSlotAnnotation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AlleleSymbolSlotAnnotation_id", evidence), 
	FOREIGN KEY("AlleleSymbolSlotAnnotation_id") REFERENCES "AlleleSymbolSlotAnnotation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "DiseaseAnnotationDTO_evidence_curies" (
	"DiseaseAnnotationDTO_id" TEXT, 
	evidence_curies TEXT, 
	PRIMARY KEY ("DiseaseAnnotationDTO_id", evidence_curies), 
	FOREIGN KEY("DiseaseAnnotationDTO_id") REFERENCES "DiseaseAnnotationDTO" (id)
);
CREATE TABLE "DiseaseAnnotationDTO_evidence_code_curies" (
	"DiseaseAnnotationDTO_id" TEXT, 
	evidence_code_curies TEXT, 
	PRIMARY KEY ("DiseaseAnnotationDTO_id", evidence_code_curies), 
	FOREIGN KEY("DiseaseAnnotationDTO_id") REFERENCES "DiseaseAnnotationDTO" (id)
);
CREATE TABLE "DiseaseAnnotationDTO_with_gene_curies" (
	"DiseaseAnnotationDTO_id" TEXT, 
	with_gene_curies TEXT, 
	PRIMARY KEY ("DiseaseAnnotationDTO_id", with_gene_curies), 
	FOREIGN KEY("DiseaseAnnotationDTO_id") REFERENCES "DiseaseAnnotationDTO" (id)
);
CREATE TABLE "DiseaseAnnotationDTO_disease_qualifier_names" (
	"DiseaseAnnotationDTO_id" TEXT, 
	disease_qualifier_names TEXT, 
	PRIMARY KEY ("DiseaseAnnotationDTO_id", disease_qualifier_names), 
	FOREIGN KEY("DiseaseAnnotationDTO_id") REFERENCES "DiseaseAnnotationDTO" (id)
);
CREATE TABLE "GeneDiseaseAnnotationDTO_evidence_curies" (
	"GeneDiseaseAnnotationDTO_id" TEXT, 
	evidence_curies TEXT, 
	PRIMARY KEY ("GeneDiseaseAnnotationDTO_id", evidence_curies), 
	FOREIGN KEY("GeneDiseaseAnnotationDTO_id") REFERENCES "GeneDiseaseAnnotationDTO" (id)
);
CREATE TABLE "GeneDiseaseAnnotationDTO_evidence_code_curies" (
	"GeneDiseaseAnnotationDTO_id" TEXT, 
	evidence_code_curies TEXT, 
	PRIMARY KEY ("GeneDiseaseAnnotationDTO_id", evidence_code_curies), 
	FOREIGN KEY("GeneDiseaseAnnotationDTO_id") REFERENCES "GeneDiseaseAnnotationDTO" (id)
);
CREATE TABLE "GeneDiseaseAnnotationDTO_with_gene_curies" (
	"GeneDiseaseAnnotationDTO_id" TEXT, 
	with_gene_curies TEXT, 
	PRIMARY KEY ("GeneDiseaseAnnotationDTO_id", with_gene_curies), 
	FOREIGN KEY("GeneDiseaseAnnotationDTO_id") REFERENCES "GeneDiseaseAnnotationDTO" (id)
);
CREATE TABLE "GeneDiseaseAnnotationDTO_disease_qualifier_names" (
	"GeneDiseaseAnnotationDTO_id" TEXT, 
	disease_qualifier_names TEXT, 
	PRIMARY KEY ("GeneDiseaseAnnotationDTO_id", disease_qualifier_names), 
	FOREIGN KEY("GeneDiseaseAnnotationDTO_id") REFERENCES "GeneDiseaseAnnotationDTO" (id)
);
CREATE TABLE "AlleleDiseaseAnnotationDTO_asserted_gene_curies" (
	"AlleleDiseaseAnnotationDTO_id" TEXT, 
	asserted_gene_curies TEXT, 
	PRIMARY KEY ("AlleleDiseaseAnnotationDTO_id", asserted_gene_curies), 
	FOREIGN KEY("AlleleDiseaseAnnotationDTO_id") REFERENCES "AlleleDiseaseAnnotationDTO" (id)
);
CREATE TABLE "AlleleDiseaseAnnotationDTO_evidence_curies" (
	"AlleleDiseaseAnnotationDTO_id" TEXT, 
	evidence_curies TEXT, 
	PRIMARY KEY ("AlleleDiseaseAnnotationDTO_id", evidence_curies), 
	FOREIGN KEY("AlleleDiseaseAnnotationDTO_id") REFERENCES "AlleleDiseaseAnnotationDTO" (id)
);
CREATE TABLE "AlleleDiseaseAnnotationDTO_evidence_code_curies" (
	"AlleleDiseaseAnnotationDTO_id" TEXT, 
	evidence_code_curies TEXT, 
	PRIMARY KEY ("AlleleDiseaseAnnotationDTO_id", evidence_code_curies), 
	FOREIGN KEY("AlleleDiseaseAnnotationDTO_id") REFERENCES "AlleleDiseaseAnnotationDTO" (id)
);
CREATE TABLE "AlleleDiseaseAnnotationDTO_with_gene_curies" (
	"AlleleDiseaseAnnotationDTO_id" TEXT, 
	with_gene_curies TEXT, 
	PRIMARY KEY ("AlleleDiseaseAnnotationDTO_id", with_gene_curies), 
	FOREIGN KEY("AlleleDiseaseAnnotationDTO_id") REFERENCES "AlleleDiseaseAnnotationDTO" (id)
);
CREATE TABLE "AlleleDiseaseAnnotationDTO_disease_qualifier_names" (
	"AlleleDiseaseAnnotationDTO_id" TEXT, 
	disease_qualifier_names TEXT, 
	PRIMARY KEY ("AlleleDiseaseAnnotationDTO_id", disease_qualifier_names), 
	FOREIGN KEY("AlleleDiseaseAnnotationDTO_id") REFERENCES "AlleleDiseaseAnnotationDTO" (id)
);
CREATE TABLE "AGMDiseaseAnnotationDTO_asserted_gene_curies" (
	"AGMDiseaseAnnotationDTO_id" TEXT, 
	asserted_gene_curies TEXT, 
	PRIMARY KEY ("AGMDiseaseAnnotationDTO_id", asserted_gene_curies), 
	FOREIGN KEY("AGMDiseaseAnnotationDTO_id") REFERENCES "AGMDiseaseAnnotationDTO" (id)
);
CREATE TABLE "AGMDiseaseAnnotationDTO_evidence_curies" (
	"AGMDiseaseAnnotationDTO_id" TEXT, 
	evidence_curies TEXT, 
	PRIMARY KEY ("AGMDiseaseAnnotationDTO_id", evidence_curies), 
	FOREIGN KEY("AGMDiseaseAnnotationDTO_id") REFERENCES "AGMDiseaseAnnotationDTO" (id)
);
CREATE TABLE "AGMDiseaseAnnotationDTO_evidence_code_curies" (
	"AGMDiseaseAnnotationDTO_id" TEXT, 
	evidence_code_curies TEXT, 
	PRIMARY KEY ("AGMDiseaseAnnotationDTO_id", evidence_code_curies), 
	FOREIGN KEY("AGMDiseaseAnnotationDTO_id") REFERENCES "AGMDiseaseAnnotationDTO" (id)
);
CREATE TABLE "AGMDiseaseAnnotationDTO_with_gene_curies" (
	"AGMDiseaseAnnotationDTO_id" TEXT, 
	with_gene_curies TEXT, 
	PRIMARY KEY ("AGMDiseaseAnnotationDTO_id", with_gene_curies), 
	FOREIGN KEY("AGMDiseaseAnnotationDTO_id") REFERENCES "AGMDiseaseAnnotationDTO" (id)
);
CREATE TABLE "AGMDiseaseAnnotationDTO_disease_qualifier_names" (
	"AGMDiseaseAnnotationDTO_id" TEXT, 
	disease_qualifier_names TEXT, 
	PRIMARY KEY ("AGMDiseaseAnnotationDTO_id", disease_qualifier_names), 
	FOREIGN KEY("AGMDiseaseAnnotationDTO_id") REFERENCES "AGMDiseaseAnnotationDTO" (id)
);
CREATE TABLE "AlleleDTO_reference_curies" (
	"AlleleDTO_curie" TEXT, 
	reference_curies TEXT, 
	PRIMARY KEY ("AlleleDTO_curie", reference_curies), 
	FOREIGN KEY("AlleleDTO_curie") REFERENCES "AlleleDTO" (curie)
);
CREATE TABLE "AlleleDTO_secondary_identifiers" (
	"AlleleDTO_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("AlleleDTO_curie", secondary_identifiers), 
	FOREIGN KEY("AlleleDTO_curie") REFERENCES "AlleleDTO" (curie)
);
CREATE TABLE "SequenceTargetingReagentDTO_reference_curies" (
	"SequenceTargetingReagentDTO_curie" TEXT, 
	reference_curies TEXT, 
	PRIMARY KEY ("SequenceTargetingReagentDTO_curie", reference_curies), 
	FOREIGN KEY("SequenceTargetingReagentDTO_curie") REFERENCES "SequenceTargetingReagentDTO" (curie)
);
CREATE TABLE "SequenceTargetingReagentDTO_secondary_identifiers" (
	"SequenceTargetingReagentDTO_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("SequenceTargetingReagentDTO_curie", secondary_identifiers), 
	FOREIGN KEY("SequenceTargetingReagentDTO_curie") REFERENCES "SequenceTargetingReagentDTO" (curie)
);
CREATE TABLE "AlleleCellLineAssociationDTO_evidence_curies" (
	"AlleleCellLineAssociationDTO_id" TEXT, 
	evidence_curies TEXT, 
	PRIMARY KEY ("AlleleCellLineAssociationDTO_id", evidence_curies), 
	FOREIGN KEY("AlleleCellLineAssociationDTO_id") REFERENCES "AlleleCellLineAssociationDTO" (id)
);
CREATE TABLE "AlleleGenerationMethodAssociationDTO_evidence_curies" (
	"AlleleGenerationMethodAssociationDTO_id" TEXT, 
	evidence_curies TEXT, 
	PRIMARY KEY ("AlleleGenerationMethodAssociationDTO_id", evidence_curies), 
	FOREIGN KEY("AlleleGenerationMethodAssociationDTO_id") REFERENCES "AlleleGenerationMethodAssociationDTO" (id)
);
CREATE TABLE "AlleleImageAssociationDTO_evidence_curies" (
	"AlleleImageAssociationDTO_id" TEXT, 
	evidence_curies TEXT, 
	PRIMARY KEY ("AlleleImageAssociationDTO_id", evidence_curies), 
	FOREIGN KEY("AlleleImageAssociationDTO_id") REFERENCES "AlleleImageAssociationDTO" (id)
);
CREATE TABLE "AlleleOriginAssociationDTO_evidence_curies" (
	"AlleleOriginAssociationDTO_id" TEXT, 
	evidence_curies TEXT, 
	PRIMARY KEY ("AlleleOriginAssociationDTO_id", evidence_curies), 
	FOREIGN KEY("AlleleOriginAssociationDTO_id") REFERENCES "AlleleOriginAssociationDTO" (id)
);
CREATE TABLE "SlotAnnotation_evidence" (
	"SlotAnnotation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("SlotAnnotation_id", evidence), 
	FOREIGN KEY("SlotAnnotation_id") REFERENCES "SlotAnnotation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "Association_evidence" (
	"Association_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("Association_id", evidence), 
	FOREIGN KEY("Association_id") REFERENCES "Association" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "ResourceDescriptor_synonyms" (
	"ResourceDescriptor_id" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("ResourceDescriptor_id", synonyms), 
	FOREIGN KEY("ResourceDescriptor_id") REFERENCES "ResourceDescriptor" (id)
);
CREATE TABLE "ResourceDescriptor_resource_pages" (
	"ResourceDescriptor_id" TEXT, 
	resource_pages_id TEXT, 
	PRIMARY KEY ("ResourceDescriptor_id", resource_pages_id), 
	FOREIGN KEY("ResourceDescriptor_id") REFERENCES "ResourceDescriptor" (id), 
	FOREIGN KEY(resource_pages_id) REFERENCES "ResourceDescriptorPage" (id)
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
CREATE TABLE "AuthorReference_cross_reference" (
	"AuthorReference_id" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("AuthorReference_id", cross_reference_id), 
	FOREIGN KEY("AuthorReference_id") REFERENCES "AuthorReference" (id), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "Reference_authors" (
	"Reference_curie" TEXT, 
	authors_id TEXT, 
	PRIMARY KEY ("Reference_curie", authors_id), 
	FOREIGN KEY("Reference_curie") REFERENCES "Reference" (curie), 
	FOREIGN KEY(authors_id) REFERENCES "AuthorReference" (id)
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
CREATE TABLE "Resource_synonyms" (
	"Resource_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("Resource_curie", synonyms), 
	FOREIGN KEY("Resource_curie") REFERENCES "Resource" (curie)
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
CREATE TABLE "Gene_gene_types_secondary" (
	"Gene_curie" TEXT, 
	gene_types_secondary TEXT, 
	PRIMARY KEY ("Gene_curie", gene_types_secondary), 
	FOREIGN KEY("Gene_curie") REFERENCES "Gene" (curie), 
	FOREIGN KEY(gene_types_secondary) REFERENCES "SOTerm" (curie)
);
CREATE TABLE "Gene_designating_laboratories" (
	"Gene_curie" TEXT, 
	designating_laboratories TEXT, 
	PRIMARY KEY ("Gene_curie", designating_laboratories), 
	FOREIGN KEY("Gene_curie") REFERENCES "Gene" (curie), 
	FOREIGN KEY(designating_laboratories) REFERENCES "Laboratory" (curie)
);
CREATE TABLE "Gene_cross_reference" (
	"Gene_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("Gene_curie", cross_reference_id), 
	FOREIGN KEY("Gene_curie") REFERENCES "Gene" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "GeneDTO_secondary_identifiers" (
	"GeneDTO_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("GeneDTO_curie", secondary_identifiers), 
	FOREIGN KEY("GeneDTO_curie") REFERENCES "GeneDTO" (curie)
);
CREATE TABLE "GeneSymbolSlotAnnotation_evidence" (
	"GeneSymbolSlotAnnotation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("GeneSymbolSlotAnnotation_id", evidence), 
	FOREIGN KEY("GeneSymbolSlotAnnotation_id") REFERENCES "GeneSymbolSlotAnnotation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "GeneFullNameSlotAnnotation_evidence" (
	"GeneFullNameSlotAnnotation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("GeneFullNameSlotAnnotation_id", evidence), 
	FOREIGN KEY("GeneFullNameSlotAnnotation_id") REFERENCES "GeneFullNameSlotAnnotation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "GeneSystematicNameSlotAnnotation_evidence" (
	"GeneSystematicNameSlotAnnotation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("GeneSystematicNameSlotAnnotation_id", evidence), 
	FOREIGN KEY("GeneSystematicNameSlotAnnotation_id") REFERENCES "GeneSystematicNameSlotAnnotation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "GeneHistory_current_status" (
	"GeneHistory_id" TEXT, 
	current_status TEXT, 
	PRIMARY KEY ("GeneHistory_id", current_status), 
	FOREIGN KEY("GeneHistory_id") REFERENCES "GeneHistory" (id)
);
CREATE TABLE "GeneHistory_merged_into" (
	"GeneHistory_id" TEXT, 
	merged_into TEXT, 
	PRIMARY KEY ("GeneHistory_id", merged_into), 
	FOREIGN KEY("GeneHistory_id") REFERENCES "GeneHistory" (id), 
	FOREIGN KEY(merged_into) REFERENCES "Gene" (curie)
);
CREATE TABLE "GeneHistory_acquires_merge" (
	"GeneHistory_id" TEXT, 
	acquires_merge TEXT, 
	PRIMARY KEY ("GeneHistory_id", acquires_merge), 
	FOREIGN KEY("GeneHistory_id") REFERENCES "GeneHistory" (id), 
	FOREIGN KEY(acquires_merge) REFERENCES "Gene" (curie)
);
CREATE TABLE "GeneHistory_split_from" (
	"GeneHistory_id" TEXT, 
	split_from TEXT, 
	PRIMARY KEY ("GeneHistory_id", split_from), 
	FOREIGN KEY("GeneHistory_id") REFERENCES "GeneHistory" (id), 
	FOREIGN KEY(split_from) REFERENCES "Gene" (curie)
);
CREATE TABLE "GeneHistory_split_into" (
	"GeneHistory_id" TEXT, 
	split_into TEXT, 
	PRIMARY KEY ("GeneHistory_id", split_into), 
	FOREIGN KEY("GeneHistory_id") REFERENCES "GeneHistory" (id), 
	FOREIGN KEY(split_into) REFERENCES "Gene" (curie)
);
CREATE TABLE "GeneToGeneAssociation_evidence" (
	"GeneToGeneAssociation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("GeneToGeneAssociation_id", evidence), 
	FOREIGN KEY("GeneToGeneAssociation_id") REFERENCES "GeneToGeneAssociation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "GeneInteraction_cross_reference" (
	"GeneInteraction_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("GeneInteraction_curie", cross_reference_id), 
	FOREIGN KEY("GeneInteraction_curie") REFERENCES "GeneInteraction" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
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
CREATE TABLE "GeneInteraction_evidence" (
	"GeneInteraction_curie" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("GeneInteraction_curie", evidence), 
	FOREIGN KEY("GeneInteraction_curie") REFERENCES "GeneInteraction" (curie), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "GeneMolecularInteraction_cross_reference" (
	"GeneMolecularInteraction_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("GeneMolecularInteraction_curie", cross_reference_id), 
	FOREIGN KEY("GeneMolecularInteraction_curie") REFERENCES "GeneMolecularInteraction" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
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
CREATE TABLE "GeneMolecularInteraction_evidence" (
	"GeneMolecularInteraction_curie" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("GeneMolecularInteraction_curie", evidence), 
	FOREIGN KEY("GeneMolecularInteraction_curie") REFERENCES "GeneMolecularInteraction" (curie), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "GeneGeneticInteraction_phenotype_or_trait" (
	"GeneGeneticInteraction_curie" TEXT, 
	phenotype_or_trait TEXT, 
	PRIMARY KEY ("GeneGeneticInteraction_curie", phenotype_or_trait), 
	FOREIGN KEY("GeneGeneticInteraction_curie") REFERENCES "GeneGeneticInteraction" (curie)
);
CREATE TABLE "GeneGeneticInteraction_cross_reference" (
	"GeneGeneticInteraction_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("GeneGeneticInteraction_curie", cross_reference_id), 
	FOREIGN KEY("GeneGeneticInteraction_curie") REFERENCES "GeneGeneticInteraction" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
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
CREATE TABLE "GeneGeneticInteraction_evidence" (
	"GeneGeneticInteraction_curie" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("GeneGeneticInteraction_curie", evidence), 
	FOREIGN KEY("GeneGeneticInteraction_curie") REFERENCES "GeneGeneticInteraction" (curie), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "BulkLoadFileHistory_load_exceptions" (
	"BulkLoadFileHistory_id" TEXT, 
	load_exceptions TEXT, 
	PRIMARY KEY ("BulkLoadFileHistory_id", load_exceptions), 
	FOREIGN KEY("BulkLoadFileHistory_id") REFERENCES "BulkLoadFileHistory" (id)
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
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Variant_curie" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(assembly) REFERENCES "Assembly" (curie), 
	FOREIGN KEY(chromosome) REFERENCES "Chromosome" (curie), 
	FOREIGN KEY(evidence_code) REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(consequence) REFERENCES "SOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY("Variant_curie") REFERENCES "Variant" (curie)
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
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(transcript) REFERENCES "Transcript" (curie), 
	FOREIGN KEY(evidence_code) REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(consequence) REFERENCES "SOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
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
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(polypeptide) REFERENCES "Transcript" (curie), 
	FOREIGN KEY(evidence_code) REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(consequence) REFERENCES "SOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "ConstructComponentAssociation" (
	id INTEGER, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES "Construct" (curie), 
	FOREIGN KEY(predicate) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(object) REFERENCES "ConstructComponent" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "SequenceTargetingReagentToGeneAssociation" (
	id INTEGER, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES "SequenceTargetingReagent" (curie), 
	FOREIGN KEY(predicate) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(object) REFERENCES "Gene" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AlleleNoteSlotAnnotation" (
	id INTEGER, 
	single_allele TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	related_note_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(single_allele) REFERENCES "Allele" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(related_note_id) REFERENCES "Note" (id)
);
CREATE TABLE "AlleleAlleleAssociation" (
	id INTEGER, 
	evidence_code TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	related_note_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(evidence_code) REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY(subject) REFERENCES "Allele" (curie), 
	FOREIGN KEY(predicate) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(object) REFERENCES "Allele" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(related_note_id) REFERENCES "Note" (id)
);
CREATE TABLE "AlleleCellLineAssociation" (
	id INTEGER, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES "Allele" (curie), 
	FOREIGN KEY(predicate) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(object) REFERENCES "CellLine" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AlleleConstructAssociation" (
	id INTEGER, 
	evidence_code TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	related_note_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(evidence_code) REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY(subject) REFERENCES "Allele" (curie), 
	FOREIGN KEY(predicate) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(object) REFERENCES "Construct" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(related_note_id) REFERENCES "Note" (id)
);
CREATE TABLE "AlleleGeneAssociation" (
	id INTEGER, 
	evidence_code TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	related_note_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(evidence_code) REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY(subject) REFERENCES "Allele" (curie), 
	FOREIGN KEY(predicate) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(object) REFERENCES "Gene" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(related_note_id) REFERENCES "Note" (id)
);
CREATE TABLE "AlleleGenomicEntityAssociation" (
	id INTEGER, 
	evidence_code TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	related_note_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(evidence_code) REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY(subject) REFERENCES "Allele" (curie), 
	FOREIGN KEY(predicate) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(object) REFERENCES "GenomicEntity" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(related_note_id) REFERENCES "Note" (id)
);
CREATE TABLE "AlleleProteinAssociation" (
	id INTEGER, 
	evidence_code TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	related_note_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(evidence_code) REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY(subject) REFERENCES "Allele" (curie), 
	FOREIGN KEY(predicate) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(object) REFERENCES "Protein" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(related_note_id) REFERENCES "Note" (id)
);
CREATE TABLE "AlleleTranscriptAssociation" (
	id INTEGER, 
	evidence_code TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	related_note_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(evidence_code) REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY(subject) REFERENCES "Allele" (curie), 
	FOREIGN KEY(predicate) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(object) REFERENCES "Transcript" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(related_note_id) REFERENCES "Note" (id)
);
CREATE TABLE "AlleleVariantAssociation" (
	id INTEGER, 
	evidence_code TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	related_note_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(evidence_code) REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY(subject) REFERENCES "Allele" (curie), 
	FOREIGN KEY(predicate) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(object) REFERENCES "Variant" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(related_note_id) REFERENCES "Note" (id)
);
CREATE TABLE "PhenotypeAnnotation" (
	curie TEXT, 
	single_reference TEXT, 
	phenotype_term TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME NOT NULL, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(phenotype_term) REFERENCES "PhenotypeTerm" (curie), 
	FOREIGN KEY(subject) REFERENCES "BiologicalEntity" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "DiseaseAnnotation" (
	curie TEXT, 
	unique_id TEXT, 
	mod_entity_id TEXT, 
	negated BOOLEAN, 
	single_reference TEXT NOT NULL, 
	annotation_type TEXT, 
	genetic_sex TEXT, 
	disease_genetic_modifier TEXT, 
	disease_genetic_modifier_relation TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	data_provider_id TEXT NOT NULL, 
	secondary_data_provider_id TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(annotation_type) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(genetic_sex) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(disease_genetic_modifier_relation) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(subject) REFERENCES "BiologicalEntity" (curie), 
	FOREIGN KEY(object) REFERENCES "DOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(data_provider_id) REFERENCES "DataProvider" (id), 
	FOREIGN KEY(secondary_data_provider_id) REFERENCES "DataProvider" (id)
);
CREATE TABLE "AlleleDiseaseAnnotation" (
	inferred_gene TEXT, 
	curie TEXT, 
	unique_id TEXT, 
	mod_entity_id TEXT, 
	negated BOOLEAN, 
	single_reference TEXT NOT NULL, 
	annotation_type TEXT, 
	genetic_sex TEXT, 
	disease_genetic_modifier TEXT, 
	disease_genetic_modifier_relation TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	data_provider_id TEXT NOT NULL, 
	secondary_data_provider_id TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(inferred_gene) REFERENCES "Gene" (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(annotation_type) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(genetic_sex) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(disease_genetic_modifier_relation) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(subject) REFERENCES "Allele" (curie), 
	FOREIGN KEY(predicate) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(object) REFERENCES "DOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(data_provider_id) REFERENCES "DataProvider" (id), 
	FOREIGN KEY(secondary_data_provider_id) REFERENCES "DataProvider" (id)
);
CREATE TABLE "ExperimentalConditionDTO" (
	id INTEGER, 
	condition_class_curie TEXT NOT NULL, 
	condition_id_curie TEXT, 
	condition_free_text TEXT, 
	condition_quantity TEXT, 
	condition_anatomy_curie TEXT, 
	condition_gene_ontology_curie TEXT, 
	condition_taxon_curie TEXT, 
	condition_chemical_curie TEXT, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"ConditionRelationDTO_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("ConditionRelationDTO_id") REFERENCES "ConditionRelationDTO" (id)
);
CREATE TABLE "AlleleNoteSlotAnnotationDTO" (
	id INTEGER, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"AlleleDTO_curie" TEXT, 
	note_dto_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("AlleleDTO_curie") REFERENCES "AlleleDTO" (curie), 
	FOREIGN KEY(note_dto_id) REFERENCES "NoteDTO" (id)
);
CREATE TABLE "AlleleAlleleAssociationDTO" (
	id INTEGER, 
	object_allele_curie TEXT, 
	allele_curie TEXT NOT NULL, 
	predicate_name TEXT NOT NULL, 
	evidence_code_curie TEXT, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	note_dto_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(note_dto_id) REFERENCES "NoteDTO" (id)
);
CREATE TABLE "AlleleConstructAssociationDTO" (
	id INTEGER, 
	construct_curie TEXT NOT NULL, 
	allele_curie TEXT NOT NULL, 
	predicate_name TEXT NOT NULL, 
	evidence_code_curie TEXT, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	note_dto_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id), 
	FOREIGN KEY(note_dto_id) REFERENCES "NoteDTO" (id)
);
CREATE TABLE "AlleleGeneAssociationDTO" (
	id INTEGER, 
	gene_curie TEXT NOT NULL, 
	allele_curie TEXT NOT NULL, 
	predicate_name TEXT NOT NULL, 
	evidence_code_curie TEXT, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	note_dto_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id), 
	FOREIGN KEY(note_dto_id) REFERENCES "NoteDTO" (id)
);
CREATE TABLE "AlleleGenomicEntityAssociationDTO" (
	id INTEGER, 
	allele_curie TEXT NOT NULL, 
	predicate_name TEXT NOT NULL, 
	evidence_code_curie TEXT, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	note_dto_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(note_dto_id) REFERENCES "NoteDTO" (id)
);
CREATE TABLE "AlleleProteinAssociationDTO" (
	id INTEGER, 
	protein_curie TEXT NOT NULL, 
	allele_curie TEXT NOT NULL, 
	predicate_name TEXT NOT NULL, 
	evidence_code_curie TEXT, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	note_dto_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id), 
	FOREIGN KEY(note_dto_id) REFERENCES "NoteDTO" (id)
);
CREATE TABLE "AlleleTranscriptAssociationDTO" (
	id INTEGER, 
	transcript_curie TEXT NOT NULL, 
	allele_curie TEXT NOT NULL, 
	predicate_name TEXT NOT NULL, 
	evidence_code_curie TEXT, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	note_dto_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id), 
	FOREIGN KEY(note_dto_id) REFERENCES "NoteDTO" (id)
);
CREATE TABLE "AlleleVariantAssociationDTO" (
	id INTEGER, 
	variant_curie TEXT, 
	allele_curie TEXT NOT NULL, 
	predicate_name TEXT NOT NULL, 
	evidence_code_curie TEXT, 
	created_by_curie TEXT, 
	date_created DATETIME, 
	updated_by_curie TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	"Ingest_id" TEXT, 
	note_dto_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Ingest_id") REFERENCES "Ingest" (id), 
	FOREIGN KEY(note_dto_id) REFERENCES "NoteDTO" (id)
);
CREATE TABLE "GenomicLocationAssociation" (
	id INTEGER, 
	has_assembly TEXT NOT NULL, 
	start INTEGER, 
	"end" INTEGER, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_assembly) REFERENCES "Assembly" (curie), 
	FOREIGN KEY(subject) REFERENCES "GenomicEntity" (curie), 
	FOREIGN KEY(object) REFERENCES "Chromosome" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AffectedGenomicModel" (
	name TEXT, 
	subtype TEXT NOT NULL, 
	parental_populations TEXT, 
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	data_provider_id TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(subtype) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(data_provider_id) REFERENCES "DataProvider" (id)
);
CREATE TABLE "Image" (
	curie TEXT, 
	associated_with_figure TEXT NOT NULL, 
	width INTEGER NOT NULL, 
	height INTEGER NOT NULL, 
	cropped_from TEXT, 
	image_x_origin INTEGER, 
	image_y_origin INTEGER, 
	video_still BOOLEAN, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	image_file_id TEXT NOT NULL, 
	image_medium_file_id TEXT NOT NULL, 
	image_thumbnail_file_id TEXT NOT NULL, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(associated_with_figure) REFERENCES "Figure" (curie), 
	FOREIGN KEY(cropped_from) REFERENCES "Image" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(image_file_id) REFERENCES "File" (id), 
	FOREIGN KEY(image_medium_file_id) REFERENCES "File" (id), 
	FOREIGN KEY(image_thumbnail_file_id) REFERENCES "File" (id)
);
CREATE TABLE "CurationReportHistory" (
	id INTEGER, 
	curation_report_timestamp DATE, 
	pdf_file_path TEXT, 
	xls_file_path TEXT, 
	html_file_path TEXT, 
	curation_report_status TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	curation_report_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(curation_report_id) REFERENCES "CurationReport" (id)
);
CREATE TABLE "BulkLoadFile" (
	id INTEGER, 
	bulkload_status VARCHAR(24), 
	md5_sum TEXT, 
	local_file_path TEXT, 
	file_size INTEGER, 
	s3_path TEXT, 
	s3_url TEXT, 
	record_count INTEGER, 
	error_message TEXT, 
	date_last_loaded DATETIME, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	bulk_load_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(bulk_load_id) REFERENCES "BulkLoad" (id)
);
CREATE TABLE "GeneCluster" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	related_note_id TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(related_note_id) REFERENCES "Note" (id)
);
CREATE TABLE "GeneCollection" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	related_note_id TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(related_note_id) REFERENCES "Note" (id)
);
CREATE TABLE "GeneNomenclatureSet" (
	curie TEXT, 
	designating_laboratory TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	related_note_id TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(designating_laboratory) REFERENCES "Laboratory" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(related_note_id) REFERENCES "Note" (id)
);
CREATE TABLE "Operon" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	related_note_id TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(taxon) REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(related_note_id) REFERENCES "Note" (id)
);
CREATE TABLE "GeneToPathwayAssociation" (
	id INTEGER, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES "Gene" (curie), 
	FOREIGN KEY(object) REFERENCES "Pathway" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Variant_related_notes" (
	"Variant_curie" TEXT, 
	related_notes_id TEXT, 
	PRIMARY KEY ("Variant_curie", related_notes_id), 
	FOREIGN KEY("Variant_curie") REFERENCES "Variant" (curie), 
	FOREIGN KEY(related_notes_id) REFERENCES "Note" (id)
);
CREATE TABLE "Variant_source_variant_locations" (
	"Variant_curie" TEXT, 
	source_variant_locations_id TEXT, 
	PRIMARY KEY ("Variant_curie", source_variant_locations_id), 
	FOREIGN KEY("Variant_curie") REFERENCES "Variant" (curie), 
	FOREIGN KEY(source_variant_locations_id) REFERENCES "SourceVariantLocation" (id)
);
CREATE TABLE "Variant_cross_reference" (
	"Variant_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("Variant_curie", cross_reference_id), 
	FOREIGN KEY("Variant_curie") REFERENCES "Variant" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "Variant_secondary_identifiers" (
	"Variant_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("Variant_curie", secondary_identifiers), 
	FOREIGN KEY("Variant_curie") REFERENCES "Variant" (curie)
);
CREATE TABLE "SourceVariantLocation_variant_locations" (
	"SourceVariantLocation_id" TEXT, 
	variant_locations_id TEXT, 
	PRIMARY KEY ("SourceVariantLocation_id", variant_locations_id), 
	FOREIGN KEY("SourceVariantLocation_id") REFERENCES "SourceVariantLocation" (id), 
	FOREIGN KEY(variant_locations_id) REFERENCES "VariantLocation" (id)
);
CREATE TABLE "OntologyTerm_ancestors" (
	"OntologyTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("OntologyTerm_curie", ancestors_id), 
	FOREIGN KEY("OntologyTerm_curie") REFERENCES "OntologyTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "OntologyTerm_descendants" (
	"OntologyTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("OntologyTerm_curie", descendants_id), 
	FOREIGN KEY("OntologyTerm_curie") REFERENCES "OntologyTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "OntologyTermClosure_relationship_type" (
	"OntologyTermClosure_id" TEXT, 
	relationship_type TEXT, 
	PRIMARY KEY ("OntologyTermClosure_id", relationship_type), 
	FOREIGN KEY("OntologyTermClosure_id") REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "OntologyTermClosure_evidence" (
	"OntologyTermClosure_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("OntologyTermClosure_id", evidence), 
	FOREIGN KEY("OntologyTermClosure_id") REFERENCES "OntologyTermClosure" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "DOTerm_ancestors" (
	"DOTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("DOTerm_curie", ancestors_id), 
	FOREIGN KEY("DOTerm_curie") REFERENCES "DOTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "DOTerm_descendants" (
	"DOTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("DOTerm_curie", descendants_id), 
	FOREIGN KEY("DOTerm_curie") REFERENCES "DOTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "ECOTerm_ancestors" (
	"ECOTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("ECOTerm_curie", ancestors_id), 
	FOREIGN KEY("ECOTerm_curie") REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "ECOTerm_descendants" (
	"ECOTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("ECOTerm_curie", descendants_id), 
	FOREIGN KEY("ECOTerm_curie") REFERENCES "ECOTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "NCBITaxonTerm_ancestors" (
	"NCBITaxonTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("NCBITaxonTerm_curie", ancestors_id), 
	FOREIGN KEY("NCBITaxonTerm_curie") REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "NCBITaxonTerm_descendants" (
	"NCBITaxonTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("NCBITaxonTerm_curie", descendants_id), 
	FOREIGN KEY("NCBITaxonTerm_curie") REFERENCES "NCBITaxonTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "FBCVTerm_ancestors" (
	"FBCVTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("FBCVTerm_curie", ancestors_id), 
	FOREIGN KEY("FBCVTerm_curie") REFERENCES "FBCVTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "FBCVTerm_descendants" (
	"FBCVTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("FBCVTerm_curie", descendants_id), 
	FOREIGN KEY("FBCVTerm_curie") REFERENCES "FBCVTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "GOTerm_ancestors" (
	"GOTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("GOTerm_curie", ancestors_id), 
	FOREIGN KEY("GOTerm_curie") REFERENCES "GOTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "GOTerm_descendants" (
	"GOTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("GOTerm_curie", descendants_id), 
	FOREIGN KEY("GOTerm_curie") REFERENCES "GOTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "ROTerm_ancestors" (
	"ROTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("ROTerm_curie", ancestors_id), 
	FOREIGN KEY("ROTerm_curie") REFERENCES "ROTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "ROTerm_descendants" (
	"ROTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("ROTerm_curie", descendants_id), 
	FOREIGN KEY("ROTerm_curie") REFERENCES "ROTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "MITerm_ancestors" (
	"MITerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("MITerm_curie", ancestors_id), 
	FOREIGN KEY("MITerm_curie") REFERENCES "MITerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "MITerm_descendants" (
	"MITerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("MITerm_curie", descendants_id), 
	FOREIGN KEY("MITerm_curie") REFERENCES "MITerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "MMOTerm_ancestors" (
	"MMOTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("MMOTerm_curie", ancestors_id), 
	FOREIGN KEY("MMOTerm_curie") REFERENCES "MMOTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "MMOTerm_descendants" (
	"MMOTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("MMOTerm_curie", descendants_id), 
	FOREIGN KEY("MMOTerm_curie") REFERENCES "MMOTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "MMUSDVTerm_ancestors" (
	"MMUSDVTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("MMUSDVTerm_curie", ancestors_id), 
	FOREIGN KEY("MMUSDVTerm_curie") REFERENCES "MMUSDVTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "MMUSDVTerm_descendants" (
	"MMUSDVTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("MMUSDVTerm_curie", descendants_id), 
	FOREIGN KEY("MMUSDVTerm_curie") REFERENCES "MMUSDVTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "SOTerm_ancestors" (
	"SOTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("SOTerm_curie", ancestors_id), 
	FOREIGN KEY("SOTerm_curie") REFERENCES "SOTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "SOTerm_descendants" (
	"SOTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("SOTerm_curie", descendants_id), 
	FOREIGN KEY("SOTerm_curie") REFERENCES "SOTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "XBEDTerm_ancestors" (
	"XBEDTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("XBEDTerm_curie", ancestors_id), 
	FOREIGN KEY("XBEDTerm_curie") REFERENCES "XBEDTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "XBEDTerm_descendants" (
	"XBEDTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("XBEDTerm_curie", descendants_id), 
	FOREIGN KEY("XBEDTerm_curie") REFERENCES "XBEDTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "CHEBITerm_ancestors" (
	"CHEBITerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("CHEBITerm_curie", ancestors_id), 
	FOREIGN KEY("CHEBITerm_curie") REFERENCES "CHEBITerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "CHEBITerm_descendants" (
	"CHEBITerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("CHEBITerm_curie", descendants_id), 
	FOREIGN KEY("CHEBITerm_curie") REFERENCES "CHEBITerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "StageTerm_ancestors" (
	"StageTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("StageTerm_curie", ancestors_id), 
	FOREIGN KEY("StageTerm_curie") REFERENCES "StageTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "StageTerm_descendants" (
	"StageTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("StageTerm_curie", descendants_id), 
	FOREIGN KEY("StageTerm_curie") REFERENCES "StageTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "FBDVTerm_ancestors" (
	"FBDVTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("FBDVTerm_curie", ancestors_id), 
	FOREIGN KEY("FBDVTerm_curie") REFERENCES "FBDVTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "FBDVTerm_descendants" (
	"FBDVTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("FBDVTerm_curie", descendants_id), 
	FOREIGN KEY("FBDVTerm_curie") REFERENCES "FBDVTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "WBLSTerm_ancestors" (
	"WBLSTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("WBLSTerm_curie", ancestors_id), 
	FOREIGN KEY("WBLSTerm_curie") REFERENCES "WBLSTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "WBLSTerm_descendants" (
	"WBLSTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("WBLSTerm_curie", descendants_id), 
	FOREIGN KEY("WBLSTerm_curie") REFERENCES "WBLSTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "XBSTerm_ancestors" (
	"XBSTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("XBSTerm_curie", ancestors_id), 
	FOREIGN KEY("XBSTerm_curie") REFERENCES "XBSTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "XBSTerm_descendants" (
	"XBSTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("XBSTerm_curie", descendants_id), 
	FOREIGN KEY("XBSTerm_curie") REFERENCES "XBSTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "ZFSTerm_ancestors" (
	"ZFSTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("ZFSTerm_curie", ancestors_id), 
	FOREIGN KEY("ZFSTerm_curie") REFERENCES "ZFSTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "ZFSTerm_descendants" (
	"ZFSTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("ZFSTerm_curie", descendants_id), 
	FOREIGN KEY("ZFSTerm_curie") REFERENCES "ZFSTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "ExperimentalConditionOntologyTerm_ancestors" (
	"ExperimentalConditionOntologyTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("ExperimentalConditionOntologyTerm_curie", ancestors_id), 
	FOREIGN KEY("ExperimentalConditionOntologyTerm_curie") REFERENCES "ExperimentalConditionOntologyTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "ExperimentalConditionOntologyTerm_descendants" (
	"ExperimentalConditionOntologyTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("ExperimentalConditionOntologyTerm_curie", descendants_id), 
	FOREIGN KEY("ExperimentalConditionOntologyTerm_curie") REFERENCES "ExperimentalConditionOntologyTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "ZECOTerm_ancestors" (
	"ZECOTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("ZECOTerm_curie", ancestors_id), 
	FOREIGN KEY("ZECOTerm_curie") REFERENCES "ZECOTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "ZECOTerm_descendants" (
	"ZECOTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("ZECOTerm_curie", descendants_id), 
	FOREIGN KEY("ZECOTerm_curie") REFERENCES "ZECOTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "XCOTerm_ancestors" (
	"XCOTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("XCOTerm_curie", ancestors_id), 
	FOREIGN KEY("XCOTerm_curie") REFERENCES "XCOTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "XCOTerm_descendants" (
	"XCOTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("XCOTerm_curie", descendants_id), 
	FOREIGN KEY("XCOTerm_curie") REFERENCES "XCOTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "AnatomicalTerm_ancestors" (
	"AnatomicalTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("AnatomicalTerm_curie", ancestors_id), 
	FOREIGN KEY("AnatomicalTerm_curie") REFERENCES "AnatomicalTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "AnatomicalTerm_descendants" (
	"AnatomicalTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("AnatomicalTerm_curie", descendants_id), 
	FOREIGN KEY("AnatomicalTerm_curie") REFERENCES "AnatomicalTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "CLTerm_ancestors" (
	"CLTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("CLTerm_curie", ancestors_id), 
	FOREIGN KEY("CLTerm_curie") REFERENCES "CLTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "CLTerm_descendants" (
	"CLTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("CLTerm_curie", descendants_id), 
	FOREIGN KEY("CLTerm_curie") REFERENCES "CLTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "EMAPATerm_ancestors" (
	"EMAPATerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("EMAPATerm_curie", ancestors_id), 
	FOREIGN KEY("EMAPATerm_curie") REFERENCES "EMAPATerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "EMAPATerm_descendants" (
	"EMAPATerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("EMAPATerm_curie", descendants_id), 
	FOREIGN KEY("EMAPATerm_curie") REFERENCES "EMAPATerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "DAOTerm_ancestors" (
	"DAOTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("DAOTerm_curie", ancestors_id), 
	FOREIGN KEY("DAOTerm_curie") REFERENCES "DAOTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "DAOTerm_descendants" (
	"DAOTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("DAOTerm_curie", descendants_id), 
	FOREIGN KEY("DAOTerm_curie") REFERENCES "DAOTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "MATerm_ancestors" (
	"MATerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("MATerm_curie", ancestors_id), 
	FOREIGN KEY("MATerm_curie") REFERENCES "MATerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "MATerm_descendants" (
	"MATerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("MATerm_curie", descendants_id), 
	FOREIGN KEY("MATerm_curie") REFERENCES "MATerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "UBERONTerm_ancestors" (
	"UBERONTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("UBERONTerm_curie", ancestors_id), 
	FOREIGN KEY("UBERONTerm_curie") REFERENCES "UBERONTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "UBERONTerm_descendants" (
	"UBERONTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("UBERONTerm_curie", descendants_id), 
	FOREIGN KEY("UBERONTerm_curie") REFERENCES "UBERONTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "WBBTTerm_ancestors" (
	"WBBTTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("WBBTTerm_curie", ancestors_id), 
	FOREIGN KEY("WBBTTerm_curie") REFERENCES "WBBTTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "WBBTTerm_descendants" (
	"WBBTTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("WBBTTerm_curie", descendants_id), 
	FOREIGN KEY("WBBTTerm_curie") REFERENCES "WBBTTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "XBATerm_ancestors" (
	"XBATerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("XBATerm_curie", ancestors_id), 
	FOREIGN KEY("XBATerm_curie") REFERENCES "XBATerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "XBATerm_descendants" (
	"XBATerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("XBATerm_curie", descendants_id), 
	FOREIGN KEY("XBATerm_curie") REFERENCES "XBATerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "ZFATerm_ancestors" (
	"ZFATerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("ZFATerm_curie", ancestors_id), 
	FOREIGN KEY("ZFATerm_curie") REFERENCES "ZFATerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "ZFATerm_descendants" (
	"ZFATerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("ZFATerm_curie", descendants_id), 
	FOREIGN KEY("ZFATerm_curie") REFERENCES "ZFATerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "PhenotypeTerm_ancestors" (
	"PhenotypeTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("PhenotypeTerm_curie", ancestors_id), 
	FOREIGN KEY("PhenotypeTerm_curie") REFERENCES "PhenotypeTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "PhenotypeTerm_descendants" (
	"PhenotypeTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("PhenotypeTerm_curie", descendants_id), 
	FOREIGN KEY("PhenotypeTerm_curie") REFERENCES "PhenotypeTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "XPOTerm_ancestors" (
	"XPOTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("XPOTerm_curie", ancestors_id), 
	FOREIGN KEY("XPOTerm_curie") REFERENCES "XPOTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "XPOTerm_descendants" (
	"XPOTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("XPOTerm_curie", descendants_id), 
	FOREIGN KEY("XPOTerm_curie") REFERENCES "XPOTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "MPTerm_ancestors" (
	"MPTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("MPTerm_curie", ancestors_id), 
	FOREIGN KEY("MPTerm_curie") REFERENCES "MPTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "MPTerm_descendants" (
	"MPTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("MPTerm_curie", descendants_id), 
	FOREIGN KEY("MPTerm_curie") REFERENCES "MPTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "ATPTerm_ancestors" (
	"ATPTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("ATPTerm_curie", ancestors_id), 
	FOREIGN KEY("ATPTerm_curie") REFERENCES "ATPTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "ATPTerm_descendants" (
	"ATPTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("ATPTerm_curie", descendants_id), 
	FOREIGN KEY("ATPTerm_curie") REFERENCES "ATPTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "ChemicalTerm_ancestors" (
	"ChemicalTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("ChemicalTerm_curie", ancestors_id), 
	FOREIGN KEY("ChemicalTerm_curie") REFERENCES "ChemicalTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "ChemicalTerm_descendants" (
	"ChemicalTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("ChemicalTerm_curie", descendants_id), 
	FOREIGN KEY("ChemicalTerm_curie") REFERENCES "ChemicalTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "XSMOTerm_ancestors" (
	"XSMOTerm_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("XSMOTerm_curie", ancestors_id), 
	FOREIGN KEY("XSMOTerm_curie") REFERENCES "XSMOTerm" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "XSMOTerm_descendants" (
	"XSMOTerm_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("XSMOTerm_curie", descendants_id), 
	FOREIGN KEY("XSMOTerm_curie") REFERENCES "XSMOTerm" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "Molecule_ancestors" (
	"Molecule_curie" TEXT, 
	ancestors_id TEXT, 
	PRIMARY KEY ("Molecule_curie", ancestors_id), 
	FOREIGN KEY("Molecule_curie") REFERENCES "Molecule" (curie), 
	FOREIGN KEY(ancestors_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "Molecule_descendants" (
	"Molecule_curie" TEXT, 
	descendants_id TEXT, 
	PRIMARY KEY ("Molecule_curie", descendants_id), 
	FOREIGN KEY("Molecule_curie") REFERENCES "Molecule" (curie), 
	FOREIGN KEY(descendants_id) REFERENCES "OntologyTermClosure" (id)
);
CREATE TABLE "Allele_allele_inheritance_modes" (
	"Allele_curie" TEXT, 
	allele_inheritance_modes_id TEXT, 
	PRIMARY KEY ("Allele_curie", allele_inheritance_modes_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(allele_inheritance_modes_id) REFERENCES "AlleleInheritanceModeSlotAnnotation" (id)
);
CREATE TABLE "Allele_allele_functional_impacts" (
	"Allele_curie" TEXT, 
	allele_functional_impacts_id TEXT, 
	PRIMARY KEY ("Allele_curie", allele_functional_impacts_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(allele_functional_impacts_id) REFERENCES "AlleleFunctionalImpactSlotAnnotation" (id)
);
CREATE TABLE "Allele_allele_nomenclature_events" (
	"Allele_curie" TEXT, 
	allele_nomenclature_events_id TEXT, 
	PRIMARY KEY ("Allele_curie", allele_nomenclature_events_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(allele_nomenclature_events_id) REFERENCES "AlleleNomenclatureEventSlotAnnotation" (id)
);
CREATE TABLE "Allele_allele_synonyms" (
	"Allele_curie" TEXT, 
	allele_synonyms_id TEXT, 
	PRIMARY KEY ("Allele_curie", allele_synonyms_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(allele_synonyms_id) REFERENCES "AlleleSynonymSlotAnnotation" (id)
);
CREATE TABLE "CellLine_cross_reference" (
	"CellLine_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("CellLine_curie", cross_reference_id), 
	FOREIGN KEY("CellLine_curie") REFERENCES "CellLine" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "CellLine_secondary_identifiers" (
	"CellLine_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("CellLine_curie", secondary_identifiers), 
	FOREIGN KEY("CellLine_curie") REFERENCES "CellLine" (curie)
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
CREATE TABLE "Construct_cross_reference" (
	"Construct_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("Construct_curie", cross_reference_id), 
	FOREIGN KEY("Construct_curie") REFERENCES "Construct" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "Construct_secondary_identifiers" (
	"Construct_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("Construct_curie", secondary_identifiers), 
	FOREIGN KEY("Construct_curie") REFERENCES "Construct" (curie)
);
CREATE TABLE "ConstructComponent_cross_reference" (
	"ConstructComponent_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("ConstructComponent_curie", cross_reference_id), 
	FOREIGN KEY("ConstructComponent_curie") REFERENCES "ConstructComponent" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "ConstructComponent_secondary_identifiers" (
	"ConstructComponent_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("ConstructComponent_curie", secondary_identifiers), 
	FOREIGN KEY("ConstructComponent_curie") REFERENCES "ConstructComponent" (curie)
);
CREATE TABLE "GenerationMethod_mutagenesis_methods" (
	"GenerationMethod_id" TEXT, 
	mutagenesis_methods TEXT, 
	PRIMARY KEY ("GenerationMethod_id", mutagenesis_methods), 
	FOREIGN KEY("GenerationMethod_id") REFERENCES "GenerationMethod" (id), 
	FOREIGN KEY(mutagenesis_methods) REFERENCES "VocabularyTerm" (name)
);
CREATE TABLE "SequenceTargetingReagent_reference" (
	"SequenceTargetingReagent_curie" TEXT, 
	reference TEXT, 
	PRIMARY KEY ("SequenceTargetingReagent_curie", reference), 
	FOREIGN KEY("SequenceTargetingReagent_curie") REFERENCES "SequenceTargetingReagent" (curie), 
	FOREIGN KEY(reference) REFERENCES "Reference" (curie)
);
CREATE TABLE "SequenceTargetingReagent_cross_reference" (
	"SequenceTargetingReagent_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("SequenceTargetingReagent_curie", cross_reference_id), 
	FOREIGN KEY("SequenceTargetingReagent_curie") REFERENCES "SequenceTargetingReagent" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "SequenceTargetingReagent_secondary_identifiers" (
	"SequenceTargetingReagent_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("SequenceTargetingReagent_curie", secondary_identifiers), 
	FOREIGN KEY("SequenceTargetingReagent_curie") REFERENCES "SequenceTargetingReagent" (curie)
);
CREATE TABLE "AlleleFunctionalImpactSlotAnnotation_functional_impacts" (
	"AlleleFunctionalImpactSlotAnnotation_id" TEXT, 
	functional_impacts TEXT NOT NULL, 
	PRIMARY KEY ("AlleleFunctionalImpactSlotAnnotation_id", functional_impacts), 
	FOREIGN KEY("AlleleFunctionalImpactSlotAnnotation_id") REFERENCES "AlleleFunctionalImpactSlotAnnotation" (id), 
	FOREIGN KEY(functional_impacts) REFERENCES "VocabularyTerm" (name)
);
CREATE TABLE "AlleleFunctionalImpactSlotAnnotation_evidence" (
	"AlleleFunctionalImpactSlotAnnotation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AlleleFunctionalImpactSlotAnnotation_id", evidence), 
	FOREIGN KEY("AlleleFunctionalImpactSlotAnnotation_id") REFERENCES "AlleleFunctionalImpactSlotAnnotation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "AlleleInheritanceModeSlotAnnotation_evidence" (
	"AlleleInheritanceModeSlotAnnotation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AlleleInheritanceModeSlotAnnotation_id", evidence), 
	FOREIGN KEY("AlleleInheritanceModeSlotAnnotation_id") REFERENCES "AlleleInheritanceModeSlotAnnotation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "AlleleNomenclatureEventSlotAnnotation_evidence" (
	"AlleleNomenclatureEventSlotAnnotation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AlleleNomenclatureEventSlotAnnotation_id", evidence), 
	FOREIGN KEY("AlleleNomenclatureEventSlotAnnotation_id") REFERENCES "AlleleNomenclatureEventSlotAnnotation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "AlleleSynonymSlotAnnotation_evidence" (
	"AlleleSynonymSlotAnnotation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AlleleSynonymSlotAnnotation_id", evidence), 
	FOREIGN KEY("AlleleSynonymSlotAnnotation_id") REFERENCES "AlleleSynonymSlotAnnotation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "AllelePhenotypeAnnotation_asserted_gene" (
	"AllelePhenotypeAnnotation_curie" TEXT, 
	asserted_gene TEXT, 
	PRIMARY KEY ("AllelePhenotypeAnnotation_curie", asserted_gene), 
	FOREIGN KEY("AllelePhenotypeAnnotation_curie") REFERENCES "AllelePhenotypeAnnotation" (curie), 
	FOREIGN KEY(asserted_gene) REFERENCES "Gene" (curie)
);
CREATE TABLE "AllelePhenotypeAnnotation_condition_relations" (
	"AllelePhenotypeAnnotation_curie" TEXT, 
	condition_relations_id TEXT, 
	PRIMARY KEY ("AllelePhenotypeAnnotation_curie", condition_relations_id), 
	FOREIGN KEY("AllelePhenotypeAnnotation_curie") REFERENCES "AllelePhenotypeAnnotation" (curie), 
	FOREIGN KEY(condition_relations_id) REFERENCES "ConditionRelation" (id)
);
CREATE TABLE "AllelePhenotypeAnnotation_evidence" (
	"AllelePhenotypeAnnotation_curie" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AllelePhenotypeAnnotation_curie", evidence), 
	FOREIGN KEY("AllelePhenotypeAnnotation_curie") REFERENCES "AllelePhenotypeAnnotation" (curie), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "ConditionRelation_conditions" (
	"ConditionRelation_id" TEXT, 
	conditions_id TEXT, 
	PRIMARY KEY ("ConditionRelation_id", conditions_id), 
	FOREIGN KEY("ConditionRelation_id") REFERENCES "ConditionRelation" (id), 
	FOREIGN KEY(conditions_id) REFERENCES "ExperimentalCondition" (id)
);
CREATE TABLE "AlleleFunctionalImpactSlotAnnotationDTO_functional_impact_names" (
	"AlleleFunctionalImpactSlotAnnotationDTO_id" TEXT, 
	functional_impact_names TEXT NOT NULL, 
	PRIMARY KEY ("AlleleFunctionalImpactSlotAnnotationDTO_id", functional_impact_names), 
	FOREIGN KEY("AlleleFunctionalImpactSlotAnnotationDTO_id") REFERENCES "AlleleFunctionalImpactSlotAnnotationDTO" (id)
);
CREATE TABLE "AlleleFunctionalImpactSlotAnnotationDTO_evidence_curies" (
	"AlleleFunctionalImpactSlotAnnotationDTO_id" TEXT, 
	evidence_curies TEXT, 
	PRIMARY KEY ("AlleleFunctionalImpactSlotAnnotationDTO_id", evidence_curies), 
	FOREIGN KEY("AlleleFunctionalImpactSlotAnnotationDTO_id") REFERENCES "AlleleFunctionalImpactSlotAnnotationDTO" (id)
);
CREATE TABLE "AlleleInheritanceModeSlotAnnotationDTO_evidence_curies" (
	"AlleleInheritanceModeSlotAnnotationDTO_id" TEXT, 
	evidence_curies TEXT, 
	PRIMARY KEY ("AlleleInheritanceModeSlotAnnotationDTO_id", evidence_curies), 
	FOREIGN KEY("AlleleInheritanceModeSlotAnnotationDTO_id") REFERENCES "AlleleInheritanceModeSlotAnnotationDTO" (id)
);
CREATE TABLE "AlleleMolecularMutationSlotAnnotationDTO_molecular_mutation_names" (
	"AlleleMolecularMutationSlotAnnotationDTO_id" TEXT, 
	molecular_mutation_names TEXT NOT NULL, 
	PRIMARY KEY ("AlleleMolecularMutationSlotAnnotationDTO_id", molecular_mutation_names), 
	FOREIGN KEY("AlleleMolecularMutationSlotAnnotationDTO_id") REFERENCES "AlleleMolecularMutationSlotAnnotationDTO" (id)
);
CREATE TABLE "AlleleMolecularMutationSlotAnnotationDTO_evidence_curies" (
	"AlleleMolecularMutationSlotAnnotationDTO_id" TEXT, 
	evidence_curies TEXT, 
	PRIMARY KEY ("AlleleMolecularMutationSlotAnnotationDTO_id", evidence_curies), 
	FOREIGN KEY("AlleleMolecularMutationSlotAnnotationDTO_id") REFERENCES "AlleleMolecularMutationSlotAnnotationDTO" (id)
);
CREATE TABLE "AlleleMutationTypeSlotAnnotationDTO_mutation_type_curies" (
	"AlleleMutationTypeSlotAnnotationDTO_id" TEXT, 
	mutation_type_curies TEXT, 
	PRIMARY KEY ("AlleleMutationTypeSlotAnnotationDTO_id", mutation_type_curies), 
	FOREIGN KEY("AlleleMutationTypeSlotAnnotationDTO_id") REFERENCES "AlleleMutationTypeSlotAnnotationDTO" (id)
);
CREATE TABLE "AlleleMutationTypeSlotAnnotationDTO_evidence_curies" (
	"AlleleMutationTypeSlotAnnotationDTO_id" TEXT, 
	evidence_curies TEXT, 
	PRIMARY KEY ("AlleleMutationTypeSlotAnnotationDTO_id", evidence_curies), 
	FOREIGN KEY("AlleleMutationTypeSlotAnnotationDTO_id") REFERENCES "AlleleMutationTypeSlotAnnotationDTO" (id)
);
CREATE TABLE "AlleleNomenclatureEventSlotAnnotationDTO_evidence_curies" (
	"AlleleNomenclatureEventSlotAnnotationDTO_id" TEXT, 
	evidence_curies TEXT, 
	PRIMARY KEY ("AlleleNomenclatureEventSlotAnnotationDTO_id", evidence_curies), 
	FOREIGN KEY("AlleleNomenclatureEventSlotAnnotationDTO_id") REFERENCES "AlleleNomenclatureEventSlotAnnotationDTO" (id)
);
CREATE TABLE "AlleleSecondaryIdSlotAnnotationDTO_evidence_curies" (
	"AlleleSecondaryIdSlotAnnotationDTO_id" TEXT, 
	evidence_curies TEXT, 
	PRIMARY KEY ("AlleleSecondaryIdSlotAnnotationDTO_id", evidence_curies), 
	FOREIGN KEY("AlleleSecondaryIdSlotAnnotationDTO_id") REFERENCES "AlleleSecondaryIdSlotAnnotationDTO" (id)
);
CREATE TABLE "GenomicEntity_cross_reference" (
	"GenomicEntity_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("GenomicEntity_curie", cross_reference_id), 
	FOREIGN KEY("GenomicEntity_curie") REFERENCES "GenomicEntity" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "GenomicEntity_secondary_identifiers" (
	"GenomicEntity_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("GenomicEntity_curie", secondary_identifiers), 
	FOREIGN KEY("GenomicEntity_curie") REFERENCES "GenomicEntity" (curie)
);
CREATE TABLE "Transcript_cross_reference" (
	"Transcript_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("Transcript_curie", cross_reference_id), 
	FOREIGN KEY("Transcript_curie") REFERENCES "Transcript" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "Transcript_secondary_identifiers" (
	"Transcript_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("Transcript_curie", secondary_identifiers), 
	FOREIGN KEY("Transcript_curie") REFERENCES "Transcript" (curie)
);
CREATE TABLE "Note_evidence" (
	"Note_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("Note_id", evidence), 
	FOREIGN KEY("Note_id") REFERENCES "Note" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "NoteDTO_evidence_curies" (
	"NoteDTO_id" TEXT, 
	evidence_curies TEXT, 
	PRIMARY KEY ("NoteDTO_id", evidence_curies), 
	FOREIGN KEY("NoteDTO_id") REFERENCES "NoteDTO" (id)
);
CREATE TABLE "NameSlotAnnotation_evidence" (
	"NameSlotAnnotation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("NameSlotAnnotation_id", evidence), 
	FOREIGN KEY("NameSlotAnnotation_id") REFERENCES "NameSlotAnnotation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "NameSlotAnnotationDTO_evidence_curies" (
	"NameSlotAnnotationDTO_id" TEXT, 
	evidence_curies TEXT, 
	PRIMARY KEY ("NameSlotAnnotationDTO_id", evidence_curies), 
	FOREIGN KEY("NameSlotAnnotationDTO_id") REFERENCES "NameSlotAnnotationDTO" (id)
);
CREATE TABLE "GenomicLocationAssociationDTO_evidence_curies" (
	"GenomicLocationAssociationDTO_id" TEXT, 
	evidence_curies TEXT, 
	PRIMARY KEY ("GenomicLocationAssociationDTO_id", evidence_curies), 
	FOREIGN KEY("GenomicLocationAssociationDTO_id") REFERENCES "GenomicLocationAssociationDTO" (id)
);
CREATE TABLE "Protein_cross_reference" (
	"Protein_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("Protein_curie", cross_reference_id), 
	FOREIGN KEY("Protein_curie") REFERENCES "Protein" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "Protein_secondary_identifiers" (
	"Protein_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("Protein_curie", secondary_identifiers), 
	FOREIGN KEY("Protein_curie") REFERENCES "Protein" (curie)
);
CREATE TABLE "VocabularyTermSet_member_terms" (
	"VocabularyTermSet_name" TEXT, 
	member_terms TEXT, 
	PRIMARY KEY ("VocabularyTermSet_name", member_terms), 
	FOREIGN KEY("VocabularyTermSet_name") REFERENCES "VocabularyTermSet" (name), 
	FOREIGN KEY(member_terms) REFERENCES "VocabularyTerm" (name)
);
CREATE TABLE "Figure_secondary_identifiers" (
	"Figure_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("Figure_curie", secondary_identifiers), 
	FOREIGN KEY("Figure_curie") REFERENCES "Figure" (curie)
);
CREATE TABLE "Gene_gene_synonyms" (
	"Gene_curie" TEXT, 
	gene_synonyms_id TEXT, 
	PRIMARY KEY ("Gene_curie", gene_synonyms_id), 
	FOREIGN KEY("Gene_curie") REFERENCES "Gene" (curie), 
	FOREIGN KEY(gene_synonyms_id) REFERENCES "GeneSynonymSlotAnnotation" (id)
);
CREATE TABLE "Gene_related_notes" (
	"Gene_curie" TEXT, 
	related_notes_id TEXT, 
	PRIMARY KEY ("Gene_curie", related_notes_id), 
	FOREIGN KEY("Gene_curie") REFERENCES "Gene" (curie), 
	FOREIGN KEY(related_notes_id) REFERENCES "Note" (id)
);
CREATE TABLE "GeneSynonymSlotAnnotation_evidence" (
	"GeneSynonymSlotAnnotation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("GeneSynonymSlotAnnotation_id", evidence), 
	FOREIGN KEY("GeneSynonymSlotAnnotation_id") REFERENCES "GeneSynonymSlotAnnotation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "GeneticMapPosition_genetic_map_position_centimorgan" (
	"GeneticMapPosition_curie" TEXT, 
	genetic_map_position_centimorgan FLOAT, 
	PRIMARY KEY ("GeneticMapPosition_curie", genetic_map_position_centimorgan), 
	FOREIGN KEY("GeneticMapPosition_curie") REFERENCES "GeneticMapPosition" (curie)
);
CREATE TABLE "GeneticMapPosition_genetic_map_position_centimorgan_error" (
	"GeneticMapPosition_curie" TEXT, 
	genetic_map_position_centimorgan_error FLOAT, 
	PRIMARY KEY ("GeneticMapPosition_curie", genetic_map_position_centimorgan_error), 
	FOREIGN KEY("GeneticMapPosition_curie") REFERENCES "GeneticMapPosition" (curie)
);
CREATE TABLE "GeneticMapPosition_genetic_map_position_radiation" (
	"GeneticMapPosition_curie" TEXT, 
	genetic_map_position_radiation FLOAT, 
	PRIMARY KEY ("GeneticMapPosition_curie", genetic_map_position_radiation), 
	FOREIGN KEY("GeneticMapPosition_curie") REFERENCES "GeneticMapPosition" (curie)
);
CREATE TABLE "GeneticMapPosition_cross_reference" (
	"GeneticMapPosition_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("GeneticMapPosition_curie", cross_reference_id), 
	FOREIGN KEY("GeneticMapPosition_curie") REFERENCES "GeneticMapPosition" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "GeneticMapPosition_secondary_identifiers" (
	"GeneticMapPosition_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("GeneticMapPosition_curie", secondary_identifiers), 
	FOREIGN KEY("GeneticMapPosition_curie") REFERENCES "GeneticMapPosition" (curie)
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
CREATE TABLE "Antibody_cross_reference" (
	"Antibody_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("Antibody_curie", cross_reference_id), 
	FOREIGN KEY("Antibody_curie") REFERENCES "Antibody" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
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
CREATE TABLE "BulkLoadGroup_loads" (
	"BulkLoadGroup_id" TEXT, 
	loads_id TEXT, 
	PRIMARY KEY ("BulkLoadGroup_id", loads_id), 
	FOREIGN KEY("BulkLoadGroup_id") REFERENCES "BulkLoadGroup" (id), 
	FOREIGN KEY(loads_id) REFERENCES "BulkLoad" (id)
);
CREATE TABLE "UniGeneSet_genes" (
	"UniGeneSet_curie" TEXT, 
	genes TEXT, 
	PRIMARY KEY ("UniGeneSet_curie", genes), 
	FOREIGN KEY("UniGeneSet_curie") REFERENCES "UniGeneSet" (curie), 
	FOREIGN KEY(genes) REFERENCES "Gene" (curie)
);
CREATE TABLE "FunctionalGeneSet_genes" (
	"FunctionalGeneSet_curie" TEXT, 
	genes TEXT, 
	PRIMARY KEY ("FunctionalGeneSet_curie", genes), 
	FOREIGN KEY("FunctionalGeneSet_curie") REFERENCES "FunctionalGeneSet" (curie), 
	FOREIGN KEY(genes) REFERENCES "Gene" (curie)
);
CREATE TABLE "ProteinComplex_proteins" (
	"ProteinComplex_curie" TEXT, 
	proteins TEXT, 
	PRIMARY KEY ("ProteinComplex_curie", proteins), 
	FOREIGN KEY("ProteinComplex_curie") REFERENCES "ProteinComplex" (curie), 
	FOREIGN KEY(proteins) REFERENCES "Protein" (curie)
);
CREATE TABLE "AlleleGenerationMethodAssociation" (
	id INTEGER, 
	mutation_target_strain TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	object_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(mutation_target_strain) REFERENCES "AffectedGenomicModel" (curie), 
	FOREIGN KEY(subject) REFERENCES "Allele" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(object_id) REFERENCES "GenerationMethod" (id)
);
CREATE TABLE "AlleleImageAssociation" (
	id INTEGER, 
	primary_image BOOLEAN, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES "Allele" (curie), 
	FOREIGN KEY(predicate) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(object) REFERENCES "Image" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AlleleOriginAssociation" (
	id INTEGER, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES "Allele" (curie), 
	FOREIGN KEY(object) REFERENCES "AffectedGenomicModel" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "GenePhenotypeAnnotation" (
	sgd_strain_background TEXT, 
	curie TEXT, 
	single_reference TEXT, 
	phenotype_term TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME NOT NULL, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(sgd_strain_background) REFERENCES "AffectedGenomicModel" (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(phenotype_term) REFERENCES "PhenotypeTerm" (curie), 
	FOREIGN KEY(subject) REFERENCES "Gene" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "AGMPhenotypeAnnotation" (
	inferred_allele TEXT, 
	inferred_gene TEXT, 
	asserted_allele TEXT, 
	curie TEXT, 
	single_reference TEXT, 
	phenotype_term TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME NOT NULL, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(inferred_allele) REFERENCES "Allele" (curie), 
	FOREIGN KEY(inferred_gene) REFERENCES "Gene" (curie), 
	FOREIGN KEY(asserted_allele) REFERENCES "Allele" (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(phenotype_term) REFERENCES "PhenotypeTerm" (curie), 
	FOREIGN KEY(subject) REFERENCES "AffectedGenomicModel" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "GeneDiseaseAnnotation" (
	sgd_strain_background TEXT, 
	curie TEXT, 
	unique_id TEXT, 
	mod_entity_id TEXT, 
	negated BOOLEAN, 
	single_reference TEXT NOT NULL, 
	annotation_type TEXT, 
	genetic_sex TEXT, 
	disease_genetic_modifier TEXT, 
	disease_genetic_modifier_relation TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	data_provider_id TEXT NOT NULL, 
	secondary_data_provider_id TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(sgd_strain_background) REFERENCES "AffectedGenomicModel" (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(annotation_type) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(genetic_sex) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(disease_genetic_modifier_relation) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(subject) REFERENCES "Gene" (curie), 
	FOREIGN KEY(predicate) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(object) REFERENCES "DOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(data_provider_id) REFERENCES "DataProvider" (id), 
	FOREIGN KEY(secondary_data_provider_id) REFERENCES "DataProvider" (id)
);
CREATE TABLE "AGMDiseaseAnnotation" (
	inferred_allele TEXT, 
	inferred_gene TEXT, 
	asserted_allele TEXT, 
	curie TEXT, 
	unique_id TEXT, 
	mod_entity_id TEXT, 
	negated BOOLEAN, 
	single_reference TEXT NOT NULL, 
	annotation_type TEXT, 
	genetic_sex TEXT, 
	disease_genetic_modifier TEXT, 
	disease_genetic_modifier_relation TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	data_provider_id TEXT NOT NULL, 
	secondary_data_provider_id TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(inferred_allele) REFERENCES "Allele" (curie), 
	FOREIGN KEY(inferred_gene) REFERENCES "Gene" (curie), 
	FOREIGN KEY(asserted_allele) REFERENCES "Allele" (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(annotation_type) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(genetic_sex) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(disease_genetic_modifier_relation) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(subject) REFERENCES "AffectedGenomicModel" (curie), 
	FOREIGN KEY(predicate) REFERENCES "VocabularyTerm" (name), 
	FOREIGN KEY(object) REFERENCES "DOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(data_provider_id) REFERENCES "DataProvider" (id), 
	FOREIGN KEY(secondary_data_provider_id) REFERENCES "DataProvider" (id)
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
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(from_image) REFERENCES "Image" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
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
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	subject_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(object) REFERENCES "Gene" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(subject_id) REFERENCES "VariantGenomeLocation" (id)
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
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	subject_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(object) REFERENCES "Transcript" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(subject_id) REFERENCES "VariantTranscriptLocation" (id)
);
CREATE TABLE "ExpressionExperiment" (
	curie TEXT NOT NULL, 
	single_reference TEXT, 
	biological_entity_assayed TEXT, 
	assay_used TEXT, 
	specimen_genomic_model TEXT, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(single_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(biological_entity_assayed) REFERENCES "BiologicalEntity" (curie), 
	FOREIGN KEY(assay_used) REFERENCES "MMOTerm" (curie), 
	FOREIGN KEY(specimen_genomic_model) REFERENCES "AffectedGenomicModel" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id)
);
CREATE TABLE "Variant_variant_polypeptide_locations" (
	"Variant_curie" TEXT, 
	variant_polypeptide_locations_id TEXT, 
	PRIMARY KEY ("Variant_curie", variant_polypeptide_locations_id), 
	FOREIGN KEY("Variant_curie") REFERENCES "Variant" (curie), 
	FOREIGN KEY(variant_polypeptide_locations_id) REFERENCES "VariantPolypeptideLocation" (id)
);
CREATE TABLE "Variant_variant_transcript_locations" (
	"Variant_curie" TEXT, 
	variant_transcript_locations_id TEXT, 
	PRIMARY KEY ("Variant_curie", variant_transcript_locations_id), 
	FOREIGN KEY("Variant_curie") REFERENCES "Variant" (curie), 
	FOREIGN KEY(variant_transcript_locations_id) REFERENCES "VariantTranscriptLocation" (id)
);
CREATE TABLE "Variant_genomic_location_associations" (
	"Variant_curie" TEXT, 
	genomic_location_associations_id TEXT, 
	PRIMARY KEY ("Variant_curie", genomic_location_associations_id), 
	FOREIGN KEY("Variant_curie") REFERENCES "Variant" (curie), 
	FOREIGN KEY(genomic_location_associations_id) REFERENCES "GenomicLocationAssociation" (id)
);
CREATE TABLE "VariantPolypeptideLocation_associated_transcripts" (
	"VariantPolypeptideLocation_id" TEXT, 
	associated_transcripts TEXT, 
	PRIMARY KEY ("VariantPolypeptideLocation_id", associated_transcripts), 
	FOREIGN KEY("VariantPolypeptideLocation_id") REFERENCES "VariantPolypeptideLocation" (id), 
	FOREIGN KEY(associated_transcripts) REFERENCES "Transcript" (curie)
);
CREATE TABLE "Allele_allele_notes" (
	"Allele_curie" TEXT, 
	allele_notes_id TEXT, 
	PRIMARY KEY ("Allele_curie", allele_notes_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(allele_notes_id) REFERENCES "AlleleNoteSlotAnnotation" (id)
);
CREATE TABLE "Allele_allele_gene_associations" (
	"Allele_curie" TEXT, 
	allele_gene_associations_id TEXT, 
	PRIMARY KEY ("Allele_curie", allele_gene_associations_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(allele_gene_associations_id) REFERENCES "AlleleGeneAssociation" (id)
);
CREATE TABLE "Allele_allele_transcript_associations" (
	"Allele_curie" TEXT, 
	allele_transcript_associations_id TEXT, 
	PRIMARY KEY ("Allele_curie", allele_transcript_associations_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(allele_transcript_associations_id) REFERENCES "AlleleTranscriptAssociation" (id)
);
CREATE TABLE "Allele_allele_protein_associations" (
	"Allele_curie" TEXT, 
	allele_protein_associations_id TEXT, 
	PRIMARY KEY ("Allele_curie", allele_protein_associations_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(allele_protein_associations_id) REFERENCES "AlleleProteinAssociation" (id)
);
CREATE TABLE "Allele_allele_allele_associations" (
	"Allele_curie" TEXT, 
	allele_allele_associations_id TEXT, 
	PRIMARY KEY ("Allele_curie", allele_allele_associations_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(allele_allele_associations_id) REFERENCES "AlleleAlleleAssociation" (id)
);
CREATE TABLE "Allele_allele_variant_associations" (
	"Allele_curie" TEXT, 
	allele_variant_associations_id TEXT, 
	PRIMARY KEY ("Allele_curie", allele_variant_associations_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(allele_variant_associations_id) REFERENCES "AlleleVariantAssociation" (id)
);
CREATE TABLE "Allele_allele_construct_associations" (
	"Allele_curie" TEXT, 
	allele_construct_associations_id TEXT, 
	PRIMARY KEY ("Allele_curie", allele_construct_associations_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(allele_construct_associations_id) REFERENCES "AlleleConstructAssociation" (id)
);
CREATE TABLE "Allele_allele_cell_line_associations" (
	"Allele_curie" TEXT, 
	allele_cell_line_associations_id TEXT, 
	PRIMARY KEY ("Allele_curie", allele_cell_line_associations_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(allele_cell_line_associations_id) REFERENCES "AlleleCellLineAssociation" (id)
);
CREATE TABLE "Allele_genomic_location_associations" (
	"Allele_curie" TEXT, 
	genomic_location_associations_id TEXT, 
	PRIMARY KEY ("Allele_curie", genomic_location_associations_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(genomic_location_associations_id) REFERENCES "GenomicLocationAssociation" (id)
);
CREATE TABLE "CellLine_genomic_location_associations" (
	"CellLine_curie" TEXT, 
	genomic_location_associations_id TEXT, 
	PRIMARY KEY ("CellLine_curie", genomic_location_associations_id), 
	FOREIGN KEY("CellLine_curie") REFERENCES "CellLine" (curie), 
	FOREIGN KEY(genomic_location_associations_id) REFERENCES "GenomicLocationAssociation" (id)
);
CREATE TABLE "Construct_genomic_location_associations" (
	"Construct_curie" TEXT, 
	genomic_location_associations_id TEXT, 
	PRIMARY KEY ("Construct_curie", genomic_location_associations_id), 
	FOREIGN KEY("Construct_curie") REFERENCES "Construct" (curie), 
	FOREIGN KEY(genomic_location_associations_id) REFERENCES "GenomicLocationAssociation" (id)
);
CREATE TABLE "ConstructComponent_genomic_location_associations" (
	"ConstructComponent_curie" TEXT, 
	genomic_location_associations_id TEXT, 
	PRIMARY KEY ("ConstructComponent_curie", genomic_location_associations_id), 
	FOREIGN KEY("ConstructComponent_curie") REFERENCES "ConstructComponent" (curie), 
	FOREIGN KEY(genomic_location_associations_id) REFERENCES "GenomicLocationAssociation" (id)
);
CREATE TABLE "ConstructComponentAssociation_evidence" (
	"ConstructComponentAssociation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("ConstructComponentAssociation_id", evidence), 
	FOREIGN KEY("ConstructComponentAssociation_id") REFERENCES "ConstructComponentAssociation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "SequenceTargetingReagent_genomic_location_associations" (
	"SequenceTargetingReagent_curie" TEXT, 
	genomic_location_associations_id TEXT, 
	PRIMARY KEY ("SequenceTargetingReagent_curie", genomic_location_associations_id), 
	FOREIGN KEY("SequenceTargetingReagent_curie") REFERENCES "SequenceTargetingReagent" (curie), 
	FOREIGN KEY(genomic_location_associations_id) REFERENCES "GenomicLocationAssociation" (id)
);
CREATE TABLE "SequenceTargetingReagentToGeneAssociation_reference" (
	"SequenceTargetingReagentToGeneAssociation_id" TEXT, 
	reference TEXT, 
	PRIMARY KEY ("SequenceTargetingReagentToGeneAssociation_id", reference), 
	FOREIGN KEY("SequenceTargetingReagentToGeneAssociation_id") REFERENCES "SequenceTargetingReagentToGeneAssociation" (id), 
	FOREIGN KEY(reference) REFERENCES "Reference" (curie)
);
CREATE TABLE "SequenceTargetingReagentToGeneAssociation_evidence" (
	"SequenceTargetingReagentToGeneAssociation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("SequenceTargetingReagentToGeneAssociation_id", evidence), 
	FOREIGN KEY("SequenceTargetingReagentToGeneAssociation_id") REFERENCES "SequenceTargetingReagentToGeneAssociation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "AlleleNoteSlotAnnotation_evidence" (
	"AlleleNoteSlotAnnotation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AlleleNoteSlotAnnotation_id", evidence), 
	FOREIGN KEY("AlleleNoteSlotAnnotation_id") REFERENCES "AlleleNoteSlotAnnotation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "AlleleAlleleAssociation_evidence" (
	"AlleleAlleleAssociation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AlleleAlleleAssociation_id", evidence), 
	FOREIGN KEY("AlleleAlleleAssociation_id") REFERENCES "AlleleAlleleAssociation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "AlleleCellLineAssociation_evidence" (
	"AlleleCellLineAssociation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AlleleCellLineAssociation_id", evidence), 
	FOREIGN KEY("AlleleCellLineAssociation_id") REFERENCES "AlleleCellLineAssociation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "AlleleConstructAssociation_evidence" (
	"AlleleConstructAssociation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AlleleConstructAssociation_id", evidence), 
	FOREIGN KEY("AlleleConstructAssociation_id") REFERENCES "AlleleConstructAssociation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "AlleleGeneAssociation_evidence" (
	"AlleleGeneAssociation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AlleleGeneAssociation_id", evidence), 
	FOREIGN KEY("AlleleGeneAssociation_id") REFERENCES "AlleleGeneAssociation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "AlleleGenomicEntityAssociation_evidence" (
	"AlleleGenomicEntityAssociation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AlleleGenomicEntityAssociation_id", evidence), 
	FOREIGN KEY("AlleleGenomicEntityAssociation_id") REFERENCES "AlleleGenomicEntityAssociation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "AlleleProteinAssociation_evidence" (
	"AlleleProteinAssociation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AlleleProteinAssociation_id", evidence), 
	FOREIGN KEY("AlleleProteinAssociation_id") REFERENCES "AlleleProteinAssociation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "AlleleTranscriptAssociation_evidence" (
	"AlleleTranscriptAssociation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AlleleTranscriptAssociation_id", evidence), 
	FOREIGN KEY("AlleleTranscriptAssociation_id") REFERENCES "AlleleTranscriptAssociation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "AlleleVariantAssociation_evidence" (
	"AlleleVariantAssociation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AlleleVariantAssociation_id", evidence), 
	FOREIGN KEY("AlleleVariantAssociation_id") REFERENCES "AlleleVariantAssociation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "PhenotypeAnnotation_condition_relations" (
	"PhenotypeAnnotation_curie" TEXT, 
	condition_relations_id TEXT, 
	PRIMARY KEY ("PhenotypeAnnotation_curie", condition_relations_id), 
	FOREIGN KEY("PhenotypeAnnotation_curie") REFERENCES "PhenotypeAnnotation" (curie), 
	FOREIGN KEY(condition_relations_id) REFERENCES "ConditionRelation" (id)
);
CREATE TABLE "PhenotypeAnnotation_evidence" (
	"PhenotypeAnnotation_curie" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("PhenotypeAnnotation_curie", evidence), 
	FOREIGN KEY("PhenotypeAnnotation_curie") REFERENCES "PhenotypeAnnotation" (curie), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "DiseaseAnnotation_evidence_codes" (
	"DiseaseAnnotation_curie" TEXT, 
	evidence_codes TEXT NOT NULL, 
	PRIMARY KEY ("DiseaseAnnotation_curie", evidence_codes), 
	FOREIGN KEY("DiseaseAnnotation_curie") REFERENCES "DiseaseAnnotation" (curie), 
	FOREIGN KEY(evidence_codes) REFERENCES "ECOTerm" (curie)
);
CREATE TABLE "DiseaseAnnotation_with_or_from" (
	"DiseaseAnnotation_curie" TEXT, 
	with_or_from TEXT, 
	PRIMARY KEY ("DiseaseAnnotation_curie", with_or_from), 
	FOREIGN KEY("DiseaseAnnotation_curie") REFERENCES "DiseaseAnnotation" (curie), 
	FOREIGN KEY(with_or_from) REFERENCES "Gene" (curie)
);
CREATE TABLE "DiseaseAnnotation_disease_qualifiers" (
	"DiseaseAnnotation_curie" TEXT, 
	disease_qualifiers TEXT, 
	PRIMARY KEY ("DiseaseAnnotation_curie", disease_qualifiers), 
	FOREIGN KEY("DiseaseAnnotation_curie") REFERENCES "DiseaseAnnotation" (curie), 
	FOREIGN KEY(disease_qualifiers) REFERENCES "VocabularyTerm" (name)
);
CREATE TABLE "DiseaseAnnotation_condition_relations" (
	"DiseaseAnnotation_curie" TEXT, 
	condition_relations_id TEXT, 
	PRIMARY KEY ("DiseaseAnnotation_curie", condition_relations_id), 
	FOREIGN KEY("DiseaseAnnotation_curie") REFERENCES "DiseaseAnnotation" (curie), 
	FOREIGN KEY(condition_relations_id) REFERENCES "ConditionRelation" (id)
);
CREATE TABLE "DiseaseAnnotation_related_notes" (
	"DiseaseAnnotation_curie" TEXT, 
	related_notes_id TEXT, 
	PRIMARY KEY ("DiseaseAnnotation_curie", related_notes_id), 
	FOREIGN KEY("DiseaseAnnotation_curie") REFERENCES "DiseaseAnnotation" (curie), 
	FOREIGN KEY(related_notes_id) REFERENCES "Note" (id)
);
CREATE TABLE "DiseaseAnnotation_evidence" (
	"DiseaseAnnotation_curie" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("DiseaseAnnotation_curie", evidence), 
	FOREIGN KEY("DiseaseAnnotation_curie") REFERENCES "DiseaseAnnotation" (curie), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "AlleleDiseaseAnnotation_asserted_gene" (
	"AlleleDiseaseAnnotation_curie" TEXT, 
	asserted_gene TEXT, 
	PRIMARY KEY ("AlleleDiseaseAnnotation_curie", asserted_gene), 
	FOREIGN KEY("AlleleDiseaseAnnotation_curie") REFERENCES "AlleleDiseaseAnnotation" (curie), 
	FOREIGN KEY(asserted_gene) REFERENCES "Gene" (curie)
);
CREATE TABLE "AlleleDiseaseAnnotation_evidence_codes" (
	"AlleleDiseaseAnnotation_curie" TEXT, 
	evidence_codes TEXT NOT NULL, 
	PRIMARY KEY ("AlleleDiseaseAnnotation_curie", evidence_codes), 
	FOREIGN KEY("AlleleDiseaseAnnotation_curie") REFERENCES "AlleleDiseaseAnnotation" (curie), 
	FOREIGN KEY(evidence_codes) REFERENCES "ECOTerm" (curie)
);
CREATE TABLE "AlleleDiseaseAnnotation_with_or_from" (
	"AlleleDiseaseAnnotation_curie" TEXT, 
	with_or_from TEXT, 
	PRIMARY KEY ("AlleleDiseaseAnnotation_curie", with_or_from), 
	FOREIGN KEY("AlleleDiseaseAnnotation_curie") REFERENCES "AlleleDiseaseAnnotation" (curie), 
	FOREIGN KEY(with_or_from) REFERENCES "Gene" (curie)
);
CREATE TABLE "AlleleDiseaseAnnotation_disease_qualifiers" (
	"AlleleDiseaseAnnotation_curie" TEXT, 
	disease_qualifiers TEXT, 
	PRIMARY KEY ("AlleleDiseaseAnnotation_curie", disease_qualifiers), 
	FOREIGN KEY("AlleleDiseaseAnnotation_curie") REFERENCES "AlleleDiseaseAnnotation" (curie), 
	FOREIGN KEY(disease_qualifiers) REFERENCES "VocabularyTerm" (name)
);
CREATE TABLE "AlleleDiseaseAnnotation_condition_relations" (
	"AlleleDiseaseAnnotation_curie" TEXT, 
	condition_relations_id TEXT, 
	PRIMARY KEY ("AlleleDiseaseAnnotation_curie", condition_relations_id), 
	FOREIGN KEY("AlleleDiseaseAnnotation_curie") REFERENCES "AlleleDiseaseAnnotation" (curie), 
	FOREIGN KEY(condition_relations_id) REFERENCES "ConditionRelation" (id)
);
CREATE TABLE "AlleleDiseaseAnnotation_related_notes" (
	"AlleleDiseaseAnnotation_curie" TEXT, 
	related_notes_id TEXT, 
	PRIMARY KEY ("AlleleDiseaseAnnotation_curie", related_notes_id), 
	FOREIGN KEY("AlleleDiseaseAnnotation_curie") REFERENCES "AlleleDiseaseAnnotation" (curie), 
	FOREIGN KEY(related_notes_id) REFERENCES "Note" (id)
);
CREATE TABLE "AlleleDiseaseAnnotation_evidence" (
	"AlleleDiseaseAnnotation_curie" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AlleleDiseaseAnnotation_curie", evidence), 
	FOREIGN KEY("AlleleDiseaseAnnotation_curie") REFERENCES "AlleleDiseaseAnnotation" (curie), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "AlleleNoteSlotAnnotationDTO_evidence_curies" (
	"AlleleNoteSlotAnnotationDTO_id" TEXT, 
	evidence_curies TEXT, 
	PRIMARY KEY ("AlleleNoteSlotAnnotationDTO_id", evidence_curies), 
	FOREIGN KEY("AlleleNoteSlotAnnotationDTO_id") REFERENCES "AlleleNoteSlotAnnotationDTO" (id)
);
CREATE TABLE "AlleleAlleleAssociationDTO_evidence_curies" (
	"AlleleAlleleAssociationDTO_id" TEXT, 
	evidence_curies TEXT NOT NULL, 
	PRIMARY KEY ("AlleleAlleleAssociationDTO_id", evidence_curies), 
	FOREIGN KEY("AlleleAlleleAssociationDTO_id") REFERENCES "AlleleAlleleAssociationDTO" (id)
);
CREATE TABLE "AlleleConstructAssociationDTO_evidence_curies" (
	"AlleleConstructAssociationDTO_id" TEXT, 
	evidence_curies TEXT NOT NULL, 
	PRIMARY KEY ("AlleleConstructAssociationDTO_id", evidence_curies), 
	FOREIGN KEY("AlleleConstructAssociationDTO_id") REFERENCES "AlleleConstructAssociationDTO" (id)
);
CREATE TABLE "AlleleGeneAssociationDTO_evidence_curies" (
	"AlleleGeneAssociationDTO_id" TEXT, 
	evidence_curies TEXT NOT NULL, 
	PRIMARY KEY ("AlleleGeneAssociationDTO_id", evidence_curies), 
	FOREIGN KEY("AlleleGeneAssociationDTO_id") REFERENCES "AlleleGeneAssociationDTO" (id)
);
CREATE TABLE "AlleleGenomicEntityAssociationDTO_evidence_curies" (
	"AlleleGenomicEntityAssociationDTO_id" TEXT, 
	evidence_curies TEXT NOT NULL, 
	PRIMARY KEY ("AlleleGenomicEntityAssociationDTO_id", evidence_curies), 
	FOREIGN KEY("AlleleGenomicEntityAssociationDTO_id") REFERENCES "AlleleGenomicEntityAssociationDTO" (id)
);
CREATE TABLE "AlleleProteinAssociationDTO_evidence_curies" (
	"AlleleProteinAssociationDTO_id" TEXT, 
	evidence_curies TEXT NOT NULL, 
	PRIMARY KEY ("AlleleProteinAssociationDTO_id", evidence_curies), 
	FOREIGN KEY("AlleleProteinAssociationDTO_id") REFERENCES "AlleleProteinAssociationDTO" (id)
);
CREATE TABLE "AlleleTranscriptAssociationDTO_evidence_curies" (
	"AlleleTranscriptAssociationDTO_id" TEXT, 
	evidence_curies TEXT NOT NULL, 
	PRIMARY KEY ("AlleleTranscriptAssociationDTO_id", evidence_curies), 
	FOREIGN KEY("AlleleTranscriptAssociationDTO_id") REFERENCES "AlleleTranscriptAssociationDTO" (id)
);
CREATE TABLE "AlleleVariantAssociationDTO_evidence_curies" (
	"AlleleVariantAssociationDTO_id" TEXT, 
	evidence_curies TEXT NOT NULL, 
	PRIMARY KEY ("AlleleVariantAssociationDTO_id", evidence_curies), 
	FOREIGN KEY("AlleleVariantAssociationDTO_id") REFERENCES "AlleleVariantAssociationDTO" (id)
);
CREATE TABLE "GenomicEntity_genomic_location_associations" (
	"GenomicEntity_curie" TEXT, 
	genomic_location_associations_id TEXT, 
	PRIMARY KEY ("GenomicEntity_curie", genomic_location_associations_id), 
	FOREIGN KEY("GenomicEntity_curie") REFERENCES "GenomicEntity" (curie), 
	FOREIGN KEY(genomic_location_associations_id) REFERENCES "GenomicLocationAssociation" (id)
);
CREATE TABLE "Transcript_genomic_location_associations" (
	"Transcript_curie" TEXT, 
	genomic_location_associations_id TEXT, 
	PRIMARY KEY ("Transcript_curie", genomic_location_associations_id), 
	FOREIGN KEY("Transcript_curie") REFERENCES "Transcript" (curie), 
	FOREIGN KEY(genomic_location_associations_id) REFERENCES "GenomicLocationAssociation" (id)
);
CREATE TABLE "GenomicLocationAssociation_evidence" (
	"GenomicLocationAssociation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("GenomicLocationAssociation_id", evidence), 
	FOREIGN KEY("GenomicLocationAssociation_id") REFERENCES "GenomicLocationAssociation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "Protein_genomic_location_associations" (
	"Protein_curie" TEXT, 
	genomic_location_associations_id TEXT, 
	PRIMARY KEY ("Protein_curie", genomic_location_associations_id), 
	FOREIGN KEY("Protein_curie") REFERENCES "Protein" (curie), 
	FOREIGN KEY(genomic_location_associations_id) REFERENCES "GenomicLocationAssociation" (id)
);
CREATE TABLE "AffectedGenomicModel_component" (
	"AffectedGenomicModel_curie" TEXT, 
	component_id TEXT, 
	PRIMARY KEY ("AffectedGenomicModel_curie", component_id), 
	FOREIGN KEY("AffectedGenomicModel_curie") REFERENCES "AffectedGenomicModel" (curie), 
	FOREIGN KEY(component_id) REFERENCES "AffectedGenomicModelComponent" (id)
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
CREATE TABLE "AffectedGenomicModel_cross_reference" (
	"AffectedGenomicModel_curie" TEXT, 
	cross_reference_id TEXT, 
	PRIMARY KEY ("AffectedGenomicModel_curie", cross_reference_id), 
	FOREIGN KEY("AffectedGenomicModel_curie") REFERENCES "AffectedGenomicModel" (curie), 
	FOREIGN KEY(cross_reference_id) REFERENCES "CrossReference" (id)
);
CREATE TABLE "AffectedGenomicModel_secondary_identifiers" (
	"AffectedGenomicModel_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("AffectedGenomicModel_curie", secondary_identifiers), 
	FOREIGN KEY("AffectedGenomicModel_curie") REFERENCES "AffectedGenomicModel" (curie)
);
CREATE TABLE "AffectedGenomicModel_genomic_location_associations" (
	"AffectedGenomicModel_curie" TEXT, 
	genomic_location_associations_id TEXT, 
	PRIMARY KEY ("AffectedGenomicModel_curie", genomic_location_associations_id), 
	FOREIGN KEY("AffectedGenomicModel_curie") REFERENCES "AffectedGenomicModel" (curie), 
	FOREIGN KEY(genomic_location_associations_id) REFERENCES "GenomicLocationAssociation" (id)
);
CREATE TABLE "Image_secondary_identifiers" (
	"Image_curie" TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY ("Image_curie", secondary_identifiers), 
	FOREIGN KEY("Image_curie") REFERENCES "Image" (curie)
);
CREATE TABLE "Gene_genomic_location_associations" (
	"Gene_curie" TEXT, 
	genomic_location_associations_id TEXT, 
	PRIMARY KEY ("Gene_curie", genomic_location_associations_id), 
	FOREIGN KEY("Gene_curie") REFERENCES "Gene" (curie), 
	FOREIGN KEY(genomic_location_associations_id) REFERENCES "GenomicLocationAssociation" (id)
);
CREATE TABLE "GeneticMapPosition_genomic_location_associations" (
	"GeneticMapPosition_curie" TEXT, 
	genomic_location_associations_id TEXT, 
	PRIMARY KEY ("GeneticMapPosition_curie", genomic_location_associations_id), 
	FOREIGN KEY("GeneticMapPosition_curie") REFERENCES "GeneticMapPosition" (curie), 
	FOREIGN KEY(genomic_location_associations_id) REFERENCES "GenomicLocationAssociation" (id)
);
CREATE TABLE "BulkLoad_load_files" (
	"BulkLoad_id" TEXT, 
	load_files_id TEXT, 
	PRIMARY KEY ("BulkLoad_id", load_files_id), 
	FOREIGN KEY("BulkLoad_id") REFERENCES "BulkLoad" (id), 
	FOREIGN KEY(load_files_id) REFERENCES "BulkLoadFile" (id)
);
CREATE TABLE "BulkScheduledLoad_load_files" (
	"BulkScheduledLoad_id" TEXT, 
	load_files_id TEXT, 
	PRIMARY KEY ("BulkScheduledLoad_id", load_files_id), 
	FOREIGN KEY("BulkScheduledLoad_id") REFERENCES "BulkScheduledLoad" (id), 
	FOREIGN KEY(load_files_id) REFERENCES "BulkLoadFile" (id)
);
CREATE TABLE "BulkFMSLoad_load_files" (
	"BulkFMSLoad_id" TEXT, 
	load_files_id TEXT, 
	PRIMARY KEY ("BulkFMSLoad_id", load_files_id), 
	FOREIGN KEY("BulkFMSLoad_id") REFERENCES "BulkFMSLoad" (id), 
	FOREIGN KEY(load_files_id) REFERENCES "BulkLoadFile" (id)
);
CREATE TABLE "BulkURLLoad_load_files" (
	"BulkURLLoad_id" TEXT, 
	load_files_id TEXT, 
	PRIMARY KEY ("BulkURLLoad_id", load_files_id), 
	FOREIGN KEY("BulkURLLoad_id") REFERENCES "BulkURLLoad" (id), 
	FOREIGN KEY(load_files_id) REFERENCES "BulkLoadFile" (id)
);
CREATE TABLE "BulkManualLoad_load_files" (
	"BulkManualLoad_id" TEXT, 
	load_files_id TEXT, 
	PRIMARY KEY ("BulkManualLoad_id", load_files_id), 
	FOREIGN KEY("BulkManualLoad_id") REFERENCES "BulkManualLoad" (id), 
	FOREIGN KEY(load_files_id) REFERENCES "BulkLoadFile" (id)
);
CREATE TABLE "GeneCluster_genes" (
	"GeneCluster_curie" TEXT, 
	genes TEXT, 
	PRIMARY KEY ("GeneCluster_curie", genes), 
	FOREIGN KEY("GeneCluster_curie") REFERENCES "GeneCluster" (curie), 
	FOREIGN KEY(genes) REFERENCES "Gene" (curie)
);
CREATE TABLE "GeneCollection_genes" (
	"GeneCollection_curie" TEXT, 
	genes TEXT, 
	PRIMARY KEY ("GeneCollection_curie", genes), 
	FOREIGN KEY("GeneCollection_curie") REFERENCES "GeneCollection" (curie), 
	FOREIGN KEY(genes) REFERENCES "Gene" (curie)
);
CREATE TABLE "GeneCollection_experiment_type" (
	"GeneCollection_curie" TEXT, 
	experiment_type TEXT, 
	PRIMARY KEY ("GeneCollection_curie", experiment_type), 
	FOREIGN KEY("GeneCollection_curie") REFERENCES "GeneCollection" (curie)
);
CREATE TABLE "GeneNomenclatureSet_genes" (
	"GeneNomenclatureSet_curie" TEXT, 
	genes TEXT, 
	PRIMARY KEY ("GeneNomenclatureSet_curie", genes), 
	FOREIGN KEY("GeneNomenclatureSet_curie") REFERENCES "GeneNomenclatureSet" (curie), 
	FOREIGN KEY(genes) REFERENCES "Gene" (curie)
);
CREATE TABLE "GeneNomenclatureSet_old_members" (
	"GeneNomenclatureSet_curie" TEXT, 
	old_members TEXT, 
	PRIMARY KEY ("GeneNomenclatureSet_curie", old_members), 
	FOREIGN KEY("GeneNomenclatureSet_curie") REFERENCES "GeneNomenclatureSet" (curie), 
	FOREIGN KEY(old_members) REFERENCES "Gene" (curie)
);
CREATE TABLE "GeneNomenclatureSet_synonyms" (
	"GeneNomenclatureSet_curie" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("GeneNomenclatureSet_curie", synonyms), 
	FOREIGN KEY("GeneNomenclatureSet_curie") REFERENCES "GeneNomenclatureSet" (curie)
);
CREATE TABLE "Operon_genes" (
	"Operon_curie" TEXT, 
	genes TEXT, 
	PRIMARY KEY ("Operon_curie", genes), 
	FOREIGN KEY("Operon_curie") REFERENCES "Operon" (curie), 
	FOREIGN KEY(genes) REFERENCES "Gene" (curie)
);
CREATE TABLE "GeneToPathwayAssociation_evidence" (
	"GeneToPathwayAssociation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("GeneToPathwayAssociation_id", evidence), 
	FOREIGN KEY("GeneToPathwayAssociation_id") REFERENCES "GeneToPathwayAssociation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "ExpressionAnnotation" (
	id INTEGER, 
	belongs_to_expression_experiment TEXT NOT NULL, 
	expression_qualifiers VARCHAR(21), 
	negated BOOLEAN, 
	uncertain BOOLEAN, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	when_expressed_id TEXT, 
	where_expressed_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(belongs_to_expression_experiment) REFERENCES "ExpressionExperiment" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(when_expressed_id) REFERENCES "TemporalContext" (id), 
	FOREIGN KEY(where_expressed_id) REFERENCES "AnatomicalSite" (id)
);
CREATE TABLE "Allele_allele_image_associations" (
	"Allele_curie" TEXT, 
	allele_image_associations_id TEXT, 
	PRIMARY KEY ("Allele_curie", allele_image_associations_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(allele_image_associations_id) REFERENCES "AlleleImageAssociation" (id)
);
CREATE TABLE "Allele_allele_origin_associations" (
	"Allele_curie" TEXT, 
	allele_origin_associations_id TEXT, 
	PRIMARY KEY ("Allele_curie", allele_origin_associations_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(allele_origin_associations_id) REFERENCES "AlleleOriginAssociation" (id)
);
CREATE TABLE "Allele_allele_generation_method_associations" (
	"Allele_curie" TEXT, 
	allele_generation_method_associations_id TEXT, 
	PRIMARY KEY ("Allele_curie", allele_generation_method_associations_id), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie), 
	FOREIGN KEY(allele_generation_method_associations_id) REFERENCES "AlleleGenerationMethodAssociation" (id)
);
CREATE TABLE "AlleleGenerationMethodAssociation_evidence" (
	"AlleleGenerationMethodAssociation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AlleleGenerationMethodAssociation_id", evidence), 
	FOREIGN KEY("AlleleGenerationMethodAssociation_id") REFERENCES "AlleleGenerationMethodAssociation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "AlleleImageAssociation_evidence" (
	"AlleleImageAssociation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AlleleImageAssociation_id", evidence), 
	FOREIGN KEY("AlleleImageAssociation_id") REFERENCES "AlleleImageAssociation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "AlleleOriginAssociation_evidence" (
	"AlleleOriginAssociation_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AlleleOriginAssociation_id", evidence), 
	FOREIGN KEY("AlleleOriginAssociation_id") REFERENCES "AlleleOriginAssociation" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "GenePhenotypeAnnotation_condition_relations" (
	"GenePhenotypeAnnotation_curie" TEXT, 
	condition_relations_id TEXT, 
	PRIMARY KEY ("GenePhenotypeAnnotation_curie", condition_relations_id), 
	FOREIGN KEY("GenePhenotypeAnnotation_curie") REFERENCES "GenePhenotypeAnnotation" (curie), 
	FOREIGN KEY(condition_relations_id) REFERENCES "ConditionRelation" (id)
);
CREATE TABLE "GenePhenotypeAnnotation_evidence" (
	"GenePhenotypeAnnotation_curie" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("GenePhenotypeAnnotation_curie", evidence), 
	FOREIGN KEY("GenePhenotypeAnnotation_curie") REFERENCES "GenePhenotypeAnnotation" (curie), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "AGMPhenotypeAnnotation_asserted_gene" (
	"AGMPhenotypeAnnotation_curie" TEXT, 
	asserted_gene TEXT, 
	PRIMARY KEY ("AGMPhenotypeAnnotation_curie", asserted_gene), 
	FOREIGN KEY("AGMPhenotypeAnnotation_curie") REFERENCES "AGMPhenotypeAnnotation" (curie), 
	FOREIGN KEY(asserted_gene) REFERENCES "Gene" (curie)
);
CREATE TABLE "AGMPhenotypeAnnotation_condition_relations" (
	"AGMPhenotypeAnnotation_curie" TEXT, 
	condition_relations_id TEXT, 
	PRIMARY KEY ("AGMPhenotypeAnnotation_curie", condition_relations_id), 
	FOREIGN KEY("AGMPhenotypeAnnotation_curie") REFERENCES "AGMPhenotypeAnnotation" (curie), 
	FOREIGN KEY(condition_relations_id) REFERENCES "ConditionRelation" (id)
);
CREATE TABLE "AGMPhenotypeAnnotation_evidence" (
	"AGMPhenotypeAnnotation_curie" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AGMPhenotypeAnnotation_curie", evidence), 
	FOREIGN KEY("AGMPhenotypeAnnotation_curie") REFERENCES "AGMPhenotypeAnnotation" (curie), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "GeneDiseaseAnnotation_evidence_codes" (
	"GeneDiseaseAnnotation_curie" TEXT, 
	evidence_codes TEXT NOT NULL, 
	PRIMARY KEY ("GeneDiseaseAnnotation_curie", evidence_codes), 
	FOREIGN KEY("GeneDiseaseAnnotation_curie") REFERENCES "GeneDiseaseAnnotation" (curie), 
	FOREIGN KEY(evidence_codes) REFERENCES "ECOTerm" (curie)
);
CREATE TABLE "GeneDiseaseAnnotation_with_or_from" (
	"GeneDiseaseAnnotation_curie" TEXT, 
	with_or_from TEXT, 
	PRIMARY KEY ("GeneDiseaseAnnotation_curie", with_or_from), 
	FOREIGN KEY("GeneDiseaseAnnotation_curie") REFERENCES "GeneDiseaseAnnotation" (curie), 
	FOREIGN KEY(with_or_from) REFERENCES "Gene" (curie)
);
CREATE TABLE "GeneDiseaseAnnotation_disease_qualifiers" (
	"GeneDiseaseAnnotation_curie" TEXT, 
	disease_qualifiers TEXT, 
	PRIMARY KEY ("GeneDiseaseAnnotation_curie", disease_qualifiers), 
	FOREIGN KEY("GeneDiseaseAnnotation_curie") REFERENCES "GeneDiseaseAnnotation" (curie), 
	FOREIGN KEY(disease_qualifiers) REFERENCES "VocabularyTerm" (name)
);
CREATE TABLE "GeneDiseaseAnnotation_condition_relations" (
	"GeneDiseaseAnnotation_curie" TEXT, 
	condition_relations_id TEXT, 
	PRIMARY KEY ("GeneDiseaseAnnotation_curie", condition_relations_id), 
	FOREIGN KEY("GeneDiseaseAnnotation_curie") REFERENCES "GeneDiseaseAnnotation" (curie), 
	FOREIGN KEY(condition_relations_id) REFERENCES "ConditionRelation" (id)
);
CREATE TABLE "GeneDiseaseAnnotation_related_notes" (
	"GeneDiseaseAnnotation_curie" TEXT, 
	related_notes_id TEXT, 
	PRIMARY KEY ("GeneDiseaseAnnotation_curie", related_notes_id), 
	FOREIGN KEY("GeneDiseaseAnnotation_curie") REFERENCES "GeneDiseaseAnnotation" (curie), 
	FOREIGN KEY(related_notes_id) REFERENCES "Note" (id)
);
CREATE TABLE "GeneDiseaseAnnotation_evidence" (
	"GeneDiseaseAnnotation_curie" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("GeneDiseaseAnnotation_curie", evidence), 
	FOREIGN KEY("GeneDiseaseAnnotation_curie") REFERENCES "GeneDiseaseAnnotation" (curie), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "AGMDiseaseAnnotation_asserted_gene" (
	"AGMDiseaseAnnotation_curie" TEXT, 
	asserted_gene TEXT, 
	PRIMARY KEY ("AGMDiseaseAnnotation_curie", asserted_gene), 
	FOREIGN KEY("AGMDiseaseAnnotation_curie") REFERENCES "AGMDiseaseAnnotation" (curie), 
	FOREIGN KEY(asserted_gene) REFERENCES "Gene" (curie)
);
CREATE TABLE "AGMDiseaseAnnotation_evidence_codes" (
	"AGMDiseaseAnnotation_curie" TEXT, 
	evidence_codes TEXT NOT NULL, 
	PRIMARY KEY ("AGMDiseaseAnnotation_curie", evidence_codes), 
	FOREIGN KEY("AGMDiseaseAnnotation_curie") REFERENCES "AGMDiseaseAnnotation" (curie), 
	FOREIGN KEY(evidence_codes) REFERENCES "ECOTerm" (curie)
);
CREATE TABLE "AGMDiseaseAnnotation_with_or_from" (
	"AGMDiseaseAnnotation_curie" TEXT, 
	with_or_from TEXT, 
	PRIMARY KEY ("AGMDiseaseAnnotation_curie", with_or_from), 
	FOREIGN KEY("AGMDiseaseAnnotation_curie") REFERENCES "AGMDiseaseAnnotation" (curie), 
	FOREIGN KEY(with_or_from) REFERENCES "Gene" (curie)
);
CREATE TABLE "AGMDiseaseAnnotation_disease_qualifiers" (
	"AGMDiseaseAnnotation_curie" TEXT, 
	disease_qualifiers TEXT, 
	PRIMARY KEY ("AGMDiseaseAnnotation_curie", disease_qualifiers), 
	FOREIGN KEY("AGMDiseaseAnnotation_curie") REFERENCES "AGMDiseaseAnnotation" (curie), 
	FOREIGN KEY(disease_qualifiers) REFERENCES "VocabularyTerm" (name)
);
CREATE TABLE "AGMDiseaseAnnotation_condition_relations" (
	"AGMDiseaseAnnotation_curie" TEXT, 
	condition_relations_id TEXT, 
	PRIMARY KEY ("AGMDiseaseAnnotation_curie", condition_relations_id), 
	FOREIGN KEY("AGMDiseaseAnnotation_curie") REFERENCES "AGMDiseaseAnnotation" (curie), 
	FOREIGN KEY(condition_relations_id) REFERENCES "ConditionRelation" (id)
);
CREATE TABLE "AGMDiseaseAnnotation_related_notes" (
	"AGMDiseaseAnnotation_curie" TEXT, 
	related_notes_id TEXT, 
	PRIMARY KEY ("AGMDiseaseAnnotation_curie", related_notes_id), 
	FOREIGN KEY("AGMDiseaseAnnotation_curie") REFERENCES "AGMDiseaseAnnotation" (curie), 
	FOREIGN KEY(related_notes_id) REFERENCES "Note" (id)
);
CREATE TABLE "AGMDiseaseAnnotation_evidence" (
	"AGMDiseaseAnnotation_curie" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("AGMDiseaseAnnotation_curie", evidence), 
	FOREIGN KEY("AGMDiseaseAnnotation_curie") REFERENCES "AGMDiseaseAnnotation" (curie), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
CREATE TABLE "ExpressionExperiment_reagents_used" (
	"ExpressionExperiment_curie" TEXT, 
	reagents_used TEXT, 
	PRIMARY KEY ("ExpressionExperiment_curie", reagents_used), 
	FOREIGN KEY("ExpressionExperiment_curie") REFERENCES "ExpressionExperiment" (curie), 
	FOREIGN KEY(reagents_used) REFERENCES "Reagent" (curie)
);
CREATE TABLE "ExpressionExperiment_specimen_alleles" (
	"ExpressionExperiment_curie" TEXT, 
	specimen_alleles TEXT, 
	PRIMARY KEY ("ExpressionExperiment_curie", specimen_alleles), 
	FOREIGN KEY("ExpressionExperiment_curie") REFERENCES "ExpressionExperiment" (curie), 
	FOREIGN KEY(specimen_alleles) REFERENCES "Allele" (curie)
);
CREATE TABLE "ExpressionExperiment_condition_relations" (
	"ExpressionExperiment_curie" TEXT, 
	condition_relations_id TEXT, 
	PRIMARY KEY ("ExpressionExperiment_curie", condition_relations_id), 
	FOREIGN KEY("ExpressionExperiment_curie") REFERENCES "ExpressionExperiment" (curie), 
	FOREIGN KEY(condition_relations_id) REFERENCES "ConditionRelation" (id)
);
CREATE TABLE "ExpressionExperiment_related_notes" (
	"ExpressionExperiment_curie" TEXT, 
	related_notes_id TEXT, 
	PRIMARY KEY ("ExpressionExperiment_curie", related_notes_id), 
	FOREIGN KEY("ExpressionExperiment_curie") REFERENCES "ExpressionExperiment" (curie), 
	FOREIGN KEY(related_notes_id) REFERENCES "Note" (id)
);
CREATE TABLE "ExpressionAnnotationImagePane" (
	id INTEGER, 
	predicate TEXT NOT NULL, 
	created_by TEXT, 
	date_created DATETIME, 
	updated_by TEXT, 
	date_updated DATETIME, 
	db_date_created DATETIME, 
	db_date_updated DATETIME, 
	internal BOOLEAN NOT NULL, 
	obsolete BOOLEAN, 
	subject_id TEXT NOT NULL, 
	object_id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(created_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(updated_by) REFERENCES "Person" (unique_id), 
	FOREIGN KEY(subject_id) REFERENCES "ExpressionAnnotation" (id), 
	FOREIGN KEY(object_id) REFERENCES "ImagePane" (id)
);
CREATE TABLE "ExpressionAnnotation_associated_with_figure" (
	"ExpressionAnnotation_id" TEXT, 
	associated_with_figure TEXT, 
	PRIMARY KEY ("ExpressionAnnotation_id", associated_with_figure), 
	FOREIGN KEY("ExpressionAnnotation_id") REFERENCES "ExpressionAnnotation" (id), 
	FOREIGN KEY(associated_with_figure) REFERENCES "Figure" (curie)
);
CREATE TABLE "ExpressionAnnotation_related_notes" (
	"ExpressionAnnotation_id" TEXT, 
	related_notes_id TEXT, 
	PRIMARY KEY ("ExpressionAnnotation_id", related_notes_id), 
	FOREIGN KEY("ExpressionAnnotation_id") REFERENCES "ExpressionAnnotation" (id), 
	FOREIGN KEY(related_notes_id) REFERENCES "Note" (id)
);
CREATE TABLE "ExpressionAnnotationImagePane_evidence" (
	"ExpressionAnnotationImagePane_id" TEXT, 
	evidence TEXT, 
	PRIMARY KEY ("ExpressionAnnotationImagePane_id", evidence), 
	FOREIGN KEY("ExpressionAnnotationImagePane_id") REFERENCES "ExpressionAnnotationImagePane" (id), 
	FOREIGN KEY(evidence) REFERENCES "InformationContentEntity" (curie)
);
