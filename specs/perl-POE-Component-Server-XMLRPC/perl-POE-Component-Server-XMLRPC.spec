# $Id$
# Authority: dag
# Upstream: Mark A. Hershberger <mah$everybody,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Server-XMLRPC

Summary: Perl module to publish POE event handlers via XMLRPC over HTTP
Name: perl-POE-Component-Server-XMLRPC
Version: 0.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Server-XMLRPC/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-Server-XMLRPC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-POE-Component-Server-XMLRPC is a Perl module to publish POE event handlers
via XMLRPC over HTTP.

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
%doc CHANGES MANIFEST README
%doc %{_mandir}/man3/POE::Component::Server::XMLRPC.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%dir %{perl_vendorlib}/POE/Component/Server/
%{perl_vendorlib}/POE/Component/Server/XMLRPC.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
