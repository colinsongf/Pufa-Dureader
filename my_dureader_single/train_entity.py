nohup python -u run.py --model_dir ../data/models_search_pretrain/entity --vocab_dir ../data/vocab_search_pretrain/entity --result_dir ../data/results_demo/entity --test_files ../data/entity/data_test_preprocessed.json --dev_files ../data/entity/data_dev_preprocessed.json --train_files ../data/entity/data_train_preprocessed.json > entity.log 2>&1 &