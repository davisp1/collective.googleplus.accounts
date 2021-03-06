# -*- coding: utf-8 -*-

from Products.CMFCore.utils import getToolByName

from collective.googleplus.accounts.config import PROJECTNAME

def uninstall(portal, reinstall=False):
    if not reinstall:
        profile = 'profile-%s:uninstall' % PROJECTNAME
        setup_tool = getToolByName(portal, 'portal_setup')
        setup_tool.runAllImportStepsFromProfile(profile)

        # XXX: Configlet is not unregistered using just GS, so we do it here;
        # we have 2 profiles: initial and default; could it be that?
        portal_controlpanel = getToolByName(portal, 'portal_controlpanel')
        portal_controlpanel.unregisterConfiglet('GooglePlusSettings')

        return "Ran all uninstall steps."
