# $Id$
# Authority: dag
# Upstream: Tomas Doran <bobtfish@bobtfish.net>


%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MooseX-Getopt

Summary: Moose role for processing command line options
Name: perl-MooseX-Getopt
Version: 0.26
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MooseX-Getopt/

Source: http://search.cpan.org/CPAN/authors/id/B/BO/BOBTFISH/MooseX-Getopt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
#BuildRequires: perl(Getopt::Long) >= 2.37
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(Getopt::Long::Descriptive) >= 0.077
BuildRequires: perl(Moose) >= 0.56
BuildRequires: perl(Test::Exception) >= 0.21
BuildRequires: perl(Test::Moose)
#BuildRequires: perl(Test::More) >= 0.62
BuildRequires: perl(Test::More)
#Requires: perl(Getopt::Long) >= 2.37
Requires: perl(Getopt::Long)
Requires: perl(Getopt::Long::Descriptive) >= 0.077
Requires: perl(Moose) >= 0.56

%filter_from_requires /^perl*/d
%filter_setup


%description
A Moose role for processing command line options.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man3/MooseX::Getopt.3pm*
%doc %{_mandir}/man3/MooseX::Getopt::*.3pm*
%dir %{perl_vendorlib}/MooseX/
%{perl_vendorlib}/MooseX/Getopt/
%{perl_vendorlib}/MooseX/Getopt.pm

%changelog
* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 0.26-1
- Updated to version 0.26.

* Wed Jul 22 2009 Christoph Maser <cmr@financial.com> - 0.20-1
- Updated to version 0.20.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.12-1
- Updated to release 0.12.

* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Sat Jan 26 2008 Dag Wieers <dag@wieers.com> - 0.10-1
- Updated to release 0.10.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 0.08-1
- Updated to release 0.08.

* Wed Dec 05 2007 Dag Wieers <dag@wieers.com> - 0.07-1
- Updated to release 0.07.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.06-1
- Updated to release 0.06.

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
