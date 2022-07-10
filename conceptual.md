### Conceptual Exercise

Answer the following questions below:

1. What are important differences between Python and JavaScript?  
  -  Python is more of a server-side language or back-end development. Python is mostly used for scientific applications. Code block with indentation(4 indent). variable_name = value . Comment out with #. == equality (strict about types)
  - JavaScript is a versatile language that allows both back-end and front-end development, mostly used by user-facing applications.Code block with {}. let (const or var) variableName = value. Comment out with #. === equality (strict about types)

2. Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  - `dict.get('c', 'Not There')`
3. What is a unit test?  
  -   `from collection import defaultdict`
  - `dict = defaultdict(list)`
  - `dict[’a’] =1`
  - `dict[’b’] =2`
  - `dict[’c’]`
  - `dict = {"a": 1, "b": 2,”c”:[]}`
  - or  `dict[’c’].append(3)`
  - `dict = {"a": 1, "b": 2,”c”:[3]}`

4. What is an integration test?
  - Intergration test is used to test out how multiple things are working together. Answering the question if the route is directing us to the right path and returning the right status code. Are multiple  functions working well together. 

5. What is the role of web application framework, like Flask?
  -  provide a standard way to build and deploy web applications. They are like a library. Web application framework handle web request, form, cookie ...

6. You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  - use URL query param when it is coming from a form

7. How do you collect data from a URL placeholder parameter using Flask?
  - `@app.route('/page/<id>')`
  - `def start_page(id):`
8. How do you collect data from the query string using Flask?
  -  `id = request.args['id']`

9. How do you collect data from the body of the request using Flask?
  - `id = request.args.get('id')`

10. What is a cookie and what kinds of things are they commonly used for?
  - They are ways to store bits of information on the client browser. They save info like what website you visted, what you searched, what you bought  

11. What is the session object in Flask?
  - they contain info for the current browser, users can't modify it 

12. What does Flask's `jsonify()` do?
  - returns data to JavaScript Object so that JS can you the info as it needs to 
