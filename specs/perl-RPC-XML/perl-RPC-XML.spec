# $Id$
# Authority: dries
# Upstream: Randy J Ray <rjray$blackperl,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name RPC-XML

Summary: Set of classes for core data, message and XML handling
Name: perl-RPC-XML
Version: 0.59
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/RPC-XML/

Source: http://www.cpan.org/modules/by-module/RPC/RPC-XML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
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
%{__perl} Makefile.PL \
	INSTALLDIRS="vendor" \
	PREFIX="%{buildroot}%{_prefix}"
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
%doc ChangeLog README*
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
%{_bindir}/make_method
%{perl_vendorlib}/Apache/RPC
%{perl_vendorlib}/RPC/XML.pm
%{perl_vendorlib}/RPC/XML/
%{perl_vendorlib}/auto/RPC/XML/

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.59-1
- Updated to release 0.59.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.58-1.2
- Rebuild for Fedora Core 5.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.58-1
- Updated to release 0.58.

* Sat Jan  1 2005 Dries Verachtert <dries@ulyssis.org> - 0.57-1
- Initial package.
