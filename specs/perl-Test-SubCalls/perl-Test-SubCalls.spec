# $Id$
# Authority: dag
# Upstream: Adam Kennedy <cpan@ali.as>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-SubCalls

Summary: Track the number of times subs are called
Name: perl-Test-SubCalls
Version: 1.06
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-SubCalls/

Source: http://www.cpan.org/modules/by-module/Test/Test-SubCalls-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0 
BuildRequires: perl(Test::Builder::Tester) >= 1.01

%description
Track the number of times subs are called.

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
%doc %{_mandir}/man3/Test::SubCalls.3pm*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/SubCalls.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.06-1
- Initial package. (using DAR)
