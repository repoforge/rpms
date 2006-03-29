# $Id$

# Authority: dries
# Upstream: T.J. Mather <tjmather$maxmind,com>

%define real_name XML-UM
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Convert UTF-8 to any encoding supported by XML::Encoding
Name: perl-XML-UM
Version: 0.01
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-UM/

Source: http://www.cpan.org/modules/by-module/XML/XML-UM-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module provides methods to convert UTF-8 strings to any XML encoding that
XML::Encoding supports. It creates mapping routines from the .xml files that
can be found in the maps/ directory in the XML::Encoding distribution. Note
that the XML::Encoding distribution does install the .enc files in your perl
directory, but not the.xml files they were created from. That's why you have
to specify $ENCDIR as in the SYNOPSIS.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/XML/UM.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1.2
- Rebuild for Fedora Core 5.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
