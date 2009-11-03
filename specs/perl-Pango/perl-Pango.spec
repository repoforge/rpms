# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Pango

Summary: Layout and render international text
Name: perl-Pango
Version: 1.221
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Pango/

Source: http://www.cpan.org/authors/id/T/TS/TSCH/Pango-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: pkgconfig
BuildRequires: pango-devel
# From yaml build_requires
BuildRequires: perl(ExtUtils::MakeMaker)
# From yaml requires
BuildRequires: perl(Cairo) >= 1.000
BuildRequires: perl(ExtUtils::Depends) >= 0.300
BuildRequires: perl(ExtUtils::PkgConfig)
BuildRequires: perl(Glib) >= 1.220


%description
Layout and render international text.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS LICENSE MANIFEST MANIFEST.SKIP META.yml NEWS README copyright.pod examples/
%doc %{_mandir}/man3/Pango.3pm*
%doc %{_mandir}/man3/Pango::*.3pm*
%{perl_vendorarch}/auto/Pango/
%{perl_vendorarch}/Pango/
%{perl_vendorarch}/Pango.pm

%changelog
* Tue Sep  8 2009 Christoph Maser <cmr@financial.com> - 1.221-1
- Updated to version 1.221.

* Sun May 10 2009 Unknown - 1.220-1
- Initial package. (using DAR)
