# -*- coding: utf-8 -*-
from pyramid.httpexceptions import HTTPForbidden, HTTPNotFound
from sqlalchemy.orm.exc import NoResultFound
from nextgisweb.models import DBSession
from ..model import Trailcam


def get_trailcam_items(request):
    trailcam_id = request.matchdict['trailcam_id']

    try:
        trailcam = DBSession.query(Trailcam).get(trailcam_id)
        trailcam_items = trailcam.items
    except NoResultFound:
        raise HTTPNotFound()

    trailcam_items_result = [trailcam_item.as_json_dict() for trailcam_item in trailcam_items]

    return trailcam_items_result
