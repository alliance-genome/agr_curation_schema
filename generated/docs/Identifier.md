# Identifier

None


```mermaid
 classDiagram
    class Identifier
      Identifier : counter
      Identifier : curie
      Identifier : subdomain_code
      Identifier : subdomain_name
      




URI: [alliance:Identifier](http://alliancegenome.org/Identifier)


## Parent Classes




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [counter](counter.md) | a number to identify an alliance resource in a subdomain |
| [curie](curie.md) | A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI |
| [subdomain_code](subdomain_code.md) | a three letter string, representing a subdomain (e.g 101 represents disease_annotation) |
| [subdomain_name](subdomain_name.md) | subdomain name (e.g disease_annotation) |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:Identifier'] |
| native | ['alliance:Identifier'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Identifier
from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
slots:
- counter
- subdomain_code
- subdomain_name
- curie

```
</details>

### Induced

<details>
```yaml
name: Identifier
from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
attributes:
  counter:
    name: counter
    description: a number to identify an alliance resource in a subdomain
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: counter
    owner: Identifier
    domain_of:
    - Identifier
    range: integer
  subdomain_code:
    name: subdomain_code
    description: a three letter string, representing a subdomain (e.g 101 represents
      disease_annotation)
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: subdomain_code
    owner: Identifier
    domain_of:
    - Identifier
    range: string
  subdomain_name:
    name: subdomain_name
    description: subdomain name (e.g disease_annotation)
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: subdomain_name
    owner: Identifier
    domain_of:
    - Identifier
    range: string
  curie:
    name: curie
    description: A unique identifier for a thing. Must be either a CURIE shorthand
      for a URI or a complete URI
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    multivalued: false
    identifier: true
    alias: curie
    owner: Identifier
    domain_of:
    - OntologyTerm
    - PhenotypeAnnotation
    - DiseaseAnnotation
    - BiologicalEntity
    - BiologicalEntityDTO
    - Chromosome
    - Assembly
    - Identifier
    - Figure
    - Image
    - Laboratory
    - InformationContentEntity
    - Reference
    - Resource
    - ModCorpusAssociation
    - GeneInteraction
    - ExpressionExperiment
    - GeneNomenclatureSet
    range: uriorcurie

```
</details>