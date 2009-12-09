# $Id$
# Authority: cmr
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-POE-Client-TCP

Summary: A POE Component providing TCP client services for test cases
Name: perl-Test-POE-Client-TCP
Version: 1.06
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-POE-Client-TCP/

Source: http://www.cpan.org/modules/by-module/Test/Test-POE-Client-TCP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(POE) >= 1.28
BuildRequires: perl(POE::Filter)
BuildRequires: perl(POE::Filter::Line)
BuildRequires: perl(POE::Wheel::ReadWrite)
BuildRequires: perl(POE::Wheel::SocketFactory)
#BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::ParseWords)
BuildRequires: perl >= 5.6.0
Requires: perl(POE) >= 1.28
Requires: perl(POE::Filter)
Requires: perl(POE::Filter::Line)
Requires: perl(POE::Wheel::ReadWrite)
Requires: perl(POE::Wheel::SocketFactory)
Requires: perl >= 5.6.0

%filter_from_requires /^perl*/d
%filter_setup



%description
A POE Component providing TCP client services for test cases.

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
%doc Changes LICENSE MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Test::POE::Client::TCP.3pm*
%dir %{perl_vendorlib}/Test/
%dir %{perl_vendorlib}/Test/POE/
%dir %{perl_vendorlib}/Test/POE/Client/
#%{perl_vendorlib}/Test/POE/Client/TCP/
%{perl_vendorlib}/Test/POE/Client/TCP.pm

%changelog
* Wed Dec  9 2009 Christoph Maser <cmr@financial.com> - 1.06-1
- Updated to version 1.06.

* Mon Sep 07 2009 Christoph Maser <cmr@financial.com> - 1.04-1
- Initial package. (using DAR)
