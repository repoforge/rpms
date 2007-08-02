# $Id$
# Authority: dries
# Upstream: Gisle Aas <gisle$ActiveState,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Font-AFM

Summary: Interface to Adobe Font Metrics files
Name: perl-Font-AFM
Version: 1.19
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Font-AFM/

Source: http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/Font-AFM-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This module implements the Font::AFM class. Objects of this
class are initialised from an AFM-file and allows you to obtain
information about the font and the metrics of the various glyphs
in the font.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Font/AFM.pm
%{perl_vendorlib}/Font/Metrics

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.19-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.19-1
- Initial package.
