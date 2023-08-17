from textual.app import App, ComposeResult
from textual.widgets import MarkdownViewer

with open("./Hist/HIDDEN.md") as file:
    INTRO_MARKDOWN = file.read()

class MarkdownExampleApp(App):
    def compose(self) -> ComposeResult:
        yield MarkdownViewer(INTRO_MARKDOWN, show_table_of_contents=True)


if __name__ == "__main__":
    app = MarkdownExampleApp()
    app.run()
