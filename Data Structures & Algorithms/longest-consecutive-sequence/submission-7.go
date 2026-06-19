	type sizeOfSeq struct {
		Num int
		Size int
	}

func longestConsecutive(nums []int) int {
	hash_table_all := make(map[int]bool)
	for n := range(nums) {
		if _, ok := hash_table_all[nums[n]]; !ok {
			hash_table_all[nums[n]] = true
		}
	}
	//fmt.Println(hash_table_all)

	longest := 0

	hash_table_begginnings := make(map[int]int)
	for n := range(nums) {
		_, hasPrev := hash_table_all[nums[n] - 1]
		//_, hasNext := hash_table_all[nums[n] + 1]
		if !hasPrev {
			hash_table_begginnings[nums[n]] = findSizeOfSequenceForThisBegginning(nums[n], hash_table_all)
			sizee := hash_table_begginnings[nums[n]]			
			if sizee > longest {
				longest = sizee
			}
		}
	}
	//fmt.Println(hash_table_begginnings)

	return longest
}	

func findSizeOfSequenceForThisBegginning(begginning int, hash_table_all map[int]bool) int {
	size := 1
	current := begginning
	for {
		_, hasNext := hash_table_all[current+1]
		if !hasNext {
			return size
		}

		size++
		current++
	}
	return size
}