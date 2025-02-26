import re


def extract_markdown_images(text):
    matches = re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_title(markdown):
    match = re.match(r"^# .+", markdown)
    if match:
        return match.group().lstrip("# ")
    raise Exception("no title found")