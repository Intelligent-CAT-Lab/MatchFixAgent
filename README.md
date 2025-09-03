# MatchFixAgent: Language-Agnostic Autonomous Repository-Level Code Translation Validation and Repair

MatchFixAgent is a language-agnostic neuro-symbolic approach for autonomous repository-level code translation validation and repair. MatchFixAgent leverages static semantic analysis combined with Large Language Model (LLM) agents to validate translations and repair bugs across multiple PLs efficiently. To simplify the problem for LLM agents, MatchFixAgent performs multifaceted semantic analyses—including control-flow and data-flow analyses—to systematically generate targeted tests, enabling demonstration of functional equivalence or detection of semantic bugs.

## Docker Container

For re-running and evaluating MatchFixAgent on more projects, we recommend using our [`Dockerfile`](./docker-env/Dockerfile) to build a docker image. All required dependencies are installed during `docker build`, making it easier for users to interact with MatchFixAgent.

To build a new image from scratch and run it inside a container:

```bash
cd docker-env                             # change directory to docker-env
bash docker_build.sh                      # build docker image
bash docker_run.sh <container_name>       # run docker image in a docker container
bash docker_shell.sh <container_name>     # open an interactive shell to docker container
```

If you want to check our results in the paper, please download and run our docker snapshots from [Zenodo](). There are 23 images, each corresponding to a specific project. Each image includes log files, agent trajectories, git branches for every source and target fragment pair.

```bash
docker load -i <image_name>.tar                                                               # load docker image (.tar file downloaded from Zenodo)
docker image list                                                                             # verify image has been loaded properly
docker run --name <container_name> -d -t <image_name>                                         # run docker image in a docker container
docker exec -it -w /workspace -e NODE_PATH=/usr/lib/node_modules <container_name> /bin/bash   # open an interactive shell to docker container
```

## Credentials

### Claude Code

The main experiments in MatchFixAgent uses [Claude Code](https://github.com/anthropics/claude-code) as its LLM agent powered by [Claude Sonnet](https://www.anthropic.com/claude/sonnet) model. We use [AWS Amazon Bedrock](https://aws.amazon.com/bedrock/) as provider to interact with the Claude model. To reproduce our results, you are required to make sure your AWS account has Claude model enabled in your desired region. Please configure your credentials in [`aws_credentials.yaml`](./configs/aws_credentials.yaml) by pasting your `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `region`, and `model` information. A sample AWS credential is shown below:

```yaml
aws_credentials:
  one:
    AWS_ACCESS_KEY_ID: <PASTE_YOUR_AWS_ACCESS_KEY_ID>
    AWS_SECRET_ACCESS_KEY: <PASTE_YOUR_AWS_SECRET_ACCESS_KEY>
    region: us-west-2
    model: us.anthropic.claude-3-7-sonnet-20250219-v1:0
```

This assumes you have enabled access to `us.anthropic.claude-3-7-sonnet-20250219-v1:0` in region `us-west-2`. Please see [AWS Amazon Bedrock](https://aws.amazon.com/bedrock/) on more information on how to get AWS credentials and enable model access. Moreover, MatchFixAgent supports dynamic selection of credentials to avoid quota problems. Please add more credentials similar to `one`, and make sure to extend `available_credentials` in experiment configurations. Here is a sample [configuration](./configs/oxidizer/match_agent_oxidizer_checkdigit_go_rust.yaml).

### Codex

MatchFixAgent can be configured with other LLM agents and models. In our experiments, we show the adaptability of MatchFixAgent with OpenAI Codex agent and model. Please configure your credentials in [`openai_credentials.yaml`](./configs/openai_credentials.yaml) by pasting your `OPENAI_API_KEY` and `model` information. A sample OpenAI credential is shown below:

```yaml
openai_credentials:
  one:
    OPENAI_API_KEY: <PASTE_YOUR_OPENAI_API_KEY>
    model: o4-mini-2025-04-16
```

Furthermore, Codex supports other LLMs, specifically open-source LLMs from [Open Router](https://openrouter.ai/). Please refer to [Codex README](https://github.com/openai/codex/blob/main/README.md) for more information on how to configure open-source LLMs.

## Reproducing Results

MatchFixAgent depends on well-defined configuaration files to run properly. We provide all configuration files required for reproducing MatchFixAgent results in [configs](./configs).

### RQ1

To run the experiment for translation validation, please execute the following script with the configuration file of your agent, tool and project. For instance, the following runs the experiment for `tool=oxidizer`, `project=checkdigit`, and `agent=match_agent`.

```bash
bash scripts/run_validation.sh configs/oxidizer/match_agent_oxidizer_checkdigit_go_rust.yaml
```

To check the effectiveness of MatchFixAgent, execute the following script to save results under `reports`:

```bash
bash scripts/analyze_validator_agent.sh match_agent oxidizer checkdigit
```

To replay the trajectory of the agent, execute the following script with the trajectory file you want to visualize. Trajectory files are stored under `data/agent_trajectories/claude` and named after `session_id` of the agent conversation. You can find the session ID from the results in `data/agent_results`.

```bash
python src/analysis/visualize_trajectory.py <path_to_trajectory_file>
```

### RQ2

MatchFixAgent generates patches for incorrect translations. Please execute the following script with the configuration file of your agent, tool and project. For instance, the following runs the experiment for `tool=oxidizer`, `project=checkdigit`, and `agent=match_agent`.

```bash
bash scripts/run_repair.sh configs/oxidizer/match_agent_oxidizer_checkdigit_go_rust.yaml
```

Prior to running the above command, please download and place `original_tool_projects.zip` in the repository directory from [Zenodo]().

### RQ3

To show the adaptability of MatchFixAgent with other LLM agents and models, we use OpenAI Codex and `o4-mini-2025-04-16`. Please execute the following script with the configuration file of your agent, tool and project. For instance, the following runs the experiment for `tool=oxidizer`, `project=checkdigit`, and `agent=openai_agent`.

```bash
bash scripts/run_validation.sh configs/oxidizer/openai_agent_oxidizer_checkdigit_go_rust.yaml
```

This experiment only focus on up to 4 samples from every project. If you need to run the experiment on all samples, please make necessary changes in [`sample_openai_study`](./src/analysis/sample_openai_study.py) file.

### RQ4

To evaluate the impact of different components in MatchFixAgent, we perform an ablation study and run the Claude agent by itself without semantic analyses and targeted test generation. Please execute the following script with the configuration file of your agent, tool and project. For instance, the following runs the experiment for `tool=oxidizer`, `project=checkdigit`, and `agent=base_agent`.

```bash
bash scripts/run_validation.sh configs/oxidizer/base_agent_oxidizer_checkdigit_go_rust.yaml
```

We perform another ablation study and run MatchFixAgent without semantic analyses. Please execute the following script with the configuration file of your agent, tool and project. For instance, the following runs the experiment for `tool=oxidizer`, `project=checkdigit`, and `agent=test_agent`.

```bash
bash scripts/run_validation.sh configs/oxidizer/test_agent_oxidizer_checkdigit_go_rust.yaml
```

## Building on MatchFixAgent

### Evaluating More Projects

You can evaluate MatchFixAgent on other projects. Please make sure you have:

- Well-defined experiment configuration files
- Store your fragments properly under [`data/agent_results`](./data/agent_results)
- Store your codebases properly under [`data/tool_projects`](./data/tool_projects)

### Extending Supported Languages

If you need to experiment with other programming languages not supported by MatchFixAgent, please add necessary scripts under [`src/static_analysis`](./src/static_analysis). You are only required to define the `CFGBuilder` class and decide on semantics of branching statements.

### MCP Servers

MatchFixAgent by default uses one custom MCP server, called `DirectoryTreeExplorer`. If you need to add more MCP servers, please add them under [`src/mcp`](./src/mcp) and configure them in [`claude_mcp_config.json`](./configs/claude_mcp_config.json) and [`codex_mcp_config.toml`](./configs/codex_mcp_config.toml). You may also need to update the [`Claude Memory`](./CLAUDE.local.md) and [`Codex Memory`](./AGENTS.md) files.
