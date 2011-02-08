# $Id$
# Authority: dries
# Upstream: Slaven Rezi# <slaven$rezic,de>


%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

%{?rh9:%define _without_tcltk_devel 1}
%{?rh8:%define _without_tcltk_devel 1}
%{?rh7:%define _without_tcltk_devel 1}
%{?el2:%define _without_tcltk_devel 1}
%{?rh6:%define _without_tcltk_devel 1}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tk

Summary: Object Oriented Tk extension for Perl
Name: perl-Tk
Version: 804.029
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tk/

Source: http://search.cpan.org/CPAN/authors/id/S/SR/SREZIC/Tk-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 1:5.7.0
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: perl(Encode)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
%{!?_without_modxorg:BuildRequires: libX11-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_tcltk_devel:BuildRequires: tk-devel}
%{?_without_tcltk_devel:BuildRequires: tk}
Requires: perl >= 1:5.7.0
Requires: perl(Encode)
Requires: perl(Test::More)
Provides: perl(Tk::LabRadio)
Provides: perl(Tk::TextReindex)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module contains an object oriented Tk extension for Perl.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" \
    XFT="1" X11LIB="%{_prefix}/X11R6/%{_lib}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

%{__perl} -pi -e 's|/bin/perl|%{_bindir}/perl|g' %{buildroot}%{perl_vendorarch}/Tk/reindex.pl
%{__perl} -pi -e 's|/usr/local/bin/perl|%{_bindir}/perl|g' \
    %{buildroot}%{perl_vendorarch}/Tk/demos/widtrib/plop.pl \
    %{buildroot}%{perl_vendorarch}/Tk/demos/widtrib/npuz.pl \
    %{buildroot}%{perl_vendorarch}/Tk/pTk/mkVFunc \
    %{buildroot}%{perl_vendorarch}/Tk/pTk/Tcl-pTk \
    %{buildroot}%{perl_vendorarch}/Tk/Text.pod

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Changes INSTALL MANIFEST README* ToDo VERSIONS
%doc %{_mandir}/man1/ptked.1*
%doc %{_mandir}/man1/ptksh.1*
%doc %{_mandir}/man1/tkjpeg.1*
%doc %{_mandir}/man1/widget.1*
%doc %{_mandir}/man3/Tie::Watch.3pm*
%doc %{_mandir}/man3/Tk.3pm*
%doc %{_mandir}/man3/Tk::*.3pm*
%{_bindir}/gedi
%{_bindir}/ptked
%{_bindir}/ptksh
%{_bindir}/tkjpeg
%{_bindir}/widget
%{perl_vendorarch}/Tie/Watch.pm
%{perl_vendorarch}/Tk.pm
%{perl_vendorarch}/Tk.pod
%{perl_vendorarch}/Tk/
%{perl_vendorarch}/auto/Tk/
%{perl_vendorarch}/fix_4_os2.pl

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 804.029-1
- Updated to version 804.029.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 804.028-2
- Got rid of wrong /usr/local/bin/nperl dependency.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 804.028-1
- Updated to release 804.028.

* Sun Aug 14 2005 Dries Verachtert <dries@ulyssis.org> - 804.027-3
- Enable XFT support (thanks to Void Main).

* Sun Aug 14 2005 Dries Verachtert <dries@ulyssis.org> - 804.027-2
- Fix for x86_64.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 804.027-1
- Initial package.
