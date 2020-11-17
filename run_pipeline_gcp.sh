python -m pipeline_demo \
	--runner DataflowRunner \
	--project energy-insights-prod \
	--temp_location gs://efficiency_models/tmp/ \
	--max_num_workers 4 \
	--job_name 'beam-demo-pipeline' \
    --region europe-west1 \
    --no_use_public_ips
