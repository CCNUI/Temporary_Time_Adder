import tkinter as tk
import customtkinter as ctk
from datetime import datetime, timedelta

class TimeAdderApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Time Adder")
        self.geometry("400x250")
        self.resizable(False, False)

        # 设置UI主题
        ctk.set_appearance_mode("System")  # 也可以是 "Dark" 或 "Light"
        ctk.set_default_color_theme("blue")

        # 创建主框架
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # --- 输入部分 ---
        input_frame = ctk.CTkFrame(main_frame)
        input_frame.pack(pady=10)

        self.minutes_entry = ctk.CTkEntry(input_frame, width=60, justify="center", font=("", 16))
        self.minutes_entry.pack(side="left", padx=(10, 0))
        self.minutes_entry.insert(0, "mm")

        colon_label = ctk.CTkLabel(input_frame, text=":", font=("", 20))
        colon_label.pack(side="left", padx=5)

        self.seconds_entry = ctk.CTkEntry(input_frame, width=60, justify="center", font=("", 16))
        self.seconds_entry.pack(side="left", padx=(0, 10))
        self.seconds_entry.insert(0, "ss")

        # 绑定事件处理
        self.minutes_entry.bind("<KeyRelease>", self.update_time)
        self.seconds_entry.bind("<KeyRelease>", self.update_time)
        self.minutes_entry.bind("<FocusIn>", self.clear_placeholder)
        self.seconds_entry.bind("<FocusIn>", self.clear_placeholder)
        self.minutes_entry.bind("<FocusOut>", lambda event, entry=self.minutes_entry, placeholder="mm": self.restore_placeholder(event, entry, placeholder))
        self.seconds_entry.bind("<FocusOut>", lambda event, entry=self.seconds_entry, placeholder="ss": self.restore_placeholder(event, entry, placeholder))


        # --- 输出部分 ---
        self.result_label = ctk.CTkLabel(main_frame, text="hh:mm:ss", font=("", 36, "bold"))
        self.result_label.pack(pady=20)

    def clear_placeholder(self, event):
        """当用户点击输入框时，清除占位符"""
        if event.widget.get() in ["mm", "ss"]:
            event.widget.delete(0, "end")

    def restore_placeholder(self, event, entry, placeholder):
        """如果输入框为空，恢复占位符"""
        if not entry.get():
            entry.insert(0, placeholder)

    def update_time(self, event=None):
        """实时计算并更新时间"""
        try:
            minutes_str = self.minutes_entry.get()
            seconds_str = self.seconds_entry.get()

            # 如果输入为空或为占位符，则不进行计算
            if not minutes_str or minutes_str == "mm":
                minutes = 0
            else:
                minutes = int(minutes_str)

            if not seconds_str or seconds_str == "ss":
                seconds = 0
            else:
                seconds = int(seconds_str)

            # 创建一个基于0点的初始时间
            initial_time = datetime.strptime("00:00:00", "%H:%M:%S")

            # 加上用户输入的时间和额外的20秒
            delta = timedelta(minutes=minutes, seconds=seconds + 20)
            new_time = initial_time + delta

            # 格式化并显示新时间
            self.result_label.configure(text=new_time.strftime("%H:%M:%S"))

        except (ValueError, TypeError):
            # 如果输入无效，则显示错误或默认值
            self.result_label.configure(text="无效输入")

if __name__ == "__main__":
    app = TimeAdderApp()
    app.mainloop()