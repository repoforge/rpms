# $Id$

# Authority: dries
# Upstream: kellan elliott-mccrea <kellan$protest,net>

%define real_name XML-RSS
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Creates and updates RSS files
Name: perl-XML-RSS
Version: 1.05
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-RSS/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/K/KE/KELLAN/XML-RSS-%{version}.tar.gz
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
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/XML/RSS.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Sun Dec 19 2004 Dries Verachtert <dries@ulyssis.org> - 1.05
- Initial package.
