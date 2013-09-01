from django import template
from django.template import Context
from django.template.loader import get_template


register = template.Library()


@register.filter
def as_bootstrap(form):
    template = get_template("bootstrap/form.html")
    for field in form.fields:
        name = form.fields[field].widget.__class__.__name__.lower()
        if not name.startswith("radio") and not name.startswith("checkbox"):
            form.fields[field].widget.attrs["class"] = " form-control"
    c = Context({"form": form})
    return template.render(c)


@register.filter
def css_class(field):
    return field.field.widget.__class__.__name__.lower()
