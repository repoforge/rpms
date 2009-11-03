# $Id$
# Authority: dag
# Upstream: Adam Trickett, E<lt>atrickett$cpan,orgE<gt>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Log-Trivial

Summary: Very simple tool for writing very simple log files
Name: perl-Log-Trivial
Version: 0.31
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Log-Trivial/

Source: http://www.cpan.org/modules/by-module/Log/Log-Trivial-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.6.1
BuildRequires: perl(Test::More)
Requires: perl >= 1:5.6.1

%description
Very simple tool for writing very simple log files.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README SIGNATURE examples/
%doc %{_mandir}/man3/Log::Trivial.3pm*
%dir %{perl_vendorlib}/Log/
#%{perl_vendorlib}/Log/Trivial/
%{perl_vendorlib}/Log/Trivial.pm

%changelog
* Sat May 10 2008 Dag Wieers <dag@wieers.com> - 0.31-1
- Initial package. (using DAR)
