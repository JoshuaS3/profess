# Basic (ideal) documentation
```
Class Profess
	Class Request
		string Request -- e.g. GET / HTTP/2.0
		string ClientHost -- client IP address
		string Path -- path to resource
		string Method -- HTTP method used
		<string, string> Headers -- dictionary of headers
		<string, string> Cookies -- parsed Cookie header (if exists)
		<string, string> Params -- URL parameters
		string Body -- request body
	Class Response
		bool Sent
		int Code
		string Mime
		<string, string> Headers -- response headers
		string Content -- response body
	Class QueryResult
		...
	Class SiteConfig
		int Port
		bool SSLEnabled
		string SSLCertificate
		string SSLKey
		View NotFound
		View Forbidden
		View Error
	Class ModelConfig
		...
		-- this is the bulk of the project, it will require different
		-- SQL APIs for different languages to be packed with releases

	Class Controller
		string Name
		<string, string> Handler(Request req, Response res) custom handler for request and response manipulation, interop with View, returns inline substitutes
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
		QueryResult Query(string QueryName) executes Queries[QueryName] and returns new QueryResult object
	Class Site
		void Start()
		bool Stop()

		Controller AddController(Controller c) returns c
		View AddView(View v) returns v
		Model AddModel(Model m) returns m

		Controller GetController(string name)
		View GetView(string name)
		Model GetModel(string name)
```