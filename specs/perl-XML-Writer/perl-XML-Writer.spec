# $Id$
# Authority: dries
# Upstream: Joseph Walton <joe$kafsemo,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Writer

Summary: Extension for writing XML documents
Name: perl-XML-Writer
Version: 0.600
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Writer/

Source: http://www.cpan.org/modules/by-module/XML/XML-Writer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module contains a perl extension for writing XML documents.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
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
%doc Changes README TODO
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/Writer.pm

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.600-1
- Updated to release 0.600.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.545-1
- Updated to release 0.545.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.530-1
- Updated to release 0.530.

* Mon Dec 20 2004 Dag Wieers <dag@wieers.com> - 0.520-1
- Updated to release 0.520.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.510-1
- Initial package.
