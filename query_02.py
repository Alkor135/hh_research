import requests
from urllib.parse import urlencode
from typing import Dict, Optional


__API_BASE_URL = "https://api.hh.ru/vacancies/"


def __encode_query_for_url(query: Optional[Dict]) -> str:
    if 'professional_roles' in query:
        query_copy = query.copy()

        roles = '&'.join([f'professional_role={r}' for r in query_copy.pop('professional_roles')])

        return roles + (f'&{urlencode(query_copy)}' if len(query_copy) > 0 else '')

    return urlencode(query)


def collect_vacancies(query: Optional[Dict], refresh: bool = False, num_workers: int = 1) -> Dict:
    if num_workers is None or num_workers < 1:
        num_workers = 1

    url_params = __encode_query_for_url(query)

    # # Get cached data if exists...
    # cache_name: str = url_params
    # cache_hash = hashlib.md5(cache_name.encode()).hexdigest()
    # cache_file = os.path.join(CACHE_DIR, cache_hash)
    # try:
    #     if not refresh:
    #         print(f"[INFO]: Get results from cache! Enable refresh option to update results.")
    #         return pickle.load(open(cache_file, "rb"))
    # except (FileNotFoundError, pickle.UnpicklingError):
    #     pass

    # Проверка количества страниц
    target_url = __API_BASE_URL + "?" + url_params
    num_pages = requests.get(target_url).json()["pages"]
    # print(num_pages)

    # Список IDs вакансий
    ids = []
    for idx in range(num_pages + 1):
        response = requests.get(target_url, {"page": idx})
        data = response.json()
        if "items" not in data:
            break
        ids.extend(x["id"] for x in data["items"])
    print(ids)

    for vacancy_id in ids:
        # vacancy_id = 98919945
        url = f"{__API_BASE_URL}{vacancy_id}"
        vacancy = requests.get(url).json()
        print(vacancy)

    # # Collect vacancies...
    # jobs_list = []
    # with ThreadPoolExecutor(max_workers=num_workers) as executor:
    #     for vacancy in tqdm(
    #             executor.map(self.get_vacancy, ids),
    #             desc="Get data via HH API",
    #             ncols=100,
    #             total=len(ids),
    #     ):
    #         jobs_list.append(vacancy)
    #
    # unzipped_list = list(zip(*jobs_list))
    #
    # result = {}
    # for idx, key in enumerate(self.__DICT_KEYS):
    #     result[key] = unzipped_list[idx]
    #
    # pickle.dump(result, open(cache_file, "wb"))
    # return result


if __name__ == "__main__":
    vacancies = collect_vacancies(
        query={"text": "Python", "area": 1, "per_page": 100},
        # refresh=True
    )
    # print(vacancies["Employer"])