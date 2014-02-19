from flask.ext.assets import Bundle
from totem import assets


js = Bundle('js/grayscale.js', filters='jsmin', output='gen/packed.js')
assets.register('js_all', js)

css = Bundle('less/grayscale.less', filters='less', output='gen/packed.css')
assets.register('css_all', css)
