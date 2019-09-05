#!/bin/sh
crf_learn -p8 -f 3 -c 4.0 template_bio_pos_20 train_bio_pos_1_0.90_0.txt model_bio_pos_1_0.90_0
crf_test -m model_bio_pos_1_0.90_0 test_bio_pos_1_0.10_0.txt >> result_bio_pos_1_0.90_0.txt
perl conlleval.pl -d "\t" < result_bio_pos_1_0.90_0.txt >> analyze_result_bio_pos_1_0.90_0.txt
