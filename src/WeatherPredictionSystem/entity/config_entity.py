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

@dataclass
class ModelTrainerConfig:
    root_dir: Path
    input_processor_path: Path
    target_processor_path: Path
    Data_dir: Path
    training_result: Path
    confusion_matrix: Path
    model_path: Path
    n_estimators: int           
    max_depth:int    
    min_samples_split: int         
    min_samples_leaf: int        
    max_features: str       
    bootstrap: bool               
    random_state: str             
    criterion: str