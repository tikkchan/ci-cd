#!/usr/bin/env python3
import logging

import connexion

from swagger_server import encoder

from prometheus_flask_exporter import PrometheusMetrics


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    metrics = PrometheusMetrics(app.app)
    app.add_api('swagger.yaml', arguments={'title': 'Онлайн-магазин комиксов API'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
