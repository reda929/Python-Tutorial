
<details open>

<summary>For better experience</summary>

**For better experience, this file is supposed to be viewed from GitHub; although conventional .md file editors would deliver an almost identical experience .**

**To avoid confusion, the code, `e.g., "# A first-level heading"` is supposed to be read from source code beside the rendered preview; omitting actual code from being displayed on preview view is intentional.**

</details>

<details>
<summary>Headers</summary>

# Headers

**To create a heading, add 1 to 6 `'#'` symbols before your heading text.**

# Examples:

# A first-level heading
## A second-level heading
### A third-level heading

</details>


<details>
<summary>Styling text</summary>

# Styling text

| Style                  | Shortcut | Output (Syntax in source code)                 |
|------------------------|----------|------------------------------------------------|
| Bold                   | Ctrl+B   | **Bald text (way 1)** or __Bald text (way 2)__ |
| Italic                 | Ctrl+I   | *Italic text (way 1)* or _Italic text (way 2)_ |
| Strikethrough          |          | ~~Strikedthrough text~~                        |
| Bold and nested italic |          | **Bald _and italic_ text (way 1)**             |
| All bold and italic    |          | **Bald *and italic* text (way 2)**             |
| Subscript              |          | Sample text<sub>subscripted text</sub>         |
| Superscript            |          | Sample text<sup>superscripted text</sup>       |

</details>

<details>
<summary>Quotes & Code Blocks</summary>

# Quotes & Code Blocks

> This is a quote 

**This is a `code text`**

```
This is distinct block code text
```

**The background color is `#0969DA`
`rgb(9, 105, 218)`
for light mode and `#000000` for dark mode.**

```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```

</details>

<details>
<summary>Comments</summary>

**Look at source Code**

`<!-- This is a comment -->`

`[//]: # (This is a comment)`
</details>

<details>
<summary>Links & Images</summary>

**Relative links are better than absolute links
Use relative link operands, such as ./ and ../.**

[Google URL text](https://www.google.com/)

[//]: # (TODO: [Contribution guidelines for this project]&#40;docs/CONTRIBUTING.md&#41;)

[//]: # (![alttext of a successful image]&#40;https://myoctocat.com/assets/images/base-octocat.svg&#41;)

[//]: # (![alttext of an usuccesful image]&#40;ahttps://myoctocat.com/assets/images/base-octocat.svg&#41;)

#Context Relative Link

| File Path                    | Syntax                |
|------------------------------|-----------------------|
| Absolute                     | `image.png`             |
| In outer file `'outer_file'` | `/outer_file/image.png` |
</details>

<details>
<summary>Lists</summary>

# Lists

## Unordered list:
**Precede one or more lines of text with `-`, `*`, or `+`:**

- Unordered list elements 1
* Unordered list elements 2
+ Unordered list elements 3

## Ordered list:
**Precede each line with a number (numerical subsequence doesn't matter).**

1. Unordered list elements 1
2. Unordered list elements 2
1354. Unordered list elements 4

## Nested List:
**Indent items below another item.**

1. First list item
    - Second nested list item
        - Third nested list item

# Task lists
**To create a task list, preface list items with a hyphen and space followed by [ ]. To mark a task as complete, use [x].**

- [x] Do thing #1 
- [x] Do thing #2 
- [ ] Do thing #3 
</details>

<details>
<summary>Paragraphs</summary>

# Paragraphs

You can create a new paragraph by leaving a blank line between lines of text.

# Footnotes

```commandline
I need footnote #1 [^1]. 
I need footnote #2 [^2].

[^1]: Here is footnote #1.
[^2]: Here is footnote #2.
```
</details>

[//]: # (TODO: look for relative links [some place][some_place_link].
 [some_place_link]: whatever link)

<details>
<summary>Creating Tables</summary>

# Creating Tables

- Use pipes `|` and hyphens `-` (at least three hyphens) to create table.

- Must include a blank line before your table for it to render correctly.

- Cells can vary in width and do not need to be perfectly aligned within columns.
# Most Simple Table
|   |
|---|

# Examples:
| Command      | Description |
|--------------|-------------|
| Col 1 Row 1  | Col 2 Row 1 |
| Col 1 Row 2  | Col 2 Row 2 |

Align text by including colons to the left, right, or on both sides of the hyphens within the header row.

| Left-aligned                                     |                  Center-aligned                   |                                    Right-aligned |
|:-------------------------------------------------|:-------------------------------------------------:|-------------------------------------------------:|
| Left-aligned text                                |                Center-aligned text                |                               Right-aligned text |
</details>

<details>
<summary>Title of Close-by-Default Details</summary>

#Close-by-Default Details
</details>

<details open>
<summary>Title of Open-by-Default Details</summary>

#Open-by-Default Details
</details>
