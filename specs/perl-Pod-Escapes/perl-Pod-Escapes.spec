# $Id$

# Authority: dries
# Upstream: Sean M. Burke <sburke$cpan,org>

%define real_name Pod-Escapes
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Resolves Pod E sequences
Name: perl-Pod-Escapes
Version: 1.04
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Pod-Escapes/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/S/SB/SBURKE/Pod-Escapes-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This module provides things that are useful in decoding Pod E...
sequences. Presumably, it should be used only by Pod parsers and/or
formatters.

By default, Pod::Escapes exports none of its symbols. But you can request
any of them to be exported. Either request them individually, as with `use
Pod::Escapes qw(symbolname symbolname2...);', or you can do `use
Pod::Escapes qw(:ALL);' to get all exportable symbols.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README ChangeLog
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Pod/Escapes.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Initial package.
