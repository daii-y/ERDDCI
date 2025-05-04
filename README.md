# ERDDCI: Exact Reversible Diffusion via Dual-Chain Inversion for High-Quality Image Editing

[![arXiv](https://img.shields.io/badge/arXiv-ERDDCI-blue)](https://arxiv.org/abs/2410.14247)
[![TI2I](https://img.shields.io/badge/benchmarks-Original_TI2I-blue)](https://drive.google.com/drive/folders/1gR_kIjFSubpDdLe-_ECLNvkrtU5wxecW?usp=sharing)
[![DOCCI](https://img.shields.io/badge/benchmarks-DOCCI-blue)](https://huggingface.co/datasets/google/docci)

> Built upon [Google's Prompt-to-Prompt](https://github.com/google/prompt-to-prompt) implementation for _Stable Diffusion_.

![teaser](docs/teaser.png)

## Setup

### System Requirements

#### Core Dependencies

- Python(tested with 3.11)
- PyTorch(tested with 2.6.0)
- [HuggingFace Diffusers](https://github.com/huggingface/diffusers)
- [HuggingFace Datasets](https://github.com/huggingface/datasets)

#### Model Backbone

Implemented using [Stable Diffusion v1.4](https://huggingface.co/CompVis/stable-diffusion-v1-4) with compatible architecture.

#### Hardware

✅ **Tested Configuration**:

- OS: Ubuntu 18.04 LTS
- GPU: NVIDIA RTX 4090 (24GB VRAM)

⚠️ **Minimum Requirements**:

- GPU with ≥12GB VRAM
- Linux recommended

> ⚠️ **Compatibility Notice**: Untested on Windows/macOS systems.

### Creating a Running Environment

#### [UV](https://docs.astral.sh/uv/) (recommended)

```bash
uv sync     # create virtual env and install dependencies
. ./.venv/bin/activate  # activate virtual env
```

#### Conda(Pip3)

```bash
conda create --name erddci python=3.11  # create virtual env
conda activate erddci                   # activate virtual env
pip install -r requirements.txt         # install dependencies
```

### Benchmarks Datasets

In the reconstruction test, we used the `datasets` package of huggingface to load the dataset. In order to cooperate with this package, we modified the [TI2I benchmark](https://github.com/MichalGeyer/plug-and-play/blob/main/README.md#ti2i-benchmarks) to a certain extent.

#### TI2I (Modified)

The TI2I2 dataset provides editing prompts (target prompts), but does not provide original image prompts (source prompts). We created prompts to match the original images ourselves and used these prompts to rename the image files to obtain a modified version of the benchmark dataset.

Since the number of images is relatively small (~60), they are directly included in the `ReconDataset` folder within this repository. The corresponding `datasets` library loading code is also provided in the same folder.

#### DOCCI

We use this dataset directly through the `datasets` package of huggingface. The code for downloading and loading the dataset is in the notebook(`erddci_w_ptp_recon.ipynb`), which will be downloaded when the dataset is first used.

**Note: This dataset is huge (7GB+).**

## Running ERDDCI

After activating the virtual environment, launch Jupyter and run:

- `erddci_w_ptp_edit.ipynb` for image editing
- `erddci_w_ptp_recon.ipynb` for reconstruction testing

```bash
jupyter lab # or jupyter notebook
```

The explanation of ERDDCI method is documented in notebook markdown cells and code comments.

### Additional Resources

For Prompt-to-Prompt editing reference: [Original Implementation Guide](https://github.com/google/prompt-to-prompt#prompt-edits).

## Citation

```bibtex
@article{dai2024erddci,
  title={ERDDCI: Exact Reversible Diffusion via Dual-Chain Inversion for High-Quality Image Editing},
  author={Dai, Jimin and Zhang, Yingzhen and Chen, Shuo and Yang, Jian and Luo, Lei},
  journal={arXiv preprint arXiv:2410.14247},
  year={2024}
}
```
