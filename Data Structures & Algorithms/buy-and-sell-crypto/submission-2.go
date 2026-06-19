func maxProfit(prices []int) int {
	minn := 1000000000
	maxxProfit := -1
	currProfit := 0

	for k := range prices {
		currProfit = prices[k] - minn
		if currProfit < 0 {
			currProfit = 0
		}
		maxxProfit = max(maxxProfit, currProfit)
		minn = min(minn, prices[k]) 
	}

	return maxxProfit
}
