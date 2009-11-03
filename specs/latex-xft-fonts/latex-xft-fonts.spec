# $Id$
#
# Authority: bert
# Upstream: <lyx-devel$lists,lyx,org>

Name: latex-xft-fonts
Version: 0.1
Release: 2%{?dist}
License: distributable
Source: http://movementarian.org/latex-xft-fonts-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Group: User Interface/X
Summary: xft-compatible versions of some LaTeX fonts
Prereq: fontconfig chkfontpath

%description
Latex-xft-fonts contains xft-compatible versions of
LaTeX fonts for use with visual math symbol display
in LyX. You will need to install this package if
your version of Qt is using Xft for displaying
fonts.

%prep
%setup -q

%install
%{__rm} -rf %{buildroot}

%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}


%post
fc-cache

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/chkfontpath -q -r %{_datadir}/fonts/latex-xft-fonts
fi
fc-cache

%files
%defattr(-, root, root, 0755)
%{_datadir}/fonts/latex-xft-fonts/*.ttf

%changelog
* Fri Jun 04 2004  Bert de Bruijn  <bert@debruijn.be>
- some minor fixes (macro's, other standards) for inclusion
  in rpm repositories.

* Fri Dec 20 2002  John Levon  <levon@movementarian.org>
- Initial version
