# $Id$
# Authority: dries
# Upstream: Slaven Rezi&#263; <slaven$rezic,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tk-FontDialog

Summary: Font dialog widget for perl/Tk
Name: perl-Tk-FontDialog
Version: 0.13
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tk-FontDialog/

Source: http://search.cpan.org/CPAN/authors/id/S/SR/SREZIC/Tk-FontDialog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Tk::FontDialog is a font chooser for perl/Tk.

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
%{perl_vendorlib}/Tk/FontDialog.pm

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.13-1
- Updated to release 0.13.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Updated to release 0.12.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.11-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Updated to release 0.11.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Initial package.
