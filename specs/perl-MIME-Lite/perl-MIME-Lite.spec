# $Id$

# Authority: dries

Summary: Simple standalone module for generating MIME messages.
Summary(nl): Een eenvoudige onafhankelijke module om MIME berichten te genereren.
Name: perl-MIME-Lite
Version: 2.117
Release: 2
License: GPL
Group: Applications/CPAN
URL: http://www.zeegee.com/code/perl/MIME-Lite/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.zeegee.com/code/perl/MIME-Lite/download/MIME-Lite-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
BuildRequires: perl
Requires: perl

%description
MIME-Lite is a simple standalone module for generating MIME messages.

%description -l nl
MIME-Lite is een eenvoudige onafhankelijke module om MIME berichten te
genereren.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup -n MIME-Lite-2.117

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor"
sed -i "s/DESTDIR =.*/DESTDIR=${RPM_BUILD_ROOT//\//\\/}\//g;" Makefile
%{__make} %{?_smp_mflags}

%install
export DESTDIR=$RPM_BUILD_ROOT
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist

%files
%defattr(-, root, root, 0755)
%doc COPYING INSTALLING README*
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Sun Dec 11 2004 Dries Verachtert <dries@ulyssis.org> 2.117-2
- cleanup of spec file

* Fri Dec 26 2003 Dries Verachtert <dries@ulyssis.org> 2.117-1
- first packaging for Fedora Core 1
