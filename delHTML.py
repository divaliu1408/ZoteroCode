% 将target_director 替换为你的storage路径
% 本代码设置成可以人工验证，每个html会打开以下，然后判断是否删除。

import os
import webbrowser


def delete_html_files(directory):
    """
    遍历指定文件夹及其子文件夹中的所有 .html 文件，
    每发现一个文件时，打开它并询问用户是否删除。

    :param directory: 要操作的文件夹路径
    """
    print(f"Starting scan in directory: {directory}")
    if not os.path.exists(directory):
        print(f"Directory does not exist: {directory}")
        return

    for root, dirs, files in os.walk(directory):
        print(f"Scanning folder: {root}")
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                print(f"Found HTML file: {file_path}")

                # 尝试打开 HTML 文件
                try:
                    webbrowser.open(f"file://{file_path}")
                    print("Opened file in default browser.")
                except Exception as e:
                    print(f"Error opening file: {file_path}. {e}")

                # 询问用户是否删除
                while True:
                    user_input = input(f"Do you want to delete this file? (y/n): ").strip().lower()
                    if user_input == 'y':
                        try:
                            os.remove(file_path)
                            print(f"Deleted: {file_path}")
                        except Exception as e:
                            print(f"Error deleting {file_path}: {e}")
                        break
                    elif user_input == 'n':
                        print(f"Skipped: {file_path}")
                        break
                    else:
                        print("Invalid input. Please enter 'y' to delete or 'n' to skip.")


if __name__ == "__main__":

    target_directory = r"...\storage" # 替换为你的目标目录路径
    print(f"Target directory: {target_directory}")
    delete_html_files(target_directory)
