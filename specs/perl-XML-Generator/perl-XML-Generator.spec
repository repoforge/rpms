# $Id$

# Authority: dries
# Upstream: Benjamin Holzman <bholzman$earthlink,net>

%define real_name XML-Generator
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Perl extension for generating XML
Name: perl-XML-Generator
Version: 0.99
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Generator/

Source: http://www.cpan.org/modules/by-module/XML/XML-Generator-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module allows you to generate XML documents.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX=%{buildroot}%{_prefix}
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
%{perl_vendorlib}/XML/Generator.pm
%{perl_vendorlib}/XML/Generator

%changelog
* Sun Mar  6 2005 Dries Verachtert <dries@ulyssis.org> - 0.99_02-1
- Initial package.
