# A Spider for mazii
# ただ技術の勉強のため作成したものですが、コンテンツを侵害している場合はご連絡ください。

- this is a spider to get mazii specialized word list and save into youdao xml format, which could also import into eudic.

##  usage
### requirements
`pip install -r requirements.txt`

### spider in multi threads
`python3 main.py`

### output
the xml file will output to `OUTPUT_DIR` set in [main.py](./main.py#L9), [xml](./xml) folder by default.

## keys of specialized word list
| key                | means                                          |
| ------------------ | ---------------------------------------------- |
| Buddh              | 仏教                                           |
| Shinto             | 神道                                           |
| aa                 | 自動車アクセサリー                             |
| aeim               | 空調・電気設備資材                             |
| agric1             | 農業                                           |
| agrihsup           | 農業・園芸用品                                 |
| agrmach            | 農業機械                                       |
| agrtool            | 農業用工具                                     |
| am                 | 研磨材                                         |
| anat               | 解剖学                                         |
| aoc                | 自動車用オイル・化学製品                       |
| archhardw          | 建築金物                                       |
| archit             | 建築学・建設                                   |
| architconst        | 建築・建設                                     |
| arm                | 接着剤・補修材                                 |
| asp                | 自動車部品                                     |
| astron             | 天文学                                         |
| ave                | 空調・換気機器・防虫用品                       |
| baseb              | 野球                                           |
| bec                | バッテリー・電装部品                           |
| bgoc               | 自転車用グリース・オイル・化学製品             |
| bh                 | 美容・理容用品                                 |
| biol               | 生物学                                         |
| bipa               | 自転車部品                                     |
| bmta               | 自転車メンテナンスツール・アクセサリー         |
| bopa               | ボディ・塗装                                   |
| bot                | 植物学                                         |
| buildmatext        | 建築材料・エクステリア                         |
| bus                | ビジネス                                       |
| caregivsup         | 介護用品                                       |
| cb                 | 完成車（自転車）                               |
| cd                 | 制御装置                                       |
| chem               | 化学                                           |
| cleanroom          | クリーンルーム用品                             |
| comp               | コンピュータ                                   |
| cpeh               | コンプレッサー・空圧機器・ホース               |
| cs                 | 清掃用品                                       |
| ct                 | 切削工具                                       |
| cwc                | 洗車・クリーニング                             |
| disprevcpsup       | 防災・防犯用品                                 |
| dn                 | 日用品                                         |
| dr                 | 洗剤・除去剤                                   |
| econ               | 経済学                                         |
| elecwatsup         | 電気・水道用品                                 |
| em                 | 電気材料                                       |
| emghygsup          | 緊急・衛生用品                                 |
| engr               | 工学                                           |
| engtool            | エンジン工具                                   |
| fb                 | 食品・飲料                                     |
| ferpestherseed     | 肥料・農薬・除草剤・種子                       |
| fimcma             | フォークリフト・産業機械・建設機械アクセサリー |
| finc               | 金融                                           |
| food               | 食品・料理                                     |
| gap                | 純正自動車部品                                 |
| geme               | ガレージ機器・メンテナンス機器                 |
| geol               | 地質学                                         |
| geom               | 幾何学                                         |
| glov               | 手袋                                           |
| gmp                | 純正バイク部品                                 |
| gtp                | 純正トラック部品                               |
| ha                 | 家電                                           |
| handtool           | 手工具                                         |
| healthcare         | ヘルスケア                                     |
| hehh               | 油圧機器・油圧ホース                           |
| internet           | インターネット                                 |
| it                 | 情報技術                                       |
| ks                 | キッチン用品                                   |
| law                | 法律                                           |
| lifest             | ライフスタイル                                 |
| ling               | 言語学                                         |
| log                | 物流                                           |
| logisup            | 物流用品                                       |
| lt                 | 照明                                           |
| mahj               | 麻雀                                           |
| mask               | マスク                                         |
| mat                | 材料（金属シート・プレート・丸棒・パイプ）     |
| math               | 数学                                           |
| mb                 | バイク車体                                     |
| mc                 | 機械部品                                       |
| mch                | 機械コンポーネント                             |
| measinstr          | 測定機器                                       |
| measserv           | 計測関連サービス                               |
| mech1              | 整備士                                         |
| mechanic           | 機械工学                                       |
| med                | 医学                                           |
| medsci             | 医療・科学                                     |
| medsup             | 医療用品                                       |
| mil                | 軍事                                           |
| mocw               | バイク用オイル・化学製品・洗浄                 |
| mp                 | バイク部品                                     |
| mts                | メンテナンスツール・収納                       |
| mtwtg              | メンテナンスツール・ウェア・ツーリングギア     |
| music              | 音楽                                           |
| of                 | オフィス家具                                   |
| officesup          | オフィス用品                                   |
| offsup             | オフィス用品                                   |
| pa                 | 塗料                                           |
| packingsup         | 梱包用品                                       |
| paintprotcovintfin | 塗装・保護カバー・内装仕上げ用品               |
| pbeh               | ポンプ・ブロワー・電気ヒーター                 |
| pc                 | パソコン                                       |
| physics            | 物理学                                         |
| pneutool           | 空圧工具                                       |
| powertool          | 電動工具                                       |
| pwfc               | 配管・水設備部品                               |
| residequip         | 住宅設備                                       |
| safequip           | 安全装備                                       |
| safesign           | 安全標識                                       |
| safesup            | 安全用品                                       |
| safetysup          | 安全用品                                       |
| safeworkshoes      | 安全靴・作業靴                                 |
| sbn                | ネジ・ボルト・釘                               |
| schooledsup        | 学校・教育用品                                 |
| scirdevsup         | 科学研究・開発用品                             |
| sewingsup          | 裁縫用品                                       |
| sfae               | 店舗什器・設備                                 |
| shipfishsup        | 船舶用品・漁業用品                             |
| shogi              | 将棋                                           |
| sog                | スプレー・オイル・グリース                     |
| sports             | スポーツ                                       |
| sras               | はんだ付け用品・静電気対策用品                 |
| storagesup         | 保管用品                                       |
| sumo               | 相撲                                           |
| surveyinstr        | 測量機器（土木・建設）                         |
| tap                | トラックアクセサリー・部品                     |
| tape               | テープ                                         |
| tc                 | 食卓消耗品                                     |
| ts                 | タイヤ・サスペンション                         |
| ttss               | トラック輸送・安全用品                         |
| tusocw             | トラック用尿素水・オイル・化学製品・洗浄       |
| tv                 | テレビ                                         |
| veh                | 車両                                           |
| workw              | 作業服                                         |
| wrktl              | 作業工具                                       |
| ws                 | 溶接用品                                       |
| zool               | 動物学                                         |
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 