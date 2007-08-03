# $Id: perl-IP-Country.spec 171 2004-03-28 01:43:07Z dag $
# Authority: dag

%define perl_vendorlib  %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch  %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name SVG

Summary: Perl extension for generating Scalable Vector Graphics (SVG) documents
Name: perl-SVG
Version: 2.33
Release: 1.2
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVG/

Source: http://www.cpan.org/modules/by-module/SVG/SVG-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503, perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
Perl extension for generating Scalable Vector Graphics (SVG) documents.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot (noarch)
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

### Clean up buildroot (arch)
%{__rm} -rf %{buildroot}%{perl_archlib} \
                %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README examples/
%doc %{_mandir}/man?/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.33-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.33-1
- Updated to release 2.33.

* Tue Apr 13 2004 Dag Wieers <dag@wieers.com> - 2.28-1
- Initial package. (using DAR)
