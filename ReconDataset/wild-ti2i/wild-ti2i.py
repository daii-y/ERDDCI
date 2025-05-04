import os
import datasets
from datasets import GeneratorBasedBuilder, Features, Value
from datasets.info import DatasetInfo
from datasets.splits import Split, SplitGenerator

_IMAGE_DIR = "/home/djm/ERDDCI/ReconDataset/wild-ti2i/data/"

class WildTI2I(GeneratorBasedBuilder):
    """Organize an image folder into a `datasets` library Dataset, with filenames as prompts."""
    VERSION = datasets.Version("1.0.0")
    BUILDER_CONFIGS = [
        datasets.BuilderConfig(name="Wild-TI2I", version=VERSION, description="Wild-TI2I images and descriptions"),
    ]
    DEFAULT_CONFIG_NAME = "Wild-TI2I"

    def _info(self):
        return DatasetInfo(
            dataset_name="Wild-TI2I",
            description=self.config.description,
            features=Features(
                {
                    "image": Value("string"),
                    "description": Value("string"),
                }
            ),
            supervised_keys=None,
        )

    def _split_generators(self, dl_manager):
        return [
            SplitGenerator(
                name=Split.TEST,
                gen_kwargs={
                    "image_folder": _IMAGE_DIR,
                },
            ),
        ]

    def _generate_examples(self, image_folder):
        allowed_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
        for filename in os.listdir(image_folder):
            if os.path.isfile(os.path.join(image_folder, filename)):
                name, ext = os.path.splitext(filename)
                if ext.lower() in allowed_extensions:
                    image_path = os.path.join(image_folder, filename)
                    description = name
            yield image_path, {"image": image_path, "description": description} 