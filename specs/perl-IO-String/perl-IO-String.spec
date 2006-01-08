# $Id$
# Authority: dries
# Upstream: Gisle Aas <gisle$ActiveState,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-String

Summary: Emulate file interface for in-core strings
Name: perl-IO-String
Version: 1.08
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-String/

Source: http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/IO-String-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

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
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/IO/String.pm

%changelog
* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Updated to release 1.08.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Updated to release 1.07.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.06-1
- Initial package.
