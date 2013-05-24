from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import IFrame
from django.utils.translation import ugettext as _
from django.conf import settings

class IFramePlugin(CMSPluginBase):
    model = IFrame
    name = _("iFrame")
    render_template = "cmsplugin_iframe/iframe.html"
    text_enabled = True
    
    def render(self, context, instance, placeholder):
        placeholder_width = context.get('width', None)
        
        if instance.width:
            width = instance.width
        else:
            width = placeholder_width
            
        context.update({'iframe':instance,
                        'iframe_width':width,
                        'iframe_height':instance.height,
                        'placeholder':placeholder})

        return context

    def icon_src(self, instance):
              return settings.STATIC_URL + u"cms/images/plugins/snippet.png"

plugin_pool.register_plugin(IFramePlugin)
