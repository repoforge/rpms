# $Id$

# Authority: dries
# Upstream: Geoffrey Rommel <grommel$sears,com>

%define real_name Math-Round
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Perl extension for rounding numbers
Name: perl-Math-Round
Version: 0.05
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Round/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/G/GR/GROMMEL/Math-Round-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Math::Round is a Perl module.  It supplies functions to round numbers,
both positive and negative, in various ways.  This may seem like an
odd thing to write a whole module for, but rounding can sometimes be
a little tricky, so I thought some people might find this useful.

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
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Math/Round.pm
%{perl_vendorlib}/auto/Math/Round/autosplit.ix
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
