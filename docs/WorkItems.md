# WorkItems

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | _id of the WorkItems. | [optional] 
**issue_link** | **str** | issueLink of the WorkItems. | [optional] 
**summary** | **str** | summary of the WorkItems. | 
**description** | **str** | description of the WorkItems. | [optional] 
**project_id** | **str** | projectId of the WorkItems. | 
**sprint_id** | **str** | sprintId of the WorkItems. | [optional] 
**release_id** | **str** | releaseId of the WorkItems. | [optional] 
**test_cases** | [**list[LinkedTestCaseSchema]**](LinkedTestCaseSchema.md) | testCases of the WorkItems. | [optional] 
**status** | **float** | status of the WorkItems. | 
**user_ids** | **list[str]** | userIds of the WorkItems. | 
**start** | **datetime** | start of the WorkItems. | [optional] 
**end** | **datetime** | end of the WorkItems. | [optional] 
**component_ids** | **list[str]** | componentIds of the WorkItems. | 
**attachment_ids** | **list[str]** | attachmentIds of the WorkItems. | 
**created** | [**UserDateSchema**](UserDateSchema.md) |  | [optional] 
**updated** | [**UserDateSchema**](UserDateSchema.md) |  | [optional] 
**archived** | **bool** | archived of the WorkItems. | [optional] 
**order** | **float** | order of the WorkItems. | [optional] 
**custom** | **object** | custom of the WorkItems. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


