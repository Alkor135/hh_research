import requests

__API_BASE_URL = "https://api.hh.ru/vacancies/"
# __DICT_KEYS = (
#     "Ids",
#     "Employer",
#     "Name",
#     "Salary",
#     "From",
#     "To",
#     "Experience",
#     "Schedule",
#     "Keys",
#     "Description",
# )
#
# query={"text": "Python", "area": 1, "per_page": 100},
# # Check number of pages...
# target_url = __API_BASE_URL + "?" + url_params
# num_pages = requests.get(target_url).json()["pages"]
#
# # Collect vacancy IDs...
# ids = []
# for idx in range(num_pages + 1):
#     response = requests.get(target_url, {"page": idx})
#     data = response.json()
#     if "items" not in data:
#         break
#     ids.extend(x["id"] for x in data["items"])

vacancy_id = 98919945
url = f"{__API_BASE_URL}{vacancy_id}"
vacancy = requests.get(url).json()
print(vacancy)
