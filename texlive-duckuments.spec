Name:		texlive-duckuments
Version:	52271
Release:	2
Summary:	Create duckified dummy content
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/duckuments
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/duckuments.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/duckuments.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/duckuments.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides facilities to create duckified dummy
contents. It was inspired by the question "Getting ducks in
example images" on TeX-LaTeX Stack Exchange. The following
macros are available: \duckument[key=val] - print a short
duckument \blindduck[key=val] - print a paragraph
\ducklist(*){environment} - create a list of type environment
\ducklistlist(*){environment} - create nested lists
\duckitemize - ducklist{itemize} \duckenumerate -
ducklist{enumerate} \duckdescription - ducklist{description}
\duckumentsCreateExampleFile \duckumentsDrawRandomDucks The
package works with pdfTeX, LuaTeX, and XeTeX.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/duckuments
%{_texmfdistdir}/tex/latex/duckuments
%doc %{_texmfdistdir}/doc/latex/duckuments

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
