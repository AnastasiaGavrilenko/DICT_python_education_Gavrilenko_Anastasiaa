# simplified_markdown_editor.py

class MarkdownEditor:
    def __init__(self):
        self.markdown_text = ""

    def show_help(self):
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        print("Special commands: !help !done")

    def format_plain(self, text):
        return text

    def format_header(self, text, level):
        return f"{'#' * level} {text}\n"

    def format_link(self, label, url):
        return f"[{label}]({url})"

    def format_list(self, rows, ordered=True):
        return '\n'.join([f"{i}. {row}" if ordered else f"* {row}" for i, row in enumerate(rows, start=1)])

    def apply_formatter(self, formatter):
        if formatter == "header":
            level = int(input("Level: > "))
            if 1 <= level <= 6:
                text = input("Text: > ")
                formatted_text = self.format_header(text, level)
                self.markdown_text += formatted_text
                print(self.markdown_text)
            else:
                print("The level should be within the range of 1 to 6.")
        elif formatter == "link":
            label = input("Label: > ")
            url = input("URL: > ")
            formatted_text = self.format_link(label, url)
            self.markdown_text += formatted_text
            print(self.markdown_text)
        elif formatter == "ordered-list" or formatter == "unordered-list":
            num_rows = int(input("Number of rows: > "))
            if num_rows > 0:
                rows = [input(f"Row #{i + 1}: > ") for i in range(num_rows)]
                formatted_text = self.format_list(rows, formatter == "ordered-list")
                self.markdown_text += formatted_text
                print(self.markdown_text)
            else:
                print("The number of rows should be greater than zero.")
        else:
            text = input("Text: > ")
            formatted_text = getattr(self, f"format_{formatter}")(text)
            self.markdown_text += formatted_text
            print(self.markdown_text)

    def save_to_file(self):
        with open("output.md", "w") as file:
            file.write(self.markdown_text)

    def run_editor(self):
        self.show_help()

        while True:
            user_input = input("Choose a formatter: > ")

            if user_input.startswith("!"):
                if user_input == "!help":
                    self.show_help()
                elif user_input == "!done":
                    print("Exiting the program. Markdown saved.")
                    self.save_to_file()
                    break
                else:
                    print("Unknown command")
            elif hasattr(self, f"format_{user_input}") or user_input in ["ordered-list", "unordered-list"]:
                self.apply_formatter(user_input)
            else:
                print("Unknown formatting type or command")


if __name__ == "__main__":
    editor = MarkdownEditor()
    editor.run_editor()
