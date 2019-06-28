from StringIO import StringIO

import mapnik
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def initialize_map():
    m = mapnik.Map(300,300)
    m.background = mapnik.Color('white')
    s = mapnik.Style()
    r = mapnik.Rule()
    polygon_symbolizer = mapnik.PolygonSymbolizer()
    polygon_symbolizer.fill = mapnik.Color('#000000')
    r.symbols.append(polygon_symbolizer)

    line_symbolizer = mapnik.LineSymbolizer()
    line_symbolizer.stroke = mapnik.Color('rgb(100%,100%,100%)')
    line_symbolizer.stroke_width = 0.5

    r.symbols.append(line_symbolizer)
    s.rules.append(r)
    m.append_style('My Style',s)
    ds = mapnik.Shapefile(file='ne_110m_admin_0_countries.shp')
    layer = mapnik.Layer('world')
    layer.datasource = ds
    layer.styles.append('My Style')
    m.layers.append(layer)
    m.zoom_all()

    return m

def render_image(map_obj):
    im = mapnik.Image(300, 300)
    # mapnik.render_to_file(map_obj, '/tmp/world.png', 'png')
    map_obj.zoom_to_box(mapnik.Box2d(32.2654333839, 27.5013261988, 35.8363969256, 33.2774264593))
    mapnik.render(map_obj, im)
    string = im.tostring('tiff')
    img = Image.open(StringIO(string))
    plt.imshow(np.array(img), cmap="gray")
    plt.axis('off')
    plt.show(axis='off')

m = initialize_map()
render_image(m)
print "rendered image to 'world.png'"