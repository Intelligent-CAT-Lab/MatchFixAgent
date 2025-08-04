FROM python:3.12.9

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV NODE_PATH=/usr/local/lib/node_modules

# Install required system packages
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    build-essential \
    git \
    vim \
    nano \
    less \
    && rm -rf /var/lib/apt/lists/*

# Install Go 1.24.4
RUN wget https://go.dev/dl/go1.24.4.linux-amd64.tar.gz \
    && tar -C /usr/local -xzf go1.24.4.linux-amd64.tar.gz \
    && rm go1.24.4.linux-amd64.tar.gz

# Install Rust 1.87.0
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --default-toolchain 1.87.0 \
    && . ~/.cargo/env \
    && rustup default 1.87.0

# Install Java 21 (Amazon Corretto)
RUN wget https://corretto.aws/downloads/latest/amazon-corretto-21-x64-linux-jdk.tar.gz \
    && tar -C /usr/local -xzf amazon-corretto-21-x64-linux-jdk.tar.gz \
    && rm amazon-corretto-21-x64-linux-jdk.tar.gz \
    && mv /usr/local/amazon-corretto-* /usr/local/java

# Install Maven 3.9.9
RUN wget https://archive.apache.org/dist/maven/maven-3/3.9.9/binaries/apache-maven-3.9.9-bin.tar.gz \
    && tar -C /usr/local -xzf apache-maven-3.9.9-bin.tar.gz \
    && rm apache-maven-3.9.9-bin.tar.gz \
    && mv /usr/local/apache-maven-3.9.9 /usr/local/maven

# Download & unpack exactly Node.js v22.16.0
RUN curl -fsSL https://nodejs.org/dist/v22.16.0/node-v22.16.0-linux-x64.tar.xz \
     | tar -xJ -C /usr/local --strip-components=1 \
     && npm install -g npm@11.4.0

# Update PATH to include all tools
ENV PATH="/usr/local/go/bin:/root/.cargo/bin:/usr/local/java/bin:/usr/local/maven/bin:${NODE_PATH}/.bin:${PATH}"
ENV JAVA_HOME="/usr/local/java"
ENV MAVEN_HOME="/usr/local/maven"
ENV GOPATH="/go"
ENV GOROOT="/usr/local/go"

# Create Go workspace
RUN mkdir -p /go/bin /go/src /go/pkg

# Verify installations
RUN node -v && npm -v \
    && go version \
    && rustc --version \
    && java -version \
    && mvn -version \
    && python --version \
    && gcc --version

# Install Node.js packages globally
RUN npm install -g \
    crc-32@1.2.2 \
    numjs@0.16.1 \
    @anthropic-ai/claude-code@1.0.67 \
    @openai/codex@0.11.0


# Install Python packages
RUN pip install --no-cache-dir \
    tree-sitter==0.24.0 \
    tree-sitter-languages==1.10.2 \
    tree-sitter-c==0.23.4 \
    tree-sitter-go==0.23.4 \
    tree-sitter-javascript==0.23.1 \
    tree-sitter-python==0.23.6 \
    tree-sitter-rust==0.23.2 \
    tree-sitter-java==0.23.5 \
    openai==1.98.0 \
    boto3==1.38.20 \
    pandas==2.2.3 \
    fastmcp==2.8.0 \
    graphviz==0.20.3 \
    matplotlib==3.10.5 \
    networkx==3.5 \
    seaborn==0.13.2 \
    scikit-learn==1.7.1 \
    pyyaml==6.0.2 \
    jinja2==3.1.6 \
    astor==0.8.1 \
    pydot==3.0.4

# Configure shell with basic coloring
RUN echo 'export TERM=xterm-256color' >> /root/.bashrc \
    && echo 'alias ls="ls --color=auto"' >> /root/.bashrc \
    && echo 'alias grep="grep --color=auto"' >> /root/.bashrc \
    && echo 'PS1="\[\033[1;36m\]\u\[\033[1;31m\]@\[\033[1;32m\]\h:\[\033[1;35m\]\w\[\033[1;31m\]\$\[\033[0m\] "' >> /root/.bashrc


# Set working directory
WORKDIR /app

# Default command
CMD ["/bin/bash"]