---
title: "How Sourcery Makes AI 10x More Useful in Large iOS Codebases"
subtitle: "Stop letting AI write unusable code – give it the context it craves."
date: 2025-01-21T03:46:18+01:00
lastmod: 2025-01-21T03:46:18+01:00
draft: false
authors: ["Igor"]
description: ""

tags: []
categories: []
series: []

hiddenFromHomePage: false
hiddenFromSearch: false

featuredImage: "header.webp"
featuredImagePreview: "header_preview.png"

math:
  enable: false
toc:
  enable: false
  auto: true
code:
  maxShownLines: 100
  lineNos: false
  wrap: false
  header: true
lightgallery: false
license: ""
---

You've seen it. You've *suffered* through it. You fed your AI coding assistant a seemingly simple task, and it spat out a steaming pile of Swift garbage.

<!--more-->

> Why? Because context is king, and most AI tools are flying blind in large iOS codebases.

There are many reasons why AI assisted coding for iOS sucks, and today I am going to focus on one of them.

AI output is as good as its input and it can't produce desired code if not provided with enough context. This matters especially on large code bases where you can't just simply copy all the source files to AI context.

Different tools use different techniques. For example aider uses "repo map" which is built using tree sitter. Unfortunately, aider does not have swift support for repo map.

Another tool is the one everybody knows - cursor. It uses RAG for building context, trying to include the most relevant bits of code to user's request.

I had situations where AI would start writing code for a component that *already existed* – it just didn't know.

File trees alone don't cut it. Projects with complex business logic? Forget it. AI won't magically know how to use your internal components.

Smaller projects? You *could* write descriptions, but they're outdated instantly.



## Sourcery: Your Secret Weapon for AI-Powered Code

{{< admonition info >}}
[Sourcery](https://github.com/krzysztofzablocki/Sourcery) is a metaprogramming tool that gives you full access to your Swift project's type information at compile time.
{{< /admonition >}}

Back in the days before swift macro and automatically synthesized equatable and hashable conformances in swift, we had to write a lot of boilerplate.

That is when I learned about beautiful tool called [Sourcery](https://github.com/krzysztofzablocki/Sourcery). This is a tool for meta programming created by Krzysztof Zabłocki.

It allows you to write code that generates *other* code. Think of it like a template engine that has *full access* to your Swift project's type information at compile time.

Simply put - this is a template engine that, at runtime, knows about *all* types in your source files. You could, for example, generate an enum containing cases for *every* type in your codebase.

```swift {open=true, lineNos=false, wrap=true, title="Bad AI Example"}
// You ask: "Create a view for displaying a user profile."

// AI generates:
struct UserProfileView: View {
  // ...completely ignores your existing User and ProfileView components...
}
```

```swift {open=true, lineNos=false, wrap=true, title="Good AI Example with Sourcery Context"}
//Sourcery generates index file which has all the types

// You ask: "Create a view for displaying a user profile."

// AI generates:
struct UserProfileView: View {
    var user: User //AI knows we already have User type

    var body: some View {
        // AI uses existing components because it *knows* about them!
        ExistingProfileView(user: user)
    }
}
```



### Getting Started with Sourcery: Installation and Basic Usage

Sourcery is a command-line tool. You have several options:

1. **Homebrew (Recommended):**  `brew install sourcery`
2. **CocoaPods:** Add `pod 'Sourcery', :subspecs => ['CLI-Only']` to your `Podfile`
3. **Binary Download:** Get prebuilt binary from the [releases page](https://github.com/krzysztofzablocki/Sourcery/releases/latest)

{{< admonition tip "Quick Setup" true >}}
1. Install via Homebrew: `brew install sourcery`
2. Create your template
3. Run: `sourcery --sources Sources --templates Template.stencil --output .project-context`
{{< /admonition >}}


## How to Generate a Project Index with Sourcery (Step-by-Step)

Create a template in `AllTypes.stencil` with the following content:

```swift {open=true, lineNos=false, wrap=true, title="AllTypes.stencil"}
// Found {{ types.all.count }} Types

enum AllTypes {
{% for type in types.all %}
case {{ type.name | lowercase }}
{% endfor %}
}
```

Then run Sourcery with your source path and template path:

```bash {open=true, lineNos=false, wrap=true, title="Command Line Usage"}
sourcery --sources Sources --templates AllTypes.stencil --output .project-context
```

That can also be configured in `.sourcery.yml`:

```yaml {open=true, lineNos=false, wrap=true, title="sourcery.yml"}
sources:
- ./Sources
templates:
- ./AllTypes.stencil
output:
- .project-context
```

Then you just run `sourcery` and that is it.

It will generate `.project-context` file in the root directory.

```swift {open=true, lineNos=false, wrap=true, title="Generated Output"}
// Found 2 Types

enum AllTypes {
case contentView
case appDelegate
}
```

For complex templates, or if you're new to Stencil, consider the `.swifttemplate` format, which uses Swift itself.

Here's a quick look at a `Type` instance's properties:

*   imports
*   accessLevel
*   name
*   variables
*   methods

Full list can be found [Type Class Reference](https://krzysztofzablocki.github.io/Sourcery/Classes/Type.html)

```swift {open=true, lineNos=false, wrap=true, title="Type Properties Example"}
{% for variable in type.variables %}
    {% if variable.defaultValue %}
        print("Property: \(variable.name) has a default value")
    {% else %}
        print("Property: \(variable.name) doesn't have a default value")
    {% endif %}
{% endfor %}
```

To make documentation comments available to sourcery you need to run it with special flag:

```bash {open=true, lineNos=false, wrap=true, title="Documentation Flag"}
sourcery --parseDocumentation
```

Also, **don't forget** to run Sourcery in watch mode – it'll automatically regenerate on source file changes:

```bash {open=true, lineNos=false, wrap=true, title="Watch Mode"}
sourcery --watch
```

To make it more tailored to our needs we can use annotations. for example we can mark specific type to be ignored in our template. First we need to add annotation to that type:

```swift {open=true, lineNos=false, wrap=true, title="Annotation Example"}
// sourcery: skipCodeIndex
class SkippedClass {
// This class will be skipped by Sourcery
}
```

Then we need to filter this annotation in template:

```swift {open=true, lineNos=false, wrap=true, title="Template Filter"}
enum AllTypes {
{% for type in types.all %}
{% if not type.annotations.skipCodeIndex %}
case {{ type.name | lowercase }}
{% endif %}
{% endfor %}
}
```

We can even add some extra instructions right in code:

```swift {open=true, lineNos=false, wrap=true, title="Extra Instructions"}
class SpecialClass {
var foo: Foo
// sourcery: extraInfo = "your text"
var bar: Bar
}
```

And then we can access it in template:
```swift {open=true, lineNos=false, wrap=true, title="Accessing Annotations"}
{% if variable.annotations.extraInfo %}// {{ variable.annotations.extraInfo }}{% endif %}
```

Here you can find materials for the workshop for Sourcery [Pages · krzysztofzablocki/SourceryWorkshops Wiki · GitHub](https://github.com/krzysztofzablocki/SourceryWorkshops/wiki)

Optionally, you can add content of your .cursorrules directly into template and then output generated file to .cursorrules so it has your rules and up to date index.


## Integrate with Cursor: Giving Your AI Superpowers

Cursor recently released a new feature which is going to significantly improve quality of the context that is provided to AI. And context is everything because quality of the output directly depends on the quality of the input.

Cursor enables AI configuration via global settings and project rules (.cursor/rules), supporting semantic descriptions and automatic attachment. Created through Cmd+Shift+P, rules feature glob matching and folder-specific settings for Cursor Chat, Ctrl/⌘ K, and code style preferences.

AI agent doesn't need to know about codebase structure all the time. Most of the time it actually works on changes for some specific feature, and only during some planning/architecture phase it probably needs to know about overall project structure. With this new feature agent can decide when to read our index file. Here is how it would looks like

```swift {open=true, lineNos=false, wrap=true, title="Cursor Configuration"}
---
description: Code index that lists all the types defined in the project.
globs: **/*.{swift,md}
---

enum AllTypes {
{% for type in types.all %}
case {{ type.name | lowercase }}
{% endfor %}
}
```

save this file in `Templates/code_index.stencil` and then define a `.sourcery.yml` with the following content:

```yaml {open=true, lineNos=false, wrap=true, title="Sourcery Configuration"}
sources:
- MyApp/Sources
- MyFramework/Sources
templates:
- Templates/code_index.stencil
output:
.cursor/rules/.full_code_index.mdc
```

## My Proven Codebase Index Template (Steal This)

Here is my index file swift template with some extra filtering to make it smaller:

{{< gist Saik0s a6f09e3f1cdeb6424ce343609a8fd581 >}}

Sourcery lets you define feature-level, domain-specific, and complex indexes. This means not only listing types, but actually personalizing it and giving your AI *exactly* the context it needs, *when* it needs it.

Run `sourcery --watch`. It's *very* handy for AI-assisted development.

Why This System Wins:

-   **Never Waste Hours Manually Documenting Types Again:** Sourcery Does It For You.
-   **Architectural Guardrails:** AI suggestions respect domain boundaries, improving overall design and reusability.
-   **Always-in-Sync Context:** Integrate with CI for continuous, up-to-date context.
-   **Prove ROI:** Track AI-assisted coding metrics to show concrete improvements.

---

P.S.
Developers are building tools for themselves like never before. The barrier to entry has basically vanished. We can whip up solutions that turbocharge our coding in minutes. Sure, we've always hacked together our own stuff - but now anyone can do it. Super exciting time.
