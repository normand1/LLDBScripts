# LLDBScripts
Helpful Debugging Scripts and How To Use Them

## What's this for?
When working with an api that returns JSON, the standard debugging response to the xcode console will look something like this: 

```
(lldb) po json
▿ 4 elements
  ▿ 0 : 2 elements
    - key : body
    - value : quia et suscipit
suscipit recusandae consequuntur expedita et cum
reprehenderit molestiae ut ut quas totam
nostrum rerum est autem sunt rem eveniet architecto
  ▿ 1 : 2 elements
    - key : id
    - value : 1
  ▿ 2 : 2 elements
    - key : title
    - value : sunt aut facere repellat provident occaecati excepturi optio reprehenderit
  ▿ 3 : 2 elements
    - key : userId
    - value : 1
```

This repository provides an easy new LLDB function that will print dictionaries as a standard json response that you can easily copy and use elsewhere.

Once the new LLDB function is available you'll be able to invoke `jprint` like so:

```
(lldb) jprint json
{
  "body" : "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
  "id" : 1,
  "title" : "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "userId" : 1
}

```

## Installation


1. Open a new terminal window
2. Clone this repo to your desired directory
3. Run the following command:
`echo "command script import {PATH TO CLONED REPO}/jprint.py" >> ~/.lldbinit`
4. Close the existing terminal and open a new one
5. run the following command:
```
lldb
(lldb) help
```
6. At the bottom of the message printed to the console you should see something like the following:
```
Current user-defined commands:
  jprint -- For more information run 'help jprint'
```

Now you should be able to access jprint from the Xcode lldb debugger the same way you use `po` and other common lldb debugging functions
