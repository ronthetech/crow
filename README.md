<div align="center">
<pre>

# crow
<p  align="center">
  <img width="150" src="https://github.com/ronthetech/image-repo/blob/42d66d8a61c3933ca2f5326f1279978ce3868586/crow-cli.jpg" alt="crow cli">
</p>
Useful cli for data entry, data cleansing, etc.
</pre>
</div>

## Usage

Open a terminal from the directory where the folder is saved, or open a terminal and navigate to the directory where the folder is saved.
Select the mode to determine the format that will be output. Type in a string as input, typically a color code followed by some color combination.

### Uppercase

```sh
C:\> python main.py
1
Some Color - Another Color- Third Color
```

For upper case, hit enter and the output will look like:

```sh
SOME COLOR/ANOTHER COLOR/THIRD COLOR
```

### Title Case

```sh
C:\> python main.py
2
SOME COLOR/ANOTHER COLOR
```
For title case, hit enter and the output will look like:

```sh
Some Color/Another Color
```

### Lowercase

```sh
C:\> python main.py
3
SOME COLOR/ANOTHER COLOR
```
For lower case, hit enter and the output will look like:

```sh
some color/another Color
```

## Meta

Ron Jean-Francois - jeanfrancoisron@gmail.com

## Contributing

1. Fork it (<https://github.com/ronthetech/crow/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
