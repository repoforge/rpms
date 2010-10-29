# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unix-PID

Summary: Perl module for getting PID info
Name: perl-Unix-PID
Version: 0.21
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unix-PID/

Source: http://search.cpan.org/CPAN/authors/id/D/DM/DMUEY/Unix-PID-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Fcntl)
BuildRequires: perl(List::Cycle)
BuildRequires: perl(Math::Fibonacci::Phi)
BuildRequires: perl(Time::HiRes)
Requires: perl(Fcntl)
Requires: perl(List::Cycle)
Requires: perl(Math::Fibonacci::Phi)
Requires: perl(Time::HiRes)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
perl-Unix-PID is a Perl module for getting PID info.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Unix::PID.3pm*
%dir %{perl_vendorlib}/Unix/
#%{perl_vendorlib}/Unix/PID/
%{perl_vendorlib}/Unix/PID.pm
%{perl_vendorlib}/Unix/PID.pod

%changelog
* Fri Oct 29 2010 Christoph Maser <cmaser@gmx.de> - 0.21-1
- Updated to version 0.21.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.0.15-1
- Updated to release 0.0.15.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.0.13-1
- Initial package. (using DAR)
