# $Id$
# Authority: dries
# Upstream: Russ Allbery <rra$stanford,edu>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Gateway

Summary: Tools for gatewaying messages between news and mail
Name: perl-Gateway
Version: 0.42
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gateway/

Source: http://search.cpan.org/CPAN/authors/id/R/RR/RRA/Gateway-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Tools for gatewaying messages between news and mail.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/News/Gateway.p*
%{perl_vendorlib}/auto/News/Gateway

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.42-1
- Initial package.
