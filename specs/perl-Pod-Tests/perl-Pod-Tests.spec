# $Id$
# Authority: dag
# Upstream: Adam Kennedy <cpan$ali,as>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Pod-Tests

Summary: Perl module named Pod-Tests
Name: perl-Pod-Tests
Version: 0.18
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Pod-Tests/

Source: http://www.cpan.org/modules/by-module/Pod/Pod-Tests-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Pod-Tests is a Perl module.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

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
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.18-1
- Initial package. (using DAR)
