from utils.api import Google_maps_api
from utils.cheking import Cheking
import allure

"""Создание, изменение и удаление новой локации"""
@allure.epic("Test create new place")
class Test_create_place():

    @allure.description("Test create, update and delete new place")
    def test_create_new_place(self):

        print("Метод POST")
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")

        Cheking.check_status_code(result_post, 200)
        print(result_post.status_code)
        Cheking.check_json_fields(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Cheking.check_json_value(result_post, 'status', 'OK')

        print("Метод GET POST")
        result_get = Google_maps_api.get_new_place(place_id)

        Cheking.check_status_code(result_get, 200)
        print(result_get.status_code)
        Cheking.check_json_fields(result_get,['location', 'accuracy',
                                              'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Cheking.check_json_value(result_get, "address", "29, side layout, cohen 09")

        print("Метод PUT")
        result_put = Google_maps_api.put_new_place(place_id)

        Cheking.check_status_code(result_put, 200)
        print(result_put.status_code)
        Cheking.check_json_fields(result_put, ['msg'])
        Cheking.check_json_value(result_put, "msg", "Address successfully updated")


        print("Метод GET PUT")
        result_get = Google_maps_api.get_new_place(place_id)

        Cheking.check_status_code(result_get, 200)
        print(result_get.status_code)
        Cheking.check_json_fields(result_get,['location', 'accuracy', 'name',
                                              'phone_number', 'address', 'types', 'website', 'language'])
        Cheking.check_json_value(result_get,"address", "100 Lenina street, RU")



        print("Метод DELETE")
        result_delete = Google_maps_api.delete_new_place(place_id)

        Cheking.check_status_code(result_delete, 200)
        print(result_delete.status_code)
        Cheking.check_json_fields(result_delete, ['status'])
        Cheking.check_json_value(result_delete,"status", "OK")


        print("Метод GET DELETE")
        result_get = Google_maps_api.get_new_place(place_id)

        Cheking.check_status_code(result_get, 404)
        print(result_get.status_code)
        Cheking.check_json_fields(result_get,['msg'])
        Cheking.check_json_value(result_get,"msg",
                                 "Get operation failed, looks like place_id  "
                                 "doesn't exists")


        print("Тестирование создания, изменения и удаления новой локации прошло успешно!")






