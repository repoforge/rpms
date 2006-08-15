# $Id$
# Authority: dries
# Upstream: 

Summary: Download videos from YouTube.com
Name: youtube-dl
Version: 0
Release: 0.2006.08.15.1
License: GPL
Group: Applications/Internet
URL: http://www.arrakis.es/~rggi3/youtube-dl/

Source: http://www.arrakis.es/~rggi3/youtube-dl/youtube-dl
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
BuildRequires: python
Requires: python

%description
youtube-dl is a small command-line program for downloading videos from 
YouTube.com.

%prep
%setup -c -T

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -m0755 -D %{SOURCE0} %{buildroot}%{_bindir}/youtube-dl

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/youtube-dl

%changelog
* Tue Aug 15 2006 Dries Verachtert <dries@ulyssis.org> - 2006.08.15-1
- Updated to release 2006.08.15.

* Sun Aug 13 2006 Dries Verachtert <dries@ulyssis.org> - 2006.08.13-1
- Updated to release 2006.08.13.

* Fri Aug 11 2006 Dries Verachtert <dries@ulyssis.org> - 2006.08.11-1
- Initial package.
