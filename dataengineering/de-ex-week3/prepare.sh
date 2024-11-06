cd $1

echo "Removing old output files in dir $1"

file1="local_sqlite_database.db"

if [ -f "$file1" ]; then
    echo "File $file1 exists. Deleting..."
    rm "$file1"
    if [ $? -eq 0 ]; then
        echo "File $file1 has been successfully deleted."
    else
        echo "Failed to delete $file1."
    fi
else
    echo "File $file1 does not exist."
fi

