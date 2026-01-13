from typing import List, Union, Dict, Optional
from pathlib import Path
from pycheevos.core.condition import Condition
from pycheevos.core.value import MemoryValue
from pycheevos.core.constants import LeaderboardFormat

class RichPresence:
    def __init__(self):
        self.lookups: Dict[str, Dict[int, str]] = {}
        self.displays: List[tuple] = []
    
    def add_lookup(self, name: str, values: Dict[Union[int, tuple, list], str]):
        clean_dict = {}
        for key, label in values.items():
            if isinstance(key, (tuple, list)):
                for k in key:
                    clean_dict[k] = label
            else:
                clean_dict[key] = label
        
        self.lookups[name] = clean_dict
        return self
    
    def add_display(self, condition: Optional[Union[str, Condition, list]], text: str):
        if condition is None:
            cond_str = ""
        elif isinstance(condition, list):
            cond_str = "_".join([c.render() if hasattr(c, 'render') else str(c) for c in condition])
        elif hasattr(condition, 'render'):
            cond_str = condition.render()
        else:
            cond_str = str(condition)
            
        self.displays.append((cond_str, text))
        return self
    
    def render(self) -> str:
        lines = []

        for name, values in self.lookups.items():
            lines.append(f"Lookup:{name}")
            for k, v in values.items():
                lines.append(f"{k}={v}")
            lines.append("")

        lines.append("Display:")
        for cond, text in self.displays:
            if not cond or cond == "True":
                lines.append(text)
            else:
                lines.append(f"?{cond}?{text}")
        
        return "\n".join(lines)
    
    def save(self, game_id: int, title: str = "Rich Presence", path: Optional[str] = None):
        if path is None:
            root = Path.cwd()
            output = root / "output" / f"{title} - {game_id}"
        else:
            output = Path(path)

        output.mkdir(parents=True, exist_ok=True)
        rp_file = output / f"{game_id}-Rich.txt"
        
        with open(rp_file, "w", encoding="utf-8") as f:
            f.write(self.render())
        
        print(f"Generated Rich Presence file: {rp_file}")

    @staticmethod
    def lookup(name: str, memory: MemoryValue) -> str:
        return f"@{name}({memory.render()})"
    
    @staticmethod
    def value(memory: MemoryValue, format: str = "VALUE") -> str:
        return f"@{format}({memory.render()})"