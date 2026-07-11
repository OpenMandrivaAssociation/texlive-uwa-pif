%global tl_name uwa-pif
%global tl_revision 78431

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.1
Release:	%{tl_revision}.1
Summary:	A Participant Information Form (PIF) for a human research protocol at the Uni...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/unicodetex/latex/uwa-pif
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uwa-pif.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uwa-pif.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uwa-pif.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package generates a Participant Information Form (PIF) for a human
research protocol at the University of Western Australia. It requires
the UWA logo in PDF format, which is available in SVG format at
https://static-listing.weboffice.uwa.edu.au/visualid/core-rebra
nd/img/uwacrest/, and uses the Calibri fonts by default. The class works
with XeLaTeX and LuaLaTeX. It depends on the uwa-letterhead package.

