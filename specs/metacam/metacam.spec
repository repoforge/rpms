# $Id$

# Authority: dag

# Upstream: Daniel Stephens <daniel$cheeseplant,org>

Name: metacam
Version: 1.2
Release: 0
Summary: Utility to read Exif data from digital camera files
Group: Applications/Multimedia
License: GPL
URL: http://www.cheeseplant.org/~daniel/pages/metacam.html

Source: ftp://ftp.cheeseplant.org/pub/%{name}-%{version}.tar.gz
Source1: %{name}.1
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++

%description 
Metacam is an utility to read and decode metadata from digital camera
images with Exif information. It was specifically written to read images
from a Nikon D1, but it supports other cameras too.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man1/
%{__install} -m0755 %{name} %{buildroot}%{_bindir}
%{__install} -m0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README* THANKS
%doc %{_mandir}/man1/*
%{_bindir}/*

%changelog
* Tue Jan 04 2005 Bert de Bruijn <bert@debruijn.be> 1.2-0
- Update

* Sat Feb 01 2003 Bert de Bruijn <bert@debruijn.be> 1.1-0
- Initial package, manpage from Conectiva.
