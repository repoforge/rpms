# $Id$
# Authority: dries
# Upstream: Johan Vromans <jvromans$squirrel,nl>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Filter

Summary: Base class for objects that can read and write text lines
Name: perl-Text-Filter
Version: 1.9
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Filter/

Source: http://www.cpan.org/modules/by-module/Text/Text-Filter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Text::Filter is a base class for modules that have in common that they
process text lines by reading from some source (usually a file),
manipulating the contents and writing something back to some
destination (usually some other file).

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
%doc CHANGES README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Text/Filter.pm
%{perl_vendorlib}/Text/Filter/

%changelog
* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.9-1
- Updated to release 1.9.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.7-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.7-1
- Initial package.
