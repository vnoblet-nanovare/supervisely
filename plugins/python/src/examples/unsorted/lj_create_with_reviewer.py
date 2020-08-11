import supervisely_lib as sly

print("start")

api = sly.Api.from_env()

lj_info = api.labeling_job.create(name="lj_with_reviewer", dataset_id=808, user_ids=[1], reviewer_id=6)
print(lj_info)

print("end")