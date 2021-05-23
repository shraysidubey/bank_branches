# bank_branches
Autocomplete API to return possible matches based on the branch name ordered by IFSC code (ascending order) with limit and offset.
a. Endpoint: /api/branches/autocomplete?q=<>
Example: /api/branches/autocomplete?q=RTGS&limit=3&offset=0
2. Search API to return possible matches across all columns and all rows, ordered by IFSC code (ascending order) with limit and offset. 
a. Endpoint: /api/branches?q=<> 
