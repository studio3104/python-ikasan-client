# Python Ikasan Client Library

post message to HipChat http gateway `ikasan`.

see: https://github.com/studio3104/ikasan

## Installation

Add this line to your application's requirements.txt:

```python
 -e git://github.com/studio3104/python-ikasan-client#egg=ikasanclient
```

And then execute:

    $ pip install -r requirements.txt

Or install it yourself as:

    $ pip install -e git://github.com/studio3104/python-ikasan-client#egg=ikasanclient

## Usage

#### Expamples

```python
from ikasanclient import IkasanClient

# ikasan server: http://localhost:4979
ikasan = IkasanClient('localhost')

# ikasan server: http://localhost
ikasan = IkasanClient('localhost', 80)
```

###### send NOTICE

```python
ikasan.notice('#channel', 'message', **{ 'color': 'random', 'message_format': 'text' })
```

###### send PRIVMSG

```python
ikasan.privmsg('#chennel', 'message', **{ 'color': 'random', 'message_format': 'text' })
```

## Contributing

1. Fork it ( http://github.com/studio3104/python-ikasan-client/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## TODO

- support https
- write more tests
