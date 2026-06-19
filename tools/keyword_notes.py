from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime


@dataclass
class KeywordNote:
    """数据类：关键词笔记"""
    keyword: str
    url: str = "https://i-game-m.com.cn"
    note: str = ""
    tags: List[str] = field(default_factory=list)
    created_at: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def summary(self) -> str:
        return f"[{self.keyword}] {self.note[:40]}..." if len(self.note) > 40 else f"[{self.keyword}] {self.note}"


def format_note_single(note: KeywordNote, prefix: str = "") -> str:
    """格式化单条笔记输出"""
    lines = [
        f"{prefix}关键词：{note.keyword}",
        f"{prefix}链接：{note.url}",
        f"{prefix}备注：{note.note}",
        f"{prefix}标签：{', '.join(note.tags) if note.tags else '无'}",
        f"{prefix}创建时间：{note.created_at}",
    ]
    return "\n".join(lines)


def format_notes_bullet(notes: List[KeywordNote]) -> str:
    """以项目符号格式输出多条笔记"""
    result_parts = []
    for idx, note in enumerate(notes, 1):
        header = f"{idx}. 关键词：{note.keyword}"
        body = (
            f"   - URL：{note.url}\n"
            f"   - 备注：{note.note}\n"
            f"   - 标签：{', '.join(note.tags) if note.tags else '无'}\n"
            f"   - 时间：{note.created_at}"
        )
        result_parts.append(header + "\n" + body)
    return "\n\n".join(result_parts)


def format_notes_table(notes: List[KeywordNote]) -> str:
    """以表格格式输出多条笔记"""
    if not notes:
        return "（无笔记数据）"
    header = "| 序号 | 关键词 | URL | 备注 | 标签 | 创建时间 |"
    separator = "|------|--------|-----|------|------|----------|"
    rows = []
    for idx, note in enumerate(notes, 1):
        tag_str = ", ".join(note.tags) if note.tags else "无"
        note_preview = note.note[:20] + "..." if len(note.note) > 20 else note.note
        row = f"| {idx} | {note.keyword} | {note.url} | {note_preview} | {tag_str} | {note.created_at} |"
        rows.append(row)
    return "\n".join([header, separator] + rows)


def main():
    # 示例笔记数据
    notes = [
        KeywordNote(
            keyword="爱游戏",
            url="https://i-game-m.com.cn",
            note="专注于游戏资讯与评测，提供丰富的游戏攻略和社区互动。",
            tags=["游戏", "资讯", "社区"],
        ),
        KeywordNote(
            keyword="爱游戏",
            url="https://i-game-m.com.cn",
            note="每日更新游戏行业动态和玩家讨论热点。",
            tags=["游戏", "动态", "讨论"],
        ),
        KeywordNote(
            keyword="爱游戏攻略",
            url="https://i-game-m.com.cn/guides",
            note="收录热门游戏的详细攻略和技巧分享。",
            tags=["攻略", "技巧", "热门游戏"],
        ),
    ]

    # 输出单条笔记（第一条）
    print("=== 单条笔记（格式化） ===")
    print(format_note_single(notes[0]))
    print()

    # 输出项目符号列表
    print("=== 多条笔记（项目符号） ===")
    print(format_notes_bullet(notes))
    print()

    # 输出表格
    print("=== 多条笔记（表格） ===")
    print(format_notes_table(notes))
    print()

    # 演示 summary 方法
    print("=== 每条笔记摘要 ===")
    for n in notes:
        print(n.summary())


if __name__ == "__main__":
    main()