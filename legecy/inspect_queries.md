## markdown to inspect queires


```python 
from django.db import connections, reset_queries
```

**list of all the stored queries**

```python

connection.queries

```

**reset the queries list**
```python

reset_queries()

```

