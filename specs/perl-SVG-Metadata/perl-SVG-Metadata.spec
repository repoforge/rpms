# $Id$
# Authority: dries
# Upstream: Bryce Harrington <bryce$osdl,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SVG-Metadata

Summary: Perl module to capture metadata info about an SVG file
Name: perl-SVG-Metadata
Version: 0.28
Release: 1.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVG-Metadata/

Source: http://www.cpan.org/modules/by-module/SVG/SVG-Metadata-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
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
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man1/svg_annotate.1*
%doc %{_mandir}/man1/svg_validate.1*
%doc %{_mandir}/man3/SVG::Metadata.3pm*
%{_bindir}/svg_annotate
%{_bindir}/svg_validate
%dir %{perl_vendorlib}/SVG/
%{perl_vendorlib}/SVG/Metadata.pm

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.28-1
- Updated to release 0.28.

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
