# add a check that the current path ends with docker-env
if [ "${PWD: -10}" != "docker-env" ]; then
    echo "Please run this script from the docker-env directory"
    exit 1
fi

# remove the matchfixagent image
if [ "$(docker images -q matchfixagent 2> /dev/null)" ]; then
    docker rmi matchfixagent
    echo "# The image is removed. Please run ./docker_build.sh to build it again if needed."
else
    echo "# No matchfixagent image found. Nothing to remove."
fi
