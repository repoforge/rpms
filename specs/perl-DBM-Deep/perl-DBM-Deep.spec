# $Id$
# Authority: dag
# Upstream: Rob Kinyon <rob,kinyon$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBM-Deep

Summary: Pure perl multi-level hash/array DBM that supports transactions
Name: perl-DBM-Deep
Version: 1.0007
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBM-Deep/

Source: http://www.cpan.org/modules/by-module/DBM/DBM-Deep-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.006
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Path) >= 0.01
BuildRequires: perl(File::Temp) >= 0.01
BuildRequires: perl(IO::Scalar) >= 0.01
BuildRequires: perl(Test::Deep) >= 0.095
BuildRequires: perl(Test::Exception) >= 0.21
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl(Test::Warn) >= 0.08
Requires: perl >= 0:5.006

%description
DBM-Deep is a Perl module that implements a pure perl multi-level
hash/array DBM that supports transactions.

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
%doc %{_mandir}/man3/DBM::Deep.3pm*
%doc %{_mandir}/man3/DBM::Deep::*.3pm*
%dir %{perl_vendorlib}/DBM/
%{perl_vendorlib}/DBM/Deep/
%{perl_vendorlib}/DBM/Deep.pm
%{perl_vendorlib}/DBM/Deep.pod

%changelog
* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.0007-1
- Updated to release 1.0007.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 1.0006-1
- Updated to release 1.0006.

* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 1.0001-1
- Initial package. (using DAR)
