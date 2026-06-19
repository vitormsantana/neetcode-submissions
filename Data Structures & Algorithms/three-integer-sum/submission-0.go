func threeSum(nums []int) [][]int {

	result := [][]int{}
	hash_table_triplets := make(map[[3]int]bool)

	sort.Ints(nums)
	for k := range(len(nums)) {
		result = appendTripletIfHasOriginalTwoSum(k, nums, result, hash_table_triplets)
	}

	return result
}


func appendTripletIfHasOriginalTwoSum(indexTarget int, array []int, triplets [][]int, hash_table_triplets map[[3]int]bool) [][]int{
	i, j := 0, len(array) - 1
	for i < j {
		if i == indexTarget {
			i += 1
		}

		if j == indexTarget {
			j -= 1
		}

		if i >= j {
			break
		}

		if array[i] + array[j] < -array[indexTarget] {
			i += 1
		} else if array[i] + array[j] > -array[indexTarget] {
			j -= 1
		} else {
			values := []int{
				array[i],
				array[j],
				array[indexTarget],
			}
			sort.Ints(values)
			key := [3]int{
				values[0],
				values[1],
				values[2],
			}

			if _, ok := hash_table_triplets[key]; !ok {
				hash_table_triplets[key] = true
				triplets = append(triplets, values)
			}
			i+= 1
		}
	}

	return triplets
}
