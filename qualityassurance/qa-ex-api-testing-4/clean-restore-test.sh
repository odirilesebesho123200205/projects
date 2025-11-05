#! /bin/sh

# This file must be copied to the submission/ directory in the grading repo
# And then it will be in the right place.
cd $(dirname $0)

# horrible hack because student projects do not have an ENV var for the petstore uri
# and swaggerapi/petstore (name 'petstore' in docker-compose.yml) will ONLY serve on 8080
sed -i -e "s/localhost/petstore:8080/" PetstoreTests/BaseTest.cs

# do a proper clean because students sometimes check in all their build files
rm -rf $(find . \( -name bin -o -name obj \))
dotnet clean

# probably not strictly necessary
dotnet restore

# and finally run the test suite
dotnet test