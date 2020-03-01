# How to using custom form with CRUD

## Create form

```bash
> bin/console make:form
The name of the form class (e.g. FierceChefType):
> CarType
The name of Entity or fully qualified model class name that the new form will be bound to (empty for none):
> Car\Car
```

```bash
created: src/Form/CarType.php

Success!

Next: Add fields to your form and start using it.
Find the documentation at https://symfony.com/doc/current/forms.html
```

## Move form sub folder

Move from `src\Form\CarType.php` to `src\Form\Type\CarType.php`

Then update namespace of class

```bash
namespace App\Form\Type;

use Sylius\Bundle\ResourceBundle\Form\Type\AbstractResourceType;
use Symfony\Component\Form\FormBuilderInterface;

class CarType extends AbstractResourceType
{
    public function buildForm(FormBuilderInterface $builder, array $options)
    {
        $builder
            ->add('category')
            ->add('brand')
            ->add('customer')
            ->add('model')
            ->add('year')
        ;
    }

    public function getBlockPrefix()
    {
        return 'app_car';
    }
}
```

## Register resouce (Update)

Update resource form `config\packages\sylius_resource.yaml`

```bash
sylius_resource:
  resources:
    app.car:
      driver: doctrine/orm
      classes:
        model: App\Entity\Car\Car
        form: App\Form\Type\CarType  #Add there
```

## Register form to service

`config/services.yaml`

```bash
services:
  app.car.form.type:
    class: App\Form\Type\CarType
    arguments: ['%app.model.car.class%']
```

## Looking information of form

```bash
> bin/console debug:container app.car.form.type
```
