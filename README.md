# 项目问题与学习笔记

记录各项目中的问题、原因、解决方案和验证结果，便于后续查阅与复用。

## 问题索引

| 编号 | 日期 | 项目 | 问题 | 状态 |
| --- | --- | --- | --- | --- |
| NOTE-0001 | 2026-11-07 | 半桥 LLC / TMS320F28035 | [比较器和运放的供电、输入共模范围与输出电源轨](projects/llc/NOTE-0001-common-mode-and-power-rails.md) | 数据手册已核对；方案待硬件验证 |
| NOTE-0002 | 2026-11-07 | UPS / U.PSDR.L.CT3K C25285 | [UPS学习记录：共用桥臂、采样偏置、启动跌落及设计学习点](projects/ups/NOTE-0002-ups-learning-record.md) | 原理及部分实测已确认；其余待验证 |

## 按项目查阅

- [半桥 LLC / TMS320F28035](projects/llc/README.md)
- [UPS](projects/ups/README.md)

## 新增记录

复制 [问题记录模板](templates/problem-note.md)，放入 `projects/项目名称/`，然后更新本页和项目页的索引。

每条记录应包含：现象、工作条件、原因、处理方案、验证证据和资料来源。区分理论计算、手册确认、仿真、编译及实际硬件验证，不将尚未测试的方案标记为已解决。

技术正文采用 Markdown，可以直接在 GitHub 浏览器中阅读和编辑。新项目可建立自己的子目录，共用本页索引。
