# add a check that the current path ends with docker-env
if [ "${PWD: -10}" != "docker-env" ]; then
    echo "Please run this script from the docker-env directory"
    exit 1
fi

mkdir -p ../logs
mkdir -p ../reports

docker run --name matchfixagent_container -d -t \
    --mount type=bind,source=$PWD/../configs,target=/workspace/configs \
    --mount type=bind,source=$PWD/../data,target=/workspace/data \
    --mount type=bind,source=$PWD/../.gitignore,target=/workspace/.gitignore \
    --mount type=bind,source=$PWD/../.gitattributes,target=/workspace/.gitattributes \
    --mount type=bind,source=$PWD/../.claude,target=/workspace/.claude \
    --mount type=bind,source=$PWD/../README.md,target=/workspace/README.md \
    --mount type=bind,source=$PWD/../AGENTS.md,target=/workspace/AGENTS.md \
    --mount type=bind,source=$PWD/../CLAUDE.local.md,target=/workspace/CLAUDE.local.md \
    --mount type=bind,source=$PWD/../scripts,target=/workspace/scripts \
    --mount type=bind,source=$PWD/../src,target=/workspace/src \
    --mount type=bind,source=$PWD/../logs,target=/workspace/logs \
    --mount type=bind,source=$PWD/../reports,target=/workspace/reports \
    matchfixagent

docker ps | grep matchfixagent_container
echo "# The container is running. To stop running the container: bash docker_stop.sh"