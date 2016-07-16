# V1LocalSubjectAccessReview

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds | [optional] 
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources | [optional] 
**namespace** | **str** | Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces | 
**verb** | **str** | Verb is one of: get, list, watch, create, update, delete | 
**resource_api_group** | **str** | Group is the API group of the resource Serialized as resourceAPIGroup to avoid confusion with the &#39;groups&#39; field when inlined | 
**resource_api_version** | **str** | Version is the API version of the resource Serialized as resourceAPIVersion to avoid confusion with TypeMeta.apiVersion and ObjectMeta.resourceVersion when inlined | 
**resource** | **str** | Resource is one of the existing resource types | 
**resource_name** | **str** | ResourceName is the name of the resource being requested for a \&quot;get\&quot; or deleted for a \&quot;delete\&quot; | 
**content** | **str** | Content is the actual content of the request for create and update | [optional] 
**user** | **str** | User is optional.  If both User and Groups are empty, the current authenticated user is used. | 
**groups** | **list[str]** | Groups is optional.  Groups is the list of groups to which the User belongs. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


