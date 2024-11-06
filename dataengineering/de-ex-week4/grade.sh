cp ./solution.dump $1/solution.dump
cd $1

echo "Comparing output in dir $1"

file1="local_sqlite_database.db"
file2="solution.dump"

# Check if both files exist
if [ ! -f "$file1" ]; then
    echo "Error: File $file1 does not exist."
    exit 2  # Exit with code 2 for file not found
fi

if [ ! -f "$file2" ]; then
    echo "Error: File $file2 does not exist."
    exit 2  # Exit with code 2 for file not found
fi

# Pattern to match table names (e.g., sales_YYYYMMDD)
table_pattern="sales_aggregated_[0-9]\{8\}"

# Expected number of entries in the matching table(s)
expected_count=9

# Query to list tables matching the pattern
matching_tables=$(sqlite3 "$db_file" ".tables" | grep -E "$table_pattern")

# Check if any matching table is found
if [ -z "$matching_tables" ]; then
    echo "No tables found matching pattern '$table_pattern'."
    exit 1
fi

# Loop through each matching table to check the row count
for table in $matching_tables; do
    # Get the actual row count for the table
    row_count=$(sqlite3 "$db_file" "SELECT COUNT(*) FROM $table;")

    # Check if the row count meets the expected count
    if [ "$row_count" -eq "$expected_count" ]; then
        echo "Table '$table' has the expected number of entries ($expected_count)."
    else
        echo "Table '$table' does not have the expected number of entries. Found $row_count entries, expected $expected_count."
        exit 1
    fi
done

# Clean up temporary dump files
rm "solution.dump"
# clean up local db file
rm "$file1"
