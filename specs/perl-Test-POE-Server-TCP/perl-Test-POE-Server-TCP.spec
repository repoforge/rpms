# $Id$
# Authority: cmr
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-POE-Server-TCP

Summary: A POE Component providing TCP server services for test cases
Name: perl-Test-POE-Server-TCP
Version: 1.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-POE-Server-TCP/

Source: http://www.cpan.org/modules/by-module/Test/Test-POE-Server-TCP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
# From yaml build_requires
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) => 0.47
BuildRequires: perl(Text::ParseWords)
# From yaml requires
BuildRequires: perl(POE) >= 1.004
BuildRequires: perl(POE::Filter)
BuildRequires: perl(POE::Filter::Line)
BuildRequires: perl(POE::Wheel::ReadWrite)
BuildRequires: perl(POE::Wheel::SocketFactory)
BuildRequires: perl >= 5.6.0
Requires: perl >= 0:5.6.0

%description
A POE Component providing TCP server services for test cases.

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
%doc %{_mandir}/man3/Test::POE::Server::TCP.3pm*
%dir %{perl_vendorlib}/Test/
%dir %{perl_vendorlib}/Test/POE/
%dir %{perl_vendorlib}/Test/POE/Server/
#%{perl_vendorlib}/Test/POE/Server/TCP/
%{perl_vendorlib}/Test/POE/Server/TCP.pm

%changelog
* Wed Aug 05 2009 Christoph Maser <cmr@financial.com> - 1.08-1
- Initial package. (using DAR)
