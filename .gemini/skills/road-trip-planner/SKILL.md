# Road Trip Planner (POI Edition)

此 Skill 協助使用者規劃行程，並產出標記景點 (POI) 的 KML 地圖。

## 核心功能

1. **景點 (POI) 標記**: 透過 `scripts/generate_kml.py` 將座標點轉化為 KML 中的地標標記。
2. **多圖層管理**: 支援在單一 KML 檔案中依日期或方案分組（圖層）。

## 使用流程

### 1. 收集座標點
整理各方案的關鍵景點座標（經度,緯度）。

### 2. 準備設定檔 (config.json)
```json
{
  "options": [
    {
      "name": "Day 1",
      "pois": [["景點名", 經度, 緯度], ...]
    }
  ]
}
```

### 3. 執行產生腳本
```bash
python3 scripts/generate_kml.py --config config.json --output my_trip.kml
```

## 注意事項
- 此版本已移除自動循跡（真實道路）功能，僅保留點位標記，以提高與 Google My Maps 的相容性。
- 產出的 KML 可直接匯入 Google My Maps。
