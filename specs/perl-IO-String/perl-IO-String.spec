# $Id$
# Authority: dries
# Upstream: Gisle Aas <gisle$ActiveState,com>

### EL6 ships with perl-IO-String-1.08-9.el6
%{?el6:# Tag: rfx}
### EL5 ships with perl-IO-String-1.08-1.1.1
%{?el5:# Tag: rfx}
### EL4 ships with perl-IO-String-1.08-1.1.el4
%{?el4:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-String

Summary: Emulate file interface for in-core strings
Name: perl-IO-String
Version: 1.08
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-String/

Source: http://www.cpan.org/modules/by-module/IO/IO-String-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
IO::String is an IO::File (and IO::Handle) compatible class that read
or write data from in-core strings.  It is really just a
simplification of what I needed from Eryq's IO-stringy modules.  As
such IO::String is a replacement for IO::Scalar.

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
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/IO/
%{perl_vendorlib}/IO/String.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.08-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Updated to release 1.08.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Updated to release 1.07.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.06-1
- Initial package.
