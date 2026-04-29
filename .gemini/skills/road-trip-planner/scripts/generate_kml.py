import sys
import json
import argparse

def create_kml(options_data, output_file):
    kml = ['<?xml version="1.0" encoding="UTF-8"?>', '<kml xmlns="http://www.opengis.net/kml/2.2">', '  <Document>']
    
    for i, opt in enumerate(options_data):
        name = opt['name']
        kml.append(f'    <Folder><name>{name}</name>')
        
        opt_pois = opt.get('pois', [])
        for p in opt_pois:
            kml.append(f'      <Placemark><name>{p[0]}</name><Point><coordinates>{p[1]},{p[2]},0</coordinates></Point></Placemark>')
        kml.append('    </Folder>')
    
    kml.append('  </Document></kml>')
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(kml))

if __name__ == "__main__":
    # 此腳本供 Skill 內部調用，接收 JSON 配置產生地圖 (僅標記點位)
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="JSON config file for POIs")
    parser.add_argument("--output", default="trip.kml")
    args = parser.parse_args()
    
    with open(args.config, "r", encoding="utf-8") as f:
        config = json.load(f)
    
    create_kml(config['options'], args.output)
    print(f"✅ KML generated (Markers only): {args.output}")
