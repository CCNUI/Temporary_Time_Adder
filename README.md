# Time Adder

A simple desktop application for Windows 11 that takes a time input in minutes and seconds (`mm:ss`) and displays the time after adding 20 seconds in `hh:mm:ss` format. The display updates in real-time as you type.

![Time Adder Screenshot](https://github.com/user-attachments/assets/872af2b5-dbe7-410b-95d5-8ce8b6616201)
![Time Adder Screenshot2](https://github.com/user-attachments/assets/9b90e64a-c6ed-4b36-a4e2-e27a37d439f4)

## ✨ Features

* **Real-time Updates**: The resulting time is recalculated and displayed instantly as you modify the input.
* **Simple Interface**: A clean and modern user interface with two input fields for minutes and seconds.
* **Modern Look**: Uses the `customtkinter` library for a contemporary Windows 11 style.

## ⚙️ Requirements

* Python 3.x
* `customtkinter`

## 🚀 How to Run

1.  **Clone the repository or download the files.**

2.  **Install the required library:**
    Open a terminal or command prompt and run:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    python main.py
    ```

4.  **How to Use:**
    * Enter the minutes in the left input box (`mm`).
    * Enter the seconds in the right input box (`ss`).
    * The time displayed below will automatically update, showing the input time plus 20 seconds in `hh:mm:ss` format.
