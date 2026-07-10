%global tl_name duckuments
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5
Release:	%{tl_revision}.1
Summary:	Create duckified dummy content
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/duckuments
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/duckuments.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/duckuments.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/duckuments.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides facilities to create duckified dummy contents. It
was inspired by the question "Getting ducks in example images" on TeX-
LaTeX Stack Exchange. The following macros are available:
\duckument[key=val] - print a short duckument \blindduck[key=val] -
print a paragraph \ducklist(*){environment} - create a list of type
environment \ducklistlist(*){environment} - create nested lists
\duckitemize - ducklist{itemize} \duckenumerate - ducklist{enumerate}
\duckdescription - ducklist{description} \duckumentsCreateExampleFile
\duckumentsDrawRandomDucks The package works with pdfTeX, LuaTeX, and
XeTeX.

