# $Id$

# Authority: dries
# Upstream: Andy Wardley <cpan$wardley,org>

%define real_name Template-Toolkit
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Template processing system
Name: perl-Template-Toolkit
Version: 2.14
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Template-Toolkit/

Source: http://www.cpan.org/modules/by-module/Template/Template-Toolkit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl-AppConfig

%description
The Template Toolkit is a collection of modules which implement a
fast, flexible, powerful and extensible template processing system.
It was originally designed and remains primarily useful for generating
dynamic web content, but it can be used equally well for processing
any other kind of text based documents: HTML, XML, POD, PostScript,
LaTeX, and so on.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL TT_DBI=n TT_XS_ENABLE=y TT_ACCEPT=y INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags} \
	TT_PREFIX=/usr/share/tt2

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	DESTDIR=%{buildroot} \
	TT_PREFIX=%{buildroot}/usr/share/tt2
#	PREFIX=%{buildroot}/usr \
#	PERLPREFIX=%{buildroot}/usr \
#	SITEPREFIX=%{buildroot}/usr \
#	VENDORPREFIX=%{buildroot}/usr \

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
%{perl_vendorarch}/Template.pm
%{perl_vendorarch}/Template
%{perl_vendorarch}/auto/Template
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/.packlist
%{_datadir}/tt2
%{_bindir}/tpage
%{_bindir}/ttree

%changelog
* Thu Nov 04 2004 Dries Verachtert <dries@ulyssis.org> - 2.14-1
- Initial package.
