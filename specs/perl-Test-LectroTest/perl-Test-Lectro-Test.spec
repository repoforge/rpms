# $Id$
# Authority: cmr
# Upstream: Tom Moertel (tom$moertel,com)

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-LectroTest

Summary: Easy, automatic, specification-based tests
Name: perl-Test-LectroTest
Version: 0.3600
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-LectroTest/

Source: http://www.cpan.org/modules/by-module/Test/Test-LectroTest-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(File::Temp)
BuildRequires: perl(Test::More)

%description
Easy, automatic, specification-based tests.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README SIGNATURE THANKS TODO
%doc %{_mandir}/man3/Test::LectroTest*.3pm*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/LectroTest/
%{perl_vendorlib}/Test/LectroTest.pm

%changelog
* Tue Jul 07 2009 Christoph Maser <cmr@fianncial.com> - 0.3600-1
- Initial package. (using DAR)
