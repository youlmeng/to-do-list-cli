<h1 align="center">to-do-list-cli <img src="https://img.shields.io/github/stars/youlmeng/to-do-list-cli?label=Stars" alt="stars"></h1>

# to-do-list-cli
待办事项（To-Do List）管理程序。它是一个命令行程序，允许用户添加、查看、删除和标记待办事项。

### 功能：
- 添加待办事项
- 查看所有待办事项
- 删除待办事项
- 标记待办事项为已完成

### 运行说明：
- 添加任务：选择选项 1 后输入任务内容，它会被添加到待办事项列表中。
- 查看任务：选择选项 2，会列出所有待办事项，显示每个任务的状态（✔ 表示已完成，✘ 表示未完成）。
- 删除任务：选择选项 3 后输入任务 ID 来删除任务。
- 标记任务为已完成：选择选项 4 后输入任务 ID 来标记任务为已完成。
- 退出程序：选择选项 5 来退出。

### 解释：
- 任务类 (Todo)：包含任务名称和是否完成的状态。mark_as_completed 方法将任务标记为已完成。
- 待办事项列表类 (TodoList)：包含一个任务列表，并提供添加、删除、列出和标记任务的方法。
- 主程序：提供一个命令行菜单，用户可以根据选项操作任务。

### 改进方向：
- 使用 JSON 或 SQLite 存储任务，以便在程序重启时保留任务数据。
- 添加 日期 或 优先级 功能，帮助用户更好地管理任务。
- 制作图形用户界面（GUI）版本，提升用户体验。

<h1 align="center">Awesome Cloudflare <img src="https://img.shields.io/github/stars/zhuima/awesome-cloudflare?label=Stars" alt="stars"></h1>
