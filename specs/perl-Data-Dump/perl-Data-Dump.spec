# $Id$

# Authority: dries
# Upstream: Gisle Aas <gisle$ActiveState,com>


%define real_name Data-Dump
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Pretty print data
Name: perl-Data-Dump
Version: 1.08
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Dump/

Source: http://www.cpan.org/modules/by-module/Data/Data-Dump-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This package contain the Data::Dump module. It can be used for pretty
printing data.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/Data/Dump/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Data/Dump.pm

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Updated to release 1.08.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.06-1.2
- Rebuild for Fedora Core 5.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.06-1
- Updated to release 1.06.

* Sat Jun 15 2004 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Initial package.
