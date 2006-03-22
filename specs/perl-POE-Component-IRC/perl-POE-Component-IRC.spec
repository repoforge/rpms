# $Id$
# Authority: dries
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-IRC

Summary: POE component for IRC
Name: perl-POE-Component-IRC
Version: 4.77
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-IRC/

Source: http://search.cpan.org/CPAN/authors/id/B/BI/BINGOS/POE-Component-IRC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
POE::Component::IRC is a POE (Perl Object Environment) component
which provides a convenient way for POE applications to create a tiny
IRC client session and send and receive IRC events through it. If that
first sentence was a bit too much, go read the POE documentation over
and over until it makes some sense.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/POE/Component/IRC.pm
%{perl_vendorlib}/POE/Component/IRC/
%{perl_vendorlib}/POE/Filter/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 4.77-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 4.77-1
- Updated to release 4.77.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 4.75-1
- Initial package.
