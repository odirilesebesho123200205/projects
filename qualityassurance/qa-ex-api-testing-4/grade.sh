# clobber student code

# check if PetstoreTests directory exists
checkdir="$1/PetStore"

if [ ! -d "$checkdir" ]; then
    echo "ERROR: PetStore directory does not exist in $1"
    exit 1
fi

cp ./PetStore.csproj $1/PetStore/PetStore.csproj
cp ./clean-restore-test.sh $1/clean-restore-test.sh
cp ./docker-compose.yml $1/docker-compose.yml

cp -r ./OpenApiClient $1/PetStore/OpenApiClient
cp ./clean-restore-test.sh $1/clean-restore-test.sh

# run grading

cd $1
docker-compose run grader
docker-compose down