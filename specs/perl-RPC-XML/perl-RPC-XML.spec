# $Id$

# Authority: dries
# Upstream: Randy J Ray <rjray$blackperl,com>

%define real_name RPC-XML
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Set of classes for core data, message and XML handling
Name: perl-RPC-XML
Version: 0.57
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/RPC-XML/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJRAY/RPC-XML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl-libwww-perl
# Apparently i used the wrong name: XML-RPC doesn't exist, it's RPC-XML
Obsoletes: perl-XML-RPC

%description
The RPC::XML package is an implementation of XML-RPC. The module provides
classes for sample client and server implementations, a server designed as
an Apache location-handler, and a suite of data-manipulation classes that 
are used by them.

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
%doc README* ChangeLog
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
%{_bindir}/make_method
%{perl_vendorlib}/Apache/RPC
%{perl_vendorlib}/RPC/XML.pm
%{perl_vendorlib}/RPC/XML
%{perl_vendorlib}/auto/RPC/XML
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Sat Jan  1 2005 Dries Verachtert <dries@ulyssis.org> - 0.57-1
- Initial package.
