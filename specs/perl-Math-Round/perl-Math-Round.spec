# $Id$
# Authority: dries
# Upstream: Geoffrey Rommel <grommel$sears,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Round

Summary: Perl extension for rounding numbers
Name: perl-Math-Round
Version: 0.06
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Round/

Source: http://www.cpan.org/modules/by-module/Math/Math-Round-%{version}.tar.gz
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
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Math/
%{perl_vendorlib}/Math/Round.pm
%dir %{perl_vendorlib}/auto/Math/
%{perl_vendorlib}/auto/Math/Round/

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Updated to release 0.06.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.05-1.2
- Rebuild for Fedora Core 5.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
