# $Id$
# Authority: dries

%define real_version 2002-12-08

Summary: PNG to icon converter
Name: png2ico
Version: 0.0.20021218
Release: 1.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.winterdrache.de/freeware/png2ico/index.html

Source: http://www.winterdrache.de/freeware/png2ico/data/png2ico-src-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, libpng-devel, zlib-devel

%description
Png2ico is a utility which converts PNG files to Windows icon resource files.

%prep
%setup -n png2ico

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 png2ico %{buildroot}%{_bindir}/png2ico
%{__install} -Dp -m0644 doc/png2ico.1 %{buildroot}%{_mandir}/man1/png2ico.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.20021218-1.2
- Rebuild for Fedora Core 5.

* Fri Jun 25 2004 Dries Verachtert <dries@ulyssis.org> - 0.0.20021218-1
- Initial package.
