# Lumenflow

一个用于相机图传（视频采集与传输）场景的 Python 项目骨架。
当前版本重点是把模块边界和基础流程先搭好，便于后续接入真实摄像头、编码器、网络传输与前端控制端。

## 当前能力

- 提供统一入口：`main.py`
- 提供基础模块骨架：
  - 相机控制（`core/camera_controller.py`）
  - 文件管理（`core/file_manager.py`）
  - API 服务（`server/api_server.py`）
  - 状态/媒体路由（`server/routes_status.py`, `server/routes_media.py`）
  - 存储索引（`storage/*`）
  - 网络与硬件占位层（`network/*`, `hardware/*`）
- 已补充必要注释与文档字符串，便于二次开发

## 项目结构

```text
lumenflow/
├── boot.py
├── main.py
├── config/                # 配置模型（相机/网络/系统）
├── core/                  # 核心流程（采集、处理、文件）
├── hardware/              # 硬件抽象层（GPIO、电源）
├── network/               # 网络抽象层（Wi-Fi、热点）
├── server/                # API 与 WebSocket 服务层
├── storage/               # 元数据存储与仓储
├── utils/                 # 通用工具（日志、时间、系统信息）
└── README.md
```

## 快速开始

### 1) 环境要求

- Python 3.11+

### 2) 运行

```bash
python main.py
```

启动后你会看到类似输出：

```text
=== LUMENFLOW SYSTEM START ===
[CameraController] Camera 0 initialized
[FileManager] File system ready
[APIServer] Listening on 0.0.0.0:8080
=== SYSTEM RUNNING ===
```
## Analysis Log（梳理日志）

- 2026-04-21
  - 目标：对仓库进行“全面梳理 → 知识点清单 → 分阶段学习路径”整理，输出可执行的学习路线与上手指南。
  - 已开始：发起全面梳理分析任务（状态：queued）。
  - 任务链接：https://github.com/yunmin311/lumenflow/tasks/af8c5317-bbdf-4a83-af44-334b124ad336
  - 下一步：
    1) 盘点仓库结构（顶层目录/文件用途）
    2) 定位运行入口（CLI / main / Web 服务入口等）
    3) 梳理依赖与环境管理方式（requirements / pyproject 等）并给出最短运行路径
    4) 识别核心模块边界与典型执行流程（调用链 & 数据流）
    5) 汇总“仓库实际涉及”的知识点清单，并拆分成 3-5 阶段学习路径（每阶段：必读文件+练习）

## 下一步建议

1. 在 `CameraController` 中接入真实摄像头 SDK 或 OpenCV 采集。
2. 在 `VideoProcessor` 中接入编码/转码流程（H264/H265）。
3. 在 `APIServer` 中替换为真实 Web 框架（如 FastAPI/Flask）。
4. 在 `WebSocketServer` 中实现实时帧推送。
5. 在 `storage` 中替换为 SQLite/PostgreSQL 等持久化存储。

## 说明

当前实现为可运行框架，不包含重型依赖，适合作为图传系统的二次开发起点。
