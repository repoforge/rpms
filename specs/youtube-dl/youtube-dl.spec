# $Id$
# Authority: dries
# Upstream: Ricardo Garcia Gonzalez <sarbalap$gmail,com>

Summary: Download videos from YouTube.com
Name: youtube-dl
Version: 0
Release: 0.2008.04.07
License: GPL
Group: Applications/Internet
URL: http://www.arrakis.es/~rggi3/youtube-dl/

Source: http://www.arrakis.es/~rggi3/youtube-dl/youtube-dl
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
Requires: python >= 2.4

%description
youtube-dl is a small command-line program for downloading videos from 
YouTube.com.

%prep
%setup -c -T

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -p -m0755 -D %{SOURCE0} %{buildroot}%{_bindir}/youtube-dl

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/youtube-dl

%changelog
* Sat Apr 12 2008 Dries Verachtert <dries@ulyssis.org> - 2008.04.07-1
- Updated to release 2008.04.07.

* Sun Jan 27 2008 Dries Verachtert <dries@ulyssis.org> - 2008.01.24-1
- Updated to release 2008.01.24.

* Tue Oct 16 2007 Dries Verachtert <dries@ulyssis.org> - 2007.10.12-1
- Updated to release 2007.10.12.

* Mon Sep  3 2007 Dries Verachtert <dries@ulyssis.org> - 2007.08.24-1
- Updated to release 2007.08.24.

* Fri Jun 29 2007 Dries Verachtert <dries@ulyssis.org> - 2007.06.22-1
- Updated to release 2007.06.22.

* Thu Jun 07 2007 Dries Verachtert <dries@ulyssis.org> - 2007.06.06-1
- Updated to release 2007.06.06.

* Wed Mar 28 2007 Dries Verachtert <dries@ulyssis.org> - 2007.03.27-1
- Updated to release 2007.03.27.

* Sat Feb 24 2007 Dries Verachtert <dries@ulyssis.org> - 2007.02.18-1
- Updated to release 2007.02.18.

* Tue Jan 23 2007 Dries Verachtert <dries@ulyssis.org> - 2007.01.19-1
- Updated to release 2007.01.19.

* Mon Jan 01 2007 Moritz Barsnick <moritz+rpm@barsnick.net> 2007.01.01-1
- Updated to release 2007.01.01
- Preserve mtime on install
- don't BR python
- require python >= 2.4 instead of just python (at least 2.3 required
    for optparse, 2.4 required for cookielib; the program indeed checks
    for >= 2.4 at runtime)

* Sat Dec 09 2006 Dries Verachtert <dries@ulyssis.org> - 2006.12.07-1
- Updated to release 2006.12.07.

* Sun Dec 03 2006 Dries Verachtert <dries@ulyssis.org> - 2006.12.03-1
- Updated to release 2006.12.03.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 2006.11.12-1
- Updated to release 2006.11.12.

* Tue Aug 15 2006 Dries Verachtert <dries@ulyssis.org> - 2006.08.15-1
- Updated to release 2006.08.15.

* Sun Aug 13 2006 Dries Verachtert <dries@ulyssis.org> - 2006.08.13-1
- Updated to release 2006.08.13.

* Fri Aug 11 2006 Dries Verachtert <dries@ulyssis.org> - 2006.08.11-1
- Initial package.
