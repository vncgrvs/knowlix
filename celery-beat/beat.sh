#!/bin/bash

celery -A tasks worker -E --loglevel=info -B -n beatworker@%h

