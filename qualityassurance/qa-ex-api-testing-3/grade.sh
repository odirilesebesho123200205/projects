# clobber student code

cp ./PetStoreTests/Api $1/PetStoreTests/Api
cp ./PetStoreTests/Client $1/PetStoreTests/Client
cp ./PetStoreTests/Model $1/PetStoreTests/Model

cp ./PetstoreTests.csproj $1/PetstoreTests/PetstoreTests.csproj
cp ./clean-restore-test.sh $1/clean-restore-test.sh

# run grading

cd $1
docker-compose run grader
docker-compose down