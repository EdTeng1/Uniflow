"""Flow config module."""

from dataclasses import dataclass, field
from typing import Dict

from uniflow.extract.config import Config as ExtractConfig
from uniflow.model.config import (
    HuggingfaceModelConfig,
    LMQGModelConfig,
    ModelConfig,
    OpenAIJsonModelConfig,
    OpenAIModelConfig,
)


@dataclass
class Config:
    """Flow Config Class."""

    flow_name: str = "ModelFlow"
    few_shot_template: Dict[str, str] = field(default_factory=lambda: {})
    num_thread: int = 1
    model_config: ModelConfig = ModelConfig()


@dataclass
class OpenAIConfig:
    """Flow Config Class."""

    flow_name: str = "ModelFlow"
    few_shot_template: Dict[str, str] = field(default_factory=lambda: {})
    num_thread: int = 1
    model_config: ModelConfig = OpenAIModelConfig()


@dataclass
class OpenAIJsonConfig:
    """Flow Config Class."""

    flow_name: str = "OpenAIJsonModelFlow"
    few_shot_template: Dict[str, str] = field(default_factory=lambda: {})
    num_thread: int = 1
    model_config: ModelConfig = OpenAIJsonModelConfig()


@dataclass
class OpenAIFewShotConfig:
    """Flow Config Class."""

    flow_name: str = "FewShotModelFlow"
    few_shot_template: Dict[str, str] = field(
        default_factory=lambda: {
            "instruction": """Generate one question and its corresponding answer based on the context.
    Following the format of the examples below. The response must include original context, question, and answer.""",
            "examples": [
                {
                    "context": """The quick brown fox jumps over the lazy dog.""",
                    "question": """What is the color of the fox?""",
                    "answer": """brown.""",
                },
                {
                    "context": """The quick brown fox jumps over the lazy black dog.""",
                    "question": """What is the color of the dog?""",
                    "answer": """black.""",
                },
            ],
        }
    )
    num_thread: int = 1
    model_config: ModelConfig = OpenAIModelConfig()


@dataclass
class HuggingfaceConfig:
    """Huggingface Config Class."""

    flow_name: str = "HuggingFaceModelFlow"
    few_shot_template: Dict[str, str] = field(default_factory=lambda: {})
    num_thread: int = 1
    model_config: ModelConfig = HuggingfaceModelConfig()


@dataclass
class LMQGConfig:
    """LMQG Config Class."""

    flow_name: str = "LMQGModelFlow"
    few_shot_template: Dict[str, str] = field(default_factory=lambda: {})
    num_thread: int = 1
    model_config: ModelConfig = LMQGModelConfig()


@dataclass
class PipelineConfig:
    """Pipeline Config Class."""

    extract_config: ExtractConfig = ExtractConfig()
    transform_config: Config = OpenAIFewShotConfig()
