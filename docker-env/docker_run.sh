# add a check that the current path ends with docker-env
if [ "${PWD: -10}" != "docker-env" ]; then
    echo "Please run this script from the docker-env directory"
    exit 1
fi

docker run --name matchfixagent_container -d -t \
    --mount type=bind,source=$PWD/..,target=/workspace/ \
    matchfixagent
docker ps | grep matchfixagent_container
echo "# The container is running. To stop running the container: bash docker_stop.sh"