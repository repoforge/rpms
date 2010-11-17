# $Id$
# Authority: dries
# Upstream: Sean M. Burke <sburke$cpan,org>

### EL6 ships with perl-Pod-Escapes-1.04-115.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Pod-Escapes

Summary: Resolves Pod E sequences
Name: perl-Pod-Escapes
Version: 1.04
Release: 1.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Pod-Escapes/

Source: http://www.cpan.org/modules/by-module/Pod/Pod-Escapes-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

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
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Pod/Escapes.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.04-1.2
- Rebuild for Fedora Core 5.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Initial package.
