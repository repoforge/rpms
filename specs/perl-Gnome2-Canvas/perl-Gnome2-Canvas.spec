# $Id$
# Authority: dag
# Upstream: Torsten Schönfeld <kaffeetisch$gmx,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Gnome2-Canvas

Summary: Perl interface to the 2.x series of the GNOME Canvas library
Name: perl-Gnome2-Canvas
Version: 1.002
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
#URL: http://search.cpan.org/dist/Gnome2-Canvas/
URL: http://gtk2-perl.sourceforge.net/

Source: http://www.cpan.org/modules/by-module/Gnome2/Gnome2-Canvas-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(ExtUtils::Depends)
BuildRequires: perl(ExtUtils::PkgConfig) >= 1.03
BuildRequires: perl(Glib) >= 1.040
BuildRequires: perl(Gtk2) >= 1.040
BuildRequires: perl(Cairo::Install::Files)
BuildRequires: libgnomeui-devel >= 2.0.0
Requires: perl >= 2:5.8.0

%description
Perl bindings to the 2.x series of the Gnome widget set.  This module allows
you to write graphical user interfaces in a perlish and object-oriented way,
freeing you from the casting and memory management in C, yet remaining very
close in spirit to original API.

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
%doc AUTHORS ChangeLog LICENSE MANIFEST MANIFEST.SKIP META.yml NEWS README TODO
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Gnome2/
%{perl_vendorarch}/Gnome2/Canvas/
%{perl_vendorarch}/Gnome2/Canvas.pm
%{perl_vendorarch}/Gnome2/Canvas.pod
%dir %{perl_vendorarch}/auto/Gnome2/
%{perl_vendorarch}/auto/Gnome2/Canvas/

%changelog
* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 1.002-2
- Cosmetic cleanup.

* Sat Jun 18 2005 Dries Verachtert <dries@ulyssis.org> - 1.002-1
- Update.

* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 1.00-1
- Initial package. (using DAR)
