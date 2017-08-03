from ..models import MLModel
from django import template


register = template.Library()

@register.inclusion_tag("nnnba/model_details_selector.html")
def show_models_details(selected_model_name):
    all_models = MLModel.objects.all()
    return { "all_models": all_models , "selected_model_name": selected_model_name}
