# $Id$

# Authority: dries
# Upstream: Matt Sergeant <matt$sergeant,org>

%define real_name XML-LibXSLT
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Interface to the gnome libxslt library
Name: perl-XML-LibXSLT
Version: 1.57
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-LibXSLT/

Source: http://www.cpan.org/modules/by-module/XML/XML-LibXSLT-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl-XML-LibXML, libxslt-devel

%description
This module is a fast XSLT library, based on the Gnome libxslt engine
that you can find at http://www.xmlsoft.org/XSLT/

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX=%{buildroot}%{_prefix}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod \
	%{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/XML/LibXSLT.pm
%{perl_vendorarch}/XML/benchmark.pl
%{perl_vendorarch}/auto/XML/LibXSLT/LibXSLT.*

%changelog
* Sun Mar  6 2005 Dries Verachtert <dries@ulyssis.org> - 1.57-1
- Initial package.
