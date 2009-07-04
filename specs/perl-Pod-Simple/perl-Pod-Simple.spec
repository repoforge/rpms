# $Id$
# Authority: dries
# Upstream: Sean M. Burke <sburke$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Pod-Simple

Summary: Framework for parsing Pod
Name: perl-Pod-Simple
Version: 3.07
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Pod-Simple/

Source: http://www.cpan.org/modules/by-module/Pod/Pod-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module contains a framework for parsing Pod.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_vendorlib}/perlpod*.pod
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Pod/Simple.*
%{perl_vendorlib}/Pod/Simple/*

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 3.07-1
- Updated to version 3.07.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 3.05-1
- Updated to release 3.05.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 3.04-1
- Updated to release 3.04.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 3.03-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 3.03-1
- Updated to release 3.03.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 3.02-1
- Initial package.
