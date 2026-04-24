import sys
import urllib.request
import json
import ssl
import argparse

def get_route(coords):
    url = f"http://router.project-osrm.org/route/v1/driving/{coords}?overview=full&geometries=geojson"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        with urllib.request.urlopen(req, context=ctx) as response:
            data = json.loads(response.read().decode())
            return data['routes'][0]['geometry']['coordinates']
    except Exception as e:
        return []

def create_kml(options_data, pois, output_file):
    colors = ["ff0000ff", "ff00aa00", "ffffaa00", "ffff00ff"]
    kml = ['<?xml version="1.0" encoding="UTF-8"?>', '<kml xmlns="http://www.opengis.net/kml/2.2">', '  <Document>']
    
    for i, opt in enumerate(options_data):
        name = opt['name']
        coords = opt['coords']
        color = colors[i % len(colors)]
        path = get_route(coords)
        coord_str = " ".join([f"{c[0]},{c[1]},0" for c in path])
        
        kml.append(f'    <Folder><name>{name}</name>')
        kml.append(f'      <Style id="s{i}"><LineStyle><color>{color}</color><width>5</width></LineStyle></Style>')
        kml.append(f'      <Placemark><name>Route</name><styleUrl>#s{i}</styleUrl><LineString><tessellate>1</tessellate><coordinates>{coord_str}</coordinates></LineString></Placemark>')
        
        opt_pois = opt.get('pois', [])
        for p in opt_pois:
            kml.append(f'      <Placemark><name>{p[0]}</name><Point><coordinates>{p[1]},{p[2]},0</coordinates></Point></Placemark>')
        kml.append('    </Folder>')
    
    kml.append('  </Document></kml>')
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(kml))

if __name__ == "__main__":
    # 此腳本供 Skill 內部調用，接收 JSON 配置產生地圖
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="JSON config file for routes and POIs")
    parser.add_argument("--output", default="trip.kml")
    args = parser.parse_args()
    
    with open(args.config, "r", encoding="utf-8") as f:
        config = json.load(f)
    
    create_kml(config['options'], config.get('common_pois', []), args.output)
    print(f"✅ KML generated: {args.output}")
