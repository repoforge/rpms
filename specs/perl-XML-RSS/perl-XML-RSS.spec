# $Id$
# Authority: dries
# Upstream: kellan elliott-mccrea <kellan$protest,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-RSS

Summary: Creates and updates RSS files
Name: perl-XML-RSS
Version: 1.22
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-RSS/

Source: http://www.cpan.org/modules/by-module/XML/XML-RSS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module was created to help those who need to manage
RDF Site Summary (RSS) files. It makes quick work of
creating, updating, and saving RSS files.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/RSS.pm

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.22-1
- Updated to release 1.22.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Updated to release 1.20.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Updated to release 1.10.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.05-1.2
- Rebuild for Fedora Core 5.

* Sun Dec 19 2004 Dries Verachtert <dries@ulyssis.org> - 1.05
- Initial package.
