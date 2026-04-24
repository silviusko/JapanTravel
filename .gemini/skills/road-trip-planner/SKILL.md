---
name: road-trip-planner
description: 全球自駕行程規劃與高精度 KML 地圖產生工具。支援呼叫路由引擎產生貼合真實道路（而非直線）的軌跡，並可管理多方案圖層與景點標記。
---

# Road Trip Planner

此 Skill 協助使用者規劃任何地區的自駕行程，並產出專業級的 KML 地圖。

## 核心功能

1. **真實道路循跡**: 透過 `scripts/generate_kml.py` 呼叫 OSRM 引擎，將座標點轉化為真實的道路曲線。
2. **多圖層方案管理**: 支援在單一 KML 檔案中封裝多個獨立方案（圖層）。
3. **景點 (POI) 整合**: 支援在路線中標記重要景點。

## 使用流程

### 1. 收集座標點
整理各方案的關鍵停留點座標（經度,緯度）。

### 2. 準備設定檔 (config.json)
```json
{
  "options": [
    {
      "name": "方案 A",
      "coords": "經1,緯1;經2,緯2;...",
      "pois": [["景點名", 經, 緯], ...]
    }
  ]
}
```

### 3. 執行產生腳本
```bash
python3 scripts/generate_kml.py --config config.json --output my_trip.kml
```

## 注意事項
- 路由引擎依賴 OpenStreetMap 數據，適用於全球大部分有道路覆蓋的地區。
- 產出的 KML 可直接匯入 Google My Maps、Maps.me 或 Garmin 等裝置。
