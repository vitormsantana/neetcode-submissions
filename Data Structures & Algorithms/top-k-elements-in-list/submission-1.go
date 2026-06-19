type Pair struct {
    Num int
    Freq int
}

func topKFrequent(nums []int, k int) []int {
    nums_freq := make(map[int]int)
    for n := range(len(nums)) {
        if _, ok := nums_freq[nums[n]]; !ok {
            nums_freq[nums[n]] = 1
        } else {
            nums_freq[nums[n]] += 1

        }
    }
    fmt.Println(nums_freq)

    pairs := []Pair{}   
    for num, freq := range nums_freq {
        pairs = append(pairs, Pair{
            Num: num,
            Freq: freq,
        })
    }

    filtered_pairs := []Pair{}   
    filtered_pairs = sort_tuples(pairs)[:k]
    
    //fmt.Println("Pairs")
    //fmt.Println(pairs)
    //fmt.Println("Ordered Pairs")
    //fmt.Println(sort_tuples(pairs))
    //fmt.Println("Filtered Pairs")
    //fmt.Println(filtered_pairs)

    result := []int{}
    for _, pair := range(filtered_pairs) {
        result = append(result, pair.Num)
    }
    return result
}

func sort_tuples(pairs_arr []Pair) []Pair {
    sort.Slice(pairs_arr, func(i, j int) bool {
        return pairs_arr[i].Freq > pairs_arr[j].Freq
    })
    return pairs_arr
}