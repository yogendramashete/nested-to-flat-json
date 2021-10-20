Flattening nested JSON to flat json excluding list types

INPUT:
{
  'user': {
    'Rachel': {
      'UserID': 1717171717,
      'Email': 'rachel1999@gmail.com',
      'friends': [
        'John',
        'Jeremy',
        'Emily'
      ]
    }
  }
}

OUTPUT

{
  'user.Rachel.UserID': 1717171717,
  'user.Rachel.Email': 'rachel1999@gmail.com',
  'user.Rachel.friends': [
    'John',
    'Jeremy',
    'Emily'
  ]
}

run command :
python flatten-json.py