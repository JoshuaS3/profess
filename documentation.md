# Basic (ideal) documentation
```
Class Profess

	-- Language independent implementation but will be the same API --
	Class Request
		...
	Class Response
		...
	Class QueryResult
		...
	Class SiteConfig
		...
	Class ModelConfig
		...
		-- this is the bulk of the project, it will require different
		-- SQL APIs for different languages to be packed with releases
	------------------------------------------------------------------

	Function Init(SiteConfig config) creates and returns new Site object


	Class Controller
		string Name
		Function Handler(Request req, Response res) custom handler for request and response manipulation, interop with View, returns int StatusCode
	Class View
		string WebAddress -- acts as the identifier (Name) because you can't have more than 1 view at the same web address
		string AcceptedMethods[]
		string MimeType
		optional string ControllerID
		optional string TemplateString -- Either TemplateString or TemplateFile are required. If both then TemplateString is preferred
		optional File TemplateFile
	Class Model
		string Name
		ModelConfig Config -- info like DB type, host, username, password, etc.
		<string, string> Queries{};
		Function Query(string QueryName) executes Queries[QueryName] and returns new QueryResult object
	Class Site
		Function Start() returns startup status
		Function Stop() returns exit status

		Function AddController(Controller c) returns c
		Function AddView(View v) returns v
		Function AddModel(Model m) returns m

		Function GetController(string name) returns Controllers[name]
		Function GetView(string name) returns Views[name]
		Function GetModel(string name) returns Models[name]

		Controller Controllers[]
		View Views[]
		Model Models[]



SiteConfig will accept files that implement an nginx-like .conf format
```