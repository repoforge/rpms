# $Id$
# Authority: dries
# Upstream: Pavel Hlavnicka <cpanuser$seznam,cz>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Sablotron

Summary: Encapsulation of the Sablotron XSLT processor
Name: perl-XML-Sablotron
Version: 1.01
Release: 1%{?dist}
License: MPL/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Sablotron/

Source: http://www.cpan.org/modules/by-module/XML/XML-Sablotron-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: sablotron-devel
BuildRequires: expat-devel >= 1.95.2

%description
XML::Sablotron is a simple Perl package, which encapsulates the C API
of Sablotron XSLT processor.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/XML/
%{perl_vendorarch}/XML/Sablotron/
%{perl_vendorarch}/XML/Sablotron.pm
%dir %{perl_vendorarch}/auto/XML/
%{perl_vendorarch}/auto/XML/Sablotron/

%changelog
* Wed Jul 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
