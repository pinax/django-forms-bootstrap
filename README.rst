Django Forms Bootstrap
======================

.. image:: https://img.shields.io/travis/pinax/django-forms-bootstrap.svg
    :target: https://travis-ci.org/pinax/django-forms-bootstrap

.. image:: https://img.shields.io/coveralls/pinax/django-forms-bootstrap.svg
    :target: https://coveralls.io/r/pinax/django-forms-bootstrap

.. image:: https://img.shields.io/pypi/dm/django-forms-bootstrap.svg
    :target:  https://pypi.python.org/pypi/django-forms-bootstrap/

.. image:: https://img.shields.io/pypi/v/django-forms-bootstrap.svg
    :target:  https://pypi.python.org/pypi/django-forms-bootstrap/

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target:  https://pypi.python.org/pypi/django-forms-bootstrap/


Simple Bootstrap filter for Django forms. Extracted from the
bootstrap theme for Pinax.


Quick Start
-----------

Include "django-forms-bootstrap" in your requirements file and
"django_forms_bootstrap" in your INSTALLED APPS.

Make sure your template loader finders includes app directories.

To style forms, add the following to the top of your template ::
    
    {% load bootstrap_tags %}

and include your form using something like the following markup: ::
    
    <form>
        <legend>My Form</legend>
        {% csrf_token %}
        {{ form|as_bootstrap }}
        <div class="form-actions">
          <a href="#back" class="btn">Go back</a>
          <button type="submit" class="btn btn-primary">Save changes</button>
        </div>
    </form>


Specifying form layouts
-----------------------

Bootstrap includes styles for three types of forms. To change the display of
your form, add one of the following class attributes to your form tag and
use the appropriate template filter:

================   ======================================   ========================================
    Class          Template filter                                Description
================   ======================================   ========================================
.form-vertical     ``{{ form|as_bootstrap }}``              Labels over controls (default)
.form-horizontal   ``{{ form|as_bootstrap_horizontal }}``   Labels on same line as controls
.form-inline       ``{{ form|as_bootstrap_inline }}``       Compact style with inline-block controls
================   ======================================   ========================================


License & Attribution
---------------------

Django Forms Bootstrap is released under the MIT license. It does not include
any styles or scripts from the Bootstrap project.
