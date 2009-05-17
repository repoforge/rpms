# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Pango

Summary: Layout and render international text
Name: perl-Pango
Version: 1.220
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Pango/

Source: http://www.cpan.org/authors/id/T/TS/TSCH/Pango-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

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
%doc AUTHORS ChangeLog LICENSE MANIFEST MANIFEST.SKIP META.yml NEWS README copyright.pod examples/
%doc %{_mandir}/man3/Pango.3pm*
%doc %{_mandir}/man3/Pango::*.3pm*
%{perl_vendorarch}/auto/Pango/
%{perl_vendorarch}/Pango/
%{perl_vendorarch}/Pango.pm

%changelog
* Sun May 10 2009 Unknown - 1.220-1
- Initial package. (using DAR)
