class LLM_Solution:
    def hIndex(self, citations: list[int]) -> int:
        """
        H-Index

        Given an array of integers citations where citations[i] is the number of citations
        a researcher received for their ith paper and citations is sorted in ascending order,
        return the researcher's h-index.
        """
        left, right = 0, len(citations) - 1
        while left <= right:
            mid = (left + right) // 2
            if citations[mid] >= len(citations) - mid:
                right = mid - 1
            else:
                left = mid + 1
        return len(citations) - left