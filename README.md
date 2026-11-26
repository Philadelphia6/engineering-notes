# 项目问题与学习笔记

记录各项目中的问题、原因、解决方案和验证结果，便于后续查阅与复用。

## 问题索引

| 编号 | 日期 | 项目 | 问题 | 状态 |
| --- | --- | --- | --- | --- |
| NOTE-0001 | 2026-11-07 | 半桥 LLC / TMS320F28035 | [比较器和运放的供电、输入共模范围与输出电源轨](projects/llc/NOTE-0001-common-mode-and-power-rails.md) | 数据手册已核对；方案待硬件验证 |
| NOTE-0002 | 2026-11-07 | UPS / U.PSDR.L.CT3K C25285 | [UPS学习记录：共用桥臂、采样偏置、启动跌落及设计学习点](projects/ups/NOTE-0002-ups-learning-record.md) | 原理及部分实测已确认；其余待验证 |
| NOTE-0003 | 2026-11-26 | 200 W双相交错Buck | [规格冻结、交错原理与电流应力](projects/buck/NOTE-0003-architecture-and-current-stress.md) | 理论计算已整理；硬件效率和温升待验证 |
| NOTE-0004 | 2026-11-26 | 200 W双相交错Buck | [每相感量计算、容差与峰值电流](projects/buck/NOTE-0004-inductance-and-worst-case.md) | 公式及数值已复算；磁件偏置和温升待实测 |
| NOTE-0005 | 2026-11-26 | 200 W双相交错Buck | [AP法、EE磁芯、气隙与平面电感](projects/buck/NOTE-0005-ferrite-area-product-and-planar.md) | 计算方法已整理；尚未冻结磁芯厂家和实物规格 |
| NOTE-0006 | 2026-11-26 | 200 W双相交错Buck | [一体成型电感与提高频率的体积收益](projects/buck/NOTE-0006-molded-inductors-and-frequency.md) | 候选规格和计算已核对；440 kHz损耗未实测 |
| NOTE-0007 | 2026-11-26 | 200 W双相交错Buck | [ISG3202与ISG3204、死区及引脚误判](projects/buck/NOTE-0007-gan-selection-and-deadtime.md) | 厂家真值表已核对；版图与实际开关波形待验证 |
| NOTE-0008 | 2026-11-26 | 200 W双相交错Buck | [辅助电源、GND/PGND及3.3 V电源并联](projects/buck/NOTE-0008-auxiliary-power-and-ground.md) | 名义计算与网表已核对；最差条件和回流待验证 |
| NOTE-0009 | 2026-11-26 | 200 W双相交错Buck | [分流器差分放大、GS8552供电与双向采样](projects/buck/NOTE-0009-shunt-differential-and-bidirectional.md) | 增益及错误网络已复算；线性/零点/温漂待实测 |
| NOTE-0010 | 2026-11-26 | 200 W双相交错Buck | [相电流采样：INA241、JSM霍尔、缩放与带宽](projects/buck/NOTE-0010-phase-current-hall-and-bandwidth.md) | 手册与比例已核对；纹波保真度和闭环带宽未实测 |
| NOTE-0011 | 2026-11-26 | 200 W双相交错Buck | [硬件过压过流：比较器、阈值与误差预算](projects/buck/NOTE-0011-comparator-ovp-ocp-and-tolerance.md) | 名义阈值和静态连接已核对；保护动态待测试 |
| NOTE-0012 | 2026-11-26 | 200 W双相交错Buck | [TZ网络名称、真实GPIO与两相硬件关断](projects/buck/NOTE-0012-dsp-trip-zone-routing.md) | 真实引脚功能已核对；固件与关断实测待完成 |
| NOTE-0013 | 2026-11-26 | 200 W双相交错Buck | [看似连通的电源标号、焊盘网名与原生验证](projects/buck/NOTE-0013-schematic-hotspots-and-net-evidence.md) | 静态证据及一次原理图修正已确认；原生ERC/DRC待执行 |
| NOTE-0014 | 2026-11-26 | 200 W双相交错Buck | [离散仿真、Mathcad与PPT的一致性](projects/buck/NOTE-0014-discrete-simulation-and-editable-calculations.md) | 已有模型/结果文件已核读；本次未重跑仿真或实板验证 |
| NOTE-0015 | 2026-11-26 | 200 W双相交错Buck | [制造一致性、历史修正与项目发布前检查](projects/buck/NOTE-0015-review-status-and-release-checklist.md) | 历史问题已归档；PCB同步及实板验证未全部关闭 |

## 按项目查阅

- [半桥 LLC / TMS320F28035](projects/llc/README.md)
- [UPS](projects/ups/README.md)

- [200 W双相交错Buck](projects/buck/README.md)

## 新增记录

复制 [问题记录模板](templates/problem-note.md)，放入 `projects/项目名称/`，然后更新本页和项目页的索引。

每条记录应包含：现象、工作条件、原因、处理方案、验证证据和资料来源。区分理论计算、手册确认、仿真、编译及实际硬件验证，不将尚未测试的方案标记为已解决。

技术正文采用 Markdown，可以直接在 GitHub 浏览器中阅读和编辑。新项目可建立自己的子目录，共用本页索引。

