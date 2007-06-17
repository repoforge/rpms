# $Id$
# Authority: dries
# Upstream: Martin Hosken <martin_hosken$sil,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-PDF

Summary: PDF Functions
Name: perl-Text-PDF
Version: 0.25
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-PDF/

Source: http://search.cpan.org/CPAN/authors/id/M/MH/MHOSKEN/Text-PDF-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
PDF functions for Perl.

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
%doc readme.txt
%doc %{_mandir}/man3/*
%{_bindir}/pdfbklt.plx
%{_bindir}/pdfrevert.plx
%{_bindir}/pdfstamp.plx
%{perl_vendorlib}/Text/PDF

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.25-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.25-1
- Initial package.
