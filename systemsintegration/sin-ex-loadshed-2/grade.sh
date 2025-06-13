echo "Copy solution tests to submission dir"
cp -rf ./grading/places/src/test $1/places/src
cp -rf ./grading/schedule/src/test $1/schedule/src
cp -rf ./grading/stage/src/test $1/stage/src

echo "Copy test CSV to submission dir"
cp ./grading/places/resources/PlaceNamesZA2008.csv $1/places/resources

echo "Changing to dir $1"
cd $1

if [ ! -e pom.xml ]; then
    echo "pom.xml was not found - please ensure you have a valid Maven Pom file for your project"
fi

mvn clean

echo "Running Maven Verify: mvn verify"
mvn verify

echo "Running Maven Test: mvn test"
mvn test
