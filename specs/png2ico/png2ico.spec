# $Id: $

# Authority: dries

%define real_version 2002-12-08

Summary: PNG to icon converter
Name: png2ico
Version: 20021218
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.winterdrache.de/freeware/png2ico/index.html

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.winterdrache.de/freeware/png2ico/data/png2ico-src-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# BuildRequires: 

%description
Png2ico is an utility which converts PNG files to Windows icon resource
files.

%prep
%setup -n png2ico

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m 0755 %{buildroot}%{_bindir} \
	%{buildroot}%{_mandir}/man1
%{__install} -m 0755 png2ico %{buildroot}%{_bindir}
%{__install} -m 0644 doc/png2ico.1 %{buildroot}%{_mandir}/man1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Fri Jun 25 2004 Dries Verachtert <dries@ulyssis.org> - 20021218-1
- Initial package.
