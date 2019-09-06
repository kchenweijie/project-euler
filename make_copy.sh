#!/bin/bash

PROB_NUM=$1

if [[ ! -d "prob$PROB_NUM" ]]; then
    cp -r template prob$PROB_NUM
fi
