# $Id$
# Authority: dries
# Upstream: Ryan Eatmon <reatmon$mail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Stream

Summary: XML Stream connection support
Name: perl-XML-Stream
Version: 1.22
Release: 1.2%{?dist}
License: LGPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Stream/

Source: http://www.cpan.org/modules/by-module/XML/XML-Stream-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module contains support for XML stream connections.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES INFO LICENSE.LGPL README
%{_mandir}/man3/*
%{perl_vendorlib}/XML/Stream.pm
%{perl_vendorlib}/XML/Stream/*

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.22-1.2
- Rebuild for Fedora Core 5.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.22-1
- Updated to release 1.22.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 1.21-1
- Initial package.
