# IdentifiersRange

None


```mermaid
 classDiagram
    class IdentifiersRange
      IdentifiersRange : first
      IdentifiersRange : last
      




URI: [alliance:IdentifiersRange](http://alliancegenome.org/IdentifiersRange)


## Parent Classes




<!-- no inheritance hierarchy -->


## Slots

| Name | Description  |
| ---  | ---  |
| [first](first.md) | first identifier in a range |
| [last](last.md) | last identifier in a range |


## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['alliance:IdentifiersRange'] |
| native | ['alliance:IdentifiersRange'] |




## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IdentifiersRange
from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
slots:
- first
- last

```
</details>

### Induced

<details>
```yaml
name: IdentifiersRange
from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
attributes:
  first:
    name: first
    description: first identifier in a range
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: first
    owner: IdentifiersRange
    domain_of:
    - IdentifiersRange
    range: Identifier
  last:
    name: last
    description: last identifier in a range
    from_schema: https://github.com/alliance-genome/agr_curation_schema/core.yaml
    alias: last
    owner: IdentifiersRange
    domain_of:
    - IdentifiersRange
    range: Identifier

```
</details>