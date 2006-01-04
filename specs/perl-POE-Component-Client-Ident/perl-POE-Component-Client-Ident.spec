# $Id$
# Authority: dries
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Client-Ident

Summary: Non-blocking Ident
Name: perl-POE-Component-Client-Ident
Version: 0.8
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Client-Ident/

Source: http://search.cpan.org/CPAN/authors/id/B/BI/BINGOS/POE-Component-Client-Ident-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
POE::Component::Client::Ident is a POE (Perl Object Environment) component which
provides a convenient way for POE applications to perform non-blocking Ident (auth/tap)
protocol remote username lookups.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/POE/Component/Client/Ident.pm
%{perl_vendorlib}/POE/Component/Client/Ident/
%{perl_vendorlib}/POE/Filter/Ident.pm

%changelog
* Thu Dec 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Initial package.
