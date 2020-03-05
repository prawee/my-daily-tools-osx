# How to adding validator to entity

## Using constraints on Entity class

Example `src\Entity\Car\Car`

```bash
use Symfony\Component\Validator\Constraints as Assert;
```

## Adding annotations with column

```bash
/**
* @Assert\NotBlank
*/
private $brand;
```
