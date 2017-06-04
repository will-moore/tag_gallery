
from django.shortcuts import render
import omero
from omero.rtypes import rstring
from omeroweb.webclient.decorators import login_required


@login_required()
def index(request, conn=None, **kwargs):
    """Home page shows a list of Galleries (tags)"""
    query = "select obj from TagAnnotation obj where obj.textValue like :start"

    query_service = conn.getQueryService()
    params = omero.sys.ParametersI()
    # Look for Tags that start with 'Gallery-' Use a % as wild-card.
    params.add('start', rstring('Gallery-%'))

    tags = query_service.findAllByQuery(query, params, conn.SERVICE_OPTS)

    tag_dict = [{'id': t.id.val, 'name': t.textValue.val.replace("Gallery-", "")} for t in tags]

    context = {'tag_dict': tag_dict}

    return render(request, 'tag_gallery/index.html', context)


@login_required()
def tag(request, tag_id, conn=None, **kwargs):

    links = list(conn.getAnnotationLinks("Image", ann_ids=[tag_id]))

    imgs = [{'id': l.parent.id.val, 'name': l.parent.name.val} for l in links]

    context = {'imgs': imgs}

    return render(request, 'tag_gallery/tag.html', context)
