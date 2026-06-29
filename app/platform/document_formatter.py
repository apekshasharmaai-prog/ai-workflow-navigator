class DocumentFormatter:
    """
    Converts structured JSON documents into
    readable enterprise documents suitable for
    chunking and semantic search.
    """

    ABBREVIATIONS = {
        "Sla": "SLA",
        "Api": "API",
        "Apis": "APIs",
        "Id": "ID",
        "Ids": "IDs",
        "Url": "URL",
        "Urls": "URLs",
        "Ui": "UI",
        "Ai": "AI",
        "Faq": "FAQ",
        "Rag": "RAG",
        "Llm": "LLM"
    }

    @classmethod
    def format(cls, document) -> str:

        lines = []

        cls._format(
            value=document,
            lines=lines,
            level=0
        )

        return "\n".join(lines)

    @classmethod
    def _format(
        cls,
        value,
        lines,
        level
    ):

        indent = "  " * level

        if isinstance(value, dict):

            for key, val in value.items():

                key = cls._prettify(key)

                if isinstance(val, (dict, list)):

                    lines.append(f"{indent}{key}:")

                    cls._format(
                        val,
                        lines,
                        level + 1
                    )

                else:

                    lines.append(
                        f"{indent}{key}: {val}"
                    )

        elif isinstance(value, list):

            for item in value:

                if isinstance(item, (dict, list)):

                    cls._format(
                        item,
                        lines,
                        level
                    )

                    lines.append("")

                else:

                    lines.append(
                        f"{indent}- {item}"
                    )

        else:

            lines.append(
                f"{indent}{value}"
            )

    @classmethod
    def _prettify(
        cls,
        text
    ) -> str:

        text = text.replace(
            "_",
            " "
        ).strip()

        text = text.title()

        for old, new in cls.ABBREVIATIONS.items():

            text = text.replace(
                old,
                new
            )

        return text