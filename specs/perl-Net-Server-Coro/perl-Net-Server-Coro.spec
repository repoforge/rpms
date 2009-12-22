# $Id$
# Authority: cmr
# Upstream: Alex Vandiver <alexmv$bestpractical,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Server-Coro

Summary: A co-operative multithreaded server using Coro
Name: perl-Net-Server-Coro
Version: 0.7
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Server-Coro/

Source: http://search.cpan.org/CPAN/authors/id/A/AL/ALEXMV/Net-Server-Coro-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Coro)
BuildRequires: perl(EV)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Net::SSLeay)
BuildRequires: perl(Net::Server)
Requires: perl(Coro)
Requires: perl(EV)
Requires: perl(Net::SSLeay)
Requires: perl(Net::Server)

%filter_from_requires /^perl*/d
%filter_setup

%description
A co-operative multithreaded server using Coro.

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
%doc MANIFEST META.yml SIGNATURE
%doc %{_mandir}/man3/Net::Server::Coro.3pm*
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/Server/
%{perl_vendorlib}/Net/Server/Proto/Coro.pm
%{perl_vendorlib}/Net/Server/Coro.pm

%changelog
* Tue Dec 22 2009 Christoph Maser <cmr@financial.com> - 0.7-1
- Updated to version 0.7.

* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 0.6-1
- Updated to version 0.6.

* Wed Jul 22 2009 Christoph Maser <cmr@financial.com> - 0.4-1
- Initial package. (using DAR)
