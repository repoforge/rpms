# $Id: $

# Authority: dries
# Upstream:

%define real_name Data-DumpXML
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Dump data structures as XML
Name: perl-Data-DumpXML
Version: 1.06
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-DumpXML/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/Data-DumpXML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
Requires: perl-XML-Parser, perl-Array-RefElem

%description
Dump arbitrary perl data structures as XML and restore them.

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
%{_mandir}/man3/*
%{perl_vendorlib}/Data/DumpXML
%{perl_vendorlib}/Data/DumpXML.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/Data/DumpXML/.packlist

%changelog
* Sat Jun 15 2004 Dries Verachtert <dries@ulyssis.org> - 1.06-1
- Initial package.
