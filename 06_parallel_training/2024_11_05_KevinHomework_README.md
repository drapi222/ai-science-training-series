# 🚀 Parallel Training Methods for AI

[Sam Foreman](https://samforeman.me)  
[Intro to AI-driven Science on Supercomputers](https://www.alcf.anl.gov/alcf-ai-science-training-series)  
_2024-11-05_

- Slides: <https://samforeman.me/talks/ai-for-science-2024/slides>
  - HTML version: <https://samforeman.me/talks/ai-for-science-2024>

## 👋 Hands On

1. Submit interactive job:

    ```bash
    qsub -A ALCFAITP -q by-node -l select=1 -l walltime=01:00:00,filesystems=eagle:home -I
    ```

1. On Sophia:

    ```bash
    export HTTP_PROXY="http://proxy.alcf.anl.gov:3128"
    export HTTPS_PROXY="http://proxy.alcf.anl.gov:3128"
    export http_proxy="http://proxy.alcf.anl.gov:3128"
    export https_proxy="http://proxy.alcf.anl.gov:3128"
    export ftp_proxy="http://proxy.alcf.anl.gov:3128"
    ```

1. Clone repos:

    1. [`saforem2/wordplay`](https://github.com/saforem2/wordplay):

        ```bash
        git clone https://github.com/saforem2/wordplay
        cd wordplay
        ```

    1. [`saforem2/ezpz`](https://github.com/saforem2/ezpz):

        ```bash
        git clone https://github.com/saforem2/ezpz deps/ezpz
        ```

1. Setup python:

    ```bash
    export PBS_O_WORKDIR=$(pwd) && source deps/ezpz/src/ezpz/bin/utils.sh
    ezpz_setup_python
    ezpz_setup_job
    ```

1. Install `{ezpz, wordplay}`:

    ```bash
    python3 -m pip install -e deps/ezpz --require-virtualenv
    python3 -m pip install -e . --require-virtualenv
    ```

1. Setup (or disable) [`wandb`](https://wandb.ai):

    ```bash
    # to setup:
    wandb login
    # to disable:
    export WANDB_DISABLED=1
    ```

1. Test Distributed Setup:

    ```bash
    mpirun -n "${NGPUS}" python3 -m ezpz.test_dist
    ```

    See: [`ezpz/test_dist.py`](https://github.com/saforem2/ezpz/blob/main/src/ezpz/test_dist.py)

1. Prepare Data:

    ```bash
    python3 data/shakespeare_char/prepare.py
    ```

1. Launch Training:

    ```bash
    mpirun -n "${NGPUS}" python3 -m wordplay \
        train.backend=DDP \
        train.eval_interval=100 \
        data=shakespeare \
        train.dtype=bf16 \
        model.batch_size=64 \
        model.block_size=1024 \
        train.max_iters=1000 \
        train.log_interval=10 \
        train.compile=false
    ```

## 🎒 Homework

Submit _proof_ that you were able to successfully follow the above instructions and launch a distributed data parallel training run.

Where _proof_ can be any of:

- The contents printed out to your terminal during the run
- A path to a logfile containing the output from a run on the ALCF filesystems
- A screenshot of:
  - the text printed out from the run
  - a graph from the W&B Run
  - anything that shows that you clearly were able to run the example
- url to a W&B Run or [W&B Report](https://api.wandb.ai/links/aurora_gpt/7du35js1)
- etc.


## 🎒 Solution

- For complete print out of the terminal during the run, refer to this Google doc: <https://docs.google.com/document/d/1Rt9Og-_6nZhus1YBPhAT09lr9EVh_uNP2CaCELwPS_0/edit?usp=sharing>

<details>
    <summary>You can find training output here</summary>
  
```bash
$ mpirun -n "${NGPUS}" python3 -m wordplay \
    train.backend=DDP \
    train.eval_interval=100 \
    data=shakespeare \
    train.dtype=bf16 \
    model.batch_size=64 \
    model.block_size=1024 \
    train.max_iters=1000 \
    train.log_interval=10 \
    train.compile=false
[LOG_CAT_ML] component basesmuma is not available but requested in hierarchy: basesmuma,basesmuma,ucx_p2p:basesmsocket,basesmuma,p2p
[LOG_CAT_ML] ml_discover_hierarchy exited with error
[LOG_CAT_ML] component basesmuma is not available but requested in hierarchy: basesmuma,basesmuma,ucx_p2p:basesmsocket,basesmuma,p2p
[LOG_CAT_ML] ml_discover_hierarchy exited with error
[LOG_CAT_ML] component basesmuma is not available but requested in hierarchy: basesmuma,basesmuma,ucx_p2p:basesmsocket,basesmuma,p2p
[LOG_CAT_ML] ml_discover_hierarchy exited with error
[LOG_CAT_ML] component basesmuma is not available but requested in hierarchy: basesmuma,basesmuma,ucx_p2p:basesmsocket,basesmuma,p2p
[LOG_CAT_ML] ml_discover_hierarchy exited with error
[LOG_CAT_ML] component basesmuma is not available but requested in hierarchy: basesmuma,basesmuma,ucx_p2p:basesmsocket,basesmuma,p2p
[LOG_CAT_ML] ml_discover_hierarchy exited with error
[LOG_CAT_ML] component basesmuma is not available but requested in hierarchy: basesmuma,basesmuma,ucx_p2p:basesmsocket,basesmuma,p2p
[LOG_CAT_ML] ml_discover_hierarchy exited with error
[LOG_CAT_ML] component basesmuma is not available but requested in hierarchy: basesmuma,basesmuma,ucx_p2p:basesmsocket,basesmuma,p2p
[LOG_CAT_ML] ml_discover_hierarchy exited with error
[LOG_CAT_ML] component basesmuma is not available but requested in hierarchy: basesmuma,basesmuma,ucx_p2p:basesmsocket,basesmuma,p2p
[LOG_CAT_ML] ml_discover_hierarchy exited with error
[2024-11-09 19:59:16.517013][INFO][configs.py:81] - Setting HF_DATASETS_CACHE to /home/kevinfang/wordplay/.cache/huggingface/datasets
[2024-11-09 19:59:17.325113][INFO][dist.py:92] - 
[dist_info]:
  • DEVICE=cuda
  • DEVICE_ID=cuda:0
  • DISTRIBUTED_BACKEND=nccl
  • GPUS_PER_NODE=8
  • HOSTS=['sophia-gpu-03.lab.alcf.anl.gov']
  • HOSTFILE=/var/spool/pbs/aux/36567.sophia-pbs-01.lab.alcf.anl.gov
  • HOSTNAME=sophia-gpu-03.lab.alcf.anl.gov
  • LOCAL_RANK=0
  • MACHINE=Sophia
  • NUM_NODES=1
  • NGPUS=8
  • NGPUS_AVAILABLE=8
  • NODE_ID=0
  • RANK=0
  • SCHEDULER=LOCAL
  • WORLD_SIZE_TOTAL=8
  • WORLD_SIZE_IN_USE=8
  • LAUNCH_CMD=None
[2024-11-09 19:59:17.327826][INFO][dist.py:728] - [0/8] Using device='cuda' with backend='DDP' + 'nccl' for distributed training.
[2024-11-09 19:59:17.330198][INFO][dist.py:348] - [device='cuda'][rank=0/7][local_rank=0/7][node=0/0]
[2024-11-09 19:59:17.330807][WARNING][dist.py:352] - Using [8 / 8] available "cuda" devices !!
[2024-11-09 19:59:18.302337][INFO][dist.py:348] - [device='cuda'][rank=5/7][local_rank=5/7][node=0/0]
[2024-11-09 19:59:18.307302][INFO][dist.py:348] - [device='cuda'][rank=1/7][local_rank=1/7][node=0/0]
[2024-11-09 19:59:18.329831][INFO][dist.py:348] - [device='cuda'][rank=2/7][local_rank=2/7][node=0/0]
[2024-11-09 19:59:18.350303][INFO][dist.py:348] - [device='cuda'][rank=3/7][local_rank=3/7][node=0/0]
[2024-11-09 19:59:18.350833][INFO][dist.py:348] - [device='cuda'][rank=4/7][local_rank=4/7][node=0/0]
[2024-11-09 19:59:18.350899][INFO][dist.py:348] - [device='cuda'][rank=6/7][local_rank=6/7][node=0/0]
[2024-11-09 19:59:18.352804][INFO][dist.py:348] - [device='cuda'][rank=7/7][local_rank=7/7][node=0/0]
[2024-11-09 19:59:20.302102][INFO][configs.py:317] - Loading train from /home/kevinfang/wordplay/data/shakespeare_char/train.bin
[2024-11-09 19:59:20.303584][INFO][configs.py:317] - Loading val from /home/kevinfang/wordplay/data/shakespeare_char/val.bin
[2024-11-09 19:59:20.305190][INFO][configs.py:442] - Tokens per iteration: 524,288
[2024-11-09 19:59:20.305769][INFO][configs.py:465] - Using self.ptdtype=torch.float16 on self.device_type='cuda'
[2024-11-09 19:59:20.306231][INFO][configs.py:471] - Initializing a new model from scratch
[2024-11-09 19:59:20.310452][INFO][dist.py:882] - Setting up wandb from rank: 0
[2024-11-09 19:59:20.311000][INFO][dist.py:883] - Using: WB PROJECT: WordPlay
wandb: Currently logged in as: 26kfang (26kfang-stratford-school). Use `wandb login --relogin` to force relogin
wandb: wandb version 0.18.6 is available!  To upgrade, please run:
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.17.6
wandb: Run data is saved locally in /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16/wandb/run-20241109_195921-snrgerlv
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run vocal-forest-1
wandb: ⭐️ View project at https://wandb.ai/26kfang-stratford-school/WordPlay
wandb: 🚀 View run at https://wandb.ai/26kfang-stratford-school/WordPlay/runs/snrgerlv
/home/kevinfang/wordplay/src/wordplay/trainer.py:303: FutureWarning: `torch.cuda.amp.GradScaler(args...)` is deprecated. Please use `torch.amp.GradScaler('cuda', args...)` instead.
  grad_scaler = GradScaler(
[2024-11-09 19:59:22.725903][CRITICAL][trainer.py:318] - "devid='cuda:3'"
/home/kevinfang/wordplay/src/wordplay/trainer.py:303: FutureWarning: `torch.cuda.amp.GradScaler(args...)` is deprecated. Please use `torch.amp.GradScaler('cuda', args...)` instead.
  grad_scaler = GradScaler(
[2024-11-09 19:59:22.730212][CRITICAL][trainer.py:318] - "devid='cuda:4'"
/home/kevinfang/wordplay/src/wordplay/trainer.py:303: FutureWarning: `torch.cuda.amp.GradScaler(args...)` is deprecated. Please use `torch.amp.GradScaler('cuda', args...)` instead.
  grad_scaler = GradScaler(
[2024-11-09 19:59:22.732458][CRITICAL][trainer.py:318] - "devid='cuda:2'"
/home/kevinfang/wordplay/src/wordplay/trainer.py:303: FutureWarning: `torch.cuda.amp.GradScaler(args...)` is deprecated. Please use `torch.amp.GradScaler('cuda', args...)` instead.
  grad_scaler = GradScaler(
[2024-11-09 19:59:22.735971][CRITICAL][trainer.py:318] - "devid='cuda:5'"
/home/kevinfang/wordplay/src/wordplay/trainer.py:303: FutureWarning: `torch.cuda.amp.GradScaler(args...)` is deprecated. Please use `torch.amp.GradScaler('cuda', args...)` instead.
  grad_scaler = GradScaler(
[2024-11-09 19:59:22.739023][CRITICAL][trainer.py:318] - "devid='cuda:7'"
/home/kevinfang/wordplay/src/wordplay/trainer.py:303: FutureWarning: `torch.cuda.amp.GradScaler(args...)` is deprecated. Please use `torch.amp.GradScaler('cuda', args...)` instead.
  grad_scaler = GradScaler(
[2024-11-09 19:59:22.746884][CRITICAL][trainer.py:318] - "devid='cuda:1'"
/home/kevinfang/wordplay/src/wordplay/trainer.py:303: FutureWarning: `torch.cuda.amp.GradScaler(args...)` is deprecated. Please use `torch.amp.GradScaler('cuda', args...)` instead.
  grad_scaler = GradScaler(
[2024-11-09 19:59:22.756220][CRITICAL][trainer.py:318] - "devid='cuda:6'"
[2024-11-09 19:59:22.953921][INFO][dist.py:908] - W&B RUN: [vocal-forest-1](https://wandb.ai/26kfang-stratford-school/WordPlay/runs/snrgerlv)
[2024-11-09 19:59:22.958201][INFO][dist.py:304] - Updating wandb.run: vocal-forest-1 config with "DIST_INFO"
[2024-11-09 19:59:22.962342][INFO][dist.py:936] - Running on machine='Sophia'
[2024-11-09 19:59:22.963818][WARNING][__main__.py:93] - {
    "train": {
        "framework": "pytorch",
        "backend": "DDP",
        "device": null,
        "seed": null,
        "port": null,
        "ds_config_path": null,
        "precision": null,
        "ngpus": null,
        "use_wandb": true,
        "eval_interval": 100,
        "log_interval": 10,
        "eval_iters": 200,
        "eval_only": false,
        "always_save_checkpoint": false,
        "init_from": "scratch",
        "wandb_project": "WordPlay",
        "max_iters": 1000,
        "warmup_iters": 100,
        "dtype": "bf16",
        "compile": false
    },
    "model": {
        "n_layer": 12,
        "n_head": 12,
        "n_embd": 768,
        "batch_size": 64,
        "block_size": 1024,
        "activation": "gelu",
        "dropout": 0.0,
        "bias": false,
        "vocab_size": 65
    },
    "data": {
        "dataset": "shakespeare_char",
        "out_dir": "out-shakespeare-char",
        "root_path": null
    },
    "optimizer": {
        "gas": 1,
        "name": "AdamW",
        "learning_rate": 0.0006,
        "weight_decay": 0.1,
        "beta1": 0.9,
        "beta2": 0.95,
        "grad_clip": 1.0,
        "decay_lr": true,
        "lr_decay_iters": 600000,
        "min_lr": 6e-05
    }
}
[2024-11-09 19:59:22.967071][WARNING][__main__.py:94] - Output dir: /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16
[2024-11-09 19:59:22.967609][INFO][trainer.py:248] - Initializing a new model from scratch
[2024-11-09 19:59:24.134755][INFO][model.py:255] - number of parameters: 85.00M
[2024-11-09 19:59:24.179842][INFO][trainer.py:266] - Model size: num_params=85003776
[2024-11-09 19:59:24.183383][INFO][model.py:445] - num decayed parameter tensors: 50, with 85,771,008 parameters
[2024-11-09 19:59:24.184025][INFO][model.py:449] - num non-decayed parameter tensors: 25, with 19,200 parameters
[2024-11-09 19:59:25.099436][INFO][model.py:465] - using fused AdamW: True
/home/kevinfang/wordplay/src/wordplay/trainer.py:303: FutureWarning: `torch.cuda.amp.GradScaler(args...)` is deprecated. Please use `torch.amp.GradScaler('cuda', args...)` instead.
  grad_scaler = GradScaler(
[2024-11-09 19:59:25.101260][CRITICAL][trainer.py:318] - "devid='cuda:0'"
[2024-11-09 19:59:25.111603][INFO][trainer.py:358] - • self.model=GPT(
  (transformer): ModuleDict(
    (wte): Embedding(65, 768)
    (wpe): Embedding(1024, 768)
    (drop): Dropout(p=0.0, inplace=False)
    (h): ModuleList(
      (0-11): 12 x Block(
        (ln_1): LayerNorm()
        (attn): CausalSelfAttention(
          (c_attn): Linear(in_features=768, out_features=2304, bias=False)
          (c_proj): Linear(in_features=768, out_features=768, bias=False)
          (attn_dropout): Dropout(p=0.0, inplace=False)
          (resid_dropout): Dropout(p=0.0, inplace=False)
        )
        (ln_2): LayerNorm()
        (mlp): MLP(
          (c_fc): Linear(in_features=768, out_features=3072, bias=False)
          (act_fn): GELU(approximate='none')
          (c_proj): Linear(in_features=3072, out_features=768, bias=False)
          (dropout): Dropout(p=0.0, inplace=False)
        )
      )
    )
    (ln_f): LayerNorm()
  )
  (lm_head): Linear(in_features=768, out_features=65, bias=False)
)
[2024-11-09 19:59:25.115606][INFO][trainer.py:359] - • self.grad_scaler=<torch.cuda.amp.grad_scaler.GradScaler object at 0x14fea8668a90>
[2024-11-09 19:59:25.116667][INFO][trainer.py:360] - • self.model_engine=DistributedDataParallel(
  (module): GPT(
    (transformer): ModuleDict(
      (wte): Embedding(65, 768)
      (wpe): Embedding(1024, 768)
      (drop): Dropout(p=0.0, inplace=False)
      (h): ModuleList(
        (0-11): 12 x Block(
          (ln_1): LayerNorm()
          (attn): CausalSelfAttention(
            (c_attn): Linear(in_features=768, out_features=2304, bias=False)
            (c_proj): Linear(in_features=768, out_features=768, bias=False)
            (attn_dropout): Dropout(p=0.0, inplace=False)
            (resid_dropout): Dropout(p=0.0, inplace=False)
          )
          (ln_2): LayerNorm()
          (mlp): MLP(
            (c_fc): Linear(in_features=768, out_features=3072, bias=False)
            (act_fn): GELU(approximate='none')
            (c_proj): Linear(in_features=3072, out_features=768, bias=False)
            (dropout): Dropout(p=0.0, inplace=False)
          )
        )
      )
      (ln_f): LayerNorm()
    )
    (lm_head): Linear(in_features=768, out_features=65, bias=False)
  )
)
[2024-11-09 19:59:25.120392][INFO][trainer.py:361] - • self.optimizer=AdamW (
Parameter Group 0
    amsgrad: False
    betas: (0.9, 0.95)
    capturable: False
    differentiable: False
    eps: 1e-08
    foreach: None
    fused: True
    lr: 0.0006
    maximize: False
    weight_decay: 0.1
Parameter Group 1
    amsgrad: False
    betas: (0.9, 0.95)
    capturable: False
    differentiable: False
    eps: 1e-08
    foreach: None
    fused: True
    lr: 0.0006
    maximize: False
    weight_decay: 0.0
)
[2024-11-09 19:59:25.236054][INFO][trainer.py:809] - Startup time: 8.6893
                Training Legend                 
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        abbr ┃ desc                           ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│        step │ Current training iteration     │
│        loss │ Loss value                     │
│          dt │ Elapsed time per training step │
│         dtf │ Elapsed time per forward step  │
│         dtb │ Elapsed time per backward step │
│         sps │ Samples per second             │
│ sps_per_gpu │ Samples per second (per GPU)   │
│         tps │ Tokens per second              │
│ tps_per_gpu │ Tokens per second (per GPU)    │
│         mfu │ Model flops utilization        │
└─────────────┴────────────────────────────────┘
[2024-11-09 19:59:26.629454][INFO][trainer.py:827] - ['prompt']: 'What is an LLM?'
[2024-11-09 19:59:26.631296][INFO][trainer.py:831] - ['response']:
What is an LLM?aaE!fmmtoBXJpjjNyaaKpXJJaaEq3dA!g!!!noVVd,Q,a;sg,qgg,g3dD,QQ,,3aFVBBoNBoQcEnoeheae BaayPgIVXaBmEfaayMfaHaaf'fyNYAQC:fAnM'''c33a3eYIhleFjV3Kg,u!BQufttVEqaVXjayy-gyfaEV3BByy-ggyJaMa,,QttHBoeMM,aK?aVV,,,VVVV;;pO,Mgtog,qnf,,,g''sqJcccee;VB,Vn3B af-Vyf-;QEg,j,g
[2024-11-09 20:00:06.652694][INFO][trainer.py:892] - step=10 loss=3.22448 dt=0.28387 dtf=0.0065803 dtb=0.0152319 sps=28.1819 sps_per_gpu=3.52274 tps=1.84693e+06 tps_per_gpu=230866 mfu=46.1191
[2024-11-09 20:00:09.621418][INFO][trainer.py:892] - step=20 loss=2.72117 dt=0.303934 dtf=0.00660222 dtb=0.0162679 sps=26.3215 sps_per_gpu=3.29019 tps=1.72501e+06 tps_per_gpu=215626 mfu=45.8147
[2024-11-09 20:00:12.649687][INFO][trainer.py:892] - step=30 loss=2.55238 dt=0.300647 dtf=0.00664809 dtb=0.020845 sps=26.6092 sps_per_gpu=3.32616 tps=1.74386e+06 tps_per_gpu=217983 mfu=45.5878
[2024-11-09 20:00:15.612295][INFO][trainer.py:892] - step=40 loss=2.50235 dt=0.281082 dtf=0.00643071 dtb=0.0202802 sps=28.4614 sps_per_gpu=3.55768 tps=1.86525e+06 tps_per_gpu=233156 mfu=45.6867
[2024-11-09 20:00:18.621994][INFO][trainer.py:892] - step=50 loss=2.4742 dt=0.29435 dtf=0.00633614 dtb=0.0202304 sps=27.1785 sps_per_gpu=3.39732 tps=1.78117e+06 tps_per_gpu=222647 mfu=45.5657
[2024-11-09 20:00:21.684479][INFO][trainer.py:892] - step=60 loss=2.48306 dt=0.306898 dtf=0.00679576 dtb=0.0147016 sps=26.0673 sps_per_gpu=3.25841 tps=1.70835e+06 tps_per_gpu=213543 mfu=45.275
[2024-11-09 20:00:24.761017][INFO][trainer.py:892] - step=70 loss=2.46159 dt=0.300238 dtf=0.00637463 dtb=0.0162115 sps=26.6455 sps_per_gpu=3.33069 tps=1.74624e+06 tps_per_gpu=218280 mfu=45.108
[2024-11-09 20:00:27.792472][INFO][trainer.py:892] - step=80 loss=2.46009 dt=0.289227 dtf=0.00689084 dtb=0.0153451 sps=27.66 sps_per_gpu=3.4575 tps=1.81272e+06 tps_per_gpu=226591 mfu=45.1237
[2024-11-09 20:00:30.858081][INFO][trainer.py:892] - step=90 loss=2.45469 dt=0.294302 dtf=0.00688507 dtb=0.0202153 sps=27.1829 sps_per_gpu=3.39787 tps=1.78146e+06 tps_per_gpu=222683 mfu=45.0598
[2024-11-09 20:00:33.914350][INFO][trainer.py:892] - step=100 loss=2.46432 dt=0.300538 dtf=0.00633763 dtb=0.0170318 sps=26.6189 sps_per_gpu=3.32736 tps=1.7445e+06 tps_per_gpu=218062 mfu=44.9099
[2024-11-09 20:00:35.039730][INFO][trainer.py:827] - ['prompt']: 'What is an LLM?'
[2024-11-09 20:00:35.040489][INFO][trainer.py:831] - ['response']:
What is an LLM?ay, thay my heatrshy,
ARK:
Trre, thelisthed manso ond thalshawesuck howingis ou,
Toss semeeecedit:
Mat bouche.
To at t aicenof masthet.
He t.
Whes be there nomanghillist ILOKILARO:
Tharof ourdit fowef bornghar olerand il hachangrther thod.
KINRDICH
[2024-11-09 20:01:12.298617][INFO][trainer.py:762] - Saving checkpoint to: /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16
[2024-11-09 20:01:12.300452][INFO][trainer.py:763] - Saving model to: /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16/model.pth
[2024-11-09 20:01:14.594824][INFO][configs.py:141] - Appending /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16 to /home/kevinfang/wordplay/src/ckpts/checkpoints.log
[2024-11-09 20:01:17.644079][INFO][trainer.py:892] - step=110 loss=2.42379 dt=0.312501 dtf=0.006564 dtb=0.0186594 sps=25.5999 sps_per_gpu=3.19999 tps=1.67772e+06 tps_per_gpu=209715 mfu=44.6083
[2024-11-09 20:01:20.748919][INFO][trainer.py:892] - step=120 loss=2.42399 dt=0.307758 dtf=0.00625625 dtb=0.0159084 sps=25.9944 sps_per_gpu=3.2493 tps=1.70357e+06 tps_per_gpu=212946 mfu=44.4014
[2024-11-09 20:01:23.803645][INFO][trainer.py:892] - step=130 loss=2.385 dt=0.311065 dtf=0.00660201 dtb=0.0143269 sps=25.7181 sps_per_gpu=3.21476 tps=1.68546e+06 tps_per_gpu=210682 mfu=44.17
[2024-11-09 20:01:26.849081][INFO][trainer.py:892] - step=140 loss=2.37143 dt=0.320912 dtf=0.00649213 dtb=0.0147958 sps=24.929 sps_per_gpu=3.11612 tps=1.63374e+06 tps_per_gpu=204218 mfu=43.8326
[2024-11-09 20:01:29.882061][INFO][trainer.py:892] - step=150 loss=2.37997 dt=0.284092 dtf=0.0065956 dtb=0.0218987 sps=28.1599 sps_per_gpu=3.51999 tps=1.84549e+06 tps_per_gpu=230686 mfu=44.0576
[2024-11-09 20:01:32.875670][INFO][trainer.py:892] - step=160 loss=2.32189 dt=0.302639 dtf=0.006334 dtb=0.0146957 sps=26.4341 sps_per_gpu=3.30427 tps=1.73239e+06 tps_per_gpu=216548 mfu=43.9777
[2024-11-09 20:01:35.894090][INFO][trainer.py:892] - step=170 loss=2.28291 dt=0.309949 dtf=0.00700915 dtb=0.015765 sps=25.8107 sps_per_gpu=3.22634 tps=1.69153e+06 tps_per_gpu=211442 mfu=43.8038
[2024-11-09 20:01:38.939440][INFO][trainer.py:892] - step=180 loss=2.18421 dt=0.307613 dtf=0.00649485 dtb=0.014971 sps=26.0067 sps_per_gpu=3.25084 tps=1.70438e+06 tps_per_gpu=213047 mfu=43.6794
[2024-11-09 20:01:41.988615][INFO][trainer.py:892] - step=190 loss=2.10171 dt=0.303026 dtf=0.00703827 dtb=0.0151893 sps=26.4004 sps_per_gpu=3.30005 tps=1.73018e+06 tps_per_gpu=216272 mfu=43.6318
[2024-11-09 20:01:45.008402][INFO][trainer.py:892] - step=200 loss=2.04105 dt=0.315365 dtf=0.00667369 dtb=0.0140146 sps=25.3675 sps_per_gpu=3.17093 tps=1.66248e+06 tps_per_gpu=207810 mfu=43.42
[2024-11-09 20:01:46.136186][INFO][trainer.py:827] - ['prompt']: 'What is an LLM?'
[2024-11-09 20:01:46.136952][INFO][trainer.py:831] - ['response']:
What is an LLM?
PAULET:
Norer for, you, nother thon thand and into bot cheard yout to and woull hou goont.
A not good dothesbeste his moth mer suser
O, min mys bepperar,
I thas ste hour, hell onceng ald in sth fanote ine ithe he sesen.
And I noing you speadert of now-mo
[2024-11-09 20:02:23.285430][INFO][trainer.py:762] - Saving checkpoint to: /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16
[2024-11-09 20:02:23.287127][INFO][trainer.py:763] - Saving model to: /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16/model.pth
[2024-11-09 20:02:26.019041][INFO][configs.py:141] - Appending /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16 to /home/kevinfang/wordplay/src/ckpts/checkpoints.log
[2024-11-09 20:02:29.101063][INFO][trainer.py:892] - step=210 loss=1.94194 dt=0.302553 dtf=0.00621142 dtb=0.0138827 sps=26.4416 sps_per_gpu=3.3052 tps=1.73288e+06 tps_per_gpu=216610 mfu=43.4051
[2024-11-09 20:02:32.136940][INFO][trainer.py:892] - step=220 loss=1.902 dt=0.313943 dtf=0.00621123 dtb=0.0148157 sps=25.4823 sps_per_gpu=3.18529 tps=1.67001e+06 tps_per_gpu=208751 mfu=43.2347
[2024-11-09 20:02:35.204412][INFO][trainer.py:892] - step=230 loss=1.82252 dt=0.304617 dtf=0.0061965 dtb=0.0167251 sps=26.2625 sps_per_gpu=3.28281 tps=1.72114e+06 tps_per_gpu=215142 mfu=43.2091
[2024-11-09 20:02:38.248461][INFO][trainer.py:892] - step=240 loss=1.73491 dt=0.312375 dtf=0.0380752 dtb=0.0214545 sps=25.6102 sps_per_gpu=3.20128 tps=1.67839e+06 tps_per_gpu=209799 mfu=43.0792
[2024-11-09 20:02:41.289518][INFO][trainer.py:892] - step=250 loss=1.69689 dt=0.301715 dtf=0.00760386 dtb=0.0181878 sps=26.5151 sps_per_gpu=3.31439 tps=1.7377e+06 tps_per_gpu=217212 mfu=43.1104
[2024-11-09 20:02:44.325859][INFO][trainer.py:892] - step=260 loss=1.62495 dt=0.301067 dtf=0.00991126 dtb=0.0187229 sps=26.5722 sps_per_gpu=3.32152 tps=1.74144e+06 tps_per_gpu=217679 mfu=43.1479
[2024-11-09 20:02:47.414509][INFO][trainer.py:892] - step=270 loss=1.59933 dt=0.296062 dtf=0.00677582 dtb=0.0183308 sps=27.0214 sps_per_gpu=3.37768 tps=1.77088e+06 tps_per_gpu=221359 mfu=43.2551
[2024-11-09 20:02:50.452077][INFO][trainer.py:892] - step=280 loss=1.56562 dt=0.291607 dtf=0.00659944 dtb=0.0159845 sps=27.4342 sps_per_gpu=3.42927 tps=1.79792e+06 tps_per_gpu=224741 mfu=43.4191
[2024-11-09 20:02:53.510132][INFO][trainer.py:892] - step=290 loss=1.50872 dt=0.302645 dtf=0.00707971 dtb=0.0168464 sps=26.4336 sps_per_gpu=3.3042 tps=1.73235e+06 tps_per_gpu=216544 mfu=43.403
[2024-11-09 20:02:56.590424][INFO][trainer.py:892] - step=300 loss=1.47936 dt=0.292868 dtf=0.00684346 dtb=0.0207579 sps=27.3161 sps_per_gpu=3.41451 tps=1.79019e+06 tps_per_gpu=223773 mfu=43.533
[2024-11-09 20:02:57.740319][INFO][trainer.py:827] - ['prompt']: 'What is an LLM?'
[2024-11-09 20:02:57.741747][INFO][trainer.py:831] - ['response']:
What is an LLM?
BRUS:
Horthen the cannot stalt than the me form,
And with make to much their condies tent.
GREEN:
Sit, I have not will dived of the proudent,
To hadst through hear againscared himselfgs leven.
ROMEO:
A then, and feel new save the leasty be endess,
From
[2024-11-09 20:03:34.982861][INFO][trainer.py:762] - Saving checkpoint to: /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16
[2024-11-09 20:03:34.984788][INFO][trainer.py:763] - Saving model to: /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16/model.pth
[2024-11-09 20:03:37.876204][INFO][configs.py:141] - Appending /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16 to /home/kevinfang/wordplay/src/ckpts/checkpoints.log
[2024-11-09 20:03:40.940115][INFO][trainer.py:892] - step=310 loss=1.42904 dt=0.311675 dtf=0.00620799 dtb=0.0156984 sps=25.6677 sps_per_gpu=3.20847 tps=1.68216e+06 tps_per_gpu=210270 mfu=43.3801
[2024-11-09 20:03:44.059771][INFO][trainer.py:892] - step=320 loss=1.37403 dt=0.324705 dtf=0.00698529 dtb=0.0179584 sps=24.6377 sps_per_gpu=3.07971 tps=1.61466e+06 tps_per_gpu=201832 mfu=43.074
[2024-11-09 20:03:47.147120][INFO][trainer.py:892] - step=330 loss=1.3536 dt=0.310527 dtf=0.00734436 dtb=0.0246029 sps=25.7627 sps_per_gpu=3.22034 tps=1.68838e+06 tps_per_gpu=211048 mfu=42.9826
[2024-11-09 20:03:50.176164][INFO][trainer.py:892] - step=340 loss=1.31101 dt=0.290842 dtf=0.00637208 dtb=0.0146657 sps=27.5064 sps_per_gpu=3.4383 tps=1.80266e+06 tps_per_gpu=225332 mfu=43.1857
[2024-11-09 20:03:53.213603][INFO][trainer.py:892] - step=350 loss=1.28254 dt=0.298417 dtf=0.0136413 dtb=0.0270846 sps=26.8081 sps_per_gpu=3.35102 tps=1.7569e+06 tps_per_gpu=219612 mfu=43.2543
[2024-11-09 20:03:56.256433][INFO][trainer.py:892] - step=360 loss=1.22671 dt=0.291037 dtf=0.00697643 dtb=0.0229445 sps=27.4879 sps_per_gpu=3.43599 tps=1.80145e+06 tps_per_gpu=225181 mfu=43.4272
[2024-11-09 20:03:59.308295][INFO][trainer.py:892] - step=370 loss=1.21254 dt=0.308919 dtf=0.00630675 dtb=0.0134343 sps=25.8968 sps_per_gpu=3.2371 tps=1.69717e+06 tps_per_gpu=212146 mfu=43.3224
[2024-11-09 20:04:02.369324][INFO][trainer.py:892] - step=380 loss=1.15602 dt=0.314461 dtf=0.0141847 dtb=0.015361 sps=25.4404 sps_per_gpu=3.18005 tps=1.66726e+06 tps_per_gpu=208408 mfu=43.1534
[2024-11-09 20:04:05.470134][INFO][trainer.py:892] - step=390 loss=1.1274 dt=0.308892 dtf=0.00631581 dtb=0.0154389 sps=25.899 sps_per_gpu=3.23738 tps=1.69732e+06 tps_per_gpu=212165 mfu=43.0764
[2024-11-09 20:04:08.520450][INFO][trainer.py:892] - step=400 loss=1.10326 dt=0.306442 dtf=0.00681081 dtb=0.0155072 sps=26.1061 sps_per_gpu=3.26326 tps=1.71089e+06 tps_per_gpu=213861 mfu=43.041
[2024-11-09 20:04:09.662135][INFO][trainer.py:827] - ['prompt']: 'What is an LLM?'
[2024-11-09 20:04:09.669498][INFO][trainer.py:831] - ['response']:
What is an LLM?
WARWICK:
And here's last, he hath shall be now weep.
BUCKINGHAM:
And not my deef nor from his married love.
BUCKINGHAM:
Harry his mind, he did so pitch'd his fear from his
Where babe than his soul business share reign.
CATESBY:
But not him lasty he in
[2024-11-09 20:04:46.799968][INFO][trainer.py:762] - Saving checkpoint to: /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16
[2024-11-09 20:04:46.801689][INFO][trainer.py:763] - Saving model to: /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16/model.pth
[2024-11-09 20:04:49.629109][INFO][configs.py:141] - Appending /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16 to /home/kevinfang/wordplay/src/ckpts/checkpoints.log
[2024-11-09 20:04:52.674013][INFO][trainer.py:892] - step=410 loss=1.06303 dt=0.301536 dtf=0.00649717 dtb=0.0157416 sps=26.5309 sps_per_gpu=3.31636 tps=1.73873e+06 tps_per_gpu=217341 mfu=43.0786
[2024-11-09 20:04:55.689013][INFO][trainer.py:892] - step=420 loss=1.01033 dt=0.301453 dtf=0.00675806 dtb=0.0149123 sps=26.5382 sps_per_gpu=3.31727 tps=1.73921e+06 tps_per_gpu=217401 mfu=43.1137
[2024-11-09 20:04:58.729969][INFO][trainer.py:892] - step=430 loss=0.951897 dt=0.299452 dtf=0.00654637 dtb=0.0216775 sps=26.7155 sps_per_gpu=3.33944 tps=1.75083e+06 tps_per_gpu=218853 mfu=43.1743
[2024-11-09 20:05:01.765799][INFO][trainer.py:892] - step=440 loss=0.900425 dt=0.294582 dtf=0.00634372 dtb=0.018925 sps=27.1571 sps_per_gpu=3.39464 tps=1.77977e+06 tps_per_gpu=222471 mfu=43.301
[2024-11-09 20:05:04.792849][INFO][trainer.py:892] - step=450 loss=0.844767 dt=0.307625 dtf=0.00668462 dtb=0.0170992 sps=26.0057 sps_per_gpu=3.25071 tps=1.70431e+06 tps_per_gpu=213039 mfu=43.2267
[2024-11-09 20:05:07.822370][INFO][trainer.py:892] - step=460 loss=0.779583 dt=0.325059 dtf=0.00612599 dtb=0.0160428 sps=24.6109 sps_per_gpu=3.07636 tps=1.6129e+06 tps_per_gpu=201612 mfu=42.9316
[2024-11-09 20:05:10.850627][INFO][trainer.py:892] - step=470 loss=0.71975 dt=0.304409 dtf=0.00687395 dtb=0.0239732 sps=26.2805 sps_per_gpu=3.28506 tps=1.72232e+06 tps_per_gpu=215290 mfu=42.9392
[2024-11-09 20:05:13.927068][INFO][trainer.py:892] - step=480 loss=0.670511 dt=0.292395 dtf=0.00654304 dtb=0.0141435 sps=27.3602 sps_per_gpu=3.42003 tps=1.79308e+06 tps_per_gpu=224135 mfu=43.1227
[2024-11-09 20:05:16.971843][INFO][trainer.py:892] - step=490 loss=0.608918 dt=0.298014 dtf=0.0066288 dtb=0.01544 sps=26.8444 sps_per_gpu=3.35555 tps=1.75927e+06 tps_per_gpu=219909 mfu=43.2034
[2024-11-09 20:05:20.003902][INFO][trainer.py:892] - step=500 loss=0.546135 dt=0.289972 dtf=0.00678498 dtb=0.0155826 sps=27.5889 sps_per_gpu=3.44861 tps=1.80806e+06 tps_per_gpu=226008 mfu=43.398
[2024-11-09 20:05:21.146822][INFO][trainer.py:827] - ['prompt']: 'What is an LLM?'
[2024-11-09 20:05:21.147909][INFO][trainer.py:831] - ['response']:
What is an LLM?
SREY:
They should therefore ask the Englishmen,
Nor Montague their of Rossider his person.
WARWICK:
Ay, but I came them voice, they begin breed.
I'll there cherist me that excuses me now.
Second Messenger:
Find with my request cannot prolbestition
I'll
[2024-11-09 20:05:58.293933][INFO][trainer.py:762] - Saving checkpoint to: /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16
[2024-11-09 20:05:58.295755][INFO][trainer.py:763] - Saving model to: /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16/model.pth
[2024-11-09 20:06:01.110064][INFO][configs.py:141] - Appending /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16 to /home/kevinfang/wordplay/src/ckpts/checkpoints.log
[2024-11-09 20:06:04.162060][INFO][trainer.py:892] - step=510 loss=0.431839 dt=0.294221 dtf=0.00716382 dtb=0.0196882 sps=27.1904 sps_per_gpu=3.39881 tps=1.78195e+06 tps_per_gpu=222744 mfu=43.5078
[2024-11-09 20:06:07.239038][INFO][trainer.py:892] - step=520 loss=0.38621 dt=0.325289 dtf=0.00662879 dtb=0.0240746 sps=24.5935 sps_per_gpu=3.07419 tps=1.61176e+06 tps_per_gpu=201470 mfu=43.1817
[2024-11-09 20:06:10.229246][INFO][trainer.py:892] - step=530 loss=0.31778 dt=0.297523 dtf=0.00645669 dtb=0.0162793 sps=26.8887 sps_per_gpu=3.36108 tps=1.76218e+06 tps_per_gpu=220272 mfu=43.2638
[2024-11-09 20:06:13.196396][INFO][trainer.py:892] - step=540 loss=0.270126 dt=0.294002 dtf=0.00743538 dtb=0.0245106 sps=27.2107 sps_per_gpu=3.40133 tps=1.78328e+06 tps_per_gpu=222910 mfu=43.3904
[2024-11-09 20:06:16.181191][INFO][trainer.py:892] - step=550 loss=0.225426 dt=0.307292 dtf=0.0064989 dtb=0.0204935 sps=26.0338 sps_per_gpu=3.25423 tps=1.70615e+06 tps_per_gpu=213269 mfu=43.3118
[2024-11-09 20:06:19.199068][INFO][trainer.py:892] - step=560 loss=0.167126 dt=0.306337 dtf=0.00689508 dtb=0.0166509 sps=26.115 sps_per_gpu=3.26438 tps=1.71147e+06 tps_per_gpu=213934 mfu=43.2543
[2024-11-09 20:06:22.201361][INFO][trainer.py:892] - step=570 loss=0.143786 dt=0.28904 dtf=0.00643907 dtb=0.0146036 sps=27.6778 sps_per_gpu=3.45973 tps=1.81389e+06 tps_per_gpu=226737 mfu=43.4583
[2024-11-09 20:06:25.218611][INFO][trainer.py:892] - step=580 loss=0.106106 dt=0.302104 dtf=0.00710844 dtb=0.0169949 sps=26.4809 sps_per_gpu=3.31012 tps=1.73545e+06 tps_per_gpu=216932 mfu=43.446
[2024-11-09 20:06:28.255773][INFO][trainer.py:892] - step=590 loss=0.0805788 dt=0.330095 dtf=0.00652657 dtb=0.013227 sps=24.2354 sps_per_gpu=3.02943 tps=1.58829e+06 tps_per_gpu=198537 mfu=43.0675
[2024-11-09 20:06:31.307328][INFO][trainer.py:892] - step=600 loss=0.155729 dt=0.317709 dtf=0.00678537 dtb=0.0179719 sps=25.1803 sps_per_gpu=3.14754 tps=1.65022e+06 tps_per_gpu=206277 mfu=42.8814
[2024-11-09 20:06:32.470786][INFO][trainer.py:827] - ['prompt']: 'What is an LLM?'
[2024-11-09 20:06:32.473143][INFO][trainer.py:831] - ['response']:
What is an LLM?Best rebellion,
Didst with my gracious lord,
And more come to London,
And him I am the king.
BRUTUS:
Look,
What is your greatest,
Your servants,
Ay, are your house.
CORIOLANUS:
To morrow,
When I know,
When meet I have patience.
BRUTUS:
I had more than h
[2024-11-09 20:07:09.573867][INFO][trainer.py:762] - Saving checkpoint to: /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16
[2024-11-09 20:07:09.575717][INFO][trainer.py:763] - Saving model to: /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16/model.pth
[2024-11-09 20:07:12.403506][INFO][configs.py:141] - Appending /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16 to /home/kevinfang/wordplay/src/ckpts/checkpoints.log
[2024-11-09 20:07:15.429031][INFO][trainer.py:892] - step=610 loss=0.150724 dt=0.294898 dtf=0.00644984 dtb=0.0221829 sps=27.128 sps_per_gpu=3.391 tps=1.77786e+06 tps_per_gpu=222233 mfu=43.0327
[2024-11-09 20:07:18.406807][INFO][trainer.py:892] - step=620 loss=0.0863345 dt=0.299016 dtf=0.0061005 dtb=0.0159788 sps=26.7544 sps_per_gpu=3.3443 tps=1.75338e+06 tps_per_gpu=219172 mfu=43.1078
[2024-11-09 20:07:21.388472][INFO][trainer.py:892] - step=630 loss=0.0626259 dt=0.302897 dtf=0.00650408 dtb=0.0167939 sps=26.4116 sps_per_gpu=3.30145 tps=1.73091e+06 tps_per_gpu=216364 mfu=43.1192
[2024-11-09 20:07:24.398580][INFO][trainer.py:892] - step=640 loss=0.0606946 dt=0.30517 dtf=0.00658476 dtb=0.0161353 sps=26.2149 sps_per_gpu=3.27686 tps=1.71802e+06 tps_per_gpu=214752 mfu=43.0973
[2024-11-09 20:07:27.404987][INFO][trainer.py:892] - step=650 loss=0.056873 dt=0.303179 dtf=0.0062306 dtb=0.0136271 sps=26.387 sps_per_gpu=3.29838 tps=1.7293e+06 tps_per_gpu=216162 mfu=43.1058
[2024-11-09 20:07:30.425912][INFO][trainer.py:892] - step=660 loss=0.354514 dt=0.306877 dtf=0.00675504 dtb=0.015822 sps=26.0691 sps_per_gpu=3.25864 tps=1.70846e+06 tps_per_gpu=213558 mfu=43.0613
[2024-11-09 20:07:33.445208][INFO][trainer.py:892] - step=670 loss=0.134486 dt=0.30056 dtf=0.00653609 dtb=0.0152208 sps=26.617 sps_per_gpu=3.32713 tps=1.74437e+06 tps_per_gpu=218047 mfu=43.111
[2024-11-09 20:07:36.494850][INFO][trainer.py:892] - step=680 loss=0.0764104 dt=0.306126 dtf=0.00645195 dtb=0.0169983 sps=26.133 sps_per_gpu=3.26663 tps=1.71266e+06 tps_per_gpu=214082 mfu=43.0765
[2024-11-09 20:07:39.489403][INFO][trainer.py:892] - step=690 loss=0.0567095 dt=0.300322 dtf=0.00642788 dtb=0.0158238 sps=26.6381 sps_per_gpu=3.32976 tps=1.74575e+06 tps_per_gpu=218219 mfu=43.1282
[2024-11-09 20:07:42.496350][INFO][trainer.py:892] - step=700 loss=0.0495633 dt=0.308562 dtf=0.00673808 dtb=0.0171983 sps=25.9267 sps_per_gpu=3.24084 tps=1.69913e+06 tps_per_gpu=212392 mfu=43.0582
[2024-11-09 20:07:43.662294][INFO][trainer.py:827] - ['prompt']: 'What is an LLM?'
[2024-11-09 20:07:43.664377][INFO][trainer.py:831] - ['response']:
What is an LLM?O Bushy, Bagot specticed
To Geor himself--accusate for him, I profess
The better new-men, desires.
HENRY BOLINGBROKE:
Here is thy time: my master is good forward
Hath pawder to keep you must be.
KING RICHARD II:
My many your soul death?
DUKE OF AUMERLE:
[2024-11-09 20:08:20.771680][INFO][trainer.py:762] - Saving checkpoint to: /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16
[2024-11-09 20:08:20.773502][INFO][trainer.py:763] - Saving model to: /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16/model.pth
[2024-11-09 20:08:23.593141][INFO][configs.py:141] - Appending /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16 to /home/kevinfang/wordplay/src/ckpts/checkpoints.log
[2024-11-09 20:08:26.586556][INFO][trainer.py:892] - step=710 loss=0.0465836 dt=0.293606 dtf=0.00620143 dtb=0.0145106 sps=27.2474 sps_per_gpu=3.40592 tps=1.78569e+06 tps_per_gpu=223211 mfu=43.2114
[2024-11-09 20:08:29.573996][INFO][trainer.py:892] - step=720 loss=0.0550064 dt=0.301726 dtf=0.00616519 dtb=0.0138501 sps=26.5141 sps_per_gpu=3.31427 tps=1.73763e+06 tps_per_gpu=217204 mfu=43.2292
[2024-11-09 20:08:32.597065][INFO][trainer.py:892] - step=730 loss=0.153065 dt=0.288127 dtf=0.00644146 dtb=0.0188749 sps=27.7655 sps_per_gpu=3.47069 tps=1.81964e+06 tps_per_gpu=227455 mfu=43.4501
[2024-11-09 20:08:35.574136][INFO][trainer.py:892] - step=740 loss=0.066891 dt=0.293076 dtf=0.00657163 dtb=0.0160024 sps=27.2967 sps_per_gpu=3.41208 tps=1.78891e+06 tps_per_gpu=223614 mfu=43.5721
[2024-11-09 20:08:38.553596][INFO][trainer.py:892] - step=750 loss=0.0489433 dt=0.30138 dtf=0.00635218 dtb=0.0161426 sps=26.5446 sps_per_gpu=3.31807 tps=1.73963e+06 tps_per_gpu=217453 mfu=43.5589
[2024-11-09 20:08:41.544657][INFO][trainer.py:892] - step=760 loss=0.0447545 dt=0.300141 dtf=0.00698229 dtb=0.0171991 sps=26.6541 sps_per_gpu=3.33176 tps=1.7468e+06 tps_per_gpu=218350 mfu=43.5649
[2024-11-09 20:08:44.511112][INFO][trainer.py:892] - step=770 loss=0.0401842 dt=0.293728 dtf=0.00746183 dtb=0.0259633 sps=27.2361 sps_per_gpu=3.40451 tps=1.78494e+06 tps_per_gpu=223118 mfu=43.6655
[2024-11-09 20:08:47.506000][INFO][trainer.py:892] - step=780 loss=0.0414722 dt=0.302556 dtf=0.00628471 dtb=0.014809 sps=26.4414 sps_per_gpu=3.30518 tps=1.73286e+06 tps_per_gpu=216608 mfu=43.626
[2024-11-09 20:08:50.513083][INFO][trainer.py:892] - step=790 loss=0.278426 dt=0.293464 dtf=0.00608121 dtb=0.0203071 sps=27.2606 sps_per_gpu=3.40758 tps=1.78655e+06 tps_per_gpu=223319 mfu=43.7246
[2024-11-09 20:08:53.502341][INFO][trainer.py:892] - step=800 loss=0.0878295 dt=0.300224 dtf=0.00706714 dtb=0.0204812 sps=26.6468 sps_per_gpu=3.33085 tps=1.74632e+06 tps_per_gpu=218291 mfu=43.7128
[2024-11-09 20:08:54.644293][INFO][trainer.py:827] - ['prompt']: 'What is an LLM?'
[2024-11-09 20:08:54.645246][INFO][trainer.py:831] - ['response']:
What is an LLM?INGBROKE:
As I long as the house of York,
That his o'clock, trusty, and gentlemen;
But or one read of kind with his presence,
And would the rest, whilst the torn in prious world,
Is the sent in with wealth in the sun,
The chain of manks and shrowd for his 
[2024-11-09 20:09:32.190306][INFO][trainer.py:762] - Saving checkpoint to: /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16
[2024-11-09 20:09:32.192167][INFO][trainer.py:763] - Saving model to: /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16/model.pth
[2024-11-09 20:09:35.012954][INFO][configs.py:141] - Appending /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16 to /home/kevinfang/wordplay/src/ckpts/checkpoints.log
[2024-11-09 20:09:38.005718][INFO][trainer.py:892] - step=810 loss=0.0474592 dt=0.295612 dtf=0.0065251 dtb=0.0147772 sps=27.0625 sps_per_gpu=3.38281 tps=1.77357e+06 tps_per_gpu=221696 mfu=43.7703
[2024-11-09 20:09:40.986994][INFO][trainer.py:892] - step=820 loss=0.0411391 dt=0.297151 dtf=0.00754408 dtb=0.0164562 sps=26.9223 sps_per_gpu=3.36529 tps=1.76438e+06 tps_per_gpu=220548 mfu=43.799
[2024-11-09 20:09:43.955502][INFO][trainer.py:892] - step=830 loss=0.0379784 dt=0.302816 dtf=0.0062668 dtb=0.0145679 sps=26.4187 sps_per_gpu=3.30234 tps=1.73138e+06 tps_per_gpu=216422 mfu=43.7425
[2024-11-09 20:09:46.955431][INFO][trainer.py:892] - step=840 loss=0.0398498 dt=0.289308 dtf=0.00673165 dtb=0.0186647 sps=27.6522 sps_per_gpu=3.45652 tps=1.81221e+06 tps_per_gpu=226526 mfu=43.8935
[2024-11-09 20:09:49.940713][INFO][trainer.py:892] - step=850 loss=0.0417054 dt=0.296685 dtf=0.00653358 dtb=0.0152698 sps=26.9646 sps_per_gpu=3.37057 tps=1.76715e+06 tps_per_gpu=220894 mfu=43.9168
[2024-11-09 20:09:52.933075][INFO][trainer.py:892] - step=860 loss=0.215297 dt=0.295801 dtf=0.00640054 dtb=0.0198991 sps=27.0452 sps_per_gpu=3.38065 tps=1.77243e+06 tps_per_gpu=221554 mfu=43.951
[2024-11-09 20:09:55.917389][INFO][trainer.py:892] - step=870 loss=0.065915 dt=0.300704 dtf=0.013056 dtb=0.0238553 sps=26.6042 sps_per_gpu=3.32553 tps=1.74353e+06 tps_per_gpu=217942 mfu=43.9097
[2024-11-09 20:09:58.915523][INFO][trainer.py:892] - step=880 loss=0.0431866 dt=0.295528 dtf=0.0062917 dtb=0.0144305 sps=27.0702 sps_per_gpu=3.38378 tps=1.77407e+06 tps_per_gpu=221759 mfu=43.9487
[2024-11-09 20:10:01.901700][INFO][trainer.py:892] - step=890 loss=0.0373346 dt=0.299605 dtf=0.00629097 dtb=0.0152616 sps=26.7018 sps_per_gpu=3.33773 tps=1.74993e+06 tps_per_gpu=218741 mfu=43.9235
[2024-11-09 20:10:04.920887][INFO][trainer.py:892] - step=900 loss=0.034101 dt=0.293815 dtf=0.00670316 dtb=0.0207335 sps=27.228 sps_per_gpu=3.4035 tps=1.78442e+06 tps_per_gpu=223052 mfu=43.987
[2024-11-09 20:10:06.070198][INFO][trainer.py:827] - ['prompt']: 'What is an LLM?'
[2024-11-09 20:10:06.071525][INFO][trainer.py:831] - ['response']:
What is an LLM?BOND:
'Tis speech for and judge.'
GREEN:
Well, then, in Broke and of peace! it is made better now
That Rome will be as well perform'd to Richard.
BUCKINGHAM:
I fear not, my lord, with all my true appeal,
Tell Keep in Sixely, while you and kingdom
The gen
[2024-11-09 20:10:43.211201][INFO][trainer.py:762] - Saving checkpoint to: /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16
[2024-11-09 20:10:43.213019][INFO][trainer.py:763] - Saving model to: /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16/model.pth
[2024-11-09 20:10:46.031719][INFO][configs.py:141] - Appending /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16 to /home/kevinfang/wordplay/src/ckpts/checkpoints.log
[2024-11-09 20:10:49.072019][INFO][trainer.py:892] - step=910 loss=0.0357021 dt=0.291862 dtf=0.00658027 dtb=0.0190143 sps=27.4102 sps_per_gpu=3.42628 tps=1.79636e+06 tps_per_gpu=224544 mfu=44.0739
[2024-11-09 20:10:52.067792][INFO][trainer.py:892] - step=920 loss=0.0383639 dt=0.286074 dtf=0.00670409 dtb=0.0157774 sps=27.9648 sps_per_gpu=3.49559 tps=1.8327e+06 tps_per_gpu=229087 mfu=44.2429
[2024-11-09 20:10:55.054536][INFO][trainer.py:892] - step=930 loss=0.0408959 dt=0.31063 dtf=0.00649649 dtb=0.0177853 sps=25.7541 sps_per_gpu=3.21926 tps=1.68782e+06 tps_per_gpu=210978 mfu=44.0332
[2024-11-09 20:10:58.023793][INFO][trainer.py:892] - step=940 loss=0.24583 dt=0.297392 dtf=0.00638411 dtb=0.01504 sps=26.9005 sps_per_gpu=3.36256 tps=1.76295e+06 tps_per_gpu=220369 mfu=44.0321
[2024-11-09 20:11:00.985056][INFO][trainer.py:892] - step=950 loss=0.063754 dt=0.296985 dtf=0.00628618 dtb=0.0145605 sps=26.9374 sps_per_gpu=3.36717 tps=1.76537e+06 tps_per_gpu=220671 mfu=44.0371
[2024-11-09 20:11:03.969651][INFO][trainer.py:892] - step=960 loss=0.0400992 dt=0.292001 dtf=0.00685426 dtb=0.0269023 sps=27.3971 sps_per_gpu=3.42464 tps=1.7955e+06 tps_per_gpu=224437 mfu=44.1169
[2024-11-09 20:11:06.942517][INFO][trainer.py:892] - step=970 loss=0.0353416 dt=0.293041 dtf=0.00655513 dtb=0.0197062 sps=27.3 sps_per_gpu=3.4125 tps=1.78913e+06 tps_per_gpu=223641 mfu=44.1728
[2024-11-09 20:11:09.929995][INFO][trainer.py:892] - step=980 loss=0.033058 dt=0.283214 dtf=0.00699655 dtb=0.019587 sps=28.2472 sps_per_gpu=3.5309 tps=1.85121e+06 tps_per_gpu=231401 mfu=44.3781
[2024-11-09 20:11:12.915783][INFO][trainer.py:892] - step=990 loss=0.0304791 dt=0.297545 dtf=0.0066327 dtb=0.0147127 sps=26.8867 sps_per_gpu=3.36084 tps=1.76205e+06 tps_per_gpu=220256 mfu=44.3403
[2024-11-09 20:11:15.959949][INFO][trainer.py:892] - step=1000 loss=0.0347885 dt=0.549696 dtf=0.00629105 dtb=0.273606 sps=14.5535 sps_per_gpu=1.81919 tps=953779 tps_per_gpu=119222 mfu=42.2879
[2024-11-09 20:11:17.110482][INFO][__main__.py:119] - ['prompt']: 'What is an LLM?'
[2024-11-09 20:11:17.112126][INFO][__main__.py:120] - ['response']:
What is an LLM?WIw becoment your lives best I make, become my lost;
And when you will not what the queen is well:
How some will be the year that is the night
When you can no way to use him with and distress'd.
LUCENTIO:
And then affections and that answer the proclaim'd
[2024-11-09 20:11:17.114534][INFO][trainer.py:762] - Saving checkpoint to: /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16
[2024-11-09 20:11:17.115115][INFO][trainer.py:763] - Saving model to: /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16/model.pth
[2024-11-09 20:11:19.927344][INFO][configs.py:141] - Appending /home/kevinfang/outputs/runs/pytorch/DDP/2024-11-09/19-59-16 to /home/kevinfang/wordplay/src/ckpts/checkpoints.log
wandb: - 0.238 MB of 0.238 MB uploaded
wandb: Run history:
wandb:                      Loss/iter ▁▁▁▁▂▂▂▂▂▃▃▃▃▃▃▄▄▄▄▄▅▅▅▅▅▅▆▆▆▆▆▇▇▇▇▇▇███
wandb:                     Loss/lossf █▇▆▆▆▆▆▆▅▅▄▄▄▄▄▃▃▃▃▂▂▂▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁
wandb:                       Loss/mfu █▇▆▆▅▄▄▄▃▃▃▃▃▃▃▂▂▃▂▃▃▃▃▂▂▂▃▃▃▃▄▄▄▄▄▄▅▄▄▁
wandb:                     Loss/train ████▅▅▅▅▄▄▄▄▃▃▃▃▃▃▃▃▂▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:                       Loss/val ████▃▃▃▃▂▂▂▂▁▁▁▁▁▁▁▁▃▃▃▃▆▆▆▆▇▇▇▇▆▆▆▆▇▇▇▇
wandb:                  Timing/dt_avg ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█
wandb:                 Timing/dt_iter ▁▁▂▁▂▂▁▂▁▂▁▁▂▁▁▂▁▁▂▁▁▁▂▂▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁█
wandb:                  Timing/dt_tot ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█
wandb:                 Timing/dtb_avg ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█
wandb:                 Timing/dtb_tot ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█
wandb:                 Timing/dtf_avg ▂▂▂▂▁▂▁▁▁▁▅▂▁▁▂▁▁▁▁▂▂▂▂▁▁▂▁▁▁▁▂▁▂▂█▁▂▁▁▁
wandb:                 Timing/dtf_tot ▂▂▂▂▁▂▁▁▁▁▅▂▁▁▂▁▁▁▁▂▂▂▂▁▁▂▁▁▁▁▂▁▂▂█▁▂▁▁▁
wandb:                    Timing/iter ▁▁▁▁▂▂▂▂▂▃▃▃▃▃▃▄▄▄▄▄▅▅▅▅▅▅▆▆▆▆▆▇▇▇▇▇▇███
wandb:         Timing/samples_per_sec █▇▇█▇▇▇▇▇▇▇█▇██▇▇▇▆▇▇█▇▆▇▇▇▇▇███▇█▇▇█▇█▁
wandb: Timing/samples_per_sec_per_gpu █▇▇█▇▇▇▇▇▇▇█▇██▇▇▇▆▇▇█▇▆▇▇▇▇▇███▇█▇▇█▇█▁
wandb:            Timing/startup_time ▁
wandb:          Timing/tokens_per_sec █▇▇█▇▇▇▇▇▇▇█▇██▇▇▇▆▇▇█▇▆▇▇▇▇▇███▇█▇▇█▇█▁
wandb:  Timing/tokens_per_sec_per_gpu █▇▇█▇▇▇▇▇▇▇█▇██▇▇▇▆▇▇█▇▆▇▇▇▇▇███▇█▇▇█▇█▁
wandb:                  Training/iter ▁▁▁▁▂▂▂▂▂▃▃▃▃▃▃▄▄▄▄▄▅▅▅▅▅▅▆▆▆▆▆▇▇▇▇▇▇███
wandb:                  Training/loss █▇▆▆▆▆▆▆▅▅▄▄▄▄▄▃▃▃▃▂▂▂▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁
wandb:              Training/loss_tot █▇▆▆▆▆▆▆▅▅▄▄▄▄▄▃▃▃▃▂▂▂▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁
wandb:                    Training/lr ▁▃▅▆████████████████████████████████████
wandb:                         dt_avg ▁▆▂▂▇▆▁▅▂▂▆▂█▁▄▆▆▃▂▂▁▂▂▂▂▂▂▂▁▂▂▂▁▃▂▁▂▁▂▂
wandb:                        dt_iter ▂▃▄▁▅█▃▃▃▃▄▂▃▅▂▇▃▂▁▅▅▂▄▄▂▄▄▄▃▃▃▁▅▁▂▅▁▃▅▂
wandb:                         dt_tot ▁▆▂▂▇▆▁▅▂▂▆▂█▁▄▆▆▃▂▂▁▂▂▂▂▂▂▂▁▂▂▂▁▃▂▁▂▁▂▂
wandb:                            dtb ▁▂▂▂█▇▁▆▃▂▂▂▄▁▄▆▆▃▁▂▁▂▂▂▂▂▂▂▁▂▂▂▁▃▂▁▂▁▂▂
wandb:                        dtb_avg ▁▂▂▂█▇▁▆▃▂▂▂▄▁▄▆▆▃▁▂▁▂▂▂▂▂▂▂▁▂▂▂▁▃▂▁▂▁▂▂
wandb:                        dtb_tot ▁▂▂▂█▇▁▆▃▂▂▂▄▁▄▆▆▃▁▂▁▂▂▂▂▂▂▂▁▂▂▂▁▃▂▁▂▁▂▂
wandb:                            dtf ▁█▁▁▁▁▁▁▁▂█▁█▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:                        dtf_avg ▁█▁▁▁▁▁▁▁▂█▁█▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:                        dtf_tot ▁█▁▁▁▁▁▁▁▂█▁█▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:                           iter ▁▁▁▂▂▂▂▂▂▃▃▃▃▃▄▄▄▄▄▄▅▅▅▅▅▅▆▆▆▆▆▇▇▇▇▇▇███
wandb:                           loss █▇▆▆▆▆▆▆▅▅▅▄▄▄▄▃▃▃▃▂▂▂▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁
wandb:                       loss_tot █▇▆▆▆▆▆▆▅▅▅▄▄▄▄▃▃▃▃▂▂▂▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁
wandb:                             lr ▁▃▅▆████████████████████████████████████
wandb:                samples_per_sec ▇▆▅▇▄▁▅▆▆▆▅▇▅▄▇▂▆▇█▄▄▇▅▄▇▅▅▅▅▆▆▇▃▇▇▄█▆▄▇
wandb:        samples_per_sec_per_gpu ▇▆▅▇▄▁▅▆▆▆▅▇▅▄▇▂▆▇█▄▄▇▅▄▇▅▅▅▅▆▆▇▃▇▇▄█▆▄▇
wandb:                 tokens_per_sec ▇▆▅▇▄▁▅▆▆▆▅▇▅▄▇▂▆▇█▄▄▇▅▄▇▅▅▅▅▆▆▇▃▇▇▄█▆▄▇
wandb:         tokens_per_sec_per_gpu ▇▆▅▇▄▁▅▆▆▆▅▇▅▄▇▂▆▇█▄▄▇▅▄▇▅▅▅▅▆▆▇▃▇▇▄█▆▄▇
wandb: 
wandb: Run summary:
wandb:                      Loss/iter 1000
wandb:                     Loss/lossf 0.03479
wandb:                       Loss/mfu 42.28789
wandb:                     Loss/train 0.03446
wandb:                       Loss/val 3.97037
wandb:                  Timing/dt_avg 0.13995
wandb:                 Timing/dt_iter 0.5497
wandb:                  Timing/dt_tot 0.2799
wandb:                 Timing/dtb_avg 0.27361
wandb:                 Timing/dtb_tot 0.27361
wandb:                 Timing/dtf_avg 0.00629
wandb:                 Timing/dtf_tot 0.00629
wandb:                    Timing/iter 999
wandb:         Timing/samples_per_sec 14.55351
wandb: Timing/samples_per_sec_per_gpu 1.81919
wandb:            Timing/startup_time 8.68931
wandb:          Timing/tokens_per_sec 953778.9143
wandb:  Timing/tokens_per_sec_per_gpu 119222.36429
wandb:                  Training/iter 999
wandb:                  Training/loss 0.03479
wandb:              Training/loss_tot 0.03479
wandb:                    Training/lr 0.0006
wandb:                         dt_avg 0.13995
wandb:                        dt_iter 0.5497
wandb:                         dt_tot 0.2799
wandb:                            dtb 0.27361
wandb:                        dtb_avg 0.27361
wandb:                        dtb_tot 0.27361
wandb:                            dtf 0.00629
wandb:                        dtf_avg 0.00629
wandb:                        dtf_tot 0.00629
wandb:                           iter 999
wandb:                           loss 0.03479
wandb:                       loss_tot 0.03479
wandb:                             lr 0.0006
wandb:                samples_per_sec 14.55351
wandb:        samples_per_sec_per_gpu 1.81919
wandb:                 tokens_per_sec 953778.9143
wandb:         tokens_per_sec_per_gpu 119222.36429
wandb: 
wandb: 🚀 View run vocal-forest-1 at: https://wandb.ai/26kfang-stratford-school/WordPlay/runs/snrgerlv
wandb: ⭐️ View project at: https://wandb.ai/26kfang-stratford-school/WordPlay
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20241109_195921-snrgerlv/logs
wandb: WARNING The new W&B backend becomes opt-out in version 0.18.0; try it out with `wandb.require("core")`! See https://wandb.me/wandb-core for more information.
```
</details>

<!--[^gpu]: If you do not have access to the ALCF systems, you can install [OpenMPI](https://docs.open-mpi.org/en/v5.0.x/) and run across multiple CPUs as well-->
