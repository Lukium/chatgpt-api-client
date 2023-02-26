# chatgpt-api-client
ChatGPTClient class designed to communicate with the chatgpt-api-server. Includes a super basic CLI interface to demonstrate operability.

The Class can be added to any project that wants to communicate to the chatgpt-api-server in https://github.com/Lukium/chatgpt-api-server

Anyone is welcome to translate the Python class into other programming languages and submit a pull request, and I will bring it into the code.

## FOR EXPERIMENTAL AND LEARNING USE ONLY:
- I came up with this project while thinking of a use case where OpenAI, when providing its capabilities for an organization, say for example a University and its employees/students, rather than providing individual accounts that are managed by OpenAI, might instead provide a single account for the entire organization, such that the organization can then manage its own users via an API like the one I developed. 

- In this scenario, the individual's API key might be passed via the API to OpenAI for moderation and user counting, such that in turn, OpenAI can charge the organization based on the number of users utilizing the API via the org account. In this use case, the overall amount of resources used for user management is drastically reduced, since the organization would already have user records for each individual, which in my opinion, makes having OpenAI have a duplicate of records on its side redundant and generally a waste of resources. As a result, this setup would make the process more efficient for OpenAI in such a use case, reducing the resource usage for user authentication (one account vs potentially thousands), message storage (offloading it to the organization's server), and user billing (billing a single account instead of potentially thousands).

- For the Organization, this makes it further beneficial, as it provides it with more granular control of ChatGPT usage, including the ability to check if a user might have committed plagiarism, since it would, in case of a suspicion, be able to verify the user's message cache. Furthermore, OpenAI, having saved in resources, might be able to pass on some of those savings to the org in the way of cheaper per/user cost, making it a win for both sides.


