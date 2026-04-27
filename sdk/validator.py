class DoctrineValidationError(ValueError):
    pass


class DoctrineValidator:
    REQUIRED_NODE_SECTIONS = ("Definition", "Usage", "Example", "ID")

    @classmethod
    def validate(cls, doctrine, strict_node=False):
        errors = []

        if not getattr(doctrine, "name", None):
            errors.append("missing name")

        if not getattr(doctrine, "id", None):
            errors.append("missing id")

        sections = getattr(doctrine, "sections", {}) or {}
        if not isinstance(sections, dict):
            errors.append("sections must be a dictionary")
            sections = {}

        if strict_node:
            for section in cls.REQUIRED_NODE_SECTIONS:
                if not sections.get(section):
                    errors.append("missing section: " + section)

        return errors

    @classmethod
    def assert_valid(cls, doctrine, strict_node=False):
        errors = cls.validate(doctrine, strict_node=strict_node)
        if errors:
            raise DoctrineValidationError("; ".join(errors))
