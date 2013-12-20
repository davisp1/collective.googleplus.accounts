# -*- coding: utf-8 -*-
from Products.Five import BrowserView
from zope.component import getUtility

from zope import schema
from zope.schema.vocabulary import SimpleVocabulary

from plone.app.controlpanel.form import ControlPanelForm

from plone.fieldsets.fieldsets import FormFieldsets
from plone.fieldsets.form import FieldsetsEditForm

from zope.component import adapts
from zope.interface import implements
from zope.interface import Interface

from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone.interfaces import IPloneSiteRoot

from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from interfaces import IGooglePlusControlPanel

from collective.facebook.accounts import _
from plone.registry.interfaces import IRegistry

from plone.i18n.normalizer.interfaces import IIDNormalizer

from collective.googleplus.accounts.config import PROJECTNAME

import json
import urllib
from datetime import datetime, timedelta
import DateTime
import logging

logger = logging.getLogger(PROJECTNAME)

class IGooglePlusSchema(Interface):
    """ Google+ App Config """
    app_key = schema.TextLine(title=_(u'App ID/API Key'),
                              description=_(u"ID for your application. "
                                             "You need to create an Google+ app"
                                             "apps"),
                              required=True)

    # I think this is not neccessary
    app_secret = schema.TextLine(title=_(u'App Secret'),
                                 description=_(u"Secret for your application. ( mandatory to get long life user token )"),
                                 required=False)


class GooglePlusControlPanelAdapter(SchemaAdapterBase):

    adapts(IPloneSiteRoot)
    implements(IGooglePlusSchema)

    app_key = ""
    app_secret = ""


class GooglePlusControlPanel(ControlPanelForm):
    """
    Google+ control panel view
    """

    implements(IGooglePlusControlPanel)

    template = ViewPageTemplateFile('./templates/googleplus-control-panel.pt')
    label = _("Google+ setup")
    description = _("""Lets you configure several Google+ accounts""")

    auth = FormFieldsets(IGooglePlusSchema)
    auth.id = 'auth'
    auth.label = _(u'Authorize')

    form_fields = FormFieldsets(
                        auth,
                        )

    request_user_auth = _(u"Request user auth")
    request_app_token = _(u"Authenticate app")

    def decodeParams(self,params):
        response = {}
        for param in params.split("&"):
            key, value = param.split("=")
            response[key] = value
        return response

    def __call__(self):
        return super(GooglePlusControlPanel, self).__call__()

    def getAccounts(self):
        registry = getUtility(IRegistry)
        accounts = registry.get('collective.googleplus.accounts', None)

        return accounts


class RemoveAuthAccount(BrowserView):

    def __call__(self, account_name):
        registry = getUtility(IRegistry)
        accounts = registry.get('collective.googleplus.accounts', None)
        if not accounts:
            accounts = {}

        try:
            del accounts[account_name]
            registry['collective.googleplus.accounts'] = accounts
        except:
            pass
