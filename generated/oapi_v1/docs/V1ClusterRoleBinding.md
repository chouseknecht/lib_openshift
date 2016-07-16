# V1ClusterRoleBinding

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds | [optional] 
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object&#39;s metadata. | [optional] 
**user_names** | **list[str]** | UserNames holds all the usernames directly bound to the role | 
**group_names** | **list[str]** | GroupNames holds all the groups directly bound to the role | 
**subjects** | [**list[V1ObjectReference]**](V1ObjectReference.md) | Subjects hold object references to authorize with this rule | 
**role_ref** | [**V1ObjectReference**](V1ObjectReference.md) | RoleRef can only reference the current namespace and the global namespace If the ClusterRoleRef cannot be resolved, the Authorizer must return an error. Since Policy is a singleton, this is sufficient knowledge to locate a role | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


