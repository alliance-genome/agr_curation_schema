

CREATE TABLE "AntibodyNote" (
	statement_subject TEXT, 
	statement_type TEXT, 
	statement_text TEXT, 
	"references" TEXT, 
	note_type VARCHAR(20), 
	PRIMARY KEY (statement_subject, statement_type, statement_text, "references", note_type)
);

CREATE TABLE "Assembly" (
	curie TEXT NOT NULL, 
	PRIMARY KEY (curie)
);

CREATE TABLE "Association" (
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (subject, predicate, object)
);

CREATE TABLE "AuthorReference" (
	corresponding_author TEXT, 
	first_name TEXT, 
	middle_names TEXT, 
	last_name TEXT, 
	initials TEXT, 
	cross_references TEXT, 
	PRIMARY KEY (corresponding_author, first_name, middle_names, last_name, initials, cross_references)
);

CREATE TABLE "CHEBITerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	is_obsolete BOOLEAN, 
	cross_references TEXT, 
	synonyms TEXT, 
	namespace TEXT, 
	PRIMARY KEY (curie)
);

CREATE TABLE "Chromosome" (
	curie TEXT NOT NULL, 
	PRIMARY KEY (curie)
);

CREATE TABLE "CLTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	is_obsolete BOOLEAN, 
	cross_references TEXT, 
	synonyms TEXT, 
	namespace TEXT, 
	PRIMARY KEY (curie)
);

CREATE TABLE "ConditionRelation" (
	curie TEXT NOT NULL, 
	condition_relation_type VARCHAR(18) NOT NULL, 
	PRIMARY KEY (curie)
);

CREATE TABLE "DOTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	is_obsolete BOOLEAN, 
	cross_references TEXT, 
	synonyms TEXT, 
	namespace TEXT, 
	PRIMARY KEY (curie)
);

CREATE TABLE "ECOTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	is_obsolete BOOLEAN, 
	cross_references TEXT, 
	synonyms TEXT, 
	namespace TEXT, 
	PRIMARY KEY (curie)
);

CREATE TABLE "EMAPATerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	is_obsolete BOOLEAN, 
	cross_references TEXT, 
	synonyms TEXT, 
	namespace TEXT, 
	PRIMARY KEY (curie)
);

CREATE TABLE "EntityStatement" (
	statement_subject TEXT, 
	statement_type TEXT, 
	statement_text TEXT, 
	"references" TEXT, 
	PRIMARY KEY (statement_subject, statement_type, statement_text, "references")
);

CREATE TABLE "EntitySynonym" (
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	predicate VARCHAR(7) NOT NULL, 
	"references" TEXT, 
	PRIMARY KEY (subject, object, predicate, "references")
);

CREATE TABLE "ExternalDatabaseLink" (
	dbkey TEXT, 
	prefix TEXT NOT NULL, 
	url_prefix TEXT, 
	url_suffix TEXT, 
	prefix_page TEXT, 
	prefix_order TEXT, 
	PRIMARY KEY (dbkey, prefix, url_prefix, url_suffix, prefix_page, prefix_order)
);

CREATE TABLE "FBBTTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	is_obsolete BOOLEAN, 
	cross_references TEXT, 
	synonyms TEXT, 
	namespace TEXT, 
	PRIMARY KEY (curie)
);

CREATE TABLE "FBCVTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	is_obsolete BOOLEAN, 
	cross_references TEXT, 
	synonyms TEXT, 
	namespace TEXT, 
	PRIMARY KEY (curie)
);

CREATE TABLE "FBDVTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	is_obsolete BOOLEAN, 
	cross_references TEXT, 
	synonyms TEXT, 
	namespace TEXT, 
	PRIMARY KEY (curie)
);

CREATE TABLE "GOTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	is_obsolete BOOLEAN, 
	cross_references TEXT, 
	synonyms TEXT, 
	namespace TEXT, 
	PRIMARY KEY (curie)
);

CREATE TABLE "MATerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	is_obsolete BOOLEAN, 
	cross_references TEXT, 
	synonyms TEXT, 
	namespace TEXT, 
	PRIMARY KEY (curie)
);

CREATE TABLE "MITerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	is_obsolete BOOLEAN, 
	cross_references TEXT, 
	synonyms TEXT, 
	namespace TEXT, 
	PRIMARY KEY (curie)
);

CREATE TABLE "MMOTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	is_obsolete BOOLEAN, 
	cross_references TEXT, 
	synonyms TEXT, 
	namespace TEXT, 
	PRIMARY KEY (curie)
);

CREATE TABLE "MMUSDVTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	is_obsolete BOOLEAN, 
	cross_references TEXT, 
	synonyms TEXT, 
	namespace TEXT, 
	PRIMARY KEY (curie)
);

CREATE TABLE "NoteType" (
	note_association VARCHAR(16), 
	notes TEXT, 
	PRIMARY KEY (note_association, notes)
);

CREATE TABLE "OntologyTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	is_obsolete BOOLEAN, 
	cross_references TEXT, 
	synonyms TEXT, 
	namespace TEXT, 
	PRIMARY KEY (curie)
);

CREATE TABLE "Person" (
	last_name TEXT, 
	first_name TEXT, 
	orcid TEXT, 
	person_id TEXT NOT NULL, 
	PRIMARY KEY (person_id)
);

CREATE TABLE "PhenotypeTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	is_obsolete BOOLEAN, 
	cross_references TEXT, 
	synonyms TEXT, 
	namespace TEXT, 
	PRIMARY KEY (curie)
);

CREATE TABLE "SOTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	is_obsolete BOOLEAN, 
	cross_references TEXT, 
	synonyms TEXT, 
	namespace TEXT, 
	PRIMARY KEY (curie)
);

CREATE TABLE "UBERONTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	is_obsolete BOOLEAN, 
	cross_references TEXT, 
	synonyms TEXT, 
	namespace TEXT, 
	PRIMARY KEY (curie)
);

CREATE TABLE "WBBTTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	is_obsolete BOOLEAN, 
	cross_references TEXT, 
	synonyms TEXT, 
	namespace TEXT, 
	PRIMARY KEY (curie)
);

CREATE TABLE "WBLSTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	is_obsolete BOOLEAN, 
	cross_references TEXT, 
	synonyms TEXT, 
	namespace TEXT, 
	PRIMARY KEY (curie)
);

CREATE TABLE "XCOTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	is_obsolete BOOLEAN, 
	cross_references TEXT, 
	synonyms TEXT, 
	namespace TEXT, 
	PRIMARY KEY (curie)
);

CREATE TABLE "ZECOTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	is_obsolete BOOLEAN, 
	cross_references TEXT, 
	synonyms TEXT, 
	namespace TEXT, 
	PRIMARY KEY (curie)
);

CREATE TABLE "ZFATerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	is_obsolete BOOLEAN, 
	cross_references TEXT, 
	synonyms TEXT, 
	namespace TEXT, 
	PRIMARY KEY (curie)
);

CREATE TABLE "ZFSTerm" (
	curie TEXT NOT NULL, 
	dbkey TEXT, 
	name TEXT, 
	definition TEXT, 
	type TEXT, 
	is_obsolete BOOLEAN, 
	cross_references TEXT, 
	synonyms TEXT, 
	namespace TEXT, 
	PRIMARY KEY (curie)
);

CREATE TABLE "AffectedGenomicModel" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	table_key INTEGER, 
	created_by TEXT NOT NULL, 
	creation_date DATE, 
	modified_by TEXT NOT NULL, 
	date_last_modified DATE, 
	name TEXT, 
	synonyms TEXT, 
	cross_references TEXT, 
	subtype VARCHAR(8), 
	parental_populations TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (person_id)
);

CREATE TABLE "Construct" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	table_key INTEGER, 
	created_by TEXT NOT NULL, 
	creation_date DATE, 
	modified_by TEXT NOT NULL, 
	date_last_modified DATE, 
	name TEXT, 
	synonyms TEXT, 
	cross_references TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (person_id)
);

CREATE TABLE "CrossReference" (
	curie TEXT NOT NULL, 
	table_key INTEGER, 
	created_by TEXT NOT NULL, 
	creation_date DATE, 
	modified_by TEXT NOT NULL, 
	date_last_modified DATE, 
	display_name TEXT NOT NULL, 
	prefix TEXT NOT NULL, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (person_id)
);

CREATE TABLE "ExperimentalCondition" (
	curie TEXT NOT NULL, 
	condition_class TEXT NOT NULL, 
	condition_statement TEXT NOT NULL, 
	condition_id TEXT, 
	condition_quantity TEXT, 
	condition_anatomy TEXT, 
	condition_gene_ontology TEXT, 
	condition_taxon TEXT, 
	condition_chemical TEXT, 
	"ConditionRelation_curie" TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(condition_class) REFERENCES "ZECOTerm" (curie), 
	FOREIGN KEY(condition_gene_ontology) REFERENCES "GOTerm" (curie), 
	FOREIGN KEY(condition_taxon) REFERENCES "OntologyTerm" (curie), 
	FOREIGN KEY(condition_chemical) REFERENCES "OntologyTerm" (curie), 
	FOREIGN KEY("ConditionRelation_curie") REFERENCES "ConditionRelation" (curie)
);

CREATE TABLE "Gene" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	table_key INTEGER, 
	created_by TEXT NOT NULL, 
	creation_date DATE, 
	modified_by TEXT NOT NULL, 
	date_last_modified DATE, 
	name TEXT, 
	synonyms TEXT, 
	cross_references TEXT, 
	symbol TEXT NOT NULL, 
	gene_synopsis TEXT, 
	"gene_synopsis_URL" TEXT, 
	type TEXT, 
	automated_gene_description TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (person_id)
);

CREATE TABLE "GenomicEntity" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	table_key INTEGER, 
	created_by TEXT NOT NULL, 
	creation_date DATE, 
	modified_by TEXT NOT NULL, 
	date_last_modified DATE, 
	name TEXT, 
	synonyms TEXT, 
	cross_references TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (person_id)
);

CREATE TABLE "MolecularMutation" (
	mutation_type TEXT NOT NULL, 
	mutation_description TEXT, 
	PRIMARY KEY (mutation_type, mutation_description), 
	FOREIGN KEY(mutation_type) REFERENCES "SOTerm" (curie)
);

CREATE TABLE "Molecule" (
	curie TEXT NOT NULL, 
	name TEXT, 
	inchi TEXT, 
	inchi_key TEXT, 
	iupac TEXT, 
	formula TEXT, 
	smiles TEXT, 
	synonyms TEXT, 
	cross_references TEXT, 
	table_key INTEGER, 
	created_by TEXT NOT NULL, 
	creation_date DATE, 
	modified_by TEXT NOT NULL, 
	date_last_modified DATE, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (person_id)
);

CREATE TABLE "Resource" (
	curie TEXT NOT NULL, 
	table_key INTEGER, 
	created_by TEXT NOT NULL, 
	creation_date DATE, 
	modified_by TEXT NOT NULL, 
	date_last_modified DATE, 
	title TEXT, 
	iso_abbreviation TEXT, 
	medline_abbreviation TEXT, 
	copyright_date DATE, 
	print_issn TEXT, 
	online_issn TEXT, 
	publisher TEXT, 
	volumes TEXT, 
	summary TEXT, 
	synonyms TEXT, 
	authors TEXT, 
	editors TEXT, 
	id TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (person_id)
);

CREATE TABLE "Transcript" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	table_key INTEGER, 
	created_by TEXT NOT NULL, 
	creation_date DATE, 
	modified_by TEXT NOT NULL, 
	date_last_modified DATE, 
	name TEXT, 
	synonyms TEXT, 
	cross_references TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (person_id)
);

CREATE TABLE "Vocabulary" (
	name TEXT NOT NULL, 
	vocabulary_description TEXT, 
	is_obsolete BOOLEAN, 
	member_terms TEXT, 
	table_key INTEGER, 
	created_by TEXT NOT NULL, 
	creation_date DATE, 
	modified_by TEXT NOT NULL, 
	date_last_modified DATE, 
	PRIMARY KEY (name, vocabulary_description, is_obsolete, member_terms, table_key, created_by, creation_date, modified_by, date_last_modified), 
	FOREIGN KEY(created_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (person_id)
);

CREATE TABLE "VocabularyTerm" (
	name TEXT NOT NULL, 
	definition TEXT, 
	is_obsolete BOOLEAN, 
	text_synonyms TEXT, 
	table_key INTEGER, 
	created_by TEXT NOT NULL, 
	creation_date DATE, 
	modified_by TEXT NOT NULL, 
	date_last_modified DATE, 
	PRIMARY KEY (name, definition, is_obsolete, text_synonyms, table_key, created_by, creation_date, modified_by, date_last_modified), 
	FOREIGN KEY(created_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (person_id)
);

CREATE TABLE "CHEBITerm_definition_urls" (
	backref_id TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY (backref_id, definition_urls), 
	FOREIGN KEY(backref_id) REFERENCES "CHEBITerm" (curie)
);

CREATE TABLE "CHEBITerm_subsets" (
	backref_id TEXT, 
	subsets TEXT, 
	PRIMARY KEY (backref_id, subsets), 
	FOREIGN KEY(backref_id) REFERENCES "CHEBITerm" (curie)
);

CREATE TABLE "CHEBITerm_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "CHEBITerm" (curie)
);

CREATE TABLE "CLTerm_definition_urls" (
	backref_id TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY (backref_id, definition_urls), 
	FOREIGN KEY(backref_id) REFERENCES "CLTerm" (curie)
);

CREATE TABLE "CLTerm_subsets" (
	backref_id TEXT, 
	subsets TEXT, 
	PRIMARY KEY (backref_id, subsets), 
	FOREIGN KEY(backref_id) REFERENCES "CLTerm" (curie)
);

CREATE TABLE "CLTerm_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "CLTerm" (curie)
);

CREATE TABLE "DOTerm_definition_urls" (
	backref_id TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY (backref_id, definition_urls), 
	FOREIGN KEY(backref_id) REFERENCES "DOTerm" (curie)
);

CREATE TABLE "DOTerm_subsets" (
	backref_id TEXT, 
	subsets TEXT, 
	PRIMARY KEY (backref_id, subsets), 
	FOREIGN KEY(backref_id) REFERENCES "DOTerm" (curie)
);

CREATE TABLE "DOTerm_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "DOTerm" (curie)
);

CREATE TABLE "ECOTerm_definition_urls" (
	backref_id TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY (backref_id, definition_urls), 
	FOREIGN KEY(backref_id) REFERENCES "ECOTerm" (curie)
);

CREATE TABLE "ECOTerm_subsets" (
	backref_id TEXT, 
	subsets TEXT, 
	PRIMARY KEY (backref_id, subsets), 
	FOREIGN KEY(backref_id) REFERENCES "ECOTerm" (curie)
);

CREATE TABLE "ECOTerm_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "ECOTerm" (curie)
);

CREATE TABLE "EMAPATerm_definition_urls" (
	backref_id TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY (backref_id, definition_urls), 
	FOREIGN KEY(backref_id) REFERENCES "EMAPATerm" (curie)
);

CREATE TABLE "EMAPATerm_subsets" (
	backref_id TEXT, 
	subsets TEXT, 
	PRIMARY KEY (backref_id, subsets), 
	FOREIGN KEY(backref_id) REFERENCES "EMAPATerm" (curie)
);

CREATE TABLE "EMAPATerm_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "EMAPATerm" (curie)
);

CREATE TABLE "FBBTTerm_definition_urls" (
	backref_id TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY (backref_id, definition_urls), 
	FOREIGN KEY(backref_id) REFERENCES "FBBTTerm" (curie)
);

CREATE TABLE "FBBTTerm_subsets" (
	backref_id TEXT, 
	subsets TEXT, 
	PRIMARY KEY (backref_id, subsets), 
	FOREIGN KEY(backref_id) REFERENCES "FBBTTerm" (curie)
);

CREATE TABLE "FBBTTerm_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "FBBTTerm" (curie)
);

CREATE TABLE "FBCVTerm_definition_urls" (
	backref_id TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY (backref_id, definition_urls), 
	FOREIGN KEY(backref_id) REFERENCES "FBCVTerm" (curie)
);

CREATE TABLE "FBCVTerm_subsets" (
	backref_id TEXT, 
	subsets TEXT, 
	PRIMARY KEY (backref_id, subsets), 
	FOREIGN KEY(backref_id) REFERENCES "FBCVTerm" (curie)
);

CREATE TABLE "FBCVTerm_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "FBCVTerm" (curie)
);

CREATE TABLE "FBDVTerm_definition_urls" (
	backref_id TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY (backref_id, definition_urls), 
	FOREIGN KEY(backref_id) REFERENCES "FBDVTerm" (curie)
);

CREATE TABLE "FBDVTerm_subsets" (
	backref_id TEXT, 
	subsets TEXT, 
	PRIMARY KEY (backref_id, subsets), 
	FOREIGN KEY(backref_id) REFERENCES "FBDVTerm" (curie)
);

CREATE TABLE "FBDVTerm_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "FBDVTerm" (curie)
);

CREATE TABLE "GOTerm_definition_urls" (
	backref_id TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY (backref_id, definition_urls), 
	FOREIGN KEY(backref_id) REFERENCES "GOTerm" (curie)
);

CREATE TABLE "GOTerm_subsets" (
	backref_id TEXT, 
	subsets TEXT, 
	PRIMARY KEY (backref_id, subsets), 
	FOREIGN KEY(backref_id) REFERENCES "GOTerm" (curie)
);

CREATE TABLE "GOTerm_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "GOTerm" (curie)
);

CREATE TABLE "MATerm_definition_urls" (
	backref_id TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY (backref_id, definition_urls), 
	FOREIGN KEY(backref_id) REFERENCES "MATerm" (curie)
);

CREATE TABLE "MATerm_subsets" (
	backref_id TEXT, 
	subsets TEXT, 
	PRIMARY KEY (backref_id, subsets), 
	FOREIGN KEY(backref_id) REFERENCES "MATerm" (curie)
);

CREATE TABLE "MATerm_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "MATerm" (curie)
);

CREATE TABLE "MITerm_definition_urls" (
	backref_id TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY (backref_id, definition_urls), 
	FOREIGN KEY(backref_id) REFERENCES "MITerm" (curie)
);

CREATE TABLE "MITerm_subsets" (
	backref_id TEXT, 
	subsets TEXT, 
	PRIMARY KEY (backref_id, subsets), 
	FOREIGN KEY(backref_id) REFERENCES "MITerm" (curie)
);

CREATE TABLE "MITerm_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "MITerm" (curie)
);

CREATE TABLE "MMOTerm_definition_urls" (
	backref_id TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY (backref_id, definition_urls), 
	FOREIGN KEY(backref_id) REFERENCES "MMOTerm" (curie)
);

CREATE TABLE "MMOTerm_subsets" (
	backref_id TEXT, 
	subsets TEXT, 
	PRIMARY KEY (backref_id, subsets), 
	FOREIGN KEY(backref_id) REFERENCES "MMOTerm" (curie)
);

CREATE TABLE "MMOTerm_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "MMOTerm" (curie)
);

CREATE TABLE "MMUSDVTerm_definition_urls" (
	backref_id TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY (backref_id, definition_urls), 
	FOREIGN KEY(backref_id) REFERENCES "MMUSDVTerm" (curie)
);

CREATE TABLE "MMUSDVTerm_subsets" (
	backref_id TEXT, 
	subsets TEXT, 
	PRIMARY KEY (backref_id, subsets), 
	FOREIGN KEY(backref_id) REFERENCES "MMUSDVTerm" (curie)
);

CREATE TABLE "MMUSDVTerm_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "MMUSDVTerm" (curie)
);

CREATE TABLE "OntologyTerm_definition_urls" (
	backref_id TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY (backref_id, definition_urls), 
	FOREIGN KEY(backref_id) REFERENCES "OntologyTerm" (curie)
);

CREATE TABLE "OntologyTerm_subsets" (
	backref_id TEXT, 
	subsets TEXT, 
	PRIMARY KEY (backref_id, subsets), 
	FOREIGN KEY(backref_id) REFERENCES "OntologyTerm" (curie)
);

CREATE TABLE "OntologyTerm_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "OntologyTerm" (curie)
);

CREATE TABLE "PhenotypeTerm_definition_urls" (
	backref_id TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY (backref_id, definition_urls), 
	FOREIGN KEY(backref_id) REFERENCES "PhenotypeTerm" (curie)
);

CREATE TABLE "PhenotypeTerm_subsets" (
	backref_id TEXT, 
	subsets TEXT, 
	PRIMARY KEY (backref_id, subsets), 
	FOREIGN KEY(backref_id) REFERENCES "PhenotypeTerm" (curie)
);

CREATE TABLE "PhenotypeTerm_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "PhenotypeTerm" (curie)
);

CREATE TABLE "SOTerm_definition_urls" (
	backref_id TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY (backref_id, definition_urls), 
	FOREIGN KEY(backref_id) REFERENCES "SOTerm" (curie)
);

CREATE TABLE "SOTerm_subsets" (
	backref_id TEXT, 
	subsets TEXT, 
	PRIMARY KEY (backref_id, subsets), 
	FOREIGN KEY(backref_id) REFERENCES "SOTerm" (curie)
);

CREATE TABLE "SOTerm_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "SOTerm" (curie)
);

CREATE TABLE "UBERONTerm_definition_urls" (
	backref_id TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY (backref_id, definition_urls), 
	FOREIGN KEY(backref_id) REFERENCES "UBERONTerm" (curie)
);

CREATE TABLE "UBERONTerm_subsets" (
	backref_id TEXT, 
	subsets TEXT, 
	PRIMARY KEY (backref_id, subsets), 
	FOREIGN KEY(backref_id) REFERENCES "UBERONTerm" (curie)
);

CREATE TABLE "UBERONTerm_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "UBERONTerm" (curie)
);

CREATE TABLE "WBBTTerm_definition_urls" (
	backref_id TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY (backref_id, definition_urls), 
	FOREIGN KEY(backref_id) REFERENCES "WBBTTerm" (curie)
);

CREATE TABLE "WBBTTerm_subsets" (
	backref_id TEXT, 
	subsets TEXT, 
	PRIMARY KEY (backref_id, subsets), 
	FOREIGN KEY(backref_id) REFERENCES "WBBTTerm" (curie)
);

CREATE TABLE "WBBTTerm_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "WBBTTerm" (curie)
);

CREATE TABLE "WBLSTerm_definition_urls" (
	backref_id TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY (backref_id, definition_urls), 
	FOREIGN KEY(backref_id) REFERENCES "WBLSTerm" (curie)
);

CREATE TABLE "WBLSTerm_subsets" (
	backref_id TEXT, 
	subsets TEXT, 
	PRIMARY KEY (backref_id, subsets), 
	FOREIGN KEY(backref_id) REFERENCES "WBLSTerm" (curie)
);

CREATE TABLE "WBLSTerm_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "WBLSTerm" (curie)
);

CREATE TABLE "XCOTerm_definition_urls" (
	backref_id TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY (backref_id, definition_urls), 
	FOREIGN KEY(backref_id) REFERENCES "XCOTerm" (curie)
);

CREATE TABLE "XCOTerm_subsets" (
	backref_id TEXT, 
	subsets TEXT, 
	PRIMARY KEY (backref_id, subsets), 
	FOREIGN KEY(backref_id) REFERENCES "XCOTerm" (curie)
);

CREATE TABLE "XCOTerm_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "XCOTerm" (curie)
);

CREATE TABLE "ZECOTerm_definition_urls" (
	backref_id TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY (backref_id, definition_urls), 
	FOREIGN KEY(backref_id) REFERENCES "ZECOTerm" (curie)
);

CREATE TABLE "ZECOTerm_subsets" (
	backref_id TEXT, 
	subsets TEXT, 
	PRIMARY KEY (backref_id, subsets), 
	FOREIGN KEY(backref_id) REFERENCES "ZECOTerm" (curie)
);

CREATE TABLE "ZECOTerm_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "ZECOTerm" (curie)
);

CREATE TABLE "ZFATerm_definition_urls" (
	backref_id TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY (backref_id, definition_urls), 
	FOREIGN KEY(backref_id) REFERENCES "ZFATerm" (curie)
);

CREATE TABLE "ZFATerm_subsets" (
	backref_id TEXT, 
	subsets TEXT, 
	PRIMARY KEY (backref_id, subsets), 
	FOREIGN KEY(backref_id) REFERENCES "ZFATerm" (curie)
);

CREATE TABLE "ZFATerm_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "ZFATerm" (curie)
);

CREATE TABLE "ZFSTerm_definition_urls" (
	backref_id TEXT, 
	definition_urls TEXT, 
	PRIMARY KEY (backref_id, definition_urls), 
	FOREIGN KEY(backref_id) REFERENCES "ZFSTerm" (curie)
);

CREATE TABLE "ZFSTerm_subsets" (
	backref_id TEXT, 
	subsets TEXT, 
	PRIMARY KEY (backref_id, subsets), 
	FOREIGN KEY(backref_id) REFERENCES "ZFSTerm" (curie)
);

CREATE TABLE "ZFSTerm_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "ZFSTerm" (curie)
);

CREATE TABLE "ConstructComponent" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	table_key INTEGER, 
	created_by TEXT NOT NULL, 
	creation_date DATE, 
	modified_by TEXT NOT NULL, 
	date_last_modified DATE, 
	name TEXT, 
	synonyms TEXT, 
	cross_references TEXT, 
	component_relation VARCHAR(15), 
	"Construct_curie" TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY("Construct_curie") REFERENCES "Construct" (curie)
);

CREATE TABLE "Reference" (
	curie TEXT NOT NULL, 
	table_key INTEGER, 
	created_by TEXT NOT NULL, 
	creation_date DATE, 
	modified_by TEXT NOT NULL, 
	date_last_modified DATE, 
	title TEXT, 
	alliance_category TEXT, 
	date_published DATE, 
	year_published TEXT, 
	month_published TEXT, 
	day_published TEXT, 
	"date_arrived_in_PubMed" DATE, 
	"date_last_modified_in_PubMed" DATE, 
	volume TEXT, 
	abstract TEXT, 
	citation TEXT, 
	"PubMed_type" TEXT, 
	issue_name TEXT, 
	issue_date DATE, 
	authors TEXT, 
	topics TEXT, 
	cross_references TEXT, 
	publisher TEXT, 
	from_resource TEXT, 
	id TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(from_resource) REFERENCES "Resource" (curie)
);

CREATE TABLE "SequenceTargetingReagent" (
	"AffectedGenomicModel_curie" TEXT, 
	PRIMARY KEY ("AffectedGenomicModel_curie"), 
	FOREIGN KEY("AffectedGenomicModel_curie") REFERENCES "AffectedGenomicModel" (curie)
);

CREATE TABLE "AffectedGenomicModel_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "AffectedGenomicModel" (curie)
);

CREATE TABLE "AffectedGenomicModel_data_provider" (
	backref_id TEXT, 
	data_provider TEXT, 
	PRIMARY KEY (backref_id, data_provider), 
	FOREIGN KEY(backref_id) REFERENCES "AffectedGenomicModel" (curie)
);

CREATE TABLE "Construct_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "Construct" (curie)
);

CREATE TABLE "CrossReference_page_areas" (
	backref_id TEXT, 
	page_areas TEXT NOT NULL, 
	PRIMARY KEY (backref_id, page_areas), 
	FOREIGN KEY(backref_id) REFERENCES "CrossReference" (curie)
);

CREATE TABLE "Gene_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "Gene" (curie)
);

CREATE TABLE "GenomicEntity_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "GenomicEntity" (curie)
);

CREATE TABLE "Transcript_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "Transcript" (curie)
);

CREATE TABLE "Antibody" (
	table_key INTEGER, 
	created_by TEXT NOT NULL, 
	creation_date DATE, 
	modified_by TEXT NOT NULL, 
	date_last_modified DATE, 
	name TEXT NOT NULL, 
	antigen_taxon TEXT, 
	clonality VARCHAR(11) NOT NULL, 
	heavy_chain_isotype VARCHAR(5), 
	light_chain_isotype VARCHAR(2), 
	antibody_target_genes TEXT, 
	cross_references TEXT, 
	"references" TEXT, 
	original_reference TEXT, 
	curie TEXT NOT NULL, 
	taxon TEXT, 
	generated_by TEXT, 
	manufactured_by TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(original_reference) REFERENCES "Reference" (curie)
);

CREATE TABLE "Figure" (
	curie TEXT NOT NULL, 
	has_reference TEXT NOT NULL, 
	label TEXT, 
	caption TEXT, 
	table_key INTEGER, 
	created_by TEXT NOT NULL, 
	creation_date DATE, 
	modified_by TEXT NOT NULL, 
	date_last_modified DATE, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(has_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (person_id)
);

CREATE TABLE "GeneDiseaseAnnotation" (
	curie TEXT NOT NULL, 
	mod_id TEXT, 
	negated BOOLEAN, 
	evidence_codes TEXT NOT NULL, 
	annotation_reference TEXT NOT NULL, 
	annotation_type VARCHAR(16), 
	with TEXT, 
	disease_qualifiers VARCHAR(19), 
	condition_relations TEXT, 
	genetic_sex VARCHAR(13), 
	private_note TEXT, 
	disease_annotation_note TEXT, 
	disease_annotation_summary TEXT, 
	disease_genetic_modifier TEXT, 
	disease_genetic_modifier_relation VARCHAR(18), 
	object TEXT NOT NULL, 
	table_key INTEGER, 
	created_by TEXT NOT NULL, 
	creation_date DATE, 
	modified_by TEXT NOT NULL, 
	date_last_modified DATE, 
	sgd_strain_background TEXT, 
	subject TEXT NOT NULL, 
	predicate VARCHAR(16) NOT NULL, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(annotation_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(with) REFERENCES "Gene" (curie), 
	FOREIGN KEY(object) REFERENCES "DOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(sgd_strain_background) REFERENCES "AffectedGenomicModel" (curie), 
	FOREIGN KEY(subject) REFERENCES "Gene" (curie)
);

CREATE TABLE "GeneMolecularInteraction" (
	curie TEXT NOT NULL, 
	cross_references TEXT, 
	interaction_data_provider VARCHAR(7) NOT NULL, 
	interaction_type VARCHAR(7) NOT NULL, 
	"interactor_A_type" VARCHAR(7) NOT NULL, 
	"interactor_B_type" VARCHAR(7) NOT NULL, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	"references" TEXT, 
	aggregation_database VARCHAR(7), 
	detection_method VARCHAR(7), 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(subject) REFERENCES "Gene" (curie), 
	FOREIGN KEY(object) REFERENCES "Gene" (curie), 
	FOREIGN KEY("references") REFERENCES "Reference" (curie)
);

CREATE TABLE "GenePhenotypeAnnotation" (
	curie TEXT NOT NULL, 
	annotation_reference TEXT NOT NULL, 
	phenotype_term TEXT, 
	condition_relations TEXT, 
	object TEXT NOT NULL, 
	creation_date DATE NOT NULL, 
	table_key INTEGER, 
	created_by TEXT NOT NULL, 
	modified_by TEXT NOT NULL, 
	date_last_modified DATE, 
	sgd_strain_background TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(annotation_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(phenotype_term) REFERENCES "PhenotypeTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(sgd_strain_background) REFERENCES "AffectedGenomicModel" (curie), 
	FOREIGN KEY(subject) REFERENCES "Gene" (curie)
);

CREATE TABLE "PhenotypeAnnotation" (
	predicate TEXT NOT NULL, 
	curie TEXT NOT NULL, 
	annotation_reference TEXT NOT NULL, 
	phenotype_term TEXT, 
	condition_relations TEXT, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	creation_date DATE NOT NULL, 
	table_key INTEGER, 
	created_by TEXT NOT NULL, 
	modified_by TEXT NOT NULL, 
	date_last_modified DATE, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(annotation_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(phenotype_term) REFERENCES "PhenotypeTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (person_id)
);

CREATE TABLE "ConstructComponent_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "ConstructComponent" (curie)
);

CREATE TABLE "Reference_pages" (
	backref_id TEXT, 
	pages TEXT, 
	PRIMARY KEY (backref_id, pages), 
	FOREIGN KEY(backref_id) REFERENCES "Reference" (curie)
);

CREATE TABLE "Reference_mod_reference_types" (
	backref_id TEXT, 
	mod_reference_types TEXT, 
	PRIMARY KEY (backref_id, mod_reference_types), 
	FOREIGN KEY(backref_id) REFERENCES "Reference" (curie)
);

CREATE TABLE "Reference_tags" (
	backref_id TEXT, 
	tags VARCHAR(5), 
	PRIMARY KEY (backref_id, tags), 
	FOREIGN KEY(backref_id) REFERENCES "Reference" (curie)
);

CREATE TABLE "Reference_keywords" (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES "Reference" (curie)
);

CREATE TABLE "Image" (
	curie TEXT NOT NULL, 
	has_figure TEXT NOT NULL, 
	width INTEGER NOT NULL, 
	height INTEGER NOT NULL, 
	image_file TEXT NOT NULL, 
	image_medium_file TEXT NOT NULL, 
	image_thumbnail_file TEXT NOT NULL, 
	cropped_from TEXT, 
	image_x_origin INTEGER, 
	image_y_origin INTEGER, 
	video_still BOOLEAN, 
	table_key INTEGER, 
	created_by TEXT NOT NULL, 
	creation_date DATE, 
	modified_by TEXT NOT NULL, 
	date_last_modified DATE, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(has_figure) REFERENCES "Figure" (curie), 
	FOREIGN KEY(cropped_from) REFERENCES "Image" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (person_id)
);

CREATE TABLE "Antibody_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "Antibody" (curie)
);

CREATE TABLE "Figure_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "Figure" (curie)
);

CREATE TABLE "GeneDiseaseAnnotation_data_provider" (
	backref_id TEXT, 
	data_provider TEXT NOT NULL, 
	PRIMARY KEY (backref_id, data_provider), 
	FOREIGN KEY(backref_id) REFERENCES "GeneDiseaseAnnotation" (curie)
);

CREATE TABLE "GeneMolecularInteraction_interactor_A_role" (
	backref_id TEXT, 
	"interactor_A_role" VARCHAR(7), 
	PRIMARY KEY (backref_id, "interactor_A_role"), 
	FOREIGN KEY(backref_id) REFERENCES "GeneMolecularInteraction" (curie)
);

CREATE TABLE "GeneMolecularInteraction_interactor_B_role" (
	backref_id TEXT, 
	"interactor_B_role" VARCHAR(7), 
	PRIMARY KEY (backref_id, "interactor_B_role"), 
	FOREIGN KEY(backref_id) REFERENCES "GeneMolecularInteraction" (curie)
);

CREATE TABLE "Allele" (
	curie TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	table_key INTEGER, 
	created_by TEXT NOT NULL, 
	creation_date DATE, 
	modified_by TEXT NOT NULL, 
	date_last_modified DATE, 
	name TEXT, 
	cross_references TEXT, 
	symbol TEXT, 
	contains_construct TEXT, 
	molecular_mutation TEXT, 
	functional_impact TEXT, 
	generation_method TEXT, 
	associated_notes TEXT, 
	germline_transmission_status TEXT, 
	parent_cell_line TEXT, 
	mutant_cell_lines TEXT, 
	embryonic_stem_cell_lines TEXT, 
	images TEXT, 
	origins TEXT, 
	database_status VARCHAR(10), 
	inheritence_mode VARCHAR(13), 
	in_collection TEXT, 
	transposon_insertion TEXT, 
	aberration TEXT, 
	is_extinct BOOLEAN, 
	synonyms TEXT, 
	embryonic_cell_lines TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(contains_construct) REFERENCES "Construct" (curie), 
	FOREIGN KEY(images) REFERENCES "Image" (curie)
);

CREATE TABLE "ImagePane" (
	images TEXT NOT NULL, 
	label TEXT, 
	width INTEGER NOT NULL, 
	height INTEGER NOT NULL, 
	image_x_origin INTEGER, 
	image_y_origin INTEGER, 
	table_key INTEGER, 
	created_by TEXT NOT NULL, 
	creation_date DATE, 
	modified_by TEXT NOT NULL, 
	date_last_modified DATE, 
	PRIMARY KEY (images, label, width, height, image_x_origin, image_y_origin, table_key, created_by, creation_date, modified_by, date_last_modified), 
	FOREIGN KEY(images) REFERENCES "Image" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (person_id)
);

CREATE TABLE "Image_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "Image" (curie)
);

CREATE TABLE "AffectedGenomicModelComponent" (
	has_allele TEXT, 
	zygosity VARCHAR(12), 
	"AffectedGenomicModel_curie" TEXT, 
	PRIMARY KEY (has_allele, zygosity, "AffectedGenomicModel_curie"), 
	FOREIGN KEY(has_allele) REFERENCES "Allele" (curie), 
	FOREIGN KEY("AffectedGenomicModel_curie") REFERENCES "AffectedGenomicModel" (curie)
);

CREATE TABLE "AGMDiseaseAnnotation" (
	curie TEXT NOT NULL, 
	mod_id TEXT, 
	negated BOOLEAN, 
	evidence_codes TEXT NOT NULL, 
	annotation_reference TEXT NOT NULL, 
	annotation_type VARCHAR(16), 
	with TEXT, 
	disease_qualifiers VARCHAR(19), 
	condition_relations TEXT, 
	genetic_sex VARCHAR(13), 
	private_note TEXT, 
	disease_annotation_note TEXT, 
	disease_annotation_summary TEXT, 
	disease_genetic_modifier TEXT, 
	disease_genetic_modifier_relation VARCHAR(18), 
	object TEXT NOT NULL, 
	table_key INTEGER, 
	created_by TEXT NOT NULL, 
	creation_date DATE, 
	modified_by TEXT NOT NULL, 
	date_last_modified DATE, 
	inferred_allele TEXT, 
	inferred_gene TEXT, 
	subject TEXT NOT NULL, 
	predicate VARCHAR(11) NOT NULL, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(annotation_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(with) REFERENCES "Gene" (curie), 
	FOREIGN KEY(object) REFERENCES "DOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(inferred_allele) REFERENCES "Allele" (curie), 
	FOREIGN KEY(inferred_gene) REFERENCES "Gene" (curie), 
	FOREIGN KEY(subject) REFERENCES "AffectedGenomicModel" (curie)
);

CREATE TABLE "AGMPhenotypeAnnotation" (
	curie TEXT NOT NULL, 
	annotation_reference TEXT NOT NULL, 
	phenotype_term TEXT, 
	condition_relations TEXT, 
	object TEXT NOT NULL, 
	creation_date DATE NOT NULL, 
	table_key INTEGER, 
	created_by TEXT NOT NULL, 
	modified_by TEXT NOT NULL, 
	date_last_modified DATE, 
	inferred_allele TEXT, 
	inferred_gene TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(annotation_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(phenotype_term) REFERENCES "PhenotypeTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(inferred_allele) REFERENCES "Allele" (curie), 
	FOREIGN KEY(inferred_gene) REFERENCES "Gene" (curie), 
	FOREIGN KEY(subject) REFERENCES "AffectedGenomicModel" (curie)
);

CREATE TABLE "AlleleDiseaseAnnotation" (
	curie TEXT NOT NULL, 
	mod_id TEXT, 
	negated BOOLEAN, 
	evidence_codes TEXT NOT NULL, 
	annotation_reference TEXT NOT NULL, 
	annotation_type VARCHAR(16), 
	with TEXT, 
	disease_qualifiers VARCHAR(19), 
	condition_relations TEXT, 
	genetic_sex VARCHAR(13), 
	private_note TEXT, 
	disease_annotation_note TEXT, 
	disease_annotation_summary TEXT, 
	disease_genetic_modifier TEXT, 
	disease_genetic_modifier_relation VARCHAR(18), 
	object TEXT NOT NULL, 
	table_key INTEGER, 
	created_by TEXT NOT NULL, 
	creation_date DATE, 
	modified_by TEXT NOT NULL, 
	date_last_modified DATE, 
	inferred_gene TEXT, 
	subject TEXT NOT NULL, 
	predicate VARCHAR(16) NOT NULL, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(annotation_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(with) REFERENCES "Gene" (curie), 
	FOREIGN KEY(object) REFERENCES "DOTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(inferred_gene) REFERENCES "Gene" (curie), 
	FOREIGN KEY(subject) REFERENCES "Allele" (curie)
);

CREATE TABLE "AllelePhenotypeAnnotation" (
	curie TEXT NOT NULL, 
	annotation_reference TEXT NOT NULL, 
	phenotype_term TEXT, 
	condition_relations TEXT, 
	object TEXT NOT NULL, 
	creation_date DATE NOT NULL, 
	table_key INTEGER, 
	created_by TEXT NOT NULL, 
	modified_by TEXT NOT NULL, 
	date_last_modified DATE, 
	inferred_gene TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(annotation_reference) REFERENCES "Reference" (curie), 
	FOREIGN KEY(phenotype_term) REFERENCES "PhenotypeTerm" (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(inferred_gene) REFERENCES "Gene" (curie), 
	FOREIGN KEY(subject) REFERENCES "Allele" (curie)
);

CREATE TABLE "GeneGeneticInteraction" (
	curie TEXT NOT NULL, 
	cross_references TEXT, 
	interaction_data_provider VARCHAR(7) NOT NULL, 
	interaction_type VARCHAR(7) NOT NULL, 
	"interactor_A_type" VARCHAR(7) NOT NULL, 
	"interactor_B_type" VARCHAR(7) NOT NULL, 
	subject TEXT NOT NULL, 
	object TEXT NOT NULL, 
	"references" TEXT, 
	"interactor_A_genetic_perturbation" TEXT, 
	"interactor_B_genetic_perturbation" TEXT, 
	predicate TEXT NOT NULL, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(subject) REFERENCES "Gene" (curie), 
	FOREIGN KEY(object) REFERENCES "Gene" (curie), 
	FOREIGN KEY("references") REFERENCES "Reference" (curie), 
	FOREIGN KEY("interactor_A_genetic_perturbation") REFERENCES "Allele" (curie), 
	FOREIGN KEY("interactor_B_genetic_perturbation") REFERENCES "Allele" (curie)
);

CREATE TABLE "ReferenceType" (
	reference_association VARCHAR(9), 
	"references" TEXT, 
	"Allele_curie" TEXT, 
	PRIMARY KEY (reference_association, "references", "Allele_curie"), 
	FOREIGN KEY("Allele_curie") REFERENCES "Allele" (curie)
);

CREATE TABLE "Variant" (
	taxon TEXT NOT NULL, 
	table_key INTEGER, 
	created_by TEXT NOT NULL, 
	creation_date DATE, 
	modified_by TEXT NOT NULL, 
	date_last_modified DATE, 
	name TEXT, 
	curie TEXT NOT NULL, 
	hgvs_nomenclature TEXT, 
	genomic_reference_sequence TEXT, 
	genomic_variant_sequence TEXT, 
	padding_left TEXT, 
	padding_right TEXT, 
	release TEXT, 
	computed_gene TEXT, 
	variant_of_transcript TEXT, 
	variant_of_allele TEXT, 
	synonyms TEXT, 
	type TEXT, 
	"references" TEXT, 
	protein_sequence TEXT, 
	cross_references TEXT, 
	PRIMARY KEY (curie), 
	FOREIGN KEY(created_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(modified_by) REFERENCES "Person" (person_id), 
	FOREIGN KEY(computed_gene) REFERENCES "Gene" (curie), 
	FOREIGN KEY(variant_of_transcript) REFERENCES "Transcript" (curie), 
	FOREIGN KEY(variant_of_allele) REFERENCES "Allele" (curie)
);

CREATE TABLE "Allele_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "Allele" (curie)
);

CREATE TABLE "Allele_affected_entities" (
	backref_id TEXT, 
	affected_entities TEXT, 
	PRIMARY KEY (backref_id, affected_entities), 
	FOREIGN KEY(backref_id) REFERENCES "Allele" (curie)
);

CREATE TABLE "GeneGenomicLocation" (
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	has_assembly TEXT NOT NULL, 
	start TEXT, 
	"end" TEXT, 
	"Gene_curie" TEXT, 
	PRIMARY KEY (subject, predicate, object, has_assembly, start, "end", "Gene_curie"), 
	FOREIGN KEY(subject) REFERENCES "Variant" (curie), 
	FOREIGN KEY(object) REFERENCES "Chromosome" (curie), 
	FOREIGN KEY(has_assembly) REFERENCES "Chromosome" (curie), 
	FOREIGN KEY("Gene_curie") REFERENCES "Gene" (curie)
);

CREATE TABLE "VariantGeneConsequence" (
	subject TEXT NOT NULL, 
	vep_consequence VARCHAR(8), 
	vep_impact TEXT, 
	polyphen_score FLOAT, 
	polyphen_prediction VARCHAR(17), 
	sift_score FLOAT, 
	sift_prediction VARCHAR(11), 
	object TEXT NOT NULL, 
	PRIMARY KEY (subject, vep_consequence, vep_impact, polyphen_score, polyphen_prediction, sift_score, sift_prediction, object), 
	FOREIGN KEY(subject) REFERENCES "Variant" (curie), 
	FOREIGN KEY(object) REFERENCES "Gene" (curie)
);

CREATE TABLE "VariantGenomicLocation" (
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	has_assembly TEXT NOT NULL, 
	start TEXT, 
	"end" TEXT, 
	PRIMARY KEY (subject, predicate, object, has_assembly, start, "end"), 
	FOREIGN KEY(subject) REFERENCES "Variant" (curie), 
	FOREIGN KEY(object) REFERENCES "Chromosome" (curie), 
	FOREIGN KEY(has_assembly) REFERENCES "Chromosome" (curie)
);

CREATE TABLE "VariantTranscriptConsequence" (
	subject TEXT NOT NULL, 
	vep_consequence VARCHAR(8), 
	vep_impact TEXT, 
	polyphen_score FLOAT, 
	polyphen_prediction VARCHAR(17), 
	sift_score FLOAT, 
	sift_prediction VARCHAR(11), 
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
	cnda_end TEXT, 
	PRIMARY KEY (subject, vep_consequence, vep_impact, polyphen_score, polyphen_prediction, sift_score, sift_prediction, amino_acid_reference, amino_acid_variant, codon_reference, codon_variant, cdna_start, cdna_end, cds_start, cds_end, protein_start, protein_end, hgvs_protein_nomenclature, hgvs_coding_nomenclature, object, cnda_end), 
	FOREIGN KEY(subject) REFERENCES "Variant" (curie), 
	FOREIGN KEY(object) REFERENCES "Transcript" (curie)
);

CREATE TABLE "AGMDiseaseAnnotation_data_provider" (
	backref_id TEXT, 
	data_provider TEXT NOT NULL, 
	PRIMARY KEY (backref_id, data_provider), 
	FOREIGN KEY(backref_id) REFERENCES "AGMDiseaseAnnotation" (curie)
);

CREATE TABLE "AlleleDiseaseAnnotation_data_provider" (
	backref_id TEXT, 
	data_provider TEXT NOT NULL, 
	PRIMARY KEY (backref_id, data_provider), 
	FOREIGN KEY(backref_id) REFERENCES "AlleleDiseaseAnnotation" (curie)
);

CREATE TABLE "GeneGeneticInteraction_interactor_A_role" (
	backref_id TEXT, 
	"interactor_A_role" VARCHAR(7), 
	PRIMARY KEY (backref_id, "interactor_A_role"), 
	FOREIGN KEY(backref_id) REFERENCES "GeneGeneticInteraction" (curie)
);

CREATE TABLE "GeneGeneticInteraction_interactor_B_role" (
	backref_id TEXT, 
	"interactor_B_role" VARCHAR(7), 
	PRIMARY KEY (backref_id, "interactor_B_role"), 
	FOREIGN KEY(backref_id) REFERENCES "GeneGeneticInteraction" (curie)
);

CREATE TABLE "GeneGeneticInteraction_phenotype_or_trait" (
	backref_id TEXT, 
	phenotype_or_trait TEXT, 
	PRIMARY KEY (backref_id, phenotype_or_trait), 
	FOREIGN KEY(backref_id) REFERENCES "GeneGeneticInteraction" (curie)
);

CREATE TABLE "Variant_secondary_identifiers" (
	backref_id TEXT, 
	secondary_identifiers TEXT, 
	PRIMARY KEY (backref_id, secondary_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "Variant" (curie)
);

CREATE TABLE "Variant_data_provider" (
	backref_id TEXT, 
	data_provider TEXT, 
	PRIMARY KEY (backref_id, data_provider), 
	FOREIGN KEY(backref_id) REFERENCES "Variant" (curie)
);

CREATE TABLE "Variant_notes" (
	backref_id TEXT, 
	notes TEXT, 
	PRIMARY KEY (backref_id, notes), 
	FOREIGN KEY(backref_id) REFERENCES "Variant" (curie)
);

