# clobber student code

cp ./Applications/PetStore/OpenApiClient $1/Applications/PetStore/OpenApiClient
cp ./clean-restore-test.sh $1/clean-restore-test.sh

# run grading

cd $1
docker-compose run grader
docker-compose down