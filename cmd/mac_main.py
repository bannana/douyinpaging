# -*- coding:utf-8 -*-
# @Time   : 2026-01-17
# @Author : bannana
# @Ori_Author : cniu6 (zerohh)
# @GitHub : https://github.com/bannana/douyinpaging
from pynput import keyboard
import time

control = keyboard.Controller()

# 状态追踪
is_shift_down = False
h_triggered = False  # 防止长按连续触发


def on_press(key):
    global is_shift_down, h_triggered

    # 记录 Shift 状态
    if key in [keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r]:
        is_shift_down = True

    # 在按下阶段检测 Shift + F5
    if key == keyboard.Key.f5 and is_shift_down:
        if not h_triggered:
            print("检测到 Shift + F5 按下 -> 映射为 H")
            control.press('h')
            control.release('h')
            h_triggered = True  # 标记已触发，防止连发


def on_release(key):
    global is_shift_down, h_triggered

    # 打印释放记录方便调试
    print(f"释放: {key}")

    # 1. PageUp -> 模拟方向上键 (保持 0.4s 延迟)
    if key == keyboard.Key.page_up:
        time.sleep(0.4)
        control.press(keyboard.Key.up)
        control.release(keyboard.Key.up)

    # 2. PageDown -> 模拟方向下键 (保持 0.4s 延迟)
    elif key == keyboard.Key.page_down:
        time.sleep(0.4)
        control.press(keyboard.Key.down)
        control.release(keyboard.Key.down)

    # 3. B 键 -> 模拟 Cmd + Q 并退出程序
    elif hasattr(key, 'char') and key.char is not None and key.char.lower() == 'b':
        print("执行 Cmd + Q 退出并关闭脚本...")
        with control.pressed(keyboard.Key.cmd):
            control.press('q')
            control.release('q')
        return False  # 停止监听器

    # 4. Esc 键
    elif key == keyboard.Key.esc:
        print("Esc 释放")

    # 5. 重置 Shift 和 F5 的触发状态
    if key in [keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r]:
        is_shift_down = False
    if key == keyboard.Key.f5:
        h_triggered = False


if __name__ == '__main__':
    print("=====================================")
    print("抖音翻页笔映射程序 Based on MacOS")
    print("""
    ╔══════════════════════════════════╗
    ║  AppName v1.1                    ║
    ║  by: bannana                     ║
    ║  build: 2026-01-17@13:19:15      ║
    ║  repo:https://github.com/bannana ║
    ╚══════════════════════════════════╝
    """)
    print("1. PageUp/Down -> 方向键 (0.4s 延迟)")
    print("2. 长按下键 (B) -> Cmd + Q 退出")
    print("3. 长按上键 (Shift+F5) -> H 键")
    print("4. 长按上键 (Esc) -> 保持 Esc 功能")
    print("=====================================")

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

