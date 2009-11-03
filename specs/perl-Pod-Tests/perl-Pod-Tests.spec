# $Id$
# Authority: dag
# Upstream: Adam Kennedy <cpan$ali,as>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Pod-Tests

Summary: Perl module named Pod-Tests
Name: perl-Pod-Tests
Version: 1.19
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Pod-Tests/

Source: http://www.cpan.org/modules/by-module/Pod/Pod-Tests-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Pod-Tests is a Perl module.

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
%doc %{_mandir}/man1/pod2test.1*
%doc %{_mandir}/man3/Pod::Tests.3pm*
%{_bindir}/pod2test
%dir %{perl_vendorlib}/Pod/
%{perl_vendorlib}/Pod/Tests.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.19-1
- Updated to version 1.19.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.18-1
- Initial package. (using DAR)
