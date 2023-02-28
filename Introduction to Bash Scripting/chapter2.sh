# 1
# Create the required variable
yourname="Sam"

# Print out the assigned name 
echo "Hi there $yourname, welcome to the website!"

# 2
# Get first ARGV into variable
temp_f=$1

# Subtract 32
temp_f2=$(echo "scale=2; $temp_f - 32" | bc)

# Multiply by 5/9
temp_c=$(echo "scale=2; $temp_f2 * 5 / 9" | bc)

# Print the celsius temp
echo $temp_c

# 3

temp_a=$(cat temps/region_A)
temp_b=$(cat temps/region_B)
temp_c=$(cat temps/region_C)

echo $temp_a
echo $temp_b
echo $temp_c

# 4
# Create a normal array with the mentioned elements using the declare method
declare -a capital_cities

# Add (append) the elements
capital_cities+=("Sydney")
capital_cities+=("Albany")
capital_cities+=("Paris")

# The array has been created for you
capital_cities=("Sydney" "Albany" "Paris")

# Print out the entire array
echo ${capital_cities[@]}

# Print out the array length
echo ${#capital_cities[@]}

# 5
# Create empty associative array
declare -A model_metrics

# Add the key-value pairs
model_metrics[model_accuracy]=98
model_metrics[model_name]="knn"
model_metrics[model_f1]=0.82

# Declare associative array with key-value pairs on one line
declare -A model_metrics=([model_accuracy]=98 [model_name]="knn" [model_f1]=0.82)

# Print out the entire array
echo ${model_metrics[@]}

# Print out just the keys
echo ${!model_metrics[@]}

# 6
# Create variables from the temperature data files
temp_b="$(cat temps/region_B)"
temp_c="$(cat temps/region_C)"

# Create an array with these variables as elements
region_temps=($temp_b $temp_c)

# Call an external program to get average temperature
average_temp=$(echo "scale=2; (${region_temps[0]} + ${region_temps[1]}) / 2" | bc)

# Append average temp to the array
region_temps+=($average_temp)

# Print out the whole array
echo ${region_temps[@]}