# $Id$
# Authority: dries
# Upstream: Ricardo Garcia Gonzalez <sarbalap$gmail,com>

### Requires python >= 2.5
# ExcludeDist: el3 el4 el5

%define real_version 2012.02.27

Summary: Download videos from YouTube.com
Name: youtube-dl
Version: 0
Release: 0.%{real_version}%{?dist}
License: GPL
Group: Applications/Internet
URL: http://rg3.github.com/youtube-dl/
Source0: http://raw.github.com/rg3/youtube-dl/%{real_version}/youtube-dl
Source1: youtube-dl.conf

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
Requires: python >= 2.5

%description
youtube-dl is a small command-line program for downloading videos from
YouTube.com.

%prep

%build

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir} %{buildroot}%{_sysconfdir}
%{__install} -p -m0755 %{SOURCE0} %{buildroot}%{_bindir}
%{__install} -p -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/youtube-dl
%config %{_sysconfdir}/youtube-dl.conf


%changelog
* Fri Aug 31 2012 Denis Fateyev <denis@fateyev.com> - 2012.2.27-1
- Updated to 2012.02.27

* Tue Dec 15 2009 Yury V. Zaytsev <yury@shurup.com> - 2009.09.13-2
- Fixed the changelog entry.

* Mon Sep 14 2009 Dries Verachtert <dries@ulyssis.org> - 2009.09.13-1
- Updated to release 2009.09.13.
- Source url now points to versioned tar ball from revision system =>
  a unique name for each version.

* Mon Jul 13 2009 Dries Verachtert <dries@ulyssis.org> - 2009.05.30-1
- Updated to release 2009.05.30.

* Sat May 23 2009 Dries Verachtert <dries@ulyssis.org> - 2009.05.23-1
- Updated to release 2009.05.23.

* Tue Apr  6 2009 Dries Verachtert <dries@ulyssis.org> - 2009.04.06-1
- Updated to release 2009.04.06.

* Mon Nov 24 2008 Dries Verachtert <dries@ulyssis.org> - 2008.11.01-1
- Updated to release 2008.11.01.

* Sat Oct 18 2008 Dries Verachtert <dries@ulyssis.org> - 2008.10.16-1
- Updated to release 2008.10.16.

* Sun Sep 21 2008 Dries Verachtert <dries@ulyssis.org> - 2008.09.20-1
- Updated to release 2008.09.20.

* Mon Aug  8 2008 Dries Verachtert <dries@ulyssis.org> - 2008.08.09-1
- Updated to release 2008.08.09.

* Mon Jul 28 2008 Dries Verachtert <dries@ulyssis.org> - 2008.07.26-1
- Updated to release 2008.07.26.

* Wed Jul 23 2008 Dries Verachtert <dries@ulyssis.org> - 2008.07.22-1
- Updated to release 2008.07.22.

* Mon Jun  9 2008 Dries Verachtert <dries@ulyssis.org> - 2008.06.08-1
- Updated to release 2008.06.08.

* Sun Apr 20 2008 Dries Verachtert <dries@ulyssis.org> - 2008.04.20-1
- Updated to release 2008.04.20.

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
