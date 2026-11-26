# 问答定位索引

[返回项目](README.md)

| 设计讨论中的问题 | 学习条目 |
| --- | --- |
| 交错Buck的拓扑、PWM和电感电流如何理解？ | [NOTE-0003 规格冻结、交错原理与电流应力](NOTE-0003-architecture-and-current-stress.md) |
| 15 μH怎么算？是否按双相减半？ | [NOTE-0004 每相感量计算、容差与峰值电流](NOTE-0004-inductance-and-worst-case.md) |
| EE22能否用？E25是否等于EE25/19？ | [NOTE-0005 AP法、EE磁芯、气隙与平面电感](NOTE-0005-ferrite-area-product-and-planar.md) |
| AP法、气隙和自然冷却电流密度怎么取？ | [NOTE-0005 AP法、EE磁芯、气隙与平面电感](NOTE-0005-ferrite-area-product-and-planar.md) |
| 平面变压器工艺能否做储能电感？ | [NOTE-0005 AP法、EE磁芯、气隙与平面电感](NOTE-0005-ferrite-area-product-and-planar.md) |
| 一体成型电感是否适合440 kHz？ | [NOTE-0006 一体成型电感与提高频率的体积收益](NOTE-0006-molded-inductors-and-frequency.md) |
| PSPMAA0805与FEXL1513A如何比较？ | [NOTE-0006 一体成型电感与提高频率的体积收益](NOTE-0006-molded-inductors-and-frequency.md) |
| 提高频率能否减小电感体积？ | [NOTE-0006 一体成型电感与提高频率的体积收益](NOTE-0006-molded-inductors-and-frequency.md) |
| ISG3202和3204有什么区别？ | [NOTE-0007 ISG3202与ISG3204、死区及引脚误判](NOTE-0007-gan-selection-and-deadtime.md) |
| 5 V源GND与GaN PGND怎样处理？ | [NOTE-0008 辅助电源、GND/PGND及3.3 V电源并联](NOTE-0008-auxiliary-power-and-ground.md) |
| PWM输入滤波电容应该接哪个地？ | [NOTE-0008 辅助电源、GND/PGND及3.3 V电源并联](NOTE-0008-auxiliary-power-and-ground.md) |
| GS8552用3.3 V还是5 V？ | [NOTE-0009 分流器差分放大、GS8552供电与双向采样](NOTE-0009-shunt-differential-and-bidirectional.md) |
| 10 mV/15 mV放大到ADC范围如何选电阻？ | [NOTE-0009 分流器差分放大、GS8552供电与双向采样](NOTE-0009-shunt-differential-and-bidirectional.md) |
| 单向放大器加负电源能否直接双向采样？ | [NOTE-0009 分流器差分放大、GS8552供电与双向采样](NOTE-0009-shunt-differential-and-bidirectional.md) |
| 双相电感电流除了隔离运放还能怎么采？ | [NOTE-0010 相电流采样：INA241、JSM霍尔、缩放与带宽](NOTE-0010-phase-current-hall-and-bandwidth.md) |
| 一个INA241是否只测一路？440 kHz能否看细节？ | [NOTE-0010 相电流采样：INA241、JSM霍尔、缩放与带宽](NOTE-0010-phase-current-hall-and-bandwidth.md) |
| ACS724-JSM如何接ADC和选择缩放电阻？ | [NOTE-0010 相电流采样：INA241、JSM霍尔、缩放与带宽](NOTE-0010-phase-current-hall-and-bandwidth.md) |
| 33k/10k与3.3k/1k哪个好？缩小倍数如何算？ | [NOTE-0010 相电流采样：INA241、JSM霍尔、缩放与带宽](NOTE-0010-phase-current-hall-and-bandwidth.md) |
| 最简单的输出OCP＋TZ3硬件方案是什么？ | [NOTE-0011 硬件过压过流：比较器、阈值与误差预算](NOTE-0011-comparator-ovp-ocp-and-tolerance.md) |
| LM393B加AND的OVP/OCP还有什么问题？ | [NOTE-0011 硬件过压过流：比较器、阈值与误差预算](NOTE-0011-comparator-ovp-ocp-and-tolerance.md) |
| TZ1接口为什么不一定能作硬件TZ？ | [NOTE-0012 TZ网络名称、真实GPIO与两相硬件关断](NOTE-0012-dsp-trip-zone-routing.md) |
| GPIO17/TZ3如何让两相四路全部锁低？ | [NOTE-0012 TZ网络名称、真实GPIO与两相硬件关断](NOTE-0012-dsp-trip-zone-routing.md) |
| 图上有3V3，为什么仍出现匿名电源网？ | [NOTE-0013 看似连通的电源标号、焊盘网名与原生验证](NOTE-0013-schematic-hotspots-and-net-evidence.md) |
| 如何做R2021b完整离散开闭环并更新波形？ | [NOTE-0014 离散仿真、Mathcad与PPT的一致性](NOTE-0014-discrete-simulation-and-editable-calculations.md) |
| Mathcad Prime9怎样保持公式可编辑？ | [NOTE-0014 离散仿真、Mathcad与PPT的一致性](NOTE-0014-discrete-simulation-and-editable-calculations.md) |
| PPT、计算和仿真如何随方案变化保持一致？ | [NOTE-0014 离散仿真、Mathcad与PPT的一致性](NOTE-0014-discrete-simulation-and-editable-calculations.md) |
| 外部铜排、端子封装、BOM和审查状态如何记录？ | [NOTE-0015 制造一致性、历史修正与项目发布前检查](NOTE-0015-review-status-and-release-checklist.md) |
| 还有哪些问题待关闭？是否已实测？ | [NOTE-0015 制造一致性、历史修正与项目发布前检查](NOTE-0015-review-status-and-release-checklist.md) |
