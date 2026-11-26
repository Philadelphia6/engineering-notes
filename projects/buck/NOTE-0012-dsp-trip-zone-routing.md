# NOTE-0012：TZ网络名称、真实GPIO与两相硬件关断

[全部问题](../../README.md) · [Buck项目索引](README.md)

| 项目 | 内容 |
| --- | --- |
| 创建 / 更新日期 | 2026-11-26（Asia/Shanghai） |
| 所属项目 | 200 W双相交错同步Buck |
| 关键词 | F28035、GPIO17/TZ3、OST、异步输入 |
| 状态 | 真实引脚功能已核对；固件与关断实测待完成 |

## 问题现象

接口叫“TZ1”并不证明它接到DSP的TZ1输入。一次跟踪发现该网实际去GPIO42/COMP1OUT；后续改用支持TZ3的GPIO17。只改网络名字、只启中断或只关一相都不能形成预期的两相硬件保护。

## 原因分析

按TMS320F28035的80脚PN封装：

| GPIO | 物理引脚 | 相关复用 |
| --- | --- | --- |
| GPIO42 | 5 | COMP1OUT输出，没有TZ1输入 |
| GPIO12 | 47 | TZ1，可与串口等用途冲突 |
| GPIO15 | 75 | TZ1，需检查板上原有下拉/电容 |
| GPIO17 | 42 | TZ3，GPAMUX2选择3 |
| GPIO29 | 34 | TZ3，另一可选路径，常与I²C/串口用途冲突 |

这些物理引脚号只适用于80脚PN，其他封装应重查。GPIO17和GPIO29都能作TZ3，不表示软件配置可互换；当前走哪根线，就必须配置哪一脚。

## 解决方案

以下仅是关键配置示例，依赖F2803x寄存器头文件，不是完整初始化/复位流程：

```c
EALLOW;
GpioCtrlRegs.GPAMUX2.bit.GPIO17 = 3; // TZ3
GpioCtrlRegs.GPAQSEL2.bit.GPIO17 = 3; // asynchronous

EPwm1Regs.TZSEL.bit.OSHT3 = 1;
EPwm2Regs.TZSEL.bit.OSHT3 = 1;
EPwm1Regs.TZCTL.bit.TZA = 2; // force low
EPwm1Regs.TZCTL.bit.TZB = 2;
EPwm2Regs.TZCTL.bit.TZA = 2;
EPwm2Regs.TZCTL.bit.TZB = 2;
EDIS;
```

先保持四路PWM关闭，等采样/参考/保护供电稳定、引脚与Trip配置完成，才受控放行。OST提供硬件锁存，不等待CPU执行中断才关波；中断用于记录/显示，故障仍在时不能无条件清除OST。CBC会按周期自动恢复，不能把它和短路锁存停机混为一谈。

检查PWM后的非反相缓冲、极性和实际GaN输入，确认“两相A/B均低”而不是逻辑高、Hi-Z或只关上管。芯片3202的H/H会直通，因此动作选择必须明确。

## 验证结果

- [x] 厂家引脚表和实际接口到焊盘映射已静态交叉核对。
- [ ] 未提供固件，示例未在目标固件中编译验证。
- [ ] 需依次验证软件强制OST、外部TZ引脚、模拟门限触发三段链路。
- [ ] 软件强制OST通过只证明后半链路，不能代替比较器/外部引脚测试。

## 经验与复用条件

网络命名、符号功能、封装引脚和硅片复用是四层信息。一个GPIO可由软件读入，不表示能任意映射成硬件TZ。不要套用其他C2000系列带INPUT X-BAR的能力，除非目标器件手册明确支持。

## 参考资料

- [TI：F28035官方数据手册，引脚及GPIO复用](https://www.ti.com/lit/ds/symlink/tms320f28035.pdf)
- [TI：F2803x TRM，ePWM Trip Zone](https://www.ti.com/lit/ug/sprui10a/sprui10a.pdf)
