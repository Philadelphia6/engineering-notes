# 200 W双相交错同步Buck：问题与学习记录

设计基准：28～32 V输入、18～25 V可调输出、200 W额定/约220 W设计上限、两只独立电感、每相目标15 μH、约440 kHz、TMS320F28035。

更新日期：2026-11-26（Asia/Shanghai）。这里归档设计讨论、计算、静态发现和方法，不将待验证建议写成实测结论。不包含完整原理图、固件、模型或第三方手册原件。

## 阅读顺序

先看架构与应力→感量与磁件→驱动/供电→采样→保护/TZ→CAD与制造一致性。每条均按问题、原因、方案、验证、经验和资料组织。

| 编号 | 专题 | 验证边界 |
| --- | --- | --- |
| NOTE-0003 | [规格冻结、交错原理与电流应力](NOTE-0003-architecture-and-current-stress.md) | 理论计算已整理；硬件效率和温升待验证 |
| NOTE-0004 | [每相感量计算、容差与峰值电流](NOTE-0004-inductance-and-worst-case.md) | 公式及数值已复算；磁件偏置和温升待实测 |
| NOTE-0005 | [AP法、EE磁芯、气隙与平面电感](NOTE-0005-ferrite-area-product-and-planar.md) | 计算方法已整理；尚未冻结磁芯厂家和实物规格 |
| NOTE-0006 | [一体成型电感与提高频率的体积收益](NOTE-0006-molded-inductors-and-frequency.md) | 候选规格和计算已核对；440 kHz损耗未实测 |
| NOTE-0007 | [ISG3202与ISG3204、死区及引脚误判](NOTE-0007-gan-selection-and-deadtime.md) | 厂家真值表已核对；版图与实际开关波形待验证 |
| NOTE-0008 | [辅助电源、GND/PGND及3.3 V电源并联](NOTE-0008-auxiliary-power-and-ground.md) | 名义计算与网表已核对；最差条件和回流待验证 |
| NOTE-0009 | [分流器差分放大、GS8552供电与双向采样](NOTE-0009-shunt-differential-and-bidirectional.md) | 增益及错误网络已复算；线性/零点/温漂待实测 |
| NOTE-0010 | [相电流采样：INA241、JSM霍尔、缩放与带宽](NOTE-0010-phase-current-hall-and-bandwidth.md) | 手册与比例已核对；纹波保真度和闭环带宽未实测 |
| NOTE-0011 | [硬件过压过流：比较器、阈值与误差预算](NOTE-0011-comparator-ovp-ocp-and-tolerance.md) | 名义阈值和静态连接已核对；保护动态待测试 |
| NOTE-0012 | [TZ网络名称、真实GPIO与两相硬件关断](NOTE-0012-dsp-trip-zone-routing.md) | 真实引脚功能已核对；固件与关断实测待完成 |
| NOTE-0013 | [看似连通的电源标号、焊盘网名与原生验证](NOTE-0013-schematic-hotspots-and-net-evidence.md) | 静态证据及一次原理图修正已确认；原生ERC/DRC待执行 |
| NOTE-0014 | [离散仿真、Mathcad与PPT的一致性](NOTE-0014-discrete-simulation-and-editable-calculations.md) | 已有模型/结果文件已核读；本次未重跑仿真或实板验证 |
| NOTE-0015 | [制造一致性、历史修正与项目发布前检查](NOTE-0015-review-status-and-release-checklist.md) | 历史问题已归档；PCB同步及实板验证未全部关闭 |

## 最容易继续误用的结论

1. 每相L按每相fs算，不因交错就直接减半；正常峰值约6.71 A，计假设偏差约7.47 A，故障另算。
2. EE22/E25外形名、25.5 A商城标题和AP初筛都不能替代完整磁件验证。
3. INA241的1.1 MHz小信号带宽不能证明440 kHz开关共模下的PWM抑制能力。
4. 霍尔分压的1 kΩ/1.8 kΩ初步建议已撤回；按JSM负载要求改用10 kΩ/18 kΩ等组合。
5. 当前可用霍尔0.33倍和推荐0.643倍是两种方案，不能混用软件比例。
6. LM393B的工作电源、共模范围、开集上拉和ADC电源轨分别核对。
7. TZ1/TZ3网名不等于实际GPIO功能；当前示例TZ3走GPIO17。
8. 原理图已改不代表PCB、BOM或实物已同步；未完成硬件测试就不记“保护已通过”。

## 复算与状态

- [轻量复算脚本](tools/recalculate.py)：仅用Python标准库，可计算关键感量、门限、带宽估计和公差示例。
- [项目问题状态](review-status.csv)：保留最后一次静态复核的边界。
- [问答索引](question-map.md)：按当时提出的问题定位专题。
- [已有共模基础笔记](../llc/NOTE-0001-common-mode-and-power-rails.md)。

原创SVG中的波形是解析示意，其余为通用原理图；均不作为实测证据。厂商资料版本变化后应重新核对具体料号与适用条件。
