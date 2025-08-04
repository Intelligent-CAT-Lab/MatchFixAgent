# MatchFixAgent: Language-Agnostic Autonomous Repository-Level Code Translation Validation and Repair

MatchFixAgent is a language-agnostic neuro-symbolic approach for autonomous repository-level
code translation validation and repair. MatchFixAgent leverages static semantic analysis combined with
Large Language Model (LLM) agents to validate translations and repair bugs across multiple PLs efficiently. To
simplify the problem for LLM agents, MatchFixAgent performs multifaceted semantic analyses—including
control-flow and data-flow analyses—to systematically generate targeted tests, enabling demonstration of
functional equivalence or detection of semantic bugs.

## Docker Container

For reproducing our results and evaluating MatchFixAgent on more projects, we recommend using our [`Dockerfile`](./docker-env/Dockerfile) to build a docker image. All required dependencies are installed during `docker build`, making it easier for users to interact with MatchFixAgent.

To build a new image from scratch and run it inside a container:

```bash
cd docker-env           # change directory to docker-env
bash docker_build.sh    # build docker image
bash docker_run.sh      # run docker image in a docker container
bash docker_shell.sh    # open an interactive shell to docker container
```

If you want to delete the image and container:

```bash
bash docker_stop.sh     # delete docker container
bash docker_rmi.sh      # delete docker image
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

This assumes you have enabled access to `us.anthropic.claude-3-7-sonnet-20250219-v1:0` in region `us-west-2`. Please see [AWS Amazon Bedrock](https://aws.amazon.com/bedrock/) on more information on how to get AWS credentials and enable model access.

> [!NOTE]
> MatchFixAgent supports dynamic selection of credentials to avoid quota problems. Please add more credentials similar to `one`, and make sure to extend `available_credentials` in experiment configurations. Here is a sample [configuration](./configs/oxidizer/match_agent_oxidizer_checkdigit_go_rust.yaml).

### Codex

MatchFixAgent can be configured with other LLM agents and models. In our experiments, we show the adaptability of MatchFixAgent with OpenAI Codex agent and model. Please configure your credentials in [`openai_credentials.yaml`](./configs/openai_credentials.yaml) by pasting your `OPENAI_API_KEY` and `model` information. A sample OpenAI credential is shown below:

```yaml
aws_credentials:
  one:
    AWS_ACCESS_KEY_ID: <PASTE_YOUR_AWS_ACCESS_KEY_ID>
    AWS_SECRET_ACCESS_KEY: <PASTE_YOUR_AWS_SECRET_ACCESS_KEY>
    region: us-west-2
    model: us.anthropic.claude-3-7-sonnet-20250219-v1:0
```

This assumes you have enabled access to `us.anthropic.claude-3-7-sonnet-20250219-v1:0` in region `us-west-2`. Please see [AWS Amazon Bedrock](https://aws.amazon.com/bedrock/) on more information on how to get AWS credentials and enable model access.

```yaml
openai_credentials:
  one:
    OPENAI_API_KEY: <PASTE_YOUR_OPENAI_API_KEY>
    model: o4-mini-2025-04-16
```

</details>

## Reproducing Results

### RQ1
### RQ2
### RQ3
### RQ4

