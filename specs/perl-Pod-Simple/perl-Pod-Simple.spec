# $Id$
# Authority: dries
# Upstream: Sean M. Burke <sburke$cpan,org>

### EL6 ships with perl-Pod-Simple-3.13-115.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Pod-Simple

Summary: Framework for parsing Pod
Name: perl-Pod-Simple
Version: 3.16
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Pod-Simple/

Source: http://search.cpan.org/CPAN/authors/id/D/DW/DWHEELER/Pod-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Carp)
BuildRequires: perl(Config)
BuildRequires: perl(Cwd)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Pod::Escapes) >= 1.04
BuildRequires: perl(Symbol)
BuildRequires: perl(Test) >= 1.25
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Wrap) >= 98.112902
BuildRequires: perl(constant)
BuildRequires: perl(integer)
BuildRequires: perl(overload)
BuildRequires: perl(strict)
Requires: perl(Carp)
Requires: perl(Config)
Requires: perl(Cwd)
Requires: perl(File::Basename)
Requires: perl(File::Find)
Requires: perl(File::Spec)
Requires: perl(Pod::Escapes) >= 1.04
Requires: perl(Symbol)
Requires: perl(Test) >= 1.25
Requires: perl(Test::More)
Requires: perl(Text::Wrap) >= 98.112902
Requires: perl(constant)
Requires: perl(integer)
Requires: perl(overload)
Requires: perl(strict)

%filter_from_requires /^perl*/d
%filter_setup

%description
This module contains a framework for parsing Pod.

%prep
%setup -q -n %{real_name}-%{version}

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
* Tue Jun 21 2011 David Hrbáč <david@hrbac.cz> - 3.16-1
- new upstream release

* Mon Nov 15 2010 David Hrbáč <david@hrbac.cz> - 3.15-1
- new upstream release

* Thu Sep 23 2010 David Hrbáč <david@hrbac.cz> - 3.14-1
- new upstream release

* Tue Dec 22 2009 Christoph Maser <cmr@financial.com> - 3.13-1
- Updated to version 3.13.

* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 3.11-1
- Updated to version 3.11.

* Wed Jul 22 2009 Christoph Maser <cmr@financial.com> - 3.08-1
- Updated to version 3.08.

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
