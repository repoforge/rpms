# $Id$
# Authority: dag
# Upstream: Daisuke Murase <typester$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Array-Diff

Summary: Find the differences between two arrays
Name: perl-Array-Diff
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Array-Diff/

Source: http://www.cpan.org/modules/by-module/Array/Array-Diff-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)

%description
Find the differences between two arrays.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Array::Diff.3pm*
%dir %{perl_vendorlib}/Array/
#%{perl_vendorlib}/Array/Diff/
%{perl_vendorlib}/Array/Diff.pm

%changelog
* Tue Jun 08 2010 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
