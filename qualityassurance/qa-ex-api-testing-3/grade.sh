# clobber student code

# check if PetstoreTests directory exists
checkdir="$1/PetStoreTests"

if [ ! -d "$checkdir" ]; then
    echo "ERROR: PetStoreTests directory does not exist in $1"
    exit 1
fi

cp ./PetStoreTests/Api $1/PetStoreTests/Api
cp ./PetStoreTests/Client $1/PetStoreTests/Client
cp ./PetStoreTests/Model $1/PetStoreTests/Model

cp ./PetStoreTests.csproj $1/PetStoreTests/PetStoreTests.csproj
cp ./clean-restore-test.sh $1/clean-restore-test.sh
cp ./docker-compose.yml $1/docker-compose.yml

# run grading

cd $1
docker-compose run grader
docker-compose down