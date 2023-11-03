import sender_request
import data

# Владимир Верхотуров, 8-я когорта - Финальный проект. Инженер по тестированию плюс.
def test_get_order_info_by_track():
    track = sender_request.create_order(data.order_body).json()['track']
    response = sender_request.get_order_info_by_track(track)
    assert response.status_code == 200