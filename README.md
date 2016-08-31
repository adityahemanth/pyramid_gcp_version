# Pyramid

Pyramid is a prototype application showing applications of [Latent Semantic Analysis][9]
on systematically classified data. Users train the classifier by uplaoding MARC records
and retrieve most relevant documents presented as a hierarchy of similar documents.
Users can also traverse the Library of Congress Classification
Outline ([LCCO][101]) to view the term frequenies of each of the categories in the hierarchy.
Data is stored in App Engine (NoSQL) High Replication Datastore (HRD) and retrieved using a strongly consistent
(ancestor) query.

## Supported Calls:
###### Home Page
```
**'/'**
```
Allows users to login and perform training and testing independently

###### Static Files:
```
**'/statics'**
```
**'/statics/lcco.json'** responds with the entire LCC hierarchy

###### RESTful Calls:
```
'/lcco?request=**request**'
```
Responds with the category containing the request node along with all its children

## Key Concepts
- [Library of Congress Classification][8]
- [Latent Semantic Analysis][9]

## Language
- [Python][2]

## APIs
- [NDB Datastore API][3]
- [Users API][4]

## Dependencies
- [gensim][1]
- [webapp2][5]
- [jinja2][6]
- [Twitter Bootstrap][7]


[1]: https://radimrehurek.com/gensim/
[2]: https://python.org
[3]: https://developers.google.com/appengine/docs/python/ndb/
[4]: https://developers.google.com/appengine/docs/python/users/
[5]: http://webapp-improved.appspot.com/
[6]: http://jinja.pocoo.org/docs/
[7]: http://twitter.github.com/bootstrap/
[8]: https://www.loc.gov/catdir/cpso/lcc.html
[9]: https://en.wikipedia.org/wiki/Latent_semantic_analysis

[101]: https://www.loc.gov/catdir/cpso/lcco/

