Name:		texlive-uwa-pif
Version:	64491
Release:	2
Summary:	A Participant Information Form (PIF) for a human research protocol at the University of Western Australia
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uwa-pif
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uwa-pif.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uwa-pif.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uwa-pif.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package generates a Participant Information Form (PIF) for
a human research protocol at the University of Western
Australia. It requires the UWA logo in PDF format, which is
available in SVG format at
https://static-listing.weboffice.uwa.edu.au/visualid/core-rebra
nd/img/uwacrest/, and uses the Calibri fonts by default. The
class works with XeLaTeX and LuaLaTeX. It depends on the
uwa-letterhead package.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/uwa-pif
%{_texmfdistdir}/tex/latex/uwa-pif
%doc %{_texmfdistdir}/doc/latex/uwa-pif

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
