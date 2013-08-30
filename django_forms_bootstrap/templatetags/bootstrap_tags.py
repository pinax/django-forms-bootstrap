from django import forms, template
from django.template import Context
from django.template.loader import get_template


register = template.Library()


def add_style_class(widget, style):
    attr_class = set(widget.attrs.setdefault("class", "").split(" "))
    attr_class.add(style)
    widget.attrs["class"] = " ".join(attr_class)


@register.filter
def as_bootstrap(form):
    for field in form:
        widget = field.field.widget
        if isinstance(widget, forms.TextInput):
            add_style_class(widget, "form-control")
    template = get_template("bootstrap/form.html")
    c = Context({"form": form})
    return template.render(c)


@register.filter
def css_class(field):
    return field.field.widget.__class__.__name__.lower()
