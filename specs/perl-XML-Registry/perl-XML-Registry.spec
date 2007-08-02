# $Id$

# Authority: dries
# Upstream: Jonathan Eisenzopf <eisen$pobox,com>

%define real_name XML-Registry
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Perl module for loading and saving an XML registry
Name: perl-XML-Registry
Version: 0.02
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Registry/

Source: http://www.cpan.org/modules/by-module/XML/XML-Registry-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
The idea is to convert XML to Perl and back again using
a specific XML syntax; in this case, a kind of registry.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX=%{buildroot}%{_prefix}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/XML/Registry.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1.2
- Rebuild for Fedora Core 5.

* Sun Mar  6 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
