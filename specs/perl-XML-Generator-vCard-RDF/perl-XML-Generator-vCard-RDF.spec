# $Id$
# Authority: dries
# Upstream: Aaron Straup Cope <ascope$cpan,org>

%define real_name XML-Generator-vCard-RDF
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Generate RDF/XML SAX2 events for vCard 3.0
Name: perl-XML-Generator-vCard-RDF
Version: 1.3
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Generator-vCard-RDF/

Source: http://www.cpan.org/modules/by-module/XML/XML-Generator-vCard-RDF-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
BuildRequires: perl

%description
Generate RDF/XML SAX2 events for vCard 3.0.

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
%{perl_vendorlib}/XML/Generator/vCard/RDF.pm

%changelog
* Mon Dec 27 2004 Dries Verachtert <dries@ulyssis.org> - 1.3-1
- Initial package.
