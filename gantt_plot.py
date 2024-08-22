import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# 定义任务
a_tasks = [
    {"name": "Task A1", "start": datetime(2023, 4, 1), "end": datetime(2023, 12, 31)},
    {"name": "Task A2", "start": datetime(2023, 6, 1), "end": datetime(2023, 8, 31)},
    {"name": "Task A3", "start": datetime(2023, 8, 1), "end": datetime(2023, 10, 31)},
    {"name": "Task A4", "start": datetime(2023, 10, 1), "end": datetime(2023, 12, 31)},
]
b_tasks = [
    {"name": "Task B1", "start": datetime(2023, 8, 1), "end": datetime(2024, 11, 30)},
    {"name": "Task B2", "start": datetime(2023, 12, 1), "end": datetime(2024, 3, 31)},
    {"name": "Task B3", "start": datetime(2024, 4, 1), "end": datetime(2024, 12, 31)},
    {"name": "Task B4", "start": datetime(2024, 8, 1), "end": datetime(2025, 3, 31)},
]
c_tasks = [
    {"name": "Task C1", "start": datetime(2025, 1, 1), "end": datetime(2025, 12, 31)},
    {"name": "Task C2", "start": datetime(2025, 4, 1), "end": datetime(2026, 3, 31)},
    {"name": "Task C3", "start": datetime(2026, 1, 1), "end": datetime(2026, 9, 30)},
    {"name": "Task C4", "start": datetime(2026, 4, 1), "end": datetime(2026, 12, 31)},
]
d_tasks = [
    {"name": "Task D1", "start": datetime(2026, 4, 1), "end": datetime(2026, 10, 31)},
    {"name": "Task D2", "start": datetime(2026, 6, 1), "end": datetime(2026, 12, 31)},
    {"name": "Task D3", "start": datetime(2026, 12, 1), "end": datetime(2027, 1, 31)},
    {"name": "Task D4", "start": datetime(2027, 2, 1), "end": datetime(2027, 3, 31)},
]


# 重要日期
important_dates = [
    {"name": "Year 0",  "date": datetime(2023, 4, 1)},
    {"name": "Year 1",  "date": datetime(2024, 4, 1)},
    {"name": "Year 2",  "date": datetime(2025, 4, 1)},
    {"name": "Year 3",  "date": datetime(2026, 4, 1)},
    {"name": "Year 4",  "date": datetime(2027, 4, 1)},
]

# 颜色映射
colors = {
    "a": "tab:blue",
    "b": "tab:orange",
    "c": "tab:red",
    "d": "tab:purple",
}

# 合并所有任务并记录分段长度
task_groups = [
    (a_tasks, colors["a"]),
    (b_tasks, colors["b"]),
    (c_tasks, colors["c"]),
    (d_tasks, colors["d"]),
]

all_tasks = []
section_lines = []

current_position = 0
for tasks, color in task_groups:
    all_tasks.extend([(t["name"], t["start"], t["end"], color) for t in tasks])
    current_position += len(tasks)
    section_lines.append(current_position - 0.5)

# 反转任务顺序
all_tasks.reverse()

# 创建图形
fig, ax = plt.subplots(figsize=(12, 8))

# 启用网格并设置zorder
ax.grid(True, which='both', linestyle='--', linewidth=0.5, zorder=1)

# 绘制甘特图
for i, (name, start, end, color) in enumerate(all_tasks):
    ax.broken_barh([(start, end - start)], (i - 0.4, 0.8), facecolors=color, zorder=2)

# 添加虚线分割线
for line_position in section_lines[:-1]:
    ax.axhline(y=len(all_tasks) - line_position - 1, color='black', linewidth=0.8, linestyle='--', zorder=3)

# 添加重要日期竖线和标注
for date in important_dates:
    ax.axvline(x=date["date"], color='black', linewidth=1, linestyle='--', zorder=4)
    ax.text(date["date"], len(all_tasks) - 0.5, date["name"], rotation=0, verticalalignment='bottom', horizontalalignment='right', zorder=5)

# 设置轴标签和标题
ax.set_yticks(range(len(all_tasks)))
ax.set_yticklabels([task[0] for task in all_tasks])
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.xticks(rotation=45)
ax.set_title('Research Plan')

plt.tight_layout()
plt.savefig("gan.png")