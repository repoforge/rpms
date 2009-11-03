# $Id$
# Authority: dag
# Upstream: Adam Kennedy<cpan@ali.as>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name PPI-Tester

Summary: wxPerl-based interactive PPI debugger/tester
Name: perl-PPI-Tester
Version: 0.15
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PPI-Tester/

Source: http://www.cpan.org/modules/by-module/PPI/PPI-Tester-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl(File::Spec) >= 0.82
BuildRequires: perl(PPI) >= 0.840
BuildRequires: perl(Wx) >= 0.19
Requires: perl >= 0:5.005

%description
A wxPerl-based interactive PPI debugger/tester.

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
%doc %{_mandir}/man3/PPI::Tester.3pm*
%doc %{_mandir}/man1/ppitester.1.gz
#%doc %{_mandir}/man3/*.3pm*
%{_bindir}/ppitester
%dir %{perl_vendorlib}/PPI/
#%{perl_vendorlib}/PPI/Tester/
%{perl_vendorlib}/PPI/Tester.pm

%changelog
* Mon Jun 22 2009 Christoph Maser <cmr@financial.com> - 0.15-1
- Updated to version 0.15.

* Mon Aug 06 2007 Jim <quien-sabe@metaorg.com> - 0.06-2
- Added BuildRequires perl(PPI) perl(Wx)
- Fixed unpackagedfiles error for ppitester

* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.06-1
- Initial package. (using DAR)
