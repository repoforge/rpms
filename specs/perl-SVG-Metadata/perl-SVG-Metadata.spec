# $Id$

# Authority: dries
# Upstream: Bryce Harrington <bryce$osdl,org>

%define real_name SVG-Metadata
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Perl module to capture metadata info about an SVG file
Name: perl-SVG-Metadata
Version: 0.25
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVG-Metadata/

Source: http://www.cpan.org/modules/by-module/SVG/SVG-Metadata-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
Provides: perl(SVG::Metadata)

%description
See `man SVG::Metadata` after installation for more details about this
Perl module.

The script svg_validate is provided as an example.  It demonstrates an
example of using SVG::Metadata to extract SVG files that have valid
metadata into a separate directory structure for packaging.  See 
`man svg_validate` after installation for more details on it.

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
%doc ChangeLog README
%{_bindir}/*
%{perl_vendorlib}/SVG/Metadata.pm
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*

%changelog
* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.25-1
- Updated to release 0.25.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Updated to release 0.21.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Updated to release 0.20.

* Thu Dec 09 2004 Dries Verachtert <dries@ulyssis.org> - 0.11-2
- Fix: added provides.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Initial package.
