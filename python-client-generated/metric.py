from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

trace.set_tracer_provider(TracerProvider())
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)
tracer = trace.get_tracer(__name__)
# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.host = 'http://localhost:8080/api/v1/'
api_client = swagger_client.ApiClient(configuration=configuration)
#api_instance = swagger_client.ComicApi(api_client=api_client)
api_instance = swagger_client.ComicApi(swagger_client.ApiClient(configuration))
comic_id = 56

try:
    with tracer.start_as_current_span("Get list of comics"):
        api_response = api_instance.comics_get()
        pprint(api_response)

    with tracer.start_as_current_span("Purchase a comic"):
        api_response = api_instance.comics_post(comic_id)
        pprint(api_response)

except ApiException as e:
    print("Exception when calling ComicApi: %s\n" % e)



# import requests
#
# response = requests.get('http://localhost:9090/metrics')
# data = response.text
#
# # Вывод метрик
# print(data)
#
# # import requests
# #
# # GRAFANA_API_URL = "http://grafana/api/datasources/proxy/1/api/v1/query"
# #
# #
# # def get_movies_count():
# #     query = "count(movies)"
# #     response = send_metric_query(query)
# #     return response
# #
# # def get_movie_duration_stats():
# #     query = "histogram_quantile(0.95, sum(rate(movie_duration_seconds_bucket[5m])) by (le))"
# #     response = send_metric_query(query)
# #     return response
# #
# # def get_movie_rating_histogram():
# #     query = "histogram(movie_rating, 10)"
# #     response = send_metric_query(query)
# #     return response
# #
# # def add_movie(movie):
# #     # код для добавления фильма в API
# #     pass
# #
# # def update_movie(movie_id, updated_movie):
# #     # код для обновления информации о фильме
# #     pass
# #
# # def delete_movie(movie_id):
# #     # код для удаления фильма из API
# #     pass
# #
# # def send_metric_query(query):
# #     url = f"{GRAFANA_API_URL}/query"
# #     params = {
# #         "query": query
# #     }
# #     response = requests.get(url, params=params)
# #     response.raise_for_status()
# #     return response.json()
# #
# # if __name__ == "__main__":
# #     # Получить количество фильмов
# #     movies_count = get_movies_count()
# #     print("Количество фильмов:", movies_count)
# #
# #     # Получить статистику продолжительности фильмов
# #     duration_stats = get_movie_duration_stats()
# #     print("Статистика продолжительности фильмов:", duration_stats)
# #
# #     # Получить гистограмму рейтингов фильмов
# #     rating_histogram = get_movie_rating_histogram()
# #     print("Гистограмма рейтингов фильмов:", rating_histogram)
# #
# #     # Добавить новый фильм
# #     new_movie = {
# #         "id": "4",
# #         "title": "Новый фильм",
# #         "description": "Описание нового фильма",
# #         "duration": 120,
# #         "rating": 8.5
# #     }
# #     add_movie(new_movie)
# #
# #     # Обновить информацию о фильме
# #     movie_id = 1
# #     updated_movie = {
# #         "title": "Новое название",
# #         "description": "Новое описание",
# #         "duration": 130,
# #         "rating": 9.0
# #     }
# #     update_movie(movie_id, updated_movie)
# #
# #     # Удалить фильм
# #     delete_movie(movie_id)
