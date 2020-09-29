# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.cloud import automl

project_id = "cadillacvehiclerecognition-poc"
dataset_id = "TEN183111566978187264"
display_name = "nlp-model-1"

def main():
    """Create a model."""
    # [START automl_language_entity_extraction_create_model]

    client = automl.AutoMlClient()

    # A resource that represents Google Cloud Platform location.
    project_location = "projects/{project_id}/locations/us-central1"
    # Leave model unset to use the default base model provided by Google
    metadata = automl.TextExtractionModelMetadata()
    model = automl.Model(
        display_name=display_name,
        dataset_id=dataset_id,
        text_extraction_model_metadata=metadata,
    )

    # Create a model with the model metadata in the region.
    response = client.create_model(parent=project_location, model=model)

    print("Training operation name: {}".format(response.operation.name))
    print("Training started...")
    # [END automl_language_entity_extraction_create_model]




if __name__ == '__main__':
    main()
