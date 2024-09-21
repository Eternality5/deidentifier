from django.shortcuts import render


def render_with_htmx(request, template_name, context):
    """
    Makes a check to see if a page can be rendered by HTMX and if it can it only renders the partial rather than the
    whole page

    param request: WGSIRequest
    param template_name: the template name not trailing "_" or directories
    param contest: the context that would be used
    """
    return (
        render(request, "processes/partials/_" + template_name, context)
        if request.headers.get('HX-Request')
        else render(request, "processes/" + template_name, context))
