# $Id$
# Authority: dag
# Upstream: Torsten Schönfeld <kaffeetisch$gmx,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Gnome2-PanelApplet

Summary: Perl interface to GNOME's applet library
Name: perl-Gnome2-PanelApplet
Version: 0.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gnome2-PanelApplet/

Source: http://www.cpan.org/modules/by-module/Gnome2/Gnome2-PanelApplet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Perl interface to GNOME's applet library.

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
%doc ChangeLog LICENSE MANIFEST MANIFEST.SKIP META.yml NEWS README copyright.pod examples/
%doc %{_mandir}/man3/Gnome2::PanelApplet.3pm*
%doc %{_mandir}/man3/Gnome2::PanelApplet::*.3pm*
%dir %{perl_vendorarch}/auto/Gnome2/
%{perl_vendorarch}/auto/Gnome2/PanelApplet/
%dir %{perl_vendorarch}/Gnome2/
%{perl_vendorarch}/Gnome2/PanelApplet.pm
%{perl_vendorarch}/Gnome2/PanelApplet/

%changelog
* Sat Jan 24 2009 Unknown - 0.02-1
- Initial package. (using DAR)
