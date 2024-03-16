from pydantic import BaseModel, Field, validator  # Pydantic model / Schemas
from typing import Optional, List, Dict, Union
from enum import Enum


class ComponentType(str, Enum):
    IMPORT = "import"
    SHADOW = "shadow"
    CROP = "crop"
    EXPORT = "export"


class ComponentSettings(BaseModel):
    settings: Optional[Dict[str, Union[int, float, str, bool]]] = None


class Component(BaseModel):
    type: ComponentType
    settings: Optional[Dict[str, Union[int, float, str, bool]]] = None


class Workflow(BaseModel):
    name: str
    components: Optional[List[Component]] = None

    @validator("components")
    def validate_components(cls, components):
        types = set()
        import_seen = False
        export_seen = False
        settings_present = False

        for c in components:
            if c.type in types:
                raise ValueError("Duplicate component type!")
            types.add(c.type)

            if c.type == ComponentType.IMPORT:
                if import_seen:
                    raise ValueError("Import component already existed!")
                import_seen = True

            if c.type == ComponentType.EXPORT:
                if export_seen:
                    raise ValueError("Export component already existed!")
                export_seen = True

            if c.settings is not None:
                settings_present = True

        if import_seen and components[0].type != ComponentType.IMPORT:
            raise ValueError("Import component must be the first component!")

        if export_seen and components[-1].type != ComponentType.EXPORT:
            raise ValueError("Export component must be the last component!")

        if settings_present != (len(components) == len([c for c in components if c.settings])):
            raise ValueError("Either all components should contain settings or none shall contain it!")

        return components