from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngstionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    prefix: str

@dataclass
class DataPreprocessorConfig:
    root_dir: Path
    input_processor_path: Path
    target_processor_path: Path