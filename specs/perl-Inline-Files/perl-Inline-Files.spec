# $Id$
# Authority: dries
# Upstream: Damian Conway <damian$conway,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Inline-Files

Summary: Multiple virtual files at the end of your code
Name: perl-Inline-Files
Version: 0.63
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Inline-Files/

Source: http://www.cpan.org/modules/by-module/Inline/Inline-Files-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Inline::Files generalizes the notion of the __DATA__ marker and the
associated DATA filehandle, to an arbitrary number of markers and
associated filehandles.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Inline/Files.pm
%{perl_vendorlib}/Inline/Files

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.63-1
- Updated to version 0.63.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.62-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.62-1
- Initial package.
