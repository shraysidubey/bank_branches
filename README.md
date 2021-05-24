# bank_branches
You need to create a REST service that can fetch bank details, using the data given in the API’s query parameters. 
* Autocomplete API to return possible matches based on the branch name ordered by IFSC code (ascending order) with limit and offset
  * Endpoint: /api/branches/autocomplete?q=<> 
  * Example: /api/branches/autocomplete?q=RTGS&limit=3&offset=0 
* Search API to return possible matches across all columns and all rows, ordered by IFSC code (ascending order) with limit and offset. 
  * Endpoint: /api/branches?q=<> 
  * Example: /api/branches?q=Bangalore&limit=4&offset=0 
  * Sample response: 3
