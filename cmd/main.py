from pynput import keyboard
import time
import sys

control = keyboard.Controller()

# 状态追踪
is_shift_down = False
h_triggered = False


def on_press(key):
    global is_shift_down, h_triggered
    # 记录 Shift 状态
    if key in [keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r]:
        is_shift_down = True

    # 捕获 Shift + F5 映射为 H (全屏)
    if key == keyboard.Key.f5 and is_shift_down:
        if not h_triggered:
            print("[LOG] 检测到 Shift+F5 -> 映射为 H")
            control.press('h')
            control.release('h')
            h_triggered = True


def on_release(key):
    global is_shift_down, h_triggered

    # 1. PageUp -> 向上键 (0.5s 延迟)
    if key == keyboard.Key.page_up:
        time.sleep(0.5)
        control.press(keyboard.Key.up)
        control.release(keyboard.Key.up)
        print("[LOG] PageUp -> 模拟方向上键")

    # 2. PageDown -> 向下键 (0.5s 延迟)
    elif key == keyboard.Key.page_down:
        time.sleep(0.5)
        control.press(keyboard.Key.down)
        control.release(keyboard.Key.down)
        print("[LOG] PageDown -> 模拟方向下键")

    # 3. B 键 -> 模拟 Alt + F4 (关闭当前窗口) 并退出脚本
    elif hasattr(key, 'char') and key.char is not None and key.char.lower() == 'b':
        print("[LOG] 检测到 B -> 执行 Alt+F4 并退出程序")
        with control.pressed(keyboard.Key.alt):
            control.press(keyboard.Key.f4)
            control.release(keyboard.Key.f4)
        sys.exit(0)

        # 4. Esc 键
    elif key == keyboard.Key.esc:
        print("[LOG] 检测到 Esc (保持默认行为)")

    # 状态重置
    if key in [keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r]:
        is_shift_down = False
    if key == keyboard.Key.f5:
        h_triggered = False


if __name__ == '__main__':
    print("=====================================")
    print("抖音翻页笔映射程序 Based on Windows")
    print("""
        ╔══════════════════════════════════╗
        ║  AppName v1.1                    ║
        ║  by: bannana                     ║
        ║  build: 2026-01-17@13:19:15      ║
        ║  repo:https://github.com/bannana ║
        ╚══════════════════════════════════╝
        """)
    print("1. PageUp/Down -> 方向键 (0.5s 延迟)")
    print("2. 长按下键 (B) -> Alt + F4 退出")
    print("3. 长按上键 (Shift+F5) -> H 键")
    print("4. 长按上键 (Esc) -> 保持 Esc 功能")
    print("=====================================")

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()