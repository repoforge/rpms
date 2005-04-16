# $Id$
# Authority: dries
# Upstream: Joshua Nathaniel Pritikin <jpritikin$pobox,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Event

Summary: Generic Perl Event Loop
Name: perl-Event
Version: 1.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Event/

Source: http://search.cpan.org/CPAN/authors/id/J/JP/JPRIT/Event-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This extension aims to provide an simple and optimized event loop for
a broad class of applications.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Event.p*
%{perl_vendorarch}/Event
%{perl_vendorarch}/auto/Event

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Initial package.
