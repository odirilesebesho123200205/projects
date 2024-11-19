cd $1

echo "Building Flutter in dir $1"

#compare output file
file1="pubspec.yaml"

if [ ! -f "$file1" ]; then
    echo "Error: File $file1 does not exist."
    exit 2  # Exit with code 2 for file not found
fi

echo "Ensuring Web platform installed"
flutter create --platforms=web .

echo "Doing Flutter pub get"
flutter pub get

echo "Building for web"
flutter build web

#TODO check if there is test dir, and run if it is there